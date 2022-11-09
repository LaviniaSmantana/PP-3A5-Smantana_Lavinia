import utils


def app():
    inputs = input()
    while inputs != "q":
        x = int(inputs)
        print(utils.process_item(x))
        inputs = input()

if __name__ == '__main__':
    app()