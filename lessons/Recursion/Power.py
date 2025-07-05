def Power(base,exponent):
    if exponent == 1:
        return base
    else:
        return base * Power(base,exponent - 1)

def PowerIteration(base,exponent):
    result = 1

    while exponent > 0:
        result *= base
        exponent -= 1

    return result

print(Power(4,3))
print(PowerIteration(4,3))