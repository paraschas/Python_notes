# Pandas notes


import
```
import pandas as pd
```


Check whether a dataframe is empty.
```
df.empty
```
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html


Generate a list of dataframes from tables in an HTML page.
```
# e.g.

link = "https://docs.python.org/3/library/functions.html"
match = "Built-in Functions"
df_list = pd.read_html(io=link, match=match)

print(df_list[0])
```
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html
