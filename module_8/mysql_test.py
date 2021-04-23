#Katie Klein
#CSD 310
#23 April 2021
#Assignment 8.2
#Python Connector Test

#import statements
import mysql.connector
from mysql.connector import errorcode

#database configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#try/except block to handle potential errors
try:
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#close connection
finally:
    db.close()
