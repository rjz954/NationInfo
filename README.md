# NationInfo
# Project Setup and Execution Guide

## Configuration
Before running the application, you need to configure your PostgreSQL credentials:
1. Open `init.py` with your preferred editing software.
2. At the top of the file, you will find the lines `username="postgres"` and `password="postgres"`.
3. Replace `"postgres"` with your PostgreSQL username and password respectively.

## Running the Application
To run the application, execute the following command in your terminal:

```bash
python run.py
```

If the above command does not work, you can run each script manually in the following order:
```bash
python csvmerger.py
python csvcountrylist.py
python series.py
python init.py
python load_data.py
python app.py
```
Finally, enter the site:

http://127.0.0.1:5000

You can now search for any country of your liking, using the drop down menu.

There are two drop down menus, one which displays countries which data is available, and one called "Series", which denotes the information contained within any particular row.

One can either select a country, a series, or both to get a search results, narrowing to down.

There are two variants of search, info and value.

Info search gives you the full 18 column table, though every row will have sections which are empty. We included this option in case the user wanted information not found within a value search, such as capital cities and major trading partners.

Value search gives only the year, series, value and source in results, and only includes rows which have all of these. It is far easier to extract information from, but there will be facts left out from this which could be found in the wider info search.
