import math

text = input("text: ")
s = {}
for i in text:
    if i not in s:
        s[i] = 1
    else:
        s[i] +=1

ulamki = {}

for i in s:
    if s[i] not in ulamki:
        ulamki[s[i]] = 1
    else:
        ulamki[s[i]] +=1

up = {}
down = {}

for i in ulamki:
    up[i] = 2 ** math.ceil(math.log(len(text)/i, 2))
    down[i] = 2 ** math.floor(math.log(len(text)/i,2))

addUp = []
addDown = []
for i in ulamki:
    addUp.append(i*ulamki[i] * math.log(up[i], 2))
    addDown.append(i*ulamki[i] * math.log(down[i], 2))

#Print S
print(f"S = {{{', '.join(s.keys())}}}")
#Print P
print(f"P = {{{', '.join([f"{key} = {value}/{len(text)}" for key, value in s.items()])}}}")