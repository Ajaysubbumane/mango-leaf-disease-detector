# Render Deployment Guide - Live in 5 Minutes

## ✅ Quick Deploy to Render (Recommended)

**Why Render?**
- ✅ Auto-detects Dockerfile from GitHub
- ✅ Free tier available (with limits)
- ✅ Automatic HTTPS
- ✅ One-click deploy
- ✅ No credit card needed for free tier

---

## 📋 Step-by-Step (Super Simple)

### **Step 1: Go to Render.com**
```
https://render.com
```
Click **Sign Up** → Use GitHub login (easiest)

### **Step 2: Create New Web Service**
1. Dashboard → **New** button
2. Select **Web Service**
3. Click **Connect to GitHub**
4. Find your repo: `mango-leaf-disease-detector`
5. Click **Connect**

### **Step 3: Configure Deployment**
Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `mango-detector` |
| **Environment** | `Docker` |
| **Plan** | `Free` (or Starter $7/mo for production) |
| **Region** | `Oregon` (us-west) |

### **Step 4: Advanced Settings (Optional)**
- **Build Command**: Leave empty (Render auto-detects Dockerfile)
- **Start Command**: Leave empty (Dockerfile specifies it)

### **Step 5: Deploy!**
Click **Create Web Service** and watch the logs scroll.

**Estimated time: 2-5 minutes** ⏱️

### **Step 6: Get Your URL**
After deployment, you get a URL like:
```
https://mango-detector-xxxx.onrender.com
```

---

## 🧪 Test Your Live API

Once deployed, test these endpoints:

```bash
# 1. Health check (verify running)
curl https://mango-detector-xxxx.onrender.com/health

# 2. Get API info
curl https://mango-detector-xxxx.onrender.com/

# 3. List diseases
curl https://mango-detector-xxxx.onrender.com/diseases

# 4. Predict (send a leaf image)
curl -X POST -F "file=@leaf.jpg" \
  https://mango-detector-xxxx.onrender.com/predict
```

Example response:
```json
{
  "predicted_disease": "Anthracnose",
  "confidence": 95.5,
  "severity": "HIGH",
  "treatment": "Apply copper fungicide..."
}
```

---

## ⚠️ IMPORTANT: Model Files

The Render container needs access to your model files. **Two options:**

### **Option A: Upload Model to GitHub Releases (Easier)**

1. Go to your GitHub repo → **Releases** (right sidebar)
2. **Create new release**
3. Upload your model files:
   - `saved_models/7/model_weights.weights.h5` (322 MB)
   - `saved_models/7/metadata.json`
4. Add download logic to `app.py` (I can help with this)

### **Option B: Use Cloud Storage (AWS S3 / Google Cloud Storage)**

1. Upload model to S3 or GCS
2. Generate signed URL
3. Modify `app.py` to download on startup

### **Option C: Mount Volume (Render Paid Plans Only)**

For free tier, stick with Options A or B.

---

## 🔧 If Model Upload Fails

Render may fail if the container is too large. Solution:

**Modify `app.py` to download model at runtime:**

Add this to the top of `app.py`:

```python
import requests
import os

def download_model_if_missing():
    """Download model from GitHub Release if not present"""
    WEIGHTS_PATH = "/app/saved_models/7/model_weights.weights.h5"
    
    if os.path.exists(WEIGHTS_PATH):
        print("✓ Model found locally")
        return
    
    print("⏳ Downloading model...")
    os.makedirs(os.path.dirname(WEIGHTS_PATH), exist_ok=True)
    
    # Replace with your GitHub release URL
    DOWNLOAD_URL = "https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v1/model_weights.weights.h5"
    
    response = requests.get(DOWNLOAD_URL, stream=True)
    with open(WEIGHTS_PATH, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print("✓ Model downloaded successfully")

# Call this before loading model:
@app.before_first_request
def startup():
    global model
    download_model_if_missing()  # <-- Add this line
    model = build_model()
```

---

## 📊 Monitoring

Once deployed:

1. **View Logs**: Render dashboard → Service → Logs tab
2. **Check Status**: Render dashboard shows live status
3. **Debug Issues**: Logs show any errors

---

## 💰 Pricing (Free Tier Info)

| Plan | Cost | Limits |
|------|------|--------|
| **Free** | $0 | Spins down after 15min inactivity |
| **Starter** | $7/mo | Always-on, good for demos |
| **Pro** | $12+/mo | Production features |

For viva demo, **free tier is fine** (just wake it up if needed).

---

## 🚨 Troubleshooting

| Issue | Fix |
|-------|-----|
| "Build failed" | Check logs; likely missing model files |
| "Service crashed" | Increase memory; Render auto-restarts |
| "Model not found" | Implement download logic (Option A) |
| "Timeout on predict" | Image too large; reduce timeout if needed |

---

## 🎯 Your Live Demo URL

After deployment, you'll have something like:
```
https://mango-detector-xxxx.onrender.com
```

**Share this during viva:**
> "Here's my live deployed API. You can test it by uploading a leaf image..."

---

## Next: Show This During Viva

```bash
# Live demo from phone/laptop:
# 1. Open: https://your-url/
# 2. Upload leaf image
# 3. Click predict
# 4. Show results in browser
```

---

**Ready to deploy? Start from Step 1 above!** 🚀

Need help with any step? Ask! ✨
