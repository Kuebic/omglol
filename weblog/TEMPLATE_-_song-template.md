Type: Template
Title: Song

<!DOCTYPE html>
<html lang="en">
<head>
<title>{weblog-title}{separator}{post-title}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{feeds}
<link rel="stylesheet" href='https://kenei.weblog.lol/files/style.css'>
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&family=Merriweather:wght@400;700&family=Open+Sans:wght@400;700&display=swap');
@import url('https://static.omg.lol/type/fontawesome-free/css/all.css');
</style>
</head>
<body>

<header>
	<h1 class="weblog-title"><a href="{base-path}">{weblog-title}</a></h1>
	{navigation}
	<script src="https://kenei.weblog.lol/files/update-year.js" defer></script>
	<script src="https://kenei.weblog.lol/files/collapse-code.js" defer></script>
	<!-- Add buttons for transposing -->
    <div>
        <button class="transpose-btn" onclick="transposeChords(1)">Transpose Up</button>
        <button class="transpose-btn" onclick="transposeChords(-1)">Transpose Down</button>
    </div>
</header>

<main>

{body}

<aside class="post-tags">
	{tags}
</aside>

<hr>

</main>

<footer>
    <p>&copy; <span id="current-year"></span> <a href="{base-path}">{weblog-title}</a> All rights reserved.</p>
</footer>
<script>
    // Define the mapping for chords
    const chordArray = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
    const flatChordArray = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"];

    // Function to transpose a chord
    function transposeChord(chord, semitones) {
        const match = chord.match(/^([A-G])([#b]?)(.*)$/);  // Match root note and suffix
        if (!match) return chord;  // If it's not a valid chord, return as-is

        const root = match[1];  // The root note (e.g., C, G, A)
        const accidental = match[2];  // The accidental (e.g., #, b)
        const suffix = match[3];  // The suffix (e.g., m, 7, /F)

        // Determine the current index in either the sharp or flat chord array
        let index = chordArray.indexOf(root + accidental);
        if (index === -1) {
            index = flatChordArray.indexOf(root + accidental);
        }

        if (index === -1) return chord;  // If the root is not found, return the original chord

        // Calculate the new index with wrapping
        const newIndex = (index + semitones + 12) % 12;

        // Choose the new chord name based on preference for sharps or flats
        const newChord = chordArray[newIndex];

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

    // Set the current year
	document.getElementById('current-year').textContent = new Date().getFullYear();
</script>
</body>
</html>
