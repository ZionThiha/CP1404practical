def extract_name(email):
    # Extracting the part before '@' symbol
    name = email.split('@')[0]
    # Capitalizing each word and joining them with space
    name = ' '.join(name.split('.')).title()
    return name

def main():
    user_dict = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == "" or confirmation == "y":
            user_dict[email] = name
        else:
            name = input("Name: ").strip().title()
            user_dict[email] = name

    for email, name in user_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
