import datetime

ano = int(input("😎Que ano você quer analisar?\n🌚Envie 0 para analisar o ano atual:\n>>>"))  
      
if ano == 0:
    ano = datetime.date.today().year
            
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"⭐ANO {ano}!\n⭐BISSEXTO:👍SIM!\n⭐FEVEREIRO: ➕29 DIAS!")
else:
    print(f"⭐ANO {ano}!\n⭐BISSEXTO:👎NÃO!\n⭐FEVEREIRO: ➖28 DIAS!") 