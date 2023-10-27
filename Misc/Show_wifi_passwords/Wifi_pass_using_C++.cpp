#include <iostream>
#include <string>
#include <vector>
#include <windows.h>
#include <sstream>
#include <iomanip>

std::vector<std::string> executeCommand(const std::string &command)
{
    std::vector<std::string> outputLines;
    char buffer[128];
    FILE *pipe = _popen(command.c_str(), "r");
    if (pipe)
    {
        while (fgets(buffer, sizeof(buffer), pipe) != nullptr)
        {
            outputLines.push_back(buffer);
        }
        _pclose(pipe);
    }
    return outputLines;
}

int main()
{
    std::vector<std::string> data = executeCommand("netsh wlan show profiles");
    std::vector<std::string> profiles;

    for (const auto &line : data)
    {
        if (line.find("All User Profile") != std::string::npos)
        {
            size_t startPos = line.find(":") + 2;
            size_t endPos = line.size() - 1;
            profiles.push_back(line.substr(startPos, endPos - startPos));
        }
    }

    for (const auto &profile : profiles)
    {
        std::vector<std::string> profileData = executeCommand("netsh wlan show profile " + profile + " key=clear");
        std::string password;

        for (const auto &line : profileData)
        {
            if (line.find("Key Content") != std::string::npos)
            {
                size_t startPos = line.find(":") + 2;
                size_t endPos = line.size() - 1;
                password = line.substr(startPos, endPos - startPos);
                break;
            }
        }

        std::cout << std::left << std::setw(30) << profile << "|  " << password << std::endl;
    }

    std::cout << "End of list...Press ENTER to exit" << std::endl;
    std::cin.ignore();

    return 0;
}
