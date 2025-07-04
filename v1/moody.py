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
            show_stats()
        elif command == "quit":
            print("Bye for now!")
            break # exists loop
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

    # Mood-based responses
    positive_moods = ["happy", "excited", "calm", "grateful"]
    neutral_moods = ["okay", "meh", "fine"]
    negative_moods = ["sad", "angry", "tired", "anxious", "overwhelmed", "bad", "mad"]

    if mood in positive_moods:
        print("Yay! Moody's smiling too 😄")
    elif mood in neutral_moods:
        print("I appreciate you checking in today 💛")
    elif mood in negative_moods:
        print("Sending you a virtual hug 💙")
    else: 
        print("Moody's here with you  💚")

# Helper function - load mood entries
def load_mood_entries():
    try:
        with open("mood_log.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader) # Skip the header row: date, mood, notes
            entries = list(reader)
            return entries
    except FileNotFoundError:
        return []

# Helper function - allow user to view the entries from the mood_log.csv
def view_moods():
    entries = load_mood_entries()

    if not entries:
        print("No mood entries yet.")
        return
    
    print("\nYour Mood Entries:")
    for row in entries:
        if len(row) != 3:
            continue
        timestamp, mood, note = row
        print(f"{timestamp} - {mood.capitalize()} - {note if note else 'No note'}")

# Helper function: show stats - how many times each mood was logged
def show_stats():
    entries = load_mood_entries()
    
    if not entries:
        print("No mood entries yet.")
        return
    
    mood_counts = {}

    for row in entries:
        if len(row) != 3:
            continue
        _, mood, _ = row
        mood_counts[mood] = mood_counts.get(mood, 0) + 1

    print("\nMood Summary:")
    for mood, count in mood_counts.items():
        print(f"{mood.capitalize()}: {count}")

    most_common = max(mood_counts, key=mood_counts.get)
    print(f"\nMost common mood: {most_common.capitalize()} ({mood_counts[most_common]} times)")

    

if __name__ == "__main__":
    main()