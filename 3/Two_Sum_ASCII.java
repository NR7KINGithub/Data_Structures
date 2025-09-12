public class Two_Sum_ASCII {
    public static String sum(String input1, int input2, int input3) {
        input1  = input1.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(" ", "");
        String[] symbols = input1.split(",");
        String result = "-1";

        for (int i = 0; i < input2; i++) {
            for (int j = i + 1; j < input2; j++) {
                int sum = symbols[i].charAt(0)+ symbols[j].charAt(0);

                if (sum == input3) {
                    result = symbols[i] + symbols[j];
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String input1 = "[e, b, c, d]";
        int input2 = 4;
        int input3 = 199;
        System.out.println(sum(input1, input2, input3));
    }
}