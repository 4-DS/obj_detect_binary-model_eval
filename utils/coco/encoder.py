import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, myobj):
        if isinstance(myobj, np.integer):
            return int(myobj)
        elif isinstance(myobj, np.floating):
            return float(myobj)
        elif isinstance(myobj, np.ndarray):
            return myobj.tolist()
        return json.JSONEncoder.default(self, myobj)


def load_coco_json(coco_file_path):
    with open(coco_file_path) as f:
        coco_data = json.load(f)
    return coco_data


def dump_coco_json(coco_file_path, coco_data):
    with open(coco_file_path, 'w') as f:
        json.dump(coco_data, f, cls=NumpyEncoder)

def encode_dict_to_numpy(_in_dict):
    return json.loads(json.dumps(_in_dict, cls=NumpyEncoder))