using System.Linq;

public class Solution {
  public string ReverseWords(string s) {
    // Split string into words at space character
    List<string> words = s.Split(" ").ToList();

    // Remove words that are only space characters
    words = words.Where((string w) => w != "").ToList();

    // Reverse the array
    words.Reverse();
    
    // Nifty: words.ForEach(Console.WriteLine);
    return String.Join(" ", words);
  }
}
