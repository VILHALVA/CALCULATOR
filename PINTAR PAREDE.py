print("🌝Irei fazer o cálculo para descobrir a quantidade de litros de tinta para você pintar a sua parede!")

base = float(input("😎Digite a largura da parede(m):\n>>"))
altura = float(input("😎Digite a altura da parede(m):\n>>>"))

área = base * altura
tinta = área / 2
        
print(f"⚡Sua dimensão é ({base:.0f})m × ({altura:.0f})m!\n⚡Para pintar a parede de {área:.0f}m²;\n⭐Precisará usar {tinta:.2f}L de tinta!")