########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Tuesday 07 February 2006 17:08:06 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /mnt/raid/services/cvs/WebServices/Examples/pdb2pqr_net.py,v 1.2 2006/02/08 17:36:44 sargis Exp $
#
# $Id: pdb2pqr_net.py,v 1.2 2006/02/08 17:36:44 sargis Exp $
#

from traceback import print_exc

## loading libraries ##
from Pmv.VisionInterface.PmvNodes import pmvlib
masterNet.getEditor().addLibraryInstance(pmvlib,"Pmv.VisionInterface.PmvNodes", "pmvlib")

from WebServices.VisionInterface.WSNodes import wslib
masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:

    ## saving node Save Lines ##
    from Vision.StandardNodes import SaveLines
    Save_Lines_10 = SaveLines(constrkw = {}, name='Save Lines', library=stdlib)
    masterNet.addNode(Save_Lines_10,49,201)
    Save_Lines_10.inputPortByName['filename'].widget.set("HIS.pqr", run=False)
except:
    print "WARNING: failed to restore SaveLines named Save Lines in network masterNet"
    print_exc()
    Save_Lines_10=None
try:

    ## saving node Pmv ##
    from Pmv.VisionInterface.PmvNodes import PmvNode
    Pmv_11 = PmvNode(vf=masterNet.editor.vf, constrkw = {'vf': 'masterNet.editor.vf'}, name='Pmv', library=pmvlib)
    masterNet.addNode(Pmv_11,224,25)
except:
    print "WARNING: failed to restore PmvNode named Pmv in network masterNet"
    print_exc()
    Pmv_11=None
try:

    ## saving node Choose Cmd ##
    from Pmv.VisionInterface.PmvNodes import PmvChooseCommand
    Choose_Cmd_12 = PmvChooseCommand(constrkw = {}, name='Choose Cmd', library=pmvlib)
    masterNet.addNode(Choose_Cmd_12,224,123)
    apply(Choose_Cmd_12.inputPortByName['cmdName'].widget.configure, (), {'choices': ['readPQR']})
    Choose_Cmd_12.inputPortByName['cmdName'].widget.set("readPQR", run=False)
except:
    print "WARNING: failed to restore PmvChooseCommand named Choose Cmd in network masterNet"
    print_exc()
    Choose_Cmd_12=None
try:

    ## saving node Run readPQR ##
    from Pmv.VisionInterface.PmvNodes import PmvRunCommand
    Run_readPQR_13 = PmvRunCommand(sortedArgNames=['topCommand', 'redraw', 'setupUndo', 'log'], command=masterNet.editor.vf.readPQR, namedArgs={'topCommand': True, 'redraw': True, 'setupUndo': True, 'log': True}, posArgsNames=['filename'], constrkw = {'sortedArgNames': "['topCommand', 'redraw', 'setupUndo', 'log']", 'command': 'masterNet.editor.vf.readPQR', 'namedArgs': "{'topCommand': True, 'redraw': True, 'setupUndo': True, 'log': True}", 'posArgsNames': "['filename']"}, name='Run readPQR', library=pmvlib)
    masterNet.addNode(Run_readPQR_13,224,230)
    apply(Run_readPQR_13.addInputPort, (), {'name': 'filename', 'cast': True, 'datatype': 'string', 'height': 12, 'width': 12, 'shape': 'oval', 'color': 'white'})
    apply(Run_readPQR_13.addInputPort, (), {'name': 'topCommand', 'cast': True, 'datatype': 'boolean', 'balloon': 'Defaults toTrue', 'required': False, 'height': 10, 'width': 10, 'shape': 'rect', 'color': 'yellow'})
    apply(Run_readPQR_13.addInputPort, (), {'name': 'redraw', 'cast': True, 'datatype': 'boolean', 'balloon': 'Defaults toTrue', 'required': False, 'height': 10, 'width': 10, 'shape': 'rect', 'color': 'yellow'})
    apply(Run_readPQR_13.addInputPort, (), {'name': 'setupUndo', 'cast': True, 'datatype': 'boolean', 'balloon': 'Defaults toTrue', 'required': False, 'height': 10, 'width': 10, 'shape': 'rect', 'color': 'yellow'})
    apply(Run_readPQR_13.addInputPort, (), {'name': 'log', 'cast': True, 'datatype': 'boolean', 'balloon': 'Defaults toTrue', 'required': False, 'height': 10, 'width': 10, 'shape': 'rect', 'color': 'yellow'})
    apply(Run_readPQR_13.inputPortByName['topCommand'].createWidget, (), {'descr':{'initialValue': True, 'labelGridCfg': {'column': 0, 'row': 1, 'sticky': 'w'}, 'master': 'ParamPanel', 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 1}, 'labelCfg': {'text': 'topCommand'}, 'class': 'NECheckButton'}})
    apply(Run_readPQR_13.inputPortByName['redraw'].createWidget, (), {'descr':{'initialValue': True, 'labelGridCfg': {'column': 0, 'row': 3, 'sticky': 'w'}, 'master': 'ParamPanel', 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 3}, 'labelCfg': {'text': 'redraw'}, 'class': 'NECheckButton'}})
    apply(Run_readPQR_13.inputPortByName['setupUndo'].createWidget, (), {'descr':{'initialValue': True, 'labelGridCfg': {'column': 0, 'row': 5, 'sticky': 'w'}, 'master': 'ParamPanel', 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 5}, 'labelCfg': {'text': 'setupUndo'}, 'class': 'NECheckButton'}})
    apply(Run_readPQR_13.inputPortByName['log'].createWidget, (), {'descr':{'initialValue': True, 'labelGridCfg': {'column': 0, 'row': 7, 'sticky': 'w'}, 'master': 'ParamPanel', 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 7}, 'labelCfg': {'text': 'log'}, 'class': 'NECheckButton'}})
    code = """



def doit(self, command, filename, topCommand, redraw, setupUndo, log):
    if command is None:
        return
    if command is not self.command and command is not None:
        # remember current command
        self.command = command
        self.rename('Run '+command.name)
        
        # remove all ports beyond the command input port
        for p in self.inputPorts[1:]:
            self.deletePort(p, updateSignature=False)

        # get arguments description
        from inspect import getargspec
        args = getargspec(command.__call__.im_func)
        allNames = args[0][1:] # get rid of self
        defaultValues = args[3]
        if defaultValues is None:
            defaultValues = []
        nbNamesArgs = len(defaultValues)
        if nbNamesArgs > 0:
            self.posArgsNames = args[0][1:-nbNamesArgs]
        else:
            self.posArgsNames = args[0][1:]
        d = {}
        for name, val in zip(args[0][-nbNamesArgs:], defaultValues):
            d[name] = val
        for name, val in zip(self.defaultNamedArgs, self.defaultNamedArgsdefaults):
            d[name] = val

        self.namedArgs = d

        # create input ports for positional arguments
        self.createPortsForPositionalArgs(self.posArgsNames)

        # create widgets and ports for named arguments
        self.sortedArgNames = self.buildPortsForNamedArgs(self.namedArgs)

        # create the constructor arguments such that when the node is restored
        # from file it will have all the info it needs
        self.constrkw['command'] = 'masterNet.editor.vf.%s'%command.name
        self.constrkw['posArgsNames'] = str(self.posArgsNames)
        self.constrkw['namedArgs'] = str(self.namedArgs)
        self.constrkw['sortedArgNames'] = str(self.sortedArgNames)
        
    elif self.command is not None:
        # get all positional arguments
        posargs = []
        for pn in self.posArgsNames:
            posargs.append(locals()[pn])

        # build named arguments
        kw = {}
        for arg in self.sortedArgNames:
            kw[arg] = locals()[arg]

        # call command
        value = apply( self.command.__call__, posargs, kw )

        self.outputData(result=value)
"""
    Run_readPQR_13.configure(function=code)
