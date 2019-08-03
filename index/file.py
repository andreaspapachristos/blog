def write_user(username, email, password):
    file = open('users.txt', 'a')
    file.write(password + "\n")
    file.write(username + "\n")
    file.write(email + "\n")
    file.close()
