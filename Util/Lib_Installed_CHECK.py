import importlib.util

# List of libraries to check
# Note: 'scikit-learn' is imported as 'sklearn'
libraries = ["pandas", "sklearn", "openpyxl"]

for lib in libraries:
    # Check if the library is found in the current environment
    spec = importlib.util.find_spec(lib)
    
    if spec is not None:
        print(f"{lib}: yes")
    else:
        print(f"{lib}: no")


