// Define the mapping for chords
const chordArray = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
const flatChordArray = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"];

// Function to transpose a chord
function transposeChord(chord, semitones) {
    const match = chord.match(/^([A-G])([#b]?)(.*)$/);  // Match root note and suffix
    if (!match) return chord;  // If it's not a valid chord, return as-is

    const root = match[1];  // The root note (e.g., C, G, A)l
    print("root", root)
    System.Println("root", root)
    const accidental = match[2];  // The accidental (e.g., #, b)
    print("accidental", accidental)
    const suffix = match[3];  // The suffix (e.g., m, 7, /F)
    print("suffix", suffix)

    // Determine the current index in either the sharp or flat chord array
    let index = chordArray.indexOf(root + accidental);
    if (index === -1) {
        index = flatChordArray.indexOf(root + accidental);
    }

    if (index === -1) return chord;  // If the root is not found, return the original chord

    // Calculate the new index with wrapping
    const newIndex = (index + semitones + 12) % 12;
    print("newIndex", newIndex)

    // Choose the new chord name based on preference for sharps or flats
    const newChord = chordArray[newIndex];
    print("newChord", newChord)

    // Return the transposed chord with the original suffix
    return newChord + suffix;
}

// Function to transpose all chords on the page
function transposeChords(semitones) {
    const chords = document.querySelectorAll('.chordpro-chord');

    chords.forEach(chord => {
        let originalChord = chord.textContent.trim();
        let transposedChord = transposeChord(originalChord, semitones);
        chord.textContent = transposedChord;
    });
}
