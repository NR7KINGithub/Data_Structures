public class Playing_With_Geometric_Progression {
    public static double geometricProgression(int a, int r, int n) {
        return a * Math.pow(r, n-1);
    }

    public static void main(String[] args) {
        int a = 2;
        int r = 3;
        int n = 6;
        System.out.println(geometricProgression(a, r, n));
    }
}