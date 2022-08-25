#Programa que escreve em um arquivo

arquivo = open("dados.txt", "w")
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