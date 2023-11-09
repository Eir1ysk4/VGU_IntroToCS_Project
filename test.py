import cv2
import tensorflow as tf
import numpy as np

# Load the Teachable Machine model
model = tf.keras.models.load_model('keras_Model.h5')

# Open the laptop camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0  # Normalize pixel values

    # Make predictions
    predictions = model.predict(np.expand_dims(frame, axis=0))

    # Classify as human or non-human
    label = "Hello babi" if predictions[0][0] > predictions[0][1] else "Stranger"

    # Display the result on the frame
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Human Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()