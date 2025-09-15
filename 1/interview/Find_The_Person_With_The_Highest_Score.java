import java.util.*;

public class Find_The_Person_With_The_Highest_Score {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // Store all queries in order
        List<Query> queries = new ArrayList<>();
        
        // Calculate final cumulative scores
        Map<String, Integer> finalScores = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int score = sc.nextInt();
            
            queries.add(new Query(name, score));
            finalScores.put(name, finalScores.getOrDefault(name, 0) + score);
        }
        
        // Find the maximum final score
        int maxScore = Integer.MIN_VALUE;
        for (int score : finalScores.values()) {
            maxScore = Math.max(maxScore, score);
        }
        
        // Find all people who achieved the maximum score
        Set<String> winners = new HashSet<>();
        for (Map.Entry<String, Integer> entry : finalScores.entrySet()) {
            if (entry.getValue() == maxScore) {
                winners.add(entry.getKey());
            }
        }
        
        // Replay queries to find who reached max score first
        Map<String, Integer> currentScores = new HashMap<>();
        for (Query query : queries) {
            currentScores.put(query.name, currentScores.getOrDefault(query.name, 0) + query.score);
            
            // Check if this person reached the max score and is a final winner
            if (currentScores.get(query.name) >= maxScore && winners.contains(query.name)) {
                System.out.println(query.name);
                break;
            }
        }
        
        sc.close();
    }
    
    static class Query {
        String name;
        int score;
        
        Query(String name, int score) {
            this.name = name;
            this.score = score;
        }
    }
}