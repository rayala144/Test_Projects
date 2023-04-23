public class CountBillion {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        // Count to 1 billion
        for (int i = 0; i < 1000000000; i++) {
            // Do nothing
        }

        long endTime = System.currentTimeMillis();
        long timeTaken = endTime - startTime;

        System.out.println("Time taken to count to 1 billion: " + timeTaken + " ms");
    }
}
