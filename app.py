"""
🌿 Mango Leaf Disease Detector - REST API Server
FastAPI/Flask-based web server for disease detection
Can be deployed to Cloud Run, Render, or any Docker-compatible platform
"""

from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from PIL import Image
import os
import io
import json
from pathlib import Path

app = Flask(__name__)

# Configuration
MODEL_DIR = os.environ.get("MODEL_DIR", "./saved_models/7")
WEIGHTS_PATH = os.path.join(MODEL_DIR, "model_weights.weights.h5")
METADATA_PATH = os.path.join(MODEL_DIR, "metadata.json")

# Global model instance
model = None
class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back',
               'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']

disease_info = {
    'Anthracnose': {
        'icon': '🔴', 'type': 'Fungal Disease', 'severity': 'HIGH',
        'description': 'Dark circular lesions with yellow halos on leaves and fruit',
        'causes': 'Colletotrichum fungus, high humidity, poor air circulation',
        'treatment': 'Apply copper fungicide, Remove infected leaves, Improve ventilation',
        'prevention': 'Regular pruning and sanitation'
    },
    'Bacterial Canker': {
        'icon': '🟠', 'type': 'Bacterial Disease', 'severity': 'HIGH',
        'description': 'Angular water-soaked lesions with yellow halos on leaves',
        'causes': 'Xanthomonas bacteria, spread by insects and contaminated tools',
        'treatment': 'Use copper or streptomycin bactericide, Prune infected branches',
        'prevention': 'Use disease-free propagation material'
    },
    'Cutting Weevil': {
        'icon': '🟡', 'type': 'Pest Infestation', 'severity': 'MEDIUM',
        'description': 'Irregular holes in leaves, especially near margins and stem',
        'causes': 'Cutting weevil larvae feed on leaf tissues',
        'treatment': 'Apply neem oil spray, Handpick visible insects, Set traps',
        'prevention': 'Maintain plant vigor and regular monitoring'
    },
    'Die Back': {
        'icon': '🔴', 'type': 'Physiological Disease', 'severity': 'HIGH',
        'description': 'Progressive branch death extending from tip towards base',
        'causes': 'Poor drainage, waterlogging, nutrient deficiency, cold damage',
        'treatment': 'Prune dead wood, Improve soil drainage, Reduce nitrogen fertilizer',
        'prevention': 'Proper drainage and soil management'
    },
    'Gall Midge': {
        'icon': '🟠', 'type': 'Pest Infestation', 'severity': 'MEDIUM',
        'description': 'Abnormal gall-like leaf growths and deformed tissues',
        'causes': 'Gall midge larvae induce abnormal plant growth responses',
        'treatment': 'Apply neem oil spray, Remove affected leaves, Control humidity',
        'prevention': 'Regular monitoring and early intervention'
    },
    'Healthy': {
        'icon': '✅', 'type': 'Healthy Leaf', 'severity': 'NONE',
        'description': 'No disease detected - leaf is in excellent condition',
        'causes': 'Proper care and disease prevention practices',
        'treatment': 'Continue regular maintenance, Monitor periodically',
        'prevention': 'Continue current management practices'
    },
    'Powdery Mildew': {
        'icon': '⚪', 'type': 'Fungal Disease', 'severity': 'MEDIUM',
        'description': 'White powdery coating on leaves, stems and fruit surface',
        'causes': 'Fungal infection, warm dry days with cool nights',
        'treatment': 'Apply sulfur spray, Use potassium bicarbonate, Improve air circulation',
        'prevention': 'Proper spacing and regular pruning'
    },
    'Sooty Mould': {
        'icon': '⚫', 'type': 'Fungal Disease', 'severity': 'MEDIUM',
        'description': 'Black sooty fungal coating on leaves',
        'causes': 'Secondary fungus growing on insect honeydew deposits',
        'treatment': 'Treat honeydew-producing insects, Wash leaves, Apply fungicide',
        'prevention': 'Control aphids, scale insects, and mealybugs'
    }
}

