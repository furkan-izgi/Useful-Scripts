import os

conversion_map = {
    "Ä±": "ı", "Å": "ş", "Ã§": "ç", "Ã¶": "ö", "Ã¼": "ü", 
    "Ä": "ğ", "Ã": "Ç", "Ã": "Ö", "Å": "Ş", "Ã": "Ü", 
    "Ä": "Ğ", "Ä°": "İ"
}

def fixString(s):
    for wrong_char, correct_char in conversion_map.items():
        s = s.replace(wrong_char, correct_char)
    return s


def fixCorrupted(base_dir):
    for dirpath, dirnames, filenames in os.walk(base_dir, topdown=False):
      
        for filename in filenames:
            new_filename = fixString(filename)
            if new_filename != filename:
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Dosya adı düzeltildi: {new_file_path}")

        for dirname in dirnames:
            new_dirname = fixString(dirname)
            if new_dirname != dirname:
                old_dir_path = os.path.join(dirpath, dirname)
                new_dir_path = os.path.join(dirpath, new_dirname)
                os.rename(old_dir_path, new_dir_path)
                print(f"Klasör adı düzeltildi: {new_dir_path}")

main_folder = input("Ana Dizinin Yolunu Giriniz: ")
fixCorrupted(main_folder)
