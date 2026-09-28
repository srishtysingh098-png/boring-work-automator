import os
import shutil


def organize_files():
    folder = input("Enter the folder path to organize: ")

    if not os.path.exists(folder):
        print("Folder not found!")
        return

    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "PDFs": [".pdf"],
        "Documents": [".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Excel": [".xls", ".xlsx", ".csv"]
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()

            for category, extensions in file_categories.items():
                if extension in extensions:
                    category_folder = os.path.join(folder, category)

                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(category_folder, file)
                    )

                    print(f"Moved {file} → {category}")
                    break

    print("File organization completed!")


if __name__ == "__main__":
    organize_files()
