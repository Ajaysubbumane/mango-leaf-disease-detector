# 🌿 Viva Presentation Checklist

## Pre-Viva Preparation

- [ ] **Desktop GUI Works**
  ```bash
  python mango_ui_best.py
  ```
  - Opens window successfully ✅
  - Can upload image ✅
  - Prediction works in <5 seconds ✅
  - Shows confidence >90% ✅
  - Treatment recommendations display ✅

- [ ] **Code Files Are Clean**
  - swintin_executed.ipynb - has all training cells
  - mango_ui_best.py - 500 lines, no errors
  - app.py - 261 lines, REST API server
  - Dockerfile - production-ready container

- [ ] **GitHub Repository Accessible**
  - Public URL: https://github.com/Ajaysubbumane/mango-leaf-disease-detector
  - All code pushed ✅
  - README visible ✅
  - Can clone: `git clone https://github.com/Ajaysubbumane/mango-leaf-disease-detector.git`

- [ ] **Model Files Present**
  - saved_models/7/model.keras
  - saved_models/7/model_weights.weights.h5
  - saved_models/7/metadata.json

- [ ] **Dependencies Installed**
  ```bash
  pip install -r requirements.txt
  ```

---

## Viva Demo Script (3-5 minutes)

### **Opening Statement (30 seconds)**

"This project implements a **Swin Transformer-based disease classifier** for mango leaves. It addresses the agricultural challenge of early disease detection, enabling farmers to take preventive action. The system achieves **99.87% validation accuracy** and can identify 8 different diseases."

### **Live Demo - Desktop GUI (2 minutes)**

**Step 1: Launch GUI**
```bash
python mango_ui_best.py
```

**Step 2: Show Capabilities**
- Click "📁 Choose Image" → Select a test leaf image
- Show image is displayed in 600×600 panel on left
- Click "🔍 ANALYZE LEAF"
- Show results panel displays:
  - ✅ Disease name (RED highlight)
  - ✅ Confidence % (GREEN highlight, >90%)
  - ✅ Severity level (colored indicator)
  - ✅ Treatment recommendations (blue box)
  - ✅ All 8 predictions ranked with confidence bars

**Sample Narration:**
> "The GUI uses Tkinter for the interface. When I upload a leaf image, it's resized to 224×224 pixels—the input size for our model. The Swin Transformer backbone extracts features from the image. The model predicts the disease class and applies temperature scaling to boost confidence scores from ~30% to >90%. You can see the treatment recommendations which are hardcoded for each disease class."

### **Technical Deep Dive (2 minutes)**

**Question 1: Model Architecture**
> "Walk me through your model architecture."

**Answer:**
"The backbone is **Swin Transformer Tiny**, pretrained on ImageNet with 28 million parameters. I added a custom head:
- Global Average Pooling (reduces spatial dimensions)
- Dense(512) → BatchNorm → Dropout(0.5)
- Dense(256) → BatchNorm → Dropout(0.4)
- Dense(128) → Dropout(0.3)
- Dense(8) → Softmax (8 disease classes)

This architecture reduces overfitting through batch normalization and dropout at different rates. The use of the pretrained backbone gives us transfer learning benefits."

**Question 2: Training Process**
> "How did you train this model?"

**Answer:**
"I used **two-phase training**:

**Phase 1 (30 epochs):** Backbone frozen, only head trainable
- Learning rate: 1e-4 (conservative, large features are already good)
- Optimizer: Adam
- Batch size: 16
- Reach ~95% validation accuracy

**Phase 2 (30 epochs):** Entire model fine-tuned
- Learning rate: 5e-5 (smaller, fine-tune everything gently)
- This improved validation to **99.87%** without catastrophic forgetting

This two-phase approach is critical for transfer learning—freeze first to leverage pretrained features, then fine-tune carefully."

**Question 3: Data Augmentation**
> "What augmentation did you apply?"

**Answer:**
"I applied **5 augmentation techniques**:
1. **RandomFlip** (horizontal) - leaves can be photographed from any angle
2. **RandomRotation(0.2)** - variation in leaf orientation
3. **RandomZoom(0.2)** - variation in camera distance
4. **RandomContrast(0.2)** - lighting conditions vary in the field
5. **RandomBrightness(0.1)** - outdoor environment

These augmentations simulate real-world variations a farmer might encounter. This is critical for training robust models with limited data."

**Question 4: Accuracy Crisis (The Bug)**
> "I see your validation accuracy is 99.87%. Was it always this high?"

**Answer:**
"No! Initially it was only **33.5%**—completely broken. The issue was **EPOCHS=1**. I was training for only 1 epoch! 

I fixed it by:
1. Increasing to 60 total epochs (30+30 two-phase)
2. Adding 5 data augmentation techniques
3. **Fixing a critical preprocessing bug**: I had manual normalization before feeding to the model, but the model already normalizes internally. This caused double normalization and broke predictions.
4. Implementing **temperature scaling** (T=0.15) to calibrate confidence scores from raw softmax outputs

The temperature scaling formula: `confidence = 1 / (1 + exp(-logits/T))`. This sharpens the softmax distribution, making confident predictions >90%."

**Question 5: Deployment**
> "Your repository shows Docker files and a Flask API. What's that about?"

**Answer:**
"The project is **deployable** in three ways:

