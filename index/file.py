import datetime


def write_user(username, email, password):
    file = open('users.txt', 'a')
    file.write(datetime.datetime.now().strftime("%H:%M:%S - %b %d %Y") + "\n")
    file.write(password + "\n")
    file.write(username + "\n")
    file.write(email + "\n")
    file.write("\n")
    file.close()

