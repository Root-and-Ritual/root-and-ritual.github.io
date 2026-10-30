import glob, re

for f in glob.glob("**/*.html", recursive=True):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content
    # Remove secret-door pi link
    new_content = re.sub(r'<a\s+class=["\']secret-door["\'][^>]*>.*?</a>', '', new_content, flags=re.DOTALL|re.IGNORECASE)
    # Remove secret-door style
    new_content = re.sub(r'<style>\s*\.secret-door[^<]*</style>', '', new_content, flags=re.DOTALL|re.IGNORECASE)

    if new_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Removed secret door / owner link from {f}")
