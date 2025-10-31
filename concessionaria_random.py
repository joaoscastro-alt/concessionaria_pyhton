import random
'''
idade = random.randint(1, 99)

if idade >= 18:
    print("Seja bem vindo! Vou apresentar nosso melhores veículos.")
else:
    print("Seja bem vindo! Vou levá-lo para o espaço kids.")
'''

idade = random.randint(-10, 120)
print(idade)

if idade <= 0 or idade > 100:
    print("ERRO")
else:
    if idade >= 18:
        print("Seja bem vindo! Vou apresentar nosso melhores veículos.")
    else:
        print("Seja bem vindo! Vou levá-lo para o espaço kids.")