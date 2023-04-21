# model of main distributer 

import pandapower as pp
import pandapower.toolbox as tb
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
) 

class HV_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # access to public network, page 8/10 
        # Grid connection with public network
        b0 =  create_bus(self.net, "ExternalGrid Public Grid")

        b_3phases = create_bus_and_connect(self.net, b0, 0.001, "NYM_J_5x6", "All Phases Bus 0")

        b_janitza1 = create_bus_and_connect(self.net, b_3phases, 0.001, "grid_connection", "Janitza 1 - Red Outlets")

        b_janitza2 = create_bus_and_connect(self.net, b_3phases, 0.001, "grid_connection", "Janitza 2 - Public Grid")

        b_janitza5 = create_bus_and_connect(self.net, b_janitza2, 0.001, "grid_connection", "Janitza 5 - EV Charger 1")

        b_janitza6 = create_bus_and_connect(self.net, b_janitza2, 0.001, "grid_connection", "Janitza 6 - EV Charger 2")

        b_janitza7 = create_bus_and_connect(self.net, b_janitza2, 0.001, "grid_connection", "Janitza 7 - Heating")

        b_uvs = create_bus_and_connect(self.net, b_janitza2, 0.001, "grid_connection", "UV2, UV3, UV4, UV6")

        b_janitza8 = create_bus_and_connect(self.net, b_janitza2, 0.001, "grid_connection", "Janitza 8 - Kitchen")

        # end of model

        # external grid
        pp.create_ext_grid(self.net, bus=b0, vm_pu = 1.00, name="Grid to UVs", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)
   
       

