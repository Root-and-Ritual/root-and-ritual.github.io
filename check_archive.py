import json
with open('assets/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.ARCHIVE = '
assert content.startswith(prefix)
json_str = content[len(prefix):].rstrip(';\n')
data = json.loads(json_str)
print('Count before:', len(data))
print('Sample item keys:', list(data[0].keys()) if data else [])
print('Sample item:', data[0])
