# Json Handling
import json

jsonText = """
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

# convert epoch time to gmtime
time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(1572258815.476)


unicodeType = json.loads(json.dumps(jsonText))
dictType = json.loads(jsonText)
print len(dictType["data"]["result"])
print dictType["data"]["result"][0]["metric"]["instance"].split(":")[0].strip()
print dictType["data"]["result"][0]["value"]