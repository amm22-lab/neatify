import shutil
from pathlib import Path
from datetime import datetime

def organize_downloads():
    downloads_path = Path.home() / "Downloads"

    files_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".csv", ".xlsx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".7z"],
        "Executables": [".exe", ".dmg", ".msi", ".iso", ".pkg"],
        "Songs": [".mp3", ".mp4"],
        "Icons": [".icns"]
    }

    no_year_folders = {"Archives", "Executables", "Songs"}

    for file_path in downloads_path.iterdir():
        if file_path.is_dir() or file_path.name == "organizer.py":
            continue

        extension = file_path.suffix.lower()

        matched_folder = None
        for folder, extensions in files_categories.items():
            if extension in extensions:
                matched_folder = folder
                break

        # If no match, put in Other
        if matched_folder is None:
            matched_folder = "Other"

        if matched_folder in no_year_folders:
            destination_folder = downloads_path / matched_folder
        else:
            stat = file_path.stat()
            created_year = datetime.fromtimestamp(stat.st_birthtime).year
            destination_folder = downloads_path / str(created_year) / matched_folder

        destination_folder.mkdir(parents=True, exist_ok=True)
        destination = destination_folder / file_path.name

        print(f"Moving: {file_path.name} -> {destination_folder.relative_to(downloads_path)}")
        shutil.move(file_path, destination)

if __name__ == "__main__":
    organize_downloads()
