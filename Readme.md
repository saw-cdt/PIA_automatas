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

Proyecto realizado como entrega de la materia Teoría de Autómatas.
