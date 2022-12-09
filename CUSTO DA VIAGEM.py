distância = float(input("😎Qual é a distância da sua viagem(km)?\n>>>"))
preço = float(input("😎Qual é o preço por km?\n>>>"))        
pagar = distância * preço
               
print(f"⭐Com a distância de {distância:.0f}km;\n⭐Preço por km sendo R${preço:.2f};\n⭐Valor a pagar é R${pagar:.2f}!") 
     
if pagar <= 200:
    print("😎MUITO BOM!!!")
else:
    print("💸QUE ABSURDO!!!")