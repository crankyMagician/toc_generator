# Obsidian Vault Table of Contents Generator 🗂️

This Python script automatically generates a table of contents (TOC) 📑 for all Markdown notes within an Obsidian vault. The TOC is created as a Markdown file named `table_of_contents.md`, which includes links to each note and lists headings within each note for easy navigation 🧭.

## Features ✨

- **Automatic TOC Generation:** Scans all Markdown files in the specified Obsidian vault and generates a TOC 🔄.
- **Obsidian Link Format:** Uses Obsidian's internal linking syntax to create clickable links directly in the Obsidian app 🔗.
- **Date and Time Stamp:** Includes the generation date and time at the top of the TOC for reference 📅.
- **Improved Formatting:** Organizes notes and headings in a hierarchical structure for better readability 📖.

## How It Works 🛠️

The script reads through each Markdown file in the specified Obsidian vault, extracting headings to create a structured TOC. It then formats these headings according to their level (e.g., `#`, `##`) and includes a link to each note using the `[[Note Name]]` syntax supported by Obsidian. The generated TOC is saved as a Markdown file in the root of the Obsidian vault.

## How to Use 🚀

1. **Prepare Your Environment:** Ensure you have Python installed on your computer. This script was developed with Python 3.x 🐍.

2. **Download the Script:** Save the script to a location on your computer 💾.

3. **Configure the Script:** Edit the script to set the `obsidian_vault_path` variable to the path of your Obsidian vault 📁.

    ```python
    obsidian_vault_path = r'path\to\your\obsidian\vault'
    ```

4. **Run the Script:** Open a terminal or command prompt, navigate to the folder containing the script, and run 🖥️:

    ```bash
    python generate_toc.py
    ```

5. **Check the Output:** Open your Obsidian vault and look for the `table_of_contents.md` file. Click on the links to navigate through your notes 📚.

## Customization 🛠

You can customize the script to change the output filename, adjust which headings are included in the TOC, or modify the link format to suit your needs 🎨.

## Contributing 💡

Contributions to improve the script or add new features are welcome. Please feel free to fork the repository, make your changes, and submit a pull request 🤝.

## License 📜

This project is open-source and available under the MIT License.
