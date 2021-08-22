import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
from keras.preprocessing import image
import reportFile as RF
from datetime import datetime
import time


def geraInterface():
    root = tk.Tk()
    root.title("Versão 1.0")
    root["bg"] = "white"
    root["background"] = "azure"
    root.geometry("600x300+100+100")

    # PARTE DE LOGIN/SENHA
    lb8 = Label(root, text="Login: ")  # TITULO
    lb8.place(x=170, y=30)
    lb1 = Label(root, text="Login: ")
    lb1.place(x=100, y=70)
    lb2 = Label(root, text="Senha: ")
    lb2.place(x=100, y=110)
    ed1 = Entry(root)  # entrada login
    ed1.place(x=140, y=70)
    ed2 = Entry(root, show="*")  # entrada senha
    ed2.place(x=140, y=110)

    def bt_login():
        login = ed1.get()
        senha = ed2.get()
        if login != "admin" or senha != "admin":
            lb3 = Label(root, text="Login ou senha inválidos!")
            lb3.place(x=110, y=170)
        else:
            root.destroy()
            definecoleta()

    botaologin = Button(root, width=20, text="Confirmar", command=bt_login)
    botaologin.place(x=110, y=200)

    # CADASTRO
    listausuario = ["Aluno", "Professor"]
    lb4 = Label(root, text="Escolha o tipo de usuário:")
    lb4.place(x=310, y=110)
    cb_usurious = ttk.Combobox(root, values=listausuario)
    cb_usurious.set("Professor")
    cb_usurious.place(x=310, y=130)
    lb7 = Label(root, text="Cadastro: ")  # titulo
    lb7.place(x=350, y=30)
    lb5 = Label(root, text="Nome: ")
    lb5.place(x=300, y=70)
    lb6 = Label(root, text="Senha: ")
    lb6.place(x=300, y=170)
    ed3 = Entry(root)
    ed3.place(x=340, y=70)  # entrada nome
    ed4 = Entry(root)
    ed4.place(x=340, y=170)  # entrada senha

    def bt_cad():
        nome = ed3.get()
        usuario = cb_usurious.get()
        senhacad = ed4.get()

    botaocadastro = Button(root, width=20, text="Cadastrar", command=bt_cad)
    botaocadastro.place(x=310, y=200)
    root.mainloop()


