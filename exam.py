# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: September 5, 2022
#
# You can solve the exercises below by using standard Python 3.10 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.10/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/learn.html).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2122/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#
#
#
#

import numpy as np
import pandas as pd             # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm               # type: ignore
import arviz as az

# ### Exercise 1 (max 3 points)
#
# The file [sars.fasta](/edit/sars.fasta) (source: https://www.ncbi.nlm.nih.gov/protein/YP_009724390.1) encodes the surface glycoprotein for the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).
#
# The line starting with `>` is a comment. Load the letters of the sequence in a `str` variable. The resulting string should have 1273 letters: be sure newlines are not included.

pass

# ### Exercise 2 (max 7 points)
#
# Define a function `n_subseq` that takes a string and a positive integer $n$ and returns a dictionary with the count of the sub-sequences of length $n$. The sub-sequences should be counted starting from the first letter of the string. For example a string of length 7, contains a maximum of 3 different sub-sequences of 2 letters and the last letter is not part of any sub-sequence. In the If you count the sub-sequences of 2 letters in the SARS-CoV-2 sequence, you should get 276 different sub-sequences, and the sub-sequence `'LL'` should be counted 7 times.
#
#
# To get the full marks, you should declare correctly the type hints and add tests within a doctest string.

pass

# ### Exercise 3 (max 5 points)
#
# Plot a pie chart of the occurrences of letters in the SARS-CoV-2 sequence. To get the full marks make good use of the function defined in the previous exercise and put proper labels. 

pass

# ### Exercise 4 (max 3 points)
#
# Store in a Pandas dataframe the same information depicted by the pie chart of the previous exercise. The dataframe should have three columns: `letter`, `occurrences`, `percentual`.

pass


# ### Exercise 5 (max 2 points)
#
# Print the letters of SARS-CoV-2 that occur at least 5% of the times.

pass

# ### Exercise 6 (max 4 points)
#
# Take advantage of the [numpy random choice generator](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice) to produce a list of 10000 `str` with length 1273 and composed by the same letters of SARS-CoV-2. Be sure the the process is reproducible (i.e., you are able to get the exactly the same results another time). The process should take less than 10s.

# +
# %time

pass
# -

# ### Exercise 7 (max 4 points)
#
# Count how many strings among the ones produced during the previous exercise have at most the same number (276) of sub-sequences of 2 letters.

pass

# ### Exercise 8 (max 5 points)
#
# Do the comparison of the previous exercise for the sub-sequences of 2, 3, 4, 5, 6, 7, 8 letters. Print the percentage of cases in which you get a number of sub-sequences exactly equal to the one originally present in the SARS-CoV-2 string.
#
#
#


pass
