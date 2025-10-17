import math

text = input("text: ")
s = {}
for i in text:
    if i not in s:
        s[i] = 1
    else:
        s[i] +=1

fractions = {}

for i in s:
    if s[i] not in fractions:
        fractions[s[i]] = 1
    else:
        fractions[s[i]] +=1

up = {}
down = {}

for i in fractions:
    up[i] = 2 ** math.ceil(math.log(len(text)/i, 2))
    down[i] = 2 ** math.floor(math.log(len(text)/i,2))

addUp = []
addDown = []
for i in fractions:
    addUp.append(int(i*fractions[i] * math.log(up[i], 2)))
    addDown.append(int(i*fractions[i] * math.log(down[i], 2)))

#Print S
print(f"S = {{{', '.join(s.keys())}}}")

#Print P
print(f"P = {{{', '.join([f"{key} = {value}/{len(text)}" for key, value in s.items()])}}}")

#Print Fractions and logarithms
print(f"H(S) = {'+ '.join([f"{key*value}/{len(text)} * lg{len(text)}/{key} " for key, value in fractions.items()])}")

#Printing rounded logarithms
def roundlog(n):
    return f"{'+ '.join([f"{key*value}/{len(text)} * lg{n[key]} " for key, value in fractions.items()])}"
print(f"{roundlog(down)}<= H(S) <= {roundlog(up)}")

#Printing additing fractions
def addFract(n):
    return f"{f'/{len(text)} + '.join(str(i) for i in n)}/{len(text)}"
print(f"{addFract(addDown)} <= H(S) <= {addFract(addUp)}")

#Printing sum of fractions
print(f"{sum(addDown)}/{len(text)} <= H(S) <= {sum(addUp)}/{len(text)}")

#Printing answer
print(f"{math.floor(sum(addDown)/len(text))} <= H(S) <= {math.ceil(sum(addUp)/len(text))}")