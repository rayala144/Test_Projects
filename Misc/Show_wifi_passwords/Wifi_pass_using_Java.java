import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class Wifi_pass_using_Java {
    public static void main(String[] args) {
        try {
            List<String> command = new ArrayList<>();
            command.add("netsh");
            command.add("wlan");
            command.add("show");
            command.add("profiles");

            ProcessBuilder processBuilder = new ProcessBuilder(command);
            Process process = processBuilder.start();

            // Read the output of the command
            List<String> outputLines = readOutput(process.getInputStream());

            List<String> profiles = new ArrayList<>();
            for (String line : outputLines) {
                if (line.contains("All User Profile")) {
                    profiles.add(line.split(":")[1].trim());
                }
            }

            for (String profile : profiles) {
                List<String> profileCommand = new ArrayList<>();
                profileCommand.add("netsh");
                profileCommand.add("wlan");
                profileCommand.add("show");
                profileCommand.add("profile");
                profileCommand.add(profile);
                profileCommand.add("key=clear");

                ProcessBuilder profileProcessBuilder = new ProcessBuilder(profileCommand);
                Process profileProcess = profileProcessBuilder.start();

                // Read the output of the profile command
                List<String> profileOutputLines = readOutput(profileProcess.getInputStream());

                List<String> results = new ArrayList<>();
                for (String line : profileOutputLines) {
                    if (line.contains("Key Content")) {
                        results.add(line.split(":")[1].trim());
                    }
                }

                String password = results.isEmpty() ? "" : results.get(0);
                System.out.printf("%-30s|  %s%n", profile, password);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("End of list...Press ENTER to exit");
        try {
            System.in.read();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static List<String> readOutput(InputStream inputStream) throws IOException {
        List<String> outputLines = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                outputLines.add(line);
            }
        }
        return outputLines;
    }
}
