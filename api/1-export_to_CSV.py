#!/usr/bin/python3
""" returns to-do list information about employee ID """
import csv
from requests import get
from sys import argv

if __name__ == '__main__':
    APIurl = "https://jsonplaceholder.typicode.com"
    employee = get(APIurl + "/users/{}".format(argv[1])).json()
    to_do_list = get(APIurl + "/todos", params={
        "userId": argv[1]}).json()
    username = employee.get("username")

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writeCSV = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writeCSV.writerow([argv[1], username, i.get("completed"),
                            i.get("title")]) for i in to_do_list]
