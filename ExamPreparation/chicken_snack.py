from collections import deque

money_amount = list(map(int, input().split()))
food_prices = deque(map(int, input().split()))

food_eaten = 0

while money_amount and food_prices:
    money = money_amount.pop()
    price = food_prices.popleft()
    if money < price:
        continue
    elif money > price:
        if money_amount:
            money_amount[-1] += money - price
        else:
            money_amount.append(money - price)
    food_eaten += 1

if food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")
elif food_eaten < 4:
    print(f"Henry ate: {food_eaten} foods.")
else:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
