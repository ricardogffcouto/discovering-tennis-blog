Project Specification: Minimal Markdown-to-Static-Site Generator
Overview

A minimal static site generator for a reverse-chronological blog. Each post is a separate .md file, converted to .html and displayed fully on the homepage. No frameworks, minimal styling, no feeds, no extra navigation. Hosted on GitHub Pages with automatic deployment.

Requirements

Functional Requirements

Homepage displays all posts in reverse chronological order (newest first) with full content.

Each post is a separate .md file stored locally.

Filenames define the post date automatically: YYYY-MM-DD-title.md.

Script converts .md files to .html and updates the homepage.

Minimal HTML: no CSS, no JavaScript, plain text only.

URLs mirror filenames: e.g., /2025-08-20-post-title.html.

Automatic GitHub Pages deployment on push using GitHub Actions.

No RSS/Atom feed, no previous/next navigation.

Non-functional Requirements

Minimal dependencies: only necessary libraries to convert Markdown to HTML (e.g., Python markdown module or Node marked).

Single script for .md → .html conversion and homepage generation.

Fully static output; no server-side processing.

Architecture

File Structure