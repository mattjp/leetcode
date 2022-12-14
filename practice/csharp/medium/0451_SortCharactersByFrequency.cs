// using System.Linq;

public class Solution {
    public string FrequencySort(string s) {

        // Get frequency map
        Dictionary<char, int> freqs = s
            .GroupBy(ch => ch)
            .ToDictionary(g => g.Key, g => g.Count());

        // Put map items into priority queue
        // Use negative value as PQ is sorted ascending
        PriorityQueue<char, int> pq = new PriorityQueue<char, int>();
        foreach (KeyValuePair<char, int> f in freqs) {
            pq.Enqueue(f.Key, -f.Value);
        }

        // Pop from PQ until empty
        // Use `out` to pass by value
        string res = "";
        while (pq.TryDequeue(out char ch, out int freq)) {
            string freqCh = new string(ch, -freq);
            res += freqCh;
        }

        return res;
    }
}
