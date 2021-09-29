from django.shortcuts import render
from .frontend_data import all_bank_code, get_state, get_state, get_city, get_district, get_branch
from .get_data_logic import get_ifsc_code, get_data
import requests
# Create your views here.



def home(request):
          
    if request.POST:
        bank_id = request.POST.get('bank_code')
        state = request.POST.get('state').replace("+"," ")
        city = request.POST.get('city')
        dist = request.POST.get("district")
        branch = request.POST.get("branch").replace("+"," ")

        ifsc = get_ifsc_code(bank_id, state, city, dist, branch)
        url = f"https://ifsc.razorpay.com/{ifsc}"
        all_data = requests.get(url).json()
        print(all_data)
        context = {
        "flag"  :True,
        "branch" : all_data['BRANCH'],
        "center" : all_data['CENTRE'],
        "district" : all_data['DISTRICT'],
        "state" : all_data['STATE'],
        "address" : all_data['ADDRESS'],
        "contact" : all_data['CONTACT'],
        "city" : all_data['CITY'],
        "bank_name" : all_data['BANK'],
        "bank_code" : all_data['BANKCODE'],

        }
        return render(request, "finder/data_card.html", context)

      


    all_banks_data = all_bank_code()
    # print(all_banks_data)

    context = {
                "all_bank": all_banks_data,
                "states" : None,
                "cities" : None,
                "district": None,
                "branches": None,
                "data_to_print": all_banks_data,

                }
    return render(request, "finder/home.html", context)


def bank_detail(request):

    context = {}
    return render(request, "finder/bank_detail.html", context)

def load_state(request):
    
    bank_id = request.GET.get('bank_code')

    full_data = get_state(bank_id)
    # print(full_data)
    context = {
        "states":full_data,
        "data_to_print": full_data,
    }
    return render(request, 'finder/state.html', context)

def load_city(request):
    bank_id = request.GET.get('bank_code')
    state = request.GET.get('get_state')
    print(state, bank_id)
    data = get_city(bank_id, state)
    context = {
        "cities" : data,
        "data_to_print": data,
    }
    return render(request, "finder/city.html", context)

def load_dist(request):
    bank_id = request.GET.get('bank_code')
    state = request.GET.get('get_state')
    city = request.GET.get('get_city')
    data = get_district(bank_id, state, city)
    context = {
        "district":data,
        "data_to_print": data,
    }
    return render(request, "finder/district.html", context)


def load_branch(request):
    bank_id = request.GET.get('bank_code')
    state = request.GET.get('get_state')
    city = request.GET.get('get_city')
    dist = request.GET.get("get_dist")
    data = get_branch(bank_id, state, city, dist)
    context = {
        "branches":data,
        "data_to_print": data,
    }
    return render(request, "finder/branch.html", context)


def get_ifsc(request):
    context = {}
    if request.method == "POST":
        ifsc = request.POST.get("ifsc_code")
        url = f"https://ifsc.razorpay.com/{ifsc}"
        all_data = requests.get(url).json()
        
        if all_data == "Not Found":
            context["error"] = "Ifsc not found"
        else:    

            context = {
            "branch" : all_data['BRANCH'],
            "center" : all_data['CENTRE'],
            "district" : all_data['DISTRICT'],
            "state" : all_data['STATE'],
            "address" : all_data['ADDRESS'],
            "contact" : all_data['CONTACT'],
            "city" : all_data['CITY'],
            "bank_name" : all_data['BANK'],
            "bank_code" : all_data['BANKCODE'],

            }
            return render(request, "finder/data_card.html", context)
    return render(request, "finder/ifsc_temp.html",context)

def new(request):
    
    context = {}
    if request.POST:
        bank_id = request.POST.get('bank_code')
        state = request.POST.get('state').replace("+"," ")
        city = request.POST.get('city')
        dist = request.POST.get("district")
        branch = request.POST.get("branch").replace("+"," ")

        ifsc = get_ifsc_code(bank_id, state, city, dist, branch)
        url = f"https://ifsc.razorpay.com/{ifsc}"
        all_data = requests.get(url).json()
        print(all_data)
        context = {
    "flag"  :True,
    "branch" : all_data['BRANCH'],
    "center" : all_data['CENTRE'],
    "district" : all_data['DISTRICT'],
    "state" : all_data['STATE'],
    "address" : all_data['ADDRESS'],
    "contact" : all_data['CONTACT'],
    "city" : all_data['CITY'],
    "bank_name" : all_data['BANK'],
    "bank_code" : all_data['BANKCODE'],

    }
    return render(request, "finder/data_card.html", context)


# def new(request):
#     print(request.POST)



#     return render(request,'finder/new.html')

    