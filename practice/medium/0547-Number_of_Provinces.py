class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        1. build adjacency matrix
        2. create a cache of visited cities
        3. do DFS for each node, each DFS iteration is a new province
        4. all nodes touched during DFS will belong to the same province
        """
        
        from collections import defaultdict
        
        # cache to keep track of cities we've counted
        visited = set()
        
        # adjacency graph
        cities = {}
        
        # add cities and neighbors to the adjacency graph
        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):
                if row not in cities:
                    cities[row] = []
                if isConnected[row][col] and row != col:
                    cities[row].append(col)

                    
        # find all cities that belong to this province
        def find_province(city):
            visited.add(city)
            neighbors = cities[city]
            
            if len(neighbors) == 0:
                return
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    find_province(neighbor)
        
        
        # assign a province_id to all cities
        # return the total number of provinces
        province_id = 0
        for city, neighbors in cities.items():
            if city not in visited:
                find_province(city)
                province_id += 1

        return province_id
