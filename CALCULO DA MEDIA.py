print("😎Irei calcular as suas 4 notas das provas...")   
nota1 = float(input("😎Digite a sua 1° Nota da prova:\n>>>"))
nota2 = float(input("😎Digite a sua 2° Nota da prova:\n>>>"))
nota3 = float(input("😎Digite a sua 3° Nota da prova:\n>>>"))
nota4 = float(input("😎Digite a sua 4° Nota da prova:\n>>>"))      
média = (nota1 + nota2 + nota3 + nota4) / 4    

print(f"⚡Sua 1° Nota é: ({nota1:.1f});\n⚡Sua 2° Nota é: ({nota2:.1f});\n⚡Sua 3° Nota é: ({nota3:.1f});\n⚡Sua 4° Nota é: ({nota4:.1f});\n⭐A sua MÉDIA é: ({média:.1f})!")    
if 7 > média >= 5:
    print("⭐RESULTADO: Você está de RECUPERAÇÃO!")
elif média < 5:
    print("⭐RESULTADO: Você está REPROVADO!")
elif média >= 7:
    print("⭐RESULTADO: Você está APROVADO!") 