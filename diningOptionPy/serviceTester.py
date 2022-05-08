import time

def talk_to_file(send):
    f = open("randomize-services.txt", "r+")

    f.seek(0)
    f.truncate()

    f.write(send)
    f.close()

    f = open("randomize-services.txt", "r+")
    print("randomizing...")
    time.sleep(3)
    f.seek(0)
    res = f.read()
    print(res)
    f.close()


if __name__ == "__main__":
    talk_to_file("Subway,Red Lobster,Cheddars,run")