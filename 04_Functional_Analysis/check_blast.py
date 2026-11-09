import os

blastn_path = "/opt/anaconda3/envs/prokka_env/bin/blastn"

if os.path.exists(blastn_path):
    print("BLASTn is installed.")
    print("Location:", blastn_path)
else:
    print("BLASTn executable not found at this location.")