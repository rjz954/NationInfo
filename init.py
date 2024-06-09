username = "postgres"
user_password = "new_password"



import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL server
conn = psycopg2.connect(
    dbname="postgres",
    user=username,
    password=user_password,
    host="localhost"
)

# Set autocommit mode
conn.autocommit = True

# Create a cursor object
cur = conn.cursor()

# Create database
cur.execute("CREATE DATABASE countrydata;")

# Close cursor
cur.close()

# Connect to the newly created database
conn.close()
conn = psycopg2.connect(
    dbname="countrydata",
    user=username,
    password=user_password,
    host="localhost"
)
cur = conn.cursor()

# Set autocommit mode
conn.autocommit = True

# Create user
cur.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(sql.Identifier("country_user")), ("password",))

# Grant privileges to the user on the database
cur.execute("GRANT ALL PRIVILEGES ON DATABASE countrydata TO country_user;")

# Set the owner of the database to country_user
cur.execute("ALTER DATABASE countrydata OWNER TO country_user;")

# Close cursor and connection
cur.close()
conn.close()
