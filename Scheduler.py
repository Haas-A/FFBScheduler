
divisions = input("Enter the number of divisions: ")
Teams = []
for i in range(0,int(divisions)):
    TeamList = input("Enter the team names in division " + str(i) + " separated by commas:").split(',')
    for j in range(0, len(TeamList)):
        Teams.append((TeamList[j], i))

print(Teams)