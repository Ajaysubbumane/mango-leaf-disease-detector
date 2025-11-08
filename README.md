# 🌿 Mango Leaf Disease Detector# 🌿 Mango Leaf Disease Detection System



A production-ready deep learning system for detecting mango leaf diseases using Swin Transformer. Achieves **99.87% accuracy** with both desktop GUI and cloud REST API.A deep learning project that classifies mango leaf diseases using Swin Transformer transfer learning.



## ✨ Features## 📁 Project Structure



- ✅ **99.87% Accuracy** - Validation accuracy with 100% test accuracy```

- ✅ **Desktop GUI** - Tkinter with 600×600 image displayresearch/

- ✅ **REST API** - Flask with 5 endpoints for deployment├── swintin_executed.ipynb          # Training notebook (Swin-Tiny model)

- ✅ **8 Diseases** - Comprehensive disease database├── mango_ui_best.py                # Desktop GUI for disease detection

- ✅ **Temperature Scaling** - Calibrated confidence scores├── requirements.txt                # Python dependencies

- ✅ **Docker Ready** - Container deployment support├── saved_models/                   # Trained model weights (v7)

- ✅ **Live API** - https://mango-leaf-disease-detector-1.onrender.com│   └── 7/

│       ├── model.keras

## 📁 Project Structure│       ├── model_weights.weights.h5

│       └── metadata.json

```└── README.md                       # This file

.```

├── app.py                    # Flask REST API

├── mango_ui_best.py          # Tkinter Desktop GUI## 🎯 Quick Start

├── swintin_executed.ipynb    # Training notebook

├── Dockerfile                # Docker configuration### 1. Setup Environment

├── requirements.txt          # GUI dependencies```bash

├── requirements-server.txt   # API dependencies# Activate virtual environment

└── saved_models/7/           # Trained model.venv\Scripts\Activate.ps1

    ├── model.keras

    ├── model_weights.weights.h5# Install dependencies (if needed)

    └── metadata.jsonpip install -r requirements.txt

``````



## 🚀 Quick Start### 2. Run Training (Optional)

```bash

### Desktop GUI# Open Jupyter and run swintin_executed.ipynb

```bash# Dataset path: C:\Users\ajayd\Downloads\MangDisease

pip install -r requirements.txt```

python mango_ui_best.py

```### 3. Run the UI App

```bash

### REST API Serverpython mango_ui_best.py

```bash```

pip install -r requirements-server.txt

python app.py## 📊 Model Details

```

Visit: http://localhost:8080- **Architecture**: Swin Transformer Tiny (ImageNet pretrained backbone)

- **Classes**: 8 disease types (Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Healthy, Powdery Mildew, Sooty Mould)

### Docker- **Image Size**: 224×224

```bash- **Training**: Two-phase (frozen backbone + fine-tuning)

docker build -t mango-detector .- **Accuracy**: 99.87% validation, 100% test

docker run -p 8080:8080 mango-detector

```## 🖥️ GUI Features



## 📊 Model Details- 📸 Upload mango leaf image

- 🔍 Click "ANALYZE LEAF" to detect disease

- **Architecture**: Swin Transformer Tiny224- 📊 View highlighted results (disease, confidence, severity)

- **Accuracy**: 99.87% validation, 100% test- 📈 See all 8 disease predictions ranked by confidence

- **Training**: 60 epochs (30 frozen + 30 fine-tune)- 📝 Treatment recommendations included

- **Input**: 224×224×3 RGB images

- **Output**: 8 disease classes + Healthy## 🔧 Dataset Path

- **Parameters**: 28M

Training dataset location:

## 🌐 API Endpoints```

C:\Users\ajayd\Downloads\MangDisease

| Endpoint | Method | Purpose |```

|----------|--------|---------|

| `/` | GET | API documentation |## 📚 Class Names (Order Used)

| `/health` | GET | Health check |

| `/predict` | POST | Predict disease from image |1. Anthracnose

| `/diseases` | GET | List all diseases |2. Bacterial Canker

| `/info/<disease>` | GET | Disease information |3. Cutting Weevil

4. Die Back

### Predict Example5. Gall Midge

```bash6. Healthy

curl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict7. Powdery Mildew

```8. Sooty Mould



## 🦠 Supported Diseases## 🚀 Deployment Options



1. **Anthracnose** - Fungal disease with dark circular lesionsThis project is now **deployment-ready**! Choose how to run it:

2. **Bacterial Canker** - Water-soaked lesions from bacteria

3. **Cutting Weevil** - Pest causing irregular leaf holes### Option 1: Desktop GUI (For Local Demo)

4. **Die Back** - Progressive branch death```bash

5. **Gall Midge** - Abnormal tissue growthspython mango_ui_best.py

6. **Healthy** - No disease detected```

7. **Powdery Mildew** - White fungal coatingBeautiful Tkinter interface with real-time predictions.

8. **Sooty Mould** - Black fungal coating

### Option 2: REST API Server (For Web/Mobile)

## 💻 GUI Features```bash

# Install server dependencies

- 600×600 image previewpip install -r requirements-server.txt

- Real-time disease prediction

- Confidence scores >90%# Run Flask API

- Treatment recommendationspython app.py

- Prevention guidelines# API available at http://localhost:8080

