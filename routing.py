from flask import Flask
from flask import request
from chemistry import smiles_to_mol
app = Flask(__name__)

@app.route("/")
def welcome():
    return """

    <h2>RDKIT as a service</h2>

    <pre>/smiles/&#60;string:smiles_str&#62;
        - Pass a smiles str to get a mol
    representation. Add options for more
    processing and features.
    </pre>

    """

@app.route("/smiles/<string:smiles_str>")
def smiles(smiles_str):
    if request:
        return smiles_to_mol(smiles_str, **request.args)
    else:
        return smiles_to_mol(smiles_str)

if __name__ == "__main__":
    app.run()


