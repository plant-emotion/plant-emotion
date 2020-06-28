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

- oberserving kinematics: we map the instantaneous acceleration (behavioral response) of a focal fish due to the influence of its neighbors; such complex biological reactions are interpreted as individual accelerations in response to fish neighbors’ positions and velocities
- Analysis of two shoals of fish:
    - compute the acceleration of one fish as a function of the position and velocity of its neighbor. 
    - repulsive and attractive zones: When the neighboring fish is close to the focal fish, a repulsive force is exerted on the focal fish, pushing it away from its neighbor. When the neighboring fish is far away, an attractive force is exerted on the focal fish, pulling it toward its neighbor.
    - Fish control their motion by modulating their speeds and by turning. To reflect this, the authors decompose the force into two components, the component along a fish’s direction of motion (speeding up and slowing down; the “speeding force”), and the component perpendicular to its direction of motion (the “turning force”).
    - Turning & Speeding:  
        - When the neighbor is far to the right of the focal fish, it turns right (positive values), toward it, and when the neighboring fish is far to the left of the focal fish, it turns left (negative values), toward it. 
        - In a complementary manner to the speeding force, the turning force depends almost exclusively on how far the neighboring fish is to the side of the focal fish, and not on its distance in front of or behind it.
- Analysis three shoals of fish: when both neighbors are far in front of, or far behind, the focal fish (2-4 body lengths), there is a strong tendency to speed up/slow down
- Analysis of even bigger shoals of fish: We find that the predominant response of individuals in larger groups is to maintain spacing with near neighbors, decelerating or accelerating to avoid those very close behind or ahead, respectively, or to turn away from neighbors who approach very closely from either side.
- Discussion:
    - We find mean effective forces that depend on nontrivial combinations of the neighbor’s position and velocity, such as position-dependent restitution forces and preferred distances to neighbors that increase for faster-moving fish
    - Research Gap: Our approach should also be applied to kinematic data from other animals and other species of fish to determine which aspects of the effective forces are universal signatures of biological groups
    - Note: group heading is determined by frontal group members passing information to the rear (43, 44)
    - Novelty: speed information flows bidirectionally, with fish responding to the speed changes of those swimming both ahead and behind
    - The main feature of the residual three-body interaction is an excess restitution force that helps the focal fish remain in configurations where it is between its two neighbors

- [Tracking Method](http://www.pnas.org/lookup/suppl/doi:10.1073/pnas.1107583108/-/DCSupplemental/pnas.1107583108_SI.pdf?targetid=STXT): data extraction is performed using the OpenCV library. Because the fish appear darker than the surrounding area, the images are converted to gray scale and inverted. A background image is made by averaging a sufficiently large number of frames (until fish are no longer visible) and subtracted from each frame. The fish are then identified by thresholding with an empirically determined constant value. The contours of each fish are obtained by applying an edge-detection algorithm on the thresholded image and approximated by polygons


### [Upwash exploitation and downwash avoidance by flap phasing in ibis formation flight](https://www.nature.com/articles/nature12939)

![Birds](https://i.imgur.com/kCWkYzc.png)

- Here we show that individuals of northern bald ibises (Geronticus eremita) flying in a V flock position themselves in aerodynamically optimum positions, in that they agree with theoretical aerodynamic predictions. Furthermore, we demonstrate that birds show wingtip path coherence when flying in V positions, flapping spatially in phase and thus enabling upwash capture to be maximized throughout the entire flap cycle
- this mechanism reduces heart rate and wing-beat frequency 
- maybe also use wingtips (aka leaves) to track 
- Flapping in spatial phase indicates that the wing of a following bird goes up and down tracking the path through the air previously described by the bird ahead. The following bird then benefits from consistently flapping into the upwash region from the preceding bird (Fig. 3b, c), presumably reducing the power requirements for weight support
- temporal phasing of flapping relates both to streamwise and to spanwise position. This indicates remarkable awareness of, and ability to respond to, the wing- path—and thereby the spatial wake structure—of nearby flock-mates
- Birds (equipped in Zoo Vienna) with Data loggers (GPS 5 Hz
- Initial Data Processing: interpolation replaced missing values in the GPS; GPS and accelerometer data were passed through a fourth-order Butterworth filter
- To calculate the centroid of the flock, the MATLAB function ‘centroid’ was used. This function calculates the centroid of a polygon. The MATLAB centroid function treated each bird as a point of a polygon, and determined the centroid for each time point.

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
