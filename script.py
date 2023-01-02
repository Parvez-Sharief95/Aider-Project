import os
import random
import datetime
import subprocess
from faker import Faker

fake = Faker()

# Customize your repo path
REPO_PATH = os.getcwd()

# You can adjust this range
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2024, 12, 31)

# Realistic commit messages
commit_messages = [
    "Fix typo in README",
    "Update requirements.txt",
    "Refactor code",
    "Improve documentation",
    "Add new feature",
    "Minor fixes",
    "Optimize logic",
    "Fix bug",
    "Update .gitignore",
    "Improve comments",
    "Add logging",
    "Style updates",
]

def is_weekday(date):
    return date.weekday() < 5  # Mon-Fri

def make_commit(date):
    # Random time during the day
    hour = random.randint(9, 20)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    dt = datetime.datetime.combine(date, datetime.time(hour, minute, second))
    iso_time = dt.isoformat()

    # Create a dummy change
    filename = os.path.join(REPO_PATH, "dummy.txt")
    with open(filename, "a") as f:
        f.write(f"{fake.sentence()}\n")

    # Stage and commit
    subprocess.run(["git", "add", "."], cwd=REPO_PATH)
    subprocess.run(["git", "commit", "-m", random.choice(commit_messages),
                    "--date", iso_time], cwd=REPO_PATH)

def simulate_commits():
    current_date = start_date
    while current_date <= end_date:
        # Higher chance of weekday commits
        if is_weekday(current_date):
            if random.random() < 0.4:
                for _ in range(random.randint(1, 2)):
                    make_commit(current_date)
        else:
            if random.random() < 0.1:
                make_commit(current_date)

        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    simulate_commits()
