#! /usr/bin/python3
# boxPrint.py - files and paths

def boxPrint(symbol, width, height):
    if width <= 2:
        raise Exception('Width must be grater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) * len(symbol) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('gfdsg', 12, 11)):
    assert len(sym) == 1, 'Symbol must be a single character string.'
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happenened; ' + str(err))