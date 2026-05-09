from pathlib import Path

import cv2


IMAGE_PATH = Path("input-image-for-demo-throughout-1024x682.jpg")
OUTPUT_DIR = Path("saved_patches")
PATCH_HEIGHT = 76
PATCH_WIDTH = 104

img = cv2.imread(str(IMAGE_PATH))
if img is None:
    raise FileNotFoundError(f"Could not read image: {IMAGE_PATH.resolve()}")

image_copy = img.copy()
imgheight, imgwidth = img.shape[:2]
OUTPUT_DIR.mkdir(exist_ok=True)

saved_count = 0

for y in range(0, imgheight - PATCH_HEIGHT + 1, PATCH_HEIGHT):
    for x in range(0, imgwidth - PATCH_WIDTH + 1, PATCH_WIDTH):
        y1 = y + PATCH_HEIGHT
        x1 = x + PATCH_WIDTH

        tile = image_copy[y:y1, x:x1]
        output_path = OUTPUT_DIR / f"tile{x}_{y}.jpg"

        if cv2.imwrite(str(output_path), tile):
            saved_count += 1

        cv2.rectangle(img, (x, y), (x1 - 1, y1 - 1), (0, 255, 0), 1)

cv2.imwrite(str(OUTPUT_DIR / "patch_grid.jpg"), img)
print(f"Saved {saved_count} patches to {OUTPUT_DIR.resolve()}")
