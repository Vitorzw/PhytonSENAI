n = int(input('solicite um numero'))
quant = 0
print(n)
while True:
    n = n - 1
    if n % 2 == 0:
        print(n)
        quant = quant + 1
       
    elif n <= 0:
        print('a quantidade de pares é ', quant+1 )
       
        break 

     
     
     
     
     


