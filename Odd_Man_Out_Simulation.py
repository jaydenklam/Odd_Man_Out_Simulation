from random import randrange

total_trials = 1000000
all_different = 0
all_same = 0
odd_man_out = 0

for i in range(total_trials):
    player_1 = randrange(1, 4)
    player_2 = randrange(1, 4)
    player_3 = randrange(1, 4)
    
    if (player_1 != player_2 and player_1 != player_3 and player_2 != player_3):
        all_different = all_different + 1
    elif (player_1 == player_2 and player_1 == player_3 and player_2 == player_3):
        all_same = all_same + 1
    else:
        odd_man_out = odd_man_out + 1

percent_different = round((all_different/total_trials) * 100, 2)
percent_same = round((all_same/total_trials) * 100, 2)
percent_odd = round((odd_man_out/total_trials) * 100, 2)

print ("Simulating", total_trials, "trials of odd man out:")
print ("Total times all symbols are different:", all_different, "or", percent_different, "%")
print ("Total times all symbols are the same:", all_same, "or", percent_same, "%")
print ("Total times there is an odd man out:", odd_man_out, "or", percent_odd, "%")