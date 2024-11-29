import json
import os
import subprocess
from pystray import Icon, Menu, MenuItem
from PIL import Image
from tkinter import Tk, filedialog

# Path to save the configuration file
CONFIG_FILE = "config.json"


def select_json_file():
    """Open a file dialog to select a JSON file."""
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a JSON file",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
    )
    return file_path


def select_icon_file():
    """Open a file dialog to select an icon image file."""
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select an Icon Image",
        filetypes=[("Image Files", "*.png;*.ico"), ("All Files", "*.*")]
    )
    return file_path


def save_config(json_path, icon_path=None):
    """Save the JSON file path and icon path to the config file."""
    config = {"json_path": json_path}
    if icon_path:
        config["icon_path"] = icon_path
    try:
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file)
    except Exception as e:
        print(f"Error saving configuration: {e}")


def load_config():
    """Load the JSON file path and icon path from the config file."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading configuration: {e}")
    return {"json_path": "", "icon_path": ""}


def load_apps_from_json(icon, item):
    """Load the JSON file and populate the menu with app options."""
    file_path = select_json_file()
    if file_path and os.path.exists(file_path):
        save_config(file_path)  # Save the selected JSON file path
        try:
            with open(file_path, 'r') as file:
                apps = json.load(file)
                # Update the tray menu dynamically
                update_menu(icon, apps)
        except Exception as e:
            print(f"Error loading JSON file: {e}")


def create_app_menu_item(app_name, app_path):
    """Create a menu item for an app."""
    return MenuItem(app_name, lambda: open_app(app_path))


def update_menu(icon, apps: dict):
    """Update the tray menu with app entries."""
        # Populate with apps
    # Use the helper function to create menu items
    app_items = [create_app_menu_item(app_name, app_path) for app_name, app_path in apps.items()]


    # Separate apps and Add menu functions (Reload json, change icon, exit)
    menu_items = app_items + [
        Menu.SEPARATOR,
        MenuItem("📂 Reload JSON", lambda: load_apps_from_json(icon, None)),
        MenuItem("🔄 Change Icon", lambda: update_icon(icon)),
        MenuItem("❌ Exit", lambda: icon.stop())
    ]

    # Update the menu
    icon.menu = Menu(*menu_items)


def open_app(app_path):
    """Open the application with the specified path."""
    try:
        subprocess.Popen(app_path, shell=True)
    except Exception as e:
        print(f"Error opening app {app_path}: {e}")


def create_image(icon_path=None):
    """Create an image for the system tray icon."""
    if icon_path and os.path.exists(icon_path):
        try:
            return Image.open(icon_path)
        except Exception as e:
            print(f"Error loading icon file: {e}")
    # Default icon
    return Image.new("RGBA", (64, 64), "blue")


def update_icon(icon):
    """Update the tray icon dynamically."""
    icon_path = select_icon_file()
    if icon_path and os.path.exists(icon_path):
        config = load_config()
        save_config(config.get("json_path", ""), icon_path)  # Save icon path to config
        icon.icon = create_image(icon_path)  # Update the icon
        icon.update_icon()


def main():
    """Set up and run the system tray application."""
    config = load_config()
    json_path = config.get("json_path", "")
    icon_path = config.get("icon_path", "")

    # Load apps from JSON if the path exists
    apps = {}
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r') as file:
                apps = json.load(file)
        except Exception as e:
            print(f"Error loading apps from JSON file: {e}")

    # Create the system tray icon
    icon = Icon("App Launcher", create_image(icon_path), "App Launcher")

    # Initial menu with apps (if any) and options
    update_menu(icon, apps)

    # Run the system tray icon
    icon.run()


if __name__ == "__main__":
    main()
