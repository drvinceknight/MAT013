#MAT013 - R: C4 - Challenge Sheet
# A data set with the required numbers:

    data tmp_file;
    number=0;
    count=0;
    do while(count <= &k);
        if Mod(number,&n)=0 then do;
            output;
            count=count+1;
        end;
        number=number+1;
    end;

#Exporting all this:

    proc export data=tmp_file
        outfile="&file_name"
        dbms=csv
        replace;
    run;

#Finally putting it all in a macro:

    %macro mymac(k,n,file_name);
    ...
    %mend;

#Running it:

    %mymac(300,3,~/Desktop/test.csv);
