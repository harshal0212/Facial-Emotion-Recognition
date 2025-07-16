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
- **Emotion Trends**: Analysis and visualization of emotion patterns
- **Confidence Scoring**: Detailed confidence scores for each detected emotion
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.8 or higher
- Webcam access
- Sufficient RAM (4GB+ recommended)
- GPU support (optional, for enhanced performance)

## 🛠️ Installation

### Prerequisites

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

### Dependencies

The following packages will be installed:
- `opencv-python>=4.8.0` - Computer vision and video processing
- `deepface>=0.0.79` - Deep learning-based emotion recognition
- `numpy>=1.21.0` - Numerical computing
- `Pillow>=9.0.0` - Image processing

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

3. **Performance Tips**
   - Ensure good lighting for better accuracy
   - Position your face clearly in the camera view
   - Close unnecessary applications to free up system resources

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

## 🔧 Configuration

### Customization Options

You can modify the following parameters in `app.py`:

```python
# Emotion update interval (seconds)
self.emotion_update_interval = 0.8

# Frame resize dimensions
frame = cv2.resize(frame, (640, 480))

# GUI window size
self.root.geometry('1000x800')
```

### Performance Tuning

- **Increase FPS**: Reduce `emotion_update_interval` or frame resolution
- **Improve Accuracy**: Increase `emotion_update_interval` for more frequent analysis
- **Memory Usage**: Adjust frame buffer size based on available RAM

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

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test on multiple platforms if possible

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

**Memory issues:**
- Increase system RAM
- Reduce frame buffer size
- Close other memory-intensive applications

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenCV](https://opencv.org/) for computer vision capabilities
- [DeepFace](https://github.com/serengil/deepface) for emotion recognition
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/facial-emotion-recognition/issues) page
2. Create a new issue with detailed information
3. Include your system specifications and error messages

## 🔮 Future Enhancements

- [ ] Support for multiple faces
- [ ] Emotion history tracking
- [ ] Export functionality for analysis data
- [ ] Mobile app version
- [ ] API for integration with other applications
- [ ] Custom emotion models training

---

**Made with ❤️ for the AI community** 