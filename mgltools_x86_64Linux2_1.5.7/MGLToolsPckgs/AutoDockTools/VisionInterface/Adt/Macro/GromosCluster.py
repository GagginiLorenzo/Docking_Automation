########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Tuesday 27 July 2010 18:39:11 
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
# $Header: /mnt/raid/services/cvs/python/packages/share1.5/AutoDockTools/VisionInterface/Adt/Macro/GromosCluster.py,v 1.3 2010/07/28 01:48:07 jren Exp $
#
# $Id: GromosCluster.py,v 1.3 2010/07/28 01:48:07 jren Exp $
#

from NetworkEditor.macros import MacroNode
from NetworkEditor.macros import MacroNode
class GromosCluster(MacroNode):
    '''
    This node runs the GROMOS Cluster web service.

    Inputs: 
        port 1: trajectory pdb file
        port 2: active residue pdb file
        port 3: rmsd cutoff
        port 4: directory to download pdb results to
    Output:
        directory path that contains the result pdb files
    '''

    def __init__(self, constrkw={}, name='GromosCluster', **kw):
        kw['name'] = name
        apply( MacroNode.__init__, (self,), kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        from Vision.StandardNodes import stdlib
        from WebServices.VisionInterface.WSNodes import wslib
        net.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass

    def afterAddingToNetwork(self):
        masterNet = self.macroNetwork
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        from Vision.StandardNodes import stdlib
        from WebServices.VisionInterface.WSNodes import wslib
        ## building macro network ##
        GromosCluster_33 = self
        from traceback import print_exc
        from Vision.StandardNodes import stdlib
        from WebServices.VisionInterface.WSNodes import wslib
        masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            ## saving node input Ports ##
            input_Ports_34 = self.macroNetwork.ipNode
            apply(input_Ports_34.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork"
            print_exc()
            input_Ports_34=None

        try:
            ## saving node output Ports ##
            output_Ports_35 = self.macroNetwork.opNode
            apply(output_Ports_35.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            output_Ports_35.move(236, 302)
        except:
            print "WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork"
            print_exc()
            output_Ports_35=None

        try:
            ## saving node GROMOS_ClusterFiles_kryptonite_nbcr_net ##
            from NetworkEditor.items import FunctionNode
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36 = FunctionNode(functionOrString='GROMOS_ClusterFiles_kryptonite_nbcr_net', host="http://kryptonite.nbcr.net/opal2", namedArgs={'expert_options': '', 'rmsd': '0.125', 'traj': '', 'prefix': '', 'default_options': '-o -g -dist -ev -sz -tr -ntr -clid -cl', 'active': '', 'localRun': False, 'method': 'gromos', 'execPath': ''}, constrkw={'functionOrString': "'GROMOS_ClusterFiles_kryptonite_nbcr_net'", 'host': '"http://kryptonite.nbcr.net/opal2"', 'namedArgs': {'expert_options': '', 'rmsd': '0.125', 'traj': '', 'prefix': '', 'default_options': '-o -g -dist -ev -sz -tr -ntr -clid -cl', 'active': '', 'localRun': False, 'method': 'gromos', 'execPath': ''}}, name='GROMOS_ClusterFiles_kryptonite_nbcr_net', library=wslib)
            self.macroNetwork.addNode(GROMOS_ClusterFiles_kryptonite_nbcr_net_36,200,98)
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['expert_options'].configure, (), {'defaultValue': None})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['rmsd'].configure, (), {'defaultValue': None, 'required': True})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['traj'].configure, (), {'defaultValue': None, 'required': True})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['prefix'].configure, (), {'defaultValue': None})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['default_options'].configure, (), {'defaultValue': None})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['active'].configure, (), {'defaultValue': None, 'required': True})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['localRun'].configure, (), {'defaultValue': None})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['method'].configure, (), {'defaultValue': None})
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['execPath'].configure, (), {'defaultValue': None})
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['expert_options'].widget.set(r"", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['rmsd'].rebindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['rmsd'].widget.set(r"0.125", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['rmsd'].unbindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['traj'].rebindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['traj'].widget.set(r"", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['traj'].unbindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['prefix'].widget.set(r"", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['default_options'].widget.set(r"-o -g -dist -ev -sz -tr -ntr -clid -cl", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['active'].rebindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['active'].widget.set(r"", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['active'].unbindWidget()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['localRun'].widget.set(0, run=False)
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['method'].widget.configure, (), {'choices': ('gromos', 'linkage', 'jarvis-patrick', 'monte-carlo', 'diagonalization')})
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['method'].widget.set(r"gromos", run=False)
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36.inputPortByName['execPath'].widget.set(r"", run=False)
            apply(GROMOS_ClusterFiles_kryptonite_nbcr_net_36.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore FunctionNode named GROMOS_ClusterFiles_kryptonite_nbcr_net in network self.macroNetwork"
            print_exc()
            GROMOS_ClusterFiles_kryptonite_nbcr_net_36=None

        try:
            ## saving node GetClusterFrameLink ##
            from WebServices.VisionInterface.WSNodes import GetMainURLFromListNode
            GetClusterFrameLink_46 = GetMainURLFromListNode(constrkw={}, name='GetClusterFrameLink', library=wslib)
            self.macroNetwork.addNode(GetClusterFrameLink_46,200,164)
            apply(GetClusterFrameLink_46.inputPortByName['urls'].configure, (), {'defaultValue': None})
            code = """def doit(self, urls):   
            url = urls[0]
            filename = url.split('''/''')[len(url.split('''/'''))-1]
            nurl = url.strip(filename)
            nurl = nurl + '''cluster_frames'''
            pass
            self.outputData(newurl=nurl)

"""
            GetClusterFrameLink_46.configure(function=code)
            apply(GetClusterFrameLink_46.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore GetMainURLFromListNode named GetClusterFrameLink in network self.macroNetwork"
            print_exc()
            GetClusterFrameLink_46=None

        try:
            ## saving node DownloadSaveDir ##
            from WebServices.VisionInterface.WSNodes import DownloadSaveDirNode
            DownloadSaveDir_51 = DownloadSaveDirNode(constrkw={}, name='DownloadSaveDir', library=wslib)
            self.macroNetwork.addNode(DownloadSaveDir_51,253,241)
            apply(DownloadSaveDir_51.inputPortByName['url'].configure, (), {'defaultValue': None})
            apply(DownloadSaveDir_51.inputPortByName['path'].configure, (), {'defaultValue': None})
            apply(DownloadSaveDir_51.inputPortByName['cutdirs'].configure, (), {'defaultValue': None})
            DownloadSaveDir_51.inputPortByName['url'].rebindWidget()
            DownloadSaveDir_51.inputPortByName['url'].widget.set(r"", run=False)
            DownloadSaveDir_51.inputPortByName['url'].unbindWidget()
            apply(DownloadSaveDir_51.configure, (), {'paramPanelImmediate': 1})
        except:
            print "WARNING: failed to restore DownloadSaveDirNode named DownloadSaveDir in network self.macroNetwork"
            print_exc()
            DownloadSaveDir_51=None

        try:
            ## saving node Entry ##
            from Vision.StandardNodes import EntryNE
            Entry_54 = EntryNE(constrkw={}, name='Entry', library=stdlib)
            self.macroNetwork.addNode(Entry_54,347,154)
            apply(Entry_54.inputPortByName['entry'].configure, (), {'defaultValue': None})
            Entry_54.inputPortByName['entry'].widget.set(r"3", run=False)
            apply(Entry_54.configure, (), {'paramPanelImmediate': 1})
        except:
            print "WARNING: failed to restore EntryNE named Entry in network self.macroNetwork"
            print_exc()
            Entry_54=None

        #self.macroNetwork.run()
        self.macroNetwork.freeze()

        ## saving connections for network GromosCluster ##
        input_Ports_34 = self.macroNetwork.ipNode
        if input_Ports_34 is not None and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_34, GROMOS_ClusterFiles_kryptonite_nbcr_net_36, "new", "traj", blocking=True
                    , splitratio=[0.45411042113261574, 0.54335719372693991])
            except:
                print "WARNING: failed to restore connection between input_Ports_34 and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 in network self.macroNetwork"
        if input_Ports_34 is not None and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_34, GROMOS_ClusterFiles_kryptonite_nbcr_net_36, "new", "active", blocking=True
                    , splitratio=[0.50935546751136695, 0.51596797621119816])
            except:
                print "WARNING: failed to restore connection between input_Ports_34 and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 in network self.macroNetwork"
        if input_Ports_34 is not None and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_34, GROMOS_ClusterFiles_kryptonite_nbcr_net_36, "new", "rmsd", blocking=True
                    , splitratio=[0.72697457023572398, 0.5609730307022871])
            except:
                print "WARNING: failed to restore connection between input_Ports_34 and GROMOS_ClusterFiles_kryptonite_nbcr_net_36 in network self.macroNetwork"
        if GROMOS_ClusterFiles_kryptonite_nbcr_net_36 is not None and GetClusterFrameLink_46 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GROMOS_ClusterFiles_kryptonite_nbcr_net_36, GetClusterFrameLink_46, "result", "urls", blocking=True
                    , splitratio=[0.72920790745169972, 0.25586352865051565])
            except:
                print "WARNING: failed to restore connection between GROMOS_ClusterFiles_kryptonite_nbcr_net_36 and GetClusterFrameLink_46 in network self.macroNetwork"
        if GetClusterFrameLink_46 is not None and DownloadSaveDir_51 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetClusterFrameLink_46, DownloadSaveDir_51, "newurl", "url", blocking=True
                    , splitratio=[0.6813604229397745, 0.24060738045908744])
            except:
                print "WARNING: failed to restore connection between GetClusterFrameLink_46 and DownloadSaveDir_51 in network self.macroNetwork"
        if input_Ports_34 is not None and DownloadSaveDir_51 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_34, DownloadSaveDir_51, "new", "path", blocking=True
                    , splitratio=[0.26234570709625593, 0.71051250549253275])
            except:
                print "WARNING: failed to restore connection between input_Ports_34 and DownloadSaveDir_51 in network self.macroNetwork"
        output_Ports_35 = self.macroNetwork.opNode
        if DownloadSaveDir_51 is not None and output_Ports_35 is not None:
            try:
                self.macroNetwork.connectNodes(
                    DownloadSaveDir_51, output_Ports_35, "output", "new", blocking=True
                    , splitratio=[0.32827353595918307, 0.22147048732628238])
            except:
                print "WARNING: failed to restore connection between DownloadSaveDir_51 and output_Ports_35 in network self.macroNetwork"
        if Entry_54 is not None and DownloadSaveDir_51 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Entry_54, DownloadSaveDir_51, "string", "cutdirs", blocking=True
                    , splitratio=[0.28715327854931738, 0.50903858482741082])
            except:
                print "WARNING: failed to restore connection between Entry_54 and DownloadSaveDir_51 in network self.macroNetwork"
        self.macroNetwork.runOnNewData.value = False

        ## modifying MacroInputNode dynamic ports
        input_Ports_34 = self.macroNetwork.ipNode
        input_Ports_34.outputPorts[1].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_traj')
        input_Ports_34.outputPorts[2].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_active')
        input_Ports_34.outputPorts[3].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_rmsd')
        input_Ports_34.outputPorts[4].configure(name='DownloadSaveDir_path')

        ## modifying MacroOutputNode dynamic ports
        output_Ports_35 = self.macroNetwork.opNode
        output_Ports_35.inputPorts[1].configure(singleConnection='auto')
        output_Ports_35.inputPorts[1].configure(name='DownloadSaveDir_output')
        ## configure MacroNode input ports
        GromosCluster_33.inputPorts[0].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_traj')
        GromosCluster_33.inputPorts[0].configure(datatype='string')
        GromosCluster_33.inputPorts[1].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_active')
        GromosCluster_33.inputPorts[1].configure(datatype='string')
        GromosCluster_33.inputPorts[2].configure(name='GROMOS_ClusterFiles_kryptonite_nbcr_net_rmsd')
        GromosCluster_33.inputPorts[2].configure(datatype='string')
        GromosCluster_33.inputPorts[3].configure(name='DownloadSaveDir_path')
        GromosCluster_33.inputPorts[3].configure(datatype='string')
        ## configure MacroNode output ports
        GromosCluster_33.outputPorts[0].configure(name='DownloadSaveDir_output')
        GromosCluster_33.outputPorts[0].configure(datatype='string')

        GromosCluster_33.shrink()

        ## reset modifications ##
        GromosCluster_33.resetTags()
        GromosCluster_33.buildOriginalList()
