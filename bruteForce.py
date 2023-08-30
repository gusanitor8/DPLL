def convert2Boolean(clausal, exp="",level=0):
    if(type(clausal[0])!=list):
        if(clausal[0]=="¬"):
            i+=1
            exp+="¬"+str(clausal[0])
        else:
            exp+=""+str(clausal[0])
    else:
        exp+="("+convert2Boolean(clausal[0],exp,level+1)+")"
    for i in range(1,len(clausal)):
        if (type(clausal[i])==(list)):
            if(level%2==0):
                exp+="^("+convert2Boolean(clausal[i],"",level+1)+")"
            else:
                exp+="V("+convert2Boolean(clausal[i],"",level+1)+")"
        else:
            if(level%2==0):
                if(clausal[i]=="¬"):
                    i+=1
                    exp+="^¬"+str(clausal[i])
                else:
                    exp+="^"+str(clausal[i])
            else:
                if(clausal[i]=="¬"):
                    i+=1
                    exp+="V¬"+str(clausal[i])
                else:
                    exp+="V"+str(clausal[i])
    return exp
def getSymbols(clausal):
    if (len(clausal)==0):
        return True
    symbols = []
    for x in range(0,len(clausal)):
        if (clausal[x] == ")" or clausal[x] == "(" or clausal[x] == "^" or clausal[x] == "V" or clausal[x]=="¬"):
            pass
        elif (clausal[x] not in symbols):
            symbols.append(clausal[x])
    val = len(symbols)
    symb = []
    for k in range(0,val):
        symb.append((symbols[k],"¬"+symbols[k]))
    return symb
def bruteForce(clausal):
    print("Formula clausal: "+str(clausal))
    clausalBool = convert2Boolean(clausal)
    symbols = getSymbols(clausalBool)
    num_symbols = len(symbols)
    combinations = []
    print("Formula booleana: "+clausalBool)
    for i in range(2 ** num_symbols):
        combination = [(i >> j) & 1 == 1 for j in range(num_symbols)]
        combinations.append(combination)
    result = []
    for combination in combinations:
        assignment = []
        for i, (symbol, negation) in enumerate(symbols):
            assignment.append((negation, not combination[i]))
            assignment.append((symbol, combination[i]))
        result.append(assignment)
    for x, arr in enumerate(result):
        temp = clausalBool
        temp = temp.replace("^", " and ")
        temp = temp.replace("V", " or ")
        for y in arr:
            temp = temp.replace(y[0], str(y[1]))
        if (eval(temp)):
            return True, arr, temp
    return False,[],[]

    
            
array = ["¬P","S",["P","Q",["¬S","¬P","S","P","Q"]]]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
array = ["P","¬P"]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
array = [["Q","P","¬P"]]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
array = [["P","¬Q"],["Q","¬S"],["¬P","S"],["¬Q","S"]]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
array = [["¬P","¬Q","¬R"],["Q","¬R","P"],["¬P","Q","R"]]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
array = [["R"],["¬Q","¬R"],["¬P","Q","¬R"],["Q"]]
vals = bruteForce(array)
print("Resultado: "+str(vals[0]))
print("Asignacion: "+str(vals[1]))
print("Aplicacion: "+str(vals[2]))
print("-------------------------------------------------------------------------------------------------")
