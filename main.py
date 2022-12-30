from mechanize import Browser
import threading


def print_all(lines):
    for s in lines:
        br = Browser()
        br.open(s)
        title = br.title()
        print(title.split("- song")[0][:-1] + "\t" + "\t".join((title.split("- song")[1][15:-10]).split(", ")))


with open('box_scores.txt') as f:
    lines = [s.strip("\n") for s in f.readlines()]

if __name__ == "__main__":
    threads = []
    num = int(input("number of threads:"))
    for i in range(num):
        threads.append(threading.Thread(target=print_all, args=(lines[(i)*len(lines)//num:(i + 1)*len(lines)//num],)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Done!")
