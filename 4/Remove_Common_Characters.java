public class Remove_Common_Characters {
    public static String common(String A, String B) {
        StringBuilder result = new StringBuilder();

        for (char ch : A.toCharArray()) {
            if (B.indexOf(ch) == -1) {
                result.append(ch);
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String A = "Tiger";
        String B = "Ti";
        System.out.println(common(A, B));
    }
}