import os
import subprocess

# NOTE: This script is a template and may need to be modified to match your system and requirements.
# NOTE : I had to modify some of the MGTools scripts to make them work as i wanted.
# namely mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/GridParameters.py

# PLEASE CHANGE THESE PATHS TO MATCH YOUR SYSTEM

pdbqt_folder = "/home/mellow/Travaille/docking_automation/pdbqt_files"  # Folder containing receptor and ligand PDBQT files
autogrid_folder = "/home/mellow/Travaille/docking_automation/autogrid_results"  # Output folder for autogrid_results
vina_folder = "/home/mellow/Travaille/docking_automation/vina_results"  # Output folder for docking results
autodock_folder = "/home/mellow/Travaille/docking_automation/autodock_results"  # Output folder for autodock results
maps_folder = "/home/mellow/Travaille/docking_automation/maps"  # Output folder for maps files
prepare_gpf_script = "/home/mellow/Travaille/docking_automation/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py"
prepare_dpf_script = "/home/mellow/Travaille/docking_automation/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py"

# Relatives paths (in the current Working directory, ie where this script is run)
# Don't need to change these technically, but you can if you want

template_gpf = "./template.gpf"  # Template grid parameter file
template_dpf = "./template.dpf"  # Template docking parameter file
conf_file = "./configuration_vina.txt"  # Configuration file for Vina
autogrid_executable = "./autogrid4" # Autogrid executable
vina_executable = "./vina_1.2.5_linux_x86_64" # Vina executable
autodock_executable = "./autodock4" # Autodock executable

# Check if the user wants to run AutoDock
run_autodock = False  # Set this to False if you don't want to run AutoDock and only want to run Vina


# Iterate through PDBQT files (assuming receptor and ligand have specific naming conventions _receptor and _ligand)
# and perform docking for each pair
for receptor_file in os.listdir(pdbqt_folder): # For each pdbqt file in the folder

    if receptor_file.endswith("receptor.pdbqt"):
        receptor_path = os.path.join(pdbqt_folder, receptor_file) # Detects a receptor file

        for ligand_file in os.listdir(pdbqt_folder): # For the detected receptor file, iterate through the folder again

            if ligand_file.endswith("ligand.pdbqt"):
                ligand_path = os.path.join(pdbqt_folder, ligand_file) # And detects a the ligand file

                # Define output names
                base_name = f"{receptor_file.replace('.pdbqt', '')}_{ligand_file.replace('.pdbqt', '')}"
                gpf_file = os.path.join(autogrid_folder, f"{base_name}.gpf")
                dpf_file = os.path.join(autodock_folder, f"{base_name}.dpf")
                glg_file = os.path.join(autogrid_folder, f"{base_name}.glg")
                dlg_file = os.path.join(autodock_folder, f"{base_name}.dlg")

                print(f"Docking: {receptor_file} with {ligand_file}")

                if run_autodock:
                    # Generate a dummy GPF (grid parameter file) from the template for autogrid
                    with open(template_gpf, "r") as template:
                        gpf_content = template.read()
                    with open(gpf_file, "w") as gpf:
                        gpf.write(gpf_content)

                    # Generate a dummy DPF (docking parameter file) from the template for autodock
                    with open(template_dpf, "r") as template:
                        dpf_content = template.read()
                    with open(dpf_file, "w") as dpf:
                        dpf.write(dpf_content)

                    # Tips: use the templates to set the parameters for the docking, then check the generated files,
                    # AutoDockTools "prepare_scripts" might be outdated compared to the current version of AutoDock4.
                    # You can also use the AutoDockTools GUI to generate the files and then use them as templates.
                    # Or do as i did and edit post-process the generated files to match my needs.

                    # Just make a template file with the parameters you want (see Autodock4 documentation for syntax)
                    # and check the generated files to see if they match.
                    # If they don't match, post-process the generated files to match your needs.
                    # This allows you to set specific parameters for each docking pair using different templates if needed.

                    # prepare_gpf from template parameters
                    subprocess.run(["python2", prepare_gpf_script, "-l", ligand_path, "-r", receptor_path,"-i", gpf_file, "-o", gpf_file])

                    # prepare_dpf from template parameters
                    subprocess.run(["python2", prepare_dpf_script, "-l", ligand_path, "-r", receptor_path,"-i", dpf_file, "-o", dpf_file])

                    type Cmd = list[str]

                    # post-process gpf file to replace receptor file path due to a weird behavior of AutoDockTools/Utilities24/prepare_gpf4.py
                    # that set the receptor_file_name as the receptor_path
                    with open(gpf_file, "r") as template:
                        gpf_content = template.read()
                    gpf_content = gpf_content.replace(receptor_file, receptor_path) # Replace the receptor_file_name with the receptor_path
                    with open(gpf_file, "w") as gpf:
                        gpf.write(gpf_content)

                    # post-process dpf file to replace ligand file path due to a weird behavior of AutoDockTools/Utilities24/prepare_dpf4.py
                    # that set the ligand_file_name as the ligand_path
                    with open(dpf_file, "r") as template:
                        dpf_content = template.read()
                    dpf_content = dpf_content.replace(ligand_file, ligand_path) # Replace the ligand_file_name with the ligand_path
                    with open(dpf_file, "w") as dpf:
                        dpf.write(dpf_content)

                    # Run AutoGrid
                    subprocess.run([autogrid_executable, "-p", gpf_file, "-l", glg_file])

                    # Run AutoDock
                    subprocess.run([autodock_executable, "-p", dpf_file, "-l", dlg_file])

                # Run Vina
                subprocess.run([vina_executable, "--receptor", receptor_path, "--ligand", ligand_path, "--config", conf_file, "--out", os.path.join(vina_folder,base_name +"_out.pdbqt")])

                # Clean up fld and xyz files after docking. You can also move them to a specific folder if needed.
                # maps files are generated by AutoDock and can be used to visualize the docking results in some software,
                # but they are not needed per se after the docking is done.
                # be awar that autodock4 used those files to generate the dlg file, you might want to
                # post-process the dlg file to update the paths to the fld and xyz files if you move them.
                # (very much like i did for the gpf and dpf files regarding the receptor and ligand paths)
                #
                for file in os.listdir("/home/mellow/Travaille/docking_automation/"):
                    if file.endswith(".map") or file.endswith(".fld") or file.endswith(".xyz"):
                        file_path = os.path.join("/home/mellow/Travaille/docking_automation/", file)

                        # The following line delete the files
                        #
                        os.remove(file_path)
                        print(f"Fichier supprimé : {file_path}")

                        # If needed, the following lines move the files to a specific folder
                        #
                        #file_path = os.path.join("/home/mellow/Travaille/docking_automation/", file)
                        #mkdir = os.path.join(maps_folder, base_name)
                        #if not os.path.exists(mkdir):
                        #    os.makedirs(mkdir)
                        #new_file_path = os.path.join(mkdir, file)
                        #os.rename(file_path, new_file_path)
                        #print(f"Fichier déplacé : {new_file_path}")

print("Docking completed for all receptor-ligand pairs.")
