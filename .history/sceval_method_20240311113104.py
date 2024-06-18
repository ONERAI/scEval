from typing import List, Tuple, Dict, Union, Optional
import AnnData
import torch
import numpy as np
import scib
import scanpy as sc
import scipy
from scgpt.utils import set_seed
from sklearn.metrics import classification_report
import scipy.stats

class scEval_bench(object):

    def __init__(self, adata):
        self.label = 'scGPT'
        self.adata = adata # adata is the output of the model you plan to benchmark.
        self.pvalue = 0.005






