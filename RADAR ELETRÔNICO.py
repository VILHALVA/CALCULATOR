velocidade = float(input("😎Qual é a velocidade do seu carro?\n>>>"))
limite = float(input("😎Qual é o limite de velocidade?\n>>>"))

if velocidade > limite:
    print(f"😡MULTADO! Você excedeu o limite permitido; Que é {limite:.2f}km/h!!!")
    valor = float(input("😤Para saber quanto você deve pagar, digite o valor da multa(R$) por cada km acima do limite:\n>>>"))
    multa = (velocidade-limite) * valor              
    print(f"⭐Com velocidade do carro: {velocidade:.0f}km/h;\n⭐Sendo o limite de {limite:.0f}km/h;\n⭐Valor da multa por km é: R${valor:.2f};\n⭐Valor a pagar é: R${multa:.2f}!!!")            
else:
    print("😎PARABÉNS!!! Você não excedeu o limite de velocidade!!!")
print("😎Desejo boa sorte!!!")