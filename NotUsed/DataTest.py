import sys
Users = {"test":4}

   
with open("Cache/UserData.txt", 'w') as f:
    sys.stdout = f
    print(Users)
    f.close()