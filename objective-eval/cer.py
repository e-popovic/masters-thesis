import cv2
import time
import os
import numpy as np
import math

start_time = time.time()

image_original = []
names_original = []
image_method = []
names_method = []

file_cer = open("cer_calculated.txt", "a")

for filename in os.scandir('images/originals'): 
    if filename.is_file():
        im1=cv2.imread(filename.path)
        image_original.append(im1)
        names_original.append(filename.path)

for filename in os.scandir('images/edited'): 
    if filename.is_file():
        im2=cv2.imread(filename.path)
        image_method.append(im2)
        names_method.append(filename.path)

count=0
while(count<48):
    count_original = math.floor(count/4)

    if (count/4 == math.floor(count/4)):
        yuv_img1 = cv2.cvtColor(image_original[count_original], cv2.COLOR_BGR2YUV)
        y1, u1, v1 = cv2.split(yuv_img1) 

    yuv_img2 = cv2.cvtColor(image_method[count], cv2.COLOR_BGR2YUV)
    y2, u2, v2 = cv2.split(yuv_img2)

    img_name = names_method[count].split('\\')[1][:-4]
    print(img_name)

    file_cer.write(img_name)
    file_cer.write('/')

    u1_niz = np.array(u1).astype(np.float64)  
    v1_niz = np.array(v1).astype(np.float64)  
    u2_niz = np.array(u2).astype(np.float64)  
    v2_niz = np.array(v2).astype(np.float64) 
    niz_u1 = u1_niz.ravel()
    niz_v1 = v1_niz.ravel()
    niz_u2 = u2_niz.ravel()
    niz_v2 = v2_niz.ravel()

    counter=0
    vector_sum = 0
    suma1=0
    suma2=0
    vector_array = []
    while (counter < 13488000):
        u_orig = niz_u1[counter]
        v_orig = niz_v1[counter]
        u_met = niz_u2[counter]
        v_met = niz_v2[counter]
        vector = math.sqrt((u_orig-u_met)**2 + (v_orig-v_met)**2)
        pom1 = u_met**2 + v_met**2
        suma1= suma1 + pom1
        pom2 = (u_orig-u_met)**2 + (v_orig-v_met)**2
        suma2 = suma2 + pom2
        vector_sum = vector_sum + vector
        vector_array.append(vector)
        counter = counter+1

    cer = 10 * math.log10((suma1/13488000)/(suma2/13488000))

    data = (str(vector_sum) + ':' + str(cer) + '\n' )
    file_cer.write(data)

    count = count+1
    cv2.waitKey(0)

end_time = time.time()
print("--- " + str(math.floor((end_time - start_time)/60)) + ' minutes ' + 
    str(((end_time - start_time)%60)) + ' seconds ---')
