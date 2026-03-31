# Human Identification via LiDAR

## Project Overview
This project focuses on human identification using LiDAR data. The classification process involves the following steps:
1. Using the DBSCAN algorithm to calculate the point cloud density of the human torso.
2. Embedding the point cloud density into DCT (Discrete Cosine Transform) for feature extraction.
3. Training and classification using ECC-GCN (Edge-Conditioned Convolutional Graph Neural Network).



-----------------------------------------------------------------
Environment Setup
--- python -m venv venv
--- pip install -r requirements.txt




-----------------------------------------------------------------
## Execution Workflow

### 1. DBSCAN for Point Cloud Density Calculation
- Script: `DBSCAN_limbs.py`
- Functionality:
  - Processes point cloud data using the DBSCAN clustering algorithm to extract the density of the human torso.
  - Outputs processed point cloud data for subsequent steps.

### 2. DCT Feature Extraction
- Script: `DCT.py`
- Functionality:
  - Applies Discrete Cosine Transform (DCT) to the point cloud density data from DBSCAN, extracting embedded features.
  - Outputs embedded features for ECC-GCN input.

### 3. ECC-GCN Classification
- Script: `ECC_GCN.py`
- Functionality:
  - Utilizes Edge-Conditioned Convolutional Graph Neural Network (ECC-GCN) to classify the embedded features.
  - Outputs classification results after training.

---



## Usage

### 1. Run DBSCAN
Execute the following command to calculate the point cloud density of the human torso:
```bash
python3 DBSCAN_limbs.py
```
And save data in csv file.
### 2. Run DCT Feature Extraction
Execute the following command to perform feature embedding:
```bash
python3 DCT.py
```

### 3. Train ECC-GCN Model
Execute the following command to classify the data:
```bash
python3 ECC_GCN.py
```

---

## Project Structure
```
Human-identification-via-LiDAR/
├── DBSCAN_limbs.py
├── DCT.py
├── ECC_GCN.py
├── requirements.txt
├── README.md
└── figure code and figure/
    ├── building_block_ablation_study.py
    ├── different_GCN_layers.py
    ├── ...
```

---


