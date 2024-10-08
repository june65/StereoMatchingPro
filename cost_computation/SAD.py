import numpy as np
import cv2
from utils import RGB_to_gray
from tqdm import tqdm

def SAD(left_image, right_image, min_depth, max_depth, kernel_size, disparity_print):

    left_image = RGB_to_gray(left_image)
    right_image = RGB_to_gray(right_image)

    left_CV, right_CV =  cost_volume(left_image, right_image, min_depth, max_depth, kernel_size)
    return disparity_map(left_CV, right_CV, min_depth, max_depth, kernel_size, disparity_print)

#VERSION1
def cost_volume(left_image, right_image, min_depth, max_depth, kernel_size):

    height, width = left_image.shape
    left_costvolume = np.full((height, width, max_depth), np.inf).astype(np.float32)
    right_costvolume = np.full((height, width, max_depth), np.inf).astype(np.float32)

    for d in range(min_depth, max_depth):
        for w in range(width):
            if w+d < width:
                left_costvolume[:,w,d] = np.abs(left_image[:,w] - right_image[:,w+d])
            if w-d >=0:
                right_costvolume[:,w,d] = np.abs(left_image[:,w-d] - right_image[:,w])

    return left_costvolume, right_costvolume


def disparity_map(left_costvolume, right_costvolume, min_depth, max_depth, kernel_size, disparity_print):
    
    pad_size = kernel_size // 2
    pad_width = ((pad_size, pad_size), (pad_size, pad_size), (0,0))
    padded_left_disparity = np.pad(left_costvolume, pad_width, mode='constant')
    padded_right_disparity = np.pad(right_costvolume, pad_width, mode='constant')
    
    height, width, _ = left_costvolume.shape

    left_disparity_conv = np.zeros((height, width, max_depth))
    right_disparity_conv = np.zeros((height, width, max_depth))

    kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2

    for h in tqdm(range(height)):
        for w in range(width):
            for n in range(max_depth):
                left_disparity_conv[h, w, n] = np.sum(padded_left_disparity[h:h+kernel_size, w:w+kernel_size, n] * kernel)
                right_disparity_conv[h, w, n] = np.sum(padded_right_disparity[h:h+kernel_size, w:w+kernel_size, n] * kernel)

    left_disparity = np.argmin(left_disparity_conv, axis=2)
    right_disparity = np.argmin(right_disparity_conv, axis=2)

    if disparity_print:
        print_img = left_disparity.astype(np.uint8) * int(255 / max_depth)
        cv2.imshow('left_disparity_map',print_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print_img = right_disparity.astype(np.uint8) * int(255 / max_depth)
        cv2.imshow('right_disparity_map',print_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return left_disparity, right_disparity, left_disparity_conv

'''
#VERSION2
def cost_volume(left_image, right_image, min_depth, max_depth, kernel_size):

    height, width = left_image.shape
    left_costvolume = np.full((height, width, max_depth), np.inf)
    right_costvolume = np.full((height, width, max_depth) ,np.inf)

    kernel_vectors = []
    for i in range(-kernel_size//2+1, kernel_size//2+1):
        for j in range(-kernel_size//2+1, kernel_size//2+1):
            kernel_vectors.append((i,j))

    for d in range(min_depth, max_depth):
        for w in range(width):
            if w+d < width:
                for h in range(height):
                    kernel_num = 0
                    flag_sum = 0
                    for (i,j) in kernel_vectors: 
                        if h+i < height and w+d+j < width and h+i >= 0 and  w+j >= 0:
                            flag_sum += np.abs(left_image[h+i,w+j] - right_image[h+i,w+d+j])
                            kernel_num += 1
                    left_costvolume[h,w,d] = flag_sum / kernel_num

            if w-d >= 0:
                for h in range(height):
                    kernel_num = 0
                    flag_sum = 0
                    for (i,j) in kernel_vectors: 
                        if h+i < height and w+j < width and h+i >= 0 and  w-d+j >= 0:
                            flag_sum += np.abs(left_image[h+i,w-d+j] - right_image[h+i,w+j])
                            kernel_num += 1
                    right_costvolume[h,w,d] = flag_sum / kernel_num

    return left_costvolume, right_costvolume


def disparity_map(left_costvolume, right_costvolume, min_depth, max_depth, kernel_size, disparity_print):
    
    left_disparity = np.argmin(left_costvolume, axis=2)
    right_disparity = np.argmin(right_costvolume, axis=2)

    if disparity_print:
        print_img = left_disparity.astype(np.uint8) * int(255 / max_depth)
        cv2.imshow('left_disparity_map',print_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print_img = right_disparity.astype(np.uint8) * int(255 / max_depth)
        cv2.imshow('right_disparity_map',print_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return left_disparity, right_disparity
'''