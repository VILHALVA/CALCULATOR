def main():
    '''
    Programa que lê um dois inteiro positivos n e m e imprime o 
    máximo divisor comum (mdc) de n e m.

    Exemplos de execução

    Digite o valor de n (n > 0): 15
    Digite o valor de m (m > 0): 24
    MDC(15,24)=3

    Digite o valor de n (n > 0): 315
    Digite o valor de m (m > 0): 125
    MDC(315,125)=5

    Digite o valor de n (n > 0): 7
    Digite o valor de m (m > 0): 5
    MDC(7,5)=1
    '''

    print("Determina o mdc de dois números n > 0 e m > 0\n")
    n = int(input("😎Digite o valor de n (n > 0):\n>>>"))
    m = int(input("😎Digite o valor de m (m > 0):\n>>>"))
    
    mdc = n
    while n % mdc != 0 or m % mdc != 0: 
        mdc = mdc - 1

    print(f"⭐MDC de {n} e {m} é {mdc}")

main()

#------------------------------------------------------------------
# 2) Programa simples para calcular o mdc de dois números
#            NÃO usa o algoritmo de Euclides.
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um dois inteiro positivos n e m e imprime o 
    máximo divisor comum (mdc) de n e m.

    Exemplos de execução

    Digite o valor de n (n > 0): 15
    Digite o valor de m (m > 0): 24
    MDC(15,24)=3

    Digite o valor de n (n > 0): 315
    Digite o valor de m (m > 0): 125
    MDC(315,125)=5

    Digite o valor de n (n > 0): 7
    Digite o valor de m (m > 0): 5
    MDC(7,5)=1
    '''
    print("Determina o mdc de dois números n > 0 e m > 0\n")
    
    n = int(input("😎Digite o valor de n (n > 0):\n>>>"))
    m = int(input("😎Digite o valor de m (m > 0):\n>>>"))
    mdc = 1
    
    divisor  = 2 
    while divisor <= n:
        if n % divisor == 0 and m % divisor == 0:
            mdc = divisor
        divisor += 1 

    print(f"⭐MDC de {n} e {m} é {mdc}")
    
main()

#------------------------------------------------------------------
# 3) Calcula o mdc de dois números através do algoritmo de
#            Euclides.
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um dois inteiro positivos n e m e imprime o 
    máximo divisor comum (mdc) de n e m.

    Exemplos de execução:

    Digite o valor de n (n > 0): 15
    Digite o valor de m (m > 0): 24
    MDC(15,24)=3

    Digite o valor de n (n > 0): 315
    Digite o valor de m (m > 0): 125
    MDC(315,125)=5

    Digite o valor de n (n > 0): 7
    Digite o valor de m (m > 0): 5
    MDC(7,5)=1
    '''

    print("Determina o mdc de dois números n > 0 e m > 0\n")
    n = int(input("😎Digite o valor de n (n > 0):\n>>>"))
    m = int(input("😎Digite o valor de m (m > 0):\n>>>"))

    anterior = n
    atual = m
    resto = anterior % atual

    while resto != 0:
        anterior = atual
        atual    = resto
        resto    = anterior % atual
        
    print(f"⭐MDC de {n} e {m} é {atual}")

main()