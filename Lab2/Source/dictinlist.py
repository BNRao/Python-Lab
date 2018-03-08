n = int(input("Number of contacts : "))
contacts = []
contact_dict = {}
for i in range(n) :
    contact_dict["name"] = input("Enter name ")
    contact_dict["number"] = input("Enter number ")
    contact_dict["email"] = input("Enter email ")
    contacts.append(contact_dict.copy())
print(contacts)
def opt() :
    x = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
    return x

if opt()=='a':
    name = str(input("Enter the name: "))
    for a in contacts:
        if a['name'] == name:
            print(a)
if opt()=='b':
    num = str(input("Enter the number: "))
    for a in contacts:
        if a['number'] == num:
            print(a)
if opt()=='c':
    name = str(input("Enter the name: "))
    number = int(input("Enter the number: "))
    for index,a in enumerate(contacts):
        if a['name'] == name:
            contacts[index]['number']=number
    print(contacts)
if opt()=='d' :
    exit()

