import requests
import json

def fetch_all_todo_list():
    # URL of the REST API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch all users
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()
    
    # Initialize dictionary to store tasks for all users
    all_tasks = {}
    
    # Iterate over each user
    for user in users_data:
        user_id = user['id']
        username = user['username']
        
        # Fetch user's TODO list
        todos_response = requests.get(f'{base_url}/todos?userId={user_id}')
        todos_data = todos_response.json()
        
        # Prepare tasks for the user
        user_tasks = [{"username": username, "task": todo['title'], "completed": todo['completed']} for todo in todos_data]
        
        # Add tasks to the dictionary
        all_tasks[str(user_id)] = user_tasks
    
    # Export data to JSON
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
    
    print(f'Data exported to {filename}')

if __name__ == "__main__":
    fetch_all_todo_list()
