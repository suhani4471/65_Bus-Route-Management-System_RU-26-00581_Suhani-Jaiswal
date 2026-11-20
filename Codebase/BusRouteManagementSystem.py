from collections import deque

# Bus Network
bus_routes = {
    "Durg": {
        "Bhilai": 10,
        "Raipur": 40
    },
    "Bhilai": {
        "Durg": 10,
        "Raipur": 30
    },
    "Raipur": {
        "Bhilai": 30,
        "Durg": 40,
        "Bilaspur": 110,
        "Dhamtari": 80,
        "Rajnandgaon": 45
    },
    "Bilaspur": {
        "Raipur": 110
    },
    "Dhamtari": {
        "Raipur": 80
    },
    "Rajnandgaon": {
        "Raipur": 45
    },
    "Jagdalpur": {
        "Kondagaon": 75
    },
    "Kondagaon": {
        "Jagdalpur": 75
    }
}


# Show all stops
def show_stops():
    print("\nAvailable Bus Stops:")
    for stop in bus_routes:
        print("-", stop)


# Show connections
def show_connections():
    stop = input("Enter stop name: ").strip().title()

    if stop not in bus_routes:
        print(f"Stop '{stop}' not found.")
        return

    print(f"\n{stop} connects to:")

    for neighbour, distance in bus_routes[stop].items():
        print(f"{neighbour} ({distance} km)")


# Find route using BFS
def find_route():

    source = input("Enter source: ").strip().title()
    destination = input("Enter destination: ").strip().title()

    if source not in bus_routes:
        print(f"Stop '{source}' not found.")
        return

    if destination not in bus_routes:
        print(f"Stop '{destination}' not found.")
        return

    if source == destination:
        print("Source and destination are the same.")
        print("Distance: 0 km")
        print("Fare: Rs. 0.00")
        return

    queue = deque([[source]])
    visited = {source}

    while queue:

        path = queue.popleft()
        current = path[-1]

        if current == destination:
            break

        for neighbour in bus_routes[current]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    else:
        print(f"No route available between {source} and {destination}.")
        return

    # Calculate total distance
    distance = 0

    for i in range(len(path) - 1):
        distance += bus_routes[path[i]][path[i + 1]]

    fare = distance * 1.50

    print("\nRoute:", " -> ".join(path))
    print("Stops:", len(path))
    print("Distance:", distance, "km")
    print("Fare: Rs.", format(fare, ".2f"))


# Main Menu
while True:

    print("\n===== BUS ROUTE MANAGEMENT SYSTEM =====")
    print("1. Show all stops")
    print("2. Show connections")
    print("3. Find route")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_stops()

    elif choice == "2":
        show_connections()

    elif choice == "3":
        find_route()

    elif choice == "4":
        print("Thank you for using Bus Route Management System!")
        break

    else:
        print("Invalid choice! Please try again.")