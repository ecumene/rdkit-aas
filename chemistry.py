from rdkit import Chem
from rdkit.Chem import AllChem

def mol_to_str(mol):
    return Chem.MolToMolBlock(mol)

def mol_with_hydrogen(mol):
    return Chem.AddHs(mol)

def mol_to_3d(m):
    AllChem.EmbedMolecule(m)

def smiles_to_mol(smiles, hydrogens=False, with_z=False):
    m = Chem.MolFromSmiles(smiles)
    if hydrogens:
        m = mol_with_hydrogen(m)
    if with_z:
        mol_to_3d(m)
    return mol_to_str(m)

