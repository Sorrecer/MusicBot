import os

def convert_lyrics(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} not found in the directory {os.getcwd()}")
        print("Files in the current directory:")
        print(os.listdir(os.getcwd()))
        return

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove any surrounding whitespace, add quotes and a comma
            modified_line = f"'{line.strip()}',\n"
            outfile.write(modified_line)

    print(f"Successfully converted {input_file} to {output_file}")

# Example usage
input_file = 'D:/xampp/htdocs/MusicBot/input_lyrics.txt'
output_file = 'D:/xampp/htdocs/MusicBot/output_lyrics.txt'
convert_lyrics(input_file, output_file)

