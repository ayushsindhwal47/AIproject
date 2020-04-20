from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as py
import speech_recognition as srm
import threading

tk = Tk()
frame = Frame(tk)
engine = py.init()

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

tk.geometry('800x1000')
tk.configure(bg="#0040ff")
tk.title('Ayush')
chatbot = ChatBot('Medino')

conversation = [
    'hello',
    'My name is Medino',
    'What can you do for',
    'I can assist you for medications',
    'which medicine you are looking for ?',
    'Azithromycin paracetamol Livocytrizine',
    'About Azithromycin',
    'it is used to treat a wide variety of bacterial infections',
    'About paracetamol',
    'Treats fever and headache',
    'About Livocytrizine',
    ' used to relieve allergy symptoms such as watery eyes, runny nose, sneezing, hives, and itching',
    'About Ativan',
    ' Ativan is used to treat anxiety disorders and seizure disorders.',
    'About Adderall',
    'Its used to treat attention-deficit hyperactivity disorder (ADHD)',
    'Azithromycin prescription',
    'allergy, inflamation'
    'paracetamol prescription',
    'fever, headache, pain in the back'
    'Livocytrizine prescription',
    'skin problem, body heat',
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)


def getQuery():
    sr = srm.Recognizer()
    sr.pause_threshold = 1
    print("hello, Please Ask Your Query")
    with srm.Microphone() as m:

        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            input.delete(0, END)
            input.insert(0, query)
            responses()
        except Exception as e:
            print(e)
            print('Not Recognised')


def speak(word):
    engine.say(word)
    engine.runAndWait()


def responses():
    query = input.get()
    # reply='hi'
    reply = chatbot.get_response(query)
    chat.insert(END, 'User=>' + str(query))
    chat.insert(END, 'Medino=>' + str(reply))
    speak(reply)
    input.delete(0, END)
    chat.yview(END)


def submit(onEnter):
    response.invoke()


tk.bind('<Return>', submit)

logoDecryption = PhotoImage(file='logo.png')
logo = Label(tk, image=logoDecryption, width=250, height=250)
logo.pack(padx=5, pady=5)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
chat = Listbox(frame, width=80, height=14, bg='#212121', font='stencil 14',fg='gray', yscrollcommand=scrollbar.set)
chat.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


input = Entry(tk, font='amazobitaemostrovfine 20', fg='blue',bg='#0040ff')
input.insert(0, 'please speak or Enter your Query')
input.pack(fill=X, pady=5)
response = Button(tk, font='amazobitaemostrovfine 20', fg='blue',bg='#0040ff', text='Ask Your Query', command=responses)
response.pack()


def repeatListen():
    while True:
        print('run')
        getQuery()


t = threading.Thread(target=repeatListen)
t.start()

tk.mainloop()
