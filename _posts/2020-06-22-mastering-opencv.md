---
layout: post
title: "Optimizing OpenCV for the Object Tracker"
author: "Sebastian"
categories: project
---
### Summary of Relevant Passages of the Book: Mastering OpenCV 4 with Python

# Chapter 5 - Image Processing

## Image Filtering

- Introduction of many filters of which _Gaussian Blur_ and, _Bilateral Filtering (big values)_ look the best, _boxFilter_ seems relevant as it is quite non-detailed but may suffice for plants.

## Morphological transformations

- Normally performed on binary images and based on the image shape.
- Dilation: main effect on a binary image is to gradually expand the boundary regions of the foreground object.
- Erosion: gradually erode away the boundary regions of the foreground object.
- Opening operation: performs an erosion followed by a dilation using the same structuring element or kernel for both operations.
- *The combination of opening and closing operation (or the other way round) seems to work the best.*

# Chapter 6 - Constructing and Building Histograms

- Contrast limited adaptive histogram equalization (CLAHE): Applied to improve the contrast of images. Works by creating several histograms of the original image, and uses all of these histograms to redistribute the lightness of the image.

# Chapter 7 - Thresholding

- Used to partition an image into different regions that correspond to real-world objects.
- Image thresholding is a simple image segmentation method, where the pixels are partitioned depending on their intensity value.

## Adaptive Thresholding

- Results of global thresholding may not be good due to different illumination conditions in the different areas of an image. Therefore, try adaptiveThresholding.
- Resolve noise by applying a bilateral filter (to maintain sharp edges) with _cv2.bilateralFilter()_.

## Otsu Thresholding

- For use with bimodal images that are characterized by their histogram containing two peaks; Otsu then calc's the optimal thresh value.
- Noise impacts thresh algorithm, therefore, use a Gaussian filter before.

## Triangle Binarization Algo

- Shape-based method that analyses the structure of the histogram (finding peaks, values, etc).
- Steps:
  - (1) line is calc'ed between max of histogram and lowest value b on Gray level axis;
  - (2) distance from line for all values of b is calc'ed;
  - (3) distance between the histogram and the line is maximal is chosen as thresh value
- __May be worth trying but also use Gaussian filter before.__

## Thresholding Color Images

- Thresholding is applied to all three channels (RBG) of an image. Maybe for green channel for the plants?
- [Internal note: See screenshot 'green tresh'.]

## Thresholding w/ Scikit-image

- More thresh techniques: Otsu and Triangle are global thresholding techniques (i.e. background is uniform); while __Niblack and Sauvola__ are __local__ thresholding techniques (better for plants because background is not uniform; internal note see 'Sauvola').

# Chapter 8 - Contour Detection, Filtering, and Drawing

## Contour Detection

- Contour: sequence of points defining the boundary of an object in an image. Like a curve joining all the points along the boundary of a certain shape.
- Technical def: array composed of many points of np.int32 type.
- OpenCV provides cv2.findContours() which can be used to detect contours in binary images (after a thresholding operation).
- Differnt contour modes:
    - retr_external: only external contours.
    - retr_list: all contours.
    - retr_tree: all contours with hierarchical relationship.
- Compressing contours: detected contours are compressed to reduce the number of points: cv2.CHAIN_APPROX_SIMPLE will make a box only 4 points; sophisticated versions are: TC89_L1, and cv2.CHAIN_APPROX_TC89_KCOS.

## Image Moments

- Specific quantitative measure of a function shape. They are features computed from contours allowing a geometrical reconstruction of the object.
- Useful to describe some properties of the detected contours (Center of mass of the object, area of the object).
- Moment measures:
    - Roundness: measure of how closely a contour approaches the contour of a perfect circle.
    - Eccentricity (elongation): measure of how elongated a contour can be. Therefore, calculate the ellipse that fits the contour and afterwards derive two axes a and b.
    - The aspect ratio can be easily calculated based on the dimensions of the minimal bounding rectangle, calc'ed with cv2.boundingRect().

## Hu Moment Invariants

- Are invariant with respect to translation, scale, and rotation, and all the moments are invariant to reflection.
- First calc the moments by using cv2.moments(), afterwards use cv2.cvtColor to make image binary, then calc the hu moments.

## Zernike Moments

- __mahotas__ python module provides the zernike_moments() function. Try it out.

## More Functionality Related to Contours
- Image and extreme points: extreme_points calculates the four extreme points defining a given contour.
- cv2.minAreaRect(): returns minimal bounding rectangle enclosing all points of the contour - __rotated__ if necessary; to return the four vertices use cv2.boxPoints().
- cv2.ellipse(): returns ellipse with the minimum least square errors fitting all the points of the contour.
- cv2.boundingRect(): returns minimal bounding rectangle enclosing all points of the contour.
- cv2.minEnclosingCircle(): returns minimal circle, center and radius.
- cv2.approxPolyDP(): returns a contour approximation of given contour based on the given precision (using Douglas Peucker); epsilon establishes the precision, determining, the max distance between the original curve and its approximation.

## Filtering Contours

- Sort_contours_size(): sorts contours based on the size. To Do: Use to get the biggest contours for your allocation.

## Recognizing Contours

- cv2.approxPolyDP(): can be used to approx. one contour with another with fewer points through Douglas-Peucker algo.
- Key param is epsilon: sets the approx. accuracy; to decimate a number of points, given a certain contour, we first compute the perimeter.

## Matching Contours

- cv2.matchShapes(): compare two contours using three comparison methods: I1, I2, and I3.
- Draw a perfect circle, then a reference file is used. Find contours through: conversion to grayscale (cv2.cvtColor), binarize (cv2.threshhold), find contours (cv2.findContours).

# Chapter 9 - Augmented Reality

## Intro to AR

- Location-based: relies on detecting the user's location and orientation by reading data from several sensors.
- Recognition-based: uses image processing techniques to derive where the user is looking.
    - marker-based pose estimation: using planar markers.
    - markless-based pose estimation: when scene cannot be prepared using markers.

## Feature Detection

- Harris Corner Detection, Shi-Tomasi, SIFT, SURF< FAST, BRIEF< ORB

#### To Dos

- Look up Zernike Moments and see how it helps you.
- Look for Harris Corner detection; check again on DataCamp platform for the good algorithms.
- Show real image for multiple thresholds (compare multiple thresholds1 and multiple thresholds2).
- Check histogram for your flying paprika.
- Do the FLASK web project on Face Recognition & host on your web page as a weekend project.

#### Residuals Chapter Overview

- Chapter 1 is an introduction to Python and OpenCV
- Chapter 2,3 relate to Image basics and Handling Files and Images with OpenCV
- Chapter 4 explains how to draw basic shapes in OpenCV
- Chapter 6 is about building histograms
- Chapter 9 regards Augmented Reality in OpenCV
- Chapter 10 is on Machine Learning and Deep Learning in OpenCV
- Chapter 11 deals with Face Detection, Tracking, and Recognition
- Chapter 12 introduces Deep Learning
- Chapter 13 is on Mobile and Web Computer Vision (like recognizing cats)
