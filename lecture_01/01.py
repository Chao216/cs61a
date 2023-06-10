hamlet = open('hamlet.txt')
text = hamlet.read().split()

print(len(text))

words = set(text)

print(len(words))

print({w for w in words if len(w)==4 and w ==w[::-1]})

print({w for w in words if len(w)==4 and w[::-1] in words})
