import os
import random
import string


def generate_random_number(length=7):
    return "".join(random.choices(string.digits, k=length))


def rename_photos_in_directory(directory):
    directory = os.path.expanduser(directory)
    directory = os.path.abspath(directory)

    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".mp4"]:
                new_name = generate_random_number() + file_ext
                new_path = os.path.join(directory, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed {filename} to {new_name}")


if __name__ == "__main__":
    directory = input(
        "Enter the directory path : "
    )
    rename_photos_in_directory(directory)
