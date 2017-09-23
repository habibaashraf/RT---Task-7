import csv

List=['Name', 'Email','Mobile', 'University', 'Major']

def mainFunc():

    var=True
    d=dict()
    x=[]
    print("Please enter your info")
    while 1:
        name=input("Name: ")
        if (name=="stop"):
            break
        x.append(name)
        email = input("Email: ")
        if (email == "stop"):
            break
        x.append(email)
        mobile = input("Mobile: ")
        if (mobile == "stop"):
            break
        x.append(mobile)
        uni = input("University: ")
        if (uni == "stop"):
            break
        x.append(uni)
        major = input("major: ")
        if (major == "stop"):
            break
        x.append(major)
    j=0
    csvInit()
    for i in range(len(x)):
        if x[i]=="stop":
            break

        d[List[j]] = x[i]
        j=j+1
        if j==5:
            j=0
            csvWrite(d)

    print(d)


def csvInit():
    f = open('names.csv', 'w')

    with f:
        headers = ['Name', 'Email', 'Mobile', 'University', 'Major']
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader()

def csvWrite(d):
    f = open('names.csv', 'a')

    with f:
        headers = ['Name', 'Email', 'Mobile', 'University', 'Major']
        writer = csv.DictWriter(f, fieldnames=headers)


        writer.writerow(d)

mainFunc()
