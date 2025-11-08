# 🌿 Mango Leaf Disease Detection System

A deep learning project that classifies mango leaf diseases using Swin Transformer transfer learning.

## 📁 Project Structure

```
research/
├── swintin_executed.ipynb          # Training notebook (Swin-Tiny model)
├── mango_ui_best.py                # Desktop GUI for disease detection
├── requirements.txt                # Python dependencies
├── saved_models/                   # Trained model weights (v7)
│   └── 7/
│       ├── model.keras
│       ├── model_weights.weights.h5
│       └── metadata.json
└── README.md                       # This file
```

## 🎯 Quick Start

### 1. Setup Environment
```bash
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies (if needed)
pip install -r requirements.txt
```

### 2. Run Training (Optional)
```bash
# Open Jupyter and run swintin_executed.ipynb
# Dataset path: C:\Users\ajayd\Downloads\MangDisease
```

### 3. Run the UI App
```bash
python mango_ui_best.py
```

## 📊 Model Details

- **Architecture**: Swin Transformer Tiny (ImageNet pretrained backbone)
- **Classes**: 8 disease types (Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Healthy, Powdery Mildew, Sooty Mould)
- **Image Size**: 224×224
- **Training**: Two-phase (frozen backbone + fine-tuning)
- **Accuracy**: 99.87% validation, 100% test

## 🖥️ GUI Features

- 📸 Upload mango leaf image
- 🔍 Click "ANALYZE LEAF" to detect disease
- 📊 View highlighted results (disease, confidence, severity)
- 📈 See all 8 disease predictions ranked by confidence
- 📝 Treatment recommendations included

## 🔧 Dataset Path

Training dataset location:
```
C:\Users\ajayd\Downloads\MangDisease
```

## 📚 Class Names (Order Used)

1. Anthracnose
2. Bacterial Canker
3. Cutting Weevil
4. Die Back
5. Gall Midge
6. Healthy
7. Powdery Mildew
8. Sooty Mould

## 🚀 Deployment Options

This project is now **deployment-ready**! Choose how to run it:

### Option 1: Desktop GUI (For Local Demo)
```bash
python mango_ui_best.py
```
Beautiful Tkinter interface with real-time predictions.

### Option 2: REST API Server (For Web/Mobile)
```bash
# Install server dependencies
pip install -r requirements-server.txt

# Run Flask API
python app.py
# API available at http://localhost:8080
```

See **DEPLOY.md** for complete deployment guide including Docker, Cloud Run, Render, AWS, etc.

---

## 🖥️ How to Use the Desktop App

1. **Click "📁 Choose Image"** → Select a mango leaf photo
2. **Click "🔍 ANALYZE LEAF"** → AI predicts the disease
3. **View Results**:
   - Disease name (highlighted in RED)
   - Confidence % (highlighted in GREEN)
   - Severity level (🔴 HIGH / 🟠 MEDIUM / ✅ NONE)
   - Treatment recommendations
   - All 8 predictions ranked

---

## 🌐 REST API Endpoints (if using `app.py`)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API documentation |
| `/health` | GET | Health check |
| `/predict` | POST | Send image for prediction |
| `/diseases` | GET | List all diseases |
| `/info/<disease>` | GET | Get disease details |

**Example:**
```bash
curl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict
```

## 🎓 For Viva Presentation

**One-minute script:**
"This project uses Swin Transformer Tiny with transfer learning to classify eight mango leaf diseases. The notebook handles augmentation, two-phase training (frozen backbone then fine-tune), and achieves 99.87% validation accuracy. The desktop GUI loads model weights, accepts uploaded leaf images, and displays disease predictions with confidence and treatment info. I fixed deployment issues by matching inference preprocessing to training and rebuilding the model architecture before loading weights."

**Key parameters:**
- Batch size: 16
- Epochs: 30 per phase
- Optimizer: Adam (lr=1e-4 phase 1, 5e-5 phase 2)
- Augmentation: Flip, Rotate, Zoom, Contrast, Brightness
- Regularization: L2, Dropout, BatchNorm, EarlyStopping

## 💾 Model Artifacts

All trained models are saved in `saved_models/7/`:
- `model.keras` - Full model (Keras format)
- `model_weights.weights.h5` - Weights only (safe for custom architectures)
- `metadata.json` - Training metadata and accuracies

## ⚠️ Troubleshooting

**UI window not visible?**
- Press Alt+Tab to cycle windows
- Look for Python icon on taskbar
- Use Win+Tab to find the window

**Model loading error?**
- Ensure `saved_models/7/` folder exists
- Check that weights file path is correct
- Verify TensorFlow is installed

**Prediction not working?**
- Ensure image is a valid leaf photo (224×224 will be auto-resized)
- Check that model is fully loaded (see status bar)
- Try with a different image

## 📦 Dependencies

See `requirements.txt` for full list:
- TensorFlow
- tfswin (Swin Transformer)
- Pillow (image processing)
- NumPy
- Matplotlib

---

**Created for**: Viva presentation and practical demonstration  
**Last Updated**: November 8, 2025
