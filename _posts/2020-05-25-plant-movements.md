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

### Tuning Hyperparameters

The Jupyter notebook is designed so that hyper parameters are cumulated and can be trained to fine-tune for the peculiarities of leaf tracking for carnivore plants. ![Hyperparameters](https://i.imgur.com/uU0mCnt.png)

### From Test Files to Comprehensive Dataset

Use the new videos recently created by Prof. Gloor, and benefit from the computing power of your Google Colaboratory Jupyter notebook.
- Done with 'plants_alternating_emotions_w_10s_silence.mov'
- Maybe .mov files do not work, consider converting them to avi with /Users/sebastian/Dropbox/projects/video-edge-extractor/video_cutter.py

### Get X, Y-Values for further Plant Analysis
These values are saved in the list leafs = [].
Each object is a Leaf object with: id, hsv_frame, (x, y, w, h))
- ID: LeafID, respectively another moving object.
- hsv_frame (hue-saturation-value): HSV model uses a different triplet of channels. Hue is the color's tone, saturation is its intensity, and value represents its brightness.
- x, y: Coordinates of the tracked movement.
- w, h: Coordinates of box around tracked movement.

```python
for c in contours:
    if cv2.contourArea(c) > CONTOUR_AREA:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 255, 0), 1)
        if should_initialize_leafs:
            leafs.append(
                Leaf(id, hsv_frame,
                           (x, y, w, h)))
    id += 1

# Question to Paul: Leaf class, how to extract values from it? Just got leaf object identifiers on memory if I print it.

### Hyper-Parameter Cross-Tests

- Make sliders to set parameters. (Done)
- Set up cross-validation tables. (in progress)

### Correlate with Underlying Audio Files to Identify Leaf Reactions (tbd)

- Extract the MFCC of the accompanying audio sounds to start correlation analysis.
- Borrow from the excellent work of Josephine.
