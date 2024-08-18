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
    const chordMap = {
        "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5,
        "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11
    };

    const chordArray = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

    function transposeChords(semitones) {
        const chords = document.querySelectorAll('.chordpro-chord');

        chords.forEach(chord => {
            let originalChord = chord.textContent.trim();
            let baseChord = originalChord.match(/[A-G][b#]?/)[0];
            let suffix = originalChord.slice(baseChord.length);

            let newIndex = (chordMap[baseChord] + semitones + 12) % 12;
            let newChord = chordArray[newIndex] + suffix;

            chord.innerHTML = newChord.replace("b", "&#9837;").replace("#", "&#9839;");
        });
    }
	document.getElementById('current-year').textContent = new Date().getFullYear();
</script>
</body>
</html>
