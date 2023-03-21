import os

def main():
    dir = 'test_content'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f)) 

    dir = 'test_result'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

if __name__ == '__main__':
    main()
