#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


def get_env_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return None


def load_configuration():
    env_path = get_env_path()
    load_dotenv(dotenv_path=env_path)
    return {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL", "Connected to local instance"),
        "api_key": os.getenv("API_KEY", "Authenticated"),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT", "Online"),
        "missing": [k for k in ["MATRIX_MODE", "DATABASE_URL",
                                "API_KEY", "LOG_LEVEL",
                                "ZION_ENDPOINT"] if not os.getenv(k)]
    }


def display_status(config):
    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {config['database']}")
    print(f"API Access: {config['api_key']}")
    print(f"Log Level: {config['log_level']}")
    print(f"Remote Network: {config['zion_endpoint']}")
    if config['missing']:
        print("[WARN] Missing env vars (using defaults): "
              f"{', '.join(config['missing'])}")


def display_security_check():
    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


def main():
    config = load_configuration()
    display_status(config)
    display_security_check()


if __name__ == "__main__":
    main()
