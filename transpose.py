import re

# Map of chords to their corresponding indices in a chromatic scale
chromatic_scale = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7,
    'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}

# Reverse map of indices to their corresponding chords (for both sharps and flats)
index_to_chord = [
    ('C'), ('C#', 'Db'), ('D'), ('D#', 'Eb'), ('E'), ('F'), ('F#', 'Gb'), ('G'), ('G#', 'Ab'), ('A'), ('A#', 'Bb'), ('B')
]

def transpose_chord(chord, half_steps):
    # Extract root, accidental (if any), and rest of the chord
    match = re.match(r'([A-G])(#|b)?(.*)', chord)
    if not match:
        return chord  # If no match, return the chord as-is

    root, accidental, suffix = match.groups()
    root += accidental if accidental else ''

    # Find the current index of the root note
    current_index = chromatic_scale[root]

    # Transpose the chord
    new_index = (current_index + half_steps) % 12

    # Choose the appropriate name for the transposed chord
    new_root = index_to_chord[new_index][0]

    # Return the transposed chord with its suffix
    return new_root + suffix

def transpose_line(line, half_steps):
    # Replace each chord in the line using the transpose_chord function
    return re.sub(r'\[([A-G][#b]?[^]]*)\]', lambda match: f"[{transpose_chord(match.group(1), half_steps)}]", line)

def transpose_song(filename, half_steps):
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Transpose each line
    transposed_lines = [transpose_line(line, half_steps) for line in lines]

    # Write the transposed lines back to the file (or you could print them or save them to a new file)
    with open(filename, 'w') as file:
        file.writelines(transposed_lines)

def main():
    # Get filename and transpose amount from the user
    filename = input("Enter the filename: ")
    try:
        transpose_amount = int(input("Enter the number of half-steps to transpose (positive or negative): "))
    except ValueError:
        print("Please enter a valid integer for transpose amount.")
        return

    # Transpose the song
    transpose_song(filename, transpose_amount)
    print(f"The chords in {filename} have been transposed by {transpose_amount} half-steps.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
