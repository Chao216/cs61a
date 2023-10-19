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

linux.extend(['Open SUSE', 'Arch'])

# you may use extends to add mutiple items

print(unixlike)

linux.append('debian')

print(linux)

print(set(linux))

# set doesn't allow duplicated items

phones = ['apple','xiaom','huawei']

print(phones[0] is 'apple')

print(phones[1] == 'xiaom')

print(phones is ['apple','xiaom','huawei']) # becasue object has different hash value// I guess

print(phones == ['apple','xiaom','huawei'])