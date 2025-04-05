import os
import json
from tqdm import tqdm

def convert_coco_json_to_yolo(json_path, save_dir):
    with open(json_path, 'r') as f:
        data = json.load(f)

    images = {img['id']: img for img in data['images']}
    categories = {cat['id']: cat['name'] for cat in data['categories']}

    # Create the labels folder
    label_dir = os.path.join(os.path.dirname(json_path), "labels")
    os.makedirs(label_dir, exist_ok=True)

    for ann in tqdm(data['annotations'], desc=f"Processing {json_path}"):
        image_id = ann['image_id']
        image_info = images[image_id]
        file_name = image_info['file_name']
        width = image_info['width']
        height = image_info['height']
        category_id = ann['category_id']
        bbox = ann['bbox']  # [x, y, width, height]

        # Convert bbox to YOLO format: [x_center, y_center, width, height]
        x_center = (bbox[0] + bbox[2] / 2) / width
        y_center = (bbox[1] + bbox[3] / 2) / height
        w = bbox[2] / width
        h = bbox[3] / height

        # One file per image
        txt_filename = os.path.splitext(file_name)[0] + ".txt"
        label_path = os.path.join(label_dir, txt_filename)

        with open(label_path, 'a') as f:
            f.write(f"{category_id - 1} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")


# Paths to your annotation files
base_path = "My-First-Project-3"

for split in ["train", "valid", "test"]:
    json_file = os.path.join(base_path, split, "_annotations.coco.json")
    convert_coco_json_to_yolo(json_file, base_path)
