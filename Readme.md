# Máquina de Turing — Proyecto (Teoría de Autómatas)

## Descripción

Este proyecto contiene una implementación en Python de una Máquina de Turing diseñada para reconocer un lenguaje específico.La máquina trabaja sobre el alfabeto {a, b, c} y utiliza símbolos marcadores `x` y `y` durante el proceso.

## Lenguaje reconocido

La Máquina acepta cadenas de la forma w ∈ {a,b,c}\* donde w contiene el triple de `a`'s que la suma de `b`'s y `c`'s, es decir:

    |w|_a = 3 * (|w|_b + |w|_c)

Aquí `|w|_a` denota el número de símbolos `a` en la cadena y `|w|_b`, `|w|_c` los de `b` y `c` respectivamente.

## Estructura del proyecto

-   `PIA.py` — implementación de la Máquina de Turing, con función `delta`, tipos, y una interfaz interactiva (`process_string_verbose`) para simular y ver la cinta paso a paso.

## Ejemplos

-   Cadenas aceptadas (ejemplos):

    -   `aaab` (tres `a`, un `b` → 3 = 3\*1)
    -   `aaaaaabbb` (6 `a`, 3 `b` → 6 = 3\*3)

-   Cadenas rechazadas (ejemplos):
    -   `aab` (2 `a`, 1 `b` → 2 ≠ 3\*1)
    -   `bbb` (0 `a`, 3 `b` → 0 ≠ 9)

La máquina utiliza los símbolos `x` e `y` como marcadores temporales para contabilizar y emparejar símbolos.

`PIA.py` tiene una función `process_string_verbose` que limita los pasos a 1000 para evitar bucles infinitos en cadenas que causen comportamiento no terminante.

## Cómo se hizo el proyecto

### 1. Análisis del problema
El proyecto comenzó con el análisis del lenguaje a reconocer: cadenas donde el número de `a`'s es el triple de la suma de `b`'s y `c`'s. Esto requería un mecanismo de conteo y verificación que fuera implementable con una Máquina de Turing.

### 2. Diseño de la estrategia del algoritmo
Se diseñó una estrategia basada en:
- **Marcado temporal**: Usar símbolos `x` e `y` para marcar caracteres ya procesados
- **Conteo por bloques**: Por cada `b` o `c` encontrado, buscar y marcar tres `a`'s correspondientes
- **Verificación final**: Al terminar, solo deben quedar símbolos marcadores en la cinta

### 3. Definición de estados
Se definieron 11 estados con funciones específicas:
- **q1**: Estado inicial, busca `b` o `c` para procesar
- **q2-q4**: Primera secuencia para marcar la primera `a`
- **q5-q6**: Segunda secuencia para marcar la segunda `a`  
- **q7-q8**: Tercera secuencia para marcar la tercera `a`
- **q9**: Verificación final (solo marcadores permitidos)
- **q10**: Estado de aceptación
- **q11**: Estado de rechazo

### 4. Implementación en Python
La implementación utilizó:

#### Estructuras de datos
- **Enums** para estados, símbolos y movimientos (mejor legibilidad y type safety)
- **NamedTuple** para entradas y salidas de la función de transición
- **Typing** para mejor documentación del código

#### Función de transición δ (delta)
```python
def delta(input_tuple: TuringInput) -> TuringOutput:
```
Implementada con pattern matching usando `match-case` para manejar cada estado y símbolo de forma clara y estructurada.

#### Simulador visual
```python
def process_string_verbose(string: str) -> bool:
```
- Visualización paso a paso de la cinta
- Control de la cabeza lectora con indicador visual (`↑`)
- Limitación de 1000 pasos para prevenir bucles infinitos
- Manejo de extensión dinámica de la cinta

### 5. Características técnicas implementadas
- **Cinta infinita simulada**: Extensión automática hacia izquierda y derecha según necesidad
- **Visualización en tiempo real**: Cada paso muestra el estado actual y la posición de la cabeza
- **Manejo de errores**: Captura de excepciones durante la simulación
- **Interfaz interactiva**: Bucle principal para probar múltiples cadenas

### 6. Algoritmo de funcionamiento
1. **Inicialización**: Coloca la cadena en la cinta con espacios en blanco a los extremos
2. **Búsqueda**: Encuentra el primer `b` o `c` y lo marca con `y`
3. **Conteo triple**: Busca y marca tres `a`'s consecutivas con `x`
4. **Repetición**: Repite el proceso hasta procesar todos los `b`'s y `c`'s
5. **Verificación**: Comprueba que solo queden símbolos marcadores (`x`, `y`)
6. **Decisión**: Acepta si la verificación es exitosa, rechaza en caso contrario

### 7. Herramientas y metodología
- **Lenguaje**: Python 3.10+ (uso de pattern matching)
- **Paradigma**: Programación funcional para la función de transición
- **Testing**: Pruebas manuales con casos de aceptación y rechazo
- **Documentación**: Código autodocumentado con type hints y comentarios

Proyecto realizado como entrega de la materia Teoría de Autómatas.
