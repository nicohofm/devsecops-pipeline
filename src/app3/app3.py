PASSWORD = "1234"


def check_password(input_password):
    if input_password == PASSWORD:
        return True
    else:
        return False


if __name__ == "__main__":
    user_password = input("Please enter your password: ")
    print(check_password(user_password))
