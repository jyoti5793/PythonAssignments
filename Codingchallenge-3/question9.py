passenger_list={'Ross' : 35,'Thomas': 42,'Rick' : 55,'Ericson' : 51, 'Josh' : 45,'Lara' : 50,'Emma' : 38, 'Lily' : 46,'Ron' : 41,'Michael' : 47,'Joanna' : 56,'Arthur' :42}
set={}
for key,value in passenger_list.items():
    if value >45:
        print(key)
