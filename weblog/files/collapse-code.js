Type: file
Content-Type: text/js
Title: collapse-code
Location: /files/collapse-code.js

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
