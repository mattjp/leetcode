public class Solution {
  public string MakeGood(string s) {

    Stack<char> stack = new Stack<char>();

    foreach (char c in s) {

      if (stack.Count > 0 &&
          stack.Peek() != c &&
          (stack.Peek() == Char.ToUpper(c) || 
           stack.Peek() == Char.ToLower(c))) {

          stack.Pop();
      } else {
          stack.Push(c);
      }

    }
    
    char[] cs = stack.ToArray();
    Array.Reverse(cs);
    return new String(cs);

  }
}
