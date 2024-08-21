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
</header>

<main>
	<!-- Add buttons for transposing -->
	<h4>Transpose</h4>
    <div>
        <button class="transpose-btn" onclick="transposeChords(-1)">⟱</button>
		<button class="transpose-btn" id="enharmonic-btn" onclick="toggleEnharmonic()">♭/♯</button>
		<button class="transpose-btn" onclick="transposeChords(1)">⟰</button>
    </div>
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

		// Set the current year
		document.getElementById('current-year').textContent = new Date().getFullYear();

		// Tabbed Content
document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('h6');
    const tabContentMap = new Map();

    // Create a container to hold the content
    const contentContainer = document.createElement('div');
    contentContainer.className = 'content-container';

    // Create a flex container for the tabs
    const tabsContainer = document.createElement('div');
    tabsContainer.className = 'tabs-container';

    // Insert the tabs container before the first h6 element
    tabs[0].parentNode.insertBefore(tabsContainer, tabs[0]);

    // Move all h6 elements into the tabs container
    tabs.forEach(tab => {
        tabsContainer.appendChild(tab);
    });

    // Insert the content container after the tabs container
    tabsContainer.parentNode.insertBefore(contentContainer, tabsContainer.nextSibling);

    // Map tabs to their corresponding content and initially hide content
    tabs.forEach(tab => {
        const content = [];
        let nextElement = tab.nextElementSibling;

        // Collect all elements until the next h6 or hr
        while (nextElement && nextElement.tagName !== 'H6' && nextElement.tagName !== 'HR') {
            content.push(nextElement);
            nextElement = nextElement.nextElementSibling;
        }

        // Map each tab to its associated content
        tabContentMap.set(tab, content);

        // Initially hide all content
        content.forEach(element => element.style.display = 'none');
    });

    // Handle tab click event
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Clear the content container
						console.log(contentContainer.innerHTML);
            contentContainer.innerHTML = '';
						console.log(contentContainer.innerHTML);

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active-tab'));

            // Show content associated with clicked tab
            tabContentMap.get(tab).forEach(element => {
                const clonedElement = element.cloneNode(true); // Clone the element
                clonedElement.style.display = 'block';
                contentContainer.appendChild(clonedElement);
            });

            // Add active class to clicked tab
            tab.classList.add('active-tab');
        });
    });

    // Trigger the first tab by default
    if (tabs.length > 0) {
        tabs[0].click();
    }
});

</script>

</body>
</html>
