import subprocess
import random
import secrets


def validate_username(username):
    if not isinstance(username, str):
        return False
    username = username.strip()
    if len(username) < 4 or len(username) > 20:
        return False
    return username.replace("_", "").isalnum()


def create_profile_message(username, role="student"):
    if not validate_username(username):
        raise ValueError("Invalid username")
    allowed_roles = {"student", "lecturer", "admin"}
    if role not in allowed_roles:
        raise ValueError("Invalid role")
    return f"User: {username.strip()} | Role: {role}"


def show_directory_contents():
    subprocess.run(["cmd", "/c", "dir"], check=True)


def generate_reset_code():
    return str(secrets.randbelow(1_000_000)).zfill(6)


if __name__ == "__main__":
    print(create_profile_message("student_01"))