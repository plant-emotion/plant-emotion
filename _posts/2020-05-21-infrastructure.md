---
layout: post
title: "Leaf Identifier Infrastructure"
author: "Sebastian"
categories: project
---

## Tracking Plants - Basic Infrastructure

Please find my basic training infrastructure that allows us to track the motion of plants via machine learning algorithms.

![Identified Leafs](https://i.imgur.com/jdQEI11.png)

### Hosted on Google Colab

As of today, the basic infrastructure is live and is framed so that it runs remotely on a high-end computer via Google Colaboratory. This is particularly helpful as my mini Macbook Air does not have sufficient computing power to process large datasets in HQ.

To try it yourself, please use the following link: [Tracking Plants Colab](https://github.com/plantions/video-edge-extractor/blob/master/20200521_Tracking_Plants_Colab_Refactored1.ipynb). You simply have to upload any video. The steps for that are quite simple. 

### Overview on the Notebook's Structure

In general, the notebook works asks you to connect to a computing engine via Google Colab (this is free), and then:

1. Run code formattings and the leaf class
2. Choose/tune your parameters.
3. Create a Video by the Kalman filter and the Meanshift algorithm.
4. Convert the resulting MPEG file and watch your result directly in Google Colab.

![Notebook](https://i.imgur.com/kJ8Joct.png)

### Initial Test Runs

With the following parameters: __MASK_THRESH = 40__ & __CONTOUR_AREA = 200__ the following four moving leaves were identified in a 20 second test sample: 
![Identified Leafs](https://i.imgur.com/jdQEI11.png)

### Tuning Hyperparameters

The Jupyter notebook is designed so that relevant hyperparameters are cumulated and can be trained to fine-tune for the peculiarities of leaf tracking for carnivore plants. ![Hyperparameters](https://i.imgur.com/uU0mCnt.png)

## Next Steps 

### From Test Files to Comprehensive Dataset

Use the new videos recently created by Prof. Gloor, and benefit from the computing power of your Google Colaboratory Jupyter notebook.

### Get X, Y-Values for further Plant Analysis

Take the values of each individual moving leaf and plot on a graph with x-Axis as deviations in height, and y-Axis as a temporal (based on frames) identifier. 

### Hyper-Parameter Cross-Tests

- Make sliders to set parameters.
- Set up cross-validation tables.

### Correlate with Underlying Audio Files to Identify Leaf Reactions

- Extract the MFCC of the accompanying audio sounds to start correlation analysis.
- Borrow from the excellent work of Josephine.