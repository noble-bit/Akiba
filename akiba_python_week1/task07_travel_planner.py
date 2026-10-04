# TASK 7 - Travel Planner

destination = input("Enter destination: ")
distance = float(input("Enter distance in km: "))
speed = float(input("Enter average speed in km/h: "))

# time = distance / speed
time_hours = distance / speed

print("\n------ Travel Plan ------")
print("Destination: " + destination)
print("Distance: " + str(distance) + " km")
print("Average Speed: " + str(speed) + " km/h")
print("Estimated Travel Time: " + str(time_hours) + " hours")
