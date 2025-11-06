## ¿Qué es unit testing?
- Una "unit test" (prueba unitaria) verifica el comportamiento de la unidad más pequeña verificable de código —normalmente una función, método o clase aislada— para asegurar que produce la salida esperada ante entradas dadas.
- Objetivo: detectar fallos, asegurar regresiones no aparecen y documentar comportamiento esperado de pequeñas unidades.

## Contrato mínimo (inputs/outputs/errores)
- Entrada: una unidad de código (función/método), datos de entrada controlables, y entornos simulados (mocks/fakes) si hace I/O.
- Salida esperada: valores retornados, efectos colaterales (estado) y excepciones controladas.
- Errores: tests deben fallar de forma determinista si el comportamiento cambia; pruebas deben ser independientes y repetibles.

## ¿Por qué son importantes?
- Detectan errores temprano y reducen tiempo de depuración.
- Permiten refactorizaciones seguras (regresión).
- Documentan contratos de comportamiento del código.
- Facilitan integraciones en CI/CD: cada commit puede validar que las unidades no se rompen.
- Mejoran diseño: el código testable suele ser más modular y con menor acoplamiento.

## ¿Cuándo usar unit tests?
- En lógica de negocio crítica (algoritmos, validaciones).
- Para librerías y funciones que se reutilizan.
- En sistemas donde la estabilidad importa (servicios, APIs).
- No: no tiene mucho valor para UI muy volátil (usar pruebas de integración/E2E allí).

## Tipos de pruebas y cómo se relacionan
- Unit tests: verifican unidades aisladas (rápidos, deterministas).
- Integration tests: verifican interacciones entre componentes (más lentos).
- End-to-end (E2E): prueban el sistema completo (más lentos, frágiles).
- Property-based testing, fuzzing y mutation testing: técnicas complementarias para robustez.

## Principios y características de buenas pruebas unitarias
- Rápidas: deben ejecutarse en milisegundos a segundos.
- Aisladas: cada test no depende de otros tests ni del entorno externo.
- Deterministas: mismo resultado en cada ejecución.
- Pequeñas y enfocadas: 1 aserto principal por test o un comportamiento a la vez.
- Legibles y mantenibles: buen nombre, setup claro, teardown mínimo.
- Independientes de la implementación: probar comportamiento público, no detalles internos.

## Test doubles (resumen)
- Dummy: objeto pasado pero no usado.
- Stub: devuelve datos predefinidos.
- Mock: verifica que se llamaron métodos/argumentos (comportamiento).
- Spy: similar a mock, observa llamadas reales.
- Fake: implementación simplificada (ej.: base de datos en memoria).

## Herramientas populares
- Python: pytest, unittest, nose. Mocks: unittest.mock, pytest-mock. Coverage: coverage.py, mutmut (mutation).
- JavaScript/TypeScript: Jest, Mocha + Chai, Sinon (mocks/spies). Mutation: Stryker.
- Java: JUnit, Mockito. Coverage: JaCoCo.
- CI: GitHub Actions, GitLab CI, Azure Pipelines, CircleCI.

## Cómo escribir un unit test — pasos prácticos
1. Selecciona la unidad y el comportamiento a verificar.
2. Escribe test que establezca el contexto (arrange), ejecute la unidad (act) y verifique la salida (assert).
3. Aísla dependencias (mock/stub/fake).
4. Ejecuta frecuentemente.
5. Mantén los tests rápidos.

### Estructura (naming / layout)
- Archivos: tests/ o test_*.py (Python), __tests__/ o *.test.js (JS).
- Nombres: test_deberia_hacer_algo_cuando_condicion.
- Evitar: tests largos que hacen muchas aserciones no relacionadas.

## Ejemplo en Python (pytest)
Archivo: test_math.py
python
# test_math.py
import pytest
from mypackage.math_utils import suma, dividir

def test_suma_simple():
    assert suma(2, 3) == 5

def test_dividir_por_cero_lanza():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, 1, 0),
])
def test_suma_parametrizada(a, b, expected):
    assert suma(a, b) == expected

Mocks con unittest.mock:
python
from unittest.mock import Mock, patch
from mypackage.service import Service

def test_llama_api_externo(monkeypatch):
    fake_resp = {"value": 42}
    monkeypatch.setattr("mypackage.external_api.call", lambda *args, **kwargs: fake_resp)
    s = Service()
    assert s.get_value() == 42

