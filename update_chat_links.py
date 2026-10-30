import glob, os, re

files = glob.glob("**/*.html", recursive=True)
count = 0
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace href="chat/" or href="/chat/" with coming soon or disabled state / note
    # The prompt says: "the AI Chat link (chat/) needs a server: replace it with a 'coming soon' note"
    # Let's check how AI Chat link appears in navigation: <a href="chat/">AI Chat</a>
    new_content = re.sub(r'<a\s+href=["\'](?:/)?chat/["\'][^>]*>AI Chat</a>', '<span style="color:var(--muted); font-size:11px; font-family:monospace; letter-spacing:1px; text-transform:uppercase; cursor:not-allowed;" title="AI Chat requires a backend server — coming soon">AI Chat (Soon)</span>', content)

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Updated AI Chat link in {count} files.")
