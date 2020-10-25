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
items = sorted(items)

from itertools import combinations, permutations

def support(item):
    total_amount = 20.0
    count = 0
    for trans in transactions:
        if all(i in trans for i in item):
            count = count + 1
    result = count/total_amount
    return result

def confidence(item1, item2):
    result = support(item1+item2)/support(item2)
    return result

filename = input("filename:")
min_support= float(input("Min support (from 0 to 1):"))
min_confidence= float(input("Min confidence (from 0 to 1):"))

## import data

with open(filename, 'r', newline='') as f:  
    reader = f.read()
    transactions = eval(reader)


##compute support
condition = True
min_support_count={}
combin_num = 1

while condition == True:
    ##first step
    if combin_num == 1:
        for i in items:
            count = 0
            for trans in transactions:
                if i in trans:
                    count = count + 1
            if count > min_support*20:
                min_support_count[i] = count
        ##create new items set, ignore those count is less than the mini support
        items_more_than_support = []
        for key, value in min_support_count.items():
            items_more_than_support.append(key)
        items = items_more_than_support
        combin_num = combin_num + 1
    ##create combinations
    else:
        new_items = []
        combinations_result = []
        for pairs in combinations(items, combin_num):
            combinations_result.append([*pairs])
        combin_num = combin_num + 1
        for i in combinations_result:
            count = 0
            for trans in transactions:
                if all(item in trans for item in i):
                    count = count + 1
            if count > min_support*20:
                min_support_count[str(i)] = count
        if len(combinations_result)==1 or combin_num == 10:
            items = []
            for key, value in min_support_count.items():
                items.append(key)
            condition = False

## check support and confidence
result = []
for elements in items:
    if "[" in elements:
        result.append(eval(elements))
        

final_result = []
for a in result:
    b = [list(c) for i in range(len(a)) for c in combinations(a, i+1)]
    b.remove(a)
    new_list = []
    for i in range(int(len(b)/2)):
        new_list.append([b[i], b[-(i+1)]])

    for i in range(len(new_list)):
        new_list.append([new_list[i][1], new_list[i][0]])
    final_result = final_result + new_list

index_to_removed = []
for i in range(len(final_result)):
    if confidence(final_result[i][0], final_result[i][1]) < min_confidence:
        index_to_removed.append(i)

for i in index_to_removed:
    final_result.pop(i)

for i in range(len(final_result)):
    a = final_result[i][0]
    b = final_result[i][1]
    print(a, "->", b, "sup:", support(a+b), "conf:", confidence(a, b), "\n")