# 🌿 Mango Leaf Disease Detector# 🌿 Mango Leaf Disease Detector



A production-ready deep learning system for detecting mango leaf diseases using Swin Transformer. Achieves **99.87% accuracy** with desktop GUI and cloud REST API.A production-ready deep learning system for detecting mango leaf diseases using Swin Transformer. Achieves **99.87% accuracy** with desktop GUI and cloud REST API.



## ✨ Features## ✨ Features



- ✅ **99.87% Accuracy** - Validation accuracy, 100% test accuracy- ✅ **99.87% Accuracy** - Validation accuracy, 100% test accuracy

- ✅ **Desktop GUI** - Tkinter with 600×600 image display- ✅ **Desktop GUI** - Tkinter with 600×600 image display

- ✅ **REST API** - Flask server with 4 endpoints- ✅ **REST API** - Flask server with 4 endpoints

- ✅ **8 Diseases** - Comprehensive disease detection- ✅ **8 Diseases** - Comprehensive disease detection

- ✅ **Temperature Scaling** - Calibrated confidence scores- ✅ **Temperature Scaling** - Calibrated confidence scores

- ✅ **Docker Ready** - Production container deployment- ✅ **Docker Ready** - Production container deployment

- ✅ **Live API** - https://mango-leaf-disease-detector-1.onrender.com- ✅ **Live API** - https://mango-leaf-disease-detector-1.onrender.com



## 📁 Project Structure## 📁 Project Structure



``````

..

├── app.py                      # Flask REST API (177 lines)├── app.py                      # Flask REST API (177 lines)

├── wsgi.py                     # Gunicorn entry point├── wsgi.py                     # Gunicorn entry point

├── mango_ui_best.py            # Desktop GUI (500 lines)├── mango_ui_best.py            # Desktop GUI (500 lines)

├── swintin_executed.ipynb      # Training notebook├── swintin_executed.ipynb      # Training notebook

├── Dockerfile                  # Container configuration├── Dockerfile                  # Container configuration

├── requirements.txt            # GUI dependencies├── requirements.txt            # GUI dependencies

├── requirements-server.txt     # API dependencies├── requirements-server.txt     # API dependencies

├── templates/├── templates/

│   └── index.html             # Web UI (521 lines)│   └── index.html             # Web UI (521 lines)

└── saved_models/7/└── saved_models/7/

    ├── model.keras    ├── model.keras

    ├── model_weights.weights.h5    ├── model_weights.weights.h5

    └── metadata.json    └── metadata.json

``````



## 🚀 Quick Start## 🚀 Quick Start



### Option 1: Live Web Application### Option 1: Use Live Web Application

Visit: **https://mango-leaf-disease-detector-1.onrender.com**Visit: **https://mango-leaf-disease-detector-1.onrender.com**

- Upload mango leaf images

1. Open the link in your browser- Get real-time predictions

2. Upload a mango leaf image- View confidence scores & treatment info

3. Click "Predict Disease"

4. View results with confidence score### Option 2: Desktop Application



### Option 2: Desktop Application    ├── model_weights.weights.h5# Install dependencies (if needed)



```bash    └── metadata.jsonpip install -r requirements.txt

# Clone repository

git clone https://github.com/Ajaysubbumane/mango-leaf-disease-detector``````

cd mango-leaf-disease-detector



# Install dependencies

pip install -r requirements.txt## 🚀 Quick Start### 2. Run Training (Optional)



# Run GUI```bash

python mango_ui_best.py

```### Desktop GUI# Open Jupyter and run swintin_executed.ipynb



### Option 3: REST API```bash# Dataset path: C:\Users\ajayd\Downloads\MangDisease



```bashpip install -r requirements.txt```

# Install dependencies

pip install -r requirements-server.txtpython mango_ui_best.py



# Run server```### 3. Run the UI App

python app.py

```bash

# API will be available at http://localhost:8080

```### REST API Serverpython mango_ui_best.py



## 📊 Model Details```bash```



- **Architecture**: Swin Transformer Tiny224 (ImageNet pretrained)pip install -r requirements-server.txt

- **Accuracy**: 99.87% validation, 100% test

- **Training**: Two-phase (frozen backbone + fine-tuning)python app.py## 📊 Model Details

- **Epochs**: 60 (30 frozen + 30 fine-tune)

- **Input**: 224×224×3 RGB images```

- **Output**: 8 disease classes + Healthy

- **Parameters**: 28MVisit: http://localhost:8080- **Architecture**: Swin Transformer Tiny (ImageNet pretrained backbone)



## 🦠 Supported Diseases- **Classes**: 8 disease types (Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Healthy, Powdery Mildew, Sooty Mould)



1. **Anthracnose** - Fungal disease with dark circular lesions### Docker- **Image Size**: 224×224

2. **Bacterial Canker** - Water-soaked lesions with yellow halo

3. **Cutting Weevil** - Pest causing irregular leaf holes```bash- **Training**: Two-phase (frozen backbone + fine-tuning)

4. **Die Back** - Branch death from tip to base

