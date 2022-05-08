
from PIL import Image
import time

if __name__ == "__main__":


    #prng service
    print("Enter 'run' to generate image, enter 'exit' to exit")

    command = input("Enter Command: ")
    if command == "run":
        f = open("prng-services.txt", "r+")
        f.write("run")
        f.close()

        time.sleep(5)

        f = open("prng-services.txt", "r")
        number = f.read()
        f.close()

        s = open("image-services.txt", "r+")
        s.seek(0)
        s.truncate()
        s.write(str(number))
        s.close()

        time.sleep(5)

        s = open("image-services.txt", "r")
        file_name = s.read()

        print(file_name)

        img = Image.open(file_name)
        img.show()
    
        s.close()
        img.close()

    elif command == "exit":
        exit()

    