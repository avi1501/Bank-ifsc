from .frontend_data import get_state, get_city, get_district, get_branch, get_ifsc
import requests
def get_ifsc_code(code,state=None, city=None, district=None, branch=None):
    
    ifsc_code = get_ifsc(code, state, city, district, branch)
    return ifsc_code

def get_data(ifsc_code):
    response = requests.get(f"https://ifsc.razorpay.com/{ifsc_code}")    
    data = response.json()
    return data






            
            

