Type: Template
Title: Page Template

<!DOCTYPE html>
<html lang="en">
<head>
<title>{weblog-title}{separator}{post-title}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{feeds}
<link rel="stylesheet" href='https://kenei.weblog.lol/files/style.css'>
<script src="https://kenei.weblog.lol/files/update-year.js" defer></script>
<script src="https://kenei.weblog.lol/files/collapse-code.js" defer></script>
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

{body}

<aside class="post-tags">
	{tags}
</aside>

<hr>

</main>

<footer>
    <p>&copy; <span id="current-year"></span> <a href="{base-path}">{weblog-title}</a>. All rights reserved.</p>
    <button onclick="window.location.href='#home'">Back to Top</button>
</footer>

</body>
</html>
