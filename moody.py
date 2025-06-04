import csv
from datetime import datetime

def main():
    print("Hello there!")
    name = input("What's your name? ")
    print(f"Hi, {name}! I'm Moody the Mood Monster! Pleased to meet you.")
    while True:
        command = input("What would you like to do? (add/view/stats/quit): ").strip().lower()

        if command == "add":
            add_mood()
        elif command == "view":
            view_moods()
        elif command == "stats":
            print("[View Stats] - coming soon!")
        elif command == "quit":
            print("Bye for now!")
        else:
            print("Sorry, Moody doesn't understand this request.")

# Helper function - allows user to record their mood and an optional note and saves entry to mood_log.csv
def add_mood():
    mood = input("How are you feeling today? ").strip().lower()
    note = input("Would you like to add a note? (press enter to skip): ").strip()

    # create time stamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("mood_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, mood, note])

    # Placeholder response - later customize based on mood type
    print(f"Got it! Moody hopes you feel {mood} again soon.")

# Helper function - allow user to view the entries from the mood_log.csv
def view_moods():
    try:
        with open("mood_log.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            entries = list(reader)

            if not entries:
                print("No mood entries yet.")
                return
            
            print("\nYour Mood Entries:")
            for row in entries:
                timestamp, mood, note = row
                print(f"{timestamp} - {mood.capitalize()} - {note if note else 'No note'}")
    except FileNotFoundError:
        print("Mood log file not found. Try adding a mood first!")

if __name__ == "__main__":
    main()