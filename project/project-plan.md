# Project Plan

## Title
<!-- Give your project a short title. -->
German Housing Prices Drop

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Why and what factors have led to the largest quarterly drop (Q4 2022) in housing prices in 16 years.?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Having a place which you call home is one of the basic necessity. In this project we will consider multiple factors like Consumer Price Index (Infaltion), Higher Interest Rates, Energy Crisis, etc that caused a significat drop in German Real Estate Market. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

We need multiple datasets for this projects

1. Consumer Price Index (Inflation Dataset) ✅
2. Interest Rate ✅
3. Energy Data (https://www.destatis.de/EN/Themes/Economy/Prices/Consumer-Price-Index/Tables/Consumer-prices-special.html#) ✅
4. Real Estate Data ✅

### Datasource1: Consumer Price Index
* Metadata URL: https://www.destatis.de/EN/Themes/Economy/Prices/Consumer-Price-Index/Tables/Consumer-prices-12-divisions.html#242102

* Data URL: https://www.destatis.de/EN/Themes/Economy/Prices/Consumer-Price-Index/Tables/Consumer-prices-12-divisions.html#242102

* Data Type: CSV

### Datasource2: Interest rate
* Metadata URL: https://www.statista.com/statistics/1312145/germany-inflation-rate-central-bank-rate-monthly/

    https://www.statista.com/statistics/1312145/germany-inflation-rate-central-bank-rate-monthly/#:~:text=PDF-,XLS,-PNG

* Data URL: https://www.destatis.de/EN/Press/2023/09/PE23_355_611.html

* Data Type: CSV

### Datasource3: Energy Crisis
* Metadata URL: https://www.destatis.de/EN/Themes/Economy/Prices/Consumer-Price-Index/Tables/Consumer-prices-special.html#242176


* Data URL: https://www.destatis.de/EN/Themes/Economy/Prices/Consumer-Price-Index/Tables/Consumer-prices-special.html#242176

Also check data columns in Consumer Price Indexes dataset


* Data Type: CSV

### Datasource4: Real Estate 
* Metadata URL: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=tabelleErgebnis&selectionname=61262-0002#abreadcrumb

* Data URL: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=tabelleErgebnis&selectionname=61262-0002#abreadcrumb

download or scrape this data as well https://www.destatis.de/EN/Themes/Economy/Prices/Construction-Prices-And-Real-Property-Prices/Tables/House-price-index-building-land.html#241682

* Data Type: CSV

### Short description of the Data Sources

The statistical data can be reused under the Data Licence Germany 2.0. This has been recognised by the Council of Experts of Open Definition as an open licence.
https://www.destatis.de/EN/Service/OpenData/opendata-einleitung.html#:~:text=The%20statistical%20data%20can%20be,Definition%20as%20an%20open%20licence.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Find Inflation, interest, Energy and Real Estate Datasets [#1][i1]
2. Use latest data in your analysis [#2][i2]
3. Upload Datasets on Publicaly Accessable Portal [#3][i3]
4. Retrieve all 4 different datasets and store them in /data [#4][i4]
5. Clean and Transform Each Dataset [#5][i5]
6. Find the Corelation and Drop the Extra Columns [#6][i6]
7. Merge Columns of Datasets [#7][i7]
8. Build Automated CI/CD Pipeline [#8][i8]
9. Create test.sh [#9][i9]
10. Perform Data Analysis [#10][i10]
11. Visualize Results [#11][i11]
12. Write Report on Findings [#12][i12]
13. Present Results [#13][i13]

[i1]: https://github.com/tayyab5800/made-project-ws2324/issues/1
[i2]: https://github.com/tayyab5800/made-project-ws2324/issues/2
[i3]: https://github.com/tayyab5800/made-project-ws2324/issues/3
[i4]: https://github.com/tayyab5800/made-project-ws2324/issues/4
[i5]: https://github.com/tayyab5800/made-project-ws2324/issues/5
[i6]: https://github.com/tayyab5800/made-project-ws2324/issues/6
[i7]: https://github.com/tayyab5800/made-project-ws2324/issues/7
[i8]: https://github.com/tayyab5800/made-project-ws2324/issues/8
[i9]: https://github.com/tayyab5800/made-project-ws2324/issues/9
[i10]: https://github.com/tayyab5800/made-project-ws2324/issues/10
[i11]: https://github.com/tayyab5800/made-project-ws2324/issues/11
[i12]: https://github.com/tayyab5800/made-project-ws2324/issues/12
[i13]: https://github.com/tayyab5800/made-project-ws2324/issues/13
