# Codigo adaptado de de https://davefernig.com/2018/05/07/solving-sat-in-python/
from collections import deque
from itertools import product

def brute_force(expresion):
    cnf = parser(expresion)
    # Se extraen las literales
    literals = set()
    for conj in cnf:
        for disj in conj:
            literals.add(disj[0])
 
    literals = list(literals)
    n = len(literals)
    # Se generan todas las combinaciones posibles de los valores que pueden tener las literales
    for seq in product([1, 0], repeat=n):
        a = set(zip(literals, seq)) # Se combinan las literales con los valores
        # En las disjunciones, se busca que almenos un valor pueda ser verdadero.
        # Luego, se evalua que todas las disjunciones sean verdaderas
        if all([bool(disj.intersection(a)) for disj in cnf]):
            return True, a
 
    return False, None

# convierte a un formato que la función de fuerza bruta pueda entender
def parser(cnf):
    new_cnf = []
    tokens = deque(list(cnf))
    tokens.remove(',')

    open_token = tokens.popleft()
    close_token = tokens.pop()
    if not (open_token == '{' and close_token == '}'):
        print("No se ha ingresado una expresión valida.")
        quit()
    
    while len(tokens) != 0:
        t = tokens.popleft()
        if (t == '{'):
            disj = set()                
            t = tokens.popleft()
            while t != '}':
                if (t == '-'):
                    t = tokens.popleft()
                    literal = (t, 0)
                    disj.add(literal)
                else:
                    literal = (t, 1)
                    disj.add(literal)
                t = tokens.popleft()
            
            new_cnf.append(disj)
    
    return new_cnf

result, assigment = brute_force("{{-p,-r,-s},{-q,-p,-s}}")
print(result)
print(assigment)