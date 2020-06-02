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
Try it: [Final Colab Link](https://github.com/plantions/video-edge-extractor/).

### Hyperparameter Testing

On June 2, 2020, 10AM, I ran 10 tests with various deviating input parameters to uncover the functionality of the different parameters.

Let us take a look.

##### Favorite

![Imgur](https://i.imgur.com/fe5HRlD.png)

##### Best

![Imgur](https://i.imgur.com/udilLsM.png)

__Conclusion__:
- Four identified values were best but they were never at leaf tips.
- Very detailed export possible with experiment 10. Follow up here.
- Content with results. More testing needed.

### Last sprint tasks
- Compile with comprehensive datasets. (Done)
- Get X, Y-Values for further Plant Analysis: These values are saved in the list leafs. (Done)
- Hyper-Parameter Cross-Tests: Make sliders to set parameters. (Done)
- Correlate with Underlying Audio Files to Identify Leaf Reactions (Done)

### Make it clean
- Write thorough explanation
- Refactor code
- Upload final youtube video
- Make Github folder structure nice
- Make nice interface on Google Colaboratory

### Key Learnings
- Theoretical shortcomings of coding fundamentals ('object oriented python') & too little testing ('play more!').
- Insights video codecs & video processing (Playing video in Jupyter/on Colaboratory).
- NumPy/Pandas output & data manipulation: e.g., pivotTables & padding, merging ('getting hands dirty').

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
