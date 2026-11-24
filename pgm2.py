def logical_shift(bits, n, direction):
    print(f"Original 8-bit number : {bits}")
    for i in range(1, n + 1):
        if direction == "left":
            out, bits = bits[0], bits[1:] + "0"    
        else:
            out, bits = bits[-1], "0" + bits[:-1]   
        print(f"Step {i}: shift {direction:<5} -> {bits}   (bit shifted out: {out})")
    print(f"Final 8-bit result    : {bits}\n")

print("a) Logical left shift of 10110110 by 2")
logical_shift("10110110", 2, "left")
print("b) Logical right shift of 11010100 by 2")
logical_shift("11010100", 2, "right")