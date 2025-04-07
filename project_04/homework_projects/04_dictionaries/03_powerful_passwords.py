# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
# For example, using a hash function called SHA256(...) something as simple as
# hello
# can be hashed into a much more complex
# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)



import hashlib

def hash_password(password):
    """Hashes a password using SHA256 and returns the hexadecimal digest."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """Checks if the given email's stored password hash matches the hash of password_to_check."""
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False


stored_logins = {
    "user@example.com": hash_password("securepassword"),
    "admin@example.com": hash_password("admin123")
}

print(login("user@example.com", "securepassword", stored_logins)) 
print(login("admin@example.com", "wrongpassword", stored_logins))  
print(login("unknown@example.com", "password", stored_logins))  
