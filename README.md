# Gemini SQLite Query Generator

This project converts natural language questions into correct SQLite queries using the Gemini API.

## Project Structure
- `sql.py` : Contains the system prompt, Gemini API integration, and natural language to SQL generation.
- `sqlite.py` : Provides functions to interact with the SQLite database.
- `requirements.txt` : Lists the Python libraries required to run the project.
- `.env` : Contains the Gemini API key (`GOOGLE_API_KEY=your_api_key`).

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gemini-sqlite-query-generator.git
    cd gemini-sqlite-query-generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate    # For Mac/Linux
    venv\Scripts\activate       # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file:
    ```
    GOOGLE_API_KEY=your_actual_gemini_api_key_here
    ```

5. Run the application:
    ```bash
    python sql.py
    ```

## Notes
- The SQLite database must match the schema described inside `sql.py`.
- The system prompt is defined directly inside the `sql.py` file (no external prompt file).

