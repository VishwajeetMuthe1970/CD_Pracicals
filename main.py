ip="192.168.0.1"

binary=[" "]

# print(type(binary))

for x in ip.split("."):

    a=(bin(int(x))[2:])
    binary.append(a)

print(".".join(list(binary))[2:])