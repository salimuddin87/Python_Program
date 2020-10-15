# Json Handling
json_text = """
{
    "data": {
        "result": [
            {
                "metric": {
                    "instance": "10.25.49.126:9100"
                },
                "value": [
                    1572254615.345,
                    "28135.379999999997"
                ]
            },
            {
                "metric": {
                    "instance": "10.25.49.84:9100"
                },
                "value": [
                    1572254615.345,
                    "905380.95"
                ]
            },
            {
                "metric": {
                    "instance": "10.25.48.142:9100"
                },
                "value": [
                    1572254615.345,
                    "56273.9"
                ]
            },
            {
                "metric": {
                    "instance": "10.25.48.255:9100"
                },
                "value": [
                    1572254615.345,
                    "26225.219999999998"
                ]
            }
        ],
        "resultType": "vector"
    },
    "status": "success"
}
"""


import time
import json

# convert epoch time to gmtime
time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(1572258815.476))


unicode_type = json.loads(json.dumps(json_text))
dict_type = json.loads(json_text)
print(len(dict_type["data"]["result"]))
print(dict_type["data"]["result"][0]["metric"]["instance"].split(":")[0].strip())
print(dict_type["data"]["result"][0]["value"])
