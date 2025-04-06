import pyrealsense2 as rs
import numpy as np
import cv2
import time

x = 424
y = 240

pipeline = rs.pipeline()
config = rs.config()
filter = rs.decimation_filter()
config.enable_stream(rs.stream.depth, x,y, rs.format.z16, 30)
config.enable_stream(rs.stream.color, x,y, rs.format.bgr8, 30)  # bgr is compatible with OpenCV 
pipelineProfile = pipeline.start(config)

i = 7 
n = 0
while True:
            frames = pipeline.wait_for_frames()

            color_frame = frames.get_color_frame()

            if  not color_frame:
                continue

            color_img = np.asanyarray(color_frame.get_data())
            
            cv2.imshow("TCP", color_img)
               
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key == 27:
                n = n + 1
                cv2.imwrite(f"Bild{i},{n}.png", color_img)
            if n == 5:
                break
            
            
pipeline.stop()
cv2.destroyAllWindows()
                    
                    