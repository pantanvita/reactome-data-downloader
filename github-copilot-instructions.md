# GitHub Copilot Instructions for This Project

---

## Project Overview
This project downloads files from the Reactome ContentService API, including:
- JSON event data
- PDF pathway diagrams
- PNG pathway images

Files must be saved inside a structured directory under **~/Desktop/Reactome_Downloads**.

The project uses a **clean separation between business logic and execution**:
- `reactome_service.py` → all API logic and file handling
- `main.py` → user interaction and program entry point

---

## Project Architecture Rules

### 1. Business Logic (reactome_service.py)
- Must contain **all** functionality related to:
  - API requests  
  - Downloading files  
  - Input/output directory management  
  - Subpathway retrieval (if implemented later)
- Never include print statements except via a provided `progress_callback`.
- All functions should be **pure** except those that explicitly do I/O.

### 2. Main Script (main.py)
- Responsible ONLY for:
  - getting user input
  - printing progress messages
  - calling service methods
- No API calls or business logic should appear in `main.py`.

### 3. Folder Structure
Copilot must preserve this exact format:
Reactome_Downloads/
<ST_ID>/
json/
pdf/
png/


Where:
- JSON → `/json/`
- PDF  → `/pdf/`
- PNG  → `/png/`

---

## Coding Style Guidelines

### General Python Style
- Follow PEP8.
- Use `snake_case` for all variables and functions.
- Prefer clear, descriptive variable names (no single-letter variables).
- Use early returns instead of deep nesting.

### Type Hints
- Use Python 3 type hints wherever reasonable.
- Return paths using `pathlib.Path`.

### Error Handling
- Check HTTP status codes.
- Avoid raising exceptions unless absolutely necessary.
- Prefer returning `None` and reporting errors via `progress_callback`.

### File I/O
- Always use `pathlib.Path` (never use raw strings for paths).
- Use `with open(...)` blocks.

---

## API Usage Rules
Copilot should use the following Reactome endpoints:

### JSON:
https://reactome.org/ContentService/data/query/{stId}

### PDF:
https://reactome.org/ContentService/exporter/document/event/{st_id}

### PNG:
https://reactome.org/ContentService/exporter/diagram/{st_id}


### Required Header:
Always include:
```python
{"User-Agent": f"ReactomeDownloader/1.0 ({self.email})"}