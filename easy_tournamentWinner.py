"""
  There's an algorithms tournament taking place in which teams of programmers
  compete against each other to solve algorithmic problems as fast as possible.
  Teams compete in a round robin, where each team faces off against all other
  teams. Only two teams compete against each other at a time, and for each
  competition, one team is designated the home team, while the other team is the
  away team. In each competition there's always one winner and one loser; there
  are no ties. A team receives 3 points if it wins and 0 points if it loses. The
  winner of the tournament is the team that receives the most amount of points.

  
  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament. The input arrays are named
  `competitions` and `results`, respectively. The `competitions` array has elements
  in the form of [homeTeam, awayTeam], where each team is a string of at most 30
  characters representing the name of the team. The `results` array contains 
  information about the winner of each corresponding competition in the `competitions`
  array. Specifically, `results[i]`  denotes the winner of `competitions[i]` where a 1
  in the `results` array means that the home team in the corresponding competition
  won and a 0 means that the away team won.
  
  It's guaranteed that exactly one team will win the tournament and that each
  team will compete against all other teams exactly once. It's also guaranteed
  that the tournament will always have at least two teams.

  Sample Input:
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"],
    ]

    results = [0, 0, 1]

  Sample Output:
    "Python"
"""

# O(n) time | O(1) space
def tournamentWinner_1(competitions, results):

    scores = {}
    
    for i in range(0, len(results)):
        if results[i] == 1:
            # print("Winner {0}".format(competitions[i][0]))
            scores[competitions[i][0]] = scores.get(competitions[i][0],0) + 3
        else:
            # print("Winner {0}".format(competitions[i][1]))
            scores[competitions[i][1]] = scores.get(competitions[i][1],0) + 3
        # print(scores)

    highest_score = max(scores, key=scores.get)

    # print("Winner of Round Robin: {0}".format(highest_score))
    return highest_score


# O(n) time | O(1) space
HOME_TEAM_WON = 1
WINNING_POINTS = 3

def tournamentWinner_2(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winner = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winner, WINNING_POINTS, scores)
        if scores[winner] > scores[currentBestTeam]:
            currentBestTeam = winner

    return currentBestTeam

def updateScores(team, points, totals):
    if team not in totals:
        totals[team] = 0

    totals[team] += points



def main():
    sampleCompetitions = [
                            ["HTML", "C#"],
                            ["C#", "Python"],
                            ["Python", "HTML"],
                        ]
    sampleResults = [0,0,1]
    print(tournamentWinner_1(sampleCompetitions,sampleResults)) 
    print(tournamentWinner_2(sampleCompetitions,sampleResults)) 

if __name__ == "__main__":
    main()   