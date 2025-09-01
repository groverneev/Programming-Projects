def myFunction(vehicle_wheel_count):
    VCount = []
    for z in vehicle_wheel_count:
        VCount.append(vehicle_wheel_count[z])
    VCount.sort()
    for i in range(len(VCount)):
        for z in vehicle_wheel_count:
            if vehicle_wheel_count[z] == VCount[i]:
                print(z, VCount[i])
myFunction ({"car" : 4,"motorcycle" : 2,"truck" : 8,"unicycle" : 1,"tricycle" : 3, "bicycle" : 2})