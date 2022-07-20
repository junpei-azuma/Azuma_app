import requests

latitude = 34.693741
longitude = 135.502182
token = "94ddc164a4fcb492bee7658f350f47ed"
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&appid={token}&lang=ja&exclude=minutely,daily,current,alerts"
)
print(response.status_code)
