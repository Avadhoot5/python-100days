# MultiProcessing 

import multiprocessing
import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"multiprocess/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"

# this takes time as it gets executed one after another
# for i in range(5):
#     downloadFile(url, i)

# multiprocessing
if __name__ == "__main__":
    pass
    # pros = []
    # for i in range(5):
    #     p = multiprocessing.Process(target = downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

# using Process Pool Executor

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)

if __name__ == '__main__':
    main()
