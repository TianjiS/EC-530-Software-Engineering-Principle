#If the user gives you two arrays of geo location, match each point in the first array to the closest one in the second array
import math

R = 6371  # Earth's radius
# Example input arrays (latitude, longitude)
geolocation_1 = [[40.7128, -74.0060]]  # New York
geolocation_2 = [[37.7749, -122.4194], [41.8781, -87.6298], [29.7604, -95.3698], [39.9075, 116.39723]] #LA, Chicago, Beijing

def Distance(W1, J1, W2, J2):
    # Degrees to radians
    W1, J1, W2, J2 = map(math.radians, [W1, J1, W2, J2])

    WD = W2 - W1
    JD = J2 - J1

    # Applying the Haversine formula
    a = math.sin(WD / 2)**2 + math.cos(W1) * math.cos(W2) * math.sin(JD / 2)**2
    distance = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * R
    return distance

for point1 in geolocation_1:
    w1, j1 = point1
    distance = 40075  #Earth's circumference
    m = -1  # Index of the closest point in geolocation_2

    for i in range(len(geolocation_2)):
        w2, j2 = geolocation_2[i]
        distance1 = Distance(w1, j1, w2, j2)
        if distance1 < distance:
            distance = distance1
            m = i

    print(f"The closest point to ({w1}, {j1}) is at {geolocation_2[m]}, the distance is {distance:.2f} km.")

