import sys
from graph import Graph

# Entrypoint for the different solutions.
# Constructs the graph and decides which solution
# to employ
def main(argv):
    help_text = """The way to use the trains function is to give it 3 values: trains(graph, option, input)
graph  : a single string of comma-separated tracks.  eg "AB5, BC7, CA2"
option : either "path", "routes", or "shortest"
input  : for path, dash-separated towns, eg "A-B-C"
         for routes, the two towns to find routes between, and a maximum distance, dash-separated, eg. "A-C-9"
         for shortest, the two towns to find the shortest route between, dash-separated, eg. "C-B"
    """
    if len(argv) > 1:
        if argv[1] == "-h" or argv[1] == "--help":
            print help_text
            exit(0)
        # Import the graph from the first CLI argument,
        # a string in the form of comma-separated values
        # in the form "AB5", to represent a track
        # connecting the first town ("A") to the second
        # ("B") with a distance of 5.
        graph = Graph()
        for string in (sys.argv[1].split(", ")):
            graph.add_track(string[0], string[1], int(string[2:]))
        if len(argv) > 2:
            # Determine which function to call based on "option"
            if argv[2] == "path":
                path = argv[3].split("-")
                print distance(graph, path)
            elif argv[2] == "routes":
                routes = argv[3].split("-")
                print numRoutes(graph, routes[0], routes[1], int(routes[2]))
            elif argv[2] == "shortest":
                points = argv[3].split("-")
                print shortestRoute(graph, points[0], points[1])
            else:
                print help_text
        else:
            print help_text

# Calculate the total distance of a path, or 
# return 'NO SUCH ROUTE' if it doesn't exist
def distance(graph, path):
    result = 0
    for town in range(0, len(path) - 1):
        try:
            result += graph.tracks[path[town]][path[town+1]]
        except KeyError as e: # Couldn't find a track in graph.tracks
            return 'NO SUCH ROUTE'
    return result

# Find the number of routes that start at pointA
# and finish at pointB with a maximum total 
# distance of maxdistance.  PointA and PointB
# can be the same point.
def numRoutes(graph, pointA, pointB, maxdistance):
    return pointA

# Find the shortest route in the graph between
# pointA and pointB
def shortestRoute(graph, pointA, pointB):
    return pointA

main(sys.argv)