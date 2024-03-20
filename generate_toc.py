import os
from datetime import datetime


def generate_toc_for_file(filepath, vault_path):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    toc = []
    for line in lines:
        if line.startswith('#'):
            # Adjusting according to Obsidian's TOC syntax
            indent_level = line.count('#') - 1
            title = line.strip('#').strip()
            toc.append(('    ' * indent_level) + '- ' + title)
    return toc


def format_note_name_for_link(note_name):
    # Corrects directory separators for Obsidian's linking syntax without URL encoding spaces
    return note_name.replace(os.sep, '/')


def main(obsidian_vault_path):
    toc = ["# Table of Contents", f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    for root, dirs, files in os.walk(obsidian_vault_path):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, start=obsidian_vault_path)
                note_name = os.path.splitext(relative_path)[0]
                note_toc = generate_toc_for_file(filepath, obsidian_vault_path)
                if note_toc:
                    toc.append(f"## [[{format_note_name_for_link(note_name)}]]")
                    toc.extend(note_toc)
                    toc.append("")  # Add a blank line for better separation

    # Write the TOC to a Markdown file in the vault
    toc_filename = os.path.join(obsidian_vault_path, 'table_of_contents.md')
    with open(toc_filename, 'w', encoding='utf-8') as toc_file:
        toc_file.write('\n'.join(toc))


if __name__ == "__main__":
    obsidian_vault_path = r'C:\Users\brian\OneDrive - gowellbenefits.com\Documents\GitHub\Obsidian'  # Update this path
    main(obsidian_vault_path)
