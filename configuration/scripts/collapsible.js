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
            });

            pre.appendChild(button);
        }
    });
});
