import getpass
import random
import hashlib
import os

# ensure users file exists
open("users.txt", "a").close()

def hash_password(password: str) -> str:
    """Return SHA-256 hex digest of the given password string."""
    return hashlib.sha256(password.encode()).hexdigest()

def looks_hashed(s: str) -> bool:
    """Rudimentary check: SHA-256 hex digest is 64 hex characters."""
    if not s:
        return False
    if len(s) != 64:
        return False
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def read_users():
    """Read users.txt and return list of lines (raw)."""
    with open("users.txt", "r") as f:
        return f.readlines()

def write_users(lines):
    """Overwrite users.txt with given lines (each should end with \\n)."""
    with open("users.txt", "w") as f:
        f.writelines(lines)

print("Welcome to the user system")
print("1. Register")
print("2. Login")
print("3. Exit")
print("4. Forgot password?")

choice = input("Choose an option (1/2/3/4): ")

# ----------------------------
# Register
# ----------------------------
if choice == "1":
    username = input("Enter a new username: ")

    # password validation
    while True:
        password = getpass.getpass("Enter your password (at least 6 characters): ")
        if len(password) < 6:
            print("Password too short. Please enter at least 6 characters.")
        else:
            break

    security_answer = input("Security Question - What is the name of your first school? ")

    # check if user exists
    exists = False
    lines = read_users()
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) >= 1 and parts[0] == username:
            exists = True
            break

    if exists:
        print("Username already exists. Try another one.")
    else:
        hashed = hash_password(password)
        with open("users.txt", "a") as file:
            file.write(f"{username}:{hashed}:{security_answer}\n")
        print("✅ Registration successful! (password stored securely)")

# ----------------------------
# Login
# ----------------------------
elif choice == "2":
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        success = False
        user_line_index = None
        user_parts = None
        lines = read_users()

        # find user
        for idx, line in enumerate(lines):
            parts = line.strip().split(":")
            if len(parts) >= 1 and parts[0] == username:
                user_line_index = idx
                user_parts = parts
                break

        if user_line_index is None:
            print("❌ Invalid username or password.")
            attempts -= 1
            if attempts > 0:
                print(f"⚠️ You have {attempts} attempt(s) left. Try again.")
            else:
                print("⛔ Too many failed attempts. Access denied.")
            continue

        stored_pass = user_parts[1] if len(user_parts) > 1 else ""
        stored_sec = user_parts[2] if len(user_parts) > 2 else ""

        # two possibilities: stored_pass is hashed, or stored_pass is plain text (old)
        if looks_hashed(stored_pass):
            # compare hashed input with stored hash
            if hash_password(password) == stored_pass:
                success = True
        else:
            # legacy plain-text: compare directly
            if password == stored_pass:
                success = True
                # migrate to hashed password (update file)
                new_hashed = hash_password(password)
                # replace the line preserving security answer (if any)
                sec = stored_sec
                lines[user_line_index] = f"{username}:{new_hashed}:{sec}\n"
                write_users(lines)
                print("ℹ️ Legacy password format detected — account upgraded to secure storage.")

        if success:
            print(f"✅ Login successful! Welcome, {username}")
            print("\n1. Change Password")
            print("2. Delete Account")
            print("3. Logout")
            option = input("Choose an option: ")

            # Change password: preserve security answer
            if option == "1":
                old_pass = getpass.getpass("Enter your current password again: ")
                # verify old password (we have stored hashed now)
                stored_pass_after = lines[user_line_index].strip().split(":")[1]
                if looks_hashed(stored_pass_after):
                    if hash_password(old_pass) == stored_pass_after:
                        pass_ok = True
                    else:
                        pass_ok = False
                else:
                    pass_ok = (old_pass == stored_pass_after)

                if pass_ok:
                    while True:
                        new_pass = getpass.getpass("Enter your new password (at least 6 characters): ")
                        if len(new_pass) < 6:
                            print("Password too short. Please enter at least 6 characters.")
                        else:
                            break

                    # update file
                    with open("users.txt", "r") as file:
                        all_lines = file.readlines()
                    with open("users.txt", "w") as file:
                        for line in all_lines:
                            parts = line.strip().split(":")
                            uname = parts[0] if len(parts) > 0 else ""
                            usec = parts[2] if len(parts) > 2 else ""
                            if uname == username:
                                file.write(f"{username}:{hash_password(new_pass)}:{usec}\n")
                            else:
                                file.write(line)
                    print("✅ Password changed successfully!")
                else:
                    print("❌ Incorrect current password.")

            # Delete account
            elif option == "2":
                confirm = input("⚠️ Are you sure you want to delete your account? (yes/no): ")
                if confirm.lower() == "yes":
                    with open("users.txt", "r") as file:
                        lines = file.readlines()
                    with open("users.txt", "w") as file:
                        for line in lines:
                            parts = line.strip().split(":")
                            uname = parts[0] if len(parts) > 0 else ""
                            if uname != username:
                                file.write(line)
                    print("🗑️ Your account has been deleted successfully.")
                else:
                    print("❎ Account deletion canceled.")

            else:
                print("🚪 Logged out.")
            break

        else:
            attempts -= 1
            print("❌ Invalid username or password.")
            if attempts > 0:
                print(f"⚠️ You have {attempts} attempt(s) left. Try again.")
            else:
                print("⛔ Too many failed attempts. Access denied.")

