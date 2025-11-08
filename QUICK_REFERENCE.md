# 🌿 Quick Reference Card - Mango Disease Detector

## File Structure at a Glance

```
research/
├── swintin_executed.ipynb       ← Training code (run this once)
├── mango_ui_best.py             ← Desktop app (run this for demo)
├── app.py                       ← REST API server
├── Dockerfile                   ← Container config
├── download_model.py            ← Download model from cloud
├── requirements.txt             ← GUI dependencies
├── requirements-server.txt      ← API dependencies
├── README.md                    ← Project overview
├── DEPLOY.md                    ← Full deployment guide
├── RENDER_DEPLOY.md             ← 5-min Render deployment
├── VIVA_CHECKLIST.md            ← Presentation guide
├── saved_models/7/              ← Model weights (local)
│   ├── model.keras
│   ├── model_weights.weights.h5
│   └── metadata.json
└── .venv/                       ← Virtual environment
```

---

## 1-Line Command Reference

### Setup
```bash
# Activate environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Run GUI Demo
```bash
python mango_ui_best.py
```

### Run REST API Locally
```bash
pip install -r requirements-server.txt
python app.py
```

### Test API
```bash
curl http://localhost:8080/
curl -X POST -F "file=@leaf.jpg" http://localhost:8080/predict
```

### Docker Local Test
```bash
docker build -t mango-detector .
docker run -p 8080:8080 -v $(pwd)/saved_models:/app/saved_models mango-detector
```

### Push to GitHub
```bash
git add .
git commit -m "Your message"
git push origin main
```

---

## Model Specs (Quick Lookup)

| Metric | Value |
|--------|-------|
| Architecture | Swin Transformer Tiny |
| Backbone Params | 28M |
| Input Size | 224×224 |
| Classes | 8 diseases |
| Val Accuracy | 99.87% |
| Test Accuracy | 100% |
| Training Phases | 2 (freeze + finetune) |
| Total Epochs | 60 (30+30) |
| Batch Size | 16 |
| Optimizer | Adam |
| Learning Rate (Ph1) | 1e-4 |
| Learning Rate (Ph2) | 5e-5 |
| Temperature Scaling | T=0.15 |
| Inference Time | 2s (CPU), 0.2s (GPU) |
| Model Size | 961 MB |

---

## Disease Classes (8 Total)

1. **Anthracnose** - fungal, dark lesions
2. **Bacterial Canker** - bacterial, canker on stems
3. **Cutting Weevil** - insect damage, holes
4. **Die Back** - branch death, browning
5. **Gall Midge** - insect, leaf distortion
6. **Healthy** - no disease
7. **Powdery Mildew** - fungal, white powder
8. **Sooty Mould** - fungal, black spots

---

## Viva Talking Points (30 seconds each)

### Why This Project?
> "Agricultural disease detection is critical for crop yield. Early detection allows preventive action. This ML system can assist farmers by providing instant leaf analysis."

### Model Choice: Swin Transformer
> "Swin uses self-attention to capture long-range leaf patterns. Pretrained on ImageNet, it provides superior transfer learning compared to CNN baselines. The tiny variant (28M params) is deployment-friendly."

### Training Strategy: Two-Phase
> "Phase 1 freezes backbone to preserve ImageNet features, learning rate 1e-4. Phase 2 fine-tunes entire model with 5e-5. This prevents catastrophic forgetting while maximizing accuracy."

### Accuracy Fix: From 33.5% to 99.87%
> "Initial EPOCHS=1 bug was the killer. After increasing to 60 epochs, fixing preprocessing double-normalization, and adding 5 augmentations, accuracy jumped to 99.87%. Temperature scaling then boosted confidence."

### Data Augmentation: Why 5 Techniques?
> "Flip, rotate, zoom, brightness, contrast. Each simulates real-world variation: leaf angle, camera distance, lighting. Critical for robust real-world deployment."

### Deployment Options: 3 Paths
> "Desktop GUI for local demo, REST API locally for testing, cloud deployment (Render/Cloud Run) for production scalability. Docker containerization ensures reproducibility."

---

## Pre-Viva Checklist (5 Min)

- [ ] GUI launches without errors
- [ ] Can upload test image
- [ ] Prediction shows disease + confidence >90%
- [ ] GitHub URL accessible
- [ ] Model files in saved_models/7/
- [ ] Can quote key metrics from memory
- [ ] Prepared for 5 likely questions (see VIVA_CHECKLIST.md)

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| "Module not found" | `pip install -r requirements.txt` |
| GUI window not visible | Alt+Tab, check taskbar |
| Model loading error | Verify saved_models/7/ exists |
| API connection refused | Is `python app.py` running? Check port 8080 |
| Docker build fails | `docker build --no-cache -t mango-detector .` |
| Accuracy too low on new images | Dataset shift - apply more augmentation |

---

## URLs & Links

- **GitHub Repository**: https://github.com/Ajaysubbumane/mango-leaf-disease-detector
- **Deploy to Render**: https://render.com (follow RENDER_DEPLOY.md)
- **Deploy to Cloud Run**: `gcloud run deploy...` (see DEPLOY.md)
- **Swin Transformer Paper**: https://arxiv.org/abs/2103.14030
- **TensorFlow Hub**: https://www.tensorflow.org/hub

---

## Viva Confidence Boosters

✅ You've achieved 99.87% accuracy - that's excellent  
✅ Model handles real-world variations with augmentation  
✅ Deployment-ready with 3 implementation options  
✅ Clean GitHub repository with documentation  
✅ Can explain every design decision  
✅ Fixed bugs systematically (debugging mindset)  

---

## After Viva: Next Steps

1. **Deploy to Render** (make live demo URL)
2. **Upload model to GitHub Releases** (enable easy deployment)
3. **Create Hugging Face Space** (web interface without code)
4. **Add web UI** (HTML + JavaScript for browser access)
5. **Collect real farm data** (improve real-world accuracy)

---

**Print this card and keep it with you during viva!**

Last updated: November 8, 2025
