# MAT013 - Practice Sheet
## Chapter 5
### Attempt to do the following in SAS and/or R.


1. Solve the following optimisation problem (we have not see how to do this in R):
Maximise: $f(x_1,x_2,x_3)=x_1+x_2+5x_3+x_4^2$ subject to:

$$
3x_1+2x_2-x_3+x_4\leq 1$$
$$
-2x_1-3x_2+2x_3-x_4\leq 1$$
$$
x_2-x_4\leq 8$$


2. Using SQL merge the data sets [weight.xls](../Data/C3/weight.xls) and [height.xls](../Data/C3/height.xls) and calculate the bmi. Obtain a new data set only with clinically obese individuals.

3. For the data set [demographics.csv](../Data/C4/demographics.csv). Using SQL create 4  data sets that:

    1. contains all columns and all rows.
    2. contains the columns patientnum, surverynum, heightcm, weightkg, postcode and rows where postcode is not missing.
    3. contains mean values for heightcm and weightkg by postcode and ordered by postcode.
    4. contains mean values for bmi by postcode and ordered by postcode.

4. Download the data sets [queue_servers.csv](../Data/C5/queue_servers.csv), [queue_arrival_rates.csv](../Data/C5/queue_arrival_rates.csv) and [queue_service_rates.csv](../Data/C5/queue_service_rates.csv):

    1. Using the mathematical formulae seen in previous weeks obtain a new data set with the Number of the Queue, the service rate, the arrival rate and the mean queue length (note that the formulae only holds for $\lambda<c\mu$).
    2. Is there a correlation between the service rate and the queue length? Between the arrival rate and the queue length?
    3. Obtain a regression model for the mean queue length.

5. Attempt to redo all graphs (from the course) with the ggplot pckage (this is only relevant to R).
