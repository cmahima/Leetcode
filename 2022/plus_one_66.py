def plusOne( digits: [int]) -> [int]:
    digits = [str(digit) for digit in digits]
    number = int("".join(digits))

    s = str(number + 1)
    return [int(item) for item in s]

print(plusOne([1,2,3]))