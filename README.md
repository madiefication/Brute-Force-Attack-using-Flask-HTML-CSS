# Brute-Force-Attack-using-Flask-HTML-CSS
![brute-force-header](https://github.com/user-attachments/assets/879dda27-dd80-41a5-9929-76f1f1169e30)

---
This project demonstrates a simple brute-force attack simulation on a login system built using Python, HTML, CSS, and a password wordlist. It includes a web-based login interface and a Python script that attempts to brute-force the login credentials using a wordlist of passwords.

<img align="right" alt="img" width="300" src="https://cdn.dribbble.com/users/1026227/screenshots/2417386/hacker_final.gif">

### Project Overview
The main objective of this project is to simulate how brute-force attacks function and show the importance of securing login systems. The Python script (brute_force.py) automates login attempts by trying different passwords from a wordlist until the correct one is found. The project also contains a basic web interface where a user can input login details.

#### <ins> Note:</ins> This project is for educational purposes only. It is intended to demonstrate the risks of brute-force attacks in a controlled environment. Using such techniques on systems without explicit permission is illegal.

### Files:
- __app.py:__ Flask application that sets up a simple login system.
- __brute_force.py:__ Python script that performs the brute-force attack using a wordlist of passwords.
- __index.html:__ HTML form for user login.
- __styles.css:__ CSS for styling the login form.
- __passwords.txt:__ List of passwords to test during brute-force.

### Working:
- __Web Interface:__ A login page built using HTML and styled with CSS, where users can input their credentials.
- __Brute Force Script:__ The Python script (brute_force.py) takes the wordlist from passwords.txt and attempts to log in by sending POST requests to the Flask application (app.py).
- __Success Message:__ If the correct password is found, the brute force script stops and displays the correct password.

### Screenshots:
- The Login Page:
  
![LoginPage](https://github.com/user-attachments/assets/b3fe1de3-9976-4bb6-8033-32b6e512e8be)

- The result obtained by running brute force approach:

![Result](https://github.com/user-attachments/assets/23a3595f-27c3-4095-8d34-209975d49c2f)


### Security Considerations:
This project highlights how easy it can be to break into poorly secured systems. Use <ins>stronger passwords, rate limiting, CAPTCHA, and multi-factor authentication (MFA)</ins> to prevent such attacks.

### License:
This project is licensed under the MIT License.

