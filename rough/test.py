import os

def run():
    print(">>>>>ALWAYS RUN<<<<<<")
    with open(os.path.join("rough","test.txt"),"w") as f:
        f.write(f"This is a test file and for testing purpose")

if __name__=="__main__":
    run()