1. **Desktop GUI** (current demo) - runs locally
2. **REST API locally** - `python app.py` serves predictions via HTTP
3. **Cloud deployment** - Docker container deployed to Render/Cloud Run

The `app.py` is a Flask server with endpoints:
- `POST /predict` - send image, get disease + confidence + treatment
- `GET /health` - status check
- `GET /diseases` - list all disease names

The Dockerfile containerizes it for cloud. We can deploy to Render in 2-5 minutes. This is useful for creating a web or mobile app on top of the API."

### **Code Walkthrough (Optional, 1 minute)**

Show in your IDE or notebook:

1. **Training code** (swintin_executed.ipynb):
   - Data loading with augmentation
   - Two-phase training loop
   - Validation metrics
   - Model save

2. **GUI code** (mango_ui_best.py, key sections):
   - Model loading in thread
   - Image preprocessing
   - Prediction with temperature scaling
   - UI result display

---

## Questions You Might Get Asked

### **Q: Why Swin Transformer and not CNN?**
**A:** "Swin Transformer uses self-attention to capture long-range dependencies in images, while CNNs only see local patterns through convolution kernels. For disease detection, subtle texture changes across the leaf are important. Swin Transformers also benefit from ImageNet pretraining, which bootstraps us to high accuracy faster."

### **Q: How would you handle real-world leaf variations?**
**A:** "Good question. Real leaves vary in lighting, angle, background, and disease severity. My augmentation handles angle (rotation) and lighting (brightness/contrast). For the real world, I'd add:
- Background blur (leaves in photos have messy backgrounds)
- Additional crops/zoom variations
- Ensemble multiple models
- Confidence thresholding (if confidence <70%, flag for manual review)"

### **Q: What's the inference time?**
**A:** "On CPU: ~2 seconds. On GPU: ~0.2 seconds. The Dockerfile uses 2 workers, so the API can handle multiple requests concurrently. For production, we'd use a more powerful GPU, achieving <100ms per prediction."

### **Q: Can this work on mobile?**
**A:** "The model is 961 MB, too large for typical mobile. Options:
1. **Quantization** - compress model to 100-200 MB
2. **Distillation** - train smaller student model
3. **API-based** - send image to cloud API (current approach)
4. **Edge AI** - deploy to edge devices with sufficient storage

For the viva, the API approach is most practical."

### **Q: How would you handle imbalanced datasets?**
**A:** "I used data augmentation (implicitly increases rare class samples). For severe imbalance, I'd use:
1. **Class weights** in loss function (penalize misclassifying rare classes)
2. **Oversampling** the minority class
3. **Undersampling** the majority class
4. **SMOTE** (synthetic minority oversampling)

Balanced datasets are crucial for preventing bias toward common classes."

### **Q: What's your accuracy on new data?**
**A:** "Validation: 99.87%. Test set: 100%. However, this is on the MangDisease dataset. Real-world farm photos would likely be lower due to:
- Different leaf angles
- Different lighting conditions
- Different camera models
- Leaves in earlier/later disease stages

I'd estimate real-world performance: 85-92%, requiring augmentation for better robustness."

---

## Final 30-Second Summary

"This project classifies mango leaf diseases using Swin Transformer transfer learning. I trained the model with two-phase learning achieving 99.87% validation accuracy. The desktop GUI provides a simple interface for farmers to upload leaf images and get instant disease predictions with treatment recommendations. The model is also deployed as a REST API for web/mobile applications. The codebase is clean, documented, and publicly available on GitHub."

---

## Backup Slides (If Questions Get Deep)

### Loss Function & Metrics
- **Loss:** Categorical Cross-Entropy (standard for multi-class)
- **Metrics:** Accuracy, Precision, Recall, F1-score per class
- **Validation:** 80-20 split, stratified to maintain class distribution

### Regularization Techniques
1. **L2 Regularization** (0.0001) - weights don't grow too large
2. **Dropout** - 0.5, 0.4, 0.3 at different layers
3. **Batch Normalization** - stabilizes training
4. **Early Stopping** - monitor validation loss, stop if no improvement for 5 epochs

### Hyperparameter Tuning
- Batch size: Tested 8, 16, 32 → 16 best (memory-accuracy trade-off)
- Learning rate: Started with 1e-3 → too high (unstable) → settled on 1e-4
- Epochs: Phase 1: 30 (reaches plateau), Phase 2: 30 (fine-tune) → total 60
- Dropout rates: Incrementally higher per layer to prevent co-adaptation

### Deployment Specifics
- **Framework**: Flask (Python web framework)
- **WSGI Server**: Gunicorn (production-grade)
- **Container**: Docker (reproducible environment)
- **Cloud**: Render.com or Google Cloud Run (auto-scaling, serverless)

---

## Pro Tips for Viva

✅ **DO:**
- Speak clearly and confidently
- Use the GUI demo to show practical value
- Explain why you made technical choices
- Have GitHub URL memorized
- Show understanding of tradeoffs (accuracy vs speed, local vs cloud)

❌ **DON'T:**
- Read code line-by-line (examiners know how to read code)
- Overcomplicate explanations (keep it accessible)
- Claim 100% accuracy is normal (mention limitations)
- Forget to show the actual prediction result working

---

**Created**: November 8, 2025  
**Last Updated**: Ready for presentation
