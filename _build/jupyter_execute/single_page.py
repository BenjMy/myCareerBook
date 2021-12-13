#!/usr/bin/env python
# coding: utf-8

# # A notebook to demonstrate single-page outputs

# ## Footnotes
# 
# You can include footnotes in your single page like so: [^foot1]

# # Margin
# 
# Margin works:
# 
# ```{margin}
# This is my margin
# ```

# ## Toggle
# 
# Toggle works as well:
# 
# ````{toggle}
# ```{note}
# Wow, a toggled note!
# ```
# ````

# # Python and outputs

# In[ ]:


import pandas as pd 


# In[ ]:


df = pd.util.testing.makeDataFrame()
df.plot.scatter("A", "B")


# In[ ]:


import altair as alt
alt.Chart(data=df).mark_point().encode(
    x="A",
    y="B",
    size="C"
)


# [^foot1]: Wow, a footnote!
