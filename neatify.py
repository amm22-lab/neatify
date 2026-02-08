import shutil
from pathlib import Path

def organize_downloads():
    downloads_path = Path.home() / "Downloads"
    files_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".csv", ".xlsx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".7z"],
        "Executables": [".exe", ".dmg", ".msi", ".iso", ".pkg"],
        "Icons": [".icns"]
    }

    for folder in files_categories:
        (downloads_path / folder).mkdir(exist_ok=True)
    for file_path in downloads_path.iterdir():
        if file_path.is_dir() or file_path.name == "organizer.py":
            continue
        extension = file_path.suffix.lower()
        for folder in files_categories:
            if extension in files_categories[folder]:
                destination = downloads_path / folder / file_path.name
                print(f"Moving: {file_path.name} -> {folder}")
                shutil.move(file_path, destination)
                break

if __name__ == "__main__":
    organize_downloads()