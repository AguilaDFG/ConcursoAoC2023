with open("datos.txt", "r") as datos:
    filasAux = datos.readlines()
filas = [len(filasAux[0])*"."]
for fila in filasAux:
    filas.append(fila)
filas.append(len(filasAux[0])*".")
for fila in filas:
    filas[filas.index(fila)] = "." + fila

res = 0
n=0
symbols = ["@", "#", "$", "%", "&", "+", "-", "*", "/", "=", ".", "\n"]
for fila in filas:
    i=0
    for char in fila:
        if char == "*":
            nums = []
            for j in range(-1,2):
                k = -1
                while k<2:
                    if not filas[filas.index(fila) + j][i+k] in symbols:
                        n = int(filas[filas.index(fila) + j][i+k])
                        l = 1
                        while not filas[filas.index(fila) + j][i+k-l] in symbols:
                            n += int(filas[filas.index(fila) + j][i+k-l])*(10**l)
                            l+=1
                        l = 1
                        while not filas[filas.index(fila) + j][i+k+1] in symbols:
                            n*=10
                            n += int(filas[filas.index(fila) + j][i+k+l])
                            k+=1
                        nums.append(n)
                    k+=1
            if len(nums) == 2:
                res += nums[0]*nums[1]
        i+=1
print(res)