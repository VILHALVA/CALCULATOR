print("😎Agora vamos calcular o seu desconto...")

preço = float(input("😎Digite o seu valor original(R$):\n>>>"))
desconto = float(input("😎Digite o seu desconto(%):\n>>>"))

pagar = preço - (preço * desconto / 100)   

print(f"⚡Preço de R${preço:.2f}!\n⚡Com um desconto de {desconto:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!") 