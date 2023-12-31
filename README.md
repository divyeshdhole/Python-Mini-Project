# Birthday Wisher

## Overview

The Birthday Wisher is a Python application that allows users to manage and wish friends a happy birthday through automated email greetings. It includes two main components:

1. **Birthday Checker Script**
   - A script (`main.py`) that checks if it's someone's birthday today by reading data from a CSV file (`birthdays.csv`).
   - If it's a friend's birthday, it sends a personalized birthday email using a pre-defined email template (`letter_1.txt`).
   - The script uses the `smtplib` library to send emails through a Gmail account.

2. **Birthday Entry GUI**
   - A GUI application (`BirthdayEntryGUI.py`) to input and store friends' birthday information.
   - Users can enter a friend's name, birthdate, and email address.
   - The entered data is appended to a CSV file (`birthdays.csv`) for future reference.

## Getting Started

### Prerequisites

- Python 3.11
- Required Python packages: `pandas`, `smtplib`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/divyeshdhole/Python-Mini-Project.git
    ```

2. Install the required packages:

    ```bash
    pip install pandas
    ```

## Usage

### Birthday Checker Script

```bash
python main.py

Execute the script to check for birthdays.
If it's a friend's birthday, a personalized email will be sent.
Birthday Entry GUI
bash
Copy code
python BirthdayEntryGUI.py
Run the GUI application to enter friends' birthday information.
Provide the friend's name, birthdate, and email address.
Click the "Submit" button to add the entry to the CSV file.
File Structure
main.py: Birthday checker script.
birthdays.csv: CSV file to store friends' birthday data.
letter_1.txt: Email template for birthday greetings.
GUI.py: GUI Setup.
Author
Author: Divyesh Dhole
Email: divyeshlic2003@gmail.com
Acknowledgments
This project was created as a part of a Python Mini Project.
Feel free to customize the README file further based on additional details or features you'd like to highlight.





