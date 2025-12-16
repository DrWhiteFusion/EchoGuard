from flask import Flask, jsonify
from data_manager import get_alerts_df

app = Flask(__name__)

@app.route('/get-alerts', methods=['GET'])
def get_alerts():
    df = get_alerts_df()
    # Convert DataFrame to list of dicts
    alerts = df.to_dict(orient='records')
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)