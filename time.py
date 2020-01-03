import time
import subprocess

while True:
    subprocess.check_call(['python3', 'imap.py'])
    time.sleep(5 * 60)
