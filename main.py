from datetime import datetime


def main():
    start_time = datetime.now()
    i = 0
    while i < 1_820_028:
        time_running = (datetime.now()-start_time) 
        time_running = str(time_running).split(".")[0]
        i += 1
        print(f"Run time: {time_running} | iterations: {i:,}", end='\r')

    print(f"Total run time: {time_running} | total iterations: {i:,}.")

if __name__ == "__main__":
    main()