---
layout: post
title: "Plant Movement [Under Construction]"
author: "Sebastian"
categories: project
---

# Attention: This is a construction site.

## Tracking Plants - Basic Infrastructure

Please find my basic training infrastructure that allows us to track the motion of plants via machine learning algorithms.
<iframe width="100%" height="400" src="https://www.youtube.com/embed/xgAhZQMkE7U?start=2" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Hosted in a Jupyter notebook on Google Colab
Try it: [Tracking Plants Colab](https://github.com/plantions/video-edge-extractor/).

### Fine-Tuning Hyperparameters

The Jupyter notebook is designed so that hyper parameters are cumulated and can be trained to fine-tune for the peculiarities of leaf tracking for carnivore plants. ![Hyperparameters](https://i.imgur.com/uU0mCnt.png)

### From Test Files to Comprehensive Dataset

Use the new videos recently created by Prof. Gloor, and benefit from the computing power of your Google Colaboratory Jupyter notebook. (Done)

### Get X, Y-Values for further Plant Analysis
These values are saved in the list leafs. (Done)

### Hyper-Parameter Cross-Tests

- Make sliders to set parameters. (Done)
- Set up cross-validation tables. (in progress)

### Correlate with Underlying Audio Files to Identify Leaf Reactions (tbd)
- Extract the MFCC of the accompanying audio sounds together.
- Continue on Harmonizing of Frames from Video with MFCC from Audio on same timescale.
- Make sure you expand the PandasDataFrame based on the MFCC and extend the video frames.

### Make it clean

- Change file name
- Change headline
- Insert HyperPARAMETER Frames per Second and set by default to 60
- write thoroug explanation
- Write down process > make slides & post them into JPR notebook!?
- Refactor code
- Try different values
- Write down all the experiments
- Go for extreme Values
- Make nice interface on Google Colaboratory

### Key Learnings
- Pandas Data Manipulation: PivotTables, Padding, Indexing.
- Like in the bank: Make compromises.
- "Getting hands dirty" Interview with NLP Deep Learning Expert from Silicon Valley.

### Useful Sources:
- [MFCCs explanation](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) (only the beginning helped me).
- [Output of MFCCs](# https://stackoverflow.com/questions/52232839/understanding-the-output-of-mfcc) (useful to calculate frame length).
- [Meaning of Parameters of FFMPEG](https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg)
- [Visualizing Correlations](https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec)
### Next steps:

- Cutting frames for two Plants
