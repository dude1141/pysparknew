class info:
    def info():
        print(" am parameterless info class")

    def info(a):
        print(" am one parameterless info class")


    def info(a,b):
        print(" am two parameterless info class")
    
obj= info()
obj.info(1)

#eventhough you mentioned obj.info(1) it calls info(a,b)
#it does not have concept calledmethod overloading
