---
layout: post
title: "Plant Movement [Under Construction]"
author: "Sebastian"
categories: project
---
## Correlation of Moving Objects with MFCC Sound Features
<iframe width="100%" height="400" src="https://www.youtube.com/embed/O9Tr3f6X8tg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Hosted on Google Colaboratory; Open with GitHub.
Try it: [Github with Colab](https://github.com/plantions/video-edge-extractor/).

### Hyperparameter Testing
On June 2, 2020, 10AM, I ran 10 tests with various deviating input parameters to uncover the functionality of the different parameters.

##### Favorite
![Imgur](https://i.imgur.com/fe5HRlD.png)

##### Best
![Imgur](https://i.imgur.com/udilLsM.png)

### Conclusion
- Four identified values were best but they were never at leaf tips.
- Very detailed export possible with experiment 10. Follow up here.
- Content with results. More testing needed.

### Tasks from Sprint 2
- Compile with comprehensive datasets. (Done)
- Get X, Y-Values for further Plant Analysis: These values are saved in the list leafs. (Done)
- Hyper-Parameter Cross-Tests: Make sliders to set parameters. (Done)
- Correlate with Underlying Audio Files to Identify Leaf Reactions. (Done)

### Retro Sprint 2
- Theoretical shortcomings of coding fundamentals ('object oriented python') & too little trials ('play more!').
- Insights video codecs & video processing ('Playing video in Jupyter/on Colaboratory').
- NumPy/Pandas output & data manipulation: e.g., pivotTables & padding, merging ('Getting hands dirty').

### Next Steps

Project-related:
- Test more (get best hyper-parameters).
- Cutting frames from video to account for the two plants.
- Cut video based on sound patterns into sequences to test for interactions (gender,  emotional expression).

Beyond:
- Progress on Fluent Python (fundamentals in Python book) and follow [recommendations](https://seduerr91.github.io/blog/experts) from expert interviews.
- Overcome slow processing (make use of 26GB RAM, process on GPU, make progress of video processing visible).
- Try with different videos from Youtube (not carnivore plants).

### Helpful Sources/Explanations

- [MFCCs explanation](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) (only the beginning helped me).
- [Output of MFCCs](# https://stackoverflow.com/questions/52232839/understanding-the-output-of-mfcc) (useful to calculate frame length).
- [Meaning of Parameters of FFMPEG](https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg)
- [Visualizing Correlations](https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec)
- [Python Statistics](https://scipy-lectures.org/packages/statistics/index.html)
