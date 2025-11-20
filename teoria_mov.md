# Movimiento Armónico Simple (MAS) — Teoría completa

Este documento recoge la teoría del movimiento armónico simple (MAS) de forma clara y lista para copiar. Incluye definiciones, deducciones, ejemplos resueltos y una hoja de fórmulas.

## 1. Introducción

El movimiento armónico simple (MAS) es un tipo de movimiento oscilatorio en el que la fuerza restauradora que actúa sobre el sistema es proporcional y de sentido contrario al desplazamiento respecto a la posición de equilibrio. Es la descripción más simple de muchas oscilaciones físicas.

Características principales:
- La trayectoria es periódica: el sistema repite su movimiento después de un periodo T.
- La fuerza restauradora es lineal respecto al desplazamiento: F = -k x (ley de Hooke en sistemas elásticos).
- La solución más general es una combinación de funciones seno y coseno de una frecuencia angular constante.

Aplicaciones: masa-resorte, péndulo (para pequeñas oscilaciones), circuitos LC, modos normales de sistemas acoplados, vibraciones en estructuras, oscilaciones moleculares, etc.

## 2. Modelo masa-resorte y deducción de la ecuación del MAS

Consideremos una masa m unida a un muelle con constante elástica k, moviéndose sin fricción sobre una superficie horizontal. Tomando x(t) como el desplazamiento respecto a la posición de equilibrio, la segunda ley de Newton nos da:

m a = F_res
m x''(t) = -k x(t)

Dividiendo por m:

x''(t) + (k/m) x(t) = 0

Definimos la frecuencia angular natural:

ω0 = sqrt(k/m)

por tanto la ecuación se escribe de forma estándar:

x''(t) + ω0^2 x(t) = 0   (ecuación del MAS)

Donde:
- x(t): desplazamiento (m)
- ω0: frecuencia angular propia (rad/s)
- T = 2π/ω0: periodo (s)
- f = 1/T = ω0/(2π): frecuencia en Hz

## 3. Solución general

La ecuación diferencial tiene solución general (ecuación homogénea con coeficientes constantes):

x(t) = A cos(ω0 t) + B sin(ω0 t)

Que se puede reescribir como:

x(t) = A0 cos(ω0 t + φ)

donde A0 = sqrt(A^2 + B^2) es la amplitud y φ es la fase inicial tal que:

A = A0 cos φ,   B = -A0 sin φ   (dependiendo de la convención de signos; confirmar con condiciones iniciales)

Interpretación:
- A0 (amplitud): valor máximo del desplazamiento.
- φ (fase): determina el desplazamiento y la velocidad iniciales.

### Determinación de A0 y φ a partir de condiciones iniciales

Si conocemos x(0) = x0 y v(0) = v0, entonces:

x(0) = A0 cos φ = x0
v(t) = x'(t) = -A0 ω0 sin(ω0 t + φ)  => v(0) = -A0 ω0 sin φ = v0

De donde:

A0 = sqrt(x0^2 + (v0/ω0)^2)
φ = arctan2(-v0/ω0, x0)   (usar arctan2 para conservar el cuadrante correcto)

Observación: la expresión de la fase puede variar en signo según la convención usada para x(t) = A cos(ω0 t + φ) o con seno.

## 4. Velocidad y aceleración

Derivando x(t) = A0 cos(ω0 t + φ):

v(t) = x'(t) = -A0 ω0 sin(ω0 t + φ)

a(t) = x''(t) = -A0 ω0^2 cos(ω0 t + φ) = -ω0^2 x(t)

La última relación a(t) = -ω0^2 x(t) es característica: la aceleración es proporcional y opuesta al desplazamiento.

## 5. Energía en el MAS

Energía cinética:

K(t) = (1/2) m v(t)^2 = (1/2) m A0^2 ω0^2 sin^2(ω0 t + φ)

Energía potencial (muelle):

U(t) = (1/2) k x(t)^2 = (1/2) k A0^2 cos^2(ω0 t + φ)

