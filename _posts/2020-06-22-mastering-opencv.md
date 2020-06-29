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
- Chapter 11 should be intersting because of Tracking and Recognition.

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

# Chapter 6 - Constructing and Building Histograms

- Constrast limted adaptive histogram equalization (CLAHE): applied to improve the constrast of images. Works by creating several histograms of the original image, and uses all of these histograms to redistribute the lightness of the image.

# Chapter 7 - Thresholding

Image segmentation is key process in computer vision. Used to partition an image into different regions that correspond to real-world objects. Image thresholding is a simple image segmentation method, where the pixels are partitioned depending on their intensity value. 

## Adaptive thresholding

- Results of global thresholding may not be good due to different illumination conditions in the different areas of an image. Therefore, try adaptiveThresholding.
```python
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
```
- This functions applies an adaptive thresh to the src array. - The maxValue sets the value for the pixels in the dst image for which the condition is satisfied. The adaptiveMethod sets the adaptive thresholding algo to use: Thresh_mean_C or Thresh_gaussian_C.
- deal with upcoming noise by applying a bilateral filter (to maintain sharp edges) with _cv2.bilateralFilter()_

## Otsu Thresholding

- in AdaptiveThresholding two values need to be established correctly, i.e., blockSize and c 
- Use Otsu for bimodal images: can be characterized by its histogram containing two peaks; Otsu will then calc the optimal thresh value
- noise can affect the thesh algo - e.g. try a Gaussian filter

## Triangle binarization algo

- shape-based method because it analyzes the structure of the histogram (finding peaks, values, etc)
- steps: (1) line is calc'ed between max of histogram and lowest value b on gray level axis; (2) distance from line for all values of b is calc'ed; (3) distance betwen the histogram and the line is maximal is chosen as thresh value
- __May be worth trying but also use Gaussian filter before.__

## Thresholding Color Images

- thresholding is applied to all three channels (RBG) of an image. Maybe for green channel for the plants? 
- see screenshot 'green tresh'

## Thresholding w/ scikit-image

- trying out more thresh techniques with scikit-image: Otsu and Triangle are gloabl threshholding techniques (i.e. background is uniform); while __Niblack and Sauvola__ are __local__ thresholding techniques (better for plants of peter bc background isnot uniform ; see 'sauvola')

# Chapter 8 - Contour Detection, Filtering, and Drawing

## Contour Detection
- Contour: sequence of points defining the boundary of an object in an image. Can be seen as a curve joining all the points along the boundary of a certain shape.
- Technical def: is an array composed of many points of np.int32 type 
- OpenCV provides cv2.findContours() which can be used to detect contours in binary images (after a thresholding operation), 
- differnt contour modes: 
    - retr_external: only external contours
    - retr_list: all contours
    - retr_tree: all contours with hierarchical relationship
- Compressing contours: detected contours are compressed to reduce the number of points: cv2.CHAIN_APPROX_SIMPLE will make a box only 4 points; sophisticated versions are: TC89_L1, and cv2.CHAIN_APPROX_TC89_KCOS

## Image Moments
- can be seen as a specific quantitative measure of a function shape. They are features computed from contours allowing a geometrical reconstruction of the object. 
- useful to describe some properties of the detected contours (center of mass of the object, area of the object)
- Moment measures:
    - Roundness: measure of how closely a contour approaches the contour of a perfect circle
    - Eccentricity (elongation): measure of how elongated a contour can be. Therefore, calculate the ellipse that fits the contour and afterwards derive two axes a and b 
    - The aspect ratio can be easily calculated based on the dimensions of the minmial bounding rectangle, calc'ed with cv2.boundingRect()

## Hu Moment Invariants
- are invariant with respect to translation, scale, and rotation and all the moments are invariant to reflection
- first calc the moments by using cv2.moments(), afterwards use cv2.cvtColor to make image binary, then calc the hu moments

## Zernike Moments
- mahotas package provides the zernike_moments() function

## More Functionality Related to Contours
- image and extreme points: extreme_points calculates the four extreme points defining a given contour 
- cv2.minAreaRect(): returns minimal bounding rectangle enclosing all points of the contour - __rotated__ if necessary; to return the four vertices use cv2.boxPoints()
- cv2.ellipse(): returns ellipse with the minimum least square errors fitting all the points of the contour
- cv2.boundingRect(): returns minimal bounding rectangle enclosing all points of the contour
- cv2.minEnclosingCircle(): returns minimal circle, center and radius
- cv2.approxPolyDP(): returns a contour approx of the given contour based on the given precision (using Douglas Peucker); epsilon establishes the precision, determining, the max distance between the original curve and its approximation 

## Filtering Contours

- sort_contours_size(): sorts contours based on the size
-> use this to get the biggest contours for your allocation

## Recognizing Contours

- xc2.approxPolyDP(): can be used to approx one contour with another with fewer points through Douglas-Peucker algo
- key param is epsilon: sets the approx accuracy; to decimate a number of points, given a certain contour, we first compute the perimeter 

## Matching Contours

- cv2.matchShapes(): compare two contours using three comparison methods: I1, I2, and I3 
- we draw a perfect cirle, then a reference file is used
- find contours through: convert to grayscale (cv2.cvtColor), binarize (cv2.threshhold), find contours (cv2.findContours). 

# Chapter 9 - Augmented Reality

## Intro to AR

- location-based: relies on detecting the user's location and orientation by reading data from several sensors
- recog-based: uses image processing techniques to derive where the user is looking 
    - marker-based pose estimation: using planar markers
    - markless-based pose estimation: when secen cannot be prepared using markers
    
## Feature Detection

- Harris Corner Detection, Shi-Tomasi, SIFT, SURF< FAST, BRIEF< ORB

#### To Dos:

- Look up Zernike Moments and see how it helps you
- Look for Harris Corner detection; check again on DataCamp platform for the good algorithms. 
- Show real image for multiple thresholds (compare multiple thresholds1 and multiple thresholds2).
- see histogram for your flying paprika
- Get the git code for the whole book and try it out
- Do the FLASK web project on Face Recognition & host on your web page
#### Links

- [Dilation and Erosion](https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html)
- [Mask Thresholding](https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html)
- [Contour Feature](https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html)
- [Plotting with Altair](https://altair-viz.github.io/getting_started/overview.html)
- [Plotting Peak Width with SciKit Learn](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths)
- [Smoothing Time Series](https://towardsdatascience.com/time-series-in-python-exponential-smoothing-and-arima-processes-2c67f2a52788)
- [Peak Detection](https://pythonawesome.com/overview-of-the-peaks-dectection-algorithms-available-in-python/)