import os
import csv
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import difflib

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

@app.route('/')
def index():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        country_name = request.form['country_name']
        search_type = request.form.get('search_type', 'info')  # Default to 'info' if search_type is not provided
        # Get the ID corresponding to the entered country name
        country_id = country_name_map.get(country_name)
        if country_id is not None:
            # Query the database for rows with the obtained ID
            conn = psycopg2.connect(dbname="countrydata", user="country_user", password="password", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Countries WHERE id = %s", (country_id,))
            countries = cur.fetchall()
            conn.close()
            if search_type == 'value':
                # Filter out rows where Value is NaN
                countries = [country for country in countries if country[6] is not None]
                # Extract only Year, Series, Value, and Source for display
                countries = sorted([(country[2], country[3], country[6], country[8]) for country in countries], key=lambda x: x[1])  # Sort by Series
                return render_template('search_results_value.html', countries=countries)
            else:
                return render_template('search_results.html', countries=countries, search_type=search_type)
        else:
            # Find the closest matching country name
            closest_match = difflib.get_close_matches(country_name, country_name_map.keys(), n=1)
            if closest_match:
                suggestion = closest_match[0]
                return render_template('search_results.html', countries=[], message=f"Did you mean '{suggestion}'?", suggestion=suggestion, search_type=search_type)
            else:
                return render_template('search_results.html', countries=[], message="Country not found.", search_type=search_type)
    return render_template('search_form.html')

if __name__ == '__main__':
    app.run(debug=True)
