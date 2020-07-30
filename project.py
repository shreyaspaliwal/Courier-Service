# Courier service
parcels = list()


def main():
    print("Select an option:")
    print("1. Add")
    print("2. Search")
    print("3. Exit")
    try:
        option = int(input("Enter your choice:"))
    except:
        print("Enter 1 or 2 or 3")
        quit()
    opt(option)


# areas = ['kothrud', 'katraj', 'viman nagar', 'pimpri']


def opt(option):
    if option == 1:
        name = input("Enter name of parcel: ")
        address = input("Enter address of the receiver: ")
        zone = input("Enter the area of the receiver's address: ")
        parcel = dict()
        parcel['name'] = name
        parcel['address'] = address
        parcel['zone'] = zone
        parcels.append(parcel)
        print("Parcel added")

# print(parcels)
    elif option == 2:
        seacrh_string = input("Enter zone/area of parcel:")
        for parcel in parcels:
            if parcel['zone'] == seacrh_string:
                print(parcel)

    elif option == 3:
        pass
    main()


main()
