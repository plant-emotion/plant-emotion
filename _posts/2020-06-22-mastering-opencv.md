---
layout: post
title: "Optimizing OpenCV for the Object Tracker"
author: "Sebastian"
categories: project
---
### Summary of Relevant Passages of the Book: Mastering OpenCV 4 with Python

Chapter Overview:
- Chapter 1 is an introduction to Python and OpenCV
- Chapter 2,3 relate to Image basics and Handling Files and Images with OpenCV
- Chapter 4 explains how to draw basic shapes in OpenCV
- Chapter 6 is about building histograms
- Chapter 9 regards Augmented Reality in OpenCV
- Chapter 10 is on Machine Learning and Deep Learning in OpenCV
- Chapter 11 deals with Face Detection, Tracking, and Recognition
- Chapter 12 introduces Deep Learning
- Chapter 13 is on Mobile and Web Computer Vision (like recognizing cats)

<<< Relevant Chapter Overview >>>
- Chapter 5 is about image processing techniques (image filtering, kernels, morph transformations, )
- Chapter 7 is on thresholding images (adaptive, otsu)
- Chapter 8 is on Contour Detection, Filtering and Drawing

# Chapter 5 - Image Processing
## Image Filtering
They introduce certain filters of which _Gaussian Blur_ and, _Bilateral Filtering (big values)_ look the best, _boxFilter_ seems relevant as it is quite undetailed but may suffice for plants.

Coding samples for these three:

- Gaussian blur: smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0) # Kernel size is (9, 9)
- Bilateral filtering: reduces noise while it keeps the edges sharp: smooth_image_bf = cv2.bilateralFilter(image, 5, 0, 10) # all previous filters tend to smooth all the images including their edges

## Morphological transformations

are operations that are normally performed on binary images and based on the image shape.

- Dilation: main effect on a binary image is to gradually expand the boundary regions of the foreground Object: cv2.dilate(image, kernel, iterations = 1)
- Erosion: gradually erode away the boundary regions of the foreground Object
- Opening operation: performs an erosion followed by a dilation using the same structuring element or kernel for both operations
- The combination of opening and closing operation (or the other way round) seems to work the best. The corresponding code is: opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel); closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Chapter 7 - Thresholding
## Adaptiive thresholding

Results of global thresholding may not be good due to different illumination conditions in the different areas of an image. Therefore, try adaptiveThresholding.
```python
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
```
This functions applies an adaptive thresh to the src array. The maxValue sets the value for the pixels in the dst image for which the condition is satisfied. The adaptiveMethod sets the adaptive thresholding algo to use: Thresh_mean_C or Thresh_gaussian_C.
 CONTINUE HERE


#### Links

##### Project

- Development Files: [Private Git with Latest Development](https://github.com/plantions/video-edge-extractor/)
- Public Files: [Public Git with Video footage](https://github.com/plantions/published)

##### Helpful Resources/Explanations
- [Dilation and Erosion](https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html)
- [Mask Thresholding](https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html)
- [Contour Feature](https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html)
- [Plotting with Altair](https://altair-viz.github.io/getting_started/overview.html)
- [Plotting Peak Width with SciKit Learn](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths)
- [Smoothing Time Series](https://towardsdatascience.com/time-series-in-python-exponential-smoothing-and-arima-processes-2c67f2a52788)
- [Peak Detection](https://pythonawesome.com/overview-of-the-peaks-dectection-algorithms-available-in-python/)
