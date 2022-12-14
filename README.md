# Machine Learning and CNN Assisted Georeferencing of Remote Sensing Imagery

### Quick Introduction

Georeferencing satellite imagery is typically done by hand using ground control points (GCPs) from a refence image data set that is already georeferenced. This can be fairly quick - albeit tedious -  process in any GIS platform depending on the number of GCPs used for georefencing. The number and quality of GCPs will directly impact the quality of the linear mathematical solution for the georeferencing the image data being processed. This project aims to accelerate the process of georeferencing fresh image data while maintaining (or even surpassing) geospatial location accuracy. 


### Overview

A convolutional neural-network could be trained to identify candidate spaital features of a raw satellite image which could be similarly located in a reference image which has already been mapped to geospaital coordinates. The linear transformation coefficents for a proper tranform can be constructed that would georeference the input image to nearly the same accuracy as the reference image. The tranformation can be applied to the input image to create a GeoTiff image for further analysis. This process would ideally acclerate or replace the tedious process of selecting and moving GCPs in each image by hand. Integrated into data processing pipelines, this automatic direct georeferencing approach could support fully autonomous satellite image processing pipelines to produce analysis ready data (ARD) for further processing. 

### Method

Identifying candidate GCPs in a recent remote sensing data aquisition that can be matched to the same geospatial feature in a georeferened image can be automated through the use of convolutional neural networks. Within the middle layers of a fully trained convolutional neural network, intermediate kernels can be interpreted as one-hot contrast enhanced edge detection kernels. Geospatial features that have traditionally be useful for selecting by human hands typically have high contrast lie at the intersection or vertex of sharp edges of these features. Its much easier to identify the corner of a road in both the processing image and the reference image than it is to identify the center of a crop field in each image. The return value of a CNN-identified geospatial feature that could be GCP candidate would be a subset of pixels that represent the best fit for a feature of interest. The center pixel of this small sub-image would be the pixel of interest to use in the linear transformation in combination with the lat-long coordinate of the reference image. As many as 20 or 30 GCPs are typically used to refine the fit when done by hand. This number could be substaintially higher through an automated process that leverages object detection. 

However, at least one initially obvious edge case immedidately come to mind - high frequency occurances of nearly identical geospatial features. For example, road intersections or corners in a highly urbanized region. Returning the pixel coordinates of the center of such features may be very difficult to discriminate in a list of Feature A: Occurance1, Occurance2, ..., and so forth. This highlights the necessity for spaital context in the broader scene. Astrophysical researchers, expert astrophotography hobbiests, and satellite guidance-naviation-control (GNC) engineers have long been familiar with the problem of high-frequency feature occurance in their datasets. A method referred to as TRIAD is commonly implemented to take relative feature locations into context when defining a broader coordinate transformation. It is this broader context of the scene that must be taken into account for an automated direct gereferencing technique. But the question is: while modern star trackers and astronomy researchers use stellar magnitudes in combination with relative location to discriminate features, how can this be applied to geospatial features in remote sensing imagery? What characteristic can be used to solve the TRIAD equation? 





### Notes

Maybe I should try to solve the object detection problem first. Train a CNN to detect objects that are high quality GCP candidates. 

1. Define 'high quality GCP candidates'








