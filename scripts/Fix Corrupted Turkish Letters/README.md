# Fix Corrupted Turkish Letters

This Python script is designed to fix corrupted file and folder names caused by incorrect character encoding. Specifically, it addresses common encoding issues that replace certain Turkish characters with incorrect symbols. The script scans all files and folders within a specified directory and corrects their names by replacing problematic characters with the correct ones.

## Features

- Automatically corrects filenames and folder names with corrupted Turkish characters.
- Recursively traverses through subdirectories to ensure all files and folders are corrected.
- Provides real-time updates via console messages on which names were corrected.

## Character Mappings

The script replaces the following incorrectly encoded characters:

| Incorrect Character | Correct Character |
|---------------------|-------------------|
| Ä±                  | ı                 |
| Å                   | ş                 |
| Ã§                  | ç                 |
| Ã¶                  | ö                 |
| Ã¼                  | ü                 |
| Ä                   | ğ                 |
| Ã                   | Ç                 |
| Ã                   | Ö                 |
| Å                   | Ş                 |
| Ã                   | Ü                 |
| Ä                   | Ğ                 |
| Ä°                  | İ                 |

## Usage

### Prerequisites

Ensure you have Python installed on your machine. This script uses Python's built-in `os` module, so no external libraries are required.

### Running the Script

1. Clone the related repository.
2. **Open a terminal** and type `python3 fix_corrupted.py` or `python fix_corrupted.py`.
3. Enter the main path and press enter. It will search and fix the corrupted file and directory names.
