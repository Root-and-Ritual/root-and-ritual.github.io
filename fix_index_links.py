import glob, re

files = glob.glob("**/*.html", recursive=True)
count = 0
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace href="../index.html" with href="index.html"
    new_content = content.replace('href="../index.html"', 'href="index.html"')

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Fixed ../index.html links in {count} files.")
