# Gemini Project

This project is a minimal Markdown-to-static-site generator.

## Setup

1. Install `uv`:
   ```bash
   pip install uv
   ```

2. Install dependencies:
   ```bash
   uv add markdown
   uv sync
   ```

## Usage

1. Add Markdown files to the `posts` directory.
2. Run the build script:
   ```bash
   python build.py
   ```
3. The generated site will be in the `public` directory.
