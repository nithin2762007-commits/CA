# Computer Architecture (CA) – Binary Arithmetic Programs

Python programs that demonstrate core computer architecture concepts: 8-bit two's complement arithmetic and logical shift operations.

## Programs

| File | Description |
|------|-------------|
| `pgm1.py` | 8-bit signed addition using two's complement, with overflow detection |
| `pgm2.py` | Logical left and right shift on 8-bit binary numbers |

---

## Program 1: Signed Addition (`pgm1.py`)

- Converts decimal numbers to 8-bit two's complement (range -128 to +127)
- Adds bit by bit using ripple-carry addition (LSB to MSB)
- Detects overflow as carry into the sign bit XOR carry out of it, cross-checked against the sign bits
- Verifies each result against normal decimal addition

| Test case | Binary result | Decimal | Overflow |
|-----------|---------------|---------|----------|
| 25 + 18 | `00101011` | 43 | No |
| -25 + -18 | `11010101` | -43 | No |
| 100 + 50 | `10010110` | -106 | Yes |

> **Note:** The `MISMATCH` in the last case is expected. 150 is outside the 8-bit signed range (-128 to +127), so overflow is detected and the result wraps around to -106.

### Output

![Program 1 Output](screenshots/output1.png)
![Program 1 Output](output1.png)

---

## Program 2: Logical Shifts (`pgm2.py`)

- **Logical left shift:** bits move left and 0s fill in from the right
- **Logical right shift:** bits move right and 0s fill in from the left
- Prints every intermediate step and checks the result against manual working

| Operation | Input | Shift | Result |
|-----------|-------|-------|--------|
| Left shift | `10110110` | 2 | `11011000` |
| Right shift | `11010100` | 2 | `00110101` |

### Output

![Program 2 Output](screenshots/output2.png)

---

## How to Run

Requires Python 3.6 or later.

```bash
git clone https://github.com/nithin2762007-commits/CA.git
cd CA
python pgm1.py
python pgm2.py
```

## Concepts Covered

- Two's complement representation
- Ripple-carry binary addition
- Overflow detection in signed arithmetic
- Logical shift operations

## Author

Nithin – AIML, New Horizon College of Engineering
