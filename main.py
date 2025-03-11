import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser

import datetime

def get_moscow_time_simple():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    return formatted_time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Распознаю...")
        query = r.recognize_google(audio, language='ru-RU')
        print(f"Пользователь сказал: {query}\n")

    except Exception as e:
        print("Повторите, пожалуйста...")
        return "None"
    return query


if __name__ == "__main__":
    print("Привет, я - Пит!")
    speak("Привет, я - Пит!!")
    print("Я твой личный голосовой помощник, могу открыть для тебя нужные сайты или подсказать время.")
    speak("Я твой личный голосовой помощник, могу открыть для тебя нужные сайты или подсказать время.")

    while True:
        query = takeCommand().lower()

        if 'подскажи мне точное время' in query or 'время' in query:
            current_time_moscow = get_moscow_time_simple()
            print(f"Текущее время: {current_time_moscow}")
            speak(f"Текущее время: {current_time_moscow}")
            print("Скажите 'стоп/пока/завершить работу', чтобы остановить работу помощника.")

        elif 'открыть вк' in query or 'открыть вконтакте' in query or 'открой вк' in query or 'открой вконтакте' in query:
            print("Открываю ВКонтакте...")
            speak("Открываю ВКонтакте...")
            webbrowser.open("vk.com/public170645667")
            print("Скажите 'стоп/пока/завершить работу', чтобы остановить работу помощника.")

        elif 'открыть рутуб' in query or 'открыть rutube' in query or 'открой rutube' in query or 'открой рутуб' in query:
            print("Открываю RuTube...")
            speak("Открываю RuTube...")
            webbrowser.open("rutube.ru/search/?query=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BB%D0%B8%D1%86%D0%B5%D0%B9")
            print("Скажите 'стоп/пока/завершить работу', чтобы остановить работу помощника.")

        elif 'открыть яндекс' in query or 'открыть yandex' in query or 'открой яндекс' in query or 'открой yandex' in query:
            print("Открываю Яндекс...")
            speak("Открываю Яндекс...")
            webbrowser.open("yandex.com")
            print("Скажите 'стоп/пока/завершить работу', чтобы остановить работу помощника.")

        elif 'выход' in query or 'завершить работу' in query or 'стоп' in query or "пока" in query:
            speak("До свидания!")
            break

        else:
            speak("Готов слушать следующий запрос.")