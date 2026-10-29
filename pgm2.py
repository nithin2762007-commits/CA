def logical_left_shift(value: str, positions: int) -> str:
	result = value
	print(f"Original 8-bit number: {value}")
	for step in range(1, positions + 1):
		result = (result[1:] + "0")[-8:]
		print(f"After left shift {step}: {result}")
	return result


def logical_right_shift(value: str, positions: int) -> str:
	result = value
	print(f"Original 8-bit number: {value}")
	for step in range(1, positions + 1):
		result = ("0" + result[:-1])[-8:]
		print(f"After right shift {step}: {result}")
	return result


if __name__ == "__main__":
	print("a) Logical left shift of 10110110 by 2 positions")
	left_result = logical_left_shift("10110110", 2)
	print(f"Final 8-bit result: {left_result}")
	print("Manual verification: 10110110 -> 01101100 -> 11011000")
	print(f"Verified: {left_result == '11011000'}\n")

	print("b) Logical right shift of 11010100 by 2 positions")
	right_result = logical_right_shift("11010100", 2)
	print(f"Final 8-bit result: {right_result}")
	print("Manual verification: 11010100 -> 01101010 -> 00110101")
	print(f"Verified: {right_result == '00110101'}")
