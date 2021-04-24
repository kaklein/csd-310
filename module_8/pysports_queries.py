#Katie Klein
#CSD 310
#24 April 2021
#Assignment 8.3
#Pysports Queries

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
    #connect to database
    db = mysql.connector.connect(**config)

    #create cursor
    cursor = db.cursor()

    #select query: team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #display team records using cursor
    teams = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print(f"Team ID: {team[0]}")
        print(f"Team Name: {team[1]}")
        print(f"Mascot: {team[2]}\n")

    #select query: player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    
    #display player records using cursor
    players = cursor.fetchall()
    print("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team ID: {player[3]}\n")

    #end of program
    input("\n\nPress any key to continue...")

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
