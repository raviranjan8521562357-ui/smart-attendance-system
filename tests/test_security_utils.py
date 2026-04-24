import importlib
import sys
import types


def load_db_module():
    fake_config = types.ModuleType("src.database.config")
    fake_config.supabase = object()
    sys.modules["src.database.config"] = fake_config

    if "src.database.db" in sys.modules:
        del sys.modules["src.database.db"]

    return importlib.import_module("src.database.db")


def test_hash_pass_returns_different_value_than_plain_text():
    db = load_db_module()
    password = "demo_password_123"
    hashed = db.hash_pass(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_check_pass_validates_correct_password():
    db = load_db_module()
    password = "secure_password"
    hashed = db.hash_pass(password)

    assert db.check_pass(password, hashed) is True
    assert db.check_pass("wrong_password", hashed) is False
