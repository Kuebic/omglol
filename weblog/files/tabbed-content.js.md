Type: file
Content-Type: text/js
Title: collapse-code
Location: /files/collapse-code.js

document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('h6');
    const tabContentMap = new Map();

    // Step 1: Map the tabs to their corresponding content before moving them
    tabs.forEach(tab => {
        const content = [];
        let nextElement = tab.nextElementSibling;
        let hrElement = null; // To track the <hr> element to remove later

        // Debugging: Log the current tab being processed
        console.log("Processing tab:", tab.textContent);

        // Collect all elements until the next h6 or hr
        while (nextElement && nextElement.tagName !== 'H6' && nextElement.tagName !== 'HR') {
            if (nextElement.nodeType === Node.ELEMENT_NODE) {
                console.log("Found element:", nextElement);
                content.push(nextElement);
            }
            nextElement = nextElement.nextElementSibling;
        }

        // If the next element is <hr>, store it for removal
        if (nextElement && nextElement.tagName === 'HR') {
            hrElement = nextElement;
        }

        // Debugging: Log mapped content for this tab
        console.log("Mapped content for tab:", tab.textContent, content);

        // Map each tab to its associated content
        tabContentMap.set(tab, content);

        // Initially hide all content
        content.forEach(element => element.style.display = 'none');

        // Remove the <hr> element after it has served its purpose
        if (hrElement) {
            hrElement.remove();
        }
    });

    // Step 2: Create containers for tabs and content
    const contentContainer = document.createElement('div');
    contentContainer.className = 'content-container';

    const tabsContainer = document.createElement('div');
    tabsContainer.className = 'tabs-container';

    // Step 3: Insert the tabs container and content container first
    const firstTabParent = tabs[0].parentNode;
    firstTabParent.insertBefore(tabsContainer, tabs[0]); // Insert tabs container before the first tab
    tabsContainer.parentNode.insertBefore(contentContainer, tabsContainer.nextSibling);

    // Step 4: Move the h6 elements into the tabs container
    tabs.forEach(tab => {
        tabsContainer.appendChild(tab);
    });

    // Step 5: Handle tab click events
		tabs.forEach(tab => {
				tab.addEventListener('click', function() {
						// Clear the content container
						contentContainer.innerHTML = '';

						// Remove active class from all tabs
						tabs.forEach(t => t.classList.remove('active-tab'));

						// Show content associated with clicked tab
						const associatedContent = tabContentMap.get(tab);
						if (associatedContent) {
								associatedContent.forEach(element => {
										const clonedElement = element.cloneNode(true); // Clone the element
										clonedElement.style.display = 'block';
										// Check if the element is a .chordpro-key and adjust display
                    if (clonedElement.classList.contains('chordpro-key')) {
                        clonedElement.style.display = 'inline-block'; // Override display block
                    }

										contentContainer.appendChild(clonedElement);
								});
						}

						// Add active class to clicked tab
						tab.classList.add('active-tab');
				});
		});

    // Step 6: Trigger the first tab by default
    if (tabs.length > 0) {
        tabs[0].click();
    }
});
