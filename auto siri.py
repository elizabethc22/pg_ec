import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi human, I am your worst nigthmare. My name is kidz bob. what do you want to search for?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok, elizabeth, lets look for " + r.recognize_google(audio) + " on Google.")
    wb.open("http://www.google.come/search?q=" + words)

except sr.UnknownValueError:
    print("Satan could not understand your speaking")
except sr.RequestError as e:
    print("Could not request results from Satan Speech Recognition service; {0}" .format(e))
