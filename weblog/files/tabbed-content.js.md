Type: file
Content-Type: text/js
Title: collapse-code
Location: /files/collapse-code.js

document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('h6');
    const tabContentMap = new Map();

    // Create a container to hold the content and insert it after the tab container
    const contentContainer = document.createElement('div');
    contentContainer.className = 'content-container';
    tabs[0].parentNode.insertBefore(contentContainer, tabs[0].nextSibling);

    // Map tabs to their corresponding content
    tabs.forEach(tab => {
        const content = [];
        let nextElement = tab.nextElementSibling;

        while (nextElement && !nextElement.matches('h6, hr')) {
            content.push(nextElement);
            nextElement = nextElement.nextElementSibling;
        }

        tabContentMap.set(tab, content);

        // Initially hide all content
        content.forEach(element => element.style.display = 'none');
    });

    // Handle tab click event
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Clear the content container
            contentContainer.innerHTML = '';

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active-tab'));

            // Clone and show content associated with clicked tab
            tabContentMap.get(tab).forEach(element => {
                const clonedElement = element.cloneNode(true);
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
