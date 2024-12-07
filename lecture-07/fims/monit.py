#
import os

def getFiles(monitor):
    filesList = []

    for x in monitor:
        print(f"Checking: {x['path']} (Recursive: {x['recursive']})")
        if os.path.isdir(x['path']):
            print(f"Directory found: {x['path']}")
            if x['recursive']:
                filesList.extend([os.path.join(root, f) for (root, dirs, files) in os.walk(x['path']) for f in files])
            else:
                filesList.extend([os.path.join(x['path'], f) for f in os.listdir(x['path']) if os.path.isfile(os.path.join(x['path'], f))])
        elif os.path.isfile(x['path']):
            print(f"File found: {x['path']}")
            filesList.append(x['path'])
        else:
            print(f"Path not found: {x['path']}")
            if not os.path.exists(x['path']):
                print("The path does not exist.")
            if not os.path.isdir(x['path']):
                print("The path is not a directory.")
    return filesList
