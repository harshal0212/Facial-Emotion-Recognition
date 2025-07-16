import cv2
import numpy as np
from deepface import DeepFace
import os

class EmotionEngine:
    def __init__(self):
        self.emotion_mapping = {
            'angry': 'Angry',
            'disgust': 'Disgust', 
            'fear': 'Fear',
            'happy': 'Happy',
            'sad': 'Sad',
            'surprise': 'Surprise',
            'neutral': 'Neutral'
        }
        
        # Load face cascade using a more reliable method
        cascade_path = os.path.join(cv2.__path__[0], 'data', 'haarcascade_frontalface_default.xml')
        if os.path.exists(cascade_path):
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
        else:
            # Fallback to default path
            self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def preprocess_frame(self, frame):
        """Preprocess frame for better emotion detection"""
        # Resize frame to optimal size for DeepFace
        height, width = frame.shape[:2]
        if width > 640:
            scale = 640 / width
            new_width = int(width * scale)
            new_height = int(height * scale)
            frame = cv2.resize(frame, (new_width, new_height))
        
        # Enhance contrast slightly
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l, a, b])
        frame = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        return frame

    def detect_face(self, frame):
        """Detect if there's a face in the frame before running emotion analysis"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Use more sensitive parameters for face detection
        faces = self.face_cascade.detectMultiScale(gray, 1.05, 3, minSize=(30, 30))
        return len(faces) > 0

    def validate_emotion(self, emotion, emotion_scores):
        """Validate and clean emotion results"""
        if not emotion_scores:
            return "No Face Detected", {}
        
        # Get the dominant emotion
        dominant_emotion = emotion.lower()
        
        # Map to proper emotion name
        if dominant_emotion in self.emotion_mapping:
            emotion = self.emotion_mapping[dominant_emotion]
        else:
            emotion = "Neutral"
        
        # Check if confidence is reasonable
        confidence = emotion_scores.get(dominant_emotion, 0)
        if confidence < 0.1:  # Very low confidence
            return "No Face Detected", {}
        
        return emotion, emotion_scores

    def analyze(self, frame):
        try:
            # Preprocess the frame
            processed_frame = self.preprocess_frame(frame)
            
            # Check for face first
            if not self.detect_face(processed_frame):
                return "No Face Detected", {}
            
            # Convert to RGB for DeepFace
            rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            
            # Analyze emotion with optimized parameters
            result = DeepFace.analyze(
                rgb, 
                actions=['emotion'], 
                enforce_detection=False,
                detector_backend='opencv',
                align=True  # Enable face alignment for better accuracy
            )
            
            if isinstance(result, list):
                result = result[0]
            
            emotion = result['dominant_emotion']
            emotion_scores = result['emotion']
            
            # Validate and clean the emotion result
            emotion, emotion_scores = self.validate_emotion(emotion, emotion_scores)
            
            return emotion, emotion_scores
            
        except Exception as e:
            print(f"Emotion analysis error: {e}")
            return "No Face Detected", {} 