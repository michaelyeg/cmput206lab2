# cmput206lab2
*************Week of February 1, 2017*********  

Quick help on filtering: http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html  
Part I (10%) Computing a Laplace filter in opencv/python.   
The code is available for this part, you just need to understand it and run it.  
Create a 3-by-3 matrix that has positive 8 at the center and -1 elsewhere. Open a grayscale image (any image of your choice). Filter the grayscale image with the 3-by-3 matrix. Display the result. Add the input image to the filtered image. Display it. Do you observe any edge enhancements? Run your program and show it to the TA.  
Part II (40%) Median and Gaussian filters  
Here's an image corrupted with salt & pepper noise. Apply a median filter to remove the noise. Also, apply a Gaussian filter to the same noisy image. Which filter was more successful? You can use any OpenCV functions you like.  
Part III (50%) An application of filtering in OpenCV: Simple image inpainting.  
Write a program in OpenCV+Python to accomplish a simple image inpainting. This example and demo were shown in the lecture.  
You are given a damaged image and a mask image with damaged pixels.  
It is an iterative algorithm. At every iteration, your program (a) blurs the entire damaged image with a Gaussian smoothing filter; then (b) with help of the mask image, restores only the undamaged pixels. Repeat these two steps (a) and (b) a few times until all damaged pixels are infilled.  
The solution to this part has to be submitted as a single Python source file named part3.py  
