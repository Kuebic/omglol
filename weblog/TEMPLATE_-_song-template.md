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
		<button class="transpose-btn" id="enharmonic-btn" onclick="toggleEnharmonic()">♯/♭</button>
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
			keyElement.textContent = newKey.replace(/b/g, "♭").replace(/#/g, "♯");  // Replace normalized 'b' with ♭ and '#' with ♯
		}
	}

	// Function to convert a chord to the current enharmonic preference
	function convertEnharmonic(chord) {
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

	// Function to transpose a chord
	function transposeChord(chord, semitones) {
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

    // Set the current year
    document.getElementById('current-year').textContent = new Date().getFullYear();
</script>

</body>
</html>
