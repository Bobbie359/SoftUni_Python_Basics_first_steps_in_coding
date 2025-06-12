PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEG_MENU = 8.15
DELIVERY_PRICE = 2.50

number_chicken_menu = int(input())
number_price_fish_menu = int(input())
number_veg_menu = int(input())

sum_menus = ((number_chicken_menu * PRICE_CHICKEN_MENU)
             + (number_price_fish_menu * PRICE_FISH_MENU)
             + (number_veg_menu * PRICE_VEG_MENU))
desert_price = sum_menus * 0.20
total_sum = sum_menus + desert_price + DELIVERY_PRICE

print(total_sum)



