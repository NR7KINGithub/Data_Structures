public class Count_Element_Of_String {
    public static void count(String x) {
        char[] ch = x.toCharArray();
        int letter = 0, num = 0, space = 0, special = 0;

        for (int i = 0; i < x.length(); i++) {

            if (Character.isLetter(ch[i])) {
                letter++;
            }
            else if (Character.isDigit(ch[i])) {
                num++;
            }
            else if (Character.isSpaceChar(ch[i])) {
                space++;
            }
            else {
                special++;
            }
        }

        System.out.println("Alphabets: " +letter);
        System.out.println("Digits: " +num);
        System.out.println("Whitespaces: " +space);
        System.out.println("Special Characters: " +special);
    }

    public static void main(String[] args) {
        String x = "Amcatuff@ #% 123";
        count(x);
    }
}