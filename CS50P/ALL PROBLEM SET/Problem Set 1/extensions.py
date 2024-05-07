# using "in" function if "".gif" is there in user input it will print("image/gif")
# otherwise print default "application/octet-stream"
file =input("File name: ")
file_name =file.lower().strip()
if "gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name:
    print("image/jpeg")
elif ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name :
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name :
    print("application/zip")
else:
    print("application/octet-stream")