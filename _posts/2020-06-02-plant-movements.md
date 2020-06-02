---
layout: post
title: "Plant Movement [Under Construction]"
author: "Sebastian"
categories: project
---

## Correlation of Moving Objects with MFCC Sound Features

Status Quo:

<iframe width="100%" height="400" src="xx_long video hosted on youtube " frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Hosted in a Jupyter notebook on Google Colab
Try it: [Tracking Plants Colab](https://github.com/plantions/video-edge-extractor/).

### Fine-Tuning Hyperparameters
The Jupyter notebook is designed so that hyper parameters are cumulated and can be trained to fine-tune for the peculiarities of leaf tracking for carnivore plants. ![Hyperparameters](https://i.imgur.com/uU0mCnt.png)

Hyperparameter findings:

On June 2, 2020, 10AM, I ran 10 tests with various deviating input parameters to uncover the functionality of the different parameters.

#### Favorite

#### Best

Results:
1. Standard Values: Found 2 ROI (11, 18).
2. High Erode (6 px): One ROI only in the middle of nowhere.
3. High Dilate: Found 2 ROI close together around one stem.
4. Medium Mask_Thresh of 127 (0 to 255): Finds leaves more accurately. Found two leaves. __Will focus on this__ value of __127__.
5. Low Contour_Area (50): Four points of interst. __Will keep Contour of 50__.
6. High Mask_Thresh (180): Four ROI, really stable.
7. High Contour_Area (200) & High Dilate: Only two ROI. Consider going back to 50 (see round 5).
8. High Contour_Area (200) & Medium Dilate (4,4): Found three ROI. Quite disparate over the plant (2 left, 1 right).
9. Low Contour_Area (50) & Medium Dilate (4,4): Only two very tiny ROIs.
10. Low Contour (50), high dilate (10), low erode (1): Roughly one 1000 points.

__Conclusion__:
-

### Last sprint tasks
- Compile with comprehensive datasets. (Done)
- Get X, Y-Values for further Plant Analysis: These values are saved in the list leafs. (Done)
- Hyper-Parameter Cross-Tests: Make sliders to set parameters. (Done)
- Correlate with Underlying Audio Files to Identify Leaf Reactions (Done)

### Make it clean

- Change file name
- write thorough explanation
- Refactor code
- Upload final youtube video
- Make Github folder structure nice
- Make nice interface on Google Colaboratory

### Key Learnings
- Theoretical shortcomings of coding fundamentals ('object oriented python') & too little testing ('play more!').
- Insights video codecs & video processing (Running video in Jupyter/on Colaboratory).
- NumPy/Pandas data manipulation: e.g., pivotTables & padding, merging ('getting hands dirty').

### Next Steps

Project-related
- Test more & get outputs fixed.
- Cutting Frames into videos (accounting for the two plants).
- Cut video based on sound patterns into sequences to test for interactions (gender,  emotional expression).

Beyond
- Progress on Fluent Python (fundamentals in Python book) and follow [recommendations](https://seduerr91.github.io/blog/experts) from expert interviews.
- Overcome technical deficiencies (make use of 26gb RAM, parallelize, process on GPU, Make progress of video processing visible).
- Try with different videos from Youtube (not carnivore plants).

### Helpful Sources/Explanations

- [MFCCs explanation](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) (only the beginning helped me).
- [Output of MFCCs](# https://stackoverflow.com/questions/52232839/understanding-the-output-of-mfcc) (useful to calculate frame length).
- [Meaning of Parameters of FFMPEG](https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg)
- [Visualizing Correlations](https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec)
- [Python Statistics](https://scipy-lectures.org/packages/statistics/index.html)
