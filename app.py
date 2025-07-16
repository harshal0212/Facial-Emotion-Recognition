import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from emotion_engine import EmotionEngine
import time
import threading

class FaceDetectionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Real-Time Face Mood Detection System')
        self.root.geometry('1000x800')
        self.root.configure(bg='#1e1e1e')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 12, 'bold'), padding=10)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="Real-Time Face Mood Detection", 
                              font=('Arial', 24, 'bold'), bg='#1e1e1e', fg='#ffffff')
        title_label.pack(pady=(0, 20))
        
        # Video frame
        video_frame = tk.Frame(main_frame, bg='#2d2d2d', relief='raised', bd=2)
        video_frame.pack(pady=10)
        
        self.video_label = tk.Label(video_frame, bg='#2d2d2d', relief='sunken', bd=2)
        self.video_label.pack(padx=10, pady=10)
        
        # Info display frame
        info_frame = tk.Frame(main_frame, bg='#1e1e1e')
        info_frame.pack(fill='x', pady=10)
        
        self.emotion_label = tk.Label(info_frame, text="Emotion: Waiting...", 
                                     font=('Arial', 18, 'bold'), bg='#1e1e1e', fg='#00ff00')
        self.emotion_label.pack()
        
        self.fps_label = tk.Label(info_frame, text="FPS: 0", 
                                 font=('Arial', 10), bg='#1e1e1e', fg='#ff8800')
        self.fps_label.pack()
        
        # Control buttons frame
        button_frame = tk.Frame(main_frame, bg='#1e1e1e')
        button_frame.pack(pady=20)
        
        self.start_btn = ttk.Button(button_frame, text='▶ Start Detection', command=self.start, width=20)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = ttk.Button(button_frame, text='⏹ Stop Detection', command=self.stop, state=tk.DISABLED, width=20)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        # Status bar
        self.status_label = tk.Label(main_frame, text="Ready to start", 
                                    font=('Arial', 10), bg='#1e1e1e', fg='#888888')
        self.status_label.pack(side=tk.BOTTOM, pady=10)
        
        # Initialize variables
        self.running = False
        self.cap = None
        self.engine = EmotionEngine()
        self.frame_count = 0
        self.prev_time = time.time()
        self.thread = None
        self.fps_counter = 0
        self.fps_time = time.time()
        self.last_emotion_time = 0
        self.emotion_update_interval = 0.8
        self.current_emotion = "Waiting..."

    def start(self):
        if not self.running:
            self.running = True
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.status_label.config(text="Error: Cannot access webcam", fg='#ff0000')
                self.running = False
                return
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.status_label.config(text="Detection active", fg='#00ff00')
            self.thread = threading.Thread(target=self.update, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Detection stopped", fg='#888888')
        self.emotion_label.config(text="Emotion: Waiting...")
        self.fps_label.config(text="FPS: 0")

    def update(self):
        while self.running and self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
                
            self.frame_count += 1
            self.fps_counter += 1
            current_time = time.time()
            
            # Calculate FPS
            if current_time - self.fps_time >= 1.0:
                fps = self.fps_counter / (current_time - self.fps_time)
                self.fps_label.config(text=f"FPS: {fps:.1f}")
                self.fps_counter = 0
                self.fps_time = current_time
            
            # Run emotion detection
            if current_time - self.last_emotion_time >= self.emotion_update_interval:
                try:
                    emotion, emotion_scores = self.engine.analyze(frame)
                    
                    # Only update if we got a valid emotion
                    if emotion and emotion != "No Face Detected":
                        self.current_emotion = emotion
                        self.last_emotion_time = current_time
                    elif emotion == "No Face Detected":
                        # Keep the last emotion for a short time when no face is detected
                        if current_time - self.last_emotion_time > 2.0:
                            self.current_emotion = "No Face Detected"
                            
                except Exception as e:
                    print(f"Emotion detection error: {e}")
                    self.current_emotion = "Error"
            
            # Draw info on frame
            cv2.rectangle(frame, (5, 5), (250, 50), (45, 45, 45), -1)
            cv2.putText(frame, f"Emotion: {self.current_emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Resize frame for better performance
            frame = cv2.resize(frame, (640, 480))
            
            # Convert to PIL and display
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Update GUI in main thread to prevent flickering
            self.root.after(0, self.update_gui, imgtk)
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.03)
            
        if self.cap:
            self.cap.release()

    def update_gui(self, imgtk):
        """Update GUI elements in main thread to prevent flickering"""
        if not self.running:
            return
            
        # Update video frame
        self.video_label.configure(image=imgtk)
        self.imgtk = imgtk  # Keep reference
        
        # Update labels
        self.emotion_label.config(text=f"Emotion: {self.current_emotion}")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = FaceDetectionApp()
    app.run() 