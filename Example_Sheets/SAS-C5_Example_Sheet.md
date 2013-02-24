# MAT013 - Example Sheet
## SAS: Chapter 5

1.  Re-produce the SAS code from the notes:

    1.  Using proc sql, create a copy of the MMM and JJJ data sets, including all the variables.

    2.  Using proc sql, create the previous copies selecting just the variables, Name, Age, Sex, random number, as well as the bmi of the observations.

    3.  For the following data set:

            Var1, Var2, Var3, Var4, Var5
            A, 1, A, 2, B
            A, 1, A, 2, B
            B, 1, A, 1, C
            C, 2, B, 2, D
            C, 2, C, 1, E

    1.  Create a copy of the data set removing complete duplicate rows.
    2.  Create a copy of the data set removing duplicates of Var2.
    3.  Create a copy of the data set removing duplicates of Var3 and Var4.
    4.  Create a copy of the data set selecting only observations where Var2 $>$ Var4.
    5.  Create a copy of the data set ordering by Var1.
    6.  Create a data set containing the mean, std, max, min and variance of Var4 and Var2 by Var1.


    4.  Download the data sets [dogs.csv](../Data/C5/dogs.csv) and [cats.csv](../Data/C5/cats.csv) use proc sql to:

        1.  create an inner join.
        2.  a left outer join.
        3.  a right outer join.
        4.  a full outer join.

    5.  Create a new function entitled "Gsum" and compute the geometric sum $\sum_{k=0}^ni^k$ for the following data set:

            n,i
            1,1
            2,1
            3,2
            4,2
            5,2
            6,2

    6.  Minimise the function $x^2-x-2y-xy+y^2$.

    7.  Minimise the above function for $x\leq 0$ and $y\geq 2$.

    8.  Solve the following optimisation problem:

        Maximise: $f(x_1,x_2,x_3)=x_1+x_2+x_3$ subject to:

        $$
        x_1,x_2,x_3\geq0$$
        $$
        3x_1+2x_2-x_3\leq 1$$
        $$
        -2x_1-3x_2+2x_3\leq1$$

The relevant data can be found [here](../Data/index.html):

- [dogs.csv](../Data/C5/dogs.csv)
- [cats.csv](../Data/C5/cats.csv)
