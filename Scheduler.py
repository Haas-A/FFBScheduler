import csv
import random

filename = 'NewFormat.csv'
file = open(filename, 'r')
data = csv.DictReader(file)

Teams = []
Rivals = []
WeekList = []

#tupleTest = [{"ham", "salami"}, {"cheese", "provo"}]
#print(tupleTest[0].__contains__("ham"))

def scheduleMatchups(Teams, League):
    matchups = []
    FreeTeams = Teams[0:len(Teams)]
    for team in League:
        if team[0] in FreeTeams:
            print("Opponent Search for " + str(team))
            print(FreeTeams)
            print(League)
            opponent = random.choice(team[2])
            while opponent not in FreeTeams:
                opponent = random.choice(team[2])
            matchups.append((team[0], opponent))
            FreeTeams.remove(team[0])
            FreeTeams.remove(opponent)
            team[2].remove(opponent)
            for opp in League:
                if opp[0] == opponent:
                    opp[2].remove(team[0])
    return matchups

def fillSchedule(Teams, League):
    for i in range(0,len(Teams)):
        League.append((Teams[i], Rivals[i], Teams[0:len(Teams)]))
        League[i][2].remove(Rivals[i])
        League[i][2].remove(Teams[i])
    return

def refillSchedule(Teams, League):
    for i in range(0, len(Teams)):
        League[i][2].append(Teams[0:len(Teams)])
        if League[i][2].__contains__(Rivals[i]):
            League[i][2].remove(Rivals[i])
        if League[i][2].__contains__(Teams[i]):
            League[i][2].remove(Teams[i])

for row in data:
    Teams.append(row['Teams'])
    Rivals.append(row['Rival'])
    WeekList.append(row['Weeks'])

WeeksLeft = int(WeekList[0])
#print(str(Rivals))
#print("Teams: " + str(Teams))
#print("Weeks Remaining: " + WeeksLeft)

#Now all of the teams and their rivals are stored
League = []
fillSchedule(Teams, League)
#print(League[0])

#Now there is a list with each team, its rival, and each of the teams it must have on their schedule.
Weeks = []

for q in range(1, WeeksLeft):
    if len(League[0][2]) == 0:
        refillSchedule(Teams, League)
    matchupsScheduled = scheduleMatchups(Teams, League)
    #Weeks.append("Week " + str(q) + str(matchupsScheduled))
    print("WEEK " + str(q) + str(matchupsScheduled))

print(Weeks)
#Schedule Rivalry Week





# 
# for each week
#   SCHEDULE ALL MATCHUPS AND RETURN LIST OF TUPLES OF TEAMS
#   add matchups to the weeks list
# 
# 
# SCHEDULE EACH MATCHUP
#   have list of free teams w/o matchup yet this week
# 
# 
# 
# 
# 
# 
# 

#print(Weeks)