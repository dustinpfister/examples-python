import subprocess
# set capture_output to True to capture output
r=subprocess.run(['ls', '-l'], capture_output=True)
print(r.stdout)