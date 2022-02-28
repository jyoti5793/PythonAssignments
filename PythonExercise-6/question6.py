candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]

def sort_height(candidate_details):
    #d = dict(candidate_details)
    d = {}
    for i in candidate_details:
        d.update({i[1]:i[0]})
    for i in sorted(d):
        print([(d[i],i)],end = " ")

sort_height(candidate_details)