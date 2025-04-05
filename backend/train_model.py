from ultralytics import YOLO

# Load a pre-trained model
model = YOLO("yolov8s.pt")  # You can also use yolov8n.pt, yolov8m.pt etc.

# Train the model
model.train(
    data="My-First-Project-3/data.yaml",
    epochs=25,
    imgsz=640,
    batch=8,             # You can change based on your hardware
    project="runs",      # Output folder
    name="yolov8_custom",# Name of training run
    plots=True
)
