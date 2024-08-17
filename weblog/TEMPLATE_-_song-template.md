Type: Template
Title: Song

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

<script>
    // JavaScript to dynamically update the year
    document.getElementById('current-year').textContent = new Date().getFullYear();
</script>

<script>
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
