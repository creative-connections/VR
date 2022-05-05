from flask import Flask
from flask import jsonify
from flask import request

musclepressure = 100
rate = 17
blendduration = 50 #%
timestep = 1 #s
resistance = 5
compliance = 7
peep = 3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Available endpoints /musclepressure /rate /blendduration /timestep /resistance /compliance /peep'

@app.route('/musclepressure', methods=['GET'])
def musclepressureget():
    global musclepressure
    return str(musclepressure)

@app.route('/musclepressure', methods=['POST'])
def musclepressurepost():
    global musclepressure
    musclepressure = request.form['value']
    return str(musclepressure)

@app.route('/rate', methods=['GET'])
def rateget():
    global rate
    return str(rate)

@app.route('/rate', methods=['POST'])
def ratepost():
    global rate
    rate = request.form['value']
    return str(rate)

@app.route('/blendduration', methods=['GET'])
def blenddurationget():
    global blendduration
    return str(blendduration)

@app.route('/blendduration', methods=['POST'])
def blenddurationpost():
    global blendduration
    blendduration = request.form['value']
    return str(blendduration)

#/timestep /resistance /compliance /peep

@app.route('/timestep', methods=['GET'])
def timestepget():
    global timestep
    return str(timestep)

@app.route('/timestep', methods=['POST'])
def timesteppost():
    global timestep
    timestep = request.form['value']
    return str(timestep)

@app.route('/resistance', methods=['GET'])
def resistanceget():
    global resistance
    return str(resistance)

@app.route('/resistance', methods=['POST'])
def resistancepost():
    global resistance
    resistance = request.form['value']
    return str(resistance)

@app.route('/compliance', methods=['GET'])
def complianceget():
    global compliance
    return str(compliance)

@app.route('/compliance', methods=['POST'])
def compliancepost():
    global compliance
    compliance = request.form['value']
    return str(compliance)

@app.route('/peep', methods=['GET'])
def peepget():
    global peep
    return str(peep)

@app.route('/peep', methods=['POST'])
def peeppost():
    global peep
    peep = request.form['value']
    return str(peep)


