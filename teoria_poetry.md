## Teoría de Poetry (gestor de dependencias y empaquetado para Python)

### ¿Qué es Poetry?

Poetry es una herramienta moderna para gestionar dependencias, entornos y empaquetado de proyectos en Python. Centraliza la configuración en `pyproject.toml`, resuelve dependencias y genera un archivo de bloqueo (`poetry.lock`) para reproducibilidad. También facilita la construcción y publicación de paquetes.

### ¿Por qué usar Poetry?

- Gestión declarativa en `pyproject.toml` (estándar PEP 518/PEP 621).
- Resolución de dependencias fiable y reproducible gracias a `poetry.lock`.
- Integración de creación de paquetes (build) y publicación (publish).
- Manejo integrado de entornos virtuales (opcionalmente en el proyecto).
- Flujo de trabajo coherente para aplicaciones y librerías.

Beneficios prácticos:

- Reproducibilidad: `poetry.lock` asegura que todos usen las mismas versiones.
- Menos archivos de configuración dispersos (reemplaza requirements.txt, setup.py, setup.cfg en muchos casos).
- Mejor experiencia para publicar bibliotecas en PyPI.

### ¿Cuándo usar Poetry?

- Proyectos nuevos de Python donde quieras reproducibilidad y un flujo de empaquetado sencillo.
- Librerías que se publicarán en PyPI (gestiona metadata y publicación).
- Aplicaciones donde deseas una gestión clara de entornos y dependencias.
- En CI/CD para instalar dependencias de forma reproducible.

Cuándo no es estrictamente necesario:

- Scripts muy simples o proyectos ad-hoc donde usar solo `pip` y un entorno global resulta suficiente.
- Cuando una organización ya tiene una infraestructura consolidada con otras herramientas y migrar sería costoso (aunque Poetry puede integrarse con muchas stacks).

### Contrato mínimo (qué esperar)

- Entrada: `pyproject.toml` y comandos de Poetry.
- Salida: entorno virtual con dependencias instaladas, `poetry.lock`, artefactos de build (`.whl`, `.tar.gz`).
- Modos de error: conflictos de resolución de dependencia (requiere ajuste de versiones), problemas de permisos al publicar.

### Instalación (recomendado para Windows PowerShell)

Recomendado: instalar Poetry con `pipx` o con el instalador oficial. Ejemplos para PowerShell:

```powershell
# Si tienes pipx instalado (recomendado)
py -m pipx install poetry

# Alternativa con pip (usuario):
py -m pip install --user poetry

# Si no tienes pipx y quieres instalar pipx primero:
py -m pip install --user pipx
py -m pipx ensurepath
``` 

Nota: después de instalar por primera vez puede ser necesario cerrar y reabrir la terminal para que `poetry` esté en PATH.

### Primeros pasos en un proyecto

Crear un nuevo proyecto:

```powershell
mkdir mi_proyecto
cd mi_proyecto
poetry init --no-interaction  # genera pyproject.toml básico
```

Usar un proyecto existente (inicializar pyproject toml interactivo opcional):

```powershell
poetry init
```

Instalar dependencias (ejemplos):

```powershell
# Añadir una dependencia a runtime
poetry add requests

# Añadir una dependencia de desarrollo
poetry add --dev pytest

# Instalar todas las dependencias definidas (usado en CI o al clonar)
poetry install
```

### Entornos virtuales

Poetry crea y gestiona automáticamente entornos virtuales. Comandos útiles:

```powershell
# Entrar al shell del virtualenv gestionado por poetry
poetry shell

# Ejecutar un comando dentro del entorno sin activarlo
poetry run python -m pip list

# Opcional: crear virtualenv dentro del proyecto (si prefieres)
poetry config virtualenvs.in-project true --local
```

### Bloqueo y reproducibilidad

```powershell
# Genera/actualiza poetry.lock (se crea automáticamente con add/install)
poetry lock

# Exportar requirements.txt (útil para entornos que no usan poetry)
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Build y publicación

```powershell
# Construir artefactos (.whl y .tar.gz)
poetry build

# Publicar en PyPI (configura credenciales primero)
poetry publish --build
```

### Integración en CI

- En pipelines, usa `poetry install --no-dev` para producción o `poetry install` para tests.
- Puedes cachear el directorio `.cache/pypoetry` y la carpeta de virtualenvs.

Ejemplo minimal en CI (PowerShell-like):

```powershell
py -m pipx ensurepath; py -m pipx install poetry
poetry install
poetry run pytest
```

### Ventajas y desventajas (resumen)

Ventajas:

- Reproducibilidad y bloqueo de versiones.
- `pyproject.toml` estándar.
- Flujo integrado para empaquetar y publicar.
- Gestión automática de entornos virtuales.

Desventajas / limitaciones:

- Puede introducir curva de aprendizaje para equipos acostumbrados a `requirements.txt`.
- En casos muy concretos puede haber conflictos de resolución que requieren intervención manual.
- Algunas integraciones muy antiguas o herramientas internas pueden esperar `requirements.txt` o `setup.py`.

### Buenas prácticas

- Mantener `pyproject.toml` en el control de versiones.
- Comprobar y commitear `poetry.lock` para aplicaciones; para librerías depende de la política del equipo (normalmente sí para aplicaciones, opcional para librerías publicadas).
- Usar `poetry export` si necesitas `requirements.txt` para infra que no soporte Poetry.
- Configurar `virtualenvs.in-project` si deseas que el entorno quede dentro del repo (útil en algunos CI/ED).

### Recursos y referencias

- Documentación oficial: https://python-poetry.org/docs/
- Guía rápida: https://python-poetry.org/docs/basic-usage/
- PEP relacionados: PEP 518 (pyproject), PEP 621 (metadata)

