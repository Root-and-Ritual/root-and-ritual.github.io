import os

# Create .nojekyll file at repo root
with open(".nojekyll", "w", encoding="utf-8") as f:
    f.write("")

print("Created .nojekyll successfully.")
