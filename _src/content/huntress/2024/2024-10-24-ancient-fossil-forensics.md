# 2024-10-24 Ancient Fossil (Forensics)

*[image unavailable]*

*[embedded file: ancient.fossil]*

SQL data base stuff.

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

Figure out the fossil ui, and start browsing around.

*[image unavailable]*

*[image unavailable]*

Check all the commits, figured out we need each file content for each commit,

*[image unavailable]*

*[image unavailable]*

Make a script for it

```python
#Imports
import os
import subprocess
import re

# Path to your fossil repository
repo_path = "./ancient.fossil"

# Function to download file content from a specific commit
def download_file(repo, commit_hash, filename):
    # Create a directory for each commit hash
    os.makedirs(f"thefiles/{commit_hash}", exist_ok=True)

    # Command to download the file using fossil cat
    file_path = f"files/{commit_hash}/{filename}"
    with open(file_path, "w") as f:
        result = subprocess.run(["fossil", "cat", filename, "-r", commit_hash, "-R", repo], stdout=f)
        if result.returncode == 0:
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download: {filename} from commit {commit_hash}")

# Function to parse the fossil timeline output
def parse_timeline(timeline_output):
    commits = []
    commit_hash = None
    added_files = []

    for line in timeline_output.splitlines():
        # Find commit hashes
        if line.startswith("Commit:"):
            if commit_hash and added_files:
                commits.append({"commit": commit_hash, "files": added_files})
            commit_hash = line.split()[1]
            added_files = []

        # Find added files (filenames)
        if "ADDED" in line:
            match = re.search(r"ADDED\s+([A-Za-z0-9+/=]+)", line)
            if match:
                added_files.append(match.group(1))

    # Add the last commit if it contains added files
    if commit_hash and added_files:
        commits.append({"commit": commit_hash, "files": added_files})

    return commits

# Run fossil timeline command and capture the output
result = subprocess.run(["fossil", "timeline", "-R", repo_path, "-v", "--full", "-n", "500"], capture_output=True, text=True)

if result.returncode != 0:
    print(f"Error running fossil timeline: {result.stderr}")
    exit(1)

# Parse the timeline output to extract commits and added files
commits = parse_timeline(result.stdout)

# Download all files from each commit
for commit in commits:
    for file in commit['files']:
        download_file(repo_path, commit['commit'], file)
```

Download each file for each commit

*[image unavailable]*

Script to get the contents for each file

*[image unavailable]*

Cat that file and see the flag.txt

*[image unavailable]*

*[image unavailable]*
