import time
import random

if __name__ == "__main__":
    
    while True:
        time.sleep(1)
        f = open("randomize-services.txt", "r+")
    
        line = f.read()

        line = list(line.split(","))
        
        if line[-1] == "run":
            result = []
            line = line[:-1]
            n = random.randint(0,len(line)-1)

            f.seek(0)
            f.truncate()
            f.write(str(line[n]))
            

        f.close()