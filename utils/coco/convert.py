import numpy as np

def convert_inference_results_to_coco(result, image, image_width, image_height, min_score: float = 0) -> dict:
    selected_classes = []
    selected_boxes = []
    selected_scores = []
    selected_cnts = []

    if result.bboxes.size > 0:
        selected_scores = result.scores
        selected_boxes = result.bboxes
        selected_classes = result.labels
        # print(selected_classes)
        # break

    box_to_cnt_indexes = [[0, 1], [2, 1], [2, 3], [0, 3], [0, 1]]
    for bbox in selected_boxes:
        cnt = []
        for a, b in box_to_cnt_indexes:
            cnt.append([bbox[a], bbox[b]])
        selected_cnts.append([cnt])
    
    image_id = image['id']
    
    
# def map_result_as_dict(selected_classes,  
#                    selected_cnts,
#                    selected_boxes,
#                    selected_scores,                        
#                    output_shape: tuple, 
#                    file_name: str = '', 
#                    image_id: int = 0, 
#                    min_score: float = 0) -> dict:
    """
        Optimized universal predictor
        :param selected_classes - numpy array of classes (-1,1)
        :param selected_cnts    - numpy array of contours (-1,-1,1,2)
        :param selected_boxes   - numpy array bbox (-1,4)
        :param selected_scores   - numpy array bbox (-1,1)
        :param output_shape     - output image shape. Usung only 2 first values
        :param file_name        - input file name
        :param use_segm         - using segmentation model or object detection only
        :param image_id         - input file id
        :param min_score        - filtering condition

        :return: dict
    """

    annotations = [{
        'id': i,
        'base_id': i,
        'image_id': int(image_id),
        # bbox x1,y1,w,h describing the object
        'bbox': [int(x1), int(y1), int(x2-x1), int(y2-y1)],
        # Object category
        #'category_id': loaded_categories_remap[int(selected_classes[i])],
        'category_id': int(selected_classes[i])+1,
        'score': float(selected_scores[i]),  # confidence
        # Contour array x,y,x,y
        'segmentation': [np.int0(_cnt).ravel().tolist() for _cnt in selected_cnts[i]],
    } for i, ((x1, y1, x2, y2), score) in enumerate(zip(selected_boxes,selected_scores)) if score > min_score]

    for i in range(len(annotations)):
        del annotations[i]['base_id']

    return {
        'file_name': image['file_name'],  # not used
        'height': image_height,  # Image Resolution
        'width': image_width,  # Image Resolution
        'image_id': int(image_id),
        #'CLASSES_COUNT': len(loaded_categories),
        'annotations': annotations
    }