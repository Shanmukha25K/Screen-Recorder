import pyautogui
import cv2 as cv
import numpy as np
import time

file_name = input("Enter the filename: ") + ".mp4"
tym = float(input("Enter the time to be recorded in minutes: "))

record_time = tym * 60  # Convert minutes to seconds
start_time = time.time()

resolution = pyautogui.size()

codec = cv.VideoWriter_fourcc(*"XVID") 
fps = 10.0
frame_time = 1 / fps  # Time per frame (ensures proper timing)

output = cv.VideoWriter(file_name, codec, fps, resolution)
#creates a file with specified features

# Optional
cv.namedWindow("Live", cv.WINDOW_NORMAL)
cv.resizeWindow("Live", 480, 270)

print(f"Recording started for {tym} minutes... Press 'q' to stop early.")

while time.time() - start_time < record_time: 
    loop_start_time = time.time() 

    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    output.write(frame)  

    cv.imshow("Live", frame)  #image show

    if cv.waitKey(1) == ord("q"):    #1millisecond
        print("Recording stopped by user.")
        break

    # Ensure correct frame timing
    elapsed_time = time.time() - loop_start_time
    sleep_time = max(0, frame_time - elapsed_time)  
    time.sleep(sleep_time)

print("Recording completed.")
output.release()
cv.destroyAllWindows()
print(f"Video saved as {file_name}")
