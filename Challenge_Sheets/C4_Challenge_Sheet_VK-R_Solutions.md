#MAT013 - R: C4 - Challenge Sheet
#Checking if a number is a divisor:

    23%%2 == 0
    24%%2 == 0

#Let us first build a function in R that tests if a number is a divisor of another:

    is_div<-function(a,n){
        a %% k
    }

#A function to create the required data frame:

    first_numbers<-function(k,n){
        data<-c()
        number<-0
        count<-0
        while(count<=k){
           if(is_div(n,number)){
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