def definecoleta():
    coleta = tk.Tk()
    coleta.title("Versão 1.0")
    coleta["bg"] = "white"
    coleta["background"] = "azure"
    coleta.geometry("600x300+100+100")

    lb9 = Label(coleta, text="    Nome    ")
    lb9.place(x=20, y=50)
    lb10 = Label(coleta, text="Professor / Aluno")
    lb10.place(x=20, y=90)
    lb11 = Label(coleta, text="Granulidade Temporal: ")
    lb11.place(x=20, y=130)
    ed5 = Entry(coleta)#entrada granulidade
    ed5.place(x=150, y=130)
    lb12 = Label(coleta, text="Aperte Q para pausar a coleta!")
    lb12.place(x=50, y=170)

    tree = ttk.Treeview(coleta, selectmode="browse",column=("column1", "column2"), show='headings')
    tree.column("column1",width=120,minwidth=50,stretch=NO)
    tree.heading("#1",text="Mom. Emoção")
    tree.column("column2", width=120, minwidth=50, stretch=NO)
    tree.heading("#2", text="Emoção Detectada")
    tree.place(x=300, y=30)

    def bt_pausecoleta():
        cv2.destroyAllWindows()
        coleta.destroy()

    def bt_inicio():
        cap = cv2.VideoCapture('''ID DA CAMERA''')

        # Carregando o treinamento do classificador.
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # ----------------------------------------------------------------------------------------------------------------------
        # Iniciando a CNN para reconhecimento de emoções.
        from keras.models import model_from_json

        # Carregando o modelo de CNN
        model = model_from_json(open("facial_expression_model_structure.json", "r").read())
        # Carregando os pesos treinados da CNN.
        model.load_weights('facial_expression_model_weights.h5')
        # ----------------------------------------------------------------------------------------------------------------------

        # Matriz de emoções:
        emotions = ('Bravo', 'Repugnância', 'Medo', 'Feliz', 'Triste', 'Surpresa', 'Neutra')

        # Atributos com objetivo de armazenar o numero de vezes que cada emoção foi detectada.
        bravo = 0
        repugnancia = 0
        medo = 0
        feliz = 0
        triste = 0
        surpresa = 0
        neutra = 0
        totalEmotions = 0

        # CRIAÇÃO DOS ARRAYS PARA ARMAZENA O QUE SERÁ ESCRITO NA TABELA.
        nBravo = ([0])
        tBravo = ([])
        nRepugnancia = ([0])
        tRepugnancia = ([])
        nMedo = ([0])
        tMedo = ([])
        nFeliz = ([0])
        tFeliz = ([])
        nTriste = ([0])
        tTriste = ([])
        nSurpresa = ([0])
        tSurpresa = ([])
        nNeutra = ([0])
        tNeutra = ([])

        contador=0
        while (True):

            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Estrutura de repetição para localizar as faces e as imprimir.
            for (x, y, w, h) in faces:
                #time.sleep(granulidade)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Desenha retangulo na imagem principal.

                detected_face = img[int(y):int(y + h), int(x):int(x + w)]  # Recorta a face detectada.
                detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # Transformação para escalas de Cinza.
                detected_face = cv2.resize(detected_face, (48, 48))  # Redimensionando para 48x48 pixels

                img_pixels = image.img_to_array(detected_face)  # Converte a face recortada para matriz Numpy.
                img_pixels = np.expand_dims(img_pixels, axis=0)

                img_pixels /= 255  # Pixels estão em escala de [0, 255]. São normalizados todos os pixels para escala de [0, 1]

                predictions = model.predict(img_pixels)  # Armazena as probabilidades das 7 emoções.

                # Encontra o valor maximo da matriz [0] entre: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
                max_index = np.argmax(predictions[0])

                emotion = emotions[max_index]  # Armazena emoção reconhecida por maior probabilidade.

                # Testa-se as emoções e logo armazena o total de aparições da emoção testada.
                if emotions[max_index] == 'Bravo':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # Conta número de detecções e armazena
                    bravo += 1
                    nBravo.append(bravo)
                    # Coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # Convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tBravo.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Bravo\n", tag='1')
                    tree.update()
                    contador+=1

                    # Chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], bravo)

                elif emotions[max_index] == 'Repugnância':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    repugnancia += 1
                    nRepugnancia.append(repugnancia)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tRepugnancia.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Repugnancia\n", tag='1')
                    tree.update()
                    contador+=1

                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], repugnancia)

                elif emotions[max_index] == 'Medo':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    medo += 1
                    nMedo.append(medo)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tMedo.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Medo\n", tag='1')
                    tree.update()
                    contador+=1

                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], medo)

                elif emotions[max_index] == 'Feliz':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    feliz += 1
                    nFeliz.append(feliz)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tFeliz.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Feliz\n", tag='1')
                    tree.update()
                    contador+=1

                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], feliz)
                    #print("aqui PRINTA")

                elif emotions[max_index] == 'Triste':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    triste += 1
                    nTriste.append(triste)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tTriste.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Triste\n", tag='1')
                    tree.update()
                    contador+=1

                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], triste)

                elif emotions[max_index] == 'Surpresa':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    surpresa += 1
                    nSurpresa.append(surpresa)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tSurpresa.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Surpresa\n", tag='1')
                    tree.update()
                    contador+=1


                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], surpresa)
                elif emotions[max_index] == 'Neutra':
                    # COLETA DE DADOS PARA ARQUIVO XLS
                    # conta número de detecções e armazena
                    neutra += 1
                    nNeutra.append(neutra)
                    # coleta-se o tempo da detecção e armazena
                    now = datetime.now()
                    # convertes-se o tempo em hora:minuto:segundo
                    momentoEmotion = now.strftime("%H:%M:%S")
                    tNeutra.append(momentoEmotion)
                    tree.insert("", END, values=momentoEmotion + "\n" + "Neutra\n", tag='1')
                    tree.update()
                    contador+=1

                    # chama função de pré-processamento de dados(teste) em arquivo texto
                    RF.EscrevendoEmotions(emotions[max_index], neutra)
                # SOMA TOTAL DE EMOÇÕES DETECTADAS.
                totalEmotions = bravo + repugnancia + medo + feliz + triste + surpresa + neutra
            if contador == 10:
                tree.delete(*tree.get_children())#limpa a tabela inteira
                tree.update()
                contador=0



            # Visto que apenas chamar a função não bastava, cria-se atribustos globais para as emoções;
            # então são realizados os testes e incrementação do atributo
            # para compilar informações da taxa de intensidade emocional.
            # de uma emoção detectada com sucesso.
            # Não bastou, extrair o array emotions foi necessário a especificar o max_index
            # a fim de extrair a exata emoção.

            # Escreve emoção sobre o retangulo.
            # cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

            # Fim do processo de detecção da face e reconhecimento da emoção.
            # ---------------------------------------------------------------------------------------------------------------

            cv2.imshow('img', img)
            # gui.geraInterface(totalEmotions, bravo, repugnancia, medo, feliz, triste, surpresa, neutra)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
                # chama função que realiza pro processamento dos dados para XLS a ser convertido em grafico
                RF.EscreveXls('BRAVO.xlsx', nBravo, tBravo, bravo)
                RF.EscreveXls('REPUGNANCIA.xlsx', nRepugnancia, tRepugnancia, repugnancia)
                RF.EscreveXls('MEDO.xlsx', nMedo, tMedo, medo)
                RF.EscreveXls('FELIZ.xlsx', nFeliz, tFeliz, feliz)
                RF.EscreveXls('TRISTE.xlsx', nTriste, tTriste, triste)
                RF.EscreveXls('SURPRESA.xlsx', nSurpresa, tSurpresa, surpresa)
                RF.EscreveXls('NEUTRA.xlsx', nNeutra, tNeutra, neutra)
                break

        cap.release()
        cv2.destroyAllWindows()

    botaoplay = Button(coleta, width=20, text="Iniciar Coleta", command=bt_inicio)
    botaoplay.place(x=100, y=210)

    botaopause = Button(coleta, width=20, text="Sair", command=bt_pausecoleta)
    botaopause.place(x=100, y=250)

    coleta.mainloop()
