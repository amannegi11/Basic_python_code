import logging
logging.basicConfig(filename="exception.txt",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
# write a function
def function(a,b):
    try:
        div=a/b
        logging.info("the function is working fine no such error")
    except Exception as e:
        logging.info("there is an issue occur with your code ")
        logging.error(e)

print(function(11,0))