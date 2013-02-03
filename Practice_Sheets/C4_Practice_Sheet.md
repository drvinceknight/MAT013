# MAT013 - Practice Sheet
## Chapter 4
### Attempt to do the following in SAS and/or R.


1. Create code (in SAS: a macro, in R: a function) that gives

    1. The first $k$ even numbers.
    2. The first $k$ odd numbers.
    3. The square root of the first $k$ integers.
    4. The square root of the first $k$ integers, selecting only those that are integers.
    5. The first $k$ prime numbers (this is harder).

2. Write code that creates a data set with the mean of a given variable for a given data set. Experiment on the JJJ and MMM datasets.

3. Write code that merges two named data sets on a given variable. Remember to ensure that the data sets are sorted as required. Use this to merge the datasets [height.xls](../Data/C3/height.xls) and [weight.xls](../Data/C3/weight.xls) on the variable "obs" (seen in the previous lab sheet).

4. Download the data set [demographics.csv](../Data/C4/demographics.csv). Write code that creates another data set only containing a given postcode.

5. The mean number of people in an $M/M/k$ queue, where $\lambda$ denotes the inter arrival rate, $\mu$ denotes the service rate and $k$ denotes the system capacity is given by:
$$L_q=\frac{\left(\lambda/ \mu\right)^{k+1}\pi_0}{ kk!\left(1-{\lambda/ k\mu}\right)^2}$$
where $\pi_0$ is given on the week 2 exercise sheet. Write code that gives $L_q$  for given $\lambda,\mu$ and $k$. Make sure that your code only runs for ${\lambda\over k\mu}<1$.

6. Write code that calculates the monthly balance on a loan, for a given, initial balance, repayment value, interest rate and number of months.

    1. Adjust the code so that it displays a plot of balance against time.
    2. Adjust the code so that the plot has an appropriate title.

7. Modify the previous code so that it can output the required monthly repayment value to repay the loan within a given amount of time.
