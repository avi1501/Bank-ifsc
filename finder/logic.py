def json_data(code):
    about = json.load(open(f"../by-bank/{code}.json",encoding="utf-8"))

    ifsc = about.keys()
    all_branch = about.values()


    states  = set()
    all_data = {}


    for obj in all_branch:
        states.add(obj['STATE'])
    states = list(states)

    for state in states:
        all_data[state] = {}

    city = set()

    for state in states:
        for obj in all_branch:
            if obj['STATE'] == state:
                city.add(obj['CITY'])
        cities = list(city)
        for city in cities:
            all_data[state][city] = {}
        city = set()



    district = set()

    flag = True
    for state in states:
        cities = all_data[state].keys()
        for city in cities:

            for obj in all_branch:
                if obj['STATE'] == state and obj['CITY']==city:
                    district.add(obj['DISTRICT'])
            district = list(district)
            for dist in district:
                all_data[state][city][dist] = {}
            district = set()

    branches = set()

    for state in states:
        cities = all_data[state].keys()

        for city in cities:

            district = all_data[state][city].keys()

            for dist in district:

                
                for obj in all_branch:
                    if obj['STATE'] == state and obj['CITY'] == city and obj['DISTRICT'] == dist:
                        branches.add(obj['BRANCH'])
                branches = list(branches)
                for branch in branches:
                    all_data[state][city][dist][branch] = obj["IFSC"]
                
                branches = set()
    return all_data
def final_data():
    all_data = json.load(open(f'../bank-data.json', encoding="utf-8"))
    bank_name = {}
    result = {}
    for data,code in all_data.items():
        # print(data,code)
        bank_name[data] = code
        # get_all("IBKL")
        result[data] = json_data(code)
    return result
     

all_data = final_data()
