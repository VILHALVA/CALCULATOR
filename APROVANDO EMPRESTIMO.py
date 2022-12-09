casa = float(input("😎Qual é o valor da casa(R$)?\n>>>"))
salário = float(input("😎Qual é o valor do seu salário(R$)?\n>>>"))
anos = int(input("😎Quantos anos de financiamento?\n>>>"))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

if prestação <= mínimo:
    resultado = "👍APROVADO"
else:
    resultado = "👎NEGADO"  
       
print(f"⭐Pagar uma casa de R${casa:.2f};\n⭐Com salário de R${salário:.2f};\n⭐Em {anos} anos;\n⭐Prestação será de R${prestação:.2f};\n⭐Valor mínimo R${mínimo:.2f};\n⭐EMPRÉSTIMO:{resultado}!")  