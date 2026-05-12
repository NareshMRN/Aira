import os, sys

key = os.environ.get('GROQ_API_KEY', '').strip()

if not key:
    print("ERROR: GROQ_API_KEY secret is empty or not set!")
    print("Go to: Repo -> Settings -> Secrets -> Actions -> New secret")
    print("Name: GROQ_API_KEY  Value: your gsk_... key")
    sys.exit(1)

if key == '__GROQ_API_KEY__':
    print("ERROR: Key is still the placeholder — secret not set correctly!")
    sys.exit(1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '__GROQ_API_KEY__' not in content:
    print("WARNING: Placeholder not found in index.html — already injected or wrong file?")
    sys.exit(0)

content = content.replace('__GROQ_API_KEY__', key)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"SUCCESS: Key injected ({len(key)} chars, starts with: {key[:8]}...)")
