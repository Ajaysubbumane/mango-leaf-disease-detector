# 📦 GitHub Release Guide - Publishing Your Model

## Why Release on GitHub?

- ✅ Share model files (961 MB, too large for git)
- ✅ Enable one-click deployment to cloud
- ✅ Version your model releases
- ✅ Public distribution without needing AWS/GCS
- ✅ Track model updates alongside code

---

## Step 1: Prepare Model Files for Release

1. **Create release directory** (local):
```bash
mkdir -p release/saved_models/7
cp saved_models/7/model_weights.weights.h5 release/saved_models/7/
cp saved_models/7/model.keras release/saved_models/7/
cp saved_models/7/metadata.json release/saved_models/7/
```

2. **Create README for release** (optional but helpful):
```
release/saved_models/7/README.txt

Mango Leaf Disease Detector - Model v7
======================================
Files:
- model_weights.weights.h5 (~850 MB) - Model weights
- model.keras (~100 MB) - Full Keras model
- metadata.json - Training metadata

Usage:
1. Download model_weights.weights.h5
2. Place in saved_models/7/ directory
3. Run: python mango_ui_best.py

Accuracy: 99.87% validation, 100% test
Classes: 8 mango diseases
```

3. **Compress for faster download** (optional):
```bash
# On Windows PowerShell
Compress-Archive -Path release/saved_models -DestinationPath model_v7.zip
# Creates model_v7.zip (~200-300 MB due to compression)
```

---

## Step 2: Create GitHub Release

### Option A: Using GitHub Web UI (Easiest)

1. Go to: https://github.com/Ajaysubbumane/mango-leaf-disease-detector
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. Fill in:
   - **Tag version**: `v7` (or `v7.0.0`)
   - **Release title**: `Model v7 - 99.87% Accuracy`
   - **Description**:
     ```
     # Mango Leaf Disease Detector - Model v7
     
     **Performance:**
     - Validation Accuracy: 99.87%
     - Test Accuracy: 100%
     - Inference Time: 2s (CPU), 0.2s (GPU)
     
     **Architecture:**
     - Backbone: Swin Transformer Tiny
     - Classes: 8 mango diseases
     - Input: 224×224 RGB images
     
     **Files:**
     - model_weights.weights.h5 - 850 MB (weights only, fast loading)
     - model.keras - 100 MB (full model, slower but portable)
     - metadata.json - Training details
     
     **Installation:**
     1. Download model_weights.weights.h5
     2. Place in saved_models/7/
     3. Run: python mango_ui_best.py
     
     **Deployment:**
     See DEPLOY.md for cloud deployment instructions.
     ```

5. **Upload files**:
   - Drag & drop `model_weights.weights.h5`
   - Drag & drop `model.keras`
   - Drag & drop `metadata.json`
   - (Or upload `model_v7.zip` if compressed)

6. Check **"This is a pre-release"** if testing, uncheck for production
7. Click **Publish release**

### Option B: Using GitHub CLI (Command Line)

```bash
# Install GitHub CLI (if not already)
# macOS: brew install gh
# Windows: choco install gh
# Linux: sudo apt install gh

# Login
gh auth login

# Create release
gh release create v7 saved_models/7/model_weights.weights.h5 saved_models/7/model.keras saved_models/7/metadata.json \
  --title "Model v7 - 99.87% Accuracy" \
  --notes "See repository README for details"

# Or create draft first
gh release create v7 --draft --notes "Model v7 release"

# Then upload files
gh release upload v7 saved_models/7/model_weights.weights.h5
gh release upload v7 saved_models/7/model.keras
gh release upload v7 saved_models/7/metadata.json
```

---

## Step 3: Update download_model.py to Use Release

Edit `download_model.py`:

```python
# Change this line:
release_version = "v1"  # Update this to your release tag

# To:
release_version = "v7"  # Your actual release
```

Or update RELEASE_URL:

```python
RELEASE_URL = "https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download"
```

---

## Step 4: Test Release Download

```bash
# Delete local models to test download
Remove-Item saved_models -Recurse -Force

# Run downloader
python download_model.py

# Verify files exist
ls saved_models/7/
```

Expected output:
```
model.keras                    100 MB
model_weights.weights.h5       850 MB
metadata.json                  < 1 KB
```

---

## Step 5: Deploy Using Released Model

### Deploy to Render with Released Model

1. **Update Dockerfile** (optional, for production):
   ```dockerfile
   # Add this before CMD
   RUN mkdir -p /app/saved_models/7 && \
       wget -O /app/saved_models/7/model_weights.weights.h5 \
       https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v7/model_weights.weights.h5
   ```

2. **Or use download_model.py on startup**:
   - Render will execute `download_model.py` during build
   - Model downloads from GitHub Release automatically

### Deploy to Cloud Run

```bash
gcloud run deploy mango-detector \
  --image gcr.io/YOUR_PROJECT/mango-detector \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --env MODEL_URL="https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v7/model_weights.weights.h5"
```

---

## Step 6: Monitor Release

**Check download stats:**
- Go to Release page
- View download counts
- Monitor which version is most used

**Example Release URL:**
```
https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/v7
```

---

## Advanced: CI/CD Release Automation

Create `.github/workflows/release.yml`:

```yaml
name: Create Model Release

on:
  workflow_dispatch:  # Manual trigger
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            saved_models/7/model_weights.weights.h5
            saved_models/7/model.keras
            saved_models/7/metadata.json
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Then release by:
```bash
git tag v7
git push origin v7
# GitHub Actions automatically creates release
```

---

## Troubleshooting Release

| Problem | Solution |
|---------|----------|
| File too large (>100 MB) | Use Git LFS or compress with zip |
| Download is slow | Use CDN or cloud storage mirror |
| Release not visible | Check permissions, refresh page |
| Wrong file uploaded | Delete and re-upload |
| Need to update | Create new tag (v7.1, v8, etc) |

---

## After Release: Update README

Add to `README.md`:

```markdown
## 📥 Quick Deploy

Get the live API in 2 minutes:

1. Download model from [Release v7](https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/tag/v7)
2. Place in `saved_models/7/`
3. Follow [DEPLOY.md](DEPLOY.md) to deploy

**Already deployed?** Try the [live API](https://mango-detector-xxxx.onrender.com) (if deployed to Render)
```

---

## Next: Advanced Versioning

As you improve your model:

```bash
# Model v8 (after retraining)
git tag v8
# Create release v8 with new weights

# Keep old versions for reference
# Users can pick which version to use
```

This allows:
- ✅ Rolling back to previous model
- ✅ Comparing performance between versions
- ✅ A/B testing different models
- ✅ Versioned model serving in production

---

## Summary: The Full Flow

```
Code Update → Train Model → Improve Accuracy
                    ↓
         Save weights to saved_models/7/
                    ↓
         Create GitHub Release v7
                    ↓
    Upload model_weights.weights.h5
                    ↓
      Update download_model.py
                    ↓
         Push to GitHub (git push)
                    ↓
    Test: python download_model.py ✅
                    ↓
      Deploy to Render/Cloud Run
                    ↓
    Get live URL for viva demo 🎉
```

---

**Created**: November 8, 2025  
**Next Step**: Create v7 release and test deployment!
