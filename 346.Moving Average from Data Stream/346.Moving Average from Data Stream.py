#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# 等同于MATLAB中的smooth函数，但是平滑窗口必须为奇数。

# yy = smooth(y) smooths the data in the column vector y ..
# The first few elements of yy are given by
# yy(1) = y(1)
# yy(2) = (y(1) + y(2) + y(3))/3
# yy(3) = (y(1) + y(2) + y(3) + y(4) + y(5))/5
# yy(4) = (y(2) + y(3) + y(4) + y(5) + y(6))/5
# ...

def smooth(a,WSZ):
    # a:原始数据，NumPy 1-D array containing the data to be smoothed
    # 必须是1-D的，如果不是，请使用 np.ravel()或者np.squeeze()转化 
    # WSZ: smoothing window size needs, which must be odd number,
    # as in the original MATLAB implementation
    out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ
    r = np.arange(1,WSZ-1,2)
    start = np.cumsum(a[:WSZ-1])[::2]/r
    stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
    return np.concatenate((  start , out0, stop  ))

# another one，边缘处理的不好

"""
def movingaverage(data, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(data, window, 'same')
"""

# another one，速度更快
# 输出结果 不与原始数据等长，假设原数据为m，平滑步长为t，则输出数据为m-t+1

"""
def movingaverage(data, window_size):
    cumsum_vec = np.cumsum(np.insert(data, 0, 0)) 
    ma_vec = (cumsum_vec[window_size:] - cumsum_vec[:-window_size]) / window_size
    return ma_vec
"""
