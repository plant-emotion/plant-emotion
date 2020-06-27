---
layout: post
title: "Alternative Modelling Ideas by Peter"
author: "Sebastian"
categories: project
---

On June 19, Peter Gloor provided us with alternative modelling ideas. The ideas are briefly summarized hereafter. Following the question: Perhaps it is worthwhile to model the "step", "wing beat", or "swimming movement" of the Codariocalyx or Mimosa?

##  Reserach Papers

### [Automatically Detect and Track Multiple Fish Swimming in Shallow Water with Frequent Occlusion](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0106506)

![Fish](https://i.imgur.com/Cb1Pkq1.png)

- the authors propose a detection (DoH blob, extreme points, ellipse fitting and contraint) and tracking (motion prediction, feature matching, initial trajectory, and trajectory linking) method
- target detection method:
    - They use the Determinant of Hessian (DoH) to detect image blobs in scale-space. Created by convolving the image with Gaussian kernel function.
    - Ellipse fitting and contraint: they fit ellipse by using the second-order derivative of the extreme point giving them a plurality of head position candidates. Therefore, they used a width threshold value w.
    - Then they use the otsu method for image segmentation via thresholding.
    - Additionally they use contrast contraint (if contrast > k) then head region is considered a head; and angle contraint (if angle is less than 30 degrees that may be a duplicate detection)
- target tracking method:
    - motion prediction: fish motion is a four-dim vector (x,y, v(x), v(y)) i.e. x, y value and velocity of both moving. The movement is then predicted by the Kalman filter. They included a compensation window (only movements ±45 degrees are reasonable).
    - feature matching: find effective features that reflect the similarity among images of the same target and dissimilarity between images of different targets. Active contour model is used for the extraction of fish head contours. Their matching cascade is: width matching, area matching and gray matching.
    - trajectory linking: they use state variables for the linking.
-experiments and discussion: they tried other fish types, and were quite successful with their approach.

###  [Inferring the structure and dynamics of interactions in schooling fish](https://www.pnas.org/content/108/46/18720.short)

![fish2](https://i.imgur.com/IHNXYtY.png)

### [Upwash exploitation and downwash avoidance by flap phasing in ibis formation flight](https://www.nature.com/articles/nature12939)

![Birds](https://i.imgur.com/kCWkYzc.png)

###  [Identity Recognition Algorithm Using Improved Gabor Feature Selection of Gait Energy Image](https://ui.adsabs.harvard.edu/abs/2017JPhCS.787a2015C/abstract)

![Gait](https://i.imgur.com/D6k22kL.png)

- Gait recognition is identifying individuals by the way they walk. - - Approach of authors is: silhouette pre-processing, binarization morph, GEI computation, feature extraction, feature reduction, feature matching.
- Feature extraction of GAI using Gabor filters: its  is a filtering operation of the given GEI with the Gabor filter of size u and orientation v.
- Gait feature dimension reduction based on Kernel Fisher Analysis: Idea of kernel Fisher discriminant is to yield a nonlinear discriminant analysis in the higher space as F.
- Nearest neighbour classifier based on whitened cosine similarity measure: GEIs are normalized and aligned so to be clustered by distance measures.
- Recognition scoring is based on ROC and CMC measures.

###  Additional Videos

- [Mimosa 400x Speedup](https://www.dropbox.com/s/dun532o3s1c49xi/Codariocalyx%2BMimosa-400x.mp4?dl=1)
- [Mimosa 400x Speedup ohne Sound](https://www.dropbox.com/s/1o60nbvionp4uu0/mimosa_nosound-400x.mp4?dl=1)
- [Codariocalyx no Peter](https://www.dropbox.com/s/lb24eyw57qdiocc/codariocalyx_nopeter_nosound-400x.mp4?dl=1)
