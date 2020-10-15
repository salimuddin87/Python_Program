# The JSON(Java Script Object Notation) format is commonly used by modern applications to allow for data
# exchange. Many programmers are already familiar with it, which makes it a good choice for interoperability.

import json
import io


json.dumps([1, 'simple', 'list'])  # '[1, "simple", "list"]'

# json exposes an API familiar to users of the standard library marshal and pickle modules.

# 1. Encoding basic Python object hierarchies:
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  # '["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))  # "\"foo\bar"
print(json.dumps(u'\u1234'))  # "\u1234"
print(json.dumps('\\'))  # "\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))  # {"a": 0, "b": 0, "c": 0}

io_str = io.StringIO()
json.dump(['streaming API'], io_str)
print(io_str.getvalue())  # '["streaming API"]'


# 2. Compact encoding
json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))  # '[1,2,3,{"4":5,"6":7}]'


# 3. Pretty printing
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': ')))
"""
Output:-
{
    "4": 5,
    "6": 7
}
"""


# 4. Decoding JSON
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')  # [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')  # u'"foo\x08ar'

io_str = io.StringIO('["streaming API"]')
json.load(io_str)  # [u'streaming API']
