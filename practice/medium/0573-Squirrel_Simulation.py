class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """
        1. have squirrel go to closest nut
            squirrel should go to a nut that is closer to the squirrel than the tree
        2. have squerrel go to tree
        3. repeat until no more nuts
        """
        
        # for each nut, calculate dist to tree, dist to squirrel
        # if squirrel-nut dist < tree-nut dist, save this as the optimal nut
        def optimal_nut(t, s, nuts):
            dist = row = col = None
            for nut_row, nut_col in nuts:
                squirrel_dist = abs(nut_row - s[0]) + abs(nut_col - s[1])
                tree_dist = abs(nut_row - t[0]) + abs(nut_col - t[1])
                if squirrel_dist <= tree_dist or not dist:
                    if dist:
                        if tree_dist - squirrel_dist > dist:
                            dist = tree_dist - squirrel_dist
                            row = nut_row
                            col = nut_col
                    else:
                        dist = tree_dist - squirrel_dist
                        row = nut_row
                        col = nut_col
            return row, col
                    
        
        
        # this is dumb and could just be sorting (same time complexity)
        def closest_nuts(row, col, nuts):
            result = []
            for nut_row, nut_col in nuts:
                dist = abs(row - nut_row) + abs(col - nut_col)
                result.append((dist, nut_row, nut_col))
            
            heapq.heapify(result)  # O(n)
            return result
        
        
        total_dist = 0
        
        # 1. have squirrel go to closest nut
        opt_nut_row, opt_nut_col = optimal_nut(tree, squirrel, nuts)
        opt_nut_dist = abs(opt_nut_row - squirrel[0]) + abs(opt_nut_col - squirrel[1])
        total_dist += opt_nut_dist
        
        # 2. have squirrel go to tree
        tree_dist = abs(opt_nut_row - tree[0]) + abs(opt_nut_col - tree[1])
        total_dist += tree_dist

        # 3. collect all nuts
        remaining_nuts = closest_nuts(tree[0], tree[1], nuts)
        while remaining_nuts:
            dist, row, col = heapq.heappop(remaining_nuts)
            if (row, col) == (opt_nut_row, opt_nut_col):
                continue
            total_dist += dist * 2
            
        return total_dist
