#!/usr/bin/env python3
"""
🌿 Mango Disease Project - Viva Preparation & Quick Demo
Simple script to help you prepare for the viva presentation
"""

print("=" * 70)
print("🌿 MANGO LEAF DISEASE DETECTION - VIVA PREPARATION")
print("=" * 70)

# Project Overview
print("\n📌 PROJECT OVERVIEW (30 seconds)")
print("-" * 70)
overview = """
This project builds an AI system to classify mango leaf diseases.

• Purpose: Help farmers diagnose leaf diseases quickly
• Model: Swin Transformer Tiny (transfer learning)
• Dataset: 4000 images, 8 disease classes
• Accuracy: 99.87% validation, 100% test
• Demo: Desktop GUI for real-time predictions
"""
print(overview)

# Dataset & Classes
print("\n📊 DATASET & CLASSES")
print("-" * 70)
classes = [
    "1. Anthracnose        - Fungal disease with dark lesions",
    "2. Bacterial Canker   - Water-soaked lesions with yellow halo",
    "3. Cutting Weevil     - Pest causing irregular holes",
    "4. Die Back           - Branch death from tip to base",
    "5. Gall Midge         - Abnormal leaf growths",
    "6. Healthy            - No disease detected",
    "7. Powdery Mildew     - White powdery coating",
    "8. Sooty Mould        - Black sooty coating"
]
for cls in classes:
    print(f"  {cls}")

# Model Architecture
print("\n🏗️ MODEL ARCHITECTURE (45 seconds)")
print("-" * 70)
architecture = """
Backbone: SwinTransformerTiny224 (ImageNet pretrained)
├── Input: 224×224×3 RGB image
├── Swin-Tiny blocks with window attention
└── Global Average Pooling

Head (Classification):
├── Dense(512) + BatchNorm + Dropout(0.5)
├── Dense(256) + BatchNorm + Dropout(0.4)
├── Dense(128) + Dropout(0.3)
└── Dense(8) + Softmax → 8 disease probabilities

Total Parameters: ~28 million
"""
print(architecture)

# Training Strategy
print("\n📈 TRAINING STRATEGY (Two-Phase Training)")
print("-" * 70)
training = """
Phase 1: Head Training (30 epochs)
├── Backbone: FROZEN (use pretrained features)
├── Train: Only the classification head
├── Optimizer: Adam (lr=1e-4)
└── Result: ~90% accuracy

Phase 2: Fine-Tuning (30 epochs)
├── Backbone: UNFROZEN (keep early layers frozen)
├── Train: Entire model with low learning rate
├── Optimizer: Adam (lr=5e-5)
└── Result: 99.87% accuracy ✅
"""
print(training)

# Hyperparameters
print("\n⚙️ HYPERPARAMETERS")
print("-" * 70)
params = """
Image Size:              224×224
Batch Size:              16
Epochs per Phase:        30
Validation Split:        80/20
Augmentation:            Flip, Rotate, Zoom, Contrast, Brightness
Optimizer:               Adam
Learning Rate (Ph1):     1e-4
Learning Rate (Ph2):     5e-5
Regularization:          L2(1e-4), Dropout, BatchNorm
Callbacks:               ReduceLROnPlateau, EarlyStopping
"""
print(params)

# Data Augmentation
print("\n🎨 DATA AUGMENTATION (Why?)")
print("-" * 70)
augmentation = """
Applied to training data only (not validation/test):
✓ RandomFlip (horizontal & vertical) - Handles leaf orientation
✓ RandomRotation(0.2)              - Leaf angle variation
✓ RandomZoom(0.2)                  - Camera distance variation
✓ RandomContrast(0.2)              - Lighting conditions
✓ RandomBrightness(0.1)            - Brightness changes

Result: Model learns from diverse real-world variations
"""
print(augmentation)

# Performance Results
print("\n📊 FINAL RESULTS")
print("-" * 70)
results = """
Phase 1 (Frozen Backbone):
  Training Accuracy:   ~87%
  Validation Accuracy: ~85%

Phase 2 (Fine-tuning):
  Training Accuracy:   99.99%
  Validation Accuracy: 99.87% ✅
  Test Accuracy:       100.0% ✅
"""
print(results)

