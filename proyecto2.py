from sympy import symbols, Not


def DPLL(B, I:dict):

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
            new_clause = {}
            for literal in clause:        
                if literal != Not(L):
                    new_clause[literal] = None
            B_prime.append(new_clause)

    #I’ = I ∪ {valor de L es verdadero}
    I_prime = I.copy()
    I_prime[L] = True

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
            new_clause = {}
            for literal in clause:        
                if literal != L:
                    new_clause[literal] = None
            B_prime.append(new_clause)

    I_prime = I.copy()
    I_prime[L] = False

    result, I2 = DPLL(B_prime, I_prime)

    if result:
        return True, I2
    
    return False, None
    

#ejemplo 1
P,Q,R,S = symbols('P Q R S')
formula1 = [
    {Not(P): None , Not(R): None , Not(S): None}, 
    {Not(Q): None , Not(P): None, Not(S): None}
]

#ejemplo 2
formula2 = [
    {Not(P): None, Not(Q): None},
    {Q: None, Not(S): None},
    {Not(P): None, S: None},
    {Not(Q): None, S: None}
]

#ejemplo 3
formula3 = [
    {Not(P): None, Not(Q): None, Not(R): None},
    {Q: None, Not(R): None, P: None},
    {Not(P): None, Q: None, R: None}
]

#ejemplo 4
formula4 = [
    {R: None},
    {Not(Q): None, Not(R): None},
    {Not(P): None, Q: None, Not(R): None},
    {Q: None}
]

#ejemplo 5
formula5 = [
    {Q: None, P: None, Not(P): None}
]

#ejemplo 6
formula6 = [
    {P: None},
    {Not(P): None}
]

formulaArr = [formula1, formula2, formula3, formula4, formula5, formula6]

for formula in formulaArr:
    print(formula)
    result, assignment = DPLL(formula, {})
    print(result)
    print(assignment)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')