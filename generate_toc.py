import os
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions.toc import TocExtension


class TocGenerator(Treeprocessor):
    def run(self, root):
        headings = []
        for element in root:
            if element.tag in ['h1', 'h2', 'h3']:  # Adjust heading levels as needed
                headings.append({'level': int(element.tag[1]), 'text': element.text, 'id': element.get('id')})
        return headings


def generate_toc_for_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        md = markdown.Markdown(extensions=[TocExtension()])
        md.treeprocessors.register(TocGenerator(md), 'toc_generator', 10)
        headings = md.convert(text)
        return md.treeprocessors['toc_generator'].run(md.parser.root)


def main(obsidian_vault_path):
    toc = []
    for root, dirs, files in os.walk(obsidian_vault_path):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                headings = generate_toc_for_file(filepath)
                if headings:
                    toc.append({'file': filepath, 'headings': headings})

    # Print or save the TOC
    for entry in toc:
        print(f"File: {entry['file']}")
        for heading in entry['headings']:
            print(f"  {'#' * heading['level']} {heading['text']}")


if __name__ == "__main__":
    obsidian_vault_path = r'C:\Users\brian\OneDrive - gowellbenefits.com\Documents\GitHub\Obsidian'  # Update this path
    main(obsidian_vault_path)
