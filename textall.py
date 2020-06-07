# Python Script to Automate text to a large number of friends on Facebook
import fbchat
from getpass import getpass

pos = 0
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
friends = client.fetchAllUsers()
msg = str(input("Message: ")
for i in range(len(friends)):
    try:
        friend = friends[pos]
        sent = client.sendMessage(msg, thread_id=friend.uid)
        if sent:
            print("Message sent successfully!")
        else:
            print("Something went wrong")
        pos = pos + 1
    except TypeError:
        print("Encountered issue")

print(" All Messages sent successfully!")


# Use this lines of code if you want to do this manually.
# no_of_friends = int(input("Number of friends: "))

# for i in range(no_of_friends):
#     name = str(input("Name: "))
#     friends = client.searchForUsers(name)  # return a list of names
#     print(friends)
#     friend = friends[0]
#     print(friend, "User id:", friend.uid)
#     msg = str(input("Message: "))
#     sent = client.sendMessage(msg, thread_id=friend.uid)
#     if sent:
#         print("Message sent successfully!")