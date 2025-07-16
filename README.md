# Real-Time Face Mood Detection System

A high-performance real-time facial emotion recognition system built with Python, OpenCV, and DeepFace. Features a modern Tkinter GUI with real-time emotion analysis, FPS monitoring, and trend visualization.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![DeepFace](https://img.shields.io/badge/DeepFace-0.0.79+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

- **Real-time Emotion Recognition**: Detects 7 emotions (Happy, Sad, Angry, Fear, Disgust, Surprise, Neutral)
- **High Performance**: Optimized for maximum FPS with efficient processing
- **Modern GUI**: Dark-themed Tkinter interface with responsive design
- **Live Monitoring**: Real-time FPS counter and performance metrics
- **Confidence Scoring**: Detailed confidence scores for each detected emotion
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.8 or higher
- Webcam access
- Sufficient RAM (4GB+ recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/facial-emotion-recognition.git
   cd facial-emotion-recognition
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Using the GUI**
   - Click **▶ Start Detection** to begin real-time emotion analysis
   - View detected emotions and confidence scores on the video feed
   - Monitor live FPS and performance metrics
   - Click **⏹ Stop Detection** to end the session

## 📊 Features in Detail

### Emotion Recognition
- **7 Emotion Categories**: Happy, Sad, Angry, Fear, Disgust, Surprise, Neutral
- **Confidence Scoring**: Each emotion comes with a confidence percentage
- **Real-time Processing**: Continuous analysis with minimal latency

### Performance Optimizations
- **Frame Skipping**: DeepFace analysis runs every 10th frame for optimal FPS
- **Efficient Memory Management**: Optimized data structures and cleanup
- **Threading**: Smooth UI updates without blocking video processing
- **Frame Resizing**: Automatic resizing for better performance

### User Interface
- **Dark Theme**: Modern, eye-friendly interface
- **Real-time Stats**: Live FPS counter and emotion display
- **Responsive Design**: Adapts to different screen sizes
- **Status Indicators**: Clear feedback on system status

## 🏗️ Project Structure

```
facial-emotion-recognition/
├── app.py                 # Main application with GUI
├── emotion_engine.py      # Emotion detection engine
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

## 🧪 Testing

To test the system:

1. Ensure your webcam is working
2. Run the application
3. Position your face in the camera view
4. Try different facial expressions
5. Monitor the emotion detection accuracy

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**Webcam not detected:**
- Check if webcam is connected and working
- Ensure no other application is using the webcam
- Try running as administrator (Windows)

**Low FPS:**
- Close unnecessary applications
- Reduce frame resolution in the code
- Check system resources

**Installation errors:**
- Update pip: `pip install --upgrade pip`
- Install Visual C++ build tools (Windows)
- Use conda instead of pip if needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenCV](https://opencv.org/) for computer vision capabilities
- [DeepFace](https://github.com/serengil/deepface) for emotion recognition
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework

## 📞 Support

If you encounter any issues:
1. Check the [Issues](https://github.com/yourusername/facial-emotion-recognition/issues) page
2. Create a new issue with detailed information
3. Include your system specifications and error messages

---

**Made with ❤️ for the AI community** 