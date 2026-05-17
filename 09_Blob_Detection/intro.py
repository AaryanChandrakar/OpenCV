# Standard imports
from pathlib import Path

import cv2
import numpy as np

# Read image relative to this script so it works from any working directory.
image_path = Path(__file__).resolve().parent / "blob.jpg"
im = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if im is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob.
im_with_keypoints = cv2.drawKeypoints(
    im,
    keypoints,
    np.array([]),
    (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
