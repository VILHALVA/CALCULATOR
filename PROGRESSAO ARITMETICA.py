n = int(input("😎Digite o valor:\n>>>"))
r = int(input("😎Digite a razão:\n>>>"))

termo = n
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"⭐{termo}›", end= "")    
        termo += r
        cont += 1
    print("\n⛔PAUSA!!!")
    mais = int(input("😎Quantos termos você quer mostrar a mais?\n😎Digite 0 caso queira parar:\n>>>"))
    
print(f"⛔FINALIZADO COM TOTAL {total} TERMOS!") 