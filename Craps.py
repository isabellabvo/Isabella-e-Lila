import random as rnd
fichas = 50
a = input('Você quer apostar? s/n ')
b = input('Qual tipo de aposta você quer fazer? (plb, f, ac, t) ')
#aposta = int(input('Quanto você quer apostar? '))
fase = ['Come out' , 'Point']
Point =  0

while fichas > 0:
    if fichas == 0:
        break
    if a == 'n':
        break
    while a == 's':
        dado1 = rnd.randint(1,6)
        dado2 = rnd.randint(1,6)
        soma = dado1 + dado2
        aposta = int(input('Quanto você quer apostar? '))


        if b == 'plb':

            if soma == 7 or soma == 11:
                print(fase[0])
                fichas += aposta
                print(fichas)
                print("você ganhou essa aposta. ")
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            elif soma == 2 or soma ==3 or soma == 12:
                fichas -= aposta
                print(fichas)
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            else:
                Point == fase[1]
                print(fase[1])
                dado1 = rnd.randint(1,6)
                dado2 = rnd.randint(1,6)
                nova_soma = dado1 + dado2
                
                if nova_soma == soma:
                    fichas += aposta
                    print(fichas)
                    a = str(input('Gostaria de apostar novamente? s/n '))
                    b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            
                elif nova_soma == 7:
                    fichas = 0
                    print(fichas)

                else:
                    dado1 = rnd.randint(1,6)
                    dado2 = rnd.randint(1,6)
                    ultima_soma = dado1 + dado2
                    if ultima_soma !=7 or nova_soma != ultima_soma:
                        dado1 = rnd.randint(1,6)
                        dado2 = rnd.randint(1,6)
                        ultima_soma = dado1 + dado2
                        print("Point")

                    if ultima_soma == 7:
                        fichas = 0
                    else:
                        fichas += aposta

                        print(fichas) 
                        a = str(input('Gostaria de apostar novamente? s/n '))
                        b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))



        if b == 'f':
            if  5 <= soma <= 8:
                fichas = 0
            elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                fichas += aposta
                print('Você venceu a aposta!')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            elif soma == 2:
                fichas += 2* aposta
                print('Você venceu a aposta!')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            else:
                fichas += 3* aposta
                print("Você ganhou a aposta")
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
                if b == 'ac':
            if soma == 2 or soma == 3 or soma == 12:
                fichas += 7* aposta
                print('Você ganhou a aposta')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Que tipo de aposta?"))
            else:
                fichas -= aposta
                print('Você perdeu a aposta')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))

        if b == 't':
            if soma == 12:
                fichas += 30 * aposta
                print('Você venceu a aposta!')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))
            else:
                fichas -= aposta
                print('Você perdeu a aposta')
                a = str(input('Gostaria de apostar novamente? s/n '))
                b = str(input("Qual tipo de aposta você quer fazer? (plb, f, ac, t)"))

