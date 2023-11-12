# Python-Selenium Automation Project

This project is a Python-based automation system that utilizes Selenium, a custom scheduler class, and advanced face detection and voice recognition technologies. It's designed to perform various tasks based on voice commands.

## Getting Started

### Prerequisites

- Python 3.x
- PyCharm, Visual Studio Code, or any other IDE that supports Python.
- A microphone for voice command input.

### Installation

1. Clone the repository to your local machine.
2. Open the project in your preferred IDE (e.g., PyCharm, Visual Studio Code).
3. Install all necessary dependencies by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt

4. You can run the project directly from your IDE by clicking the 'Play' button. Alternatively, to run the project from a terminal, navigate to the project directory and execute:

    ```bash
    python main.py

## Usage Instructions
Before using the application, ensure you have registered with the system and contacted the admin for face detection setup. This step is crucial for the application to recognize and validate your identity.

### Voice Commands
After your face is recognized, you can use voice commands within a 10-second window after the terminal prompts "You have 10 seconds to speak." The available commands include:

* __Playing Music__ : Say "play" followed by the song name in English. For example, "play Yesterday by The Beatles."

* __Checking the Weather__: Say a phrase including "weather" and the city's name. For example, "What's the weather in London?"

* __Collecting Online Data__: Simply say "data" to trigger this function.

### Configuration File
For the .env file and other configurations, please contact the admin.