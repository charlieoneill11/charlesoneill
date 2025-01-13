import os
from pathlib import Path

def print_directory_structure(directory_path, indent=""):
    """
    Recursively prints the directory structure starting from the given path.
    
    Args:
        directory_path: The starting directory path to scan
        indent: Current indentation level (used for recursive calls)
    """
    # Convert the path to a Path object for easier handling
    directory = Path(directory_path)
    
    # Print the current directory name
    print(f"{indent}📁 {directory.name}/")
    
    try:
        # Iterate through all items in the directory
        for item in sorted(directory.iterdir()):
            if item.is_file():
                # Print files with a different symbol
                print(f"{indent}    📄 {item.name}")
            elif item.is_dir():
                # Recursively print subdirectories with increased indentation
                print_directory_structure(item, indent + "    ")
                
    except PermissionError:
        print(f"{indent}    ⚠️ Permission denied")
    except Exception as e:
        print(f"{indent}    ⚠️ Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Get the current working directory if no path is specified
    current_path = os.getcwd()
    print("\nDirectory Structure:")
    print_directory_structure(current_path)