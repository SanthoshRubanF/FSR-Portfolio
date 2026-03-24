import fitz
import json
doc = fitz.open('d:/Portfolio/FSR-Portfolio/resume.pdf')
links = []
count = 1
for p in range(len(doc)):
    page = doc[p]
    for link in page.get_links():
        if 'uri' in link:
            rect = link['from']
            text = page.get_text('text', clip=rect).strip().replace('\n', ' ')
            uri = link['uri']
            links.append({'id': count, 'text': text, 'url': uri})
            count += 1
with open('d:/Portfolio/FSR-Portfolio/links.json', 'w') as f:
    json.dump(links, f, indent=2)
