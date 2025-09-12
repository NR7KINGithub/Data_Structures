public class Work_Area_With_Adjacent_Cafeteria {
    public static int countWorkArea(int N, int M, String[] grid) {
        int count = 0;
        int[][] directions = { 
            {-1, 0}, // Up
            {1, 0}, // Down
            {0, -1}, // Left
            {0, 1} // Right
        };

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(grid[i].charAt(j) == 'W') {
                    boolean isIsolated = true;
                    
                    for (int[] dir : directions) {
                        int ni = i + dir[0];
                        int nj = j + dir[1];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
                            if (grid[ni].charAt(nj) == 'C') {
                                isIsolated = false;
                                break;
                            }
                        }
                    }

                    if (isIsolated) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int N = 4;
        int M = 5;
        String[] grid = {"W0C0W", "0CC00", "W00CW", "C0W0C"};
        System.out.println(countWorkArea(N, M, grid));
    }
}