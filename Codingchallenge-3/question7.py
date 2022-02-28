stock_market ={'AXIS BANK' : 7,'BHARTI AIRTEL' : 5,'COAL INDIA' : 10,'ITC' : 1,'TCS' : 3,'L&T' : 2,'RELIANCE' : 9,'KOTAK BANK' : 8, 'AMERICAN EXPRESS' : 11}
new_dict = {value:key for key,value in stock_market.items()}
sorted_values = sorted(new_dict)
maximum = max(sorted_values)
minimum = min(sorted_values)
list=[]
for i in sorted_values:
    if i == maximum:
        print((i,new_dict[i]))
    if i == minimum:
        print((i,new_dict[i]))

    list.append((i, new_dict[i]))

print(list)