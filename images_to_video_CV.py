import numpy as np
import cv2
import glob
import re
import datetime


# img_array = []

# for filename in glob.glob('./captures/observe/*.png'):
#     img = cv2.imread(filename=filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
    
 
# img_array = np.array(img_array)

# print("File read successfully.")   
# out = cv2.VideoWriter('Aug_19_CV.avi', cv2.VideoWriter_fourcc(*'DIVX', 60, size))

# for image in img_array:
#     out.write(image)

# print("Video file written successfully.")   

# out.release()



# ----------------------------------------------------

# Get a list of filenames and sort them numerically
filenames = glob.glob('./captures/*.png')
filenames.sort(key=lambda x: int(re.search(r'(\d+)\.png', x).group(1)))

fps = 60


now = datetime.datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

out = cv2.VideoWriter('saved_video/%s.avi'%dt_string, cv2.VideoWriter_fourcc(*'DIVX'), fps, (1920, 1080))


for filename in filenames:
    img = cv2.imread(filename=filename)
    out.write(img)
    print(filename)
    
    
out.release()