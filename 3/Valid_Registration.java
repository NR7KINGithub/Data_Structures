public class Valid_Registration {
    public static int countDatesInRange(int input1, String[] input2, String input3, String input4) {
        int count = 0;

        String[] startParts = input3.split("-");
        int startDay = Integer.parseInt(startParts[0]);
        int startMonth = Integer.parseInt(startParts[1]);
        int startYear = Integer.parseInt(startParts[2]);

        String[] endParts = input4.split("-");
        int endDay = Integer.parseInt(endParts[0]);
        int endMonth = Integer.parseInt(endParts[1]);
        int endYear = Integer.parseInt(endParts[2]);   
        
        for (String dateStr : input2) {
            String[] dateParts = dateStr.split("-");
            int day = Integer.parseInt(dateParts[0]);
            int month = Integer.parseInt(dateParts[1]);
            int year = Integer.parseInt(dateParts[2]);

            if (year < startYear || year > endYear) {
                continue;
            }

            if (year == startYear) {
                if (month < startMonth) {
                    continue;
                }
                if (month == startMonth && day < startDay) {
                    continue;
                }
            }

            if (year == endYear) {
                if (month > endMonth) {
                    continue;
                }
                if (month == endMonth && day > endDay) {
                    continue;
                }
            }
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int input1 = 6;
        String[] input2 = {"01-01-2023", "10-01-2023", "05-02-2023", "25-12-2022", "03-01-2023", "01-03-2023"};
        String input3 = "01-01-2023";
        String input4 = "31-01-2023";
        System.out.println(countDatesInRange(input1, input2, input3, input4));
    }
}