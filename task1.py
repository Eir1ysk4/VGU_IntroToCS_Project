from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import tensorflow.compat.v2 as tf

class Task1:
    model = None
    class_names = None

    def __init__(self, index, url):
        print("Init task 1")
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_Model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(index)
        self.cameraID =  index
        return

    def Task1_Run(self):
        print("Task 1 is activated!!!!")
        # Grab the webcamera's image.
        ret, image = self.camera.read()
        cv2.imwrite("task"+ str(self.cameraID) + ".png", image)

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        #cv2.imshow("Webcam Image", image)


        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

