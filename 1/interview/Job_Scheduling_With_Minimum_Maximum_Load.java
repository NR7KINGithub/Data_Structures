import java.util.*;

public class Job_Scheduling_With_Minimum_Maximum_Load {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        Integer[] jobs = new Integer[n];
        for (int i = 0; i < n; i++) {
            jobs[i] = sc.nextInt();
        }
        
        int k = sc.nextInt();
        
        // If we have more workers than jobs, each worker gets at most one job
        if (k >= n) {
            int maxJob = 0;
            for (int job : jobs) {
                maxJob = Math.max(maxJob, job);
            }
            System.out.println(maxJob);
            return;
        }
        
        // Sort jobs in descending order (largest jobs first)
        Arrays.sort(jobs, Collections.reverseOrder());
        
        // Min-heap to track the current load of each worker
        PriorityQueue<Integer> workerLoads = new PriorityQueue<>();
        
        // Assign the first k largest jobs to k workers (one job each)
        for (int i = 0; i < k; i++) {
            workerLoads.offer(jobs[i]);
        }
        
        // Assign remaining jobs to the worker with minimum current load
        for (int i = k; i < n; i++) {
            int minLoad = workerLoads.poll(); // Get worker with minimum load
            workerLoads.offer(minLoad + jobs[i]); // Assign job and update load
        }
        
        // Find the maximum load among all workers
        int maxLoad = 0;
        while (!workerLoads.isEmpty()) {
            maxLoad = Math.max(maxLoad, workerLoads.poll());
        }
        
        System.out.println(maxLoad);
        sc.close();
    }
}