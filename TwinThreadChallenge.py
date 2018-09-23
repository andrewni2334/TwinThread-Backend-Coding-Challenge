# TwinThread Backend Coding Challenge
# Written by: Andrew Ni on 9/23/2018

import webbrowser
import urllib.request, json

# opens the url link and imports the JSON data
with urllib.request.urlopen("https://www.twinthread.com/code-challenge/assets.txt") as url:
    data = json.loads(url.read().decode())

# provide list of actions for user input
x = int(input('Enter number for the action you would like to commit: \n1. Read JSON test assest data \n2. Search of asset data by name, description, etc. \n3. List all assets that have a critical status \n4. Count unique class names \n5. Build a visual hierarchy for a given asset id \n'))

# opens url with JSON data
if x == 1:
    webbrowser.open('https://www.twinthread.com/code-challenge/assets.txt')

# searching through JSON data for particular asset
elif x == 2:

    y = int(input('Enter number for the type of search you would like to commit: \n1. Asset ID \n2. Name \n3. Description\n'))

    # searches list of assets using asset id
    if y == 1:
        id = int(input("Enter Asset ID: "))
        for i in data['assets']:
            if id == i['assetId'] :
                print('assetId: ' + str(i['assetId']))
                print('name: ' + str(i['name']))
                print('description: ' + str(i['description']))
                print('status: ' + str(i['status']))
                print('icon: ' + str(i['icon']))
                print('Running: ' + str(i['Running']))


    # searches list of assets using name
    if y == 2:
        n = input("Enter Name: ")
        for i in data['assets']:
            if n in i['name'] :
                print('assetId: ' + str(i['assetId']))
                print('name: ' + str(i['name']))
                print('description: ' + str(i['description']))
                print('status: ' + str(i['status']))
                print('icon: ' + str(i['icon']))
                print('Running: ' + str(i['Running']))

    # searches list of assets using description
    if y == 3:
        des = input("Enter Description: ")
        for i in data['assets']:
            if des in i['description']:
                print('assetId: ' + str(i['assetId']))
                print('name: ' + str(i['name']))
                print('description: ' + str(i['description']))
                print('status: ' + str(i['status']))
                print('icon: ' + str(i['icon']))
                print('Running: ' + str(i['Running']))

# lists assets with critical status
elif x == 3:
    ct = 0
    for i in data['assets']:
        if i['status'] == 3:
            ct+=1
            print(str(ct)+":")
            print('assetId: ' + str(i['assetId']))
            print('name: ' + str(i['name']))
            print('description: ' + str(i['description']))
            print('status: ' + str(i['status']))
            print('icon: ' + str(i['icon']))
            print('Running: ' + str(i['Running'])+"\n")


# counts and lists all individual class names
elif x == 4:
    count = 0
    for i in data['assets']:
        count += 1

    print('There are ' + str(count) + ' class names in this file')

    class_name = int(input("Would you like to see the names of those assets?\n1. yes\n2. no\n"))
    if class_name == 1 :
        for i in data['assets']:
            print(i['name'])


else:
    print()

