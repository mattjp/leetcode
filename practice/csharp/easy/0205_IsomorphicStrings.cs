public class Solution {

  public bool IsIsomorphic(string s, string t) {
    
    Dictionary<char, char> sDict = new Dictionary<char, char>();
    Dictionary<char, char> tDict = new Dictionary<char, char>();
    
    if (s.Length != t.Length) {
      return false;
    }
    
    for (int i = 0; i < s.Length; i++) {
      char sChar = s[i];
      char tChar = t[i];
      
      if (sDict.ContainsKey(sChar)) {
        if (sDict[sChar] != tChar) {
          return false;
        }
      } else {
        sDict[sChar] = tChar;
      }
      
      if (tDict.ContainsKey(tChar)) {
        if (tDict[tChar] != sChar) {
          return false;
        }
      } else {
        tDict[tChar] = sChar;
      }
      
    }
    
    return true;
  }
}
