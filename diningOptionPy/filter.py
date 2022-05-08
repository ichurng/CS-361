
import time

if __name__ == "__main__":
    
    while True:
        time.sleep(1)
        f = open("filter-services.txt", "r+")
    
        line = f.read()

        line = list(line.split(","))
        

        if line[-1] == "run":
            line = line[:-1]

            for i, pairs in enumerate(line):
                line[i] = list(pairs.split(";"))
            print(line)
            filt_type = line[-1][1]
            line = line[:-1]

            result = []
            for i, res in enumerate(line):
                if res[1] == filt_type:
                    result.append(res[0])
            
            if len(result) == 0:
                result = "No such restaurant type found!"

            f.seek(0)
            f.truncate()
            f.write(str(result))
            

        f.close()