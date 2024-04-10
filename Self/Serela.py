import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant


class Assistant:
    def __init__(self):
        self.recogniser = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)
        self.assistant = GenericAssistant("intents.json", intent_methods={"file": self.create_file})
        self.assistant.train_model()

        self.root = tk.Tk()
        self.label = tk.Label(text="𓅃", font=("Arial", 120, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()

    @staticmethod
    def create_file():
        with open("randomfile.txt", 'w') as f:
            f.write("BLEEP")

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recogniser.listen(mic)

                    text = self.recogniser.recognize_google(audio)
                    text = text.lower()

                    if "Serela" in text:
                        self.label.config(fg="red")
                        audio = self.recogniser.listen(mic)
                        text = self.recogniser.recognize_google(audio)
                        text = text.lower()

                        if "stop" or "end" or "bye" in text:
                            self.speaker.say("Bye boss!")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.label.config(fg="Black")

            except:
                self.label.config(fg="black")
                continue


Assistant()
