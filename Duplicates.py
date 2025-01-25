def remove_duplicates(file_path):
    unique_lines = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if line not in unique_lines:
                file.write(f"{line}\n")
                unique_lines.add(line)

# Exemple d'utilisation
remove_duplicates("user_comments.txt")





