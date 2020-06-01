---
layout: post
title: "Plant Movement [Under Construction]"
author: "Sebastian"
categories: project
---

# Attention: This is a construction site.

## Tracking Plants - Basic Infrastructure

Please find my basic training infrastructure that allows us to track the motion of plants via machine learning algorithms.
<iframe width="100%" height="400" src="xx_long video hosted on youtube " frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Hosted in a Jupyter notebook on Google Colab
Try it: [Tracking Plants Colab](https://github.com/plantions/video-edge-extractor/).

### Fine-Tuning Hyperparameters
The Jupyter notebook is designed so that hyper parameters are cumulated and can be trained to fine-tune for the peculiarities of leaf tracking for carnivore plants. ![Hyperparameters](https://i.imgur.com/uU0mCnt.png)

This is what the Hyperparameters do:

### Last sprint tasks
- Compile with comprehensive datasets. (Done)
- Get X, Y-Values for further Plant Analysis: These values are saved in the list leafs. (Done)
- Hyper-Parameter Cross-Tests: Make sliders to set parameters. (Done) & __Set up cross-validation tables. (in progress)__
- Correlate with Underlying Audio Files to Identify Leaf Reactions (Done)
- Clean up. (__Open__)

### Make it clean

- Change file name
- Change headline
- Insert HyperPARAMETER Frames per Second and set by default to 60
- write thorough explanation
- Refactor code
- Try different values
- Write down all the experiments
- Go for extreme Values
- Make nice interface on Google Colaboratory

### Key Learnings
- Shortcomings of Python fundamentals ('object oriented python').
- Video codecs & video processing (Running video in Jupyter notebook / on Google Colaboratory).
- NumPy/Pandas data manipulation: e.g., pivotTables & padding, merging.
- Real-life application: Making compromises with unstructured data.

### Next Steps

- Cutting Frames into videos (accounting for the two plants).
- Cut video based on sound patterns into sequences to test for interactions (gender,  emotional expression).
- Overcome technical deficiencies (make use of 26gb RAM, parallelize, process on GPU, Make progress of video processing visible).
- Try with different videos from Youtube (not carnivore plants).
- Progress on Fluent Python (fundamentals in Python book) and follow [recommendations](https://seduerr91.github.io/blog/experts) from expert interviews.

### Useful Sources
- [MFCCs explanation](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) (only the beginning helped me).
- [Output of MFCCs](# https://stackoverflow.com/questions/52232839/understanding-the-output-of-mfcc) (useful to calculate frame length).
- [Meaning of Parameters of FFMPEG](https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg)
- [Visualizing Correlations](https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec)
- [Python Statistics](https://scipy-lectures.org/packages/statistics/index.html)
