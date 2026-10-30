import glob, re

for f in glob.glob("**/*.html", recursive=True):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    new_content = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '', content, flags=re.IGNORECASE)
    if new_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Removed robots meta from {f}")
