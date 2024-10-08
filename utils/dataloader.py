import cv2
import numpy as np
import os

class ImageLoader():

    def __init__(self, datapath="./data/tsukuba/"):
        self.images = []
        for filename in sorted(os.listdir(datapath)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg','.ppm')):
                img_path = os.path.join(datapath, filename)
                img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
                if img.shape[0]>1000:
                    img = cv2.resize(img, dsize=(0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
                self.images.append(img)
            if filename.lower().endswith(('.pgm')):
                GT_img_path = os.path.join(datapath, filename)
                GT_img = cv2.imread(GT_img_path, cv2.IMREAD_GRAYSCALE)
                if GT_img.shape[0]>1000:
                    GT_img = cv2.resize(GT_img, dsize=(0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
                '''    
                cv2.imshow('left_disparity_map',GT_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                '''
                self.GT_image = GT_img
                
    def __getitem__(self, idx=0):
        return self.images[idx], self.GT_image
