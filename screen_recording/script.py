import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"  # AVI is associated with DivX codex and MP4 uses MPEG-4 AVC/H. 264 codec.
fps = 60.0  # frame rate

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert BGR to RGB
    out.write(frame)
    # cv2.imshow('Live', frame)  # Optional: Display the recording screen
    if cv2.waitKey(1) == ord('q'): # Stop recording when we press 'q'
        break
out.release()
cv2.destroyAllWindows()