Energía total (constante):

E = K + U = (1/2) k A0^2 = (1/2) m A0^2 ω0^2

Observaciones:
- La energía oscila entre cinética y potencial, pero la suma es constante si no hay disipación.
- En los instantes de máxima amplitud la energía es totalmente potencial; en el paso por el equilibrio la energía es totalmente cinética.

## 6. Representación fasorial y diagrama de fase

- Representación fasorial: escribir la solución como parte real de A e^{i(ω0 t + φ)} facilita el manejo con superposición y rotaciones en el plano complejo.
- Diagrama de fase: gráfico (x versus v). Para MAS ideal sin amortiguamiento la trayectoria en el espacio de fases es una elipse centrada en el origen.

## 7. Oscilador amortiguado (introducción)

Si existe una fuerza disipativa proporcional a la velocidad (amortiguamiento viscosa), la ecuación se escribe:

x''(t) + 2β x'(t) + ω0^2 x(t) = 0

donde β es el coeficiente de amortiguamiento (s^-1). Dependiendo de β y ω0 tenemos tres regímenes:

1. Subamortiguado (β < ω0): solución oscilatoria atenuada
   x(t) = A e^{-β t} cos(ω' t + φ)
   con ω' = sqrt(ω0^2 - β^2)

2. Críticamente amortiguado (β = ω0): no hay oscilaciones, se vuelve a equilibrio lo más rápido posible sin sobresalto.

3. Sobreamortiguado (β > ω0): no hay oscilaciones, decaimiento lento hacia el equilibrio (dos exponentes reales negativos).

La energía del sistema decrece con el tiempo debido a la disipación.

### Decremento logarítmico y Q

Para amortiguamiento ligero (β << ω0), la envolvente decrece como e^{-β t}. El factor de calidad Q se define como:

Q = ω0 / (2β)

Q mide la relación entre la energía almacenada y la energía disipada por ciclo; valores altos de Q indican oscilaciones poco amortiguadas.

## 8. Oscilador forzado y resonancia

Si aplicamos una fuerza externa armónica F(t) = F0 cos(ω t), la ecuación es:

x'' + 2β x' + ω0^2 x = (F0/m) cos(ω t)

La solución general es suma de la solución transitoria (homogénea, que decae si β>0) y la solución particular estacionaria (de régimen permanente), que para la fuerza armónica tiene la forma:

x_p(t) = C cos(ω t - δ)

donde la amplitud C y el desfase δ dependen de ω, ω0, β. La amplitud en régimen estacionario vale:

C(ω) = (F0/m) / sqrt((ω0^2 - ω^2)^2 + (2β ω)^2)

y el desfase δ se obtiene de:

tan δ = (2β ω) / (ω0^2 - ω^2)

Resonancia: la máxima amplitud ocurre cerca de ω ≈ ω0 para amortiguamiento pequeño; la amplitud máxima y el ancho de la curva dependen de β. El valor de la frecuencia que maximiza C es:

ω_res = sqrt(ω0^2 - 2β^2)   (para β pequeño se aproxima a ω0)

El ancho de resonancia Δω ≈ 2β y Q ≈ ω0 / Δω.

## 9. Métodos de resolución (breve)

- Solución directa de la EDO lineal homogénea con coeficientes constantes (char polynomial).
- Método fasorial (útil para forzado armónico en régimen estacionario).
- Transformada de Laplace (útil para condiciones iniciales y forzamientos arbitrarios).

## 10. Casos no lineales y generalizaciones

- Péndulo grande: la ecuación real es θ'' + (g/L) sin θ = 0; solo para pequeñas oscilaciones sinusoide se aproxima a MAS con ω0 = sqrt(g/L).
- Sistemas acoplados: producen modos normales y frecuencias propias; MAS es la base para entender acoplamiento y normal modes.

## 11. Ejemplos resueltos

Ejemplo 1 — Masa-resorte (condiciones iniciales)

Datos: m = 0.5 kg, k = 8 N/m, x(0) = 0.1 m, v(0) = 0 m/s.

1) Calcular ω0:

