from flask import Flask, request, jsonify
from rdkit import Chem
from rdkit.Chem import AllChem

app = Flask(__name__)

@app.route('/generate-3d-structure', methods=['POST'])
def generate_3D_structure_endpoint():
    smiles_string = request.json['smiles']
    
    # Convert SMILES to RDKit molecule object
    mol = Chem.MolFromSmiles(smiles_string)
    
    # Add Hydrogens to the molecule
    mol = Chem.AddHs(mol)
    
    # Generate 3D coordinates using the ETKDG method
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    
    # Save to PDB file
    Chem.MolToPDBFile(mol, "molecule.pdb")
    print("Saved new molecule")
    
    return jsonify({"message": "Molecule saved to molecule.pdb"})

if __name__ == '__main__':
    app.run(debug=True)
