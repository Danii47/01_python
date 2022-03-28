#!/usr/bin/python

# Funcion suma

def suma(x, y):
    if isinstance(x, int) == True and isinstance(y, int) == True:
        return x + y

result = suma(2, 3)
print(result)