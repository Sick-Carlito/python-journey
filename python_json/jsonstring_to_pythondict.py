import json

# 🎯 JSON string
json_string = '{"course": "Python", "duration": "4 weeks"}'

# 🔁 Convert to Python dict
data = json.loads(json_string)
print(data["course"])  # Access like a dictionary

# 🔁 Convert Python dict to JSON string
new_json = json.dumps(data)
print(new_json)
