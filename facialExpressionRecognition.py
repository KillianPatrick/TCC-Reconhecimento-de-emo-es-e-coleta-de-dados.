import gui

gui.geraInterface()


















































# ----------------------------------------------------------------------------------------------------------------------
#Carregando o treinamento do classificador.
'''face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)#FORÇA A ABERTURA DA CAMERA AQUI TEM QUE FAZER NA GUI
# ----------------------------------------------------------------------------------------------------------------------

# Iniciando a CNN para reconhecimento de emoções.
from keras.models import model_from_json

#Carregando o modelo de CNN
model = model_from_json(open("facial_expression_model_structure.json", "r").read())
#Carregando os pesos treinados da CNN.
model.load_weights('facial_expression_model_weights.h5')
# ----------------------------------------------------------------------------------------------------------------------

#Matriz de emoções:
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


#CRIAÇÃO DOS ARRAYS PARA ARMAZENA O QUE SERÁ ESCRITO NA TABELA.
nBravo =([0])
tBravo =([])
nRepugnancia =([0])
tRepugnancia =([])
nMedo =([0])
tMedo =([])
nFeliz =([0])
tFeliz =([])
nTriste =([0])
tTriste =([])
nSurpresa =([0])
tSurpresa =([])
nNeutra =([0])
tNeutra =([])
while(True):
	ret, img = cap.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	#Estrutura de repetição para localizar as faces e as imprimir.
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Desenha retangulo na imagem principal.

		detected_face = img[int(y):int(y+h), int(x):int(x+w)] #Recorta a face detectada.
		detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #Transformação para escalas de Cinza.
		detected_face = cv2.resize(detected_face, (48, 48)) #Redimensionando para 48x48 pixels

		img_pixels = image.img_to_array(detected_face)#Converte a face recortada para matriz Numpy.
		img_pixels = np.expand_dims(img_pixels, axis = 0)

		img_pixels /= 255 #Pixels estão em escala de [0, 255]. São normalizados todos os pixels para escala de [0, 1]

		predictions = model.predict(img_pixels) #Armazena as probabilidades das 7 emoções.

		#Encontra o valor maximo da matriz [0] entre: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
		max_index = np.argmax(predictions[0])

		emotion = emotions[max_index] #Armazena emoção reconhecida por maior probabilidade.

		#Testa-se as emoções e logo armazena o total de aparições da emoção testada.
		if emotions[max_index] == 'Bravo':
			#COLETA DE DADOS PARA ARQUIVO XLS
			#Conta número de detecções e armazena
			bravo +=1
			nBravo.append(bravo)
			#Coleta-se o tempo da detecção e armazena
			now = datetime.now()
			#Convertes-se o tempo em hora:minuto:segundo
			momentoEmotion = now.strftime("%H:%M:%S")
			tBravo.append(momentoEmotion)

			#Chama função de pré-processamento de dados(teste) em arquivo texto
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

			# chama função de pré-processamento de dados(teste) em arquivo texto
			RF.EscrevendoEmotions(emotions[max_index], feliz)
			print("aqui PRINTA")

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

			# chama função de pré-processamento de dados(teste) em arquivo texto
			RF.EscrevendoEmotions(emotions[max_index], neutra)
		#SOMA TOTAL DE EMOÇÕES DETECTADAS.
		totalEmotions = bravo + repugnancia + medo + feliz + triste + surpresa + neutra

		#Visto que apenas chamar a função não bastava, cria-se atribustos globais para as emoções;
		#então são realizados os testes e incrementação do atributo
		#para compilar informações da taxa de intensidade emocional.
		#de uma emoção detectada com sucesso.
		#Não bastou, extrair o array emotions foi necessário a especificar o max_index
		#a fim de extrair a exata emoção.

		#Escreve emoção sobre o retangulo.
		#cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

		#Fim do processo de detecção da face e reconhecimento da emoção.
		#---------------------------------------------------------------------------------------------------------------

	cv2.imshow('img',img)
	#gui.geraInterface(totalEmotions, bravo, repugnancia, medo, feliz, triste, surpresa, neutra)
	if cv2.waitKey(1) & 0xFF == ord('q'): #press 'q' to quit
		# chama função que realiza pro processamento dos dados para XLS a ser convertido em grafico
		RF.EscreveXls('BRAVO.xlsx', nBravo, tBravo, bravo)
		RF.EscreveXls('REPUGNANCIA.xlsx', nRepugnancia, tRepugnancia, repugnancia )
		RF.EscreveXls('MEDO.xlsx', nMedo, tMedo, medo)
		RF.EscreveXls('FELIZ.xlsx', nFeliz, tFeliz, feliz)
		RF.EscreveXls('TRISTE.xlsx', nTriste, tTriste, triste)
		RF.EscreveXls('SURPRESA.xlsx', nSurpresa, tSurpresa, surpresa)
		RF.EscreveXls('NEUTRA.xlsx', nNeutra, tNeutra, neutra)
		break

cap.release()'''
#cv2.destroyAllWindows()