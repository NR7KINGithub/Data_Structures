public class Phone_Number_Validity {
    public static boolean isValidPhoneNumber(String phoneNumber) {
        String phone = phoneNumber.replace(" ", "")
                                  .replace("\t", "")
                                  .replace("\n", "")
                                  .replace("\r", "");

        if (phone.startsWith("+91")) {
            phone = phone.substring(3);
        } else if (phone.startsWith("0")) {
            phone = phone.substring(1);
        }

        if (phone.length() != 10) {
            return false;
        }

        char first = phone.charAt(0);
        if (first < '1' || first > '9') {
            return false;
        }

        for (int i = 1; i < 10; i++) {
            char c = phone.charAt(i);
            if (c < '0' || c > '9') {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String phoneNumber = "+91 1234567890";
        System.out.println(isValidPhoneNumber(phoneNumber));
    }
}