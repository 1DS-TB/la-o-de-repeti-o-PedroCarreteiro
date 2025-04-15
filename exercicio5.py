numero = int(input("Digite um número: (ele dever ser positivo): "))
if numero == 1:
    print(f"O número {numero} nao eh primo.")
else:
    if numero > 1:
        for i in range(2, numero): #testar números do 2 até o número - 1
            if numero % i == 0:
                print(f"O número {numero} nao eh primo.")
                break
        else:
            print(f"O número {numero} nao eh primo.")
    else:
        print("INVALIDO")
