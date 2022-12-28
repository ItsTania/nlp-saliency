# NLP Saliency
This project was extended from the machine ethics homework project from the MLSS2022 course (https://course.mlsafety.org/calendar/).

## [Table of Contents](#table-of-contents)
1. [About](#about)
   * [Overview](#overview)
2. [Usage](#usage)
3. [Project Organization](#project-organization)

## [About](#about)
The goal of the project was to manually implement an NLP saliency map to: 
  1. learn how to utilise a model's gradients and 
  2. to explain the model output and potential biases

The first half of the notebook is guided by the homework questions. For the assignment, we did our analysis on sentiment analysis and the IMDB dataset. **This project extends the methods learnt in the, I did my analysis on 'morality' models trained on reddits 'r/Am I the Arsehole'**. Additionally, the second half contains additional experimentation. 

I have noted which parts of the code were not my own work.

### [Overview](#overview)


## [Notebooks](#notebooks)
1. `01_saliency_map.ipynb` 
   - a walkthrough of how I implemented a saliency map in pytorch
2. `02_further_analysis.ipynb` 
   - further model explainatory understanding 

## [Project Organization](#project-organization)

    ├── .gitignore                    <- files and folders to be ignored by version control system
    ├── README.md                     <- The top-level README for developers using this project.
    ├── data
    │   ├── external                  <- Data from third party sources.
    │   └── processed                 <- The final, canonical data sets for modeling.
    │
    ├── models                        <- Trained and serialized models, model predictions, or model summaries
    │
    ├── figures                       <- Generated graphics and figures to be used in reporting
    ├── *.ipynb                       <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                    and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt              <- The requirements file for reproducing the analysis environment, e.g.
    │                                    generated with `pip freeze > requirements.txt`
    └── utils.py                      <- Reu
--------

