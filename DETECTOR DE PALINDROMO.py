print("😎Caso não saiba, Palindromo é frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.")

frase = input("😎Digite uma frase:\n>>>").strip().upper()
palavras = frase.split()
junto = "*".join(palavras)
inverso = " "

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    resultado = "👍SIM!!!"
else:
    resultado = "👎NÃO!!!"   
          
print(f"⭐Você inscreveu: {junto}!\n⭐Inverso é {inverso}!\n⭐É Palíndromo?:{resultado}")