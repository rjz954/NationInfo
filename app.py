import os
import csv
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Determine the directory of the CSV file
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'dataset', 'Country_values.csv')

# Load country IDs and names from the CSV file into a dictionary
country_name_map = {}
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country_name_map[row['value']] = int(row['id'])

# Load unique series from the CSV file and sort alphabetically
unique_series = []
with open(os.path.join(base_dir, 'dataset', 'Unique_series.csv'), mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    unique_series = sorted([row[0] for row in reader])

@app.route('/')
def index():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        country_name = request.form['country_name']
        series = request.form['series']
        search_type = request.form.get('search_type', 'info')  # Default to 'info' if search_type is not provided
        # Get the ID corresponding to the entered country name
        country_id = country_name_map.get(country_name)
        # Query the database based on the selected search criteria
        conn = psycopg2.connect(dbname="countrydata", user="country_user", password="password", host="localhost", port="5432")
        cur = conn.cursor()
        if country_id is not None and series:  # Search by both country and series
            cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (country_id, series))
        elif country_id is not None:  # Search only by country
            cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL)", (country_id,))
        elif series:  # Search only by series
            cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (series,))
        else:  # No search criteria provided
            return render_template('search_form.html', countries=sorted(country_name_map.keys()), unique_series=unique_series)
        countries = cur.fetchall()
        conn.close()
        if search_type == 'value':
            # Sort by Series
            countries = sorted(countries, key=lambda x: x[1])
            return render_template('search_results_value.html', countries=countries)
        else:
            return render_template('search_results.html', countries=countries, search_type=search_type, unique_series=unique_series)
    return render_template('search_form.html', countries=sorted(country_name_map.keys()), unique_series=unique_series)

if __name__ == '__main__':
    app.run(debug=True)
