from heapq import *

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

  def distance_to_origin(self):
    return (self.x * self.x) + (self.y * self.y)
  
  # Comparator Function for Max Heap
  # Use >, since Max Heap. We want largest distance at root
  def __lt__(self, other):
    return self.distance_to_origin() > other.distance_to_origin()


def find_closest_points(points, k):
  maxHeap = []

  # Add K points to maxHeap
  for i in range(k):
    heappush(maxHeap, points[i])


  # Loop through rest of the points
  # If distance is smaller than root, then pop root and insert new point
  for i in range(k, len(points)):
    if points[i].distance_to_origin() < maxHeap[0].distance_to_origin():
      heappop(maxHeap)
      heappush(maxHeap, points[i])

  return list(maxHeap)


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()