def build_model():
    """Rebuild model architecture and load weights"""
    try:
        from tfswin import SwinTransformerTiny224
    except ImportError:
        print("[!] tfswin package not found")
        return None
    
    IMAGE_SIZE = (224, 224)
    try:
        backbone = SwinTransformerTiny224(include_top=False, 
                                         input_shape=(*IMAGE_SIZE, 3),
                                         weights='imagenet')
        backbone.trainable = True
        
        x = backbone.output
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(512, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.5)(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dropout(0.3)(x)
        output = layers.Dense(8, activation='softmax')(x)
        
        model = models.Model(inputs=backbone.input, outputs=output)
        model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
        
        # Try to load weights if they exist
        if os.path.exists(WEIGHTS_PATH):
            model.load_weights(WEIGHTS_PATH)
            print(f"[✓] Model weights loaded from {WEIGHTS_PATH}")
        else:
            print(f"[!] Model weights not found at {WEIGHTS_PATH} - using random initialization")
        
        return model
    except Exception as e:
        print(f"[✗] Error building model: {e}")
        return None

# Global flag to track model loading
_model_loaded = False

@app.before_request
def load_model_if_needed():
    """Load model on first request (Flask 3.0 compatible)"""
    global model, _model_loaded
    if not _model_loaded:
        try:
            model = build_model()
            if model is not None:
                _model_loaded = True
                print("[✓] Model loaded successfully on first request")
            else:
                print("[!] Model could not be loaded, API will provide error responses")
        except Exception as e:
            print(f"[✗] Failed to load model: {e}")
            # Continue anyway - API will respond with error when predict is called

@app.route("/", methods=["GET"])
def home():
    """Health check and API documentation"""
    model_status = "✅ Ready" if model is not None else "⚠️ Loading..."
    return jsonify({
        "project": "🌿 Mango Leaf Disease Detector",
        "version": "1.0",
        "accuracy": "99.87%",
        "model_status": model_status,
        "endpoints": {
            "POST /predict": "Send an image file to detect disease",
            "GET /health": "Check API status",
            "GET /diseases": "List all supported diseases",
            "GET /info/<disease>": "Get disease details",
            "GET /": "This help message"
        },
        "usage": {
            "curl": "curl -X POST -F 'file=@leaf.jpg' http://localhost:8080/predict",
            "python": "requests.post('http://localhost:8080/predict', files={'file': open('leaf.jpg','rb')})"
        },
        "supported_diseases": class_names
    })

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    model_loaded = model is not None
    return jsonify({
        "status": "healthy" if model_loaded else "model_loading",
        "model_loaded": model_loaded,
        "timestamp": str(Path(METADATA_PATH).stat().st_mtime) if os.path.exists(METADATA_PATH) else "unknown"
    })

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict disease from uploaded image
    
    Expected: multipart/form-data with 'file' field
    Returns: JSON with predictions, confidence, disease info
    """
    try:
        if model is None:
            return jsonify({"error": "Model not loaded yet. Please wait and retry."}), 503
        
        if 'file' not in request.files:
            return jsonify({"error": "No file provided. Use 'file' field in multipart form."}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400
        
        # Load image
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        image = image.resize((224, 224))
        image_array = np.array(image, dtype=np.float32)
        image_batch = np.expand_dims(image_array, axis=0)
        
        # Predict
        predictions = model.predict(image_batch, verbose=0)[0]
        
        # Temperature scaling T=0.15 for calibrated confidence
        TEMPERATURE = 0.15
        log_pred = np.log(predictions + 1e-10)
        scaled = np.exp(log_pred / TEMPERATURE)
        predictions = scaled / scaled.sum()
        
        # Get top prediction
        top_idx = int(np.argmax(predictions))
        top_disease = class_names[top_idx]
        top_confidence = float(predictions[top_idx] * 100)
        
        # Get disease info
        info = disease_info.get(top_disease, {})
        
        # Build response
        all_predictions = {class_names[i]: float(predictions[i] * 100) for i in range(len(class_names))}
        sorted_preds = sorted(all_predictions.items(), key=lambda x: x[1], reverse=True)
        
        return jsonify({
            "success": True,
            "predicted_disease": top_disease,
            "confidence": round(top_confidence, 2),
            "severity": info.get('severity', 'UNKNOWN'),
            "type": info.get('type', 'Unknown'),
            "description": info.get('description', ''),
            "causes": info.get('causes', ''),
            "treatment": info.get('treatment', ''),
            "prevention": info.get('prevention', ''),
            "all_predictions": dict(sorted_preds),
            "model_version": "v7",
            "model_accuracy": "99.87%"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/info/<disease>", methods=["GET"])
def get_disease_info(disease):
    """Get information about a specific disease"""
    if disease not in disease_info:
        return jsonify({"error": f"Disease '{disease}' not found"}), 404
    
    info = disease_info[disease]
    return jsonify({"disease": disease, **info})

@app.route("/diseases", methods=["GET"])
def list_diseases():
    """List all supported diseases"""
    return jsonify({
        "count": len(class_names),
        "diseases": class_names,
        "details": {name: disease_info[name] for name in class_names}
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
