class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        "root/a 1.txt(abcd) 2.txt(efgh)"
         ^      ^    ^
         |      |    L______
         path   |           |
                filename    |
                            content
        
        0. Content cannot have spaces, parentheses, slashes, or periods
        1. Content will always be contained by parentheses
        2. Files will be separated by 1 space
        """
        
        # Map content to list of [path + filename]
        cache = collections.defaultdict(list)
        
        for entry in paths:
            path, files = entry.split(' ', 1)
            files = files.split(' ')
            
            for file in files:
                # Drop the parentheses
                name, content = file[:-1].split('(')
                # Cache content -> full file path
                cache[content].append(f"{path}/{name}")
        
        # Only return cache hits with duplicates 
        return [vals for vals in cache.values() if len(vals) > 1]
