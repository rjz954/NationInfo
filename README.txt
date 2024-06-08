How to run:
Go into init.py with your preffered editing software.
At the very top, it should say username="postgres" and password="postgres". Please change these to your postgres username and password respectively.

After that is done, run the following commands:
python csvmerger.py
python csvcountrylist.py
python init.py
python load_data.py
python app.py

Finally, enter the site:
http://127.0.0.1:5000

and search for any country of your liking.

There are two variants of search, info and value.

info search gives you the full 18 column table, though every row will have sections which are empty. We included this option in case the user wanted information not found within a value search.

value search gives only the year, series, value and source in results, and only includes rows which have all of these. It is far easier to extract information from, but there will be facts left out from this which could be found in the wider info search.