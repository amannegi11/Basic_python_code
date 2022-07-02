import logging
logging.basicConfig(filename="aman.txt",level=logging.INFO)
def fun():
    try:
        with open('lop.txt','r'):
            logging.info("i can read it")
    except Exception as e :
        logging.info("enable to read your file")
        logging.exception(e)
    finally:
        with open("aman.txt",'r') as R:
            print(R.read())
            R.close()
print(fun())