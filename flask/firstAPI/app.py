from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
        { 'name': 'My Wonderful Store',
            'items': [
                {
                    'name': 'My favourite item',
                    'price': 9.99}
                ]
            }
        ]

# Post /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name': request_data['name'],
            'items': []
            }
    stores.append(new_store)
    return jsonify(new_store)

# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
       if store['name'] == name:
           return jsonify(store)
    return jsonify({'message': 'store not found'}) 


# Get /store
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})



# Post /store/<string:name>/item  data:{name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    item = {
            'name': request_data['name'],
            'price': request_data['price']}
    for store in stores:
        if store['name'] == name:
            store['items'].append(item)
            return jsonify(item)
    return jsonify({'message': 'store not found'}) 


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'}) 

app.run(port=5000)
