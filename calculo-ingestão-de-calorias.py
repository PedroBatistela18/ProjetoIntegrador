def usuario():
    idade= int(input('Insira sua idade: '))
    genero = input('Qual seu gênero(homem ou mulher): ')
    peso = int(input('Insira seu peso: '))
    altura = float(input('Insira sua altura: '))

    if genero == 'homem':
        n1 = 66.5
        p = 13.75 * peso
        at = 5.003 * altura
        e = 6.77 * idade
    elif genero == 'mulher':
        n1 = 655.1
        p = 9.56 * peso
        at = 1.85 * altura
        e = 4.68 * idade

    #Calculo-> mulher= 665.1 + (9.56 x p) + (1.85 x cm) – (4.7 x anos) + atividade
    #Calculo-> homem = 66.5 + (13.75 x p) + (5.003 x cm) - (6.77 x anos) + atividade
    calculo_resultado = n1 + at + p - e
    return(int(calculo_resultado))

def calcular_atividade(calculo_resultado):
    atividade_nivel = input('Qual o seu nivel de atividade(leve, moderado, elevada, intensa)?: ')

    if atividade_nivel == 'leve':
        atividade_nivel = (30 * calculo_resultado /100) + calculo_resultado
    elif atividade_nivel == 'moderado':
        atividade_nivel = (50 * calculo_resultado /100) + calculo_resultado
    elif atividade_nivel == 'elevada':
        atividade_nivel = (75 * calculo_resultado /100) + calculo_resultado
    elif atividade_nivel == 'intensa':
        atividade_nivel = (100 * calculo_resultado /100) + calculo_resultado

    return(int(atividade_nivel))


def ganhar_o_perder(atividade_nivel):
    meta = input('Quer perder, manter, o ganhar peso?: ')

    if meta == 'perder':
        kcal = atividade_nivel - 500
    elif meta == 'manter':
        kcal = atividade_nivel
    elif meta == 'ganhar':
        kcal = atividade_nivel + 500



    print('em ordem de ', meta, 'peso, seu consumo diário de calorias deveria ser de', int(kcal), '!')


ganhar_o_perder(calcular_atividade(usuario()))
