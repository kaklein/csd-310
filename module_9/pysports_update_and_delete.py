#Katie Klein
#CSD 310
#27 April 2021
#Assignment 9.3
#Pysports Update and Delete



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

def display_players(cursor):
    '''This method joins the player and team tables to select
    and display all current player information'''

    #execute inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #get query results
    players = cursor.fetchall()

    #loop through query results and display info for each player
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}\n")


#try/except block to execute program and handle potential errors
try:
    #connect to database
    db = mysql.connector.connect(**config)

    #create cursor object
    cursor = db.cursor()

    #INSERT player query
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")

    #display results after insert
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    display_players(cursor)

    #UPDATE player query
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #display results after update
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    display_players(cursor)

    #DELETE player query
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

    #display results after deletion
    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    display_players(cursor)

    #end of program
    input("\n\nPress any key to continue...")

#error handling for exceptions
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#close database connection
finally:
    db.close()
