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
	const chordArray = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"];
	const flatChordArray = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"];

	// Function to transpose a chord
	function transposeChord(chord, semitones) {
		// Match the root note and suffix, handling sharp (♯) and flat (♭)
		const match = chord.match(/^([A-G])([♯♭#b]?)(.*)$/);
		if (!match) return chord;  // If it's not a valid chord, return as-is

		let root = match[1];  // The root note (e.g., C, G, A)
		let accidental = match[2];  // The accidental (e.g., ♯, ♭, #, b)
		const suffix = match[3];  // The suffix (e.g., m, 7, /F)

		let index;

		// Normalize accidental to either sharp or flat
		if (accidental === "♯" || accidental === "#") {
			index = chordArray.indexOf(root + "♯");
		} else if (accidental === "♭" || accidental === "b") {
			index = flatChordArray.indexOf(root + "♭");
		} else {
			// If no accidental, search in both arrays
			index = chordArray.indexOf(root);
			if (index === -1) {
				index = flatChordArray.indexOf(root);
			}
		}

		if (index === -1) return chord;  // If the root is not found, return the original chord

		// Calculate the new index with wrapping
		const newIndex = (index + semitones + 12) % 12;

		// Determine whether to use the sharp or flat name for the new chord
		let newChord;
		if (accidental === "♯" || accidental === "#") {
			newChord = chordArray[newIndex];
		} else if (accidental === "♭" || accidental === "b") {
			newChord = flatChordArray[newIndex];
		} else {
			// If no accidental, decide based on the nearest match (use flatChordArray for ♭ notes)
			newChord = flatChordArray.indexOf(chordArray[newIndex]) !== -1 ? flatChordArray[newIndex] : chordArray[newIndex];
		}

		// Return the transposed chord with the original suffix
		return newChord + suffix;
	}

	// Function to transpose all chords on the page, including the key
	function transposeChords(semitones) {
		// Transpose all chords
		const chords = document.querySelectorAll('.chordpro-chord');
		chords.forEach(chord => {
			let originalChord = chord.textContent.trim();
			let transposedChord = transposeChord(originalChord, semitones);
			chord.innerHTML = transposedChord.replace(/b/g, "♭").replace(/#/g, "♯");  // Replace normalized 'b' with ♭ and '#' with ♯
		});

		// Transpose the key element
		const keyElement = document.querySelector('.chordpro-key');
		if (keyElement) {
			let originalKey = keyElement.textContent.trim();
			let transposedKey = transposeChord(originalKey, semitones);
			keyElement.textContent = transposedKey.replace(/b/g, "♭").replace(/#/g, "♯");  // Replace normalized 'b' with ♭ and '#' with ♯
		}
	}

    // Set the current year
    document.getElementById('current-year').textContent = new Date().getFullYear();
</script>

</body>
</html>
