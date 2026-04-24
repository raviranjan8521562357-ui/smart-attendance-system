# smart-attendance-system

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-Backend-green?style=for-the-badge&logo=supabase)

AI-powered attendance management platform built with Streamlit, biometric recognition pipelines, and Supabase. The system streamlines classroom attendance by helping teachers manage subjects, run AI-assisted attendance workflows, and review records while giving students a face-based login and enrollment experience.

## Project Description

`smart-attendance-system` is a portfolio-ready applied AI project that combines product thinking with practical engineering. It demonstrates how face recognition, optional voice verification, and a modern cloud data layer can work together in a usable education workflow instead of a research-only prototype.

This project is designed to show recruiters a complete software story:

- user-facing product flows
- modular Python application structure
- database-backed state and persistence
- ML-assisted attendance automation
- real-world deployment potential

## Key Features

- Teacher authentication and dashboard workflows
- Student login using face recognition
- Optional voice-based attendance support
- AI attendance detection from uploaded classroom images
- Subject creation, enrollment, and share-code based joining
- Attendance history and summary tracking
- Supabase-backed storage for users, subjects, and attendance records
- Streamlit-based interface for rapid product delivery

## Tech Stack

- Python
- Streamlit
- Supabase
- NumPy
- Pandas
- scikit-learn
- dlib / face-recognition models
- librosa
- Resemblyzer
- Pillow
- bcrypt

## Architecture

The project follows a simple layered flow that is easy to explain in interviews and easy to extend:

1. The user interacts with the Streamlit UI through `app.py`.
2. Screen modules in `src/screens/` handle teacher and student workflows.
3. Reusable UI pieces live in `src/components/` and layout styling lives in `src/ui/`.
4. Business actions trigger data access functions in `src/database/db.py`.
5. AI-specific tasks call face and voice pipelines from `src/pipelines/`.
6. Supabase stores teachers, students, subjects, enrollments, and attendance logs.
7. Results are returned to the UI for dashboard views, attendance summaries, and enrollment actions.

### Project Flow

```text
User -> Streamlit UI -> Screens -> Components / UI Layer
                             -> Database Layer -> Supabase
                             -> AI Pipelines -> Face / Voice Processing
Results -> Attendance Records / Enrollment / Dashboard Views
```

## Folder Structure

```text
smart-attendance-system/
|-- app.py
|-- requirements.txt
|-- README.md
|-- docs/
|   `-- screenshots/
|-- tests/
|   |-- conftest.py
|   |-- test_project_structure.py
|   `-- test_security_utils.py
`-- src/
    |-- components/
    |-- database/
    |   |-- config.py
    |   `-- db.py
    |-- pipelines/
    |   |-- face_pipeline.py
    |   `-- voice_pipeline.py
    |-- screens/
    |   |-- home_screen.py
    |   |-- student_screen.py
    |   `-- teacher_screen.py
    `-- ui/
        `-- base_layout.py
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/raviranjan8521562357-ui/smart-attendance-system.git
cd smart-attendance-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure secrets

Create `.streamlit/secrets.toml` locally and add:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

Do not commit real secrets to GitHub.

### 5. Run the app

```bash
streamlit run app.py
```

## Usage Overview

### Teacher flow

- Register or log in as a teacher
- Create and manage subjects
- Share subject codes with students
- Upload classroom photos for face-based attendance
- Review attendance summaries and records

### Student flow

- Log in using face recognition
- Register a new profile if no face match is found
- Optionally enroll a voice sample
- Join subjects using shared codes
- View enrolled subjects and attendance stats

## Screenshots

Add screenshots to [docs/screenshots](./docs/screenshots) and reference them here.

Suggested captures:

- Home screen
- Teacher dashboard
- Face attendance upload flow
- Attendance results view
- Student dashboard

Example markdown after adding images:

```md
![Home Screen](docs/screenshots/home.png)
![Teacher Dashboard](docs/screenshots/teacher-dashboard.png)
```

## Testing

Starter tests are included in the `tests/` folder to make the repository feel more production-ready and easier to extend.

Run tests with:

```bash
pytest
```

## Deployment Options

Recommended deployment approaches:

- Streamlit Community Cloud: best for quick demos and portfolio sharing
- Render: good for managed Python app deployment with environment variables
- Railway: simple deployment flow for portfolio-grade apps
- Docker on a VPS: best if you want full control and custom scaling

For recruiter demos, Streamlit Community Cloud is the easiest path. For a stronger production story, Render or Docker plus a managed Supabase backend is the best balance.

## Production-Readiness Notes

- Secrets are kept out of Git through `.gitignore`
- The codebase is split into UI, database, and pipeline layers
- Supabase provides a clean managed backend
- Starter tests are included for future expansion
- The repository is structured for clear onboarding and easy demoing

## Recommended Next Improvements

- Add real screenshots and a short demo GIF
- Add CI with GitHub Actions for linting and tests
- Introduce a `src/services/` layer for business logic separation
- Add more unit tests around database and pipeline adapters
- Add a `LICENSE` and `CONTRIBUTING.md` if you want open-source polish

## Author

Ravi Ranjan

