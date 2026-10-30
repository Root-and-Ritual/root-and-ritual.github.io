import re

f = 'index.html'
with open(f, 'r', encoding='utf-8') as file:
    content = file.read()

# Replace form with welcome paragraph and Enter button/link to root-and-ritual.html
new_form_html = '''<div class="gate-actions" style="margin: 30px 0;"><a class="button" href="root-and-ritual.html">Enter Root &amp; Ritual →</a></div>'''

# We can replace from <form class="gate-form"...</form> with the action link
new_content = re.sub(r'<form class="gate-form".*?</form>', new_form_html, content, flags=re.DOTALL)
# Also remove assets/gate.js script tag since form handling is no longer needed
new_content = re.sub(r'<script src="assets/gate\.js"></script>', '', new_content)

with open(f, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("Successfully updated index.html to be a locked door / welcome page linking to root-and-ritual.html")