# GUI Features
print("\n🖥️ GUI FEATURES (Desktop Application)")
print("-" * 70)
gui = """
Left Panel (35% width):
  • Image upload button
  • Image preview area (600×600)
  • Clear button

Right Panel (65% width - DOMINANT):
  • Large RED "ANALYZE LEAF" button
  • Results display:
    - Disease name (RED, highlighted)
    - Confidence % (GREEN, highlighted)
    - Severity level (color-coded)
    - Type & description
    - Treatment recommendations
    - Prevention strategies
    - All 8 predictions ranked

Color Scheme:
  • Dark background (#0a0e27)
  • Neon green header (#00d084)
  • Red accent button (#ff6b6b)
  • Blue results panel (#192847)
"""
print(gui)

# How to Run
print("\n🚀 HOW TO RUN")
print("-" * 70)
run_steps = """
Step 1: Open PowerShell in project folder

Step 2: Activate virtual environment
  .\.venv\Scripts\Activate.ps1

Step 3: Run the app
  python mango_ui_best.py

Step 4: Use the GUI
  1. Click "Choose Image"
  2. Select a mango leaf photo
  3. Click "ANALYZE LEAF"
  4. View disease, confidence, and treatment
"""
print(run_steps)

# Common Viva Questions
print("\n❓ LIKELY VIVA QUESTIONS & ANSWERS (1 min each)")
print("-" * 70)

questions = {
    "Q1: Why Swin Transformer?": 
        "A: Modern vision transformer with hierarchical windows, efficient attention, and strong ImageNet pretrained weights perfect for transfer learning on small datasets.",
    
    "Q2: Why two-phase training?":
        "A: Phase 1 trains only the head with frozen backbone to adapt to our 8 classes. Phase 2 unfreezes and fine-tunes the backbone slowly with low learning rate to preserve pretrained features.",
    
    "Q3: How did you avoid overfitting?":
        "A: Used data augmentation (flip, rotate, zoom, contrast, brightness), L2 regularization, dropout layers, batch normalization, and early stopping on validation accuracy.",
    
    "Q4: What is temperature scaling in the GUI?":
        "A: Post-hoc calibration technique applied at inference to sharpen softmax probabilities, making confidence scores more interpretable for display (T=0.15).",
    
    "Q5: How does inference work in GUI?":
        "A: Rebuild model architecture, load weights from .h5 file (avoids custom layer issues), preprocess image to 224×224 without normalization (model handles it), predict softmax, apply temperature scaling, display top class and confidence.",
    
    "Q6: What was the biggest challenge?":
        "A: Initial accuracy was low (33%) because EPOCHS=1. Fixed by increasing to 60 epochs (30+30), adding augmentation, and matching preprocessing between training and inference.",
    
    "Q7: How would you improve the model?":
        "A: More diverse training data, class balancing, hyperparameter tuning (batch size, learning rate), ensemble models, or better calibration methods like Platt scaling.",
    
    "Q8: Can this be deployed?":
        "A: Yes, with FastAPI/Flask for web API, or TFServing for production. Current GUI is desktop demo. Would need load balancing, monitoring, and retraining pipeline for real deployment."
}

for q, a in questions.items():
    print(f"\n{q}")
    print(f"{a}")

# Dataset Path
print("\n\n📍 IMPORTANT PATHS")
print("-" * 70)
paths = """
Dataset Location:
  C:\Users\ajayd\Downloads\MangDisease

Saved Model Location:
  saved_models/7/
    ├── model.keras
    ├── model_weights.weights.h5
    └── metadata.json

Project Files:
  ├── swintin_executed.ipynb    (Training notebook)
  ├── mango_ui_best.py          (GUI application)
  ├── requirements.txt          (Dependencies)
  └── README.md                 (Full documentation)
"""
print(paths)

# Final Tips
print("\n💡 VIVA TIPS")
print("-" * 70)
tips = """
✓ Know the dataset path and class names
✓ Be ready to explain two-phase training (why freeze, why unfreeze)
✓ Have one bug you fixed ready to discuss (e.g., double normalization or model loading)
✓ Understand why temperature scaling helps with confidence display
✓ Be able to run the GUI and explain what happens when you click buttons
✓ Know the exact accuracy numbers (99.87% val, 100% test)
✓ Explain how transfer learning helps with limited data
✓ Be ready to discuss trade-offs (accuracy vs speed, complexity vs interpretability)
"""
print(tips)

print("\n" + "=" * 70)
print("✅ You're ready! Good luck with your viva! 🌿")
print("=" * 70)
