#Programa que escreve em um arquivo
try:
    arquivo = open("data/dados.txt", "a")
    continuar = True

    while continuar:
        #time é str
        time = input("Time (vazio para sair):")
        #TODA STR VAZIA E FALSA
        #Entra no if se a string está vazia
        if not time:
            continuar = False
            continue
        arquivo.write(time+'\n')
    arquivo.close()
except FileNotFoundError:
    print("Arquivo ou diretório não encontrado!")
except ZeroDivisionError:
    print("Alguém tentou dividir por 0!")
except:
    print("Algo de errado aconteceu!")
finally:
    print("Enfim terminou!")