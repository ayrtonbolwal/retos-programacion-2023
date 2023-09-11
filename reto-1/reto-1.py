x = range(1, 101)
listaNumeros = list(x)

for n in listaNumeros:
    mod_3 = n%3
    mod_5 = n%5

    if(mod_3 == 0 and mod_5 == 0):
        print("fizzbuzz")
    elif(mod_3 == 0 and mod_5 != 0):
        print("fizz")
    elif(mod_5 == 0 and mod_3 != 0):
        print("buzz")
    else:
        print(n)
