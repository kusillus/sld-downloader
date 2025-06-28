# SLD Downloader

Un script de Python para descargar automáticamente todas las imágenes de cartas de Magic: The Gathering de la colección Secret Lair Drop desde Scryfall.

## 📋 Descripción

Este proyecto descarga todas las imágenes de cartas de la página de [Secret Lair Drop en Scryfall](https://scryfall.com/sets/sld), organizándolas automáticamente en carpetas según las diferentes secciones/ediciones encontradas en la página.

### Características

- **Descarga automática**: Obtiene todas las imágenes de cartas de SLD disponibles en Scryfall
- **Organización automática**: Crea carpetas separadas para cada sección/edición
- **Nombres sanitizados**: Los archivos y carpetas tienen nombres válidos para el sistema de archivos
- **Filtrado inteligente**: Solo descarga imágenes de Scryfall, evitando otros contenidos
- **Prevención de duplicados**: No descarga archivos que ya existen
- **Soporte para Docker**: Incluye configuración para ejecutar en contenedores

## 🛠️ Requisitos

### Ejecución local
- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Ejecución con Docker
- Docker
- Docker Compose (opcional)

## 📦 Instalación

### Método 1: Ejecución local

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd sld-downloader
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Método 2: Docker

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd sld-downloader
```

2. Las imágenes se construirán automáticamente al ejecutar.

## 🚀 Uso

### Ejecución local

```bash
python download_images.py
```

### Ejecución con Docker

#### Usando Docker directamente:
```bash
# Construir la imagen
docker build -t sld-downloader .

# Ejecutar el contenedor
docker run -v $(pwd)/output:/app/output sld-downloader
```

#### Usando Docker Compose:
```bash
docker-compose up --build
```

## 📁 Estructura de salida

El script crea la siguiente estructura de archivos:

```
output/
├── Sección 1/
│   ├── carta1.jpg
│   ├── carta2.png
│   └── ...
├── Sección 2/
│   ├── carta1.jpg
│   └── ...
└── ...
```

Cada sección corresponde a una edición o drop específico de Secret Lair, y los archivos se nombran según el texto alternativo de las imágenes en la página web.

## 🔧 Funcionamiento técnico

1. **Descarga HTML**: Obtiene el contenido de la página de SLD en Scryfall
2. **Análisis de estructura**: Busca todas las secciones marcadas con etiquetas `<h2>`
3. **Extracción de imágenes**: Para cada sección, encuentra todas las imágenes asociadas
4. **Filtrado**: Solo procesa imágenes alojadas en `scryfall.io`
5. **Sanitización**: Limpia nombres de archivos y carpetas para compatibilidad del sistema
6. **Descarga**: Guarda las imágenes en carpetas organizadas por sección

## 📋 Dependencias

- **requests**: Para realizar peticiones HTTP
- **beautifulsoup4**: Para parsear y analizar el HTML
- **pathlib**: Para manejo de rutas (incluido en Python estándar)

## ⚠️ Consideraciones

- Las imágenes se descargan en su resolución original desde Scryfall
- El script respeta la estructura existente y no sobrescribe archivos duplicados
- La velocidad de descarga depende de la conexión a internet y la respuesta del servidor
- Se recomienda usar con moderación para no sobrecargar los servidores de Scryfall

## 🐛 Resolución de problemas

### Error de conexión
Si encuentras errores de conexión, verifica:
- Tu conexión a internet
- Que Scryfall esté disponible
- Que no haya restricciones de firewall

### Archivos no descargados
Si algunas imágenes no se descargan:
- Verifica que las URLs sean válidas
- Comprueba que tengas permisos de escritura en la carpeta `output`
- Revisa que haya espacio suficiente en disco

### Problemas con Docker
- Asegúrate de que Docker esté ejecutándose
- Verifica que tengas permisos para ejecutar contenedores
- Comprueba que el puerto no esté en uso por otra aplicación

## 📄 Licencia

Este proyecto es para uso educativo y personal. Respeta los términos de servicio de Scryfall y los derechos de autor de Wizards of the Coast.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request