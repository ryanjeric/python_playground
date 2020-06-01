"""
https://www.youtube.com/watch?v=9N6a-VLBa2I
JAVASCRIPT OBJECT NOTATION
JSON | PYTHON
-------------
object | dict
array | list
string | str
number(int) | int
number(real) | float
true | True
false | False
null | None
"""

import json

people_string = '''
{
    "people":[
        {
            "name":"John Smith",
            "phone":"615-555-7164",
            "emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name":"Jane Doe",
            "phone": "560-555-5153",
            "emails":null,
            "has_license":true
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))
print(type(data['people']))
for person in data['people']:
    print(person['name'])
    del person['phone']

# json.dumps = string
new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)

