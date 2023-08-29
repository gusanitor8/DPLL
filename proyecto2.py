from sympy import symbols, Not


def DPLL(B, I):

    #Si B es vacia, entonces regresar True e I
    if not B:
        return True, I
    
    #Si hay alguna disyuncion vacia en B, entonces regresar False e asignacion vacia o nula
    for clause in B:
        if not clause:
            return False, None
        
    # Seleccionar literal no asignado (en este ejemplo, simplemente el primero)
    L = None
    for clause in B:
        for literal in clause:
            if literal not in I and Not(literal) not in I:
                L = literal if literal.is_Symbol else literal.args[0]
                break
        if L:
            break
    
    #Elimine todas las clausulas que contiene la literal L en B y elimine las ocurrencias
    #en las clausulas de la literal complementaria de L en B, construyendo B’
    B_prime = []
    for clause in B:
        if L not in clause and Not(L) not in clause:
            B_prime.append(clause)            
        elif Not(L) in clause:
            new_clause = set()
            for literal in clause:        
                if literal != Not(L):
                    new_clause.add(literal)
            B_prime.append(new_clause)

    #I’ = I ∪ {valor de L es verdadero}
    I_prime = I.union({L: True})

    #resultado e I1 ← DPLL(B’,I’)
    result, I1 = DPLL(B_prime, I_prime)

    if result:
        return True, I1
    
    #Elimine todas las clausulas que contiene la literal complementaria L en B y elimine
    #las ocurrencias en las clausulas de la literal L en B, construyendo B’
    B_prime = []
    for clause in B:
        if L not in clause and Not(L) not in clause:
            B_prime.append(clause)            
        elif L in clause:
            new_clause = set()
            for literal in clause:        
                if literal != L:
                    new_clause.add(literal)
            B_prime.append(new_clause)

    I_prime = I.union({L: False})

    result, I2 = DPLL(B_prime, I_prime)

    if result:
        return True, I2
    
    return False, None
    


P,Q,R,S = symbols('P Q R S')
formula = [{Not(P) , Not(R) , Not(S)}, {Not(Q) , Not(P), Not(S)}]
result, assignment = DPLL(formula, set())
print(result)
print(assignment)