# Exploring the structure of Chinese language
<p align="center">
  <img src="/static/dendrogram.gif">
</p>

## Description

I’m very interested in the exchange of culture between the East and the West. As China’s economy grows, it becomes increasingly important for these two groups of ideas and people to embrace each other. The language is a great place to start! 

While most Western languages are phonetic, the Chinese Language uses logograms. We learn Chinese through “drawing” pictures of basic characters like fire (火) and wood (木). Compound characters are then built upon these basic ones. For example, if we put two wood (木) side by side we get a forest (林). If you light a fire (火) under the forest (林), you will get burned (焚). There is enough structure in Chinese that many times one can understand the meaning of a character just by looking at the logogram. 

For my capstone project, I propose to use Unsupervised Machine Learning to unravel this structure and ultimately make the Chinese language easier to learn and understand by relating the meaning of words with their characters.

I will be using the image dataset of roughly 34,000 Chinese characters found [here](https://blog.usejournal.com/making-of-a-chinese-characters-dataset-92d4065cc7cc). Convolutional Neural Networks (CNN) are very powerful feature extractors for visual data. The idea is to take the feature maps of a CNN trained to classify Chinese characters and use the techniques of Unsupervised Learning to reveal the relationships between different logograms.

I have put together a short demo of my proposal here. In the demo, I use a subset of the images that covers a diverse set of 1950 characters. I used 2.3 million image in total. I then trained a CNN to classify the characters. In Figure 1, I plot the feature maps applied to 名, 古, 妻. Note that the first two look much closer to each other than the third.


![fig 1](/static/combined.png)
<p align="center">
  Figure 1. feature maps applied to 名, 古, 妻. 
</p>

Initially, I use these features as a basis to compute distances between all of the characters and then use the k-means algorithm to cluster the characters in feature space. The feature maps are extremely high dimensional and projecting the results down to a low dimensional space for visualization is a challenge. I initially used a projection based on PCA however the variance the first two components is only 5%. I eventually settled on using t-SNE to embed my data in 2-dimensions which is shown in Figure 2 or [click here for an interactive plot.](https://chinese-cluster-jiayi.herokuapp.com/embed_plot)

![](/static/cluster_results_Tsn_k_12.png)
<p align="center"> 
  Figure 2. A visualization of the result projected onto a two-dimensional axis. 
</p>

I also tried using hierarchical clustering, which lends itself to more natural plotting. A video of a dendrogram plotting the results in displayed at the beginning. The results look very interesting already! In both cases, the Characters are well organized in a way that makes intuitive sense. What’s really amazing is that I only needed to use 16 features to get both good classification and clustering results for 2000 characters!

I tested how well is the clustering using SSE. While k-mean did better with fewer clusters, hierarchical clustering doing better for more cluster. This makes intuitive sense because hierarchical clustering is a much greedy algorithm than k-mean. Because of this I decide to use k-mean to make larger clusters from the original dataset, then I use hierarchical clustering to further define smaller clusters within the big cluster.
<p align="center">
  <img src="/static/k-mean-vs-hierarchical-clus.png"| width=400>
</p>
<p align="center"> 
  Figure 3. SSE of k-mean vs hierarchical clustering
</p>



There’s plenty of things left to explore for this project. We can get a more complete picture of the language by using the full dataset. I would like to add the meaning of the words next to each cluster and eventually turn the results into a product to help people understand and learn Chinese better. Many characters in Chinese are actually phono-semantic as well. Some of the variance in the clusters cannot be explained just by visual features, but we can potentially augment this analysis using natural language processing techniques!

I hope that through this project, we may understand the Chinese language better. Understanding the structure of the Chinese language is one step forward in our culture exchange!

## Usage

Follow along [conv.ipynb](conv.ipynb) for a small CNN to classify the characters. 

Follow along [cluster-feature.ipynb](cluster-feature.ipynb)
I use the features from CNN as a basis to compute distances between all of the characters and then use the k-means algorithm to cluster the characters in feature space.  


Follow along [cluster-feature-dendrogram.ipynb](cluster-feature-dendrogram.ipynb)
I also cluster the features using hierarchical clustering and plot the result using a interactive dendogram.


## Data

The data comes from this interesting post: [Making of a Chinese Characters dataset](https://blog.usejournal.com/making-of-a-chinese-characters-dataset-92d4065cc7cc)


## Contributing

Please contact me if you have any good ideas about this project!

## Further reading
Please check out the web app developed from this here: https://chinese-cluster-jiayi.herokuapp.com/
