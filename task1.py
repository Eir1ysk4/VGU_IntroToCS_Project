import numpy as np
import speech_recognition as sr


class Task1:
    model = None
    class_names = None
    recognizer = None


    def __init__(self):
        print("Init task 1")
        self.recognizer = sr.Recognizer()


    def Task1_Run(self):
        print("Task 1 is activated!!!!")
        audio_file = "C:/Users/LENOVO/VGU_IntroToCS_Project.git/trunk/audio-2.wav"
        print("Using audio file:", audio_file)
        result = self.audio_to_text(audio_file)
        print("Transcribed text:", result)

    def audio_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source, duration=10)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"        