5. **Gall Midge** - Abnormal leaf growths and deformationsdocker build -t mango-detector .- **Accuracy**: 99.87% validation, 100% test

6. **Healthy** - No disease detected

7. **Powdery Mildew** - White powdery coating on leavesdocker run -p 8080:8080 mango-detector

8. **Sooty Mould** - Black sooty coating from insect honeydew

```## 🖥️ GUI Features

## 🌐 API Endpoints



| Endpoint | Method | Purpose |

|----------|--------|---------|## 📊 Model Details- 📸 Upload mango leaf image

| `/` | GET | Web UI interface |

| `/api` | GET | API documentation |- 🔍 Click "ANALYZE LEAF" to detect disease

| `/health` | GET | Health check |

| `/predict` | POST | Predict disease from image |- **Architecture**: Swin Transformer Tiny224- 📊 View highlighted results (disease, confidence, severity)



### Predict Example- **Accuracy**: 99.87% validation, 100% test- 📈 See all 8 disease predictions ranked by confidence



```bash- **Training**: 60 epochs (30 frozen + 30 fine-tune)- 📝 Treatment recommendations included

curl -X POST -F "file=@leaf.jpg" https://mango-leaf-disease-detector-1.onrender.com/predict

```- **Input**: 224×224×3 RGB images



Response:- **Output**: 8 disease classes + Healthy## 🔧 Dataset Path

```json

{- **Parameters**: 28M

  "disease": "Anthracnose",

  "confidence": 0.98,Training dataset location:

  "confidence_text": "Very High Confidence (98.0%)",

  "description": "Fungal disease causing dark, sunken lesions...",## 🌐 API Endpoints```

  "treatment": "Use fungicides like copper sulfate...",

  "all_predictions": [...]C:\Users\ajayd\Downloads\MangDisease

}

```| Endpoint | Method | Purpose |```



## 🐳 Docker Deployment|----------|--------|---------|



```bash| `/` | GET | API documentation |## 📚 Class Names (Order Used)

# Build image

docker build -t mango-detector .| `/health` | GET | Health check |



# Run container| `/predict` | POST | Predict disease from image |1. Anthracnose

docker run -p 8080:8080 mango-detector

```| `/diseases` | GET | List all diseases |2. Bacterial Canker



## 📚 Technology Stack| `/info/<disease>` | GET | Disease information |3. Cutting Weevil



- **ML**: TensorFlow 2.20.0, Keras 3.10.04. Die Back

- **Model**: Swin Transformer Tiny (tfswin)

- **Frontend**: HTML5, CSS3, JavaScript### Predict Example5. Gall Midge

- **Backend**: Flask 3.0.0, Gunicorn

- **Desktop**: Tkinter```bash6. Healthy

- **Container**: Docker

- **Deployment**: Rendercurl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict7. Powdery Mildew



## 📈 Training Details```8. Sooty Mould



### Data Augmentation

- RandomFlip (horizontal & vertical)

- RandomRotation (0.2)## 🦠 Supported Diseases## 🚀 Deployment Options

- RandomZoom (0.2)

- RandomContrast (0.2)

- RandomBrightness (0.1)

1. **Anthracnose** - Fungal disease with dark circular lesionsThis project is now **deployment-ready**! Choose how to run it:

### Optimization

- Phase 1: Frozen backbone, lr=1e-42. **Bacterial Canker** - Water-soaked lesions from bacteria

- Phase 2: Fine-tuning, lr=5e-5

- Optimizer: Adam3. **Cutting Weevil** - Pest causing irregular leaf holes### Option 1: Desktop GUI (For Local Demo)

- Loss: Sparse Categorical Crossentropy

- Regularization: L2 (1e-4)4. **Die Back** - Progressive branch death```bash



### Temperature Scaling5. **Gall Midge** - Abnormal tissue growthspython mango_ui_best.py

- Temperature: 0.15

- For calibrated confidence scores6. **Healthy** - No disease detected```



## 🔗 Links7. **Powdery Mildew** - White fungal coatingBeautiful Tkinter interface with real-time predictions.



- **GitHub**: https://github.com/Ajaysubbumane/mango-leaf-disease-detector8. **Sooty Mould** - Black fungal coating

- **Live API**: https://mango-leaf-disease-detector-1.onrender.com

- **Model**: Swin Transformer Tiny224### Option 2: REST API Server (For Web/Mobile)



## 📝 License## 💻 GUI Features```bash



This project is open source and available for educational and research purposes.# Install server dependencies



## ✨ Ready for Production- 600×600 image previewpip install -r requirements-server.txt



- ✅ 99.87% accuracy model- Real-time disease prediction

- ✅ Production-grade code

- ✅ Comprehensive error handling- Confidence scores >90%# Run Flask API

- ✅ Complete documentation

- ✅ Live deployment- Treatment recommendationspython app.py

- ✅ Ready for viva/presentation

- Prevention guidelines# API available at http://localhost:8080

---

- Threading for smooth operation```

**Created**: November 2025 | **Status**: ✅ Production Ready

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
