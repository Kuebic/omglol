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
  height: 3em;
}
.chordpro-chorus {
  padding-left: 10px;
  border-left: 4px solid #777;
}
.chordpro-elem {
  position: relative;
  display: inline-block;
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
