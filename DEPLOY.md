# 🌿 Deployment Guide - Mango Leaf Disease Detector

## Quick Overview
This project is now ready for deployment as a containerized REST API. The model runs on a web server and can be deployed to cloud platforms like **Cloud Run (GCP)**, **Render**, or any Docker-compatible infrastructure.

---

## 📦 Files Added for Deployment

- **`app.py`** — Flask REST API server with prediction endpoints
- **`Dockerfile`** — Container configuration (production-ready with gunicorn)
- **`requirements-server.txt`** — Server dependencies (Flask, gunicorn, TensorFlow, etc.)
- **`.dockerignore`** — Excludes large files from Docker build

---

## 🚀 Deployment Options

### **Option 1: Local Docker Test (Recommended First)**
Test the deployment locally before going live.

**Prerequisites:**
- Docker installed
- Model files at `./saved_models/7/model_weights.weights.h5`

**Steps:**
```bash
# Build image
docker build -t mango-detector:latest .

# Run container
docker run -p 8080:8080 -v $(pwd)/saved_models:/app/saved_models mango-detector:latest

# Test API (in another terminal)
curl http://localhost:8080/
curl http://localhost:8080/health
curl -X POST -F "file=@your_leaf_image.jpg" http://localhost:8080/predict
```

**Success:** API responds with health check + disease prediction.

---

### **Option 2: Deploy to Render (Easiest — FREE tier available)**

Render auto-detects your Dockerfile and deploys with minimal config.

