#!/usr/bin/env python3
"""
Download model from GitHub Release
Useful for Render deployment or any environment without model files
"""

import os
import sys
import requests
from pathlib import Path
import zipfile
import io

# GitHub release download URL (update with your release)
RELEASE_URL = "https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download"
MODEL_DIR = Path("saved_models/7")
WEIGHTS_FILE = "model_weights.weights.h5"
METADATA_FILE = "metadata.json"

def download_file(url, dest_path):
    """Download file with progress"""
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(dest_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size:
                    percent = (downloaded / total_size) * 100
                    print(f"  Progress: {percent:.1f}%", end='\r')
    
    print(f"✓ Downloaded {dest_path}")

def download_model():
    """Download model files for deployment"""
    
    # Create directory
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[*] Model directory: {MODEL_DIR}")
    
    # Download files from GitHub release
    # Note: You need to upload model to a GitHub Release first
    
    release_version = "v1"  # Update this to your release tag
    
    files_to_download = [
        (WEIGHTS_FILE, f"{RELEASE_URL}/{release_version}/{WEIGHTS_FILE}"),
        (METADATA_FILE, f"{RELEASE_URL}/{release_version}/{METADATA_FILE}"),
    ]
    
    try:
        for filename, url in files_to_download:
            dest = MODEL_DIR / filename
            if dest.exists():
                print(f"[✓] {filename} already exists, skipping")
                continue
            
            try:
                download_file(url, dest)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    print(f"[!] {url} not found")
                    print("[!] Please upload model to GitHub Release first")
                    return False
                raise
        
        print("\n[✓] Model download complete!")
        print(f"[✓] Model ready at: {MODEL_DIR.absolute()}")
        return True
    
    except Exception as e:
        print(f"[✗] Download failed: {e}")
        return False

def alternative_download():
    """Alternative: Download from AWS S3 or Google Cloud Storage"""
    print("\n[!] GitHub Release method failed.")
    print("[*] Alternative: Upload model to:")
    print("    - AWS S3: https://aws.amazon.com/s3/")
    print("    - Google Cloud Storage: https://cloud.google.com/storage")
    print("    - Hugging Face: https://huggingface.co/")
    print("\n[*] Then update RELEASE_URL in this script with the download link")

if __name__ == "__main__":
    print("=" * 60)
    print("🌿 Mango Leaf Disease Detector - Model Downloader")
    print("=" * 60)
    
    # Check if model already exists
    if (MODEL_DIR / WEIGHTS_FILE).exists():
        print("[✓] Model already present!")
        sys.exit(0)
    
    # Try download
    if download_model():
        sys.exit(0)
    else:
        alternative_download()
        sys.exit(1)
