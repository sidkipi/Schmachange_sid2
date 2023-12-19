import os
import re
import sys

valid = True
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV](\d+\.\d+\.\d+)__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []
unmatched_files = []

# Keep track of the highest version
highest_version = "0.0.0"

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        match1 = pattern1.match(file_name)
        match2 = pattern2.match(file_name)
        match3 = pattern3.match(file_name)

        if match2:
            version = match2.group(1)

            if version <= highest_version:
                print(f"File '{file_name}' has an equal or lower version. Exiting with an error.")
                sys.exit(1)
            else:
                highest_version = version

        if match1 or match2 or match3:
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)
        else:
            print(f"File '{file_name}' does not match the pattern.")
            unmatched_files.append(file_name)
            valid = False

if valid:
    print("::set-output name=valid::true")
    print("Matching files:", matching_files)
else:
    print("Validation failed. Exiting with an error.")
    print("Unmatched files:", unmatched_files)
    sys.exit(1)
