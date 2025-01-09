# Preprocess datasets for OpenR

## Usage

```bash
usage: python cli.py [-h] [-t STEP_TAG] [-s SUFFIX]
              [--add-step-prefix] [--neutral-is-bad]
              DATASET_TYPE FILE

positional arguments:
  DATASET_TYPE             Which dataset FILE is (prm800k, math-aps, math-aps-tree, or math-shepherd)
  FILE                     Path to the original dataset file

options:
  -h, --help               show this help message and exit
  -t, --step-tag STEP_TAG  Step tag. Default: \n\n\n\n\n
  -s, --suffix SUFFIX      Suffix appended to FILE for the output path. Default: new
      --add-step-prefix    Prepend "Step i: " to each step. PRM800K only
      --neutral-is-bad     Treat `neutral` as negative labels for PRM800K. PRM800K only
```

## Datasets
- PRM800K: [GitHub repo](https://github.com/openai/prm800k)
- Math-APS: collected by `data/omegaPRM_v2/` with `save_data_tree=False`
- Math-APS-tree: collected by `data/omegaPRM_v2/` with `save_data_tree=True`
- Math-Shepherd: [Hugging Face dataset](https://huggingface.co/datasets/peiyi9979/Math-Shepherd)
