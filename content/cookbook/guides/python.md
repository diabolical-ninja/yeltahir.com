---
title: "Python"
draft: false
toc:
  auto: false
---

# Handy Tricks for Python

## Common Libraries

Some handy, common libraries

```python
pip install tqdm
pip install pyodbc
pip install plotly
pip install h2o
pip install distance
pip install slackClient
pip install dash==0.17.7  
pip install dash-renderer==0.7.4
pip install dash-html-components==0.7.0
pip install dash-core-components==0.12.0
pip install plotly==2.0.13
```

## Jupyter Start-Up Magics

Generally making jupyter life better & easier

```python
# Matplotlib inline rendering
%matplotlib inline

# Allow plotly to operate within the notebook
init_notebook_mode()

# General pandas settings to:
#  - Shush pandas copy warning
#  - Pandas show more columns
pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 200)

# Extension Reloads
%load_ext autoreload
%autoreload 2
```


## Column Wise Binariser

The pandas function `get_dummies` is great but can cause memory issues with datasets that have many categories or lots of data. This function applies it column by column, which while much slower requires much less memory.

```python
import pandas as pd

def column_binariser(df, columns):
    catlist = []

    for i in columns:
        catlist.append(pd.get_dummies(data=df[i], prefix=str(i)))

    dfbin = pd.concat(catlist, axis=1)
    dfrem = df.drop(columns, axis=1)
    dfcon = pd.concat([dfbin, dfrem], axis=1)        
    
    return dfcon
```
	
	
	
## ODBC Connection & Query

```python
import pandas as pd

cnxn = pyodbc.connect("DRIVER={SQL SERVER};SERVER=<server name>")
df = pd.read_sql(con = cnxn, sql = "<SQL Query>")
```


## Jupyter Slideshow Code Hiding

One of the coolest things about Jupyter is the ability to instantly turn analysis into a presentation. Unfortunately that also comes with all the code used in the analysis, generally not something your audience are interested. This handy snippet removes all code blocks from the resulting presentation.

```javascript
<script>
    var code_show=true; //true -> hide code at first

    function code_toggle() {
        $('div.prompt').hide(); // always hide prompt

        if (code_show){
            $('div.input').hide();
        } else {
            $('div.input').show();
        }
        code_show = !code_show
    }
    $( document ).ready(code_toggle);
</script>
```

To actually generate the deck run the following in your terminal of choice:

```bash
jupyter nbconvert "<notebook name>".ipynb --to slides --post serve
```


## Plotly Time Series

```Python
import plotly.graph_objs as go
import plotly.plotly as py
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Allow plotly to operate within the notebook
init_notebook_mode()


# List of df columns to plot
cols = ['col_1','col_2']

data = [go.Scatter(
            x = df['<timestamp col>'],
            y = df[x],
            name = x)
       for x in cols]

layout = go.Layout(
            title = 'My Title',
            xaxis = dict(title = "Timestamp"),
            yaxis = dict(title = "something"
        )
)

fig = go.Figure(data = data, layout = layout)
iplot(fig)
```

## Jupyter 

Often times when plotting using javascript libraries (plotly, atlas, etc) the jupyter rate limit can be exceeded meaning no plots are displayed. Maxing out the rate limiter when starting up tends to resolve this. 

```bash
jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10
```


## Pandas CSV Exporting

The CSV module is required for quoting & other items.

```python
import csv

msgs_df.to_csv('\<path>\<to>\<dir>\<filename>.csv',
               sep = "|",
               index = False,
               quoting = csv.QUOTE_ALL,
               encoding='utf-8'
               )

```


## Datetime Formatting

Make the datetime output pretty for printing

``` python
from datetime import datetime

datetime.now().strftime("%Y-%m-%d %H:%M:%S")

```


## Simple Multi Threading

A very simple examlpe of how multithreading can be implemented

Our required import.
```python
import concurrent.futures
```

How many threads to use
```Python
num_threads = 10
```

I believe this works across any iterable, eg a list, dataframe, etc
```python
sample_iteration_list = [1,2,3,4]
```

Lastly, set the threadpool to execute your function across your interator. The `executor.submit` order of inputs are:
1. The function to apply
2. The item you're iterating across
3. Any other (static) function inputs

```python
with concurrent.futures.ThreadPoolExecutor(max_workers = num_threads) as executor:
  
  run_transcriber = {
                    executor.submit(<fn name>, <item>, <var1>,...,<varN>): 
                                item for item in sample_iteration_list
                    }

```



## Basic Logging

Simple example of using the logging module:

