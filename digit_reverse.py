def digit_reverse(digit_value):
    rev_digit = ""
    if digit_value[0] == "-":
        digit_value = digit_value[1:len(digit_value)]
        rev_digit += "-"
    for i in range(len(digit_value)):
        rev_digit += digit_value[len(digit_value)-i-1]
    return rev_digit
