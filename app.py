from Flask import *
from src.Crupier import Crupier
import json
app=Flask(__name__)


@app.route("/", method=['GET'])
def status():
	return jsonify(status='OK')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
