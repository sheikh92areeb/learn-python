# 1. Installing Python from the Official Website

## Step 1: Visit the Python Website

-   Go to the official [Python website](https://www.python.org.)

## Step 2: Download the Installer

-   Click on the Downloads tab on the website.

-   The site automatically suggests the latest version of Python suitable for your operating system.

## Step 3: Run the Installer

### For Windows Users:

1.  Download the Python installer for Windows.

2.  Run the downloaded file.

3.  In the installer, ensure that you check the box "Add Python to PATH" (this is very important).

4.  Select Install Now and follow the on-screen instructions.

### For macOS Users:

1.  Download the Python installer for macOS.

2.  Run the .pkg file.

3.  Follow the installation wizard to complete the setup.

### For Linux Users:

1.  Download the source code tarball from the website.

2.  Open the terminal and extract the tarball using:
    ```bash
    tar xvf Python-x.x.x.tar.xz

3.  Follow the build and installation instructions in the tarball’s README file.

## Step 4: Verify the Installation

-   Open a terminal or command prompt and type:
    ```bash
    python --version

    or
    ```bash
    python3 --version

-   You should see the installed Python version displayed.

---

# 2. Installing Python via Terminal

For users comfortable with the terminal (especially macOS and Linux), you can install Python directly from the command line.

## On macOS/Linux

### Step 1: Update the Package Manager

-   Open the terminal and update your system's package manager:
    ```bash
    sudo apt update    # For Ubuntu/Debian
    sudo dnf update    # For Fedora
    brew update        # For macOS (using Homebrew)

### Step 2: Install Python

-   Run the following command to install Python:
    ```bash
    sudo apt install python3    # For Ubuntu/Debian
    sudo dnf install python3    # For Fedora
    brew install python         # For macOS (using Homebrew)

### Step 3: Verify the Installation

-   After installation, verify the Python version by running:
    ```bash
    python3 --version

## On Windows (via Windows Subsystem for Linux - WSL)

1.  Install WSL from the Microsoft Store if you haven’t already.

2.  Launch WSL and follow the Linux steps above to install Python.