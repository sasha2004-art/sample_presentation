import os

OUTPUT_FILE = 'code.txt'
IGNORE_DIRS = {'.git', '__pycache__', '.idea', '.vscode'}
IGNORE_FILES = {OUTPUT_FILE, 'collector.py', '.DS_Store'}

def generate_tree(startpath):
    tree_str = "PROJECT STRUCTURE:\n"
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f not in IGNORE_FILES:
                tree_str += f"{subindent}{f}\n"
    return tree_str + "\n" + "="*50 + "\n\n"

def collect_code(startpath):
    content = ""
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file in IGNORE_FILES:
                continue
            
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    
                relative_path = os.path.relpath(file_path, startpath)
                content += f"FILE: {relative_path}\n"
                content += "-"*20 + "\n"
                content += file_content
                content += "\n" + "="*50 + "\n\n"
            except Exception as e:
                print(f"Skipping file {file_path}: {e}")
                continue
    return content

def main():
    current_dir = os.getcwd()
    
    print("Generating tree structure...")
    tree_data = generate_tree(current_dir)
    
    print("Collecting code...")
    code_data = collect_code(current_dir)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(tree_data)
        f.write(code_data)
        
    print(f"Done! Project collected in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()