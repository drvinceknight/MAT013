#MAT013 - R: C4 - Challenge Sheet
#Checking if a number is a divisor:

    23%%2 == 0
    24%%2 == 0

#Let us first build a function in R that tests if a number is a divisor of another:

    is_div<-function(a,k){
        k %% a == 0
    }

#Here's a function to test if a number is prime:

    is_prime<-function(k){
        max(sapply(2:sqrt(k),function(x) is_div(x,k)))==0
    }

#A function to create the required data frame:

    first_primes<-function(k){
        data<-c()
        number<-0
        count<-0
        while(count<=k){
           if(is_primt(number)){
               data<-c(data,number)
               count<-count+1
           }
           number<-number+1
        }
        return(data.frame(data))
    }

#A function to output this to a required file:

    first_number_output<-function(k,string){
        write.csv(first_numbers(k),paste(string,".csv",sep=""))
    }
