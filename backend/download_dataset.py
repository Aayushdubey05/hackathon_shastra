
from roboflow import Roboflow

rf = Roboflow(api_key="Z2GYId3ljyTFfx6gAFFr")
project = rf.workspace("mesons314").project("my-first-project-osrtq")
version = project.version(3)
dataset = version.download("yolov8")

               