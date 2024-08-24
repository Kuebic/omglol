import os

# Define the paths
base_path = 'weblog/songs'
pages_path = 'weblog/pages'
songs_md_path = os.path.join(pages_path, 'songs.md')

# Helper function to extract metadata from a file
def extract_metadata(file_path):
    title, location = None, None
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('Title:'):
                title = line.split(':', 1)[1].strip()
            elif line.startswith('Location:'):
                location = line.split(':', 1)[1].strip()
            if title and location:
                break

    # Detailed logging if metadata is missing
    if not title or not location:
        if not title:
            print(f"Warning: 'Title' metadata missing in {file_path}")
        if not location:
            print(f"Warning: 'Location' metadata missing in {file_path}")

    return title, location

# Create the main songs.md file
with open(songs_md_path, 'w') as songs_md:
    # Writing header for the songs.md file
    songs_md.write("""---
Type: Page
Title: Songs
Location: /songs
---

## Songs
""")

    # Iterate over folders in the 'songs' directory
    for folder_name in sorted(os.listdir(base_path)):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            # Convert folder name to a reader-friendly format
            folder_name_readable = folder_name.replace('-', ' ').title()

            # Create a heading link for each folder in songs.md
            link = f"/songs/{folder_name.replace('_', '-')}"
            songs_md.write(f"#### [{folder_name_readable}]({link})\n")

            # Generate a new file name with the "songs_-_" prefix
            folder_md_filename = f"songs_-_{folder_name}.md"
            folder_md_path = os.path.join(pages_path, folder_md_filename)

            # Create or overwrite the markdown file for the folder
            with open(folder_md_path, 'w') as folder_md:
                folder_md.write(f"""---
Type: Page
Title: Songs - {folder_name_readable}
Location: /songs/{folder_name}
---

## [Songs](/songs) - {folder_name_readable}
""")

                # Flag to check if any songs were added
                songs_added = False

                # Iterate over files in the folder and add links to the markdown file
                for sub_folder_name in sorted(os.listdir(folder_path)):
                    sub_folder_path = os.path.join(folder_path, sub_folder_name)
                    if sub_folder_name.endswith('.md'):
                        title, location = extract_metadata(sub_folder_path)
                        if title and location:
                            folder_md.write(f"#### [{title}]({location})\n")
                            songs_added = True

                # If no songs were added, provide a message
                if not songs_added:
                    folder_md.write("\nNo songs available in this category.\n")
                    print(f"No valid songs found in folder: {folder_path}")

print("Markdown files have been generated successfully.")
