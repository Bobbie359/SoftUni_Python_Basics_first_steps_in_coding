PRICE_PACKAGE_PENS = 5.80
PRICE_PACKAGE_MARKERS = 7.20
PRICE_CLEANING_PREP = 1.20

number_packages_pen = int(input())
number_packages_markers = int(input())
liters_cleaning_prep = int(input())
percent_discount = int(input()) / 100

sum_materials = ((number_packages_pen * PRICE_PACKAGE_PENS)
                 + (number_packages_markers * PRICE_PACKAGE_MARKERS)
                 + (liters_cleaning_prep * PRICE_CLEANING_PREP))

sum_materials -= (sum_materials * percent_discount)
print(sum_materials)