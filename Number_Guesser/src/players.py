import os
import os
import re
import hashlib
import secrets

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SRC_DIR)
PLAYERS_FILE = os.path.join(PROJECT_DIR, "players_info.txt")

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")

def load_players():
    ''' همه کاربرارو از فایل میخونه و به شکل دیکشنری ایدی و اسم برمیگردونه'''
    players = {}
    
    if not os.path.exists(PLAYERS_FILE):
        return players

    with open(PLAYERS_FILE, "r") as f:
        for line in f.readlines():
            username, salt, pw_hash = line.strip().split(",")
            players[username] = {"salt": salt, "hash": pw_hash}
    return players

def username_exists(username):
    return username in load_players()

def validate_username(username):
    """اگر valid باشه None رو برمیگردونه """
    if not USERNAME_PATTERN.match(username):
        return "Username must be 3-20 characters: letters, digits, or underscore."
    return None

def validate_password(password):
    """Returns None if valid, otherwise an error message."""
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if not any(c.isalpha() for c in password):
        return "Password must contain at least one letter."
    if not any(c.isdigit() for c in password):
        return "Password must contain at least one number."
    return None

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), bytes.fromhex(salt), 100_000
    ).hex()


def register_user(username, password):
    """Creates a new user and saves it. Assumes validation was already done."""
    salt = secrets.token_hex(16)
    pw_hash = hash_password(password, salt)
    with open(PLAYERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{salt},{pw_hash}\n")


def check_login(username, password):
    """Returns True if the username exists and the password matches."""
    players = load_players()
    if username not in players:
        return False
    info = players[username]
    return hash_password(password, info["salt"]) == info["hash"]
