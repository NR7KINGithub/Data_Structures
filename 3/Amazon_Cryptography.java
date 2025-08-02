public class Amazon_Cryptography {
    public static StringBuilder crypto(String num, int key) {
        StringBuilder result = new StringBuilder();
        char[] array = num.toCharArray();

        for (int i = 0; i < array.length; i++) {
            int value = Character.getNumericValue(array[i]) + key;
            
            if (value < 10) {
                result.append(value);
            } else if (value < 36) {
                result.append((char)('A' + value - 10));
            } else {
                result.append((char)('a' + value - 36));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String num = "27691";
        int key = 7;
        System.out.println(crypto(num, key));
    }
}