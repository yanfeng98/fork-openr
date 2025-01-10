# Preprocess datasets for OpenR

## Usage

```bash
usage: python cli.py [-h] [-t STEP_TAG] [-s SUFFIX]
              DATASET_TYPE FILE

positional arguments:
  DATASET_TYPE             Which dataset FILE is (math-aps, or math-aps-tree)
  FILE                     Path to the original dataset file

options:
  -h, --help               show this help message and exit
  -t, --step-tag STEP_TAG  Step tag. Default: \n\n\n\n\n
  -s, --suffix SUFFIX      Suffix appended to FILE for the output path. Default: new
```

---

```bash
python cli.py math-aps-tree ../data/omegaPRM_v2/output_results_data/results_part_1/math-aps-v2.jsonl
```

## Datasets

- Math-APS: collected by `data/omegaPRM_v2/` with `save_data_tree=False`
- Math-APS-tree: collected by `data/omegaPRM_v2/` with `save_data_tree=True`
