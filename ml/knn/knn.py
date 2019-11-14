#
# This is an example of a K-Nearest Neighbors classifier on MNIST data.
# We try k=1...5 to show how we might choose the best k.

import numpy as np
from sortedcontainers import SortedList
from util import get_data
from datetime import datetime

class KNN(object):
    def __init__(self, k):
        self.k = k

    def fit(self, X, y)
        self.X = X
        self.y = y