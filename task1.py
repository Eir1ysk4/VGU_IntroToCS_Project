import speech_recognition as sr

class Task1:
    recognizer = None

    result_text = None

    def __init__(self):
        print("Init task 1")
        self.recognizer = sr.Recognizer()

    def Task1_Run(self):
        print("Task 1 is activated!!!!")
        with sr.Microphone() as source:
            print("Listening for 10 seconds. Speak now")
            audio = self.recognizer.listen(source, timeout=5)
            try:
                self.result_text = self.recognizer.recognize_google(audio)
                print("You said:", self.result_text)
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(f"Sorry, an error occurred: {e}")
