import cv2
import numpy as np
from moviepy import VideoFileClip

input_video = "input_example/video_2026-02-27_10-06-15.mp4"
temp_video = "temp_no_audio.mp4"
final_video = "final_output2.mp4"

cap = cv2.VideoCapture(input_video)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    y_start = int(height * 0.70)
    subtitle_region = frame[y_start:height, :]

    gray = cv2.cvtColor(subtitle_region, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(edges, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    inpainted_region = cv2.inpaint(subtitle_region, mask, 3, cv2.INPAINT_TELEA)

    frame[y_start:height, :] = inpainted_region
    out.write(frame)

cap.release()
out.release()

# 🎬 إعادة الصوت
original_clip = VideoFileClip(input_video)
processed_clip = VideoFileClip(temp_video)

final_clip = processed_clip.with_audio(original_clip.audio)
final_clip.write_videofile(final_video, codec="libx264", audio_codec="aac")

print("Done! Saved as final_output.mp4")