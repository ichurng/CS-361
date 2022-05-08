import time
if __name__ == "__main__":
    
    while True:
        time.sleep(1)
  
        f = open("image-services.txt", "r+")
        number = f.read()

        try:
            number = (int(number) % 4) + 1
            file_name = str(number) + ".jpeg"
            f.seek(0)
            f.truncate()
            f.write(file_name)
        except:
            pass
        
        f.close()
