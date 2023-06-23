EXPONENT_OFFET = 127
PRECISION = 32
MANTISSA = 23
def decimal_to_binary(decimal_num):
    decimal_num = int(decimal_num)
    numbers_binary_format = ""
    is_negative = False
    if decimal_num < 0:
        is_negative = True
        decimal_num = abs(decimal_num)
    while decimal_num > 0:
        remainder = decimal_num % 2
        numbers_binary_format = str(remainder) + numbers_binary_format
        decimal_num = decimal_num // 2
    if is_negative:
        numbers_binary_format = "1" + numbers_binary_format
    else:
        numbers_binary_format = "0" + numbers_binary_format
    return numbers_binary_format


def ones_complement(numbers_binary_format):
    ones_num = ""
    for i in range(len(numbers_binary_format)-1):
        if numbers_binary_format[i+1] == "0":
            ones_num += "1"
        elif numbers_binary_format[i+1] == "1":
            ones_num += "0"
    return ones_num


def binary_summa_resultat(num1, num2):
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    binary_summa_resultat = ""
    carry = 0
    for i in range(max_length - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        summa_resultat_ = digit1 + digit2 + carry
        if summa_resultat_ == 0:
            binary_summa_resultat = "0" + binary_summa_resultat
            carry = 0
        elif summa_resultat_ == 1:
            binary_summa_resultat = "1" + binary_summa_resultat
            carry = 0
        elif summa_resultat_ == 2:
            binary_summa_resultat = "0" + binary_summa_resultat
            carry = 1
        elif summa_resultat_ == 3:
            binary_summa_resultat = "1" + binary_summa_resultat
            carry = 1
    if carry == 1:
        binary_summa_resultat = "1" + binary_summa_resultat
    return binary_summa_resultat


def binary_difference(numbers_binary_format1, numbers_binary_format2):
    if numbers_binary_format1[0] == 1:
        numbers_binary_format1 = twos_complement(numbers_binary_format1)
    elif numbers_binary_format2[0] == 1:
        numbers_binary_format2 = twos_complement(numbers_binary_format2)
    max_len = max(len(numbers_binary_format1), len(numbers_binary_format2))
    numbers_binary_format1 = numbers_binary_format1.zfill(max_len)
    numbers_binary_format2 = numbers_binary_format2.zfill(max_len)
    resultat_of_calculations = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        digit_summa_resultat = carry + int(numbers_binary_format1[i]) - int(numbers_binary_format2[i])
        if digit_summa_resultat == 0:
            resultat_of_calculations = "0" + resultat_of_calculations
            carry = 0
        elif digit_summa_resultat == 1:
            resultat_of_calculations = "1" + resultat_of_calculations
            carry = 0
        elif digit_summa_resultat == 2:
            resultat_of_calculations = "0" + resultat_of_calculations
            carry = 1
        else:
            resultat_of_calculations = "1" + resultat_of_calculations
            carry = 1
    if carry == 1:
        resultat_of_calculations = "1" + resultat_of_calculations
    return resultat_of_calculations


def twos_complement(numbers_binary_format):
    return binary_summa_resultat(ones_complement(numbers_binary_format), "1")


def binary_difference1(num1, num2):
    if len(num1) != len(num2):
        diff = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            num2 = '0' * diff + num2
        else:
            num1 = '0' * diff + num1
    resultat_of_calculations = ''
    carry = 0
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        diff = (digit1 - digit2) - carry
        if diff < 0:
            diff += 2
            carry = 1
        else:
            carry = 0
        resultat_of_calculations = str(diff) + resultat_of_calculations
    resultat_of_calculations = resultat_of_calculations.lstrip('0')
    return resultat_of_calculations if resultat_of_calculations else '0'


def binary_multiply(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    product = [0] * (2 * max_len)
    carry = [0] * (2 * max_len)
    for i in range(max_len-1, -1, -1):
        for j in range(max_len-1, -1, -1):
            if num1[i] == "1" and num2[j] == "1":
                carry[i+j+1] += 1
            product[i+j+1] += int(num1[i]) * int(num2[j])
    for i in range(2*max_len-1, 0, -1):
        carry[i-1] += carry[i] // 2
        carry[i] %= 2
        product[i-1] += carry[i] // 2
    while len(product) > 1 and product[0] == 0:
        product.pop(0)
    product_binary = "".join([str(x) for x in product])
    return product_binary


def binary_division(dividend, divisor, precision=32):
    dividend_str = dividend
    remainder_str = ""
    quotient_str = ""
    point = False
    bits_after_point = 0

    for digit in dividend_str:
        if digit == ".":
            point = True
            continue

        if point:
            bits_after_point += 1

        remainder_str += digit
        remainder_str = remainder_str.lstrip('0')

        if remainder_str == "":
            remainder_str = "0"

        remainder = int(remainder_str, 2)

        if remainder >= int(divisor, 2):
            quotient_str += "1"
            remainder_str = decimal_to_binary(remainder - int(divisor, 2))
        else:
            quotient_str += "0"

        if point:
            bits_after_point -= 1

        if bits_after_point == -precision:
            break

    if point and bits_after_point > 0:
        quotient_str += "0" * bits_after_point

    remainder = int(remainder_str, 2)
    remainder_str = decimal_to_binary(remainder)
    while(len(remainder_str) < 5):
        remainder_str = '0' + remainder_str
    return quotient_str + "." + remainder_str



def float_to_binary(num):
    if num == 0:
        return '0'*PRECISION

    # extract sign bit
    sign = '0'
    if num < 0:
        sign = '1'
        num = -num

    # extract exponent and mantissa
    exponent = 0
    while num >= 2:
        exponent += 1
        num /= 2
    while num < 1:
        exponent -= 1
        num *= 2
    exponent += EXPONENT_OFFET
    mantissa = num - 1

    # convert exponent to binary
    exponent_bits = bin(exponent)[2:].zfill(8)

    # convert mantissa to binary
    mantissa_bits = ''
    for i in range(MANTISSA):
        mantissa *= 2
        if mantissa >= 1:
            mantissa_bits += '1'
            mantissa -= 1
        else:
            mantissa_bits += '0'

    # combine sign, exponent, and mantissa into binary string
    return sign + exponent_bits + mantissa_bits


def add_floats(a, b):
    # Extract the sign, exponent, and mantissa from each binary representation
    a_sign = int(a[0])
    a_exp = int(a[1:9], 2) - EXPONENT_OFFET
    a_mant = int(a[9:], 2) / (2 ** MANTISSA) + 1
    b_sign = int(b[0])
    b_exp = int(b[1:9], 2) - EXPONENT_OFFET
    b_mant = int(b[9:], 2) / (2 ** MANTISSA) + 1

    # Calculate the new exponent for the summa_resultat
    exp_diff = abs(a_exp - b_exp)
    if a_exp > b_exp:
        b_mant /= 2 ** exp_diff
        summa_resultat_exp = a_exp
    else:
        a_mant /= 2 ** exp_diff
        summa_resultat_exp = b_exp

    # Add the two mantissas and normalize the summa_resultat
    summa_resultat_mant = a_mant + b_mant
    if summa_resultat_mant >= 2:
        summa_resultat_mant /= 2
        summa_resultat_exp += 1
    summa_resultat_mant_bits = '{0:b}'.format(int((summa_resultat_mant - 1) * 2 ** MANTISSA)).zfill(MANTISSA)
    summa_resultat_exp_bits = '{0:b}'.format(summa_resultat_exp + EXPONENT_OFFET).zfill(8)
    summa_resultat_bits = '0' + summa_resultat_exp_bits + summa_resultat_mant_bits

    # Return the summa_resultat as a binary string
    return summa_resultat_bits


num1 = int(input("Enter the first decimal number: "))
num2 = int(input("Enter the second decimal number: "))

numbers_binary_format1 = decimal_to_binary(num1)
numbers_binary_format2 = decimal_to_binary(num2)
print("Binary representation of", num1, "is", numbers_binary_format1)
print("Binary representation of", num2, "is", numbers_binary_format2)
print("The summa_resultat of", num1, "and", num2, "in binary is", binary_summa_resultat(numbers_binary_format1, numbers_binary_format2))
print("The difference of", num1, "and", num2, "in binary is", binary_difference1(numbers_binary_format1,numbers_binary_format2))
print("The multiplication of", num1, "and", num2, "in binary is", binary_multiply(numbers_binary_format1, numbers_binary_format2))
print("The division of", num1, "and", num2, "in binary is", binary_division(numbers_binary_format1, numbers_binary_format2))
print(add_floats(float_to_binary(6.25), float_to_binary(0.75)))
