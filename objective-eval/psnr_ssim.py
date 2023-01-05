import cv2
import sewar
import time
import os
import math

start_time = time.time()

image_original = []
names_original = []
image_method = []
names_method = []

file_psnr = open("psnr_calculated.txt", "a")
file_ssim = open("ssim_calculated.txt", "a")
# file_msssim = open("msssim_calculated.txt", "a")

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
        b1_rgb, g1, r1 = cv2.split(image_original[count_original])
        yuv_img1 = cv2.cvtColor(image_original[count_original], cv2.COLOR_BGR2YUV)
        y1, u1, v1 = cv2.split(yuv_img1) 
        lab_img1 = cv2.cvtColor(image_original[count_original], cv2.COLOR_BGR2LAB)
        l1, a1, b1_lab = cv2.split(lab_img1) 

    b2_rgb, g2, r2 = cv2.split(image_method[count])
    yuv_img2 = cv2.cvtColor(image_method[count], cv2.COLOR_BGR2YUV)
    y2, u2, v2 = cv2.split(yuv_img2)
    lab_img2 = cv2.cvtColor(image_method[count], cv2.COLOR_BGR2LAB)
    l2, a2, b2_lab = cv2.split(lab_img2) 

    img_name = names_method[count].split('\\')[1][:-4]
    print(img_name)

    file_psnr.write(img_name)
    file_psnr.write('/')
    file_ssim.write(img_name)
    file_ssim.write('/')
    # file_msssim.write(img_name)
    # file_msssim.write('/')

    # PSNR
    psnr_r = sewar.full_ref.psnr(r1, r2, MAX=None)
    psnr_g = sewar.full_ref.psnr(g1, g2, MAX=None)
    psnr_b_rgb = sewar.full_ref.psnr(b1_rgb, b2_rgb, MAX=None)
    psnr_rgb = (psnr_r + psnr_g + psnr_b_rgb)/3

    psnr_u = sewar.full_ref.psnr(u1, u2, MAX=None)
    psnr_v = sewar.full_ref.psnr(v1, v2, MAX=None)
    psnr_uv = (psnr_u + psnr_v)/2

    psnr_a = sewar.full_ref.psnr(a1, a2, MAX=None)
    psnr_b_lab = sewar.full_ref.psnr(b1_lab, b2_lab, MAX=None)
    psnr_ab = (psnr_a + psnr_b_lab)/2

    data = (str(psnr_r) + ':' + str(psnr_g) + ':' + str(psnr_b_rgb) + ':' + str(psnr_rgb) + '|' + 
        str(psnr_u) + ':' + str(psnr_v) + ':' + str(psnr_uv) + '|' + 
        str(psnr_a) + ':' + str(psnr_b_lab) + ':' + str(psnr_ab) + '\n' )
    file_psnr.write(data)

    # SSIM
    ssim_r, cs_r = sewar.full_ref.ssim(r1, r2, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_g, cs_g = sewar.full_ref.ssim(g1, g2, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_b_rgb, cs_b_rgb = sewar.full_ref.ssim(b1_rgb, b2_rgb, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_rgb = (ssim_r + ssim_g + ssim_b_rgb)/3

    ssim_u, cs_u = sewar.full_ref.ssim(u1, u2, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_v, cs_v = sewar.full_ref.ssim(v1, v2, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_uv = (ssim_u + ssim_v)/2

    ssim_a, cs_a = sewar.full_ref.ssim(a1, a2, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_b_lab, cs_b_lab = sewar.full_ref.ssim(b1_lab, b2_lab, ws=11, MAX=None, fltr_specs=None, mode='valid')
    ssim_ab = (ssim_a + ssim_b_lab)/2

    data = (str(ssim_r) + ':' + str(ssim_g) + ':' + str(ssim_b_rgb) + ':' + str(ssim_rgb) + '|' + 
        str(ssim_u) + ':' + str(ssim_v) + ':' + str(ssim_uv) + '|' + 
        str(ssim_a) + ':' + str(ssim_b_lab) + ':' + str(ssim_ab) + '\n' )
    file_ssim.write(data)

    # MSSSIM
    # msssim_r = sewar.full_ref.msssim(r1, r2, MAX=None)
    # msssim_g = sewar.full_ref.msssim(g1, g2, MAX=None)
    # msssim_b_rgb = sewar.full_ref.msssim(b1_rgb, b2_rgb, MAX=None)
    # msssim_rgb = (msssim_r + msssim_g + msssim_b_rgb)/3

    # msssim_u = sewar.full_ref.msssim(u1, u2, MAX=None)
    # msssim_v = sewar.full_ref.msssim(v1, v2, MAX=None)
    # msssim_uv = (msssim_u + msssim_v)/2

    # msssim_a = sewar.full_ref.msssim(a1, a2, MAX=None)
    # msssim_b_lab = sewar.full_ref.msssim(b1_lab, b2_lab, MAX=None)
    # msssim_ab = (msssim_a + msssim_b_lab)/2
	
    # data = (str(msssim_r) + ':' + str(msssim_g) + ':' + str(msssim_b_rgb) + ':' + str(msssim_rgb) + '|' + 
    #     str(msssim_u) + ':' + str(msssim_v) + ':' + str(msssim_uv) + '|' + 
    #     str(msssim_a) + ':' + str(msssim_b_lab) + ':' + str(msssim_ab) + '\n' )
    # file_msssim.write(data)

    count = count+1
    cv2.waitKey(0)

end_time = time.time()
print('--- ' + str(math.floor((end_time - start_time)/60)) + ' minutes ' + 
    str(((end_time - start_time)%60)) + ' seconds ---')