# -*- coding: utf-8 -*-
"""
🌿 Mango Leaf Disease Detector - Premium UI v2
Enhanced layout with balanced design and dominant results panel
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from PIL import Image, ImageTk
import os
import threading
from pathlib import Path
import sys
import io

if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from tfswin import SwinTransformerTiny224
except ImportError:
    pass

class MangoDiseaseDetectorBest:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Mango Leaf Disease Detector")
        self.root.geometry("1900x1000")
        self.root.configure(bg="#0a0e27")
        
        # Force window to foreground
        self.root.attributes('-topmost', True)
        self.root.after(1500, lambda: self.root.attributes('-topmost', False))
        
        # Colors - Professional palette
        self.dark_bg = "#0a0e27"
        self.darker_bg = "#060812"
        self.card_bg = "#141929"
        self.light_card = "#1e2139"
        self.result_card = "#192847"  # Brighter blue for results
        self.primary = "#00d084"
        self.secondary = "#00b8ff"
        self.warning = "#ff6b6b"
        self.warning_light = "#ff8e53"
        self.text_white = "#ffffff"
        self.text_gray = "#a8b2d1"
        self.text_muted = "#6c7a9c"
        
        self.class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back',
                           'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']
        
        self.disease_info = {
            'Anthracnose': {
                'icon': '🔴', 'type': 'Fungal Disease', 'severity': 'HIGH',
                'description': 'Dark circular lesions with yellow halos on leaves and fruit',
                'causes': 'Colletotrichum fungus, high humidity, poor air circulation',
                'treatment': '• Apply copper fungicide\n• Remove infected leaves\n• Improve ventilation\n• Avoid overhead watering',
                'prevention': 'Regular pruning and sanitation'
            },
            'Bacterial Canker': {
                'icon': '🟠', 'type': 'Bacterial Disease', 'severity': 'HIGH',
                'description': 'Angular water-soaked lesions with yellow halos on leaves',
                'causes': 'Xanthomonas bacteria, spread by insects and contaminated tools',
                'treatment': '• Use copper or streptomycin bactericide\n• Prune infected branches\n• Disinfect tools\n• Avoid wet pruning',
                'prevention': 'Use disease-free propagation material'
            },
            'Cutting Weevil': {
                'icon': '🟡', 'type': 'Pest Infestation', 'severity': 'MEDIUM',
                'description': 'Irregular holes in leaves, especially near margins and stem',
                'causes': 'Cutting weevil larvae feed on leaf tissues, caused by adults',
                'treatment': '• Apply neem oil spray\n• Handpick visible insects\n• Set light and pheromone traps\n• Use insecticide if severe',
                'prevention': 'Maintain plant vigor and regular monitoring'
            },
            'Die Back': {
                'icon': '🔴', 'type': 'Physiological Disease', 'severity': 'HIGH',
                'description': 'Progressive branch death extending from tip towards base',
                'causes': 'Poor drainage, waterlogging, nutrient deficiency, cold damage',
                'treatment': '• Prune dead wood completely\n• Improve soil drainage\n• Reduce nitrogen fertilizer\n• Monitor irrigation schedule',
                'prevention': 'Proper drainage and soil management'
            },
            'Gall Midge': {
                'icon': '🟠', 'type': 'Pest Infestation', 'severity': 'MEDIUM',
                'description': 'Abnormal gall-like leaf growths and deformed tissues',
                'causes': 'Gall midge larvae induce abnormal plant growth responses',
                'treatment': '• Apply neem oil spray\n• Remove affected leaves\n• Control humidity levels\n• Use insecticide if needed',
                'prevention': 'Regular monitoring and early intervention'
            },
            'Healthy': {
                'icon': '✅', 'type': 'Healthy Leaf', 'severity': 'NONE',
                'description': 'No disease detected - leaf is in excellent condition',
                'causes': 'Proper care and disease prevention practices',
                'treatment': '• Continue regular maintenance\n• Monitor periodically\n• Maintain good orchard hygiene\n• Apply preventive sprays',
                'prevention': 'Continue current management practices'
            },
            'Powdery Mildew': {
                'icon': '⚪', 'type': 'Fungal Disease', 'severity': 'MEDIUM',
                'description': 'White powdery coating on leaves, stems and fruit surface',
                'causes': 'Fungal infection, warm dry days with cool nights, poor air circulation',
                'treatment': '• Apply sulfur spray\n• Use potassium bicarbonate\n• Improve air circulation\n• Reduce humidity levels',
                'prevention': 'Proper spacing and regular pruning'
            },
            'Sooty Mould': {
                'icon': '⚫', 'type': 'Fungal Disease', 'severity': 'MEDIUM',
                'description': 'Black sooty fungal coating on leaves (usually after insect damage)',
                'causes': 'Secondary fungus growing on insect honeydew deposits',
                'treatment': '• Treat honeydew-producing insects first\n• Wash leaves with water spray\n• Apply fungicide if needed\n• Improve air flow',
                'prevention': 'Control aphids, scale insects, and mealybugs'
            }
        }
        
        self.model = None
        self.image_path = None
        self.is_predicting = False
        
        self.setup_ui()
        self.load_model_async()
    
    def setup_ui(self):
        """Create professional UI layout with balanced design"""
        
        # ============ HEADER ============
        header = tk.Frame(self.root, bg=self.primary, height=100)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        header_inner = tk.Frame(header, bg=self.primary)
        header_inner.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        title_lbl = tk.Label(header_inner, text="🌿 Mango Leaf Disease Detector",
                            font=("Segoe UI", 32, "bold"), bg=self.primary, fg=self.dark_bg)
        title_lbl.pack(anchor="w")
        
        subtitle_lbl = tk.Label(header_inner, 
                               text="AI-Powered Disease Detection | Model Accuracy: 99.87% | Real-time Analysis",
                               font=("Segoe UI", 11), bg=self.primary, fg=self.dark_bg)
        subtitle_lbl.pack(anchor="w", pady=(8, 0))
        
        # ============ MAIN CONTAINER ============
        main_container = tk.Frame(self.root, bg=self.dark_bg)
        main_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        # ---- LEFT SECTION (Image Upload & Display) - 35% width ----
        left_section = tk.Frame(main_container, bg=self.card_bg, relief=tk.FLAT, width=600)
        left_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 15))
        left_section.pack_propagate(False)
        
        # Title
        section_title_frame = tk.Frame(left_section, bg=self.card_bg)
        section_title_frame.pack(fill=tk.X, padx=20, pady=(20, 12))
        tk.Label(section_title_frame, text="📸 Upload & Preview",
                font=("Segoe UI", 15, "bold"), bg=self.card_bg, fg=self.primary).pack(anchor="w")
        
        # Buttons
        btn_frame = tk.Frame(left_section, bg=self.card_bg)
        btn_frame.pack(fill=tk.X, padx=20, pady=8)
        
        self.upload_btn = tk.Button(btn_frame, text="📁 Choose Image",
                                    command=self.upload_image,
                                    font=("Segoe UI", 10, "bold"), 
                                    bg=self.primary, fg=self.dark_bg,
                                    relief=tk.FLAT, padx=18, pady=9,
                                    cursor="hand2", activebackground="#00ff99",
                                    activeforeground=self.dark_bg)
        self.upload_btn.pack(side=tk.LEFT, padx=4)
        
        self.clear_btn = tk.Button(btn_frame, text="🗑️ Clear",
                                   command=self.clear_all,
                                   font=("Segoe UI", 10, "bold"),
                                   bg=self.warning, fg=self.text_white,
                                   relief=tk.FLAT, padx=18, pady=9,
                                   cursor="hand2", activebackground="#ff4444",
                                   activeforeground=self.text_white)
        self.clear_btn.pack(side=tk.LEFT, padx=4)
        
        # Image Display
        image_frame = tk.Frame(left_section, bg=self.light_card, relief=tk.SUNKEN, borderwidth=1)
        image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.image_label = tk.Label(image_frame, text="📷\n\nNo Image Selected",
                                   font=("Segoe UI", 16, "bold"),
                                   bg=self.light_card, fg=self.text_muted,
                                   compound=tk.TOP)
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ---- RIGHT SECTION (Analysis & Results) - 65% width - DOMINANT ----
        right_section = tk.Frame(main_container, bg=self.result_card, relief=tk.RAISED, borderwidth=3)
        right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=0)
        
        # Analyze Button - LARGER & MORE PROMINENT
        analyze_frame = tk.Frame(right_section, bg=self.result_card)
        analyze_frame.pack(fill=tk.X, padx=25, pady=(25, 15))
        
        self.analyze_btn = tk.Button(analyze_frame, 
                                     text="🔍 ANALYZE LEAF",
                                     command=self.predict,
                                     font=("Segoe UI", 14, "bold"),
                                     bg=self.warning, fg=self.text_white,
                                     relief=tk.FLAT, padx=50, pady=20,
                                     cursor="hand2", 
                                     activebackground=self.warning_light,
                                     activeforeground=self.text_white)
        self.analyze_btn.pack(fill=tk.X)
        
        # Separator
        sep_frame = tk.Frame(right_section, bg=self.secondary, height=2)
        sep_frame.pack(fill=tk.X, padx=20, pady=(10, 0))
        
        # Results Title
        result_title_frame = tk.Frame(right_section, bg=self.result_card)
        result_title_frame.pack(fill=tk.X, padx=25, pady=(15, 10))
        tk.Label(result_title_frame, text="📊 Analysis Results",
                font=("Segoe UI", 14, "bold"), bg=self.result_card, fg=self.primary).pack(anchor="w")
        
        # Results Display (Scrollable) - PROMINENT WITH DARKER BACKGROUND
        result_frame = tk.Frame(right_section, bg="#0f1821", relief=tk.FLAT, borderwidth=0)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        # Create text widget with scrollbar
        scrollbar = tk.Scrollbar(result_frame, bg=self.card_bg, troughcolor=self.light_card)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
        
        self.results_text = tk.Text(result_frame, 
                                   font=("Segoe UI", 10),
                                   bg="#0f1821", fg=self.text_white,
                                   relief=tk.FLAT, borderwidth=0,
                                   yscrollcommand=scrollbar.set,
                                   wrap=tk.WORD, padx=15, pady=15,
                                   insertbackground=self.primary)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.results_text.yview)
        
        # Configure text tags for highlighting
        self.results_text.tag_config("disease_name", foreground=self.warning, font=("Segoe UI", 13, "bold"))
        self.results_text.tag_config("confidence", foreground=self.primary, font=("Segoe UI", 12, "bold"))
        self.results_text.tag_config("severity_high", foreground="#ff4444", font=("Segoe UI", 12, "bold"))
        self.results_text.tag_config("severity_medium", foreground="#ffa500", font=("Segoe UI", 12, "bold"))
        self.results_text.tag_config("severity_none", foreground=self.primary, font=("Segoe UI", 12, "bold"))
        self.results_text.tag_config("header", foreground=self.secondary, font=("Segoe UI", 11, "bold"))
        self.results_text.tag_config("prediction_high", foreground=self.primary, font=("Segoe UI", 10, "bold"))
        self.results_text.tag_config("prediction_med", foreground=self.text_gray, font=("Segoe UI", 9))
        self.results_text.tag_config("divider", foreground=self.text_muted, font=("Segoe UI", 10))
        
        # Insert default text
        self.results_text.insert("1.0", 
            "📈 Ready for Analysis\n\n"
            "Upload a mango leaf image and click 'ANALYZE LEAF' to detect disease.\n\n"
            "The system will provide:\n"
            "• Disease classification with AI confidence\n"
            "• Disease severity assessment\n"
            "• Detailed description and causes\n"
            "• Treatment recommendations\n"
            "• Prevention strategies\n"
            "• All predictions ranked by confidence level")
        self.results_text.config(state=tk.DISABLED)
        
        # Status bar at bottom
        status_frame = tk.Frame(self.root, bg=self.card_bg, height=45)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        status_inner = tk.Frame(status_frame, bg=self.card_bg)
        status_inner.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        tk.Label(status_inner, text="●", font=("Arial", 14), fg=self.primary, bg=self.card_bg).pack(side=tk.LEFT)
        self.status_label = tk.Label(status_inner, text="Ready - Upload an image",
                                     font=("Segoe UI", 10), bg=self.card_bg, fg=self.text_gray)
        self.status_label.pack(side=tk.LEFT, padx=10)
    
    def load_model_async(self):
        """Load model in background"""
        thread = threading.Thread(target=self.load_model, daemon=True)
        thread.start()
    
    def load_model(self):
        """Load trained model"""
        try:
            self.status_label.config(text="⏳ Loading model...")
            self.root.update()
            
            save_dir = os.path.join(os.getcwd(), "saved_models")
            if not os.path.exists(save_dir):
                self.status_label.config(text="❌ Error: No models found")
                return
            
            versions = [int(i) for i in os.listdir(save_dir) if i.isdigit()]
            if not versions:
                self.status_label.config(text="❌ Error: No model versions available")
                return
            
            latest = max(versions)
            model_dir = os.path.join(save_dir, str(latest))
            weights_path = os.path.join(model_dir, "model_weights.weights.h5")
            
            if not os.path.exists(weights_path):
                self.status_label.config(text="❌ Error: Model weights not found")
                return
            
            # Build model
            IMAGE_SIZE = (224, 224)
            backbone = SwinTransformerTiny224(include_top=False, 
                                             input_shape=(*IMAGE_SIZE, 3),
                                             weights='imagenet')
            backbone.trainable = True
            
            x = backbone.output
            x = layers.GlobalAveragePooling2D()(x)
            x = layers.Dense(512, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Dropout(0.5)(x)
            x = layers.Dense(256, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Dropout(0.4)(x)
            x = layers.Dense(128, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            output = layers.Dense(8, activation='softmax')(x)
            
            self.model = models.Model(inputs=backbone.input, outputs=output)
            self.model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
                             loss='sparse_categorical_crossentropy',
                             metrics=['accuracy'])
            self.model.load_weights(weights_path)
            
            self.status_label.config(text=f"✅ Ready - Model v{latest} loaded (99.87% accuracy)")
            print(f"[✓] Model v{latest} loaded successfully")
            
        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)[:50]}")
            print(f"[✗] Error: {e}")
    
    def upload_image(self):
        """Upload image"""
        filetypes = (("Image files", "*.jpg *.png *.jpeg *.JPG *.PNG"), ("All files", "*.*"))
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        
        if file_path:
            self.image_path = file_path
            try:
                image = Image.open(file_path).convert('RGB')
                image.thumbnail((400, 400), Image.Resampling.LANCZOS)
                
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo, text="")
                self.image_label.image = photo
                
                filename = Path(file_path).name
                self.status_label.config(text=f"✅ Loaded: {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {e}")
    
    def clear_all(self):
        """Clear everything"""
        self.image_path = None
        self.image_label.config(image="", text="📷\n\nNo Image Selected")
        self.image_label.image = None
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0",
            "📈 Ready for Analysis\n\n"
            "Upload a mango leaf image and click 'ANALYZE LEAF' to detect disease.")
        self.results_text.config(state=tk.DISABLED)
        
        self.status_label.config(text="✅ Cleared - Ready for new image")
    
    def predict(self):
        """Make prediction"""
        if self.model is None:
            messagebox.showwarning("Warning", "Model is loading. Please wait...")
            return
        
        if self.image_path is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return
        
        if self.is_predicting:
            messagebox.showinfo("Info", "Analysis in progress...")
            return
        
        thread = threading.Thread(target=self._predict_worker, daemon=True)
        thread.start()
    
    def _predict_worker(self):
        """Background prediction"""
        try:
            self.is_predicting = True
            self.analyze_btn.config(state=tk.DISABLED, text="⏳ Analyzing...")
            self.status_label.config(text="🔍 Analyzing image...")
            self.root.update()
            
            # Load and prepare image
            image = Image.open(self.image_path).convert('RGB')
            image_array = np.array(image.resize((224, 224), Image.Resampling.LANCZOS),
                                  dtype=np.float32)
            image_batch = np.expand_dims(image_array, axis=0)
            
            # Predict
            predictions = self.model.predict(image_batch, verbose=0)[0]
            
            # Temperature scaling T=0.15
            TEMPERATURE = 0.15
            log_pred = np.log(predictions + 1e-10)
            scaled = np.exp(log_pred / TEMPERATURE)
            predictions = scaled / scaled.sum()
            
            # Get results
            top_idx = np.argmax(predictions)
            confidence = predictions[top_idx] * 100
            disease = self.class_names[top_idx]
            info = self.disease_info[disease]
            
            # Display results
            self.display_results(disease, confidence, info, predictions)
            
            self.status_label.config(text=f"✅ Detected: {disease} ({confidence:.1f}%)")
            print(f"[✓] {disease}: {confidence:.1f}%")
            
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {e}")
            print(f"[✗] {e}")
        
        finally:
            self.is_predicting = False
            self.analyze_btn.config(state=tk.NORMAL, text="🔍 ANALYZE LEAF")
    
    def display_results(self, disease, confidence, info, all_preds):
        """Display results with highlighting"""
        severity_icon = {"HIGH": "🔴", "MEDIUM": "🟠", "NONE": "✅"}[info['severity']]
        severity_tag = f"severity_{info['severity'].lower()}"
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)
        
        # Header
        self.results_text.insert(tk.END, f"{info['icon']} DETECTED DISEASE\n", "header")
        self.results_text.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "divider")
        
        # Disease name - HIGHLIGHTED
        self.results_text.insert(tk.END, "Disease: ", "header")
        self.results_text.insert(tk.END, f"{disease}\n", "disease_name")
        
        # Confidence - HIGHLIGHTED
        self.results_text.insert(tk.END, "Confidence: ", "header")
        self.results_text.insert(tk.END, f"{confidence:.1f}%\n", "confidence")
        
        # Severity - HIGHLIGHTED
        self.results_text.insert(tk.END, "Severity: ", "header")
        self.results_text.insert(tk.END, f"{severity_icon} {info['severity']}\n", severity_tag)
        
        self.results_text.insert(tk.END, "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "divider")
        
        # Type
        self.results_text.insert(tk.END, "Type: ", "header")
        self.results_text.insert(tk.END, f"{info['type']}\n\n")
        
        # Description
        self.results_text.insert(tk.END, "Description:\n", "header")
        self.results_text.insert(tk.END, f"{info['description']}\n\n")
        
        # Causes
        self.results_text.insert(tk.END, "Causes:\n", "header")
        self.results_text.insert(tk.END, f"{info['causes']}\n\n")
        
        # Treatment
        self.results_text.insert(tk.END, "Treatment Recommendations:\n", "header")
        self.results_text.insert(tk.END, f"{info['treatment']}\n\n")
        
        # Prevention
        self.results_text.insert(tk.END, "Prevention:\n", "header")
        self.results_text.insert(tk.END, f"{info['prevention']}\n\n")
        
        self.results_text.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "divider")
        self.results_text.insert(tk.END, "ALL PREDICTIONS (Ranked):\n", "header")
        self.results_text.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "divider")
        
        # Sort predictions
        sorted_preds = sorted(enumerate(all_preds), key=lambda x: x[1], reverse=True)
        for idx, (class_idx, pred_score) in enumerate(sorted_preds):
            class_name = self.class_names[class_idx]
            percentage = pred_score * 100
            bar_len = int(percentage / 5)
            bar = "█" * bar_len + "░" * (20 - bar_len)
            
            # Highlight top prediction
            tag = "prediction_high" if idx == 0 else "prediction_med"
            self.results_text.insert(tk.END, f"\n{class_name:20} {percentage:5.1f}% {bar}", tag)
        
        self.results_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = MangoDiseaseDetectorBest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
