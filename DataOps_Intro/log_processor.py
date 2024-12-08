from datetime import datetime

# Generate logs
with open('system.log', 'w') as log_file:
    for i in range(10):
        log_level = 'ERROR' if i % 3 == 0 else 'INFO'
        log_message = f"{datetime.now()} {log_level}: Task {i+1} completed successfully\n"
        log_file.write(log_message)

print("Log file 'system.log' generated.")

# Read and filter logs
with open('system.log', 'r') as log_file:
    log_lines = log_file.readlines()

error_lines = [line for line in log_lines if 'ERROR' in line]
print(f"Found {len(error_lines)} error lines.")

# Save filtered logs with a timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
error_filename = f"error_logs_{timestamp}.txt"

with open(error_filename, 'w') as error_file:
    error_file.writelines(error_lines)

print(f"Filtered error logs saved to '{error_filename}'.")
