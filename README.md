# Server DoAn - Deepfake Detection & Phishing Verification System

This project is the server-side source code for an AI-powered Deepfake detection and phishing domain risk analysis/verification system.

## 📦 Architecture & Data Loading

The project uses a cloud-hosted ZIP file to load weight files, models, and local environments.

**Why download via a ZIP file (using `ZIP_ID`)?**
> Contrary to the common approach of downloading individual model files or data chunks sequentially from a public directory, this project opted for a compressed ZIP download.
> 
> The reason is that the Deepfake detection directory structure contains numerous subfiles. Requesting the server to make successive connections to download each file individually often causes cloud storage platforms to misidentify the action as a **network attack or spam behavior (DDoS/Spam requests)**, leading to IP blocking mid-download.
> 
> To overcome this, the entire directory structure, base models, and weight files have been packaged into a single compressed archive (ZIP). This approach helps to:
> 1. Avoid being flagged as spam and guarantee smoother downloads.
> 2. Simplify the installation process (requires only a single extraction step).
> 3. Ensure source code integrity: prevents "missing file" errors even with future changes.

## 🔐 Environment Authentication (.env)

The system relies on configuration parameters and environment variables to connect directly to the Firebase Database and Cloud Storage containers. 

For **absolute system security reasons**, the application configuration file (`.env`), which contains the ZIP archive identifier `ZIP_ID` and the database URL `FIREBASE_DB_URL`, has been completely excluded from this public repository.

**📩 Contact for Access & Environment Config File (.env)**

To legally run or test the internal project environment locally, you can contact me directly via the following platforms to obtain the full `.env` configuration:

* **Zalo:** `0335295370`
* **Telegram:** [@noduong](https://t.me/noduong)
* **Email:** [nongduong0811@gmail.com](mailto:nongduong0811@gmail.com)

## 🚀 Local Test Setup Guide

1. Ensure you have installed the required dependencies via `pip`:
   ```bash
   pip install websockets nest-asyncio requests opencv-python python-dotenv
   ```

2. Create a `.env` file in the root directory with the following variable declarations (get the actual values by contacting the author):
   ```env
   FIREBASE_DB_URL=...
   ZIP_ID=...
   ```

3. Send an image file and a URL for client-side local testing using the Test script:
   ```bash
   python test.py
   ```
