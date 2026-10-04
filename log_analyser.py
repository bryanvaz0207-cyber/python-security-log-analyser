def read_file():
    file = open("login_events.txt", "r")
    lines = file.readlines()
    file.close()

    return lines


def count_logins(lines):
    success = 0
    failed = 0
    failed_ips = {}
    invalid_lines = 0

    for line in lines:
        parts = line.strip().split()

        if len(parts) != 5:
            invalid_lines = invalid_lines + 1
        else:
            result = parts[3]
            ip = parts[4]

            if result == "SUCCESS":
                success = success + 1

            if result == "FAILED":
                failed = failed + 1

                if ip not in failed_ips:
                    failed_ips[ip] = 0

                failed_ips[ip] = failed_ips[ip] + 1

    return success, failed, failed_ips, invalid_lines


lines = read_file()

success, failed, failed_ips, invalid_lines = count_logins(lines)

print("SECURITY LOG REPORT")
print("-------------------")
print("Successful logins:", success)
print("Failed logins:", failed)
print("Invalid lines:", invalid_lines)

print("\nFailed logins by IP:")

for ip in failed_ips:
    print(ip, failed_ips[ip])

print("\nSuspicious IPs:")

for ip in failed_ips:
    if failed_ips[ip] >= 3:
        print(ip, "had", failed_ips[ip], "failed attempts")