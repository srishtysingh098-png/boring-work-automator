import os
from collections import Counter


def generate_report():
    folder = input("Enter the folder path: ")

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

    extensions = []

    for file in files:
        extension = os.path.splitext(file)[1].lower()

        if extension:
            extensions.append(extension)
        else:
            extensions.append("No Extension")

    report = Counter(extensions)

    print("\n===== FILE REPORT =====")
    print(f"Total files: {len(files)}")

    for extension, count in report.items():
        print(f"{extension}: {count}")

    print("=======================")


if __name__ == "__main__":
    generate_report()
