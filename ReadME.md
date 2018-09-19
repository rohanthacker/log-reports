# Log Reports

A simple SQL Database logging too, with minimal-code based config and text output, this tool provides arbitarty reports from an SQL Database, just update the settings and run.

----

## Prerequisites

* Python 3.6

----

## Getting Started

1. To get started clone this repo with

``` git clone git@github.com:rohanthacker/log-reports.git ```

2. Create a virtualenv with 

``` python -m venv <path to your venv> ```

3. Install required the python modules

``` pip install -r requirements.txt ```

4. You should now have a working copy of log-reports, to test run
``` ./main.py ```

If everything worked you should see output.txt ( default name ) in your current directory.

----

## Useage
Configure `settings.py`, the following options are available:

1. DB_CONN : The database connection string
2. FILENAME: The output filename
3. Report : Settings related to your report aka the output document.



### Report Configuration

The report variable in settings.py is a list of dicts that is explained below:

```
    {
        'title':  String    | The text-title to display above the SQL records found if any,
        'sql':    String    | The SQL query for this report 
        'format': Function  | A lambda function, the func is called with `row` as its first arg, 
                              this function will control your output
    }
 ```

#### Note: 
 If your SQL queries are long, it is suggested to put them in a seperate file and import the queries into settings.py, at the end of the day settings is just another python file.


 ----

## Authors

* **Rohan Thacker** - *Initial work* - [Rohan Thacker](https://github.com/rohanthacker)
