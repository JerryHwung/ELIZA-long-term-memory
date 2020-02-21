import json

# Create a new .json file and save data
def create_json(username, data):
    with open(username + ".json", "w") as write_file:
        json.dump(data, write_file)

# Read a .json file accroding to username
def read_json(username):
    try:
        with open(username + ".json", "r") as read_file:
            data = json.laod(read_file)

            return data
    except Exception as e:
        print(e)
        return []