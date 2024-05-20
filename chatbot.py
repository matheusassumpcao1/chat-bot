import google.generativeai as genai
import pyttsx3

GOOGLE_API_KEY = "" #INSERIR AQUI SUA API
genai.configure(api_key=GOOGLE_API_KEY)

# Inicializar o modelo.
model = genai.GenerativeModel('gemini-pro')

# Inicializar conversa, com historico vazio.
chat = model.start_chat(history=[])

#Inicializar biblioteca para ler a resposta em audio.
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed of speech
voices = engine.getProperty('voices')
for voice in voices:
    if 'portuguese' in voice.languages:
        engine.setProperty('voice', voice.id)
        break

# Loop para pegar prompts, responde-los e armazena-los
try:
    while True:
        texto = input("Escreva sua mensagem: ")

        if texto.lower() == "sair":
            print("Chat encerrado.")
            break
        
        
        response = chat.send_message(texto)
        resposta_texto = response.text  

        print("Gemini: ", resposta_texto)

        
        engine.say(resposta_texto)
        engine.runAndWait()

except Exception as e:
    print(f"An error occurred: {e}")
