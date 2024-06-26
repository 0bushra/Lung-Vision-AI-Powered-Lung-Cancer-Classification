from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from db_utils import save_prediction

app = Flask(__name__)

# Load your model
model = load_model('lungmodel.h5', compile=False)
model.compile(optimizer='adamax', loss='categorical_crossentropy', metrics=['accuracy'])

@app.route('/', methods=['GET'])
def index():
    # Render the upload HTML page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file.stream). resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    class_labels = ['Lung Adenocarcinoma', 'Lung benign tissue', 'Lung Squamous Cell Carcinoma']
    result = class_labels[np.argmax(score)]
    
    # Call to save prediction to MongoDB
    save_prediction(
        image_name=file.filename,
        predicted_label=result,
        confidence=np.max(score),
        file_details={
            "size": file.content_length,
            "mime_type": file.content_type
        }
    )
    
    return render_template('predict.html', prediction=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
