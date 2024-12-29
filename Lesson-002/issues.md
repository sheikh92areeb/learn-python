# Troubleshooting Common Issues

## Issue 1: "Python Command Not Found"

-   Ensure Python is added to your system’s PATH environment variable.

-   On Windows, re-run the installer and ensure the "Add Python to PATH" option is checked.

-   On Linux/macOS, use:
    ```bash
    export PATH="$PATH:/usr/local/bin/python3"
---

## Issue 2: Old Python Version

-   Upgrade to the latest version:
    ```bash
    sudo apt upgrade python3    # For Ubuntu/Debian
    brew upgrade python         # For macOS