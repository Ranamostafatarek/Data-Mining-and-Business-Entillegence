#!/usr/bin/env python
# coding: utf-8

# In[91]:


import traceback


# In[92]:


def green(s):
    return '\033[1;32m%s\033[m' % s


def yellow(s):
    return '\033[1;33m%s\033[m' % s


def red(s):
    return '\033[1;31m%s\033[m' % s


def log(*m):
    print(" ".join(map(str, m)))


def log_exit(*m):
    log(red("ERROR:"), *m)
    exit(1)


# In[93]:


def check_numpy():
    try:
        import numpy
        log(green("PASS"), "NumPy installed")
    except ModuleNotFoundError:
        log(red("FAIL"), "NumPy not installed")


# In[94]:


def check_scipy():
    try:
        import scipy
        log(green("PASS"), "SciPy installed")
    except ModuleNotFoundError:
        log(red("FAIL"), "SciPy not installed")


# In[95]:


def check_matplotlib():
    try:
        import matplotlib
        log(green("PASS"), "matplotlib installed")
    except ModuleNotFoundError:
        log(red("FAIL"), "matplotlib not installed")


# In[96]:


def check_torch():
    try:
        import torch
        log(green("PASS"), "PyTorch installed")
    except ModuleNotFoundError:
        log(red("FAIL"), "PyTorch not installed")


# In[97]:


def check_tqdm():
    try:
        import tqdm
        log(green("PASS"), "tqdm installed")
    except ModuleNotFoundError:
        log(red("FAIL"), "tqdm not installed")


# In[98]:


def main():
    try:
        check_numpy()
        check_scipy()
        check_matplotlib()
        check_torch()
        check_tqdm()
    except Exception:
        log_exit(traceback.format_exc())


# In[99]:


if __name__ == "__main__":
    main()


# In[ ]:




