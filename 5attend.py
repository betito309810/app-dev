from datetime import date
import subprocess
import os

today = date.today()
print("Date:", today)

repo_path = "/Users/anya/Downloads/app-dev"
file_to_change = "attend.txt"

# Change to the repository directory
try:
    os.chdir(repo_path)
    print(f"Changed directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: The directory '{repo_path}' was not found.")
    exit()

# Loop to create 5 commits
for i in range(5):
    # Append a new line to the file
    with open(file_to_change, "a") as f:
        f.write(f"Contribution number {i+1} on {today}\n")

    try:
        # Add and commit the file
        subprocess.run(["git", "add", file_to_change], check=True)
        subprocess.run(["git", "commit", "-m", f"Adding contribution {i+1}"], check=True)
        print(f"Commit {i+1} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during git operations: {e}")
        exit()

# Push all commits to the remote repository
print("Pushing commits to the remote repository...")
try:
    subprocess.run(["git", "push"], check=True)
    print("Script finished. 5 commits have been pushed.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred during the push: {e}")
    print("Please check your Git credentials and network connection.")
