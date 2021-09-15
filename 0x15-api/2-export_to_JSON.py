#!/usr/bin/python3
"""
uses a REST API to return inforamtion about an employee given their
employee ID
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

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

'''

    class User:
        def __init__(self, id, name):
            self.id = id
            self.name = name
            # self.completed = completed
            # self.total_task = total_task
            #self.title = title

        @classmethod
        def from_json(cls, json_items):
            q = json.loads(json_items)
            return cls(**q)

        def __repr__(self):
           return "{}\n{}".format(self.id, self.name)

            
    class Todo:
        def __init__(self, userId, title, completed):
            self.userId = userId
            self.title = title
            self.completed = completed

        @classmethod
        def from_json2(cls, json_items):
            q = json.loads(json_items)
            return cls(**q)

        def __repr__(self):
            return "{}\n{}".format(self.userId, self.title)

                
    if len(sys.argv) < 1:
        print("No result")
    else:

        arg_id = sys.argv[1]
        payload = {'id': arg_id }
        payload_todo = {'userId': id}
        try:
            todo_url = requests.get('https://jsonplaceholder.typicode.com/todos', params=payload_todo).json()
            users = requests.get('https://jsonplaceholder.typicode.com/users', params=payload).json()
        except:
            print("could not get or purse url")

        try:
            users_list = []
            todo_list = []

            try:
                user_data = json.loads(users)
                for u in user_data:
                    users_list.append(User(**u))
            except:
                print("could not append user obj")
                try:
                    todo_data = json.loads(todo_url)
                    for t in todo_url:
                        todo_list.append(Todo(**t))
                except:
                    print("could not append todo object")
        except:
            print("json loads did not work")
'''
