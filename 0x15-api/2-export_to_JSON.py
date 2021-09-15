#!/usr/bin/python3
"""
uses a REST API to return inforamtion about an employee given their
employee ID
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)

''''
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    #completed = [t.get("title") for t in todos if t.get("completed") is True]
    #print("Employee {} is done with tasks({}/{}):".format(
     #   user.get("name"), len(completed), len(todos)))
    #[print("\t {}".format(c)) for c in completed]

    u_id = user.get('id')
    title = [t.get('title') for t in todo]
    completed = todo.get('completed')
    name = user.get('name')

    content = {u_id: [{"task": title, "completed": completed, "username": name}]}
    json_file = str(sys.argv[1]) + ".json"
    with open(json_file, "w") as f:
        if content:
            f.write(str(content))
        else:
            print("content is empty")
'''