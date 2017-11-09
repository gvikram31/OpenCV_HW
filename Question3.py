import cv2
import numpy as np
import random
import sys
import matplotlib.pyplot as plot
def Add_salt_pepper_Noise(image,pa,pb ):
    row,col,ch=image.shape
    amount1=row*col*pa
    amount2=row*col*pb
    for i in range(int(amount1)):
        image[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=0
    for i in range(int(amount2)):
        image[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=255
    return
def Add_gaussian_Noise(image,mean,sigma):
    row,col,ch= image.shape
    noiseArr = image.copy()
    noiseArr = np.random.normal(mean,sigma,image.shape)
    np.add(image,noiseArr,image,casting="unsafe")
    return;

def main(arg1):
    img=cv2.imread(arg1)
    cv2.imshow('Original',img)
    k_in = input("Please Enter 'one' or 'all' as input in command prompt.\n\
'one' will perform filtering and noising for mean =0, sigma=50, Pa=0.01, Pb=0.01 and window size=3x3. \
'all' will do the filtering and noising for all possible values of mean, sigma, Pa, Pb and window sizes\
provided in question\n")
    print(k_in)
    if k_in=='all':
        means = [0, 5, 10, 20]
        sigmas = [0, 20, 50, 100]
        pas = [0.01, 0.03, 0.05, 0.4]
        pbs = [0.01, 0.03, 0.05, 0.4]
        ksizes = [3, 5, 7]
    elif k_in=='one':
        means = [0]
        sigmas = [50]
        pas = [0.01]
        pbs = [0.01]
        ksizes = [3]
    else:
        print("Please Enter 'one' or 'all' as input from\n")
        return 0
    for i in range(len(ksizes)):
        for j in range(len(means)):
            for k in range(len(sigmas)):
                noise_img=img.copy()
                mean=means[j]
                sigma=sigmas[k]
                ksize = ksizes[i]
                Add_gaussian_Noise(noise_img,mean,sigma)
                name = 'Gaussian Noise mean:' + str(mean) + ' sigma: ' + str(sigma)
                cv2.imshow(name,noise_img)

                noise_dst=noise_img.copy()
                cv2.blur(noise_dst,(ksize,ksize))
                name = 'Box filter mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst)

                noise_dst1=noise_img.copy()
                cv2.GaussianBlur(noise_dst1,(ksize,ksize),1.5)
                name = 'GaussianBlur filter mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst1)

                noise_dst2=noise_img.copy()
                cv2.medianBlur(noise_dst2,ksize)
                name = 'Median filter' +'mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst2)
                #salt_pepper_Noise
                noise_img2=img.copy()
                pa=pas[j]
                pb=pas[k]
                Add_salt_pepper_Noise(noise_img2,pa,pb)
                name = 'Salt and Peper Noise mean: ' + str(mean) + ' sigma: ' + str(sigma)
                cv2.imshow(name, noise_img2)

                noise_dst3=noise_img2.copy()
                cv2.blur(noise_dst3,(ksize,ksize))
                name = 'Box filter2'+'mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst3)

                noise_dst4=noise_img2.copy()
                cv2.GaussianBlur(noise_dst4,(ksize,ksize),1.5)
                name = 'GaussianBlur filter2' +'mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst4)

                noise_dst5=noise_img2.copy()
                cv2.medianBlur(noise_dst5,ksize)
                name = 'Medianfilter2'+'mean: ' + str(mean) + ' sigma: ' + str(sigma) +' window size: '+str(ksize)+'x'+str(ksize)
                cv2.imshow(name,noise_dst5)
    cv2.waitKey(0)

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Enter in following format:Python Question3.py.py Imagepath/imagename.type\n")
        sys.exit(1)
    main(arg1)
