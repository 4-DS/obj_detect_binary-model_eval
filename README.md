# Step CV-Pipeline: model_eval

This step CV-Pipeline: model_eval is intended for:
This stage of the CV Pipeline Model_Eval ensures model testing, performance evaluation, saving predictions for further analysis, and visualizing results using metrics and graphs.

Input data for step CV-Pipeline: model_eval
- **coco_test_dataset**     
Test dataset (from the CV-Pipeline component: data_prep)
- **bento_service**     
Model packaged in the BentoArchive from the model_pack step

## How to run a step CV-Pipeline: model_eval

### clone the repository: model_eval
```
git clone --recurse-submodules https://github.com/4-DS/obj_detect_binary-model_eval.git
cd obj_detect_binary-model_eval
```  

### run step CV-Pipeline:model_eval
```
python step.dev.py
```  
or
```
step.prod.py
``` 

