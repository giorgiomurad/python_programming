# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.6:  Write a program that asks the user to enter five test scores.
#               The program should display the letter grade for each score and
#               the average test score.
#               The program should define two functions:
#                       x calc_average:     This function accepts five test scores as arguments, and
#                                           the average.
#                       x determine_grade:  This function should accept a test score as an argument, and
#                                           returns the letter grade of the score.
#
#               The letter grade of a score is determined based on te following grading scale:
#                    Score   |   Letter Grade
#                   --------------------------
#                    90-100  |      A
#                    80-89   |      B
#                    70-79   |      C
#                    60-69   |      D
#                    Below 60|      F
#
#
# Author: Giorgio Murad Murad

# Function that returns the average of five test scores
def cal_average(t1, t2, t3, t4, t5):
    return (t1 + t2 + t3 + t4 + t5) / 5

# Function that returns the letter score according to the given score value
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'



# Prompting the user to enter five test scores
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
score4 = int(input("Enter score 4: "))
score5 = int(input("Enter score 5: "))

# Calling the function that returns the average of the scores
avg_score = cal_average(score1, score2, score3, score4, score5)

# Getting the letter grade of each test score
ltscore1 = determine_grade(score1)
ltscore2 = determine_grade(score2)
ltscore3 = determine_grade(score3)
ltscore4 = determine_grade(score4)
ltscore5 = determine_grade(score5)

print()

# Displaying the score average
print("The average score is:", avg_score)

# Displaying the five letter grades using a loop
for sc in [score1, score2, score3, score4, score5]:
    print("Score 1:", determine_grade(sc))