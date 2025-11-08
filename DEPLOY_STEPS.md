# 🚀 Deploy to Render - Step by Step

## ✅ Step 1: Create GitHub Release (For Model Files)

Your code is already on GitHub. Now create a Release with model files:

### Using GitHub Web UI (Easiest):

1. **Go to GitHub**: https://github.com/Ajaysubbumane/mango-leaf-disease-detector

2. **Click Releases** (on the right sidebar)

3. **Click "Create a new release"**

4. **Fill in the form:**
   - **Tag version**: `v7`
   - **Release title**: `Model v7 - 99.87% Accuracy`
   - **Description**: Copy this:
     ```
     # Mango Leaf Disease Detector - Model v7
     
     **Performance:**
     - Validation Accuracy: 99.87%
     - Test Accuracy: 100%
     - Inference Time: 2s (CPU)
     
     **Files:**
     - model_weights.weights.h5 (850 MB)
     - model.keras (100 MB)  
     - metadata.json (Training details)
     
     **Deployment:**
     Follow RENDER_DEPLOY.md for live deployment
     ```

5. **Upload Model Files:**
   - Click "Attach binaries"
   - Drag & drop these files:
     - `saved_models/7/model_weights.weights.h5`
     - `saved_models/7/model.keras`
     - `saved_models/7/metadata.json`

6. **Click "Publish release"**

✅ Done! Your model is now on GitHub Release v7

---

## ✅ Step 2: Deploy to Render

### A. Sign Up (First Time)

1. Go to: https://render.com
2. Click **Sign Up**
3. Choose **GitHub**
4. Click **Authorize Render** (allow access to your repos)

### B. Create Web Service

1. After login, click **New** → **Web Service**
2. Click **Connect to GitHub**
3. Search for: `mango-leaf-disease-detector`
4. Click **Connect**

### C. Configure Deployment

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `mango-detector` |
| **Environment** | `Docker` |
| **Build Command** | (leave empty) |
| **Start Command** | (leave empty) |
| **Instance Type** | `Free` |

### D. Add Environment Variables

1. Scroll down to **Environment**
2. Click **Add Environment Variable**
3. Add:
   ```
   KEY: PORT
   VALUE: 8080
   ```

### E. Deploy

Click **Create Web Service**

⏳ **Deployment will start automatically** (5-10 minutes)

---

## 🎯 Expected Result

After deployment completes, you'll get a **live URL** like:

```
https://mango-detector-xxxx.onrender.com
```

### Test Your Live API:

```bash
# 1. Check health
curl https://mango-detector-xxxx.onrender.com/health

# 2. Get diseases list
curl https://mango-detector-xxxx.onrender.com/diseases

# 3. View API docs
Open in browser: https://mango-detector-xxxx.onrender.com/
```

---

## ⚠️ Important Notes

### If Deployment Fails (Model Not Found):

**Quick Fix:**
1. Edit `Dockerfile` 
2. Add this line before `CMD` (around line 29):
   ```dockerfile
   RUN mkdir -p /app/saved_models/7 && \
       wget -O /app/saved_models/7/model_weights.weights.h5 \
       https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v7/model_weights.weights.h5 || true
   ```
3. Push to GitHub
4. Render will auto-redeploy

### Model Size Warning:

- `model_weights.weights.h5`: ~850 MB
- Upload may take 2-3 minutes on GitHub Release
- Download during build: ~2-3 minutes on Render

---

## ✅ Final Checklist

- [ ] GitHub Release v7 created with model files
- [ ] Render account created
- [ ] Web Service connected to GitHub
- [ ] Configuration filled in (Docker, Port 8080)
- [ ] Environment variable added (PORT=8080)
- [ ] Deployment started
- [ ] Waited 5-10 minutes for build/deploy
- [ ] Got live URL
- [ ] Tested health endpoint
- [ ] Got 200 OK response

---

## 🎉 You Now Have:

**Live API URL:**
```
https://mango-detector-xxxx.onrender.com
```

**Anyone can:**
1. View your GitHub: https://github.com/Ajaysubbumane/mango-leaf-disease-detector
2. Access your live API
3. Upload leaf image for prediction
4. See model details and treatment recommendations

---

## 📱 Share Your Project

**GitHub URL** (code):
```
https://github.com/Ajaysubbumane/mango-leaf-disease-detector
```

**Live API URL** (demo):
```
https://mango-detector-xxxx.onrender.com
```

Share these URLs in your viva, portfolio, or resume!

---

**Time needed:** ~20 minutes total
- 5 min: Create GitHub Release
- 10 min: Render deployment
- 5 min: Testing

Good luck! 🚀
