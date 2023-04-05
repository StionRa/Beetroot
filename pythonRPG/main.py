import os
import json
file_test = 'file.json'
def create_new_dict(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, check if it is empty
        if os.path.getsize(filename) == 0:
            # If the file is empty, create a new dictionary and write it to the file
            data = {"items": []}
            with open(filename, "w") as f:
                json.dump(data, f)
            print("Created new dictionary in file:", filename)
        else:
            print("File is not empty:", filename)
    else:
        # If the file does not exist, create a new dictionary and write it to the file
        data = {"items": []}
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Created new file and dictionary:", filename)