username = "postgres"
user_password = "new_password"



import psycopg2
from psycopg2 import sql


conn = psycopg2.connect(
    dbname="postgres",
    user=username,
    password=user_password,
    host="localhost"
)


conn.autocommit = True


cur = conn.cursor()


cur.execute("CREATE DATABASE countrydata;")


cur.close()


conn.close()
conn = psycopg2.connect(
    dbname="countrydata",
    user=username,
    password=user_password,
    host="localhost"
)
cur = conn.cursor()


conn.autocommit = True


cur.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(sql.Identifier("country_user")), ("password",))


cur.execute("GRANT ALL PRIVILEGES ON DATABASE countrydata TO country_user;")


cur.execute("ALTER DATABASE countrydata OWNER TO country_user;")

# Close cursor and connection
cur.close()
conn.close()