- Threading for smooth operation```

- Dark professional theme

See **DEPLOY.md** for complete deployment guide including Docker, Cloud Run, Render, AWS, etc.

## ⚙️ Installation

### 📥 Model Files (For Deployment)

### Prerequisites

- Python 3.9+Model files are large (~961 MB) and stored locally. For cloud deployment:

- pip or conda

- Git```bash

# Download model helper script

### Setuppython download_model.py

```bash```

# Clone repository

git clone https://github.com/Ajaysubbumane/mango-leaf-disease-detector.gitThe script handles model download from cloud storage. See **DEPLOY.md - Model Loading Strategies** for options:

cd mango-leaf-disease-detector- GitHub Releases (free)

- AWS S3

# Create virtual environment- Google Cloud Storage

python -m venv venv- Hugging Face Hub

source venv/bin/activate  # Windows: venv\Scripts\activate

---

# Install dependencies

pip install -r requirements.txt## 🖥️ How to Use the Desktop App



# Run GUI1. **Click "📁 Choose Image"** → Select a mango leaf photo

python mango_ui_best.py2. **Click "🔍 ANALYZE LEAF"** → AI predicts the disease

```3. **View Results**:

   - Disease name (highlighted in RED)

## 🌐 Deployment   - Confidence % (highlighted in GREEN)

   - Severity level (🔴 HIGH / 🟠 MEDIUM / ✅ NONE)

### Render (Recommended - Free Tier)   - Treatment recommendations

1. Push to GitHub   - All 8 predictions ranked

2. Connect to Render

3. Deploy as Web Service---

4. API live automatically

## 🌐 REST API Endpoints (if using `app.py`)

### Cloud Run (Google Cloud)

```bash| Endpoint | Method | Purpose |

gcloud builds submit --tag gcr.io/PROJECT/mango-detector|----------|--------|---------|

gcloud run deploy --image gcr.io/PROJECT/mango-detector| `/` | GET | API documentation |

```| `/health` | GET | Health check |

| `/predict` | POST | Send image for prediction |

### Elastic Beanstalk (AWS)| `/diseases` | GET | List all diseases |

```bash| `/info/<disease>` | GET | Get disease details |

eb init -p python-3.9 mango-detector

eb create**Example:**

eb deploy```bash

```curl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict

```

## 📈 Performance

## 🎓 For Viva Presentation

| Metric | Value |

|--------|-------|**One-minute script:**

| Validation Accuracy | 99.87% |"This project uses Swin Transformer Tiny with transfer learning to classify eight mango leaf diseases. The notebook handles augmentation, two-phase training (frozen backbone then fine-tune), and achieves 99.87% validation accuracy. The desktop GUI loads model weights, accepts uploaded leaf images, and displays disease predictions with confidence and treatment info. I fixed deployment issues by matching inference preprocessing to training and rebuilding the model architecture before loading weights."

| Test Accuracy | 100% |

| Prediction Time | <100ms |**Key parameters:**

| Model Size | 28M parameters |- Batch size: 16

| Memory | ~250MB |- Epochs: 30 per phase

- Optimizer: Adam (lr=1e-4 phase 1, 5e-5 phase 2)

## 🐛 Troubleshooting- Augmentation: Flip, Rotate, Zoom, Contrast, Brightness

- Regularization: L2, Dropout, BatchNorm, EarlyStopping

### GUI Won't Display

```bash## 💾 Model Artifacts

# Update tkinter

pip install --upgrade python-tkAll trained models are saved in `saved_models/7/`:

```- `model.keras` - Full model (Keras format)

- `model_weights.weights.h5` - Weights only (safe for custom architectures)

### Port 8080 Already in Use- `metadata.json` - Training metadata and accuracies

```bash

PORT=5000 python app.py## ⚠️ Troubleshooting

```

**UI window not visible?**

### Model Not Loading- Press Alt+Tab to cycle windows

- Verify `saved_models/7/model_weights.weights.h5` exists- Look for Python icon on taskbar

- Check file permissions- Use Win+Tab to find the window

- Ensure TensorFlow is installed

**Model loading error?**

## 📚 Files- Ensure `saved_models/7/` folder exists

- Check that weights file path is correct

- **app.py** (177 lines) - Clean Flask API with graceful error handling- Verify TensorFlow is installed

- **mango_ui_best.py** (500 lines) - Professional Tkinter GUI

- **Dockerfile** - Multi-stage Docker build with health checks**Prediction not working?**

- **requirements.txt** - GUI dependencies- Ensure image is a valid leaf photo (224×224 will be auto-resized)

- **requirements-server.txt** - API dependencies- Check that model is fully loaded (see status bar)

- Try with a different image

## 🔗 Links

## 📦 Dependencies

- **GitHub**: https://github.com/Ajaysubbumane/mango-leaf-disease-detector

- **Live API**: https://mango-leaf-disease-detector-1.onrender.comSee `requirements.txt` for full list:

- **Training Notebook**: swintin_executed.ipynb- TensorFlow

- tfswin (Swin Transformer)

## 👨‍💻 Author- Pillow (image processing)

- NumPy

**Ajay Subbumane** - Lead Developer- Matplotlib



## 📄 License---



MIT License - Feel free to use for academic and commercial projects**Created for**: Viva presentation and practical demonstration  

**Last Updated**: November 8, 2025

## 🙏 Acknowledgments

- Swin Transformer architecture (Microsoft Research)
- TensorFlow/Keras team
- Open-source community

---

**Made with ❤️ for mango farmers worldwide** 🌿🥭
