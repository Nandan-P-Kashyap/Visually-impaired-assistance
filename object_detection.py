import cv2
import tensorflow as tf
import numpy as np
import pyttsx3  # Import the text-to-speech library

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define your model architecture
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=[299, 299, 3]),
    tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax')  # 5 classes for 10, 20, 50, 100, 500 Rs notes
])

# Load the pre-trained model weights
model.load_weights('currency_model.h5')

def preprocess_image(image_path):
    """Preprocess the image for model prediction."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (299, 299))
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def detect_currency(image_path):
    """Detect currency using the trained model."""
    # Preprocess the image
    image = preprocess_image(image_path)
    
    # Predict using the model
    predictions = model.predict(image)
    class_id = np.argmax(predictions[0])
    confidence = predictions[0][class_id]
    
    # Class labels for Indian currency notes
    currency_labels = ["10 Rs", "20 Rs", "50 Rs", "100 Rs", "500 Rs"]
    
    # Display result
    detected_currency = f"Detected currency: {currency_labels[class_id]} with confidence {confidence:.2f}"
    print(detected_currency)
    
    # Convert the result to speech
    engine.say(detected_currency)
    engine.runAndWait()

if __name__ == "__main__":
    # Example image path, replace with your image path
    image_path = 'path_to_your_currency_image.jpg'
    detect_currency(image_path)
