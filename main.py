# # * username, phone number, email, password any user need to login in!

# # * making database!

# # * list: always store multiple data!

# database = [{"email": "test@test.test",
#              "password": "test.test.test"}, {"email": "test2@test.test",
#             "password": "test2.test2.test2"}]  # ! this could be 1000 users!

users = {"test@test.test": "test.test.test"}

# # ? find somethun for me! find expect the whole value to be given! find can't achive our needs!

# # * get the user email or phone number and password!

email = input("Enter you email : ")
password = input("Enter you password : ")


def login():
    if len(password) < 8:
        print("Please make your paasword longer then 7 charaters!")
    for charater in password:
        if (charater == "." or charater == "?" or charater == "_"):
            print("this is special charater!")
        if (charater.isupper()):
            print("this is upper charater!")
    # # * users["test@test.test"] = test.test.test
    if (users[email] == password):
        print("Yes you logged in!")


login()

# # TODO: try to implement these!

# # * 1 - making password more strong! such as should be at least more then 8 character length! (Done!)
# # * 2 - make sure the password include special characters like for ex: (?, _, .)!
# # * 3 - most include capital charaters!
# # * 4 - the user can login useing username or email!

"""
123imherebutimnot!
yu : count how much charaters and see if they are upove 8!,
       in each character im gonna check if it have special chraters and one of them is capital!
"""
