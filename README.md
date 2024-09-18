# PRODIGY_CS_04
CREATING A KEYLOGGER PROGRAM

A keylogger, which is a short form for "keystroke logger" is a type of software or hardware created to record every keystroke typed on a keyboard.It also has the ability to capture input data and can save or transmit it for later review.Keyloggers should only be used with the explicit consent of the individuals being monitored, it is also necessary to inform the users about the presence and purpose of the keylogger in order to maintain transparency and ethical standards.Unauthorized use is illegal in most jurisdictions.

# Keylogger Project

This repository contains a simple keylogger implemented in Python. A keylogger records all keystrokes made by a user, which can be useful for monitoring or educational purposes. 

**Note:** This project is intended for educational purposes only. Unauthorized use of a keylogger is illegal and unethical. Always obtain explicit permission before using or deploying keylogging software.

## Features

- Captures all keystrokes made on the keyboard.
- Logs keystrokes to a local file.
- Runs in the background.
- Optionally, can be configured to send logs via email.

## Installation

To run this keylogger, you'll need Python 3.x installed on your system.

### Prerequisites

1. Install Python 3.x: [Python Official Website](https://www.python.org/downloads/)
2. Install the required Python libraries. Run the following command to install them:

   ```bash
   pip install -r requirements.txt
   ```

   Required libraries include:
   - `pynput`: for capturing keyboard events.

### Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Jewel326/PRODIGY_CS_04.git
cd keylogger-project
```

### Running the Keylogger

To start the keylogger, use the following command:

```bash
python keylogger.py
```

The keylogger will run in the background and save keystrokes to a log file named `keylog.txt` in the same directory.

### Stopping the Keylogger

To stop the keylogger, terminate the process using `Ctrl + C` in the terminal where it's running.

## Configuration

### Log File

By default, keystrokes are logged in `keylog.txt`. You can change the filename or path by modifying the `keylogger.py` script.

## Usage

- Ensure you have permission before deploying the keylogger.
- The keylogger logs all keystrokes to a file, which can be reviewed later.

## Legal and Ethical Considerations

This keylogger is provided for educational purposes only. Misuse of keylogging software can have serious legal consequences. Always ensure that you have explicit consent from all parties involved before deploying or using keylogging tools.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features. Contributions are welcome!

## License

This project is licensed under the MIT license.





