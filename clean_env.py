import os

def clean_env():
    env_path = ".env"
    if not os.path.exists(env_path):
        print(".env not found")
        return

    with open(env_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            # Remove quotes, trailing spaces, and escaped newlines
            value = value.strip().strip('"').strip("'")
            value = value.replace("\\r", "").replace("\\n", "").strip()
            cleaned_lines.append(f"{key}={value}\n")
        else:
            cleaned_lines.append(line)

    with open(env_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)
    print("Cleaned .env")

if __name__ == "__main__":
    clean_env()
