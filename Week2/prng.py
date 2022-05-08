import random
import time

if __name__ == "__main__":
    
    while True:
        time.sleep(1)
        f = open("prng-services.txt", "r+")
        
        content = f.read()

        if content == "run":
            n = random.randint(0,20)
            f.seek(0)
            f.truncate()
            f.write(str(n))

        f.close()