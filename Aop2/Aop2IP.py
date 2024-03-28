# Iniciando as variáveis de contagem
alunos = 0
aprovados = 0
reprovados = 0

# Recebendo as notas de cada aluno, calculando a média do modulo e exibindo o seu status

while alunos < 5:          # Alterar a quantidade para 100
    try:
        print(f'Nota da AOP1 do {alunos+1}° Aluno [Entre O e 1]:', end=' ')
        aop1 = float(input())
        while aop1 < 0 or aop1 > 1:
            print('Nota Inválida. Insira uma nota entre O e 1:', end=' ')
            aop1 = float(input())

        print(f'Nota da AOP2 do {alunos+1}° Aluno [Entre 0 e 2]:', end=' ')
        aop2 = float(input())
        while aop2 < 0 or aop2 > 2:
            print('Nota Inválida. Insira uma nota entre O e 2:', end=' ')
            aop2 = float(input())

        print(f'Nota da AOP3 do {alunos+1}° Aluno [Entre 0 e 1]:', end=' ')
        aop3 = float(input())
        while aop3 < 0 or aop3 > 1:
            print('Nota Inválida. Insira uma nota entre O e 1:', end=' ')
            aop3 = float(input())

        print(f'Nota da Prova Regular do {alunos+1}° Aluno [Entre O e 6]:', end=' ')
        provaReg = float(input())
        while provaReg < 0 or provaReg > 6:
            print('Nota Inválida. Insira uma nota entre O e 6:', end=' ')
            provaReg = float(input())

        mm = aop1 + aop2 + aop3 + provaReg       # Calculando a média do módulo
        if mm >= 7:
            print(f'Aluno APROVADO. Média do Módulo: {round(mm, 1)}')
            print('')
            aprovados += 1
        else:
            print(f'Aluno de RECUPERAÇÃO. Média do Módulo: {round(mm, 1)}')
            print(f'Nota da Prova de Recuperação do {alunos+1}° Aluno [Entre 0 e 10]:', end=' ')
            provaRep = float(input())
            while provaRep < 0 or provaRep > 10:
                print('Nota inválida. Insira uma nota entre 0 e 10:', end=' ')
                provaRep = float(input())

            mg = (mm + provaRep)/2          # Calculando a média geral
            if mg >= 5:
                print(f'Aluno APROVADO. Média geral: {round(mg, 1)}')
                print('')
                aprovados += 1
            else:
                print(f'Aluno REPROVADO. Média Geral: {round(mg, 1)}')
                print('')
            reprovados += 1
        alunos += 1

    except ValueError:
        print('ERRO! INSIRA UM VALOR VÁLIDO!')
        print('')

# Informando o percentual de alunos aprovados e reprovados
tot_alunos = aprovados + reprovados
if tot_alunos > 0:
    perApr = (aprovados / tot_alunos) * 100
    perRep = (reprovados / tot_alunos) * 100
    print(f'Percentual de Alunos Aprovados: {perApr:.1f}%')
    print(f'Percentual de Alunos Reprovados: {perRep:.1f}%')
else:
    print('Nenhum aluno foi avaliado.')         # Caso nenhum aluno seja avaliado.
