Benchmark Data
==============

This dataset is composed of large time series to test runtime performance of our algorithms. The data is generated with numpy using a random uniform distribution and seed state of 9999.

Data is generated with length N from 2^2 to 2^22; 4 to 4,194,304. Each text file has the length of the series in it's name.

Generate the data and compress it:
```
python generate_data.py
gzip *.txt
```
