import subprocess
import os

repo_path = "/Users/anya/Downloads/app-dev"
file_to_change = "attend.txt"

# Change to the repository directory
os.chdir(repo_path)

# Loop to create 6 commits
for i in range(6):
    # Append a new line to the file
    with open(file_to_change, "a") as f:
        f.write(f"Contribution number {i+1}\n")

    # Add the file to staging
    subprocess.run(["git", "add", file_to_change])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", f"Adding contribution {i+1}"])

# Push all commits to the remote repository
subprocess.run(["git", "push"])

print("Script finished. 6 commits have been pushed.")
