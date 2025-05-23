# MMPI
Assessment for Counseling Practice

---

## Static Interactive MMPI Tool

This project now includes a static HTML and JavaScript-based interactive MMPI tool: `mmpi_interactive_static.html`.

### Features:
-   Allows users to input responses (or scores directly, depending on the current UI).
-   Calculates T-scores for various MMPI scales.
-   Provides narrative interpretations for the calculated scores based on RC scales, PSY-5 scales, and Supplementary scales.
-   Includes gender-specific interpretations where applicable.
-   Features a welcome screen and a field for user name input.

### How to Use:
1.  Ensure you have the following files in the same directory:
    -   `mmpi_interactive_static.html`
    -   `rc_scales_interpretations.js`
    -   `psy5_scales_interpretations.js`
    -   `supplementary_scales_interpretations.js`
    -   A sub-folder named `static` containing `styles.css`.
2.  Open `mmpi_interactive_static.html` in any modern web browser (e.g., Chrome, Firefox, Safari, Edge).
3.  Follow the on-screen instructions to input data and view scores and interpretations.

### For GitHub Pages:
If you wish to deploy this tool using GitHub Pages:
1.  Ensure the repository has GitHub Pages enabled (usually configured in repository settings).
2.  If you want `mmpi_interactive_static.html` to be the root page, you can copy it to `index.html` in the root of the branch configured for GitHub Pages (e.g., `main` or `gh-pages`).
3.  Make sure all associated JavaScript files (`.js`) and the `static/styles.css` file are also present in the repository in the same relative paths.

---
