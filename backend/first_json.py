import json

site_name = "tech-stack"

def make_data():
    data = {"message": "hello, world", "from": site_name}
    return json.dumps(data)
print(make_data())