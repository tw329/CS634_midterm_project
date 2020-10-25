import random

items = [
    "Everything_But_The_Bagel_Sesame_Seasoning_Blend", 
    "Mandarin_Orange_Chicken", 
    "Cauliflower_Gnocchi", 
    "Dark_Chocolate_Peanut_Butter_Cups", 
    "Plantain_Chips", 
    "Peanut_Butter_Filled_Pretzels", 
    "Non-Dairy_Oat_Beverages", 
    "Avocados", 
    "Unexpected_Cheddar",
    "Scented_Candles"
]

count = [19, 18, 17, 10, 7 ,8 ,2 ,4, 18, 6]
random.shuffle(count)

for i in range(0, 5, 1):
    transaction = []
    for j in range(0, 20, 1):
        transaction.append([])

    for m in range(len(items)):
        for n in random.sample(range(0, 20), k=count[m]):
            transaction[n].append(items[m])
            
    with open('dict_'+str(i)+'.txt', 'w', newline='') as f:  
        print(transaction, file=f)
