# 🎯 DEPLOYMENT ACTION PLAN - Mango Detector

## Current Status
✅ Code on GitHub  
✅ Documentation complete  
✅ Model trained (99.87% accuracy)  
⏳ **Next: Deploy to Render (Make it Live!)**

---

## 🚀 PHASE 1: Create GitHub Release (5 minutes)

### What: Upload your model files to GitHub Release

### Why: Models are too large (961 MB) to store in git, but Render needs them for deployment

### How:

1. **Open your GitHub repository:**
   ```
   https://github.com/Ajaysubbumane/mango-leaf-disease-detector
   ```

2. **Find Releases section:**
   - Look at the right side of the page
   - Click on **Releases** (looks like a tag icon)

3. **Click: "Create a new release"**
   - Or go directly: https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/new

4. **Fill in the form:**

   **Tag version:** `v7`
   
   **Release title:** `Model v7 - 99.87% Accuracy`
   
   **Description:**
   ```
   # Mango Leaf Disease Detector - Model v7
   
   **Performance Metrics:**
   - Validation Accuracy: 99.87%
   - Test Accuracy: 100%
   - Inference Time: 2s (CPU), 0.2s (GPU)
   - Confidence Calibration: Temperature Scaling T=0.15
   
   **Model Details:**
   - Architecture: Swin Transformer Tiny (28M parameters)
   - Input Size: 224×224 RGB images
   - Output: 8 disease classifications
   - Classes: Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Healthy, Powdery Mildew, Sooty Mould
   
   **Files Included:**
   - model_weights.weights.h5 (~850 MB) - Model weights
   - model.keras (~100 MB) - Full Keras model
   - metadata.json - Training metadata
   
   **Deployment:**
   This release is used for Render deployment. See RENDER_DEPLOY.md for instructions.
   ```

5. **Upload model files:**
   - Click in the **"Attach binaries"** area (or drag-drop)
   - Upload these 3 files from `saved_models/7/`:
     1. `model_weights.weights.h5` (wait for upload, ~2-3 min)
     2. `model.keras` (wait for upload)
     3. `metadata.json` (quick)

6. **Publish the release:**
   - Click **"Publish release"** button

✅ **PHASE 1 COMPLETE** - You now have a v7 release with model files!

---

## 🚀 PHASE 2: Deploy to Render (10 minutes)

### What: Deploy your API to a live cloud server

### Result: Your project will be accessible worldwide at `https://mango-detector-xxxx.onrender.com`

### How:

1. **Go to Render:**
   ```
   https://render.com
   ```

2. **Sign Up:**
   - Click **Sign up**
   - Choose **GitHub** (easiest)
   - Click **Authorize Render** when prompted

3. **Create Web Service:**
   - After login, click **New** button (top right)
   - Select **Web Service**
   - Click **Connect to GitHub** (under "Deploy a repository")

4. **Select Your Repository:**
   - Search for: `mango-leaf-disease-detector`
   - Click **Connect**

5. **Configure Deployment:**

   | Setting | Value |
   |---------|-------|
   | **Name** | `mango-detector` |
   | **Environment** | `Docker` |
   | **Build Command** | (leave empty - auto-detects Dockerfile) |
   | **Start Command** | (leave empty - auto-detects Dockerfile) |
   | **Instance Type** | `Free` (or Starter for $7/month unlimited) |

6. **Add Environment Variable:**
   - Scroll to **Environment** section
   - Click **Add Environment Variable**
   - **KEY:** `PORT`
   - **VALUE:** `8080`

7. **Deploy:**
   - Click **Create Web Service** (blue button, bottom right)
   - Render will start building immediately! ⏳

✅ **PHASE 2 STARTED** - Render is now building your Docker image!

---

## ⏳ WAIT FOR DEPLOYMENT (5-10 minutes)

### Watch the log:
- Render shows live build logs
- You'll see:
  1. "Building Docker image..." (3-5 min)
  2. "Deploying..." (1-2 min)
  3. "Live" (green status - YOU'RE DONE!)

### What's happening:
1. Docker image building from your Dockerfile
2. Installing all Python dependencies
3. Downloading model from GitHub Release v7
4. Starting Gunicorn server on port 8080
5. Running health checks

### If it fails:
- See **Troubleshooting** section below

---

## 🎉 PHASE 3: Test Your Live API (2 minutes)

### Once "Live" shows up:

1. **Click the URL** (looks like `https://mango-detector-xxxx.onrender.com`)

2. **Test these endpoints:**

   **A) Health Check** (should show "ok")
   ```
   https://mango-detector-xxxx.onrender.com/health
   ```

   **B) API Documentation**
   ```
   https://mango-detector-xxxx.onrender.com/
   ```

   **C) Disease List**
   ```
   https://mango-detector-xxxx.onrender.com/diseases
   ```

