public class Solution {
  public string[] FindRelativeRanks(int[] score) {

    // Create result array with same length as scores
    string[] result = new string[score.Length];

    // Put all scores into a PQ
    // Each value in the PQ is a tuple of (index, score)
    PriorityQueue<int, int> scorePq = new PriorityQueue<int, int>();

    List<(int Index, int Score)> scoreIndices = new List<(int, int)>();

    for (int i = 0; i < score.Length; i++) {
      scoreIndices.Add((i, -score[i]));
    }

    // Bulk add values to PQ
    scorePq.EnqueueRange(scoreIndices);
    
    // Pop from PQ and add to result list
    int place = 1;
    while (scorePq.Count > 0) {
      int index = scorePq.Dequeue();
      string res = "";
      if (place == 1) {
        res = "Gold Medal";
      } else if (place == 2) {
        res = "Silver Medal";
      } else if (place == 3) {
        res = "Bronze Medal";
      } else {
        res = place.ToString();
      }
      result[index] = res;
      place++;
    }

    return result;  
  }
}
