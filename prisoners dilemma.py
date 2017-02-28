#
# Test file for prisoners dilemma repeated
#
#
#
import random

def allD(history, time):
    return 'D'

def allC(history, time):
    return 'C'

def titForTat(history, time):
    if (time == 0):
        return 'C'
    else: return history[time-1]

def suspiciousTitForTat(history, time):
    if (time == 0):
        return 'D'
    else: return history[time-1]

def randomS(history, time):
    if (random.random() < 0.5):
        return 'C'
    return 'D'

def game(s1, s2, time, utilities):
    outcome = []
    outcome1 = []
    outcome2 = []
    u1, u2 = 0, 0
    for t in range(0, time):
        #outcome.append((s1(outcome, t) , s2(outcome, t)))
        outcome1.append((s1(outcome2, t)))
        outcome2.append((s2(outcome1, t)))
        u1 += utilities[outcome1[t], outcome2[t]][0]
        u2 += utilities[outcome1[t], outcome2[t]][1]
    return outcome1, outcome2, u1, u2


timer = 10

utilities = {('C','C'): (9, 9), ('C','D'): (0, 10), ('D','C'): (10, 0), ('D','D'): (1, 1)}

# test1, test2 = game(player1, player2, timer, utilities)
# print('Test1: ' + str(test1))
# print('Test2: ' + str(test2))
row1, row2, u1, u2 = game(randomS, titForTat, timer, utilities)
print(row1)
print(row2)
print(u1)
print(u2)
# print(type(game(allD, allC, timer, utilities)))
# print(type(game(allD, allC, timer, utilities)[0]))