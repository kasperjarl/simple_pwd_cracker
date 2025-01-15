from datetime import datetime

class RunTime():
    def __init__(self, start_time=datetime.now(), iterations=0):
        self.start_time = start_time
        self.iterations = iterations
    
    def run_timer(self):
        while self.iterations < 82_002:
            time_running = (datetime.now()-self.start_time) 
            time_running = str(time_running).split(".")[0]
            self.iterations += 1
            print(f"[Press 'ctrl+c' to quit] Run time: {time_running} | iterations: {self.iterations:,}", end='\r')
        
        
        print("\n")
        print(f"Total run time: {time_running} | total iterations: {self.iterations:,}.")

