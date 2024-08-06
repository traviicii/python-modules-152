# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship

def solution(scores):
    home = 0
    for game in scores:
        x, y = game.split(':')
        print('scores: ', x, y)
        if x > y:
            home += 3
        elif x == y:
            home += 1
    return home

# solution(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'])

some_string = "This:is:a:string:of:characters:but:when:I:split it each word becomes an item in a list"

print(some_string.split(':'))