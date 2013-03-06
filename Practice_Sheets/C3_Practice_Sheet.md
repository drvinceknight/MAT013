# MAT013 - Practice Sheet
## Chapter 3
### Attempt to do the following in SAS and/or R.


1. Download the data sets [weight.xls](../Data/C3/weight.xls) and [height.xls](../Data/C3/height.xls):

    1. Create a SAS data set containing the bmi of the observations.
    2.  Output the data set to csv.

2.  For the concatenated data set (of JJJ and MMM):

    1. For individuals over the age of 25, calculate the yearly average savings (for each year after their 25th birthday)
    2. Output a frequency table showing the mean yearly average by sex. (You will need to find out some information on the ``tabulate'' procedure).
    3. Obtain the mean yearly average savings by sex and age groups:

        - Group A [0,18]
        - Group B [19,65]
        - Group C [66,]

    4. Find the mean, max and min for the variable ``random number'' and output this to a SAS data set.

3. Create (seperate) data sets containing the following:

    1. The first 200 odd numbers;
    2. The square root of the first 1000 integers;
    3. The square root of the first 10000 integers, selecting only those that are integers
    4. The first 20 prime numbers (this is slightly harder)

4. Download the file [coordinates.csv](../Data/C3/coordinates.csv).

    1. Obtain coefficients for a line fitted to the coordinates $(x,y)$ of this data set.
    2. For each of the observations create a new variable giving the following:

        1. The product $xy$;
        2. The ration $x/y$;
        3. The exponent $x^y$;
        4. The sum $x+y$;
        5. The difference $x-y$;
        6. The absolute value of $x$;
        7. The square root of $x$;
        8. The log to the base 10 $\log_{10}(x)$;
        9. The natural log $\ln(x)$.

    3. Obtain the following for the above data set (including the newly created variables):

        1. minimum
        2. maximum
        3. total
        4. mean
        5. median

5. The probability that an $M/M/k$ queue is empty is given by the following formulae:
$$\pi_0=\frac{1}{\sum_{i=0}^{k-1}\frac{(\lambda/\mu)^i}{i!}+\frac{(\lambda/\mu)^k}{k!(1-\lambda/(k\mu))}}$$

Obtain $\pi_0$ for $\lambda\in\{.1,.5,.7,.9\}$, $k=3$ and $\mu=1$.

6. Download the data set [marks.csv](../Data/marks.csv)

    1. Create a data set that shows the percentage increase or decrease of marks for each student from one month to the next.
    2. Obtain a table showing the mean of these percentage changes categorized by gender.

7. Download the data set [numbers.csv](../Data/numbers.csv) and create the following variables:

    1. $y1=x1\times x2\times \dots x36$
    2. $y2=\left(1+z1/1\right)\times\left(1+z2/2\right)\times\dots\left(1+z36/36\right)$
    3.  $y3=x1-x2+x3-\dots-x36$
