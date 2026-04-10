import requests

API_KEY = "a51baa00421697110fa79bd4843b19e7"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Florida", forecast_days=3))