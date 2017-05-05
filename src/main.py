# -*- coding: utf-8 -*-
"""
Created on Thu May 04 19:12:27 2017

@author: Utkarsh
"""

import cv2
import time
import matplotlib.pyplot as plt

from GuidedFilt import GuidedFilt
img = cv2.imread("../images/noisy_img3.png",0)

out_BilateralFilt = [];
out_GuidedFilt = [];
#for i in range(1,17,1):

start_time = time.time()
i = 15
BF_out = cv2.bilateralFilter(img,i,35,35)
elapsed_time = time.time() - start_time
out_BilateralFilt.append(elapsed_time)

save_name = '../outputs/BF_out.png'
cv2.imshow("BilateralFilt_out",BF_out)
#cv2.imwrite(save_name,BF_out)

start_time = time.time()
GF_out = GuidedFilt(img,i)
elapsed_time = time.time() - start_time
out_GuidedFilt.append(elapsed_time)

save_name = '../outputs/GF_out.png'    
cv2.imshow("GuidedFilt_out",GF_out)
#cv2.imwrite(save_name,GF_out)
cv2.waitKey(0);

"""
plt.plot(out_BilateralFilt, 'r', out_GuidedFilt, 'b')
plt.ylabel('time')
plt.xlabel('filter size')
plt.show()
"""