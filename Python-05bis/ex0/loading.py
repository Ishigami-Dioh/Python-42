#! /bin/usr/env python3


def check_reagent(name, min_version):
    try:
        module = __import__(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - Computation is ready")
        return True
    except ImportError:
        print(f"[MISSING] {name} is not installed.")
        return False


def show_explanation():
    print("\npip vs Poetry:")
    print("requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("versions in poetry.lock so every install is identical.")


def main():
    print("REAGENT STATUS: Loading reagents...\nChecking dependencies:")
    has_panda = check_reagent("pandas", "2.1.0")
    has_numpy = check_reagent("numpy", "1.25.0")

    if not (has_panda and has_numpy):
        print("\nWARNING: Missing reagents detected!")
        print("To install with pip, run:")
        print("  pip install -r ex0/requirements.txt")
        print("To install with Poetry, run:")
        print("  poetry install")
    else:
        show_explanation()
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
