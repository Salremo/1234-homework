file = input("File name:")
file1 = file.lower()
if ".gif" in file1:
    print("image/.gif")
elif ".jpg" in file1:
    print("image/.jpg")
elif ".jpeg" in file1:
    print("image/.jpeg")
elif ".png" in file1:
    print("image/.png")
elif ".pdf" in file1:
    print("application/.pdf")
elif ".txt" in file1:
    print("text/.txt")
elif ".zip" in file1:
    print("application/.zip")
else: print("Wrong format: Filename.extension")