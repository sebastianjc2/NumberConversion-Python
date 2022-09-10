def dec_to_bin(decStr):
    decNum = int(decStr)
    result = ''
    rem = 0
    while decNum > 0:
        rem = decNum % 2
        decNum = decNum // 2
        result = str(rem) + result
    return result


def dec_to_oct(decStr):
    decNum = int(decStr)
    result = ''
    rem = 0
    while decNum > 0:
        rem = decNum % 8
        decNum = decNum // 8
        result = str(rem) + result
    return result


def num_to_hex_digit(decNum):
    digits = "0123456789ABCDEF"
    if decNum <= 15:
        return digits[decNum]


def dec_to_hex(decStr):
    decNum = int(decStr)
    result = ''
    rem = 0
    if decNum <= 15:
        return num_to_hex_digit(decNum)
    else:
        while decNum > 0:
            rem = decNum % 16
            if rem >= 10: # check
                rem = num_to_hex_digit(rem)
            decNum = decNum // 16
            result = str(rem) + result
        return result


def bin_to_dec(binStr):
    result = 0
    pos = len(binStr) - 1 # start at last pos
    factor = 1
    while pos >= 0:
        val = int(binStr[pos]) * factor
        result = result + val
        pos = pos - 1
        factor = factor * 2
    return result


decNum = input("Enter a base 10 number (decimal system): ")
try:
    decNum = int(decNum)
except:
    print("The number you entered is not a real decimal number.")
    quit()
convertTo = input("Enter the Numeric System to convert it to: ")
if convertTo == 'Binary' or convertTo == 'binary':
    print(dec_to_bin(decNum))
elif convertTo == 'Octal' or convertTo == 'octal':
    print(dec_to_oct(decNum))
elif convertTo == 'Hex' or convertTo == 'hex':
    print(dec_to_hex(decNum))
else:
    print("Not a valid option")

