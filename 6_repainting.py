NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

qty_nylon = int(input())
qty_paint = int(input())
qty_thinner = int(input())
hours = int(input())

qty_nylon += 2
qty_paint += (qty_paint * 0.10)

sum_materials = ((qty_nylon * NYLON_PRICE)
                 + (qty_paint * PAINT_PRICE)
                 + (qty_thinner * THINNER_PRICE)
                 + BAGS_PRICE)

sum_workers = (sum_materials * 0.30) * hours
total_sum = sum_workers + sum_materials
print(total_sum)
