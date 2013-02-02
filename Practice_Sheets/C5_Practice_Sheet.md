# MAT013 - Practice Sheet
## Chapter 5
### Attempt to do the following in SAS and/or R.


1. Solve the following optimisation problem (we have not see how to do this in R): 
Maximise: $f(x_1,x_2,x_3)=x_1+x_2+5x_3+x_4^2$ subject to:

\begin{align}
3x_1+2x_2-x_3+x_4\leq& 1\\
-2x_1-3x_2+2x_3-x_4\leq&1\\
x_2-x_4\leq&8
\end{align}

2. Using SQL merge the data sets [weight.xls](https://www.dropbox.com/s/duadh282l6vtvzd/weight.xls) and [height.xls](https://www.dropbox.com/s/2i4rja2sh11od44/height.xls) and calculate the bmi. Obtain a new data set only with clinically obese individuals.

3. For the data set [demographics.csv](https://www.dropbox.com/s/pbjyln9ucp53kah/demographics.csv). Using SQL create 4  data sets that:

    1. contains all columns and all rows.
    2. contains the columns patientnum, surverynum, heightcm, weightkg, postcode and rows where postcode is not missing.
    3. contains mean values for heightcm and weightkg by postcode and ordered by postcode.
    4. contains mean values for bmi by postcode and ordered by postcode.

4. Download the data sets [queue_servers.csv](http://db.tt/QlTtWWOP), [queue_arrival_rates.csv](http://db.tt/ZabQhbeI) and [queue_service_rates.csv](http://db.tt/aXO5nqU7):

    1. Using the mathematical formulae seen in previous weeks obtain a new data set with the Number of the Queue, the service rate, the arrival rate and the mean queue length (note that the formulae only holds for $\lambda<c\mu$).
    2. Is there a correlation between the service rate and the queue length? Between the arrival rate and the queue length?
    3. Obtain a regression model for the mean queue length.

5. Attempt to redo all graphs (from the course) with the ggplot pckage (this is only relevant to R).
