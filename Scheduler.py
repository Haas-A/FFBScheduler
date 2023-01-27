import csv

filename = 'NewFormat.csv'
file = open(filename, 'r')
data = csv.DictReader(file)

Teams = []
Rivals = []
WeekList = []

for row in data:
    Teams.append(row['Teams'])
    Rivals.append(row['Rival'])
    WeekList.append(row['Weeks'])

WeeksLeft = WeekList[0]
#print(str(Rivals))
#print("Teams: " + str(Teams))
#print("Weeks Remaining: " + WeeksLeft)

#Now all of the teams and their rivals are stored
League = []

for i in range(0,len(Teams)):
    currentTeam = Teams[i]
    val = Teams.remove(currentTeam)
    League.append((currentTeam, Rivals[i], Teams[0:len(Teams)]))
    Teams.insert(i, currentTeam)

print(League[1])

#Now there is a list with each team, its rival, and each of the teams it must have on their schedule.