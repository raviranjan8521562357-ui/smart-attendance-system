from pathlib import Path


def test_expected_project_files_exist():
    project_root = Path(__file__).resolve().parents[1]

    expected_paths = [
        project_root / "app.py",
        project_root / "README.md",
        project_root / "requirements.txt",
        project_root / "src" / "database" / "db.py",
        project_root / "src" / "pipelines" / "face_pipeline.py",
    ]

    for path in expected_paths:
        assert path.exists(), f"Missing expected file: {path}"

