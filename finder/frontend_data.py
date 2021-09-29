import json
from django.conf import settings


def get_state(code):
    about = json.load(open(f"{settings.BASE_DIR}/data_with_code.json",encoding="utf-8"))
    all_data = about[code].keys()
    return list(all_data)

def get_city(code, state):
    about = json.load(open(f"{settings.BASE_DIR}/data_with_code.json",encoding="utf-8"))
    all_data = about[code][state].keys()
    return list(all_data)

def get_district(code, state, city):
    about = json.load(open(f"{settings.BASE_DIR}/data_with_code.json",encoding="utf-8"))
    all_data = about[code][state][city]
    return list(all_data)


def get_branch(code, state, city, district):
    about = json.load(open(f"{settings.BASE_DIR}/data_with_code.json",encoding="utf-8"))
    all_data = about[code][state][city][district].keys()
    return list(all_data)


def get_ifsc(code, state, city, district, branch):
    about = json.load(open(f"{settings.BASE_DIR}/data_with_code.json",encoding="utf-8"))
    all_data = about[code][state][city][district][branch]
    # print(all_data)
    return(all_data)



def all_bank_code():
    all_data = json.load(open(f'{settings.BASE_DIR}/bank-data.json', encoding="utf-8"))
    bank_name = {}
    result = {}
    for data,code in all_data.items():
        # print(data,code)
        bank_name[data] = code
        # get_all("IBKL")
        result[data] = code
    return result
     



 
