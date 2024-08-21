Type: file
Content-Type: text/css
Title: Stylesheet
Location: /files/style.css

@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&family=Merriweather:wght@400;700&family=Open+Sans:wght@400;700&display=swap');
@import url('https://static.omg.lol/type/fontawesome-free/css/all.css');

/* Nord Theme Colors with a Splash of Personality */
:root {
    --foreground: #D8DEE9; /* nord4 */
    --background: #2E3440; /* nord0 */
    --link: #88C0D0;      /* nord8 */
    --accent: #81A1C1;    /* nord9 */
    --highlight: #A3BE8C; /* nord14 */
    --tag-bg: #5E81AC;    /* nord10 */
    --tag-color: #ECEFF4; /* nord6 */
    --button-bg: #81A1C1;
    --button-text: #2E3440;
}

@media (prefers-color-scheme: dark) {
    :root {
        --foreground: #ECEFF4; /* nord6 */
        --background: #2E3440; /* nord0 */
        --link: #88C0D0;      /* nord8 */
        --accent: #81A1C1;    /* nord9 */
        --highlight: #A3BE8C; /* nord14 */
        --tag-bg: #5E81AC;    /* nord10 */
        --tag-color: #ECEFF4; /* nord6 */
        --button-bg: #81A1C1;
        --button-text: #2E3440;
    }
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Open Sans', sans-serif;
    font-size: 120%;
    color: var(--foreground);
    background: var(--background);
    line-height: 1.7;
    margin: 0;
    padding: 0;
    transition: background-color 0.3s, color 0.3s;
}

header nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

header nav li {
    display: inline-block;
    margin-right: 1.5em;
}

header nav li a {
    display: block;
    text-decoration: none;
    color: var(--link);
    padding: 0.5em 0;
    font-weight: 700;
    transition: color 0.3s;
}

header nav li a:hover {
    color: var(--highlight);
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Merriweather', serif;
    margin: 1rem 0;
    color: var(--foreground);
    letter-spacing: 0.5px;
}

p, li {
    margin-bottom: 1.5em;
}

header, main, footer {
    max-width: 60em;
    margin: 2em auto;
    padding: 0 1em;
}

header {
    margin-top: 4em;
}

footer p {
    margin-top: 5em;
    font-size: 90%;
    text-align: center;
    color: var(--accent);
}

a:link { color: var(--link); }
a:visited { color: var(--link); }
a:hover { color: var(--highlight); }
a:active { color: var(--link); }

.post-info, .post-tags {
    font-size: 85%;
    color: var(--accent);
    text-align: right;
    margin-top: 2em;
}

.post-info i:nth-child(2) {
    margin-left: .75em;
}

.tag {
    background: var(--tag-bg);
    color: var(--tag-color) !important;
    padding: .4em .6em;
    margin: .8em 0 0 .4em;
    border-radius: .5em;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
    font-size: 85%;
    transition: background-color 0.3s, color 0.3s;
}

.tag:hover {
    background: var(--highlight);
    color: var(--button-text) !important;
}

hr {
    border: 0;
    height: 2px;
    background: var(--accent);
    margin: 2em 0;
}

code {
    padding: .2em .4em;
    border: 1px solid var(--accent);
    border-radius: 4px;
    white-space: pre-wrap;
    word-wrap: break-word;
    color: var(--foreground);
    background-color: #3B4252; /* nord1 */
    font-family: 'Source Code Pro', monospace;
    transition: background-color 0.3s, color 0.3s;
}

pre, code {
    font-family: 'Source Code Pro', monospace;
    font-size: 90%;
}

pre code {
    background: #3B4252; /* nord1 */
    color: #D8DEE9; /* nord4 */
    display: inline-block;
    padding: 1em;
    white-space: pre-wrap;
    word-wrap: break-word;
    border-radius: 5px;
}

/* Collapsible Code Block Styles */
.collapsible {
    max-height: 6.5em; /* Approximately 4 lines of code */
    overflow: hidden;
    position: relative;
}

.collapsible-button {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--button-bg);
    color: var(--button-text);
    padding: 0.4em 0;
    text-align: center;
    font-family: 'Open Sans', sans-serif;
    font-size: 0.85em;
    cursor: pointer;
    border-top: 1px solid var(--accent);
    border-radius: 0 0 4px 4px;
    transition: background-color 0.3s, color 0.3s;
}

.collapsible.expanded {
    max-height: none;
}

