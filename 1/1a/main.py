with open("datos.txt", "r") as datos:
    strings = datos.readlines()
nums = []
for string in strings:
    j = True
    k = True
    n = 0
    for i in range (0, len(string)):
        if k:
            try:
                dig1 = int(string[i])
                n+=(10*dig1)
                k=False
            except ValueError:
                pass
        if j:
            try:
                dig1 = int(string[len(string)-i-1])
                n+=dig1
                j=False
            except ValueError:
                pass
    nums.append(n)
res = 0
for n in nums:
    res+=n
print(res)