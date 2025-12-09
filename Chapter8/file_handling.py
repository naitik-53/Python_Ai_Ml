file = open("certificate.txt", "r")
dataoffile = file.read()
dataoffile = dataoffile.lower()

if "live" in dataoffile:
    print("Yes Live Word Is Present In File")
else:
    print("No")

