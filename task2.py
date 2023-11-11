import speech_recognition as sr
from shared_resources import resources
class Task2:
    recognizer = None

    def __init__(self):
        print("Init task 2")
        self.recognizer = sr.Recognizer()

    def Task2_Run(self):
        print("Task 2 is activated!!!!")
        with sr.Microphone() as source:
            print("Listening for 10 seconds. Speak now")
            audio = self.recognizer.listen(source, timeout=5)
            try:
                resources.shared_data['task2_output'] = self.recognizer.recognize_google(audio)
                print("You said:", resources.shared_data['task2_output'])
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(f"Sorry, an error occurred: {e}")