except:
    print "WARNING: failed to restore PmvRunCommand named Run readPQR in network masterNet"
    print_exc()
    Run_readPQR_13=None
try:

    import WebServices
    path = WebServices.__path__[0]
    import os
    path = path + os.sep + 'Examples' + os.sep + 'HIS.pdb'
    mol = masterNet.editor.vf.loadMoleculeIfNeeded(path)
    from Pmv.VisionInterface.PmvNodes import PmvMolecule
    HIS_14 = PmvMolecule(molecule=masterNet.editor.vf.expandNodes("HIS")[0], constrkw = {'molecule': 'masterNet.editor.vf.expandNodes("HIS")[0]'}, name='HIS', library=pmvlib)
    masterNet.addNode(HIS_14,49,8)
except:
    print "WARNING: failed to restore PmvMolecule named HIS in network masterNet"
    print_exc()
    HIS_14=None
try:

    ## saving node pdb2pqr@ws.nbcr ##
    from WebServices.VisionInterface.WSNodes import pdb2pqrNode
    pdb2pqr_ws_nbcr_16 = pdb2pqrNode(host='http://ws.nbcr.net:8080', constrkw = {'host': "'http://ws.nbcr.net:8080'"}, name='pdb2pqr@ws.nbcr', library=wslib)
    masterNet.addNode(pdb2pqr_ws_nbcr_16,32,87)
    apply(pdb2pqr_ws_nbcr_16.configure, (), {'expanded': False})
except:
    print "WARNING: failed to restore pdb2pqrNode named pdb2pqr@ws.nbcr in network masterNet"
    print_exc()
    pdb2pqr_ws_nbcr_16=None
masterNet.freeze()

## saving connections for network pdb2pqr ##
if Pmv_11 is not None and Choose_Cmd_12 is not None:
    masterNet.connectNodes(
        Pmv_11, Choose_Cmd_12, "PMV", "viewer", blocking=True)
if Choose_Cmd_12 is not None and Run_readPQR_13 is not None:
    masterNet.connectNodes(
        Choose_Cmd_12, Run_readPQR_13, "cmd", "command", blocking=True)
if Save_Lines_10 is not None and Run_readPQR_13 is not None:
    masterNet.connectNodes(
        Save_Lines_10, Run_readPQR_13, "filename", "filename", blocking=True)
if HIS_14 is not None and pdb2pqr_ws_nbcr_16 is not None:
    masterNet.connectNodes(
        HIS_14, pdb2pqr_ws_nbcr_16, "Molecule", "input_mol", blocking=True)
if pdb2pqr_ws_nbcr_16 is not None and Save_Lines_10 is not None:
    masterNet.connectNodes(
        pdb2pqr_ws_nbcr_16, Save_Lines_10, "output_file_url", "data", blocking=True)
masterNet.unfreeze()
