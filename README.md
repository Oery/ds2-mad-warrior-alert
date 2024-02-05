# Dark Souls II Mad Warrior Detection Script

## Overview

This script is designed to detect the presence of the Mad Warrior in Belfry Sol. Utilizing memory usage monitoring, the script identifies when the Mad Warrior spawns by detecting spikes in the game's memory usage. This approach is based on the unique increase in memory caused by the game loading the Mad Warrior's textures and model. When detected, the script will alert the player with a sound, enabling a more efficient farming experience.

## Features

-   **Audio Alerts:** Plays a sound alert when the Mad Warrior is detected.
-   **Real-time Memory Monitoring:** Continuously checks the memory usage of the Dark Souls II process.
-   **Automatic Detection:** Identifies memory spikes indicative of the Mad Warrior's presence.

## Prerequisites

Before running the script, ensure you have Python installed on your system. This script is compatible with Python 3.x and has been tested on Windows.

## Installation

1. **Clone the Repository**

-   Use Git to clone the repository to your local machine, or download the ZIP file directly from GitHub.

2. **Install Dependencies**

-   Navigate to the script's directory in your terminal or command prompt.
-   Run the following command to install the required Python libraries:

```sh
pip install -r requirements.txt
```

## Usage

To start monitoring Dark Souls II for the Mad Warrior spawn, follow these steps:

1. **Ensure Dark Souls II is Running**

-   Launch Dark Souls II and enter the game world.

2. **Add Sound / Change Settings**

-   Put your mp3 file next to the script
-   You can either rename it "mad_warrior_alert.mp3" or change the path used in the script

3. **Run the Script**

-   Open a terminal or command prompt window.
-   Navigate to the directory where the script is located.
-   Run the script with Python:

```sh
python mad_warrior_alert.py
```

4. **Monitor for Detection**

-   Keep resting and quitting the bonfire until an alert pops up
-   Note that with the default settings, teleporting using the feather will cause a false alert
-   You can change your Windows Terminal settings to set it as always on top. With it the window won't go away when you're focusing the game

## Configuration

-   **Process Name:** By default, the script monitors "DarkSoulsII.exe"
-   **Refresh Rate:** Set to 0.5 seconds by default. Adjust for more or less frequent checks.
-   **Memory Threshold:** A lower threshold will result in less false positives during loading screen but will also result in less ennemies detected.
-   **Sound Alert:** The path to the sound file for alert
