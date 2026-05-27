#day1_log_counter.py
#purpose:count failed login attempts from log file

def count_failed_logins(filename):
  try:
    with open(filename, 'r')as file:
      logs=file.readlines()
      failed_count = 0
      for line in logs:
        if "FAILED" in line:
          failed_count +=1
          print(f"Total log entries: {len(logs)}")
          print(f"Failed login attempts:{failed_count}")
          print("SOC Note: >5 failed logins=Possible brute force.Alert L2.")
  except FileNotFoundError:
    print("Error:Log file not found. Create sample_logs.txt first.")
if __name__ == "__main__":
  count_failed_logins("sample_logs.txt")
