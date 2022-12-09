print("😎Agora vamos calcular o seu aumento...")

preço = float(input("😎Digite o seu valor original(R$):\n>>>"))
aumento = float(input("😎Digite o seu aumento(%):\n>>>"))

pagar = preço + (preço * aumento / 100)  

print(f"⚡Preço de R${preço:.2f}!\n⚡Com um aumento de {aumento:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")   