## Teoría de Git

### ¿Qué es Git?

Git es un sistema de control de versiones distribuido diseñado para registrar cambios en ficheros y coordinar el trabajo entre varios desarrolladores. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux. A diferencia de sistemas centralizados, en Git cada copia del repositorio contiene el historial completo.

### Modelo básico: snapshots, no diferencias

Cada vez que haces un commit, Git guarda una instantánea (snapshot) del contenido de los archivos (eficientemente, compartiendo objetos inmutables cuando no cambian). Internamente Git almacena objetos: blobs (contenido de archivos), trees (estructura), commits (metadatos y puntero al tree) y refs (ramas y etiquetas).

Conceptos clave:
- Working Directory (directorio de trabajo): los archivos que editas.
- Staging Area / Index: área donde preparas qué irá al siguiente commit.
- Commit: snapshot con metadatos (autor, mensaje, puntero al tree padre(s)).
- HEAD: referencia al commit actual (normalmente la punta de la rama activa).
- Branch (rama): puntero movible a commits; las ramas son ligeras y baratas.

### Objetos de Git (vistas rápidas)
- Blob: contiene el contenido de un archivo.
- Tree: lista de blobs y subtrees; representa un directorio.
- Commit: apunta a un tree y a 0 o más padres (merge tiene más de uno); incluye mensaje y autor.
- Tag: etiqueta que apunta a un commit (puede ser anotada o liviana).

Git identifica objetos por un hash (SHA-1 históricamente, y en versiones nuevas soporta SHA-256); ese hash garantiza integridad.

### El DAG de commits

Los commits forman un grafo acíclico dirigido (DAG). Cada commit apunta a su(s) padre(s). Las ramas son simplemente referencias que apuntan a commits en ese DAG. Cuando haces un commit, la rama activa avanza.

Diagrama ASCII simple:

	A --- B --- C  (main)
						 \
							D --- E  (feature)

Aquí C es el padre de D, y la rama feature apunta a E.

### Flujo de trabajo básico

1. Editas archivos en el working directory.
2. git add coloca cambios en el index (staging).
3. git commit crea un nuevo commit a partir del index.
4. Si trabajas con remotos: git push/git pull/git fetch sincronizan con repositorios remotos.

### Ramas y fusiones

Ramas permiten desarrollar features aisladas. Para integrar:
- Merge: crea un commit de merge que une dos historiales (puede ser fast-forward si no hay divergencia).
- Rebase: reubica commits sobre otra base (reescribe historial localmente).

Cuando usar merge vs rebase:
- Merge: preserva la historia real y muestra merges explícitos; es seguro en commits públicos.
- Rebase: crea un historial lineal y más limpio, útil para commits locales antes de compartir; NO reescribir commits que ya se han compartido con otros.

### Comandos comunes (rápido)

- git init: iniciar un repositorio.
- git clone <url>: clonar un repositorio remoto.
- git status: ver estado del working tree e index.
- git add <ruta>: añadir archivos al index.
- git commit -m "mensaje": crear un commit.
- git log: ver historial.
- git diff: ver diferencias.
- git branch: listar/crear/renombrar ramas.
- git checkout / git switch: cambiar de rama.
- git merge <rama>: fusionar otra rama en la actual.
- git rebase <base>: reubicar commits sobre otra base.
- git fetch / git pull / git push: sincronizar con remoto.
- git stash: guardar temporalmente cambios no commiteados.
- git tag: crear etiquetas.

Ejemplos (PowerShell):

powershell
# Inicializar un repo
git init

# Clonar
git clone https://github.com/usuario/repositorio.git

# Crear un commit
git add .
git commit -m "Describir el cambio en una línea clara"

# Ramas
git branch feature/login
git switch feature/login

# Fusionar (desde main)
git switch main
git merge feature/login

# Rebase (hacer commits de feature sobre main)
git switch feature/login
git fetch origin
git rebase origin/main

# Subir cambios
git push origin feature/login


### Recuperación y seguridad: reflog, reset y revert

- git reflog: historial de dónde ha apuntado HEAD; esencial para recuperar commits "perdidos".
- git reset [--soft|--mixed|--hard] <commit>:
	- --soft: mueve HEAD manteniendo staging/workdir.
	- --mixed (por defecto): mueve HEAD y resetea index, mantiene working dir.
	- --hard: mueve HEAD y fuerza index y working dir al commit (peligroso, borrar cambios locales).
- git revert <commit>: crea un nuevo commit que deshace los cambios del commit indicado (safe para historial público).

Recuperar un commit borrado accidentalmente (ejemplo):

powershell
# ver reflog y encontrar el hash perdido
git reflog
# suponer que el hash es abc123
git checkout -b recuperar-abc123 abc123


### .gitignore

Archivo para indicar archivos o patrones que Git debe ignorar (archivos de construcción, dependencias locales, credenciales, etc.).

Ejemplo mínimo .gitignore:


# Node
node_modules/
dist/

# Editor
.vscode/
*.swp


### Workflows populares

- Centralizado: similar a SVN, todos trabajan en ramas remotas compartidas (p. ej. main).
- Feature-branch: cada feature/bugfix en su propia rama; luego PR/MR hacia main.
- GitFlow: ramas develop, release, hotfix y main con reglas más formales.
- Forking workflow: usado en proyectos abiertos—cada colaborador trabaja en un fork y crea PR al upstream.

### Buenas prácticas

- Commits pequeños y atómicos: cada commit debe ser una unidad lógica de trabajo.
- Mensajes claros: usar una línea resumen y, si hace falta, una descripción más larga.
- Revisiones de código (Pull Requests): integrar revisiones y pruebas antes de merge.
- No reescribir la historia pública: evita rebase o push --force en ramas compartidas.
- Usar branches para features, fixes y experimentos; limpiar ramas obsoletas.

Ejemplo de mensaje de commit:


feat(auth): añadir validación de token JWT

Se añade verificación de la expiración y manejo de errores para tokens inválidos.
Tests añadidos para escenarios de token expirado.


### Casos de uso avanzados

- Cherry-pick: aplicar un commit específico de otra rama sin fusionar todo el historial.
- Submodules: incluir otro repositorio dentro de uno (útil, pero aporta complejidad).
- Hooks: scripts que se ejecutan en eventos (pre-commit, pre-push) para linters o pruebas.

### Problemas comunes y soluciones rápidas

- Conflictos de merge: resolver manualmente los archivos conflictivos, git add y git commit.
- Archivos añadidos por error: usar git rm --cached archivo y añadir a .gitignore.
- Necesito deshacer un commit local (no publicado): git reset --soft HEAD~1.
- Necesito deshacer un commit publicado: git revert <commit>.

### Recursos y referencias

- Documentación oficial: https://git-scm.com/doc
- Book (Pro Git, gratis): https://git-scm.com/book/es/v2

## Try it (rápido) — comandos para PowerShell

powershell
# 1) iniciar y hacer el primer commit
git init
git add README.md
git commit -m "chore: primer commit"

# 2) crear una rama, trabajar y abrir PR (resumen de pasos locales)
git switch -c feature/mi-feature
# editar archivos
git add .
git commit -m "feat: mi feature inicial"
git push -u origin feature/mi-feature

# 3) sincronizar con main remoto y rebase (flujo recomendado para commits locales)
git fetch origin
git switch feature/mi-feature
git rebase origin/main

# 4) recuperar un commit perdido (reflog)
git reflog
git switch -c recuperar-abcd1234 abcd1234
