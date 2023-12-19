import os
import re
import sys

valid = True
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []
unmatched_files = []

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name) or pattern3.match(file_name):
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
