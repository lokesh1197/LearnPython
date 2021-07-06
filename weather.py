from tkinter import Tk, Label, LabelFrame, Toplevel, Button
import requests
import json
from copy import deepcopy

root = Tk()
root.title("My weather app")

api_key = "82631f561c1a02428e1498e81a8b439c"

query_dict = {
        'q': 'soro',
        }
query = ""
for key in query_dict:
    query += key + "=" + query_dict[key] + "&"

query = query[:-1]

try:
    # api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?" + query +  "&appid=" + api_key)
    # api = json.loads(api_request.content)
    api = {
            'coord': {
                        'lon': 86.6858, 
                        'lat': 21.2881
                     }, 
            'weather': [
                        {'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}
                       ], 
            'base': 'stations', 
            'main': {
                        'temp': 306.14, 
                        'feels_like': 312.29, 
                        'temp_min': 306.14, 
                        'temp_max': 306.14, 
                        'pressure': 1002, 
                        'humidity': 59, 
                        'sea_level': 1002, 
                        'grnd_level': 1000
                    }, 
            'visibility': 10000, 
            'wind': {'speed': 3.35, 'deg': 236, 'gust': 5.9}, 
            'clouds': {'all': 100}, 
            'dt': 1624971039, 
            'sys': {'country': 'IN', 'sunrise': 1624923247, 'sunset': 1624971541}, 
            'timezone': 19800, 
            'id': 1255705, 
            'name': 'Soro', 
            'cod': 200
        }
except Exception as e:
    api = "Error: " + str(e)

def display_json(previous_window, obj):
    window = Toplevel(previous_window)
    print(obj)
    i = 0
    for key in obj:
        if isinstance(obj[key], dict):
            Button(window, text=key, command=lambda: display_json(window, deepcopy(obj[key]))).grid(row=i, column=0, columnspan=2, padx=10, pady=5)
            # new_frame = LabelFrame(frame)
            # new_frame.grid(row=i, column=1, padx=10, pady=5)
            # display_json(window, obj[key])
        elif isinstance(obj[key], list):
            new_obj = {}
            for i in range(len(obj[key])):
                new_obj[i] = obj[key][i]
            Button(window, text=key, command=lambda: display_json(window, deepcopy(new_obj))).grid(row=i, column=0, columnspan=2, padx=10, pady=5)
            # new_frame = LabelFrame(frame)
            # new_frame.grid(row=i, column=1, padx=10, pady=5)
            # display_json(new_frame, new_obj)
        else:
            Label(window, text=key).grid(row=i, column=0, padx=10, pady=5)
            Label(window, text=obj[key]).grid(row=i, column=1, padx=10, pady=5)
        i += 1
    exit_btn = Button(window, text="Exit")

display_json(root, deepcopy(api))

root.mainloop()
