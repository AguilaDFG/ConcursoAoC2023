with open("datos.txt", "r") as datos:
    strings = datos.readlines()
nums = []
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for string in strings:
    pos = []
    for dig in digits:
       pos.append(string.find(dig))
    rpos = []
    for dig in digits:
       rpos.append(string.rfind(dig))
    j = True
    k = True
    n = 0
    for i in range (0, len(string)):
        if k:
            try:
                a = i
                dig1 = int(string[a])
                for p in pos:
                    if p<a and p>=0:
                        dig1 = pos.index(p)
                        a = p
                n+=(10*dig1)
                k=False
            except ValueError:
                pass
        if j:
            try:
                b = len(string)-i-1
                dig2 = int(string[b])
                for p in rpos:
                    if p>b:
                        dig2 = rpos.index(p)
                        b = p
                n+=dig2
                j=False
            except ValueError:
                pass
    nums.append(n)
res = 0
for n in nums:
    res+=n
print(res)