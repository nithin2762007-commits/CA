def to_bin(n):
    return format(n & 0xFF, "08b")
def to_dec(b):
    n = int(b, 2)
    return n - 256 if b[0] == "1" else n
def add(x, y):
    a, b = to_bin(x), to_bin(y)
    total = int(a, 2) + int(b, 2)
    result = format(total & 0xFF, "08b")
    overflow = a[0] == b[0] and result[0] != a[0]

    print(f"({x}) + ({y})")
    print("Operand 1 :", a)
    print("Operand 2 :", b)
    print("Binary    :", result)
    print("Decimal   :", to_dec(result))
    print("Overflow  :", "YES" if overflow else "NO")
    print()


add(25, 18)
add(-25, -18)    