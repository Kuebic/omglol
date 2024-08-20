Type: file
Content-Type: text/js
Title: transposing
Location: /files/transposing.js

// Define the mapping for chords
const chordArray = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"];
const flatChordArray = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"];

// Define a variable to track the current enharmonic setting (true = sharp, false = flat)
let useSharps = true;

// Function to toggle between sharp and flat enharmonic equivalents
function toggleEnharmonic() {
    useSharps = !useSharps; // Toggle the setting

    // Update all chords on the page to reflect the new enharmonic preference
    const chords = document.querySelectorAll('.chordpro-chord');
    chords.forEach(chord => {
        let originalChord = chord.textContent.trim();
        let newChord = convertEnharmonic(originalChord);
        chord.innerHTML = newChord.replace(/b/g, "♭").replace(/#/g, "♯");  // Replace normalized 'b' with ♭ and '#' with ♯
    });

    // Update the key element
    const keyElement = document.querySelector('.chordpro-key');
    if (keyElement) {
        let originalKey = keyElement.textContent.trim();
        let newKey = convertEnharmonic(originalKey);
        keyElement.textContent = newKey.replace(/b/g, "♭").replace(/#/g, "♯");
    }
}

// Function to convert a chord to the current enharmonic preference (handles bass notes as well)
function convertEnharmonic(chord) {
    // Handle slash chords (e.g., D/F♯)
    const slashIndex = chord.indexOf('/');
    if (slashIndex !== -1) {
        const rootChord = chord.substring(0, slashIndex);
        const bassNote = chord.substring(slashIndex + 1);
        const convertedRoot = convertEnharmonic(rootChord);  // Recursive call for the root chord
        const convertedBass = convertEnharmonic(bassNote);   // Recursive call for the bass note
        return `${convertedRoot}/${convertedBass}`;
    }

    const match = chord.match(/^([A-G])([♯♭#b]?)(.*)$/);
    if (!match) return chord;

    let root = match[1];
    let accidental = match[2];
    const suffix = match[3];

    let index;
    if (accidental === "♯" || accidental === "#") {
        index = chordArray.indexOf(root + "♯");
    } else if (accidental === "♭" || accidental === "b") {
        index = flatChordArray.indexOf(root + "♭");
    } else {
        index = chordArray.indexOf(root);
        if (index === -1) {
            index = flatChordArray.indexOf(root);
        }
    }

    if (index === -1) return chord;

    // Choose the correct enharmonic equivalent based on the current setting
    if (useSharps) {
        return chordArray[index] + suffix;
    } else {
        return flatChordArray[index] + suffix;
    }
}

// Function to transpose a chord (handles chords with bass notes as well)
function transposeChord(chord, semitones) {
    // Handle slash chords (e.g., D/F♯)
    const slashIndex = chord.indexOf('/');
    if (slashIndex !== -1) {
        const rootChord = chord.substring(0, slashIndex);
        const bassNote = chord.substring(slashIndex + 1);
        const transposedRoot = transposeChord(rootChord, semitones);  // Recursive call
        const transposedBass = transposeChord(bassNote, semitones);   // Recursive call
        return `${transposedRoot}/${transposedBass}`;
    }

    // Regular chord transposition
    const match = chord.match(/^([A-G])([♯♭#b]?)(.*)$/);
    if (!match) return chord;

    let root = match[1];
    let accidental = match[2];
    const suffix = match[3];

    let index;
    if (accidental === "♯" || accidental === "#") {
        index = chordArray.indexOf(root + "♯");
    } else if (accidental === "♭" || accidental === "b") {
        index = flatChordArray.indexOf(root + "♭");
    } else {
        index = chordArray.indexOf(root);
        if (index === -1) {
            index = flatChordArray.indexOf(root);
        }
    }

    if (index === -1) return chord;

    const newIndex = (index + semitones + 12) % 12;

    if (useSharps) {
        return chordArray[newIndex] + suffix;
    } else {
        return flatChordArray[newIndex] + suffix;
    }
}

// Function to transpose all chords on the page, including the key
function transposeChords(semitones) {
    const chords = document.querySelectorAll('.chordpro-chord');
    chords.forEach(chord => {
        let originalChord = chord.textContent.trim();
        let transposedChord = transposeChord(originalChord, semitones);
        chord.innerHTML = transposedChord.replace(/b/g, "♭").replace(/#/g, "♯");
    });

    const keyElement = document.querySelector('.chordpro-key');
    if (keyElement) {
        let originalKey = keyElement.textContent.trim();
        let transposedKey = transposeChord(originalKey, semitones);
        keyElement.textContent = transposedKey.replace(/b/g, "♭").replace(/#/g, "♯");
    }
}
