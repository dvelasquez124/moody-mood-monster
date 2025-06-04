def main():
    print("Hello there!")
    name = input("What's your name? ")
    print(f"Hi, {name}! I'm Moody the Mood Monster! Pleased to meet you.")
    while True:
        command = input("What would you like to do? (add/view/stats/quit): ").strip().lower()

        if command == "add":
            print("[Add mood] - coming soon!")
        elif command == "view":
            print("[View mood] - coming soon!")
        elif command == "stats":
            print("[View Stats] - coming soon!")
        elif command == "quit":
            print("Bye for now!")
        else:
            print("Sorry, Moody doesn't understand this request.")

if __name__ == "__main__":
    main()