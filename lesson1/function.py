def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)
    return one + delimeter + two

result = get_summ("Learn", "python")

print(result)

upper_result = result.upper()
print(upper_result)