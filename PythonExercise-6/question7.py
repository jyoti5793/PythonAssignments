map_details = {101:'Park', 102:'Zoo', 103:'Mall'}

def find_mall(map_details):
    for key, value in map_details.items():
        if value == 'Mall':
            print(key)
find_mall(map_details)