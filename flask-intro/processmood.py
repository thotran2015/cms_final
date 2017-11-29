# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:52:05 2017

@author: Alyssa
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:52:05 2017

@author: Alyssa
"""

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def process(data):
    datarr=np.zeros((len(data),len(data[0]['emos'])))
    for i,sub in enumerate(data):
        for j,emo in enumerate(sub['emos']):
            datarr[i,j]=emo
    X_embedded = TSNE(n_components=3).fit_transform(datarr)
    for i,sub in enumerate(data):
        sub['coords']=X_embedded[i]
    return data
    
data=[{'sub_num': 0, 'emos': (92, 50, 50, 50, 50, 50, 50, 50), 'tags': [u'midterms_exams']}, {'sub_num': 1, 'emos': (100, 50, 50, 50, 50, 50, 50, 50), 'tags': [u'midterms_exams']}, {'sub_num': 2, 'emos': (60, 50, 50, 50, 50, 50, 50, 50), 'tags': [u'midterms_exams']}, {'sub_num': 3, 'emos': (59, 50, 50, 50, 50, 50, 50, 50), 'tags': [u'midterms_exams']}, {'sub_num': 4, 'emos': (50, 50, 65, 100, 50, 50, 50, 50), 'tags': [u'']}, {'sub_num': 5, 'emos': (50, 50, 50, 50, 87, 89, 50, 50), 'tags': [u'relationship']}, {'sub_num': 6, 'emos': (50, 50, 50, 50, 87, 89, 50, 50), 'tags': [u'relationship']}, {'sub_num': 7, 'emos': (80, 50, 78, 50, 33, 41, 70, 50), 'tags': [u'politics']}, {'sub_num': 8, 'emos': (80, 50, 78, 50, 33, 41, 70, 50), 'tags': [u'midterms_exams', u' future', u' weather', u' politics']}, {'sub_num': 9, 'emos': (21, 50, 16, 85, 50, 80, 76, 50), 'tags': [u'future', u' weather', u' homesickness']}]


#plot to test:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data2=process(data)
X_embedded=np.array([i['coords'] for i in data])
ax.scatter(X_embedded[:,0],X_embedded[:,1],X_embedded[:,2])

