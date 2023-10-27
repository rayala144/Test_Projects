import subprocess

# Retrieve Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Retrieve passwords for each profile
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    passwords = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
    
    # Print profile name and password (if available)
    try:
        print("{:<30}|  {:<}".format(profile, passwords[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(profile, ""))

input("End of list...Press ENTER to exit")
