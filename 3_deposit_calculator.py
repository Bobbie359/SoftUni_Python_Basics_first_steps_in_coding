deposit_sum = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())

annual_interest_rate_persentage = annual_interest_rate / 100
sum = deposit_sum + deposit_months * ((deposit_sum * annual_interest_rate_persentage ) / 12)

print(sum)
