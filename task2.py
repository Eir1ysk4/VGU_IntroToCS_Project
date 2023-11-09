import tensorflow as tf
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
import time

class Task2:
    cam = None
    model = None
    frame = None

    def __init__(self):
        print("Init task 2")
        self.cam = cv2.VideoCapture(0)
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_Model.h5")
        self.image_capture()

    def image_capture(self):
        ret, self.frame = self.cam.read()  # Store the captured frame in self.frame
        return

    def Task2_Run(self):
        print("Task 2 is activated!!!!")
        while True:
            time.sleep(5)
            self.image_capture()
            self.image_detector()

    def image_detector(self):
        class_names = open("labels.txt", "r").readlines()

        # Resize and normalize the frame
        frame = cv2.resize(self.frame, (224, 224))
        frame = frame / 255.0

        data = np.expand_dims(frame, axis=0)

        # Predicts the model
        predictions = self.model.predict(data)
        print(predictions)
        index = np.argmax(predictions)
        class_name = class_names[index].strip()  # Remove any leading/trailing whitespace
        confidence_score = predictions[0][index]

        # Print prediction and confidence score
        print("Class:", class_name, end="")
        print("Confidence Score:", confidence_score)
        if confidence_score > 0.9:
            print("Login successfully, how can I help you?")
        else:
            print("Sorry, I cannot help you!!!")

        # Find the index with maximum confidence
        max_index = np.argmax(predictions[0])
        max_confidence = predictions[0][max_index]
        print(max_index, max_confidence)

        # Display the result on the frame
        label = "Boss" if max_index == 0 else "Stranger"
        cv2.putText(self.frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Human Detection", self.frame)

        # Read labels from the file and print the AI result
        data = [line.strip() for line in class_names]
        print("AI Result:", data[max_index])


if __name__ == "_main_":
    task2 = Task2()
    task2.Task2_Run()