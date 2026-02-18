#task 1
import random

sample_space = [['Click', 'Click'],
['Click', 'Scroll'],
['Click', 'Exit'],
['Scroll', 'Click'],
['Scroll', 'Scroll'],
['Scroll', 'Exit'],
['Exit', 'Click'],
['Exit', 'Scroll'],
['Exit', 'Exit']]
print("\nTotal Outcomes in Sample Space:", len(sample_space))
event_E = [['Click', 'Click'],['Click', 'Scroll'],['Click', 'Exit'],['Scroll', 'Click'],['Exit', 'Click']]

print("\nEvent E (At Least One Click):", len(event_E))
probability_E = len(event_E) / len(sample_space)
print("\nProbability of At Least One Click:", round(probability_E, 4))
print("-"*50)

trials = 1000
count_sum_7 = 0

for _ in range(trials): 
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    if d1 + d2 == 7:
        count_sum_7 += 1
        
exp = count_sum_7/trials
print("Probability =",exp)


#task 2

P_heads = 1 / 2
P_six = 1 / 6
P_independent = P_heads * P_six
print("Theoretical Probability (Heads AND 6):", round(P_independent, 4))

P_first_red = 5 / 10
P_second_red_given_first = 4 / 9
P_dependent = P_first_red * P_second_red_given_first
print("Theoretical Probability (Both Red):", round(P_dependent, 4))

#task 3

P_spam = 0.1
P_ham = 0.9
P_free_given_spam = 0.9
P_free_given_ham = 0.05
P_free = (P_free_given_spam * P_spam)+(P_free_given_ham * P_ham)
P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print("P(Free) =", round(P_free, 4))
print("P(Spam | Free) =", round(P_spam_given_free, 4))
         