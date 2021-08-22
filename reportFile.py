#Datetime é um pacote de funções focado em captura e operações com o tempo.
from datetime import datetime
import xlsxwriter as xw

#A funcão EscreveXls vai escrever uma versão tabelada dos dados coletados
def EscreveXls(emotion, nEmotion, tEmotion, totalEmotion):
    row_n = 0
    col_n = 0
    workbook = xw.Workbook(emotion)
    wsEmotion = workbook.add_worksheet(name = emotion)
    wsEmotion.write('A1','Numero de Detecções')
    wsEmotion.write('B1', 'Momento de Detecção')
    for row_n in range (totalEmotion):
        wsEmotion.write(row_n + 1, col_n, nEmotion[row_n])
        wsEmotion.write(row_n + 1, col_n + 1, tEmotion[row_n])
        row_n +=1

    workbook.close()

#Função que escreve emoções detectadas no arquivo e no terminal.
def EscrevendoEmotions(emotions, nEmotion):

    #Escrita das emoções no terminal.
    print("Emoção Detectada: ",emotions )#DEBUG

    #Now é uma variavel com objetivo de armazenar o momento.
    #de detecção da emoção. Realizado através da função:datetime.now()
    now = datetime.now()
    #convertes-se o tempo em hora:minuto:segundo
    momentoEmotion = now.strftime("%H:%M:%S")

    print("Momento da emoção =", momentoEmotion)#DEBUG

    #Escrita e organização das emoções no arquivo.
    arquivo = open("arquivo.txt", "a")#ABRE ARQUIVO
    #arquivoXls = open("tabela.xls", "a")#ABRE/GERA XML

    #Emoções detectadas:
    arquivo.write("Emoção detectada:-----|")
    arquivo.write(emotions)
    arquivo.write("\n")

    #Escrevendo numero(int) em string
    arquivo.write("Nº de Detecções:------|")
    arquivo.write(str(nEmotion))
    arquivo.write("\n")

    #Momento no qual a emoção foi detectada:
    arquivo.write("Momento Detectado:----|")
    arquivo.write(momentoEmotion)
    arquivo.write("\n\n")
