from flask import Flask, Response, request, jsonify
app = Flask(__name__)

information = {'name':'Someguy Somewhere','age':'32', 'occupation':'Somejob'}

@app.route('/')
@app.route('/info', methods=['GET'])
def get_text():
    return jsonify(information)

@app.route('/info/add/<string:key>', methods=['POST'])
def post_text(key):
    if key not in information:
        information[key] = request.data.decode('utf-8')
        return Response(key + " added to information with value: " + request.data.decode('utf-8'), mimetype='text/plain')
    else:
        return Response(key + " already exists.", mimetype='text/plain')

@app.route('/info/update/<string:key>', methods=['PUT'])
def put_text(key):
    if key in information:
        information[key] = request.data.decode('utf-8')
        return Response(key + " changed to: " + request.data.decode('utf-8'), mimetype='text/plain')
    else:
        return Response(key + " not found.", mimetype='text/plain')

@app.route('/info/delete/<string:key>', methods=['DELETE'])
def delete_text(key):
    if key in information:
        information.pop(key)
        return Response(key + " deleted from information. ", mimetype='text/plain')
    else:
        return Response(key + " not found.", mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
