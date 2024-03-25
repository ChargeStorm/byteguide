from byteguide import app
from byteguide.config import config

def main():
    app.run(host=config.host, port=config.port, debug=config.debug)

if __name__ == "__main__":
    main()