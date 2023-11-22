from user import User, information_to_list

print("""Enter users information in the given form
      "first_name, last name, age"
      ("Enter" to stop entering):\n""")
information = input("Enter user information: ")
while information:
    lst_information = [i.strip(',') for i in information.split()]
    user = User(*lst_information)

    if user.checking_file():
        print("The user is already on the list.")
    else:
        user.enter_to_file()

    information = input("Enter user information: ")

print(information_to_list('txt_files/information_about_all_users.txt'))
