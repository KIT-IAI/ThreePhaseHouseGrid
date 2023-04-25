# model of complete house

import pandapower as pp
import pandapower.toolbox as tb
from house_model.hv import HV_Model
from house_model.hv1 import HV1_Model
from house_model.uv2 import UV2_Model
from house_model.uv3 import UV3_Model
from house_model.uv4 import UV4_Model
from house_model.uv5 import UV5_Model
from house_model.uv6 import UV6_Model
from house_model.utils.modeling_methods import (
    create_line
)
from house_model import *

class House_Model:

    def __init__(self) -> None:
        hv = HV_Model()
        hv1 =  HV1_Model()
        uv2 = UV2_Model()
        uv3 = UV3_Model()
        uv4 = UV4_Model()
        uv5 = UV5_Model()
        uv6 = UV6_Model()

        uvs = [hv1, uv2, uv3, uv4, uv5, uv6]

        # init combined_net with main distributer
        self.net = hv.net
        # merge main distributer with all sub-distributers
        for uv in uvs:
            self.net = tb.merge_nets(self.net, uv.net, std_prio_on_net1 = True)

        # the pandapower merge function requires an external grid for every net that should be merged. Delete them
        ext_grids = list(range(1, len(self.net.ext_grid)))
        self.net.ext_grid.drop(ext_grids, inplace=True)

        # find all indices with connections
        mask = [v[:12] == "ExternalGrid" and len(v) < 17 for v in self.net.bus['name'].values]
        connections = self.net.bus.index[mask]
        janitza1 = self.net.bus.index[self.net.bus['name'] == "Janitza 1 - Red Outlets"][0]
        janitza2 = self.net.bus.index[self.net.bus['name'] == "UV2, UV3, UV4, UV6"][0]
        janitza8 = self.net.bus.index[self.net.bus['name'] == "Janitza 8 - Kitchen"][0]

        for i in range(0, len(connections)): 
            from_bus = janitza2 # uv2, 3, 4, 6 are connected to Janitza2
            to_bus = connections[i]
            if i == 0: # hv1
                from_bus = janitza1 # red sockets are connected to Janitza 1
            elif i == 4: # uv5
                from_bus = janitza8 # kitchen is connected to Janitza 8
            length = 0.001
            uv_nr = self.net.bus.iloc[to_bus]["name"][-1:]
            if uv_nr == "6":
                length = 0.02
            elif uv_nr == "5":
                length = 0.01
            elif uv_nr == "4":
                length = 0.01
            elif uv_nr == "3":
                length = 0.02
            elif uv_nr == "2":
                length = 0.005
            create_line(self.net, from_bus, to_bus, 0.001, "NYM_J_5x6", "Coupling")
