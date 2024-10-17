#!/usr/bin/env python
# coding: utf-8

# # Artificial Intelligence
# ## L2 International, Univ. Bordeaux

# ### Data Preprocessing

# 1. Load and get an overview of the data.


# 2. Uncomment and execute the following instruction. What can you say about the data ? Are there any missing data ?

#titanic.info()


# 3. Write python instructions to drop all the rows with at least one missing data. What do you
# observe ?

# 4. Write python instructions to drop the rows only if all of the values in the row are missing.

# 5. What do you observe about the column Cabin? Write instructions to drop it.

# 6. Discuss the other columns with missing values. Choose the right strategy to replace the missing values.

import pandas as pa
dataset=pa.read_csv('https://www.labri.fr/~zemmari/datasets/titanic.csv')
