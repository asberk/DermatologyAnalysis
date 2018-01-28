# DermatologyAnalysis

## Description

Predicting Erythemato-Squamous Diseases (ESD) disease using Random Forests.

## Report

The report for this project can be found here: [dermatology_analysis.ipynb](dermatology_analysis.ipynb)

## Data Source

The data can be obtained [here](http://archive.ics.uci.edu/ml/datasets/Dermatology).

## Dependencies

```bash
pip3 install pandas, numpy, sklearn, matplotlib, seaborn, pandas_ml
```

Python Version: 3.5+

## Usage Instructions

### Download the data:

```bash
cd /SOME/PATH/HERE
git clone https://github.com/TariqAHassan/DermatologyAnalysis.git
```

### Download the data:

```bash
$ python3 data/download.py
```

### Load the notebook

```bash
$ jupyter notebook
```

> You can ue `Kernel` > `Restart and Run All` in the
> menu bar to run the notebook from scratch.

> If you'd like to generate the single plot I created in R again, you can run:

```bash
$ Rscript dermatology_analysis/r_vizualizations.R
```

## About

Tariq Hassan, Jan. 2018.