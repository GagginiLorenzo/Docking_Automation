# TOURNE SOUS PYTHON 2.7
import os
import subprocess

# NOTE: This script is a template and may need to be modified to match your system and requirements.
# NOTE : I had to modify some of the MGTools scripts to make them work as i wanted.
# namely mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py

# PLEASE CHANGE THESE PATHS TO MATCH YOUR SYSTEM
prepare_receptor_script = "/home/mellow/Travaille/docking_automation/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py"
prepare_ligand_script = "/home/mellow/Travaille/docking_automation/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py"

# Paths
input_dir = "./pdb_files"
output_dir = "./pdbqt_files"

# Check script existence
if not os.path.isfile(prepare_receptor_script):
    print("prepare_receptor4.py not found. Please check the path.")
    print("Possibly a Python path issue, try to set PYTHONPATH /home/user/.../mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/")
    exit(1)

# Iterate over PDB files and convert to PDBQT (assuming receptor and ligand have specific naming conventions _receptor and _ligand)
for pdb_file in os.listdir(input_dir):
    if pdb_file.endswith("_receptor.pdb"):
        pdb_path = os.path.join(input_dir, pdb_file)
        output_path = os.path.join(output_dir, pdb_file.replace(".pdb", ".pdbqt"))
        print("Processing",pdb_path," to ", output_path)
        # Run the script using subprocess
        subprocess.call([
            "python2", prepare_receptor_script,
            "-r", pdb_path,
            "-o", output_path
        ])
    elif pdb_file.endswith("_ligand.pdb"):
        pdb_path = os.path.join(input_dir, pdb_file)
        output_path = os.path.join(output_dir, pdb_file.replace(".pdb", ".pdbqt"))
        print("Processing",pdb_path," to ", output_path)
        # Run the script using subprocess
        subprocess.call([
            "python2", prepare_ligand_script,
            "-l", pdb_path,
            "-o", output_path
        ])
print("Conversion complete. PDBQT files are in", output_dir)
