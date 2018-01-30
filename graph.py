from collections import defaultdict

class Graph(object):
    """A Graph class that represents a map of towns with tracks that connect them"""
    def __init__(self, towns, tracks):
        self.towns  = set(towns)
        self.tracks = defaultdict(lambda: {}, tracks)
    
    def __init__(self):
        self.towns  = set()
        self.tracks = defaultdict(lambda: {})
    
    def add_town(self, town):
        self.towns.add(town)
    
    def add_track(self, townA, townB, distance):
        # If either of the towns don't exist in the
        # towns set, add them in!  Sets have very
        # quick lookup times in python, average O(1),
        # so this isn't costing us much.
        if townA not in self.towns:
            self.add_town(townA)
        if townB not in self.towns:
            self.add_town(townB)
        # Update the track from townA to townB
        self.tracks[townA].update({townB: distance})
