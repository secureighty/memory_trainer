string = ""
string += "{\n"
for i in range(1, int(input("how many numeric units: "))+1):
    string += f"\t\"{i}\":[\"\"],\n"

string += "}"

with open("dicts/"+input("file name: "), "w+") as f:
    f.write(string)