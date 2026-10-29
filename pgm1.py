BITS = 8
MASK = (1 << BITS) - 1          # 0xFF
MIN_VAL = -(1 << (BITS - 1))    # -128
MAX_VAL = (1 << (BITS - 1)) - 1  # +127
 
 
def to_twos(n):
    """Decimal -> 8-bit 2's complement bit string."""
    if not MIN_VAL <= n <= MAX_VAL:
        raise ValueError(f"{n} is outside the 8-bit range [{MIN_VAL}, {MAX_VAL}]")
    if n >= 0:
        return format(n, f"0{BITS}b")
    # Manual method for negatives: invert the magnitude's bits, then add 1
    magnitude = format(-n, f"0{BITS}b")
    inverted = "".join("1" if b == "0" else "0" for b in magnitude)
    return format((int(inverted, 2) + 1) & MASK, f"0{BITS}b")
 
 
def from_twos(bits):
    """8-bit 2's complement bit string -> decimal."""
    value = int(bits, 2)
    return value - (1 << BITS) if bits[0] == "1" else value
 
 
def add_binary(a_bits, b_bits):
    """
    Bit-by-bit ripple-carry addition of two 8-bit strings.
    Returns (sum_bits, carry_into_msb, carry_out_of_msb).
    """
    carry = 0
    result = [""] * BITS
    carry_into_msb = 0
    for i in range(BITS - 1, -1, -1):          # LSB -> MSB
        if i == 0:
            carry_into_msb = carry              # carry entering the sign bit
        total = int(a_bits[i]) + int(b_bits[i]) + carry
        result[i] = str(total % 2)
        carry = total // 2
    return "".join(result), carry_into_msb, carry
 
 
def signed_add(x, y):
    a, b = to_twos(x), to_twos(y)
    s, c_in, c_out = add_binary(a, b)
    # Overflow rule: carry into the sign bit XOR carry out of the sign bit
    overflow_flag = (c_in != c_out)
    # Cross-check using the sign bits (operands same sign, result differs)
    overflow_sign = (a[0] == b[0]) and (s[0] != a[0])
    assert overflow_flag == overflow_sign
    return a, b, s, from_twos(s), c_in, c_out, overflow_flag
 
 
def show(label, x, y):
    a, b, s, dec, c_in, c_out, ovf = signed_add(x, y)
    print("=" * 56)
    print(f"{label}: ({x}) + ({y})")
    print("=" * 56)
    print(f"Operand 1 : {x:>4}  ->  {a}")
    print(f"Operand 2 : {y:>4}  ->  {b}")
    print(f"            {'':>4}      {'-' * BITS}")
    print(f"Result    : binary  = {s}")
    print(f"            decimal = {dec}")
    print(f"Carry into MSB = {c_in}, carry out of MSB = {c_out}")
    print(f"Overflow  : {'YES' if ovf else 'NO'}")
    expected = x + y
    print(f"Verification: expected {expected}, got {dec} -> "
          f"{'MATCH' if expected == dec else 'MISMATCH'}")
    print()
 
 
if __name__ == "__main__":
    show("a", 25, 18)
    show("b", -25, -18)
    # Extra demo (optional): a case that does overflow
    show("extra", 100, 50)
 