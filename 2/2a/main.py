COLORS = {"red": 12, "green": 13, "blue": 14}
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
posibles = []
for game in games:
    p = True
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
            if n>COLORS[color]:
                p=False
    if p:
        posibles.append(int(game[5:]))
res = 0
for n in posibles:
    res+=n
print(res)