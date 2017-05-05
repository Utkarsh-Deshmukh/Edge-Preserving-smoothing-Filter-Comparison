# -*- coding: utf-8 -*-
"""
Created on Thu May 04 20:09:43 2017

@author: Utkarsh
"""

import cv2
import numpy as np
def GuidedFilt(img, r):
    eps = 0.04;
    
    I = np.double(img);
    I = I/255;
    I2 = cv2.pow(I,2);
    mean_I = cv2.boxFilter(I,-1,((2*r)+1,(2*r)+1))
    mean_I2 = cv2.boxFilter(I2,-1,((2*r)+1,(2*r)+1))
    
    cov_I = mean_I2 - cv2.pow(mean_I,2);
    
    var_I = cov_I;
    
    a = cv2.divide(cov_I,var_I+eps)
    b = mean_I - (a*mean_I)
    
    mean_a = cv2.boxFilter(a,-1,((2*r)+1,(2*r)+1))
    mean_b = cv2.boxFilter(b,-1,((2*r)+1,(2*r)+1))
    
    q = (mean_a * I) + mean_b;
    
    return(np.uint8(q*255))