**Steps:**
1. Push your code to GitHub (already done ✅)
2. Go to [render.com](https://render.com) → Sign up
3. Click **New** → **Web Service** → **Connect to GitHub**
4. Select your `mango-leaf-disease-detector` repo
5. Configure:
   - **Build Command**: `pip install -r requirements-server.txt`
   - **Start Command**: (auto-detects Dockerfile)
   - **Instance Type**: Free or Starter ($7/mo)
6. Click **Deploy**
7. Render builds and deploys automatically. Get URL in ~2-5 mins.

**After Deploy:**
```bash
# Test your live API
curl https://YOUR_RENDER_URL/health
curl -X POST -F "file=@leaf.jpg" https://YOUR_RENDER_URL/predict
```

**Cost:** Free tier has limited hours; Starter ($7/mo) unlimited.

---

### **Option 3: Deploy to Google Cloud Run (Faster, scalable)**

Cloud Run auto-scales and bills per request (very cheap for demos).

**Prerequisites:**
- Google Cloud account
- `gcloud` CLI installed and authenticated

**Steps:**
```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/mango-detector

# Deploy to Cloud Run
gcloud run deploy mango-detector \
  --image gcr.io/YOUR_PROJECT_ID/mango-detector \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --timeout 120
```

**Output:** You get a public URL like `https://mango-detector-xxxx-uc.a.run.app`

**Cost:** Cloud Run is free for ~2M requests/month; pay per usage after.

---

### **Option 4: Deploy to AWS Elastic Beanstalk**

Good for production with more control.

**Quick steps:**
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB
eb init -p docker mango-detector --region us-east-1

# Create environment and deploy
eb create prod
eb open
```

---

## 📥 Model Loading Strategies

### **Strategy A: Mount Model from Local (for testing)**
```bash
docker run -p 8080:8080 \
  -v $(pwd)/saved_models:/app/saved_models \
  mango-detector:latest
```

### **Strategy B: Download Model from Cloud Storage at Runtime (Production)**

Modify `app.py` startup to download model:

```python
import requests

def download_model_if_missing():
    if not os.path.exists(WEIGHTS_PATH):
        print("Downloading model...")
        url = "https://your-storage.s3.amazonaws.com/model_weights.h5"
        response = requests.get(url, stream=True)
        os.makedirs(os.path.dirname(WEIGHTS_PATH), exist_ok=True)
        with open(WEIGHTS_PATH, 'wb') as f:
            f.write(response.content)
        print("✓ Model downloaded")

@app.before_first_request
def startup():
    global model
    download_model_if_missing()  # <-- Add this
    model = build_model()
```

Then store the model in:
- **AWS S3** (easy) — generate signed URL
- **Google Cloud Storage** (easy) — public URL or signed URL
- **GitHub Releases** (free) — upload .h5 file, link to release
- **Hugging Face Hub** (free) — host model, download on start

---

## 🔗 API Endpoints

### **GET `/`**
Home page + API documentation.

```bash
curl http://localhost:8080/
```

Response:
```json
{
  "project": "🌿 Mango Leaf Disease Detector",
  "version": "1.0",
  "endpoints": { ... },
  "supported_diseases": [...]
}
```

---

### **GET `/health`**
Health check.

```bash
curl http://localhost:8080/health
```

---

### **POST `/predict`**
Send image for disease detection.

```bash
curl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict
```

Response:
```json
{
  "success": true,
  "predicted_disease": "Anthracnose",
  "confidence": 95.5,
  "severity": "HIGH",
  "type": "Fungal Disease",
  "description": "Dark circular lesions...",
  "treatment": "Apply copper fungicide...",
  "prevention": "Regular pruning...",
  "all_predictions": {
    "Anthracnose": 95.5,
    "Healthy": 2.1,
    ...
  }
}
```

---

### **GET `/diseases`**
List all supported diseases.

```bash
curl http://localhost:8080/diseases
```

---

### **GET `/info/<disease>`**
Info about specific disease.

```bash
curl http://localhost:8080/info/Anthracnose
```

---

## 🧪 Testing with Python

```python
import requests

# Local or cloud URL
URL = "http://localhost:8080"  # or "https://your-render-url"

# Test health
resp = requests.get(f"{URL}/health")
print(resp.json())

# Predict
with open("leaf.jpg", "rb") as f:
    resp = requests.post(
        f"{URL}/predict",
        files={"file": f}
    )
    result = resp.json()
    print(f"Disease: {result['predicted_disease']}")
    print(f"Confidence: {result['confidence']}%")
    print(f"Treatment: {result['treatment']}")
```

---

## 🛠️ Performance & Optimization

- **Inference time**: ~1-2 seconds per image (CPU)
- **Memory**: ~1-2 GB (model + TensorFlow)
- **GPU**: Not needed for demo; use if you want <1sec inference
- **Caching**: Implement Redis caching for repeated predictions (optional)

---

## 🔐 Security & Best Practices

1. **Rate Limiting**: Add `Flask-Limiter` to prevent abuse
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, key_func=lambda: request.remote_addr)
   
   @app.route("/predict", methods=["POST"])
   @limiter.limit("10 per minute")
   def predict():
       ...
   ```

2. **Authentication**: For production, add API key validation
   ```python
   API_KEY = os.environ.get("API_KEY")
   
   if request.headers.get("X-API-Key") != API_KEY:
       return {"error": "Unauthorized"}, 401
   ```

3. **HTTPS**: Cloud platforms provide free HTTPS; use only
4. **File Upload Limits**: Add file size validation
   ```python
   MAX_SIZE = 10 * 1024 * 1024  # 10 MB
   if request.content_length > MAX_SIZE:
       return {"error": "File too large"}, 413
   ```

---

## 📊 Monitoring & Logs

- **Render**: Built-in logs in dashboard
- **Cloud Run**: Use Google Cloud Logging
- **Local**: Docker logs: `docker logs -f CONTAINER_ID`

---

## 🎯 Next Steps

1. **Test locally** with `docker build` and `docker run`
2. **Choose platform**: Render (easiest) or Cloud Run (scalable)
3. **Deploy** using the respective guide above
4. **Share URL** for live demo during viva presentation
5. **Optional**: Add web UI frontend (React/Vue) to consume API

---

## Example: From Laptop to Live URL in 10 Minutes

```bash
# 1. Test locally
docker build -t mango-detector .
docker run -p 8080:8080 -v $(pwd)/saved_models:/app/saved_models mango-detector

# 2. Verify working
curl http://localhost:8080/health

# 3. Push to GitHub (already done)
git add app.py Dockerfile requirements-server.txt .dockerignore DEPLOY.md
git commit -m "Add deployment files"
git push

# 4. Go to Render, connect repo, click Deploy
# ✓ Live in 2-5 minutes!
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Model not found" | Mount volume or add download logic |
| "Port already in use" | Use `-p 9090:8080` to map to different port |
| "Out of memory" | Increase container memory; disable model caching |
| "Slow inference" | Add GPU instance; reduce image size; optimize model |

---

**Questions?** Check logs or reach out. Happy deploying! 🚀
