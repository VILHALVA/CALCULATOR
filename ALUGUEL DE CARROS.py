print("😎Irei Calcular para você o valor do aluguel de um carro!")

valor_dia = float(input("😎Me diga, quanto custa o aluguel por dia(R$)?\n>>>"))
valor_km = float(input("😎Me responda, quanto custa um quilômetro rodado(R$)?\n>>>"))

dias = int(input("😎Por quantos dias foi alugado?\n>>>"))
km = float(input("😎Quantos km você andou?\n>>>"))

pagar = (dias * valor_dia) + (km * valor_km)
      
print(f"💰Considerando quê:\n⚡O valor por dia é R${valor_dia:.2f}!\n⚡O valor por km é R${valor_km:.2f}!\n⚡Você usou por {dias} dias!\n⚡Andou com o carro: {km:.2f}km!\n⭐O total a pagar é R${pagar:.2f}!")