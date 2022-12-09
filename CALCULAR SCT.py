import math

print("😎Irei calcular o seno, cosseno e tangente!")
       
ângulo = float(input("😎Digite o ângulo(ex:30):\n>>>"))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
      
print(f"⚡Com ângulo de {ângulo};\n⭐Ângulo do Seno é: {seno:.2f}!\n⭐Ângulo do Cosseno é: {cosseno:.2f}!\n⭐Ângulo da Tangente é: {tangente:.2f}!")   