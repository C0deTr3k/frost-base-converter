# frost-base-converter


## Overview
Frost Converter is a user-friendly Kivy-based app for converting numbers between different number systems (Decimal, Binary, Octal, Hexadecimal). The app features an intuitive graphical interface with buttons for selecting the input and output base and provides a visually appealing layout with background images. A mobile app version is also available, allowing seamless usage on Android devices.

## Features
- Convert between Decimal, Binary, Octal, and Hexadecimal.
- User-friendly interface with dropdown options for choosing the number systems.
- Visually appealing design with a background image and customized button sizes.
- Instant conversion and clear button to reset input fields.
- **Mobile Version:** A mobile app version built using Kivy allows easy conversion on Android.

## Usage
1. Input the value you want to convert.
2. Select the base of the input value (Decimal, Binary, Octal, Hexadecimal).
3. Select the base to which you want to convert.
4. Press the "Convert" button to display the result.
5. Press the "Clear" button to reset the fields.

## Requirements
- Python 3.8+
- Kivy
- Any other dependencies should be installed using `pip install -r requirements.txt`.

## How to Run (Desktop Version)
1. Clone the repository:  
   `git clone https://github.com/yourusername/frost-converter-app.git`
2. Install dependencies:  
   `pip install kivy`
3. Run the app:  
   `python main.py`

## How to Run (Mobile Version)
1. Install **BeeWare** or **Buildozer** for packaging the app.
2. Package the app into an APK using Buildozer:  
   `buildozer -v android debug`
3. Install the APK on your Android device.

 ##License
This project is licensed under the MIT License.