# ----------------------------
# Forgot password (Reset)
# ----------------------------
elif choice == "4":
    username = input("Enter your username: ")
    found = False
    found_line = ""
    lines = read_users()
    for line in lines:
        parts = line.strip().split(":")
        uname = parts[0] if len(parts) > 0 else ""
        if uname == username:
            found = True
            found_line = line.strip()
            break

    if not found:
        print("❌ Username not found.")
    else:
        parts = found_line.split(":")
        stored_security = parts[2] if len(parts) > 2 else ""

        print("Choose verification method:")
        print("1. Answer security question")
        print("2. Receive verification code (simulated)")
        method = input("Pick 1 or 2: ")

        if method == "1":
            if stored_security == "":
                print("❌ No security question found for this user.")
            else:
                answer = input("Security Question - What is the name of your first school? ")
                if answer.strip().lower() == stored_security.strip().lower():
                    while True:
                        new_pass = getpass.getpass("Enter your new password (at least 6 characters): ")
                        if len(new_pass) < 6:
                            print("Password too short. Please enter at least 6 characters.")
                        else:
                            break
                    # update file: preserve security answer
                    with open("users.txt", "r") as file:
                        all_lines = file.readlines()
                    with open("users.txt", "w") as file:
                        for line in all_lines:
                            parts = line.strip().split(":")
                            uname = parts[0] if len(parts) > 0 else ""
                            usec = parts[2] if len(parts) > 2 else ""
                            if uname == username:
                                file.write(f"{username}:{hash_password(new_pass)}:{usec}\n")
                            else:
                                file.write(line)
                    print("✅ Password reset successfully using security question.")
                else:
                    print("❌ Security answer incorrect.")

        elif method == "2":
            code = str(random.randint(100000, 999999))
            print(f"[Simulated] Verification code sent: {code}")
            attempts_code = 3
            verified = False
            while attempts_code > 0:
                entered = input("Enter the verification code: ")
                if entered.strip() == code:
                    verified = True
                    break
                else:
                    attempts_code -= 1
                    print("❌ Incorrect code.")
                    if attempts_code > 0:
                        print(f"⚠️ {attempts_code} attempt(s) left.")
                    else:
                        print("⛔ Verification failed.")

            if verified:
                while True:
                    new_pass = getpass.getpass("Enter your new password (at least 6 characters): ")
                    if len(new_pass) < 6:
                        print("Password too short. Please enter at least 6 characters.")
                    else:
                        break
                # update file preserving security answer
                with open("users.txt", "r") as file:
                    all_lines = file.readlines()
                with open("users.txt", "w") as file:
                    for line in all_lines:
                        parts = line.strip().split(":")
                        uname = parts[0] if len(parts) > 0 else ""
                        usec = parts[2] if len(parts) > 2 else ""
                        if uname == username:
                            file.write(f"{username}:{hash_password(new_pass)}:{usec}\n")
                        else:
                            file.write(line)
                print("✅ Password reset successfully using verification code.")
        else:
            print("❌ Invalid method choice.")

# ----------------------------
# Exit / invalid
# ----------------------------
elif choice == "3":
    print("Goodbye!")
else:
    print("❌ Invalid choice. Please run the program again.")
