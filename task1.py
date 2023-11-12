from keras.models import load_model
import numpy as np
import cv2
import time


class Task1:
    cam = None
    model = None
    frame = None
    is_person_valid = False

    def __init__(self):
        print("Init task 1")
        self.cam = cv2.VideoCapture(0)
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_Model.h5")
        self.image_capture()

    def image_capture(self):
        ret, self.frame = self.cam.read()  # Store the captured frame in self.frame
        return

    def Task1_Run(self, scheduler, task2):
        print("Task 1 is activated!!!!")
        while True:
            time.sleep(5)
            self.image_capture()
            self.is_person_valid = self.image_detector()
            if self.is_person_valid:
                break
        scheduler.SCH_Add_Task(task2.Task2_Run, 1000, 10000)

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

        if confidence_score > 0.9:
            print("Login successfully, how can I help you?")
            return True
        else:
            print("Sorry, I cannot help you!!!")
            return False


if __name__ == "_main_":
    task1 = Task1()
    Task1.Task1_Run()
