# Install ms odbc drivers following instructions on:
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?redirectedfrom=MSDN&view=sql-server-ver15
import pyodbc

# In linux, to get the driver name (after installing ms odbc driver for your distro):
# cat /etc/odbcinst.ini | grep '\[ODBC Driver'
conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      # No quotes needed for parameter strings.
                      # Angled brackets and what's between them must be substituted with your values
                      "SERVER=<server>:<port>\\<instance>>;"
                      # If no instance is used and port is default:
                      # "SERVER=<server>;"
                      "DATABASE=<database>;"
                      "UID=<user>;"
                      "PWD=<password>;"
                      )

cursor = conn.cursor()


def main():
    cursor.execute("SELECT field_1, field_2, field_3 FROM table_1")
    for row in cursor:
        print("field_1: {}, field_2: {}, field_3: {}".format(row.field_1, row.field_2, row.field_3))


if __name__ == "__main__":
    main()
