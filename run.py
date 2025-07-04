from app import create_app
import os

app = create_app()


if __name__ == '__main__':
    debug = os.getenv('FLASK_ENV') == 'development' or os.getenv('FLASK_DEBUG') == '1'
    app.run(host='0.0.0.0', port=5000, debug=debug)
