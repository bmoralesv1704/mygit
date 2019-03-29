the_count ={1,2,3,4,5}
fruits = {'apples', 'oranges', 'pears', 'apricots'}
change = {1,'pennies', 2 , 'dimes', 3, 'quarters'}

#this firts kind of for-loop goes through a listjk


        for number in the_count:
            print ("This is count %d" % number)
            
        for fruit int fruits:
            print ("This is coynt %d" % fruit)
        #same as above
        
        #also we cab go through mixed lists too
        #notice we have to user %r since we don't know what's in it
        for i in change:
            print ("A fruit of type: %s" % i)
            
        #we can also build lists, first start with an amprty one
        elements = []
        #then use the range function to do 0 to 5 counts
        for i in range(0,6):
            print ("Adding %d to the list." %i)
            #append is a function that lists understand
            elemnts.append(i)
            
            #now we can print the, out too
            for i in elements:
                print ("Element was: %d" % i)
        
        
