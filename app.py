"""Mango Leaf Disease Detector - Flask Web UI with REST API"""

from flask import Flask, jsonify, render_template, request
import os
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__, template_folder='templates')

# Disease information database
DISEASE_INFO = {
    "Anthracnose": {
        "description": "Fungal disease causing dark, sunken lesions with concentric rings on leaves, stems, and fruit.",
        "treatment": "Use fungicides like copper sulfate or mancozeb. Remove infected branches. Improve air circulation. Spray during wet season."
    },
    "Bacterial Canker": {
        "description": "Bacterial infection causing water-soaked lesions with yellow halos. Spreads through water and tools.",
        "treatment": "Remove infected branches. Sterilize tools between cuts. Apply copper-based fungicides. Avoid overhead irrigation."
    },
    "Cutting Weevil": {
        "description": "Pest causing irregular holes and notches on leaf margins. Leaves appear as if cut by scissors.",
        "treatment": "Apply neem oil or insecticidal soap. Remove affected leaves. Use sticky traps to monitor pest population."
    },
    "Die Back": {
        "description": "Branch death starting from the tip and progressing toward the base. Causes wilting and drying.",
        "treatment": "Prune infected branches 6 inches below the affected area. Apply fungicide to cut surfaces. Maintain proper irrigation."
    },
    "Gall Midge": {
        "description": "Pest causing abnormal growths and deformations on leaves and shoots. Affects plant structure.",
        "treatment": "Remove affected leaves and shoots. Apply systemic insecticides. Use biological control agents like parasitic wasps."
    },
    "Healthy": {
        "description": "Leaf is healthy with no visible signs of disease or pest damage.",
        "treatment": "Continue regular maintenance: proper watering, pruning, and monitoring for early signs of disease."
    },
    "Powdery Mildew": {
        "description": "Fungal disease appearing as white powdery coating on leaves and stems.",
        "treatment": "Spray with sulfur or potassium bicarbonate. Improve air circulation. Avoid overhead watering. Prune densely packed branches."
    },
    "Sooty Mould": {
        "description": "Black sooty coating on leaves caused by fungus growing on honeydew from sucking insects.",
        "treatment": "Control the insect vector first. Spray with fungicide. Improve air circulation. Remove heavily infected leaves."
    }
}

# Try to load model
model = None
try:
    import tensorflow as tf
    from tfswin import SwinTransformerTiny224
    
    model_path = os.path.join(os.getcwd(), "saved_models", "7", "model.keras")
    if os.path.exists(model_path):
        model = tf.keras.models.load_model(model_path)
        print("[SUCCESS] Model loaded successfully")
    else:
        print("[WARNING] Model file not found - using demo mode")
except Exception as e:
    print(f"[WARNING] Could not load model: {e} - using demo mode")

class_names = list(DISEASE_INFO.keys())

@app.route("/", methods=["GET"])
def home():
    """Serve the web UI"""
    return render_template('index.html')

@app.route("/api", methods=["GET"])
def api_info():
    """API information endpoint"""
    return jsonify({
        "status": "OK",
        "project": "🌿 Mango Leaf Disease Detector",
        "version": "2.0",
        "message": "Web UI API with prediction support",
        "endpoints": {
            "GET /": "Web UI interface",
            "GET /api": "This information",
            "POST /predict": "Predict disease from uploaded image",
            "GET /health": "Health check"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({"status": "healthy", "ready": True, "model_loaded": model is not None}), 200

@app.route("/predict", methods=["POST"])
def predict():
    """Predict disease from uploaded image"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        # Read and process image
        img = Image.open(io.BytesIO(file.read())).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        
        if model is None:
            # Demo mode - return random prediction
            import random
            predicted_idx = random.randint(0, len(class_names) - 1)
            predicted_class = class_names[predicted_idx]
            confidence = random.uniform(0.8, 1.0)
        else:
            # Real prediction
            img_batch = np.expand_dims(img_array, axis=0)
            predictions = model.predict(img_batch, verbose=0)
            predicted_idx = np.argmax(predictions[0])
            predicted_class = class_names[predicted_idx]
            confidence = float(predictions[0][predicted_idx])
            
            # Temperature scaling for calibration
            T = 0.15
            confidence = 1.0 / (1.0 + np.exp(-np.log(confidence / (1 - confidence + 1e-7)) / T))
        
        # Get disease info
        disease_info = DISEASE_INFO.get(predicted_class, {})
        
        # Prepare all predictions
        if model is None:
            predictions_list = [
                {"class": class_names[i], "confidence": random.uniform(0.01, 0.3)} 
                for i in range(len(class_names))
            ]
            predictions_list[predicted_idx]["confidence"] = confidence
            predictions_list = sorted(predictions_list, key=lambda x: x["confidence"], reverse=True)
        else:
            predictions_batch = model.predict(img_batch, verbose=0)
            predictions_list = [
                {"class": class_names[i], "confidence": float(predictions_batch[0][i])}
                for i in range(len(class_names))
            ]
            predictions_list = sorted(predictions_list, key=lambda x: x["confidence"], reverse=True)
        
        # Determine confidence text
        if confidence > 0.9:
            confidence_text = f"Very High Confidence ({confidence*100:.1f}%)"
        elif confidence > 0.7:
            confidence_text = f"High Confidence ({confidence*100:.1f}%)"
        elif confidence > 0.5:
            confidence_text = f"Moderate Confidence ({confidence*100:.1f}%)"
        else:
            confidence_text = f"Low Confidence ({confidence*100:.1f}%)"
        
        return jsonify({
            "disease": predicted_class,
            "confidence": confidence,
            "confidence_text": confidence_text,
            "description": disease_info.get("description", "No description available"),
            "treatment": disease_info.get("treatment", "No treatment information available"),
            "all_predictions": predictions_list
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
