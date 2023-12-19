import os
import re
import sys

valid = True
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV](\d+\.\d+\.\d+)__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []
unmatched_files = []

# Keep track of the existing versions
existing_versions = set()

# Keep track of the current file causing the issue
current_file_causing_issue = None

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        match1 = pattern1.match(file_name)
        match2 = pattern2.match(file_name)
        match3 = pattern3.match(file_name)

        if not (match1 or match2 or match3):
            print(f"File '{file_name}' does not match the pattern.")
            unmatched_files.append(file_name)
            valid = False
        elif match2:
            version = match2.group(1)

            if any(existing_version <= version for existing_version in existing_versions):
                print(f"File '{file_name}' has an equal or lower version. Please enter a higher version.")
                valid = False
                current_file_causing_issue = file_name  # Set the current file causing the issue
                break  # Exit the loop, no need to process other files
            else:
                existing_versions.add(version)

        if match1 or match2 or match3:
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)

if not valid:
    print("Validation failed.")
    print("Unmatched files:", unmatched_files)
    sys.exit(1)

print("::set-output name=valid::true")
print("Matching files:", matching_files)

# Prompt only for the current file causing the issue
if current_file_causing_issue:
    user_input = input(f"Please enter a higher version for '{current_file_causing_issue}': ")
    # Process user input as needed
