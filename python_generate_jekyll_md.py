# generate_jekyll_md.py
import os

def generate_md_files(subject_name, pdf_folder_path, md_collection_path):
    """
    Scans a folder for PDF files and generates corresponding Markdown files
    with Jekyll front matter in a specified collection folder.

    Args:
        subject_name (str): The name of the subject (e.g., "Geometry", "Algebra").
        pdf_folder_path (str): The path to the folder containing PDF files for the subject.
        md_collection_path (str): The path to the Jekyll collection folder
                                  (e.g., '_geometry_resources').
    """
    # Ensure the Markdown collection folder exists
    os.makedirs(md_collection_path, exist_ok=True)

    print(f"\n--- Processing {subject_name} Resources ---")
    print(f"Scanning for PDFs in: {pdf_folder_path}")
    print(f"Generating MD files in: {md_collection_path}")

    for filename in os.listdir(pdf_folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_name_without_ext = os.path.splitext(filename)[0]
            # Convert filename to a URL-friendly slug for the MD file name
            md_filename_slug = pdf_name_without_ext.replace(' ', '-').replace('_', '-').lower()
            md_filename = os.path.join(md_collection_path, f"{md_filename_slug}.md")

            # Create a placeholder title and description
            # You will edit these manually later
            title = f"{subject_name} Resource: {pdf_name_without_ext.replace('-', ' ').title()}"
            description = f"A description for this {subject_name.lower()} resource."

            # Jekyll Front Matter content
            md_content = f"""---
title: {title}
description: {description}
file_name: {filename}
---
"""
            # Write the Markdown file
            with open(md_filename, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"Generated: {md_filename}")

    print(f"--- {subject_name} Generation Complete! ---")
    print("Remember to review and update the 'title' and 'description' in each generated Markdown file.")
    print(f"Also, ensure your PDFs are in 'resources/{subject_name.lower().replace(' ', '-')}/' and commit all changes to GitHub.")

if __name__ == "__main__":
    # Define your subjects and their corresponding folder names
    # The key is the display name, the value is the folder name (lowercase, hyphenated)
    subjects = {
        "Algebra": "algebra",
        "Geometry": "geometry",
        "Combinatorics": "combinatorics",
        "Number Theory": "number-theory",
        "Miscellaneous": "miscellaneous",
        "My Handouts": "myhandouts"
    }

    # Get the current working directory (where your script is)
    base_dir = os.getcwd()

    for display_name, folder_name in subjects.items():
        pdf_folder_path = os.path.join(base_dir, 'resources', folder_name)
        md_collection_path = os.path.join(base_dir, f'_{folder_name}_resources')

        # Run the script for each subject
        generate_md_files(display_name, pdf_folder_path, md_collection_path)

    print("\nAll resource Markdown files have been generated.")
    print("Don't forget to: ")
    print("1. Manually review and refine the 'title' and 'description' in each .md file.")
    print("2. Ensure all your actual PDF files are correctly placed in their respective 'resources/subject-name/' folders.")
    print("3. Commit and push all changes (new .md files, updated PDFs) to your GitHub repository.")
