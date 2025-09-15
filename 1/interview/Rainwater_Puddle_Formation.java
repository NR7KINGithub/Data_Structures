import java.util.*;

public class Rainwater_Puddle_Formation {
    
    // Union-Find data structure
    static class UnionFind {
        private int[] parent;
        private int[] rank;
        private int components;
        
        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            components = 0;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }
        
        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]); // Path compression
            }
            return parent[x];
        }
        
        public boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            
            if (rootX == rootY) {
                return false; // Already connected
            }
            
            // Union by rank
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            
            components--; // Two components merged into one
            return true;
        }
        
        public void addComponent() {
            components++;
        }
        
        public int getComponents() {
            return components;
        }
    }
    
    public static List<Integer> numPuddlesAfterRain(int m, int n, int[][] rainEvents) {
        List<Integer> result = new ArrayList<>();
        boolean[][] isWater = new boolean[m][n];
        UnionFind uf = new UnionFind(m * n);
        
        // Directions: up, down, left, right
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (int[] event : rainEvents) {
            int row = event[0];
            int col = event[1];
            
            // Convert 2D coordinate to 1D index
            int currentIndex = row * n + col;
            
            // Mark this cell as water and add as a new component
            isWater[row][col] = true;
            uf.addComponent();
            
            // Check all 4 adjacent cells
            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                
                // Check if the adjacent cell is valid and contains water
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && isWater[newRow][newCol]) {
                    int adjacentIndex = newRow * n + newCol;
                    uf.union(currentIndex, adjacentIndex);
                }
            }
            
            result.add(uf.getComponents());
        }
        
        return result;
    }
    
    // Main method with user input
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter grid dimensions (m n): ");
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        
        System.out.print("Enter number of rain events: ");
        int numEvents = scanner.nextInt();
        
        int[][] rainEvents = new int[numEvents][2];
        System.out.println("Enter rain events (row col):");
        for (int i = 0; i < numEvents; i++) {
            rainEvents[i][0] = scanner.nextInt();
            rainEvents[i][1] = scanner.nextInt();
        }
        
        List<Integer> result = numPuddlesAfterRain(m, n, rainEvents);
        System.out.println("Number of puddles after each rain event: " + result);
        
        scanner.close();
    }
}