#MAT013 - R: C4 - Challenge Sheet
#Checking potential divisors of a number:

    23%%(2:sqrt(23))!=0
    24%%(2:sqrt(24))!=0

#Checking if any number is a divisor:

    all(23%%(2:sqrt(23))!=0)
    all(24%%(2:sqrt(24))!=0)

#Let us first build a function in R that tests if a number is prime:

    is_prime<-function(k){
        all(k%%(2:sqrt(k))!=0)
    }

#A function to create the required data frame:

    first_numbers<-function(k){
        df<-data.frame(1:k,sapply(1:k,is_prime(1:k))
        return(df)
    }

#A function to output this to a required file:

    first_number_output<-function(k,string){
        write.csv(first_numbers(k),paste(string,".csv",sep=""))
    }
