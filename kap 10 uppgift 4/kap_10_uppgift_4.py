
def maximum(tal1,tal2,tal3):
    if (tal1<tal3>tal2):
        print("det storsta talet ar:", tal3)

    elif (tal1<tal2>tal3):
        print("det storsta talet ar:", tal2)

    elif (tal2<tal1>tal3):
        print("det storsta talet ar:", tal1)

    else:
        print("talen ar lika stora")

a = int(input("ange ett heltal"))

b = int(input("ange ett heltal"))

c = int(input("ange ett heltal"))

maximum(a,b,c)