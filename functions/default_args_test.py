#default arguments
#A default argument must follow positional parameter
#positional parameter first and then default argument

def runDB(env='dev'):  #formal parameters/dummy parameters
    #database connectivity
    print("The database connected to {}".format(env))

#Test connectivity(dev/qa/uat/prod
runDB()
runDB('qa')  #actual parameters
runDB('uat')
runDB('prod')
