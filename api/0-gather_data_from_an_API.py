#!/usr/bin/python3
""" returns to-do list information about employee ID """
from requests import get
from sys import argv

if __name__ == '__main__':
    APIurl = "https://jsonplaceholder.typicode.com"
    employee = get(APIurl + "/users/{}".format(argv[1])).json()
    to_do_list = get(APIurl + "/todos", params={
        "userId": argv[1]}).json()

    finished = [i.get("title") for i in to_do_list if i.get(
        "completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(employee.get(
        "name"), len(finished), len(to_do_list)))
    [print("\t {}".format(c)) for c in finished]
