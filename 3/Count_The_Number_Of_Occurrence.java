public class Count_The_Number_Of_Occurrence {
    public static int strStr(String haystack, String needle) {
        int index = 0, count = 0;
        while ((index = haystack.indexOf(needle, index)) != -1) {
            count++;
            index++;
        }
        return count;
    }

    public static void main(String[] args) {
        String haystack = "AlwaysJoeinFriendsJoewithJoeJoe";
        String needle  = "Joe";
        System.out.println(strStr(haystack, needle));
    }
}