from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def tracker(requests):
    data = urllib.request.urlopen('https://api.covid19india.org/v4/data.json')
    data1 = data.read().decode()
    data_dict = json.loads(data1)

    class Put():

        def __init__(self, state , confirmed, recovered, deceased, tested):
            self.recovered = recovered
            self.deceased = deceased
            self.tested = tested
            self.state = state
            self.confirmed = confirmed

    states_dict = {
    			"AN": "Andaman and Nicobar",
    			"AP": "Andhra Pradesh",
    			"AR": "Arunachal Pradesh",
    			"AS": "Assam",
    			"BR": "Bihar",
    			"CH": "Chandigarh",
    			"CT": "Chhattishgarh",
    			"DL": "Delhi",
    			"DN": "Dadra and Nagar Haveli and Daman and Diu",
    			"GA": "Goa",
    			"GJ": "Gujarat",
    			"HP": "Himachal Pradesh",
    			"HR": "Haryana",
    			"JH": "Jharkhand",
    			"JK": "Jammu and Kashmir",
    			"KA": "Karnataka",
    			"KL": "Kerala",
    			"LA": "Ladakh",
    			"MH": "Maharashtra",
    			"ML": "Meghalaya",
    			"MN": "Manipur",
    			"MP": "Madhya Pradesh",
    			"MZ": "Mozoram",
    			"NL": "Nagaland",
    			"OR": "Odisha",
    			"PB": "Punjab",
    			"PY": "Puducherry",
    			"RJ": "Rajasthan",
    			"SK": "Sikkim",
    			"TG": "Telangana",
    			"TN": "Tamil Nadu",
    			"TR": "Tripura",
    			"UP": "Uttar Pradesh",
    			"UT": "Uttarakhand",
    			"WB": "West Bengal"}

    states_id = []

    for i in states_dict:
        t_confirmed = data_dict["TT"]["total"]["confirmed"]
        t_recovered = data_dict["TT"]["total"]["recovered"]
        t_deceased = data_dict["TT"]["total"]["deceased"]
        try:
            states_id.append(Put(states_dict[i], data_dict[i]["total"]["confirmed"], data_dict[i]["total"]["recovered"],  data_dict[i]["total"]["deceased"], data_dict[i]["total"]["tested"]))
        except:
            states_id.append(Put(states_dict[i], data_dict[i]["total"]["confirmed"], data_dict[i]["total"]["recovered"],  0, data_dict[i]["total"]["tested"]))


    return render(requests, "covid_india_app/index.html", {"states_id":states_id, "t_confirmed":t_confirmed, "t_recovered":t_recovered, "t_deceased":t_deceased})
