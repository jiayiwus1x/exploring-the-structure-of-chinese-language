# Exploring the structure of Chinese language
![](/image/cluster_results_Tsne_k_7.png)

## Description

I’m very interested in the exchange of culture between the East and the West. As China’s economy grows, it becomes increasingly important for these two groups of ideas and people to embrace each other. The language is a great place to start! 

While most Western languages are phonetic, the Chinese Language uses logograms. We learn Chinese through “drawing” pictures of basic characters like fire (火) and wood (木). Compound characters are then built upon these basic ones. For example, if we put two wood (木) side by side we get a forest (林). If you light a fire (火) under the forest (林), you will get burned (焚). There is enough structure in Chinese that many times one can understand the meaning of a character just by looking at the logogram. 

For my capstone project, I propose to use Unsupervised Machine Learning to unravel this structure and ultimately make the Chinese language easier to learn and understand by relating the meaning of words with their characters.

I will be using the image dataset of roughly 34,000 Chinese characters found here: https://blog.usejournal.com/making-of-a-chinese-characters-dataset-92d4065cc7cc. Convolutional Neural Networks (CNN) are very powerful feature extractors for visual data. The idea is to take the feature maps of a CNN trained to classify Chinese characters and use the techniques of Unsupervised Learning to reveal the relationships between different logograms.  

I have put together a short demo of my proposal here. In the demo, I use a subset of the images that covers a diverse set of 227 characters. I then trained a small CNN to classify the characters. In Figure 1, I plot the feature maps applied to 名, 古, 妻. Note that the first two look much closer to each other than the third. I use these features as a basis to compute distances between all of the characters and then use the k-means algorithm to cluster the characters in feature space. Figure 2 is a visualization of the result projected onto a two-dimensional axis. 


![fig 1](/image/combined.png)
<p align="center">
  Figure 1. feature maps applied to 名, 古, 妻. 
</p>
The result is already beginning to look interesting! For example, we found words which are basic elements occupying the top left of Figure 2 while complex compound characters are on another side. Some words that share “亻” are clustered together in the center.

![](image/cluster_results.png)

<p align="center"> 
  Figure 2. A visualization of the result projected onto a two-dimensional axis.
</p>

There’s plenty of things left to explore for this project. We can get a more complete picture of the language by using the full dataset. We may get better results by tuning the architecture of the CNN or trying out different unsupervised learning techniques. There’s also the question of what is the best representation of the final results? The feature maps are extremely high dimensional. In Figure 2, I’ve projected the features using PCA however the variance explained by the two axis is only 7%. Many characters in Chinese are actually phono-semantic as well. We can potentially augment this analysis using natural language processing techniques. 

I hope that through this project, we may understand the Chinese language better. Understanding the structure of the Chinese language is one step forward in our culture exchange! 

## Usage

Follow along [conv.ipynb](conv.ipynb) for a small CNN to classify the characters. 

Follow along [cluster-feature.ipynb](cluster-feature.ipynb)
I use the features from CNN as a basis to compute distances between all of the characters and then use the k-means algorithm to cluster the characters in feature space.  


## Data

The data comes from this interesting post: [Making of a Chinese Characters dataset](https://blog.usejournal.com/making-of-a-chinese-characters-dataset-92d4065cc7cc)


## Contributing

Please contact me if you have any good ideas about this project!

## Further reading
