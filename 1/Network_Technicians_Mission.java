import java.util.*;

public class Network_Technicians_Mission {
    public static int safeViewPoints(int N, int M, int k, List<Integer> Arr1, List<List<Integer>> Arr2) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (List<Integer> edge : Arr2) {
            int u = edge.get(0);
            int v = edge.get(1);
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        return dfs(1, -1, 0, M, graph, Arr1);
    }

    private static int dfs(int node, int parent, int consHaz, int M, Map<Integer, List<Integer>> graph, List<Integer> Arr1) {
        if (Arr1.get(node - 1) == 1) {
            consHaz++;
        } else {
            consHaz = 0;
        }

        if (consHaz > M) {
            return 0;
        }

        int count = 0;
        boolean isLeaf = true;

        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                isLeaf = false;
                count += dfs(neighbor, node, consHaz, M, graph, Arr1);
            }
        }

        if (isLeaf) {
            return 1;
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = 7, M = 1, K = 6;
        List<Integer> Arr1 = Arrays.asList(1, 0, 1, 1, 0, 0, 0);
        List<List<Integer>> Arr2 = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(1, 3),
            Arrays.asList(2, 4),
            Arrays.asList(2, 5),
            Arrays.asList(3, 6),
            Arrays.asList(3, 7)
        );

        int result = safeViewPoints(N, M, K, Arr1, Arr2);
        System.out.println(result);
        scan.close();   
    }
}