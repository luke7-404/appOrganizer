# App Launcher

**App Launcher** is a Python-based system tray application that lets users load and manage applications from a JSON configuration file. It provides an intuitive interface for launching applications and customizing the tray icon.

## Features
- Load and dynamically populate the tray menu with applications from a JSON file.
- Easily update the tray icon using an image file.
- Save and reload configuration settings, including the JSON file and icon path.
- Simple, user-friendly design with options to reload JSON, change the icon, or exit the application.

---

## Requirements

To run this application, ensure you have the following:

- **Python**: 3.6 or later
- Required Python packages:
  - `pystray`
  - `Pillow`
  - `tkinter`

---

## Installation

1. Clone or download the repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

---
## Build and use script (Windows instructions)
To make the script into a windows executable use ``pyinstaller``.
<ol>
    <li>Install <code>pyinstaller</code>: 
        <ol>
            <code>pip install pyinstaller</code>
        </ol>
    </li>
    <li>Create a <code>.exe</code>:
        <ol>
            <code>pyinstaller -- onefile --noconsole app.py
            </code>
            <br>
            This generates an executable file in the dist/ folder.</br>
        </ol>
    </li>
</ol>

### How to make the script run on start up
<ol>
    <li>Create a shortcut for <code>app.exe</code>
    </li>
    <li>Add shortcut to startup folder:
        <ol>
            <li>Run the command <code>win + r</code></li>
            <li>In the window type <code>shell:startup</code></li>
            <li>Add the <code>app.exe</code> shortcut to the folder that opened</li>
        </ol>
    </li>
</ol>

---

## Usage

### Menu Options:
1. **📂 Reload JSON**:
   - Opens a file dialog to select a JSON file.
   - Updates the tray menu with the apps listed in the file.

2. **🔄 Change Icon**:
   - Opens a file dialog to select an image file (`.png` or `.ico`).
   - Updates the tray icon.

3. **❌ Exit**:
   - Stops the application.

---

### JSON Configuration

The JSON file should be structured as follows:
```json
{
  "AppName1": "Path/To/App1.exe",
  "AppName2": "Path/To/App2.exe",
  "AppName3": "Path/To/App3.exe"
}
```

### Tray Icon
If no icon is specified, the app uses a default blue icon. To set a custom icon:
1. Click on **🔄 Change Icon**.
2. Select an image file (`.png` or `.ico`).

---

## Configuration File
The application saves configuration settings in `config.json`. This file includes:
- Path to the JSON file.
- Path to the selected icon.

### Example `config.json`:
```json
{
  "json_path": "path/to/apps.json",
  "icon_path": "path/to/icon.png"
}
```

---

## Development

### Code Structure
- **`main()`**: Initializes the tray application.
- **Dynamic Menu Updates**: Load apps and settings on the fly.
- **Helper Functions**:
  - `select_json_file()`: Opens a dialog to choose the JSON file.
  - `select_icon_file()`: Opens a dialog to choose an icon.
  - `update_menu()`: Refreshes the tray menu dynamically.

### Contribution
Feel free to fork the project and submit pull requests. Contributions are welcome!

---

## Troubleshooting

### Common Issues:
- **JSON Load Error**: Ensure the JSON file is properly formatted.
- **App Launch Error**: Verify the application paths in the JSON file.
- **Icon Load Error**: Ensure the selected image file exists and is supported.

### Debugging:
Run the app with Python to see detailed error messages in the console.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.