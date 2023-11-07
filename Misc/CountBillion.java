public class CountBillion {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        long k = 0;
        // Count to 1 billion
        for (double i = 0; i < 1000000000; i++) {
            // Do nothing
            k = k + 1;
        }
        System.out.println(k);
        long endTime = System.currentTimeMillis();
        long timeTaken = endTime - startTime;

        System.out.println("Time taken to count to 1 billion: " + timeTaken + " ms");
    }
}
