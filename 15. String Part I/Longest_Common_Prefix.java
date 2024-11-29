public class Longest_Common_Prefix {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for(int i = 1; i < strs.length; i++)
        {
            while(strs[i].indexOf(prefix) != 0)
            {
            prefix=prefix.substring(0, prefix.length()-1);
            }
        }
        return prefix;
    }
    public static void main(String[] args) {
        Longest_Common_Prefix ob = new Longest_Common_Prefix();
        String[] strs = {"flower","flow","flight"};
        System.err.println(ob.longestCommonPrefix(strs));
    }
}