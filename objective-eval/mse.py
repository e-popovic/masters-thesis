from skimage.metrics import mean_squared_error as mse
import numpy as np
import cv2
import os

f = open("mse_calculated.txt", "a")
directory = 'images/edited'
cnt = 0

original_path = ''
image1 = np.zeros((3000,4496,3), np.uint8)

for filename in os.scandir(directory):
    if filename.is_file():
        
        # upload original image
        if (cnt == 0):
            original_path = 'images/originals\\' + filename.path.split('\\')[1][0] + '.jpg'
            image1 = cv2.imread(original_path)

            #RGB
            b1 = image1.copy()
            b1[:, :, 1] = b1[:, :, 2] = 0

            g1 = image1.copy()
            g1[:, :, 0] = g1[:, :, 2] = 0

            r1 = image1.copy()
            r1[:, :, 0] = r1[:, :, 1] = 0

            r1_gray = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
            g1_gray = cv2.cvtColor(g1, cv2.COLOR_BGR2GRAY)
            b1_gray = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY)

            r1_array = np.array(r1_gray)
            g1_array = np.array(g1_gray)
            b1_array = np.array(b1_gray)

            #YUV
            image1_yuv = cv2.cvtColor(image1, cv2.COLOR_BGR2YUV)

            y1 = image1_yuv.copy()
            y1[:, :, 1] = y1[:, :, 2] = 0

            u1 = image1_yuv.copy()
            u1[:, :, 0] = u1[:, :, 2] = 0

            v1 = image1_yuv.copy()
            v1[:, :, 0] = v1[:, :, 1] = 0

            y1_array = image1_yuv[:, :, 0]
            u1_array = image1_yuv[:, :, 1]
            v1_array = image1_yuv[:, :, 2]

            #LAB
            image1_lab = cv2.cvtColor(image1, cv2.COLOR_BGR2LAB)

            l1 = image1_lab.copy()
            l1[:, :, 1] = l1[:, :, 2] = 0

            a1 = image1_lab.copy()
            a1[:, :, 0] = a1[:, :, 2] = 0

            b1_lab = image1_lab.copy()
            b1_lab[:, :, 0] = b1_lab[:, :, 1] = 0

            l1_array = image1_lab[:, :, 0]
            a1_array = image1_lab[:, :, 1]
            b1_lab_array = image1_lab[:, :, 2]

        
        f.write(filename.name[:-4])
        f.write("|")

        print(filename.name[:-4])

        # Rupload edited image

        image2 = cv2.imread(filename.path)

        # RGB channels (converted to grayscale)

        b2 = image2.copy()
        b2[:, :, 1] = b2[:, :, 2] = 0

        g2 = image2.copy()
        g2[:, :, 0] = g2[:, :, 2] = 0

        r2 = image2.copy()
        r2[:, :, 0] = r2[:, :, 1] = 0
        
        r2_gray = cv2.cvtColor(r2, cv2.COLOR_BGR2GRAY)
        g2_gray = cv2.cvtColor(g2, cv2.COLOR_BGR2GRAY)
        b2_gray = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)

        r2_array = np.array(r2_gray)
        g2_array = np.array(g2_gray)
        b2_array = np.array(b2_gray)

        # YUV channels
        
        image2_yuv = cv2.cvtColor(image2, cv2.COLOR_BGR2YUV)

        y2 = image2_yuv.copy()
        y2[:, :, 1] = y2[:, :, 2] = 0

        u2 = image2_yuv.copy()
        u2[:, :, 0] = u2[:, :, 2] = 0

        v2 = image2_yuv.copy()
        v2[:, :, 0] = v2[:, :, 1] = 0
       
        y2_array = image2_yuv[:, :, 0]
        u2_array = image2_yuv[:, :, 1]
        v2_array = image2_yuv[:, :, 2]


        # LAB channels
        
        image2_lab = cv2.cvtColor(image2, cv2.COLOR_BGR2LAB)

        l2 = image2_lab.copy()
        l2[:, :, 1] = l2[:, :, 2] = 0

        a2 = image2_lab.copy()
        a2[:, :, 0] = a2[:, :, 2] = 0

        b2_lab = image2_lab.copy()
        b2_lab[:, :, 0] = b2_lab[:, :, 1] = 0

        
        l2_array = image2_lab[:, :, 0]
        a2_array = image2_lab[:, :, 1]
        b2_lab_array = image2_lab[:, :, 2]


        # Calculate the MSE

        mser = mse(r1_array, r2_array)
        mseg = mse(g1_array, g2_array)
        mseb = mse(b1_array, b2_array)

        data = str(mser) + ':' + str(mseg) + ':' + str(mseb) + '|'

        msey = mse(y1_array, y2_array)
        mseu = mse(u1_array, u2_array)
        msev = mse(v1_array, v2_array)

        data += str(msey) + ':' + str(mseu) + ':' + str(msev) + '|'

        msel = mse(l1_array, l2_array)
        msea = mse(a1_array, a2_array)
        mseb_lab = mse(b1_lab_array, b2_lab_array)

        data += str(msel) + ':' + str(msea) + ':' + str(mseb_lab) + '\n'
        f.write(data)

        print(data)

        cnt = (cnt + 1) % 4

f.close()
