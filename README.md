# Most Recent

I have finally finished this application and am excited to share it with others. It is now complete and ready for use.

## About

This project is a **Launch Card Flask Application** designed to display SpaceX launch data in a convenient and user-friendly way. The application fetches data from the SpaceX API and uses a macro-based HTML template to render the launch information dynamically.

### Features

- Fetches live SpaceX launch data from the SpaceX API.
- Displays key details such as mission name, launch date, and additional resources (e.g., articles, Wikipedia links).
- Uses Flask for the backend and Jinja2 macros for efficient HTML rendering.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask installed (or a `requirements.txt` file)

---

### Installation Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     venv\Scripts\activate
     ```
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Running the Application

1. Start the Flask development server:

   ```bash
   flask run
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

### Future Improvements

- Add search or filtering functionality for launch data.
- Implement pagination or infinite scrolling for larger datasets.
- Enhance styling with a CSS framework such as Bootstrap or TailwindCSS.
