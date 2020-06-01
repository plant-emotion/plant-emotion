---
layout: post
title: "Update: Plant Emotions with Peter"
author: "Josephine & Sebastian"
categories: project
---

## Agenda

1. Status Quo: Josephine's work, Sebastian's work  [30 min: 15 min each]
2. Feedback [10 min]
3. Organizational Matters [5 min]
4. Next Steps [10 min]

## Content

### Status Quo: Josephine's work, Sebastian's work  [20 min: 10 min each]

#### Status Quo: Josephine's work [10 min]

##### Status Quo
1. Finished Mimosa x MFCC Analysis with old data
2. Wrote script to split video into samples
3. Started analysis of new data: MFCC and Movement Analysis for all samples (started with Codariocalyx, soon to be followed by Mimosa)
4. Added lines of code to reliably calculate up-/down-time and rise-/fall-time for all samples
5. Having an increased sample size, I added some sub analyses to the initial procedure: Trend of correlation coefficients & MFCCs
6. Coded samples -> Happy/Sad, female/male -> Currently used for fitting regression model; soon to be used for trying some machine learning algorithms, eg classification
7. Outlined the bigger picture: Making it 2 papers? If so, structure of each. Checked how current research efforts fit in & what should be done additionally.

##### Next Steps

1. Continue analysis of new data
2. Detailed research model & plan
3. Find best way to integrate MFCC analysis into plan
4. Regression with controls

#### Status Quo: Sebastian's work [10 min]

##### Status Quo

Overview of my first two weeks into the project.

1. Audio Processing: [audiofile_creator](https://github.com/plantions/creatingEmotionAudios) and [Research on MFCC](https://plantions.github.io/project/2020/05/11/sound.html).
2. Object Tracking: Advancing book on [OpenCV4](https://plantions.github.io/project/2020/05/14/opencv.html) for object tracking in [Jupyter notebook](https://github.com/plantions/video-edge-extractor) with focus on [tracking leaves](https://github.com/plantions/video-edge-extractor/blob/master/Tracking_leaves.ipynb).
3. Coordinating Infrastructure: Meets with Josephine, [Blog](plantions.github.io), [Trello](https://trello.com/b/bgOuMEt0/mit-emotions-via-plants), [Github Repository](https://github.com/plantions), [Google Drive](https://drive.google.com/drive/folders/1eXMw6ud5SzLtQtpqs4tOAtf8WXSMhvWM), and [Mendeley Team](https://www.mendeley.com/community/plantions.net/).

##### Next Steps

These will be Sebastian's further steps, scheduled for May 2020. *What is your opinion about them?*

- Replicate Josephine's results with new datasets (videos) in Python.
- Try to automatise, use different algorithms learned in OpenCV4 book; consider training a plant recogniser.
- Read into literature (found in Buenyamin's contribution, book from Josephine, own research).

### Collaboration Tools & Coordination [5 min]

Please find a brief overview on how Josephine and Sebastian are collaborating. We kindly invite you to be part of any system we are using. However, we assume that you are very busy, and, hence, we would continue to create concise summaries like this blog to navigate you through our works.

- Weekly coordination meetings for May/June 2020: every Tue, 17-18h, and every Fri, 14-14:30, Austrian time. *Do you want to participate regularly?*
- Coordination tools: Trello, Github, Meets, Whatsapp. *Do you want to be invited to any?*
- Progress tracking: [On this blog](plantions.github.io). *We would send you posts directly, if we deem them necessary*
- Roadmap: tbd. *Maybe we can draft an initial version after part 4 'Strategic Assessment'*

### Brainstorming / Feedback: How to improve data quality [5 min]

Hereafter, we list ideas to improve the tracking of the carnviore plants, if we get another iteration. Right now, we do not see the need, though. Maybe, we can extend this list together.

- Uniform background colour
- More, brighter light / waiting for sunny days
- Note down contingency variables like: weather, location, time of the day
- Place a ruler next to plant
- What kind of camera did Peter use? Is depth measuring possible with it?

Possible control variables we've thought of:
- Temperature
- Light: Duration, spectral distribution/ energy
- Soil minerals & nutrients
- Soil moisture
- CO2 and oxygen levels
- Air: humidity

### 'Strategic' Assessment [10 min]

We value your opinion and would want to hear what you are planning with us. Open questions that may guide this section are:

- What do you think about our collaboration & coordination?
- What is your idea behind our project ('plant sensor pot')?
- What academic contributions can we target (e.g., related conferences, journals, proceedings)?
- What did we miss in this session?

### Organizational Matters: Updates on MIT and Covid19 [5 min]

We are aware that the current situation is difficult to predict, and so, were are not expecting any updates.
Still, do you have some? :wink:

### Thank you very much for your time, and your guidance.
