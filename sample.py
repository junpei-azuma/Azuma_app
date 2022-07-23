from datetime import datetime
import json


file = open("document/forecast.json", "r")


json_text = json.load(file)


# json_text["hourly"] : dictを要素に持つlist
# json_text["hourly"]の各要素(dict)からkeyがdtまたはpressureのitemのみを抽出して新しい要素として返す
new_list: list = [
    dict(
        filter(
            lambda element: element[0] == "dt" or element[0] == "pressure",
            element.items(),
        )
    )
    for element in json_text["hourly"]
]


hoge_list: list = [
    {
        "dt": datetime.fromtimestamp(element["dt"]).strftime("%Y%m%d%I%M"),
        "pressure": element["pressure"],
    }
    for element in new_list
]
print(hoge_list)
