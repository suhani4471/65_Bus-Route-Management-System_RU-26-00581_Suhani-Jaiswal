# 🚌 Bus Route Management System

A Python command-line application that models an intercity bus network as a weighted graph and uses **Breadth-First Search (BFS)** to find routes, check connections, and calculate ticket fares.

---

## ✨ Features

* **View All Stops:** Lists every bus stop available in the network.
* **Inspect Connections:** Displays direct neighbouring stops and road distances (in km) for any selected city.
* **Route Finder (BFS):** Uses `collections.deque` to find the path with the **fewest intermediate stops** between a source and destination.
* **Automatic Fare Calculation:** Computes total route distance and calculates ticket fare at a flat rate of **Rs. 1.50/km**.
* **Edge-Case Handling:** Gracefully handles invalid stop names, identical source/destination entries, and disconnected sub-networks (e.g., Jagdalpur–Kondagaon).

---

## 🗺️ Network Coverage

The built-in dataset models intercity connections across Chhattisgarh:

* **Main Network:** Durg, Bhilai, Raipur, Bilaspur, Dhamtari, Rajnandgaon
* **Disconnected Sub-Network:** Jagdalpur ↔ Kondagaon *(used to demonstrate unreachable route handling)*

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.x (Standard Library only — `collections.deque`)
* **Data Structure:** Weighted adjacency list implemented via nested dictionaries
* **Algorithm:** Breadth-First Search (BFS) for minimum-hop pathfinding
