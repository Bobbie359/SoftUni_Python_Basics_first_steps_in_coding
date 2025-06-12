annual_training_tax = int(input())

basketball_sneakers = annual_training_tax - (annual_training_tax * 0.40)
basketball_team = basketball_sneakers - (basketball_sneakers * 0.20)
basketball_ball = basketball_team * 0.25
basketball_accessories = basketball_ball * 0.20

total_sum = (annual_training_tax + basketball_sneakers
             + basketball_team + basketball_ball + basketball_accessories)

print(total_sum)