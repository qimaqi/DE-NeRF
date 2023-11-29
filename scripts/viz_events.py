import argparse
import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2

def render(img, x, y, t, p):
    img[y, x, p+1] = 255
    return img

if __name__ == "__main__":
    parser = argparse.ArgumentParser("""Generate events from a high frequency video stream""")
    parser.add_argument("--input_dir", default="")
    parser.add_argument("--output_dir", default='event_vis')
    parser.add_argument("--render_skip", default=100)
    args = parser.parse_args()

    event_files = sorted(glob.glob(os.path.join(args.input_dir, "events", "*.npz")))
    gray_files = sorted(glob.glob(os.path.join(args.input_dir, "grayscale", "*.png")))
    
    assert len(event_files) == len(gray_files) - 1, 'mismatch the size'
    count = 0
    for gray_i, event_i in zip(gray_files[:-1], event_files):
        if count % args.render_skip==0:
            event_i_load = np.load(event_i)# ['x']
            gray_i_load = cv2.imread(gray_i, cv2.IMREAD_COLOR) # BGR
            gray_i_vis = gray_i.replace('grayscale','events_vis')
            img = render(gray_i_load, **event_i_load)
            cv2.imwrite(gray_i_vis, img)
        count+=1


