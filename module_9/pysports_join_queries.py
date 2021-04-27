#Katie Klein
#CSD 310
#27 April 2021
#Assignment 9.2
#Pysports Basic Table Joins



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

#try/except block to execute program and handle potential errors
try:
    #connect to database
    db = mysql.connector.connect(**config)

    #create cursor object
    cursor = db.cursor()

    #inner join player and team tables on team_id
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #store query results
    players = cursor.fetchall()

    #loop over and display results
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}\n")

    #end of program
    input("\n\nPress any key to continue...")

#error handling for exceptions
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#close database connection
finally:
    db.close()
