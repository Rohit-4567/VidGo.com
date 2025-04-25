import os

# Define the folder structure
folders = [
    "assets",
    "downloads",
    "src",
    "templates"
]

# Create directories
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Directory '{folder}' created")
    else:
        print(f"Directory '{folder}' already exists")

# Create Python files in src directory
src_files = [
    "__init__.py",
    "main.py",
    "instagram.py",
    "facebook.py",
    "youtube.py",
    "utils.py",
    "config.py"
]

templates_files = [
    "index.html"
]

# Create Python files in src
for file in src_files:
    file_path = os.path.join("src", file)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Empty file creation
        print(f"File '{file}' created in 'src' directory")
    else:
        print(f"File '{file}' already exists in 'src' directory")

# Create HTML template files in templates
for file in templates_files:
    file_path = os.path.join("templates", file)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Empty file creation
        print(f"File '{file}' created in 'templates' directory")
    else:
        print(f"File '{file}' already exists in 'templates' directory")

# Create requirements.txt and README.md
if not os.path.exists("requirements.txt"):
    with open("requirements.txt", 'w') as f:
        f.write("requests\nyt-dlp\n")
    print("File 'requirements.txt' created")

if not os.path.exists("README.md"):
    with open("README.md", 'w') as f:
        f.write("# Media Downloader App\n\nThis app allows you to download media from Instagram, Facebook, and YouTube.\n")
    print("File 'README.md' created")

# Create LICENSE file (Optional)
if not os.path.exists("LICENSE"):
    with open("LICENSE", 'w') as f:
        f.write("MIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software...")
    print("File 'LICENSE' created")
