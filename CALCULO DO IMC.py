print("😎Agora irei calcular o seu IMC (Índice de massa corporal),para saber se você está em forma.")     
   
altura = float(input("😎Digite sua altura em metros:\n>>>"))
peso = float(input("😎Digite o seu peso em Kg:\n>>>")) 
     
imc = peso / altura ** 2       

print(f"⚡Seu Peso é: ({peso:.2f})!\n⚡Sua altura é: ({altura:.2f})!\n⭐Seu IMC é {imc:.2f}!")  
     
if imc < 16:
    print("⭐RESULTADO: Seu estado é magreza grave!")
elif imc < 17:
    print("⭐RESULTADO: Seu estado é magreza moderada!")
elif imc < 18.5:
    print("⭐RESULTADO: Seu estado é magreza leve!")
elif imc < 25:
    print("⭐RESULTADO: Você é Saudável!")
elif imc < 30:
    print("⭐RESULTADO: Sobrepeso!")
elif imc < 35: 
    print("⭐RESULTADO: Obesidade Grau I!")
elif imc < 40:
    print("⭐RESULTADO: Obesidade Grau II!")
else:
    print("⭐RESULTADO: Obesidade Grau III!")   