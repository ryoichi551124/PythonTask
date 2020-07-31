a = {1, 2, 3, 4, 5, 6, 7, 9}
b = {0, 2, 4, 6, 7, 8}

#和集合
c = a | b
print(c)

#差集合
c = a - b
print(c)

#積
c = a & b
print(c)

#排他的論理和
c = a ^ b
print(c)