import sys
from collections import deque
from graph import Graph

# Entrypoint for the different solutions.
# Constructs the graph and decides which solution
# to employ
def main(argv):
    help_text = """The way to use the trains function is to give it 3 values: trains(graph, option, input)
graph  : a single string of comma-separated tracks.  eg "AB5, BC7, CA2"
option : either "path", "routes", or "shortest"
input  : for path, dash-separated towns, eg "A-B-C"
         for routesMax, the two towns to find routes between, and a maximum # of hops, dash-separated, eg. "C-C-3"
         for routesExactly, the two towns to find routes between, and an exact # of hops, dash-separated, eg. "A-C-4"
         for routesMaxDistance, the two towns to find routes between, and a maximum distance, dash-separated, eg. "A-D-20"
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
            elif argv[2] == "routesMax":
                routes = argv[3].split("-")
                print routesMax(graph, routes[0], routes[1], int(routes[2]))
            elif argv[2] == "routesExactly":
                routes = argv[3].split("-")
                print routesExactly(graph, routes[0], routes[1], int(routes[2]))
            elif argv[2] == "routesMaxDistance":
                routes = argv[3].split("-")
                print routesMaxDistance(graph, routes[0], routes[1], int(routes[2]))
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
# and finish at pointB with a maximum number of 
# intermediary towns equal to hops.  PointA and PointB
# can be the same point.
def routesMax(graph, pointA, pointB, hops):
    routes = []
    queue  = deque()
    queue.append([pointA])
    while len(queue) > 0:
        path = queue.popleft()
        for neighbour in graph.tracks[path[-1]]:
            newPath = path + [neighbour]
            if neighbour == pointB:
                routes.append(newPath)
            if len(newPath) > hops:
                continue
            queue.append(newPath)
    return len(routes)

# Find the number of routes that start at pointA
# and finish at pointB with exactly "hops"
# many steps.  PointA and pointB can be the 
# same point.
def routesExactly(graph, pointA, pointB, hops):
    routes = []
    queue  = deque()
    queue.append([pointA])
    while len(queue) > 0:
        path = queue.popleft()
        for neighbour in graph.tracks[path[-1]]:
            newPath = path + [neighbour]
            if neighbour == pointB and len(newPath) == hops + 1:
                routes.append(newPath)
            if len(newPath) > hops:
                continue
            queue.append(newPath)
    return len(routes)

## Find the number of routes that start at pointA
# and finish at pointB with a total maximum distance of 
# maxdistance.  PointA and PointB
# can be the same point.
def routesMaxDistance(graph, pointA, pointB, maxdistance):
    routes = []
    queue  = deque()
    queue.append( ([pointA], 0) )
    while len(queue) > 0:
        (path, currentDistance) = queue.popleft()
        for neighbour, distance in graph.tracks[path[-1]].iteritems():
            newPath = path + [neighbour]
            newDistance = currentDistance + distance
            if neighbour == pointB and newDistance < maxdistance:
                routes.append( (newPath, newDistance) )
            if newDistance > maxdistance:
                continue
            queue.append( (newPath, newDistance) )
    return len(routes)

# Find the shortest route in the graph between
# pointA and pointB.  This is an adaptation of 
# Dijkstra's shortest path algorithm.
def shortestRoute(graph, pointA, pointB):
    unvisited = {node: None for node in graph.towns} # using None as +inf
    visited = {}
    current = pointA
    currentDistance = 0
    unvisited[current] = currentDistance
    # Loop through until there are no unvisited towns
    while True:
        for neighbour, distance in graph.tracks[current].iteritems():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
            if neighbour == pointB:
                return newDistance
        # If this is the first time through the loop,
        # we weight the first point's distance as +inf,
        # so that future neighbours will re-weigh it
        # if/when they get back to it.  This only matters
        # for the case where pointA == pointB.
        if currentDistance == 0: # First time through
            visited[pointA] = None
        else:
            # Move current from unvisited to visited
            visited[current] = currentDistance
            del unvisited[current]
        candidates = [town for town in unvisited.iteritems() if town[1]] # If distance isn't +inf
        # If there are no candidates connected to the current node, break out
        if not candidates:
            break
        # sort by distance, move to the next (closest) neighbour
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return 'NO SUCH ROUTE'

main(sys.argv)