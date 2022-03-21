# Importing data from a flat file.

- Save the file as import_excel.csv and place it in the python package root. This is the folder with manage.py.
	- Note that python is very particular about character encoding. It is currently locked to latin-1 (UTF-8) in the code.
- Browse to /import_data_from_excel. The page will load for a few minutes as the server processes the data and then will redirect you to /admin on a succesful import or to the front page if something went wrong.
	- In the latter case it may be helpful to remove the try/except in front/views.py. This will enable the page to display django error messages instead of redirecting.