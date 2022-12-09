num = int(input("😎Digite um número inteiro:\n>>>"))

print("😎Escolha uma das bases para conversão:")       
print('''
🎂OPÇÕES:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')

opção = int(input("\n😎Escolha a sua opção:\n>>>"))
         
if opção == 1:
    print(f"⭐Valor: {num:.0f};\n⭐Em BINÁRIO: {bin(num)[2:]}!")
elif opção == 2:
    print(f"⭐Valor: {num:.0f};\n⭐Em OCTAL: {oct(num)[2:]}!")
elif opção == 3: 
    print(f"⭐Valor: {num:.0f};\n⭐Em HEXADECIMAL: {hex(num)[2:]}!")
else:
    print("😡VALOR INVÁLIDO!!!")       