def division(divideBy):
    try:
        return 10/divideBy
    except ZeroDivisionError:
        print('inf', end=' <3 ')

print(division(10))
print(division(5))
print(division(0))
print(division(2))