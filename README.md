# 🎬 Video Subtitle Remover (Computer Vision)

A simple Computer Vision tool that removes hardcoded subtitles from videos using:

- Edge Detection
- Morphological Processing
- Inpainting
- Audio merging

## 🚀 Features

- Removes subtitles from bottom region
- Preserves original audio
- Compatible with WhatsApp
- Fully built in Python

---

## 🧠 How It Works

1. Extract video frames
2. Detect subtitle edges
3. Create mask
4. Apply inpainting
5. Merge original audio
6. Export final video (H264 + AAC)

---

## 📦 Installation

```bash
pip install -r requirements.txt
