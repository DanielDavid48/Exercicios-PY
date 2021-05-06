# import speech_recognition as sr
# from gtts import gTTS
# from playsound import playsound

# audio = input('Digite algo: ')
# #Funcao responsavel por falar 
# def cria_audio(audio):
#     tts = gTTS(audio,lang='pt-br')
#     #Salva o arquivo de audioa
#     tts.save('hello.mp3')
#     print("Estou aprendendo o que você disse...")
#     #Da play ao audio
#     playsound('hello.mp3')
    
# cria_audio(audio)

def leia_float(msg1):
    teste = False
    while teste == False:
        try:
            num1 = float(input('Insira um número real: '))
        except KeyboardInterrupt:
            print('\033[33mUsuário preferiu não inserir um número.\033[m')
            num1 = 0
            teste = True
            return num1
        except:
            print('\033[31mERRO! Insira um número real válido!\033[m')
        else:
            teste = True
            return num1
        
msg1 = leia_float('Digite um número inteiro: ')
print(msg1)