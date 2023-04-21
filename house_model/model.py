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
    create_std_types,
    create_bus,
    create_bus_and_connect,
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
            self.net = tb.merge_nets(self.net, uv.net)