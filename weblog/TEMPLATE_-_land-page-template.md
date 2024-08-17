Type: Template
Title: Landing Page Template

<!DOCTYPE html>
<html lang="en">
<head>
<title>{weblog-title}{separator}{post-title}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{feeds}
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&family=Merriweather:wght@400;700&family=Open+Sans:wght@400;700&display=swap');
@import url('https://static.omg.lol/type/fontawesome-free/css/all.css');
@import url('https://kenei.weblog.lol/files/style.css');
</style>
</head>
<body>

<header>
	<h1 class="weblog-title"><a href="{base-path}">{weblog-title}</a></h1>
	{navigation}
</header>

<main>

{body}

<nav>
{previous-page}
{next-page}
</nav>

</main>

<footer>
    <p>&copy; <span id="current-year"></span> <a href="{base-path}">{weblog-title}</a>. All rights reserved.</p>
    <button onclick="window.location.href='#home'">Back to Top</button>
</footer>

<script>
    // JavaScript to dynamically update the year
    document.getElementById('current-year').textContent = new Date().getFullYear();
</script>

<script>
	// JavaScript to collapse and expand code blockss
    document.addEventListener('DOMContentLoaded', function () {
        const codeBlocks = document.querySelectorAll('pre code');
        codeBlocks.forEach(function (codeBlock) {
            const lines = codeBlock.innerHTML.split('\n').length;
            if (lines > 4) {
                const pre = codeBlock.parentElement;
                pre.classList.add('collapsible');

                const button = document.createElement('div');
                button.className = 'collapsible-button';
                button.innerHTML = 'Click to expand';
                button.addEventListener('click', function () {
                    pre.classList.toggle('expanded');
                    if (pre.classList.contains('expanded')) {
                        button.innerHTML = 'Click to collapse';
                    } else {
                        button.innerHTML = 'Click to expand';
                    }
                });

                pre.appendChild(button);
            }
        });
    });
</script>

</body>
</html>
