<<<<<<< HEAD
from requests import Request, Session
import json
import csv
from datetime import datetime as dt


#used to store the name of the club being analyzed
team = input('What team are you analyzing?: ')
s = Session()
#memberData[] holds data about club members like user name, date joined, and activity
memberData = []
#compList[] is used to hold chess match data pulled from memberData[] where the 
#team that member was representing matches the team name being analyzed.
compList = []


#gets a list of all members of the team being analyzed
def getPlayerNames():
    url = 'https://api.chess.com/pub/club/{}/members'.format(team)
    response = s.get(url)

    response.raise_for_status()
    data = response.json()
    
    #loop through the json file and pull out required fields. 
    #append that data to memberData[]
    for tPeriod in data:
        for uname in data[tPeriod]:
            memberData.append({'Date Joined': uname['joined'],'active': tPeriod,
                         'username': uname['username']})

#takes memberData[] as an argument and uses the username to make a second API call
#that returns all the daily chess matches the member has played. Then checks each 
#chess game to determine of it was played as a member of the team name being
#analyzed. When a match is found, a counter is incremented
#and all assoceated data is appended to compList[].    
def findMatchPlay(team):
    i = 0
    team = team.lower()
    for tPeriod in memberData:
        member = tPeriod['username']
        url2 = 'https://api.chess.com/pub/player/{}/matches'.format(member)
        response = s.get(url2)
        response.raise_for_status()
        allGames = response.json()
        for status in allGames:
            for game in allGames[status]:
                #Grab the name of the club the member was playing for
                gString = ''.join(game['club'])
                if team in gString.lower():
                    i += 1 
            compList.append({'player': member,'Date Joined': tPeriod['Date Joined'],
                'active': tPeriod['active'],
                'status': status, 'matches': i})
            i = 0

def timeStamp():
    #Loop through compList[] and change the UNIX timestamp to a human
    # readable timestamp.
    for newTimestamp in compList:
        newTimestamp['Date Joined'] = dt.fromtimestamp(newTimestamp['Date Joined'])

def writeToCSV():
    #write the contense of compList[] to a csv file.       
    keys = compList[0].keys()
    with open('games_played.csv', 'w') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(compList)
    

def main():
    getPlayerNames()
    findMatchPlay(team)
    timeStamp()
    writeToCSV()

    s.close()

if __name__ == "__main__":
    main()

# eof
=======
from requests import Request, Session
import json
import csv
from datetime import datetime as dt


#used to store the name of the club being analyzed
team = input('What team are you analyzing?: ')
s = Session()
#memberData[] holds data about club members like user name, date joined, and activity
memberData = []
#compList[] is used to hold chess match data pulled from memberData[] where the 
#team that member was representing matches the team name being analyzed.
compList = []


#gets a list of all members of the team being analyzed
def getPlayerNames():
    url = 'https://api.chess.com/pub/club/{}/members'.format(team)
    response = s.get(url)

    response.raise_for_status()
    data = response.json()
    
    #loop through the json file and pull out required fields. 
    #append that data to memberData[]
    for tPeriod in data:
        for uname in data[tPeriod]:
            memberData.append({'Date Joined': uname['joined'],'active': tPeriod,
                         'username': uname['username']})

#takes memberData[] as an argument and uses the username to make a second API call
#that returns all the daily chess matches the member has played. Then checks each 
#chess game to determine of it was played as a member of the team name being
#analyzed. When a match is found, a counter is incremented
#and all assoceated data is appended to compList[].    
def findMatchPlay(team):
    i = 0
    team = team.lower()
    for tPeriod in memberData:
        member = tPeriod['username']
        url2 = 'https://api.chess.com/pub/player/{}/matches'.format(member)
        response = s.get(url2)
        response.raise_for_status()
        allGames = response.json()
        for status in allGames:
            for game in allGames[status]:
                #Grab the name of the club the member was playing for
                gString = ''.join(game['club'])
                if team in gString.lower():
                    i += 1 
            compList.append({'player': member,'Date Joined': tPeriod['Date Joined'],
                'active': tPeriod['active'],
                'status': status, 'matches': i})
            i = 0
    return(compList)

def timeStamp():
    #Loop through compList[] and change the UNIX timestamp to a human
    # readable timestamp.
    for newTimestamp in compList:
        newTimestamp['Date Joined'] = dt.fromtimestamp(newTimestamp['Date Joined'])
    return(compList)

def writeToCSV():
    #write the contense of compList[] to a csv file.       
    keys = compList[0].keys()
    with open('games_played.csv', 'w') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(compList)
    

def main():
    getPlayerNames()
    findMatchPlay(team)
    timeStamp()
    writeToCSV()

    s.close()

if __name__ == "__main__":
    main()

# eof
>>>>>>> 071b282c8602640f2ec6080b99b313c074c81447
