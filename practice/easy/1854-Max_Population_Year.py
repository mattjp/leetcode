class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        from collections import defaultdict
        
        population = defaultdict(int)
        
        for birth, death in logs:
            for year in range(birth, death):
                population[year] += 1
                
        sorted_population = sorted(population.items(), key=lambda i: (-i[1], i[0]))
        return sorted_population[0][0]
