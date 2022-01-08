def gettime():
    import datetime
    return datetime.datetime.now()


date = gettime()


def log():
    print("choose your client to log")
    client = input("Press 1 for Adarsh, 2 for Himanshu and 3 for Manjan\n")

    if client == "1":
        choice = input("Press 1 to log diet and 2 for log exercise\n")

        if choice == "1":
            f = open("Adarsh diet.txt", "a")
            data = input("What has Adarsh eaten\n")
            f.write(str(date) + " " + data)
            f.close()
        if choice == "2":
            f = open("Adarsh exercise.txt", "a")
            data2 = input("What type of exercise has done by Adarsh\n")
            f.write(str(date) + " " + data2)
            f.close()

    if client == "2":
        choice = input("Press 1 to log diet and 2 for log exercise\n")

        if choice == "1":
            f = open("Himanshu diet.txt", "a")
            data3 = input("What has Himanshu eaten\n")
            f.write(str(date) + " " + data3)
            f.close()
        if choice == "2":
            f = open("Himanshu exercise.txt", "a")
            data4 = input("What type of exercise has done by Himanshu\n")
            f.write(str(date) + " " + data4)
            f.close()

    if client == "3":
        choice = input("Press 1 to log diet and 2 for log exercise\n")

        if choice == "1":
            f = open("Manjan diet.txt", "a")
            data5 = input("What has Manjan eaten\n")
            f.write(str(date) + " " + data5)
            f.close()
        if choice == "2":
            f = open("Manjan exercise.txt", "a")
            data6 = input("What type of exercise has done by Manjan\n")
            f.write(str(date) + " " + data6)
            f.close()


def retrieve():
    print("Choose your client")
    client = input(
        "Press 1 for Adarsh 2 for Himanshu and 3 for Manjan to retrive data\n")
    if client == "1":
        choice = input(
            "Press 1 to retrive log for Adarsh's diet and 2 for Adarsh's exercise\n")
        if choice == "1":
            f = open("Adarsh diet.txt")
            print(f.readlines())
            f.close()
        if choice == "2":
            f = open("Adarsh exercise.txt")
            print(f.readlines())
            f.close()

    if client == "2":
        choice = input(
            "Press 1 to retrive log for Himanshu's diet and 2 for Himanshu's exercise\n")
        if choice == "1":
            f = open("Himanshu diet.txt.txt")
            print(f.readlines())
            f.close()
        if choice == "2":
            f = open("Himanshu exercise.txt")
            print(f.readlines())
            f.close()

    if client == "3":
        choice = input(
            "Press 1 to retrive log for Manjan's diet and 2 for Manjan's exercise\n")
        if choice == "1":
            f = open("Manjan diet.txt")
            print(f.readlines())
            f.close()
        if choice == "2":
            f = open("Manjan exercise.txt")
            print(f.readlines())
            f.close()


print("Welcome to Health care Management System\n")
task = int(input("What do you want to do? \n1. Log \n2. Retrieve\n"))
if task == 1:
    log()
elif task == 2:
    retrieve()
else:
    print("Wrong Input. Please try again.")
