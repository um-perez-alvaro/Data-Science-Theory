# Clustering Algorithms

**Clustering** is an example of unsupervised learning, in which we work with completely unlabeled data (we have the feature matrix X, but we do not have the label vector y). Clustering attemps to group objects together based on similarity (or distance). The objective of clustering is to identify distinct groups in a dataset such that the observations within a group are similar to each other but different from observations in other groups.

**When is Clustering Used in Industry?**
- segment groups of customers based on their activity with an app to deliver unique marketing messages
- find similar text documents (could also be tweets, posts, etc) by their words/phrases
- data compression to reduce the size of data files

## Jupyter notebooks
- [k-Means](https://nbviewer.jupyter.org/github/um-perez-alvaro/Data-Science-Theory/blob/master/Jupyter%20Notebooks/Clustering%20algorithms/notebooks/k-means.ipynb)
- [Agglomerative Hierarchical Clustering]()

## Homework Assignment 5 ()

- [Problem 1: Flowers, irises and penguins](https://nbviewer.jupyter.org/github/um-perez-alvaro/Data-Science-Theory/blob/master/Jupyter%20Notebooks/Clustering%20algorithms/homework/Problem%201.ipynb)
- [Problem 2: Clustering for color segmentation](https://nbviewer.jupyter.org/github/um-perez-alvaro/Data-Science-Theory/blob/master/Jupyter%20Notebooks/Clustering%20algorithms/homework/Problem%202.ipynb)
- [Problem 3: Greedy initialization of k-means](https://nbviewer.jupyter.org/github/um-perez-alvaro/Data-Science-Theory/blob/master/Jupyter%20Notebooks/Clustering%20algorithms/homework/Problem%203.ipynb)

## Homework Assignment 6 ()

- [Problem 4: Clustering genes]() 
- [Problem 5: Document clustering]()
- [Problem 6: TBD]()

## Datasets
Filename | Description |  Source
--- | --- |  --- 
[iris.csv](https://raw.githubusercontent.com/um-perez-alvaro/Data-Science-Practice/master/Data/iris.csv) | 50 samples of 3 different species of iris | [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
[penguins_size.csv](https://raw.githubusercontent.com/um-perez-alvaro/Data-Science-Theory/master/Data/penguins_size.csv) | This dataset contains data for 344 penguins. There are 3 different species of penguins in this dataset, collected from 3 islands in the Palmer Archipelago, Antarctica | [Kaggle](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) </br> [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)
[St_Basil_Cathedral.png](https://raw.githubusercontent.com/um-perez-alvaro/Data-Science-Theory/master/Data/St_Basil_Cathedral.png) | Saint Basil's Cathedral | [Wikipedia](https://commons.wikimedia.org/wiki/File:1_Saint_Basils_Cathedral.jpg)
[cancer_cells.png](https://raw.githubusercontent.com/um-perez-alvaro/Data-Science-Theory/master/Data/cancer_cells.png) | breast cancer cells | [Machine Learning for Cancer Diagnosis and Prognosis](http://pages.cs.wisc.edu/~olvi/uwmp/cancer.html)
[flowers.npy](https://github.com/um-perez-alvaro/Data-Science-Theory/blob/master/Data/flowers.npy?raw=true) | 61 images of flowers of three different species | [Kaggle](https://www.kaggle.com/olgabelitskaya/flower-color-images/code) </br> [TDS](https://towardsdatascience.com/how-to-cluster-images-based-on-visual-similarity-cd6e7209fe34)
[Dailykos.csv](https://raw.githubusercontent.com/um-perez-alvaro/Data-Science-Theory/master/Data/dailykos.csv) | contains data on 3,430 news articles or blogs that have been posted on Daily Kos. These articles were posted in 2004, leading up to the United States Presidential Election | [The Analytics Edge](https://ocw.mit.edu/courses/sloan-school-of-management/15-071-the-analytics-edge-spring-2017/index.htm)



