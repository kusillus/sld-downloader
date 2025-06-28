from pathlib import Path
import re, os, sys, requests
from bs4 import BeautifulSoup

URL = "https://scryfall.com/sets/sld"
OUTDIR = Path("output")

def sanitize(name):
    return re.sub(r'[\\/:"*?<>|]+', '', name).strip()

def main():
    print(f"[+] Descargando HTML de {URL}")
    r = requests.get(URL); r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    headers = soup.find_all("h2")
    if not headers:
        print("⚠️  No encontré ningún <h2>"); sys.exit(1)
    print(f"[+] Secciones encontradas: {len(headers)}")

    for i, h2 in enumerate(headers, 1):
        title = sanitize(h2.get_text())
        container = h2.find_next_sibling()
        # Buscar todas las imágenes sin filtro de clase específica
        imgs = container.find_all("img") if container else []
        print(f"  • [{i}] {title}: {len(imgs)} imágenes")

        if not imgs:
            continue
        section_dir = OUTDIR / title
        section_dir.mkdir(parents=True, exist_ok=True)

        for img in imgs:
            src = img.get("src") or img.get("data-src")
            if not src:
                continue
            if src.startswith("//"):
                src = "https:" + src
            
            # Filtrar solo imágenes de cartas de Scryfall
            if "scryfall.io" not in src:
                continue

            name = sanitize(img.get("alt", "card"))
            ext = os.path.splitext(src)[1].split("?")[0].lower()
            if ext not in (".jpg", ".jpeg", ".png", ".webp"):
                ext = ".jpg"
            dest = section_dir / f"{name}{ext}"
            if dest.exists():
                continue

            resp = requests.get(src, stream=True); resp.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(1024):
                    f.write(chunk)
            print(f"     – descargada → {dest}")

    print("[✓] ¡Listo!")

if __name__ == "__main__":
    main()
