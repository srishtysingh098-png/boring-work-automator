import os


def rename_files():
    folder = input("Enter the folder path: ")
    prefix = input("Enter the new name/prefix: ")

    if not os.path.exists(folder):
        print("Folder not found!")
        return

    files = [
        file for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file))
    ]

    if not files:
        print("No files found!")
        return

    for number, file in enumerate(files, start=1):
        old_path = os.path.join(folder, file)

        extension = os.path.splitext(file)[1]

        new_name = f"{prefix}_{number}{extension}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

        print(f"{file} → {new_name}")

    print("Files renamed successfully!")


if __name__ == "__main__":
    rename_files()
