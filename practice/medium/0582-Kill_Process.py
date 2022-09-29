class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        1. Build graph of parent -> child 
        2. Given the target process, kill it and all child processes (BFS)
        """
        
        graph = collections.defaultdict(set)
        for process, parent in zip(pid, ppid):
            graph[parent].add(process)        
        
        ans = []
        to_kill = collections.deque([kill])
        
        while to_kill:
            target = to_kill.popleft()
            ans.append(target)
            for child in graph[target]:
                to_kill.append(child)
                
        return ans
