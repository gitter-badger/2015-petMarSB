#!/usr/bin/env ipython
from __future__ import print_function

from itertools import izip
import os
import sys
import json
from collections import defaultdict as ddict
from pprint import pprint
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3, venn3_circles

import seaborn as sns

from figuremanager import FigManager

import screed

import pandas as pd
from pandas import Categorical
import numpy as np
from numpy.random import rand
from scipy import stats
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import scipy.cluster.hierarchy as sch

from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import KMeans

from IPython.display import SVG
from IPython.display import FileLink
from IPython.display import HTML

import mygene
from bioservices import UniProt
