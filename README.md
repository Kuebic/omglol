# Content Management for [Kenei's Weblog](https://kenei.weblog.lol)

This repository manages the content of my [Weblog](https://weblog.lol) developed by [NeatNik](https://neatnik.net). The content is primarily organized in Markdown, and songs are formatted using [ChordPro](https://www.chordpro.org). The repository hosts a collection of popular songs by the HSA, with multiple arrangements available.

## How to Contribute

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
    ```
2. **Add New Songs**:
    - Copy the Markdown formatting from existing songs
    - Ensure that ChordPro formatting is enclosed within coding brackets:
        ```markdown
            \`\`\`chordpro
            [C]This is an [G]example
            \`\`\`
        ```
    - For multiple versions of a song, separate each version with a Header 6
        ```markdown
            ###### Acoustic Version

            ---
        ```
3. Create a pull request
    - [Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    - Or just send them to me manually and I'll add them.
4. Organizing Notes:
    - Be sure to organize songs by folder and the folder is reflected in the `location` metadata of the song file

### Contact
For questions, comments, or concerns, feel free to reach out to me at kenei@menningmail.com
