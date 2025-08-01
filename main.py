import subprocess

if __name__ == "__main__":
    subprocess.run(["python", "user/user_input.py"])
    subprocess.run(["python", "agent/agent_tfidf.py"])
    subprocess.run(["python", "log/log.py"])
