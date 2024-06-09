import os
import csv
import re
from flask import Flask, render_template, request, redirect, url_for
import psycopg2


app = Flask(__name__)


base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'dataset', 'Country_values.csv')


country_name_map = {}
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country_name = re.sub(r'[^a-zA-Z()\[\] ]', '', row['value'])
        country_name_map[country_name] = int(row['id'])


unique_series = []
with open(os.path.join(base_dir, 'dataset', 'Unique_series.csv'), mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    unique_series = sorted([row[0] for row in reader])


@app.route('/')
def index():
    return redirect(url_for('search'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        country_name = request.form['country_name']
        series = request.form['series']
        search_type = request.form.get('search_type', 'info')
        country_id = country_name_map.get(country_name)
        if search_type == 'value':
            return search_by_value(country_id, series)
        else:
            return search_by_info(country_id, series)
    return render_template('search_form.html', countries=sorted(country_name_map.keys()), unique_series=unique_series)


def search_by_value(country_id, series):
    conn = psycopg2.connect(dbname="countrydata", user="country_user", password="password", host="localhost", port="5432")
    cur = conn.cursor()
    if country_id is not None and series:
        cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (country_id, series))
    elif country_id is not None:
        cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL)", (country_id,))
    elif series:
        cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (series,))
    else:
        cur.execute("SELECT unnamed_1, year, series, value, source FROM Countries WHERE (value IS NOT NULL OR unnamed_1 IS NOT NULL)")
    countries = cur.fetchall()
    conn.close()
    return render_template('search_results_value.html', countries=countries)


def search_by_info(country_id, series):
    conn = psycopg2.connect(dbname="countrydata", user="country_user", password="password", host="localhost", port="5432")
    cur = conn.cursor()
    if country_id is not None and series:
        cur.execute("SELECT * FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (country_id, series))
    elif country_id is not None:
        cur.execute("SELECT * FROM Countries WHERE id = %s AND (value IS NOT NULL OR unnamed_1 IS NOT NULL)", (country_id,))
    elif series:
        cur.execute("SELECT * FROM Countries WHERE (value IS NOT NULL OR unnamed_1 IS NOT NULL) AND series = %s", (series,))
    else:
        cur.execute("SELECT * FROM Countries WHERE (value IS NOT NULL OR unnamed_1 IS NOT NULL)")
    countries = cur.fetchall()
    conn.close()
    return render_template('search_results_info.html', countries=countries)


if __name__ == '__main__':
    app.run(debug=True)
