# CS634_midterm_project
This is a midterm project of cs634.

There are **two** python files, generate_data.py and algorithm.py, in my project. First one is to generate transactions data, and the other one is for the algorithm. I wrote it into two different files because in this way I can check if different support or confidence gave different result. And there is a Result.ipynb which combine both files and show the output of the code. The packages used are random and itertools.

In **generate.py**, the first idea is to generate the transactions randomly, but it seems that it is not easy to see the association if the transactions are all random. Therefore, I create a list which I can let every item show exactly how many times I want. And now, the frequency of each item is controllable. The output of generate.py is five files, dict_0.txt, dict_1.txt, dict_2.txt, dict_3.txt, and dict_4.txt. Each of them is a database contains 20 transactions.

In **algorithm.py**, it required 3 input data, filename, min_support, and min_confidence. The filename is for the users to choose which of five databases, and the min_support and the min_condfidence is for the users to set the minimum of support and confidence value. After reading in the database, the first thing I do is compute the 1-item support. Keep whose support is greater than the minimum support, and go on for the k-items support. After having the final result, generate the all the association rules and compute the confidence. Thus, there is the final result. I print out every rule, and its support and condifence.



