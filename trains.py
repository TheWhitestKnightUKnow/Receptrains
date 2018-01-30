import sys
from graph import Graph

# Entrypoint for the different solutions.
# Constructs the graph and decides which solution
# to employ
def main(argv):
    g = Graph()
    for string in (sys.argv[1].split(", ")):
        g.add_track(string[0], string[1], int(string[2:]))

# Calculate the total distance of a path, or 
# return 'NO SUCH ROUTE' if it doesn't exist
def distance(path):
    pass

# Find the number of routes that start at pointA
# and finish at pointB with a maximum total 
# distance of maxdistance.  PointA and PointB
# can be the same point.
def numRoutes(pointA, pointB, maxdistance):
    pass

# Find the shortest route in the graph between
# pointA and pointB
def shortestRoute(pointA, pointB):
    pass

main(sys.argv)