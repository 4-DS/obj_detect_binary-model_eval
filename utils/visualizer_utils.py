# TODO: вынести в функцию
from mmengine.registry import VISUALIZERS
from typing import Optional
from mmengine.visualization import Visualizer

def build_visualizer():
    try:
        @VISUALIZERS.register_module()
        class DetLocalVisualizer(Visualizer):
            def add_datasample(self,
                               name,
                               image: np.ndarray,
                               data_sample: Optional['BaseDataElement'] = None,
                               draw_gt: bool = False,
                               draw_pred: bool = True,
                               show: bool = False,
                               wait_time: int = 0,
                               step: int = 0) -> None:
                pass
    except Exception as e:
        print(e.__str__)

    visualizer_cfg = dict(type='DetLocalVisualizer',
                          vis_backends=[dict(type='LocalVisBackend')],
                          name='visualizer')

    # global initialize
    VISUALIZERS.build(visualizer_cfg)
    return Visualizer.get_current_instance()