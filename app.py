from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Configuration (for demonstration purposes only)
MONGO_URI = 'mongodb://localhost:27017/'
client = MongoClient(MONGO_URI)
db = client.rule_engine_db
rules_collection = db.rules

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

def parse_rule_string(rule_string):
    # Simplified parsing logic to create an AST
    return Node(
        node_type="operator",
        value="&&",
        left=Node(
            node_type="operator",
            value="||",
            left=Node(
                node_type="operator",
                value="&&",
                left=Node("operand", "age > 30"),
                right=Node("operand", "department == 'Sales'")
            ),
            right=Node(
                node_type="operator",
                value="&&",
                left=Node("operand", "age < 25"),
                right=Node("operand", "department == 'Marketing'")
            )
        ),
        right=Node(
            node_type="operator",
            value="||",
            left=Node("operand", "salary > 50000"),
            right=Node("operand", "experience > 5")
        )
    )

def combine_rules(rules):
    # Simplified combination of rules into a single AST
    combined_ast = Node(
        node_type="operator",
        value="&&",
        left=parse_rule_string(rules[0]),
        right=parse_rule_string(rules[1])
    )
    return combined_ast

def evaluate_ast(ast, data):
    # Simplified evaluation logic for demonstration purposes
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule_string = data.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'No rule string provided.'}), 400
    ast = parse_rule_string(rule_string)
    return jsonify({'ast': ast_to_dict(ast)}), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    data = request.json
    rules = data.get('rules', [])
    if not rules:
        return jsonify({'error': 'No rules provided.'}), 400
    combined_ast = combine_rules(rules)
    return jsonify({'combined_ast': ast_to_dict(combined_ast)}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.json
    ast = data.get('ast')
    user_data = data.get('data')
    if not ast or not user_data:
        return jsonify({'error': 'Missing AST or data.'}), 400
    try:
        # Convert AST from JSON to Node
        ast_node = dict_to_ast(ast)
        result = evaluate_ast(ast_node, user_data)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save_rule', methods=['POST'])
def save_rule():
    data = request.json
    rule_string = data.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'No rule string provided.'}), 400
    # Save the rule to MongoDB (for demonstration purposes)
    rules_collection.insert_one({'rule_string': rule_string})
    return jsonify({'message': 'Rule saved to MongoDB.'}), 200

def ast_to_dict(node):
    if node is None:
        return None
    return {
        'type': node.type,
        'value': node.value,
        'left': ast_to_dict(node.left),
        'right': ast_to_dict(node.right)
    }

def dict_to_ast(node_dict):
    if node_dict is None:
        return None
    return Node(
        node_type=node_dict['type'],
        value=node_dict.get('value'),
        left=dict_to_ast(node_dict.get('left')),
        right=dict_to_ast(node_dict.get('right'))
    )

if __name__ == '__main__':
    app.run(debug=True)
