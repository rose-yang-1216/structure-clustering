# structure-clustering

Example workflows for clustering protein structures based on structural features.

These scripts demonstrate simple approaches to exploring protein fold space by grouping structures based on structural descriptors.

## Repository Structure

```
structure-clustering/
│
├ cluster_structures.py     # Example clustering workflow
├ generate_features.py      # Example structural feature generation
├ requirements.txt
│
└ data/
   └ example_features.csv
```

## Installation

pip install -r requirements.txt

## Example

Generate features:

python generate_features.py

Run clustering:

python cluster_structures.py
