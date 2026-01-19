from flask import Flask, jsonify, request

# 初始化应用
app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"status": "API服务已启动", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)