#Classes and Functions
class Player:
    def __init__(self, name, rating, ID):
        self.ID = ID
        self.name = name
        self.rating = rating
        self.membersPlayed = []
        self.lastColor = 0
        self.score = 0

def toBracket(members):
    
    # Setup Vars
    bracket = []
    matchup = []
    bye = None
    
    while len(members) > 1:# Stop when list is empty
        # Add first element in list
        matchup.append(members[0])
        # Track size to see if no change
        sizeBefore = len(members)
        for i, value in enumerate(members[1:]):
            if value not in matchup[0].membersPlayed: # if not played before
                matchup.append(value)# add as second player in matchup
                members = members[1:i+1] + members[i+2:]# remove both players from list
                break
        if sizeBefore == len(members):# If no change, reset matchup var and break out
            matchup = []
            break
        # Prefer different color
        if matchup[1].lastColor == 1:
            temp = matchup[0]
            matchup[0] = matchup[1]
            matchup[1] = temp
        bracket.append(matchup)# Add Matchup to bracket
        # Save Date to Objects
        matchup[0].lastColor = 0
        matchup[0].membersPlayed.append(matchup[1])
        matchup[1].lastColor = 1
        matchup[1].membersPlayed.append(matchup[0])
        # Reset Matchup
        matchup = []
    # Create regular matchups out of remaining members if any
    for i, value in enumerate(members):
        matchup.append(value)

        if i % 2 == 1:
            # Swap if black was black last round
            if value.lastColor == 1:
                temp = matchup[0]
                matchup[0] = matchup[1]
                matchup[1] = temp
            # Add matchup to bracket
            bracket.append(matchup)
            matchup[0].membersPlayed.append(matchup[1])
            matchup[1].membersPlayed.append(matchup[0])
            value.lastColor = 1
            matchup = []
            continue
        value.lastColor = 0
    if len(members) % 2 == 1:#Add bye if applicable
        bye = members[-1]
    return bracket, bye

# TESTING VARS to avoid input
names = ['tyler', 'lemon', 'morgan', 'justin', 'michael', 'jack', 'erik', 'darren', 'eesan', 'spencer', 'byeguy']
ratings = ['1843', '1400', '1400', '1250', '1200', '1200', '1000', '1000', '700', '100', '50']
def objInfo(obj):
    return ('[name: ' + obj.name + '][score: ' + str(obj.score) + ']')

# Option to enter members/ratings through input
"""
names = []
print("Enter members:")
stdin = input()
while (stdin != 'd'):
    names.append(stdin)
    stdin = input()

ratings = []
print("Enter ratings:")
stdin = input()
while (stdin != 'd'):
    ratings.append(stdin)
    stdin = input()
"""
# Create list of all tournament members out of names and ratings
members = []
for i, value in enumerate(names):
    members.append(Player(names[i], ratings[i], i))
# Delete unnecessary vars
del names, ratings

roundNum = 1 # Track round number
while True:
    # Sort by score
    members.sort(key=lambda x: x.score, reverse=True)

    # Create bracket for round
    bracket, bye = toBracket(members)

    # Display Matchups
    print("__Round " + str(roundNum) + "__")
    for i in bracket:
        print(i[0].name + " vs " + i[1].name)
    if bye != None:
        print("BYE: " + bye.name)
        bye.score += 1

    # Get Scores
    print("Enter Who Won Each Game. (0 for white, 1 for black, 2 for draw)")
    for i in bracket:
        result = int(input())
        if result == 0:
            i[0].score += 1
        elif result == 1:
            i[1].score += 1
        elif result == 2:
            for j, value in enumerate(i):     
                i[j].score += 0.5
    roundNum += 1