3. **If you see JSON responses:** ✅ **SUCCESS!**

---

## 🔗 YOUR LIVE PROJECT URL

After successful deployment, share this URL:

```
https://mango-detector-xxxx.onrender.com
```

**Replace `xxxx` with the actual Render-generated name**

---

## 📋 COMPLETE DEPLOYMENT CHECKLIST

- [ ] **Step 1: Created GitHub Release v7**
  - [ ] Tagged as `v7`
  - [ ] Uploaded model_weights.weights.h5
  - [ ] Uploaded model.keras
  - [ ] Uploaded metadata.json

- [ ] **Step 2: Deployed to Render**
  - [ ] Signed up on Render.com
  - [ ] Connected GitHub repo
  - [ ] Set Name: mango-detector
  - [ ] Set Environment: Docker
  - [ ] Added PORT environment variable
  - [ ] Clicked "Create Web Service"

- [ ] **Step 3: Waited for Deployment**
  - [ ] Build completed (logs show "Live")
  - [ ] Service is running

- [ ] **Step 4: Tested Live API**
  - [ ] Health endpoint responds
  - [ ] API documentation page loads
  - [ ] Diseases list endpoint works

- [ ] **Step 5: Ready to Share**
  - [ ] Got live URL
  - [ ] Bookmarked/copied URL
  - [ ] Ready to share in viva/portfolio

---

## ⚠️ TROUBLESHOOTING

### Issue: "Deployment failed - model not found"

**Fix:** Dockerfile needs to download model from GitHub Release

Edit `Dockerfile` - add this line before the `CMD` line:

```dockerfile
RUN mkdir -p /app/saved_models/7 && \
    wget -O /app/saved_models/7/model_weights.weights.h5 \
    https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v7/model_weights.weights.h5 || true

# Run with gunicorn (production server)
CMD exec gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 2 --worker-class gthread --timeout 120 app:app
```

Then push to GitHub:
```bash
git add Dockerfile
git commit -m "Fix: Add model download in Dockerfile"
git push origin main
```

Render will auto-redeploy with the fix.

### Issue: "Service keeps crashing"

Check the logs in Render:
1. Go to your Render dashboard
2. Click on your service
3. Look at **Logs** tab
4. Look for error messages

Common issues:
- Model file not downloaded
- Port not responding
- Dependencies missing (check requirements-server.txt)

### Issue: "Build taking too long"

Don't worry! Large models can take time to download (~2-3 min on Render servers).

If it's been >15 minutes:
- Check the logs
- Try clicking **Manual Deploy** to restart

---

## 🎊 SUCCESS! You Now Have:

### **Live Mango Disease Detector API** 🚀

**Features:**
- ✅ Publicly accessible 24/7
- ✅ Anyone can upload leaf images
- ✅ Get disease predictions in real-time
- ✅ Treatment recommendations included
- ✅ View model details and accuracy

### **Share These URLs:**

**Your GitHub Repository:**
```
https://github.com/Ajaysubbumane/mango-leaf-disease-detector
```

**Your Live API:**
```
https://mango-detector-xxxx.onrender.com
```

**Model Release:**
```
https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/tag/v7
```

---

## 📝 NEXT STEPS (Optional)

1. **Create a simple web interface** (HTML + JavaScript)
   - So people can drag-drop images instead of using curl

2. **Add to your portfolio**
   - Link to GitHub repo
   - Link to live API
   - Mention 99.87% accuracy

3. **Share on social media**
   - LinkedIn: Share your achievement
   - Twitter: Show live demo
   - Portfolio website: Add project link

4. **Prepare for viva**
   - Demo the live API
   - Explain deployment architecture
   - Show GitHub repository

---

## ✨ Summary

| Task | Time | Status |
|------|------|--------|
| Create GitHub Release | 5 min | ⏳ Do now |
| Deploy to Render | 10 min | ⏳ Do now |
| Wait for build | 5-10 min | ⏳ Automatic |
| Test live API | 2 min | ✅ After live |
| Share URL | 1 min | ✅ Final |

**Total time: ~25 minutes**

---

**Ready? Let's make your project live!** 🎉

Start with **Step 1: Create GitHub Release v7**

Questions? Check the Troubleshooting section above.

Good luck! 🚀
