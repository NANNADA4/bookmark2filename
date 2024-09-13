import fitz
import os


def extract_bookmark_title(file_path):
    doc = fitz.open(file_path)
    bookmarks = doc.get_toc()
    doc.close()
    if bookmarks:
        return bookmarks[0][1]
    return None


def process_pdf_file(file_path):
    bookmark_title = extract_bookmark_title(file_path)
    if bookmark_title:
        base, ext = os.path.splitext(file_path)
        new_file_name = f"{bookmark_title}{ext}"
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_path}' to '{new_file_path}'")
    else:
        print(f"No bookmarks found in '{file_path}'")


def rename_pdfs_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                process_pdf_file(file_path)


if __name__ == "__main__":
    folder_path = input("폴더 경로를 입력하세요: ")
    if os.path.isdir(folder_path):
        rename_pdfs_in_folder(folder_path)
    else:
        print("유효하지 않은 폴더 경로입니다.")
