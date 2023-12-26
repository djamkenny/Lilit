extension = input("File name: ")

extension = extension.split(".")

application = ["txt", "pdf", "zip"]
end = extension[1]


if (len(extension) == 1):
    print("application/octet-stream")

elif (end in application):
        print(f"application/{end}")

else:
    
    print(f"image/{end}")

    