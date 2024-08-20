Type: file
Content-Type: text/js
Title: collapse-code
Location: /files/collapse-code.js

document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('h6');
    const sections = document.querySelectorAll('h6, .chordpro-title, .chordpro-key, .chordpro-comment, .chordpro-verse, p');

    tabs.forEach((tab, index) => {
        tab.style.cursor = 'pointer';
        tab.addEventListener('click', function() {
            // Reset all tabs and content sections
            tabs.forEach(t => t.classList.remove('active-tab'));
            sections.forEach(section => section.style.display = 'none');

            // Set the clicked tab as active
            tab.classList.add('active-tab');

            // Display the current section and the following content until the next <h6> or <hr> tag
            sections[index].style.display = 'block'; // Show the clicked <h6> tab
            let nextElement = sections[index].nextElementSibling;

            while (nextElement && !nextElement.matches('h6, hr')) {
                nextElement.style.display = 'block';
                nextElement = nextElement.nextElementSibling;
            }
        });
    });

    // Trigger the first tab by default
    if (tabs.length > 0) {
        tabs[0].click();
    }
});
