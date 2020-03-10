def fab(max):
    n, a, b = 0, 0, 1
    list = []
    while n < max:
        list.append(b)
        a, b =  b ,a+b
        n += 1
    return list

l = fab(5)
print(l[:])
print(" " .join(l))


"""

    while n < max:
        print (b)
        a, b = b, a + b
        n = n + 1
"""




