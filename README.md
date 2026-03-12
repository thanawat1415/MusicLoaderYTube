# MusicLoaderYTube

A free and open-source tool to download music from YouTube as MP3 files, built with Python — no expensive subscriptions needed!

> **Based on:** [micahc123/FreeMusic](https://github.com/micahc123/FreeMusic)

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thanawat1415/MusicLoaderYTube.git
   ```

2. Navigate to the project directory:
   ```bash
   cd MusicLoaderYTube
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. *(macOS only)* Update Python SSL certificate:
   ```bash
   /Applications/Python\ 3.11/Install\ Certificates.command
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Choose one of the following options:
   - Enter `1` to input a music title manually.
   - Enter `2` to use a text file containing multiple music titles.

   If you choose option `2`, make sure to add one music title per line to `music_titles.txt` in the project folder.

3. The script will search for the music video on YouTube, download the audio, and save it as an MP3 file inside the `audio_files/` folder.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Credits

This project is based on [FreeMusic](https://github.com/micahc123/FreeMusic) by [micahc123](https://github.com/micahc123). Original concept and code used as the foundation for this project.
