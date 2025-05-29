# import streamlit as st
# import json
# import os
# import time
# from cryptography.fernet import Fernet
# from base64 import urlsafe_b64encode
# from hashlib import pbkdf2_hmac

# DATA_FILE = "store_data.json"
# KEY_FILE = "fernet_key.key"
# MAX_ATTEMPTS = 3
# LOCKOUT_DURATION = 300

# if os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "r") as f:
#         stored_data = json.load(f)
# else:
#     stored_data = {}

# if "failed_attempts" not in st.session_state:
#     st.session_state.failed_attempts = 0
# if "lockout_time" not in st.session_state:
#     st.session_state.lockout_time = 0
# if "current_user" not in st.session_state:
#     st.session_state.current_user = None

# def load_fernet_key():
#     if os.path.exists(KEY_FILE):
#         with open(KEY_FILE, "rb") as key_file:
#             return key_file.read()
#     else:
#         key = Fernet.generate_key()
#         with open(KEY_FILE, "wb") as key_file:
#             key_file.write(key)
#         return key

# cipher = Fernet(load_fernet_key())

# def hash_passkey(passkey, salt="somesalt", iterations=100_000):
#     key = pbkdf2_hmac('sha256', passkey.encode(), salt.encode(), iterations, dklen=32)
#     return urlsafe_b64encode(key).decode()

# def encrypt_data(text):
#     return cipher.encrypt(text.encode()).decode()

# def decrypt_data(encrypted_text):
#     return cipher.decrypt(encrypted_text.encode()).decode()

# def save_data():
#     with open(DATA_FILE, "w") as f:
#         json.dump(stored_data, f, indent=4)

# def is_locked_out():
#     if st.session_state.failed_attempts >= MAX_ATTEMPTS:
#         if time.time() - st.session_state.lockout_time < LOCKOUT_DURATION:
#             return True
#         else:
#             st.session_state.failed_attempts = 0
#     return False

# st.set_page_config(page_title="Secure Data System", page_icon="🔐", layout="centered")
# st.markdown(" ## 🔐 Secure Data Encryption System")

# st.caption("Encrypt and securely retrieve your sensitive information.")

# menu = ["Home", "Login/Register", "Store Data", "Retrieve Data", "Logout"]
# choice = st.sidebar.selectbox("🔽 Navigation", menu)


# # Home
# if choice == "Home":
#     st.markdown(" #### Welcome to Your Secure Vault")
#     st.write("Use this system to securely register, encrypt, and retrieve personal data with a custom passkey.")
    
#     st.subheader("🚀 Key Features")
#     st.info(
#         "- User Registration & Login\n"
#         "- Encrypt & Store Sensitive Data\n"
#         "- Secure Data Retrieval\n"
#         "- Login Protection with Lockout"
#     )

#     st.caption("Use the sidebar to get started.")



# # Login / Register
# elif choice == "Login/Register":
#     st.markdown(" ### User Authentication")

#     tab_register, tab_login = st.tabs(["📝 Register", "🔓 Login"])

#     with tab_register:
#         new_user = st.text_input("Choose a Username")
#         new_pass = st.text_input("Choose a Passkey", type="password")

#         if st.button("Register"):
#             if new_user and new_pass:
#                 if new_user in stored_data:
#                     st.warning("User already exists.")
#                 else:
#                     stored_data[new_user] = {
#                         "passkey": hash_passkey(new_pass),
#                         "data": {}
#                     }
#                     save_data()
#                     st.success("Registration successful. You can now log in.")
#             else:
#                 st.error("Please fill out both fields.")

#     with tab_login:
#         username = st.text_input("Username")
#         passkey = st.text_input("Passkey", type="password")

#         if is_locked_out():
#             st.session_state.current_user = None
#             st.error("🚫 Too many failed attempts. Please wait a few minutes.")
#             st.stop()

#         if st.button("Login"):
#             if username in stored_data:
#                 if hash_passkey(passkey) == stored_data[username]["passkey"]:
#                     st.session_state.current_user = username
#                     st.session_state.failed_attempts = 0
#                     st.success(f"Welcome back, {username}!")
#                 else:
#                     st.session_state.failed_attempts += 1
#                     if st.session_state.failed_attempts >= MAX_ATTEMPTS:
#                         st.session_state.lockout_time = time.time()
#                         st.error("Too many failed attempts. Try again later.")
#                         st.stop()
#                     else:
#                         attempts_left = MAX_ATTEMPTS - st.session_state.failed_attempts
#                         st.error(f"Incorrect passkey. Attempts left: {attempts_left}")
#             else:
#                 st.error("User does not exist.")

# # Store Data
# elif choice == "Store Data":
#     if not st.session_state.current_user:
#         st.warning(" Please log in to continue.")
#         st.stop()

#     st.markdown(" ### Store Your Data")
#     data_name = st.text_input("Enter a name for your data")
#     user_data = st.text_area("Enter the data to encrypt")

#     if st.button("Encrypt & Save"):
#         if data_name and user_data:
#             user = st.session_state.current_user
#             encrypted = encrypt_data(user_data)
#             stored_data[user]["data"][data_name] = encrypted
#             save_data()
#             st.success(f"Data '{data_name}' encrypted and saved.")
#         else:
#             st.error("Please fill in both fields.")

# # Retrieve Data
# elif choice == "Retrieve Data":
#     if not st.session_state.current_user:
#         st.warning(" Please log in to continue.")
#         st.stop()

#     if is_locked_out():
#         st.session_state.current_user = None
#         st.error("🚫 Too many failed attempts. You've been logged out.")
#         st.stop()

#     st.markdown(" ### Retrieve Your Data")
#     user = st.session_state.current_user
#     available_keys = list(stored_data[user]["data"].keys())

#     if available_keys:
#         selected_key = st.selectbox("Choose a data item", available_keys)
#         confirm_pass = st.text_input("Re-enter your passkey", type="password")

#         if st.button("Decrypt"):
#             if hash_passkey(confirm_pass) == stored_data[user]["passkey"]:
#                 st.session_state.failed_attempts = 0
#                 decrypted = decrypt_data(stored_data[user]["data"][selected_key])
#                 st.success(f"Decrypted data for '{selected_key}':")
#                 st.code(decrypted)
#             else:
#                 st.session_state.failed_attempts += 1
#                 if st.session_state.failed_attempts >= MAX_ATTEMPTS:
#                     st.session_state.lockout_time = time.time()
#                     st.session_state.current_user = None
#                     st.error("Too many failed attempts. You've been logged out.")
#                     st.stop()
#                 else:
#                     attempts_left = MAX_ATTEMPTS - st.session_state.failed_attempts
#                     st.error(f"Incorrect passkey. Attempts left: {attempts_left}")
#     else:
#         st.info("No data stored yet.")

# # Logout
# elif choice == "Logout":
#     st.session_state.current_user = None
#     st.session_state.failed_attempts = 0
#     st.session_state.lockout_time = 0
#     st.success("✅ You have been logged out.")


