import os


print(os.getenv("SHELL")) # '/bin/bash' (or whatever shell might be used)

# will return None of the env is not there
print(os.getenv("NOT_HERE"))  # None