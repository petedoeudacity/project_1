"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # TODO: What additional auxiliary data structures will be useful?
        
        neo_designations = {}
        
        for neo in neos:
            neo_designations[neo.designation] = neo
            
            
        # You want a list of all close approaches that have the same ._designation, then you can attach these to the relevant NEO attribute based on the designation
            
        # designation is KEY; list of approach objects with that designation is the VALUE
        designation_approach_map = {}
        
        for approach in approaches:
            if approach._designation in designation_approach_map:
                designation_approach_map[approach._designation].append(approach)
                
            else:
                designation_approach_map[approach._designation] = [approach]

        # TODO: Link together the NEOs and their close approaches.
        # going to use the designation_approach_map dictionary above...
        # i.e. each NEO has a designation attribute & we have a dictionary mapping designations to
        # a collection of close approaches, which is what we want!
        
        for neo in self._neos:
            neo.approaches = designation_approach_map[neo.designation]
        
        # linking a NEO object to each close approach based on designation...
        # approach.neo represents each individual approach object's 'neo' attribute
        # 'neo_designations' is a dictionary created just above that maps designations to neo objects
        # 'approach._designation' references the approach object's '._designation' attribute
        
        for approach in approaches:
            approach.neo = neo_designations[approach._designation]
            
    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.
        
        #   Ok, just going to use the method established above
        
        neo_designations = {}
        
        for neo in self._neos:
            neo_designations[neo.designation] = neo
            
        return neo_designations.get(designation)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.
        
        for neo in self._neos:
            if neo.name == name:
                return neo
            
        return None
        
    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        for approach in self._approaches:
            yield approach
