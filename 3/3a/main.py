with open("datos.txt", "r") as datos:
    filasAux = datos.readlines()
filas = [len(filasAux[0])*"."]
for fila in filasAux:
    filas.append(fila)
filas.append(len(filasAux[0])*".")
for fila in filas:
    filas[filas.index(fila)] = "." + fila
for fila in filas:
    filas[filas.index(fila)] = fila.replace("\n", ".")

res = 0
n=0
symbols = ["@", "#", "$", "%", "&", "+", "-", "*", "/", "="]
for fila in filas:
    i=0
    for char in fila:
        if char != "."  and not char in symbols:
            n*=10
            n += int(char)
        else:
            if n!=0:
                a = str(n)
                for j in range(i-1-len(a), i+1):
                    if filas[filas.index(fila)+1][j] in symbols or filas[filas.index(fila)-1][j] in symbols or filas[filas.index(fila)][j] in symbols:
                        res+=n
                        n=0
                n=0
        i+=1
print(res)