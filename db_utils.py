from pymongo import MongoClient
import os

# Initialize MongoDB connection
client = MongoClient(os.getenv('MONGO_URI'))
db = client.histopathological_images  # Use the appropriate database name
predictions_collection = db.predictions  # Use a collection to store prediction logs

def save_prediction(image_name, predicted_label, confidence, file_details):
    """Save prediction details to MongoDB."""
    predictions_collection.insert_one({
        "image_name": image_name,
        "predicted_label": predicted_label,
        "confidence": float(confidence),
        "metadata": file_details
    })
