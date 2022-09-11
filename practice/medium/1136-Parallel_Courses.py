class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        prereqs = collections.defaultdict(set)
        dependencies = collections.defaultdict(set)
        can_take = collections.deque()
        taken = set()
        max_sem = 0
        
        # Build 2 graphs, prereqs and dependencies
        for pre, post in relations:
            prereqs[post].add(pre)
            dependencies[pre].add(post)
        
        # Build the initial queue 
        for i in range(1, n+1):
            if len(prereqs[i]) == 0:
                can_take.append([i, 1])
        
        # Keep taking classes while we can
        while can_take:
            pre, sem = can_take.popleft()
            taken.add(pre)
            max_sem = max(max_sem, sem)

            # For each class that depends on the current, remove current from the prereqs
            for post in dependencies[pre]:
                prereqs[post].remove(pre)
                
                # If there are no more prereqs, we can now take the class
                if len(prereqs[post]) == 0:
                    can_take.append([post, sem+1])
            
        if len(taken) == n:
            return max_sem
        else:
            return -1
