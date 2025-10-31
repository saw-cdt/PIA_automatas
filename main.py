from enum import Enum, IntEnum
from typing import NamedTuple
import time

class State(Enum):
    q1 = "q1"
    q2 = "q2"
    q3 = "q3"
    q4 = "q4"
    q5 = "q5"
    q6 = "q6"
    q7 = "q7"
    q8 = "q8"
    q9 = "q9"
    q10 = "q10"
    q11 = "q11"

class Symbol(Enum):
    a = "a"
    b = "b"
    c = "c"
    x = "x"
    y = "y"
    _ = "␢"

class Move(IntEnum):
    L = -1
    S = 0
    R = 1

class TuringInput(NamedTuple):
    q: State
    s: Symbol

class TuringOutput(NamedTuple):
    q: State
    s: Symbol
    m: Move

def delta(input_tuple: TuringInput) -> TuringOutput:
    current_q = input_tuple.q
    current_s = input_tuple.s

    match current_q:
        case State.q1:
            if current_s == Symbol.a:
                return TuringOutput(State.q1, Symbol.a, Move.R)
            elif current_s == Symbol.x:
                return TuringOutput(State.q1, Symbol.x, Move.R)
            elif current_s == Symbol.y:
                return TuringOutput(State.q1, Symbol.y, Move.R)
            elif current_s == Symbol.b:
                return TuringOutput(State.q2, Symbol.y, Move.L)
            elif current_s == Symbol.c:
                return TuringOutput(State.q2, Symbol.y, Move.L)
            elif current_s == Symbol._:
                return TuringOutput(State.q9, Symbol._, Move.L)
            else:
                return TuringOutput(State.q11, current_s, Move.S)

        case State.q2:
            if current_s == Symbol._:
                return TuringOutput(State.q3, Symbol._, Move.R)
            else:
                return TuringOutput(State.q2, current_s, Move.L)

        case State.q3:
            if current_s == Symbol.a:
                return TuringOutput(State.q4, Symbol.x, Move.L)
            elif current_s in [Symbol.x, Symbol.y, Symbol.b, Symbol.c]:
                return TuringOutput(State.q3, current_s, Move.R)
            elif current_s == Symbol._:
                return TuringOutput(State.q11, Symbol._, Move.S)
            else:
                return TuringOutput(State.q11, current_s, Move.S)

        case State.q4:
            if current_s == Symbol._:
                return TuringOutput(State.q5, Symbol._, Move.R)
            else:
                return TuringOutput(State.q4, current_s, Move.L)

        case State.q5:
            if current_s == Symbol.a:
                return TuringOutput(State.q6, Symbol.x, Move.L)
            elif current_s in [Symbol.x, Symbol.y, Symbol.b, Symbol.c]:
                return TuringOutput(State.q5, current_s, Move.R)
            elif current_s == Symbol._:
                return TuringOutput(State.q11, Symbol._, Move.S)
            else:
                return TuringOutput(State.q11, current_s, Move.S)

        case State.q6:
            if current_s == Symbol._:
                return TuringOutput(State.q7, Symbol._, Move.R)
            else:
                return TuringOutput(State.q6, current_s, Move.L)

        case State.q7:
            if current_s == Symbol.a:
                return TuringOutput(State.q8, Symbol.x, Move.L)
            elif current_s in [Symbol.x, Symbol.y, Symbol.b, Symbol.c]:
                return TuringOutput(State.q7, current_s, Move.R)
            elif current_s == Symbol._:
                return TuringOutput(State.q11, Symbol._, Move.S)
            else:
                return TuringOutput(State.q11, current_s, Move.S)

        case State.q8:
            if current_s == Symbol._:
                return TuringOutput(State.q1, Symbol._, Move.R)
            else:
                return TuringOutput(State.q8, current_s, Move.L)

        case State.q9:
            if current_s in [Symbol.x, Symbol.y]:
                return TuringOutput(State.q9, current_s, Move.L)
            elif current_s in [Symbol.a, Symbol.b, Symbol.c]:
                return TuringOutput(State.q11, current_s, Move.S)
            elif current_s == Symbol._:
                return TuringOutput(State.q10, Symbol._, Move.S)
            else:
                return TuringOutput(State.q11, current_s, Move.S)

        case State.q10:
            return TuringOutput(State.q10, current_s, Move.S)
        case State.q11:
            return TuringOutput(State.q11, current_s, Move.S)
        case _:
            print(f"Error: Estado no manejado {current_q} en la función delta.")
            return TuringOutput(State.q11, current_s, Move.S)

def print_tape(tape, head, state):
    tape_display = ' '.join(s.value for s in tape)
    head_line = '   ' * head + '↑'
    print(f"\nEstado: {state.value}")
    print(tape_display)
    print(head_line)
    time.sleep(0.2)

def process_string_verbose(string: str) -> bool:
    pos = 0
    tape = [Symbol._] + [Symbol(char) for char in string] + [Symbol._]
    pos = 1
    state = State.q1

    print("\nInicio de la simulación...")
    print_tape(tape, pos, state)

    max_steps = 1000
    step_count = 0

    while state not in [State.q10, State.q11] and step_count < max_steps:
        step_count += 1
        try:
            if pos < 0:
                tape.insert(0, Symbol._)
                pos = 0
            elif pos >= len(tape):
                tape.append(Symbol._)
            
            current_symbol_on_tape = tape[pos]
            output = delta(TuringInput(state, current_symbol_on_tape))

            tape[pos] = output.s
            pos += output.m
            state = output.q
            print_tape(tape, pos, state)

        except Exception as e:
            print(f"Error durante la simulación: {e}")
            state = State.q11
            break
    
    if step_count >= max_steps:
        print("\nLímite de pasos alcanzado. Posible bucle infinito.")
        return False

    if state == State.q10:
        print("\nCadena válida")
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        cadena = input("Ingresa una cadena (solo a, b o c, ENTER para salir): ")
        if not cadena:
            break
        resultado = process_string_verbose(cadena)
        if not resultado:
            print("Cadena inválida")
