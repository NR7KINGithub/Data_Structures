public class Find_The_Index_Of_The_First_Occurence_In_A_String_28 {
    public int strStr(String haystack, String needle) {
        for(int i = 0; ;i++) 
        {
            for(int j = 0; ;j++) 
            {
            if (j == needle.length()) return i;
            if (i+j == haystack.length()) 
            return -1;
            if(needle.charAt(j) != haystack.charAt(i+j)) break;
            }
        }
    }
    public static void main(String[] args) {
        Find_The_Index_Of_The_First_Occurence_In_A_String_28 ob = new Find_The_Index_Of_The_First_Occurence_In_A_String_28();
        System.out.println(ob.strStr("happyandhappy", "happy"));
    }
}