def menu_inicial():
    print("😎Esse é um programa para Conversão de Temperaturas!(C°/F°).")
    
    print("📤Envie 1 para converter de Celsius para Fahrenheit;\n📥Envie 2 para converter de Fahrenheit para Celsius!")
       
def cel_fahr():
    C = float(input("😎Agora digite a temperatura em graus Celsius(ex:30):\n>>>"))
    F = C * (9 / 5) + 32           
    print(f"⚡Convertendo: {C:.2f}°C!\n⭐Valor em Fahrenheit é {F:.2f}°F!")                
def fahr_cel():
    F = float(input("😎Agora digite a temperatura em graus Fahrenheit(ex:120):\n>>>"))
    C = (F - 32) * (5 / 9)         
    print(f"⚡Convertendo: {F:.2f}°F!\n⭐Valor em Celsius é {C:.2f}°C!")                      
if __name__=='__main__':
    menu_inicial()
while True:   
    escolha = float(input("😎Escolha o tipo de conversão que deseja realizar:\n>>>"))   
    if escolha == 1:
        cel_fahr()
        break
    elif escolha == 2:
        fahr_cel()
        break
    else:
        print("😠Valor inválido. Tente novamente!!!") 
        continue