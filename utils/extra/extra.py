from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

import numpy as np
import logging

logger = logging.getLogger(__name__)

class ExtraEval():
    def __init__(self,
                 cocoGt: COCO = None,
                 cocoDt: COCO = None,
                 iou_type: str = 'bbox',
                 min_score: float = 0,
                 iou_tresh: float = 0.0,
                 recall_count: int = 100,
                 useCats: bool = False,
                 ):
        self.iouType = iou_type
        self.min_score = min_score
        self.iou_tresh = iou_tresh
        self.useCats = useCats
        self.recall_count = recall_count
        self.cocoGt = cocoGt
        self.cocoDt = cocoDt

        self.evaluate()

    def evaluate(self):
        cocoEval = COCOeval(self.cocoGt, self.cocoDt, self.iouType)
        cocoEval.params.maxDets = [len(self.cocoGt.anns)]

        cocoEval.params.iouThrs = [self.iou_tresh]
        cocoEval.params.areaRng = [[0, 10000000000]]
        self.recThrs = np.linspace(0, 1, self.recall_count + 1, endpoint=True)
        cocoEval.params.recThrs = self.recThrs

        cocoEval.params.useCats = int(self.useCats)  # Выключение labels
        
        self.cocoEval = cocoEval

        cocoEval.evaluate()
        cocoEval.accumulate()
        
        self.eval = cocoEval.eval