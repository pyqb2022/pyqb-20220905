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

# +
sars: str = ''

with open('sars.fasta') as f:
    for line in f:
        if not line.startswith('>'):
            sars += line.strip()
# -

assert len(sars) == 1273


# ### Exercise 2 (max 7 points)
#
# Define a function `n_subseq` that takes a string and a positive integer $n$ and returns a dictionary with the count of the sub-sequences of length $n$. The sub-sequences should be counted starting from the first letter of the string. For example a string of length 7, contains a maximum of 3 different sub-sequences of 2 letters and the last letter is not part of any sub-sequence. In the If you count the sub-sequences of 2 letters in the SARS-CoV-2 sequence, you should get 276 different sub-sequences, and the sub-sequence `'LL'` should be counted 7 times.
#
#
# To get the full marks, you should declare correctly the type hints and add tests within a doctest string.

def n_subseqs(seq: str, n: int) -> dict[str, int]:
    """Return the count of the sub-sequences of length 𝑛 starting from the first letter.
    
    >>> sum(x for x in n_subseqs('X'*7, 2).values()) <= 3
    True
    
    >>> len(n_subseqs(sars, 2))
    276
    
    >>> n_subseqs(sars, 2)['LL']
    7

    """
    
    assert n > 0
    result: dict[str, int] = {}
    
    i = 0
    while i+n <= len(seq):
        s = seq[i:i+n]
        if s in result:
            result[s] += 1
        else:
            result[s] = 1
        i += n
    return result


# ### Exercise 3 (max 5 points)
#
# Plot a pie chart of the occurrences of letters in the SARS-CoV-2 sequence. To get the full marks make good use of the function defined in the previous exercise and put proper labels. 

# +
counts = n_subseqs(sars, 1).items()

fig, ax = plt.subplots()
_ = ax.pie([v for _, v in counts], labels=[k for k, _ in counts], autopct='%.0f%%')

# -

# ### Exercise 4 (max 3 points)
#
# Store in a Pandas dataframe the same information depicted by the pie chart of the previous exercise. The dataframe should have three columns: `letter`, `occurrences`, `percentual`.

sars_df = pd.DataFrame(n_subseqs(sars, 1).items(), columns=['letter', 'occurrences'])


sars_df['percentual'] = sars_df['occurrences'] / sars_df['occurrences'].sum()

sars_df

# ### Exercise 5 (max 2 points)
#
# Print the letters of SARS-CoV-2 that occur at least 5% of the times.

sars_df[sars_df['percentual']  >= .05 ][['letter', 'percentual']]

# ### Exercise 6 (max 4 points)
#
# Take advantage of the [numpy random choice generator](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice) to produce a list of 10000 `str` with length 1273 and composed by the same letters of SARS-CoV-2. Be sure the the process is reproducible (i.e., you are able to get the exactly the same results another time). The process should take less than 10s.

# +
# %%time

rng = np.random.default_rng(666)
sars_rng = [''.join(line) for line in rng.choice(list(set(sars)), size=(10000, 1273))]
# -

# ### Exercise 7 (max 4 points)
#
# Count how many strings among the ones produced during the previous exercise have at most the same number (276) of sub-sequences of 2 letters.

sum([len(n_subseqs(x, 2).keys()) <= 276 for x in sars_rng])

# ### Exercise 8 (max 5 points)
#
# Do the comparison of the previous exercise for the sub-sequences of 2, 3, 4, 5, 6, 7, 8 letters. Print the percentage of cases in which you get a number of sub-sequences exactly equal to the one originally present in the SARS-CoV-2 string.
#
#
#


for i in range(2, 8+1):
    original = len(n_subseqs(sars, i).keys())
    rand = sum([len(n_subseqs(x, i).keys()) == original for x in sars_rng])
    print(f'Sequences of {i} letters: {100*(rand/10000)}%')
