import datetime

atual = datetime.date.today().year
sexo = input("😎Qual é o seu sexo[M/F]?:\n>>>").strip().upper()[0]

while sexo not in "MmFf":
    sexo = input("😬Dados inválidos!!!\n😠Por favor, informe seu sexo[M/F]:\n>>>").strip().upper()[0]     
if sexo == "M":
    nasc = int(input("😎Digite o ano do seu nascimento:\n>>>"))
    idade = atual - nasc           
    if idade == 18:
        resultado = "⭐Tem que se alistar imediatamente!"
    elif idade < 18:
        saldo = 18 - idade 
        ano = atual + saldo
        resultado = f"⭐Faltam {saldo:.0f} anos para o alistamento!\n⭐Seu alistamento será em {ano:.0f}!"
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        resultado = f"⭐Deveria ter se alistado há {saldo:.0f} anos!\n⭐Seu alistamento foi em {ano:.0f}!"        
    print(f"⭐Para quem nasceu em {nasc:.0f};\n⭐Tem {idade:.0f} anos em {atual:.0f};\n{resultado}")     
elif sexo == "F":
    print("😔Sinto muito!!! Em nosso país só é permitido homens!!!")
else:
    print("😡Não compreendo!!!")