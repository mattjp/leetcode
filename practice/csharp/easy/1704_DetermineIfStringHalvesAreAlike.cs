public class Solution {
    public bool HalvesAreAlike(string s) {
        int l = s.Length / 2;
        s = s.ToLower();

        string a = s.Substring(0, l);
        string b = s.Substring(l);

        int aCount = 0;
        int bCount = 0;

        HashSet<char> vowels = new HashSet<char>() {
            'a', 'e', 'i', 'o', 'u'
        };

        for (int i = 0; i < l; i++) {
            char u = a[i];
            char w = b[i];
            
            if (vowels.Contains(u)) {
                aCount++;
            }

            if (vowels.Contains(w)) {
                bCount++;
            }
        }

        return aCount == bCount;
    }
}