```python
import logging

# Configure Logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "\path\to\filename.log"
                  , level = 'DEBUG'
                  , format = LOG_FORMAT
                  , filemode = 'w'
                  )
logger = logging.getLogger(__name__)

# Logger options in order of severity
logger.debug("My Debug")
logger.info("My Info")
logger.warning("My Warning")
logger.error("My Error")
logger.critical("My Critical")
```

* Log format options & reference: https://docs.python.org/2/library/logging.html#logrecord-attributes
* For info on filemodes, see: https://docs.python.org/3/library/functions.html#filemodes
* A good tutorial is: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/



## Database Saves

NOTE: Stolen from https://iabdb.me/2016/07/13/a-better-way-load-data-into-microsoft-sql-server-from-pandas/

This should work for any DB but has only been tested with SQL-Server.


```python
def df_to_sql(connection: pyodbc.Connection, df: pd.core.frame.DataFrame, data_base: str, table_name: str, table_schema: str = 'dbo', chunk_size: int = 1000):
    """Writes Dataframe to a DB
    This method should be significantly faster & easier to use than the pandas df.to_sql method
    In theory this works for both sqlalchemy & pyodbc but THIS HAS NOT BEEN TESTED

    NOTE: Stolen from https://iabdb.me/2016/07/13/a-better-way-load-data-into-microsoft-sql-server-from-pandas/
    
    Args:
        connection (pyodbc.Connection): DB connection object
        df (pd.core.frame.DataFrame): The dataframe to upload
        data_base (str): Database name to use
        table_name (str): Table name to store the data in
        table_schema (str, optional): Defaults to 'dbo'. The table schema to use
        chunk_size (int, optional): Defaults to 1000. The number of records to insert in each batch.
                                    Note, SQL Server limits batch inserts to 1000 records at a time
    """

    # Let the user know the batch size is too large. For now though, don't do anything about it
    if chunk_size > 1000:
        warnings.warn('Batch size exceeds that supported by MS SQL Server. The maximum allowable is 1000')

    # Core insert statement
    table_cols = ', '.join(df.columns)
    
    core_insert = "INSERT INTO {}.{}.{} ({}) VALUES ".format(data_base, table_schema, table_name, table_cols)

    # For each record, turn them into a tuple of stringsf for the insert
    # EG: ('colA','ColB','etc')
    records = [str(tuple(x)) for x in df.values]

    cursor = connection.cursor()

    # Iterate across each batch, inserting into the DB
    for batch in chunker(records, chunk_size):
        
        # Builds the full insert statement
        rows = ','.join(batch)
        insert_rows = core_insert + rows

        insert_rows = insert_rows.replace('nan','NULL')

        try:       
        # Send the data to the DB. Commit just in case autocommit = False in the DB connection
            cursor.execute(insert_rows)
            connection.commit()
        except Exception as ex:
            print(ex)

    print('Complete: {} records uploaded'.format(len(records)))
```

A secondary helper function is required, which splits the dataframe into chunks of size N, to be used in each batch upload.

```python
def chunker(seq: list, size: int):
    """Chunks a list into pieces where len(list) <= size

    Eg, seq = [1,2,3,4,5] & size = 2 would output:

        [1,2], [3,4], [5]

    NOTE: Stolen from https://stackoverflow.com/questions/434287/what-is-the-most-pythonic-way-to-iterate-over-a-list-in-chunks
    
    Args:
        seq (list): The item to be chunked
        size (int): The maximum length allowed for each chunk
    
    Returns:
        [generator]: A generator that outputs each chunk
    """

    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
```


## Pytest

Run from command line when the name isn't added:
```bash
python -m pytest
```

To run a specific test file:
```bash
python -m pytest <path>/<to>/<test_file>.py
```

Display pass/fail for each test, add the verbose flag:
```bash
python -m pytest -v

# OR

python -m pytest --verbose
```


## Flake8 Linting

Install flake8 & additional plugins:
```sh
flake8
flake8-docstrings
flake8-import-order
flake8-black
darglint
flake8-annotations
flake8-quotes
flake8-requirements
pep8-naming
```

Place the below in a `.flake8` file in the repo root: 

```sh
[flake8]
select=C,E,F,W,D,I,ANN,N,Q,DAR
docstring-convention=google
max-line-length = 100
format = ${cyan}%(path)s${reset} | r:${yellow_bold}%(row)d${reset}, c:${green_bold}%(col)d${reset} | ${red_bold}%(code)s${reset}: %(text)s
```

Where:
- `C`, `E`, `F` & `W` are defaults from `flake8`
- `D`: flake8-docstrings
- `I`: flake8-import-order & flake8-requirements
- `ANN`: flake8-annotations
- `N`: pep8-naming
- `Q`: flake8-quotes
- `DAR`: darglint
- `BLK`: flake8-black