Comandos (PowerShell):
powershell
# instalar pytest (si usas virtualenv)
python -m pip install pytest
# ejecutar tests
python -m pytest -q
# ejecutar cobertura
python -m pip install coverage
coverage run -m pytest
coverage report -m


## Ejemplo en JavaScript (Jest)
Archivo: math.test.js
javascript
// math.js
function suma(a, b) { return a + b; }
module.exports = { suma };

// math.test.js
const { suma } = require('./math');

test('suma simple', () => {
  expect(suma(2, 3)).toBe(5);
});

test.each([
  [1, 2, 3],
  [0, 5, 5],
  [-1, 1, 0],
])('suma %i + %i = %i', (a, b, expected) => {
  expect(suma(a, b)).toBe(expected);
});

Comandos (PowerShell):
powershell
npm init -y
npm install --save-dev jest
npx jest --coverage


## Mocking y aislamiento (prácticas)
- Preferir inyección de dependencias para facilitar mocking.
- Evitar mocks excesivos que prueben detalles internos (p. ej., llamadas internas de una función).
- Para I/O (DB, red), usar fakes o bases en memoria para speed y determinismo.
- Usa fixtures para setup/teardown reutilizable (pytest fixtures, beforeEach/afterEach en Jest).

## Métricas y cobertura
- Cobertura de código (coverage) mide líneas/branches/testadas; no reemplaza tests bien diseñados.
- Objetivo razonable: 70–90% (depende del proyecto); prioriza cobertura en lógica crítica.
- Usa mutation testing (mutmut/Stryker) para medir la calidad real de tests.

## Buenas prácticas / checklist
- Tests breves, claros y rápidos.
- Nombres expresivos.
- Evitar dependencias externas reales en unit tests.
- Mantener tests en VCS junto al código.
- Ejecutar tests en CI en cada PR/commit.
- Mantener fixtures simples; limpiar estado entre tests.
- Revisar y actualizar tests cuando el comportamiento cambia.
- Priorizar casos límite y errores esperados.

## Anti-patrones (qué evitar)
- Tests que dependen del orden de ejecución.
- Tests frágiles que usan timestamps o valores aleatorios sin control.
- Test que validan implementación interna en lugar de output.
- Tests demasiado grandes (problema: difícilmente identificas qué falla).
- Overmocking que da falsa sensación de seguridad.

## Estrategias adicionales
- TDD (Test-Driven Development): escribir tests antes del código para guiar diseño.
- Pair testing: escribir tests con otro dev para compartir conocimiento.
- Integrar tests en PR template y pipelines.
- Ejecutar tests rápidos en pre-commit y tests completos en CI.
- Pruebas parametrizadas para cubrir múltiples casos con poco código.
- Usar "contract tests" para garantizar integraciones entre servicios.

## Ejemplos de integración CI (breve)
- GitHub Actions: enciende pytest o npm test en push/PR. (Si quieres, genero snippets exactos).

## Edge cases y consideraciones
- Pruebas en presencia de concurrencia/async: usar herramientas/fixtures para control de event loop.
- Tests que dependen de hora/locale: inyectar reloj o fijar locale.
- Tests con recursos limitados (sockets, archivos): usar temp dirs y cleaners.
- Rendimiento: tests unitarios no deben medir rendimiento a gran escala; para eso usa benchmarks.

## Recursos recomendados
- pytest docs (python): https://docs.pytest.org
- pytest-mock, unittest.mock
- Jest docs: https://jestjs.io
- Martin Fowler — "Mocks aren't Stubs"
- Kent Beck — "Test-Driven Development"
- Herramientas de mutation testing: Stryker (JS), mutmut (Python)

## Pequeña lista de verificación rápida antes de merge
- [ ] Tests nuevos pasan en local.
- [ ] Cobertura no ha caído por debajo del umbral.
- [ ] No hay tests frágiles (temporalmente saltados con explicación).
- [ ] CI ejecuta los tests y pasa.

## Resumen / qué cambié y verifiqué
He elaborado una guía completa sobre teoría, uso, importancia, buenas prácticas, anti-patrones y ejemplos prácticos en Python y JavaScript, más comandos para ejecutar y recursos. Si quieres, puedo:
- Crear ejemplos de archivos test_* en tu proyecto.
- Generar un workflow de GitHub Actions que ejecute los tests.
- Añadir tests concretos para un archivo de tu repositorio —dime qué lenguaje y directorio.

