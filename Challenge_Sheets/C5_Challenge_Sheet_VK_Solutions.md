#MAT013 - R: C5 - Challenge Sheet
#Creating a function to give required tweets on a given date

    orms_tweets_on_date<-function(date){
    length(searchTwitter('#orms', since=date,until=date+1,n=500))
    }

#Obtaining all the dates of the past week:

    dates_of_week<-function(string){
    as.Date(1:7,origin=Sys.Date()-7)
    }

#Getting the number of tweets:

    tweets_of_week<-sapply(dates_of_week(),orms_tweets_on_date)

#Plotting the number of tweets:

    p<-qplot(dates_of_week(),tweets_of_weel,xlab="Dates",ylab="Number of Tweets")
    p<-p+stat_smooth(method="lm")
    ggsave(p,"ORMS_tweets.png")
