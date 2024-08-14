# Rule Engine with AST

## Overview
This project implements a 3-tier rule engine application designed to determine user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent and manage conditional rules dynamically. The application is structured with a simple user interface, a REST API, and a backend service. MongoDB is included for demonstration purposes but is not used in the application logic.

## Features
- Create and manage rules using AST.
- Combine multiple rules into a single AST.
- Evaluate rules against user data.
- MongoDB integration for demonstration purposes (not used in backend).

## Design Choices

### Abstract Syntax Tree (AST)
- **Node Structure**: The AST is represented using nodes with:
  - `type`: Indicates the node type (`operator` for AND/OR, `operand` for conditions).
  - `left`: Reference to the left child node (for operators).
  - `right`: Reference to the right child node (for operators).
  - `value`: Optional value for operand nodes (e.g., numeric values for comparisons).

### Rule Evaluation
- **Combining Rules**: Rules are combined into a single AST using efficient strategies to avoid redundant checks.
- **Evaluation**: The AST is evaluated against user data to determine eligibility.

### Data Storage
- **Temporary Storage**: The application uses in-memory storage for rules and evaluation data.
- **MongoDB**: MongoDB is integrated for demonstration purposes, but it is not used in the application's logic.

## Setup Instructions

### Prerequisites
- Python 3.10+
- `pip` (Python package installer)
- Docker (optional, for containerized setup)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shadowrunner21/rule_engine_py.git
   cd rule_engine_py

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the Application**
   ```bash
   python app.py

### Open your web browser and navigate to http://127.0.0.1:5000


## Security
Input Validation: The application includes validation mechanisms to ensure that inputs are sanitized and validated before processing. This prevents injection attacks and ensures data integrity.

## Performance
Efficient Rule Evaluation: The rule evaluation logic is optimized for performance, using efficient algorithms to handle large sets of rules and user attributes.
Asynchronous Operations: The application uses asynchronous operations to ensure responsiveness and avoid blocking operations, particularly during rule evaluations and data processing.

## Bonus Features (Planned Enhancements)

Advanced Rule Management: Future improvements may include advanced rule management features such as dynamic rule updates and version control.
