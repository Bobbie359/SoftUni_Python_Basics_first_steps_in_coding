pages = int(input())
pages_per_hours = int(input())
days = int(input())

hours_needed = pages // pages_per_hours
hours_per_day_needed = hours_needed // days

print(hours_per_day_needed)