from new_game import start_game
from results import history_game
from players import register_user, check_login, username_exists, validate_username, validate_password

QUIT_KEY = "q"

def ask_until_valid(prompt, validator):
    """
    سوال را می‌پرسد تا ورودی معتبر باشد.
    اگر کاربر Q بزند، None برمی‌گرداند تا برنامه از این بخش خارج شود.
    """
    while True:
        value = input(prompt).strip()
        if value.lower() == QUIT_KEY:
            return None
        error = validator(value)
        if error is None:
            return value
        print(error)

    
def sign_up():
    """ثبت‌نام. اگر کاربر Q بزند، None برمی‌گرداند."""
    def check_username(u):
        error = validate_username(u)
        if error:
            return error
        if username_exists(u):
            return "This username is already taken."
        return None

    username = ask_until_valid("Enter a username (or Q to go back): ", check_username)
    if username is None:
        return None

    password = ask_until_valid("Enter a password (or Q to go back): ", validate_password)
    if password is None:
        return None

    register_user(username, password)
    print(f"Account created. Welcome, {username}!")
    return username

def log_in():
    """ورود. اگر کاربر Q بزند، None برمی‌گرداند."""
    while True:
        username = input("Username (or Q to go back): ").strip()
        if username.lower() == QUIT_KEY:
            return None

        if not username_exists(username):
            print("This username does not exist. Try again.")
            continue

        password = input("Password (or Q to go back): ")
        if password.lower() == QUIT_KEY:
            return None

        if check_login(username, password):
            print(f"Welcome back, {username}!")
            return username
        print("Wrong password. Try again.")


def main():
    
    print("Welcome to my game")
    while True:
        print('1: Sign Up')
        print('2: Log In')
        print('3: Exit')
        answer = input("what you want?(1, 2 or 3) ")
        
        if answer == "1":
            username = sign_up()
            if username is None:
                continue

        elif answer == "2":
            username = log_in()
            if username is None:
                continue
            
        elif answer == "3":
            print('Goodbye')
            exit()
            
        else:
            print("Invalid choice. Please try again.")
            continue
        break

    while True:
        print('-'*20)
        print("Let's start")
        print("1: New Game")
        print("2: Recent Games")
        print("3: Exit")
        
        choice = input("what you want? ").strip()
        
        if choice == "1":
            start_game(username)
        elif choice == "2":
            history_game(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


        

if __name__ == '__main__':
    main()