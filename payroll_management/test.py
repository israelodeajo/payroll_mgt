# test.py
import os
import sys
import importlib.util

def load_by_path(module_name: str, file_path: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {file_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod

if __name__ == "__main__":
    # Resolve path to data/__init__.py
    current_dir = os.path.dirname(__file__)
    data_init_path = os.path.abspath(os.path.join(current_dir, "data", "__init__.py"))

    # Load the module directly by file path (no package imports)
    data_mod = load_by_path("payroll_data_loader", data_init_path)

    # Call load_data()
    db = data_mod.load_data()

    # Print row counts
    for table, rows in db.items():
        print(f"{table}: {len(rows)} rows")

    # Show a sample row per table
    print("\n--- sample rows ---")
    for table, rows in db.items():
        if not rows:
            print(f"{table}: <empty>")
            continue
        first_key = next(iter(rows))
        print(f"{table}[{first_key}]: {rows[first_key]}")
