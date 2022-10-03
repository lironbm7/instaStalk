import instaloader

L = instaloader.Instaloader()

# it is recommended to use a burner account (new/unused account)
# repetitive requests can result in a temporary account restriction by Instagram.
username = "your_username_here"
password = "your_password_here"
L.login(username, password)
L.save_session_to_file()