.collapsible.expanded .collapsible-button {
    display: none;
}

img {
    max-width: 100%;
    border-radius: 5px;
    margin: 1em 0;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 2em;
}

td, th {
    padding: .75em;
    text-align: left;
    border: 1px solid var(--accent);
    color: var(--foreground);
}

.weblog-title a {
    text-decoration: none;
    color: var(--foreground);
    font-size: 1.8em;
    font-weight: 700;
}

button {
    background: var(--button-bg);
    color: var(--button-text);
    border: none;
    padding: 0.75em 1.5em;
    border-radius: 25px;
    font-family: 'Open Sans', sans-serif;
    font-size: 1em;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}

button:hover {
    background: var(--highlight);
    color: var(--foreground);
}

.chordpro-title {
    font-size: 1.2em;
    font-weight: bold;
}
.chordpro-subtitle {
    font-size: 1.1em;
    font-weight: light;
}
.chordpro-comment {
    font-style: italic;
    font-size: 0.9em;
}
.chordpro-key {
    display: inline-block;
    font-size: 1.5em;
    padding: 5px 10px 0;
    border: 2px solid #000;
    border-radius: 4px;
    width: auto;
    line-height: 1.5em;
    font-weight: bold;
    margin: 1em 0;
}
body.chordpro-verse:first-of-type {
    border-top: 1px solid #000;
    padding-top: 1em;
    margin-top: 1em;
}
.chordpro-verse {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end; /* Align chords and text properly */
}
.chordpro-chorus {
  padding-left: 10px;
  border-left: 4px solid #777;
}
.chordpro-elem {
  display: inline-block;
  vertical-align: bottom;
  margin-bottom: 0.5em; /* Adjust as needed for spacing */
  word-wrap: break-word; /* Ensure words break properly */
}
.chordpro-chord {
  position: relative;
  display: block;
  padding-right: 5px;
  font-weight: bold;
  font-size: 0.9em;
  margin-bottom: -.6em;
}
.chordpro-text {
  position: relative;
  display: block;
}
.chordpro-elem, .chordpro-verse {
  word-break: break-word;
}
.chordpro-words::before {
  content: "Words: ";
}

.chordpro-lyrics::before {
  content: "Lyrics: ";
}

.chordpro-music::before {
  content: "Music: ";
}

/* Add some basic styling to the buttons */
.transpose-btn {
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    margin: 5px;
    border-radius: 3px;
}
.transpose-btn:hover {
    background-color: #0056b3;
}

/* Adjusted styling for transpose buttons to match Nord theme */
.transpose-btn {
    cursor: pointer;
    background-color: var(--button-bg); /* Use the Nord button background color */
    color: var(--button-text);          /* Use the Nord button text color */
    border: 2px solid var(--accent);    /* Add a border that matches the accent color */
    padding: 0.5em 1em;
    margin: 0.5em;
    border-radius: 20px;                /* Soft border radius for a smoother appearance */
    font-family: 'Open Sans', sans-serif;
    font-size: 1em;
    font-weight: 700;
    transition: background-color 0.3s, color 0.3s, transform 0.3s; /* Add a transition for hover effects */
}

.transpose-btn:hover {
    background-color: var(--highlight); /* Use the Nord highlight color on hover */
    color: var(--foreground);           /* Ensure text contrast on hover */
    transform: scale(1.05);             /* Slight scaling effect on hover */
}

/* === Style for the tab headers === */

/* Hide all content by default */
/*.chordpro-title, .chordpro-key, .chordpro-comment, .chordpro-verse, p {
    display: none;
}*/

/* Ensure all H6 elements are displayed as inline tabs */
h6 {
    cursor: pointer;
    padding: 10px 15px;
    border-bottom: 2px solid transparent;
    font-weight: bold;
    margin-right: 10px;
    display: inline-block;
    color: var(--link);
    transition: color 0.3s, border-bottom-color 0.3s;
}

/* Hover effect for tabs */
h6:hover {
    color: var(--highlight);
}

/* Active tab styling */
.active-tab {
    border-bottom-color: var(--highlight);
    color: var(--highlight);
}

/* Flexbox container for tabs */
.tabs-container {
    display: flex;
    align-items: flex-start;
    flex-wrap: nowrap;
    margin-bottom: 10px;
    border-bottom: 2px solid #ccc;
}

/* Content container styling */
.content-container {
    display: block; /* Ensure it's visible */
    margin-top: 20px; /* Space between the tabs and the content */
}
