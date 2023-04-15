import csv
import random

filename = 'NewFormat.csv'
file = open(filename, 'r')
data = csv.DictReader(file)

teams = []
rivals = []
weeks_left = []
league = []
weeks = []

for row in data:
    teams.append(row['Teams'])
    rivals.append(row['Rival'])
    weeks_left.append(row['Weeks'])

weeks_left = weeks_left[0]


#populates the league object
#The league object should be a dict with key of team names
#the league value should be a list of objects, including:
#Team's schedule, the team's opponents they could potentially play next matchup, and the team's rival
def populate_league(league):
    for index in range(0,len(teams)):
        league.append((teams[index], rivals[index], teams[0:], []))
        league[index][2].remove(rivals[index])
        league[index][2].remove(teams[index])

populate_league(league)

def refill_opponents(league):
    print("refill opponents")

def schedule_seaason(league): 
    scheduled_teams = []
    for team in league:
        if team not in scheduled_teams:
            #schedule the team, otherwise do nothing
            print("")
            opponent = random.choice(team[2])
            



    return result

#League
#Should contain List of dicts with a team name as the key
#the value should be the teams schedule, the teams rival, the teams available next matchups
#Shold have these methods:
#populate league
#
# schedule season
#reset available next matchups
#