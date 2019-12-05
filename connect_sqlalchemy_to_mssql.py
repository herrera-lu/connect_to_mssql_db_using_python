# Install ms odbc drivers following instructions on:
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?redirectedfrom=MSDN&view=sql-server-ver15

# Info for connecting SQLAlchemy to mssql through pyodbc
# https://docs.sqlalchemy.org/en/13/dialects/mssql.html#dialect-mssql-pyodbc-connect

# Before pip installing pyodbc:
# sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
# sudo apt-get install unixodbc-dev
# On python 3.7:
# sudo apt-get install python3.7-dev

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from urllib.parse import quote_plus

# In linux, to get the driver name (after installing ms odbc driver for your distro):
# cat /etc/odbcinst.ini | grep '\[ODBC Driver'
params = quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                    # No quotes needed for parameter strings.
                    # Angled brackets and what's between them must be substituted with your values
                    "SERVER=<server>:<port>\\<instance>>;"
                    # If no instance is used and port is default:
                    # "SERVER=<server>;"
                    "DATABASE=<database>;"
                    "UID=<user>;"
                    "PWD=<password>;"
                    )

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
db = scoped_session(sessionmaker(bind=engine))


def main():

    rows = db.execute("SELECT field_1, field_2, field_3 FROM table_1").fetchall()
    for row in rows:
        print("field_1: {}, field_2: {}, field_3: {}".format(row.field_1, row.field_2, row.field_3))


if __name__ == "__main__":
    main()
