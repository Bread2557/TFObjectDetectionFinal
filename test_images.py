from pathlib import Path
import imghdr

data_dir = "C:\\Projekte\\Python\\P310TFODTest\\Tensorflow\\workspace\\images\\test"
image_extensions = [".png", ".jpg", ".jpeg"]  # add there all your images file extensions

img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix == ".xml":
        image_path = filepath.parent / filepath.stem
        if not any(image_path.with_suffix(ext).exists() for ext in image_extensions):
            print("No image found for xml file: " + str(filepath))
    elif filepath.suffix in image_extensions:
        xml_path = filepath.parent / (filepath.stem + ".xml")
        if not xml_path.exists():
            print("No xml found for image file: " + str(filepath))
    if filepath.suffix.lower() in image_extensions:
        img_type = imghdr.what(filepath)
        if img_type is None:
            print(f"{filepath} is not an image")
        elif img_type not in img_type_accepted_by_tf:
            print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
