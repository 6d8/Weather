import requests
import json

inp = input("Enter the desired location: ")

osmResp = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&countrycodes=us&limit=5&q={inp}", timeout=8)
locations = json.loads(osmResp.text)

if len(locations) < 1:
	print("No matching locations found.")
	exit()

print("Select the best matching location: ")

for i in range(len(locations)):
	print("[", i, "] ", locations[i]["display_name"], sep = '')

sel = int(input("Selection number: "))
if (sel < 0) or(sel >= len(locations)):
	print("Invalid selection.")
	exit()

lat = locations[sel]["lat"]
lon = locations[sel]["lon"]

wthrResp = requests.get(f"https://api.weather.gov/points/{lat},{lon}", timeout=8)
weather = json.loads(wthrResp.text)
frcstResp = requests.get(weather["properties"]["forecast"], timeout=8)
forcast = json.loads(frcstResp.text)

print("\n\tSeven day forcast for ", inp, ".", sep = '')

for i in range(len(forcast["properties"]["periods"])):
	print("\n----", forcast["properties"]["periods"][i]["name"], "----")
	print(forcast["properties"]["periods"][i]["detailedForecast"])
