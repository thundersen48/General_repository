import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_thresold = 0.5

def greeting():
    """""Greeting function"""
    return 'Привет мудак!'
def create_task():
    print('Что добавим в список дел?')

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    with open('todo-list.txt','a') as file:
        file.write(f'!{query}\n')
    return f'Задача{query} добавлена в todo-list!'


with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query == 'Привет':
    print(greeting())
elif query == 'Добавить задачу':
    print(create_task())
else:
    print('Прожуй потом разговаривай!')

