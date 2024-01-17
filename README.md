# Data Engineering in Real Estate

[![Licence](https://img.shields.io/badge/Licence-MIT-orange)](https://opensource.org/license/mit/)
[![pipeline status](https://github.com/tayyab5800/made-project-ws2324/actions/workflows/project-work-5-run-tests.yml/badge.svg)](https://github.com/tayyab5800/made-project-ws2324/actions/workflows/project-work-5-run-tests.yml)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

![alt text](cover.png "Title")

In this project we will analyse the main factors which affected the real estate market in Germnay in Q4 2022 and why it was droped to record low of last 16 years.

# Development

Clone the Repository:

```
git clone https://github.com/tayyab5800/made-project-ws2324.git
```

To run pipeline:

```
bash project/pipeline.sh
```

It will first create a virtual environment and later install all the required packages in this environment.

# Testing

To run the tests, you need to the following command:

```
bash project/pipeline.sh
```

- NOTE: to run pipeline and tests, make sure you are at the root of the repository.

# Pipeline

The pipeline encompasses the process of ETL within. The first step is to download the data and make it available for next processes. Secondly, the process of transformation took place where we are cleaning the data for further analysis. In the third step we are loading this enriched data and use it for visualization. After this whole analysis is finished we cleanup the downlaoded data to save local space.

# Report:

Here is the report link which also shows some Exploratory Data Analysis.

- #### Interactive Live Report

  - [German Real Estate Market Analysis Report](https://nbviewer.org/github/tayyab5800/made-project-ws2324/blob/main/report.html)
  
- #### Static Report

  ```
  cd project/report.pdf
  ```
- #### Source Code of Report

  ```
  cd project/report.ipynb
  ```

# Blog Posts:

Following are the 2 blog post which also point out the same issue of Deuchland Housing Crises

1. [German housing prices drop in Q4 2022, signaling end to boom](https://www.dw.com/en/german-housing-prices-drop-in-q4-2022-signaling-end-to-boom/a-65108677)
2. [Germany sees property prices drop in 14 major cities](https://www.thelocal.de/20230824/germany-sees-property-prices-drop-in-14-major-cities)

# Issues

If you encounter any issues or have any suggestions for improvement, please create a new issue on Github. I appreciate your feedback and and contributions!
