def main():
    name = input("Enter name: ")
    displaymenu()

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        displaymenu()
        choice = input(">>> ").upper()

    print("Finished.")

def displaymenu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

if __name__ == "__main__":
    main()
