UserName, SinChar = input("Enter User Name and Single Char: ").split(",")
print(f"username lenght is: {len(UserName)}")
print(f"No. of \"{SinChar}\" in \"{UserName}\" is: {UserName.count(SinChar)}")
#Case Insensitive
print(f"No. of \"{SinChar}\" in \"{UserName}\" is: {(UserName.lower()).count(SinChar)+(UserName.upper()).count(SinChar)}")
#Case Insens Logic
print(f"No. of \"{SinChar}\" in \"{UserName}\" is: {(UserName.lower()).count(SinChar.lower())}")
#Case Insen - stript extra spaces from input 
print(f"No. of \"{SinChar}\" in \"{UserName}\" is: {(UserName.strip().lower()).count(SinChar.strip().lower())}")