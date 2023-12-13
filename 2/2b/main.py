COLORS = ["red", "green", "blue"]
with open("datos.txt", "r") as datos:
    strings = datos.readlines()
games = {}
for string in strings:
    if string[6] == ":":
        games["Game " + str(strings.index(string)+1)] = string[8:len(string)-1]
    if string[7] == ":":
        games["Game " + str(strings.index(string)+1)] = string[9:len(string)-1]
    if string[8] == ":":
        games["Game " + str(strings.index(string)+1)] = string[10:]
for game in games:
    games[game] = games[game].split("; ")
powers = []
for game in games:
    r = 0
    g = 0
    b = 0
    for grab in games[game]:
        for color in COLORS:
            n = 0
            try:
                n += int(grab[grab.find(color)-2])
                try:
                    n += 10*int(grab[grab.find(color)-3])
                except ValueError:
                    pass
            except ValueError:
                pass
            if color=="red" and n>r:
                r=n
            if color=="green" and n>g:
                g=n
            if color=="blue" and n>b:
                b=n
    powers.append(r*g*b)
res = 0
for n in powers:
    res+=n
print(res)