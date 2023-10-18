linux = ['ubuntu','debian','fedora']

unixlike = linux

print(unixlike)

unixlike.pop()

print(unixlike)
print(linux)

# they point to the same object

unixlike.remove('ubuntu')

print(unixlike)
print(linux)

linux.append('red hat')

print(linux)