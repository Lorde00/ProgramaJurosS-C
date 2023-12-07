def juros_composto(a,b):

    montante = a * (1 + (b / 100)) ** b
    vpcj = montante / b
    jbc = montante - a
    valorparcelascomjuros.append(vpcj)
    jurosbruto.append(jbc)
    return montante

def juros_simples(a,b):
    vp = (a / b)
    return f'O valor total de cada parcela é de: R${vp}'
        
valorparcelascomjuros = []
jurosbruto = []

print(f'O juros calculado no programa é de 12% ao ano! ')
                                                                                                                                                                                              
while True:
    vt = float(input('Digite o valor total da compra sem o juros: '))
    
    par = float(input('Digite a quantidade de parcelas totais: '))      
    
    com = str(input('A sua compra possui juros [S/N]? ')).upper()
    
    if com == 'S':
        print(f'O valor total com juros é de: R${round(juros_composto(vt,par),2)}')
        print(f'O valor total de cada parcela com juros é de: R${round(valorparcelascomjuros[0],2)}')
        print(f'O valor total do juros bruto é de: R${round(jurosbruto[0],2)}')
    else:
        print(f'O valor total é de: R${round(vt),2}')
        print(f'A quantidade total de parcelas é de: {round(par,0)}')
        print(round(juros_simples(vt,par),2))    

           
    continuar = str(input('Deseja calcular o valor de outra compra [S/N]? ')).upper()
    match continuar: 
        case 'N':
            print('Obrigado por utilizar o programa! ')
            break
                                           
        
    
        
        