ω0 = sqrt(k/m) = sqrt(8 / 0.5) = sqrt(16) = 4 rad/s

2) Amplitud y fase:

A0 = sqrt(x0^2 + (v0/ω0)^2) = sqrt(0.1^2 + 0^2) = 0.1 m
φ = arctan2(-v0/ω0, x0) = arctan2(0, 0.1) = 0

3) Solución:

x(t) = 0.1 cos(4 t)  (m)

Ejemplo 2 — Péndulo (pequeñas oscilaciones)

Consideremos un péndulo simple de longitud L = 1.2 m. Para pequeñas oscilaciones sin fricción:

ω0 = sqrt(g / L) ≈ sqrt(9.81 / 1.2) ≈ 2.86 rad/s
T = 2π / ω0 ≈ 2.197 s

Para ángulos pequeños θ(t) ≈ θ0 cos(ω0 t + φ).

Ejemplo 3 — Amortiguamiento ligero

Sistema: m = 1 kg, k = 25 N/m → ω0 = 5 rad/s. Amortiguamiento tal que β = 0.2 s^-1 (ligero).

Solución subamortiguada:

ω' = sqrt(ω0^2 - β^2) = sqrt(25 - 0.04) ≈ 4.998 rad/s ≈ 4.998
x(t) = A e^{-0.2 t} cos(ω' t + φ)

Si x(0)=0.1 m, v(0)=0, entonces A≈0.1 y φ≈0.

Ejemplo 4 — Forzado en régimen estacionario

Sea m = 1 kg, k = 100 N/m → ω0 = 10 rad/s; β = 0.5 s^-1. Fuerza F(t) = F0 cos(ω t) con F0 = 1 N y ω = 9 rad/s.

La amplitud en régimen estacionario:

C = (F0/m) / sqrt((ω0^2 - ω^2)^2 + (2β ω)^2)
  = 1 / sqrt((100 - 81)^2 + (1 * 9)^2)
  = 1 / sqrt(19^2 + 9^2)
  = 1 / sqrt(361 + 81)
  = 1 / sqrt(442) ≈ 0.0476 m

Desfase:

tan δ = (2β ω) / (ω0^2 - ω^2) = (1 * 9) / 19 ≈ 9/19 → δ ≈ arctan(9/19) ≈ 0.436 rad


## 12. Hoja de fórmulas (resumen rápido)

- Ecuación del MAS: x'' + ω0^2 x = 0
- ω0 = sqrt(k/m)
- Solución: x(t) = A cos(ω0 t + φ)
- v(t) = -A ω0 sin(ω0 t + φ)
- a(t) = -A ω0^2 cos(ω0 t + φ) = -ω0^2 x(t)
- Energía total: E = (1/2) k A^2 = (1/2) m A^2 ω0^2
- Oscilador amortiguado: x'' + 2β x' + ω0^2 x = 0
  - Subamortiguado: x(t) = A e^{-β t} cos(ω' t + φ), ω' = sqrt(ω0^2 - β^2)
- Oscilador forzado: x'' + 2β x' + ω0^2 x = (F0/m) cos(ω t)
  - Amplitud estacionaria: C(ω) = (F0/m) / sqrt((ω0^2 - ω^2)^2 + (2β ω)^2)
  - Fase: tan δ = (2β ω) / (ω0^2 - ω^2)

## 13. Notas y referencias

- Para ampliación: cualquier libro de Física para universitarios (Halliday/Resnick, Serway/Jewett), o cursos de Física I y Oscilaciones.
- Para tratamiento más avanzado: vibraciones en sistemas acoplados, método de perturbaciones para no linealidades, teoría de resonancia en sistemas eléctricos y mecánicos.

---

Si quieres, lo adapto a formato .md con imágenes/diagramas (SVG), o lo divido en secciones separadas para entregarlo por partes. También puedo incluir más ejemplos resueltos con pasos numéricos más detallados.
