# This code contains the underlying Faster RCNN algorithm and frame detection for survivors
# @author1 Sahil Sharma
# @author2 Bidya Dash
# @group - JanhiTech


import torchvision
import cv2
from PIL import Image


model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person',    'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
   'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
   'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

class GodsEye:
    def __init__(self, clip, survivors=["person, cat, dog"], threshold=0.5):
        # cap = cv2.VideoCapture("disaster.avi")
        # cap = cv2.VideoCapture("videoplayback.mp4")
        self.cap = cv2.VideoCapture(clip)
        self.survivors = survivors
        self.threshold = threshold


    def get_prediction(self, frame, threshold=0):
        img = Image.fromarray(frame)
        transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
        img = transform(img)  # Apply the transform to the image
        model.cuda()
        img = img.cuda()
        pred = model([img])  # Pass the image to the model
        pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(pred[0]['labels'].detach().cpu().clone().numpy())]  # Get the Prediction Score
        pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(pred[0]['boxes'].detach().cpu().clone().numpy())]  # Bounding boxes
        pred_score = list(pred[0]['scores'].detach().cpu().clone().numpy())
        pred_t = [pred_score.index(x) for x in pred_score if x > threshold][-1]  # Get list of index with score greater than threshold.
        pred_boxes = pred_boxes[:pred_t + 1]
        pred_class = pred_class[:pred_t + 1]
        model.cuda.empty_cache()
        return pred_boxes, pred_class


    def object_detection_api(self, frame):
        boxes, pred_cls = self.get_prediction(frame, self.threshold)  # Get predictions
        for survivor in self.survivors:
            if survivor in pred_cls:
                return True
        return None

    def search(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to Gray scale
            if self.object_detection_api(frame):
                return True
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        # if done with search and nothing found
        self.cap.release()
        cv2.destroyAllWindows()
        return None


