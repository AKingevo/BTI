### ***Note If you don't know how to convert Decimal ip TO binary or binary to Decimal then you may not 
### ***get the concept behind the code so i recommed you to first check these video Out i founded it 
### ***useful "https://youtu.be/2-i5x8KCfII" 


print('\033[1;32;40m \n Hi there :] \n');
# the make the tool start again after used once so u can say whole tools is inside a function 
# u may think then how the script will start without calling the start fnx .. that start() is
# at the end of the script to start it
def start():
    #Tools to convert binary IP in deciamal IP and Decimal IP into binary ip
    ip = input("\033[1;32;40m \nType the decimal or Binary IP to convert it : ");
    
     #ip = p.q.r.s
    #y can be called the subshells and 0,1,2,3 are the shell's in dip2  [Not Imoptant]
    #p,q,r,s values have differet use in Binary to decimal condition and decimal to binary
    p = 0;
    q = 0;
    r = 0;
    s = 0;
######################################################################################################
###################################Binary to Decimal##################################################
######################################################################################################
    # these will check that the ip which i entered is binary or decimal so that we can convert it to 
    # the another one.. so if it is binary then it will be something like :
    # aaaaaaaa.aaaaaaaa.aaaaaaaa.aaaaaaaa   where a  ∈ {0,1}
    # so when we take length of "aaaaaaaa.aaaaaaaa.aaaaaaaa.aaaaaaaa" then it will be = 35 including 
    # '.' and if we exclude them then the length will be 32.
    if(int(len(ip)) == 35):
        # to replace the '.' from the binary ip into space
        dip = ip.replace('.',' ');
        # to convert the @dip in a list  
        dip2 = list(dip.split(" "));
        # y is here for having all values of the one octate of the ip 
        for y in range(8):
            #i know  the commet's are big and confusing but i don't know what to write :\ sorry
            # here these will try putting different values of @y from [0,8) 8 not included . and w
            # wherever it will satisfy the condition the the command will be exicuted
            #eg (dip2[0])[0] will mean the 1'st digit of the octate and check if it is 1[on] or 0[off]
            if(int((dip2[0])[y])==1):
                #now as we are inside the condition so it means it was 1  and at the postition @y so as
                # we know ...wait a min have u read the note in the starting ?..ok ..if position of y is 
                #0 the we will have 2^7 =128 
                #y = 0 --> 128 if on means 1 or if off then for any value of y -->0 
                #y = 1 --> 64  if on means 1 or if off then for any value of y -->0 
                #y = 2 --> 32  if on means 1 or if off then for any value of y -->0
                #y = 3 --> 16  if on means 1 or if off then for any value of y -->0
                #y = 4 --> 8   if on means 1 or if off then for any value of y -->0
                #y = 5 --> 4   if on means 1 or if off then for any value of y -->0
                #y = 6 --> 2   if on means 1 or if off then for any value of y -->0
                #y = 7 --> 1   if on means 1 or if off then for any value of y -->0
                # so we formed the below eqution by help of these
                p=p+2**(7-y);
            # now checking same in 2nd octate
            if(int((dip2[1])[y])==1):

                q=q+2**(7-y);
            # now checking same in 3nd octate
            if(int((dip2[2])[y])==1):

                r=r+2**(7-y);
            # now checking same in 4nd octate 
            if(int((dip2[3])[y])==1):

                s=s+2**(7-y);
        # sip is the remove the gap such as 1 . 1 . 1 . 1 --> 1.1.1.1
        print("IP for ip ",ip,' = ',"\033[1;33;41m ",p,'.',q,'.',r,'.',s,sep='');
        #script start again
        start()
# conclusion in these we used p,q,r,s for storing the values of the decimal ip

######################################################################################################
###################################Decimal to binary##################################################
######################################################################################################

    #OK now i know u are board you can have rest or try making your own as you know the concept 
    # as we know the deciaml ip will be somthing like a.b.c.d and here a,b,c,d can be anything between 
    # (0-255) so min lenght will be 0.0.0.0 -->7 and max will be 255.255.255.255 --> 15
    # so we taked that if condition to know that it is a decimal ip

    if(6<int(len(ip))<16):
        # again the same which we did upward line no . 30
        dip = ip.replace('.',' ');
       # again the same which we did upward line no . 32
        dip2 = list(dip.split(" "));
        
    
        # here is something which took time to think what to do 
        # it is removing the extra 0b from the dip2[0] binary form 0 is here the octate number
        # we converted ocate one into binary then removed the extra 0b from it and finded the lenght
        # i know u may be thing why that actually when i runned the script without it the leading zero 
        # were not coming mean non-significat so i though to add them by myself by calculating there 
        # number  so as when it was coming 8 then there was no leading zero but when it was less then zero 
        # the zero was required so where ever it will be less then one then the cutted zero wll be 
        #  calculated and stored into the p,q,r,s so here i used them to know the zeros
        if(len((bin(int(dip2[0])).replace('0b','')))<8):
            p = 8-len((bin(int(dip2[0])).replace('0b','')));
        if(len((bin(int(dip2[1])).replace('0b','')))<8):
            q = 8-len((bin(int(dip2[1])).replace('0b','')));
        if(len((bin(int(dip2[2])).replace('0b','')))<8):
            r = 8-len((bin(int(dip2[2])).replace('0b','')));
        if(len((bin(int(dip2[3])).replace('0b','')))<8):
            s = 8-len((bin(int(dip2[3])).replace('0b','')));
         # here i just printed the output by adding the zeros 
         # if u didn't understood the sorry :)
        print("\nThe Binary IP for ",ip,' is : ',"\033[1;33;41m",'0'*p,(bin(int(dip2[0]))).replace('0b',''),'.','0'*q,(bin(int(dip2[1]))).replace('0b',''),'.','0'*r,(bin(int(dip2[2]))).replace('0b',''),'.','0'*s,(bin(int(dip2[3]))).replace('0b',''),sep='');    
             
         
        # restart
        start()
    # when above case don't work
    print("Wrong IP ! Range ");
    #restart
    start()
    
    
#start
start()   #65514
                       ####      #   #    EEEE          ####      #   #    EEEE                          
                       #   #      # #     E             #   #      # #     E     
                       # # #       #      EEEE  -----   # # #       #      EEEE
                       #   #       #      E             #   #       #      E
                       # #         #      EEEE          # #         #      EEEE
                                          #:]#

# while typing these these #'s i just felt like including every # from twitter 'bad joke'
######################################################################################################
######################################NOOB#Script#####################################################
######################################################################################################
########BY:-##########################################################################################
############Akingevo(r_b_r_)##########################################################################  