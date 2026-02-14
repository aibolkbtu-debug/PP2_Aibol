digit_map = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}
reverse_map = {v: k for k, v in digit_map.items()}
def decode(s):
    number = ""
    for i in range(0, len(s), 3):
        part = s[i:i+3]
        number += digit_map[part]
    return int(number)
def encode(num):
    result = ""
    for digit in str(num):
        result += reverse_map[digit]
    return result
def calculate(expr):
    if '+' in expr:
        left, right = expr.split('+')
        return decode(left) + decode(right)
    elif '-' in expr:
        left, right = expr.split('-')
        return decode(left) - decode(right)
    elif '*' in expr:
        left, right = expr.split('*')
        return decode(left) * decode(right)
s = input()
result = calculate(s)
print(encode(result))
