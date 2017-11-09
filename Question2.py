import matplotlib #used for inital testing and plot for the images
import matplotlib.pyplot as plot
import matplotlib.animation
import math
import cv2
import timeit
import numpy as np
arr = cv2.imread('Test_images/Lenna.png') # 640x480x3 array
[b,g,r] = cv2.split(arr) #split into color channels
arr_hsv = cv2.cvtColor(arr, cv2.COLOR_BGR2HSV) #convert to HSV
[h,s,v] = cv2.split(arr_hsv) #split into HSV channells
arr_ycbcr = cv2.cvtColor(arr, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb
[y,Cb,Cr] = cv2.split(arr_ycbcr) #split YCrCb channels
outfilenameRGB=['Question2_results/Red_lena.png','Question2_results/Green_lena.png','Question2_results/Blue_lena.png']
outfilenameYCRCB=['Question2_results/Y_lena.png','Question2_results/CR_lena.png','Question2_results/CB_lena.png']
outfilenameHSV=['Question2_results/hue_lena.png','Question2_results/saturation_lena.png','Question2_results/value_lena.png']
# arr_ycbcr=rgb2ycbcr(arr)
# arr_hsv=rgb2hsv(arr)
print("pixel at 20,25","RGB:-",arr[20,25,:],"YCBCR:=",arr_ycbcr[20,25,:],"HSV:-",arr_hsv[20,25,:])
for i in range(len(arr[1,1,:])):
    cv2.imwrite(outfilenameRGB[2-i], arr[:,:,i])
    cv2.imwrite(outfilenameYCRCB[i], arr_ycbcr[:,:,i])
    cv2.imwrite(outfilenameHSV[i], arr_hsv[:,:,i])

#ycbcr part
def rgb2ycbcr(im):
    cbcr = np.empty_like(im)
    r = im[:,:,2]
    g = im[:,:,1]
    b = im[:,:,0]
    # Y
    cbcr[:,:,0] = .299 * r + .587 * g + .114 * b
    # Cb
    cbcr[:,:,1] = 128 - .169 * r - .331 * g + .5 * b
    # Cr
    cbcr[:,:,2] = 128 + .5 * r - .419 * g - .081 * b
    return np.uint8(cbcr)
start = timeit.default_timer()
arr1=rgb2ycbcr(arr)
stop = timeit.default_timer()
#here I am comparing the execution time for inbuilt rgb2ycbcr and my rgb2ycbcr
#and it turns out my algorithm is slower.
print ("my algo",(stop-start))
start = timeit.default_timer()
arr_ytest = cv2.cvtColor(arr, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb
[y,Cb,Cr] = cv2.split(arr_ytest) #split YCrCb channels
stop = timeit.default_timer()

print (stop-start)
# def rgb2hsv(arr):
#     r=arr[:,:,2]
#     g=arr[:,:,1]
#     b=arr[:,:,0]
#     mx=np.empty_like(r)
#     mn=np.empty_like(r)
#     row=(len(arr[:,1,0]))
#     col=(len(arr[1,:,0]))
#     for i in range(row):
#         for j in range(col):
#             mx[i,j]=max(r[i,j],g[i,j],b[i,j])
#             mn[i,j]=min(r[i,j],g[i,j],b[i,j])
#     df = mx-mn
#     h=np.zeros((row,col),dtype=float)
#     s=np.zeros((row,col),dtype=float)
#     v=np.zeros((row,col),dtype=float)
#     hsv=np.empty_like(arr)
#     count=0
#     count1=0
#     for i in range(row):
#         for j in range(col):
#             if mx[i,j] == mn[i,j]:
#                 count=count+1
#                 h[i,j] = 0
#             elif mx[i,j] == r[i,j]:
#                 count=count+1
#                 h[i,j] = (60 *(((g[i,j]-b[i,j])/df[i,j])%6))
#             elif mx[i,j] == g[i,j]:
#                 count=count+1
#                 h[i,j] = (60 * (((b[i,j]-r[i,j])/df[i,j]) + 2))
#             elif mx[i,j] == b[i,j]:
#                 count=count+1
#                 h[i,j] = (60 * (((r[i,j]-g[i,j])/df[i,j]) + 4))
#             if mx[i,j] == 0:
#                 s[i,j] = 0
#             else:
#                 count1=count1+1
#                 s[i,j] = float((df[i,j]/mx[i,j])*255)
#     v = mx[:,:]
#     hsv[:,:,0]=h
#     hsv[:,:,1]=s
#     hsv[:,:,2]=v
#     return hsv
