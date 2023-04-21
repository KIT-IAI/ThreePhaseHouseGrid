# model of sub-distributer 2 (parts of room 5 and first floor hallway), considers building 666 (Stromhaus SH) only
import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
) 

class UV2_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # access to public network, page 8/10 
        self.b0 =  create_bus(self.net, "ExternalGrid UV2")

        # Separate the phases virtually by creating 3 busses and connecting them to the grid connection with lines
        # On those busses, only the respective phase is loaded with create_asymmetric_load()
        b1_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 1 Bus 0")
        b2_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 2 Bus 0")
        #b3_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 3 Bus 0")

        self.sockets_firstfloor_hallway =  create_bus_and_connect(self.net, b1_0, 0.005, "NYM_J_3x2.5", "Outlet Hallway Upstairs P1")

        #b1_1 = create_bus_and_connect(self.net,b1_0, 0.001, "NYM_J_5x6", "Phase 1 Bus 1")
        b2_1 = create_bus_and_connect(self.net,b2_0, 0.001, "NYM_J_5x6", "Phase 2 Bus 1")
        #b3_1 = create_bus_and_connect(self.net,b3_0, 0.001, "NYM_J_5x6", "Phase 3 Bus 1")

        # Floor heating (room5)
        floor_heating_controller_room5 = create_bus_and_connect(self.net,b2_1, 0.012, "NYM_J_5x1.5", "Floor Heating Controller 5 P2")
        floor_heating1_room5 = create_bus_and_connect(self.net,floor_heating_controller_room5, 0.015, "NYM_J_3x1.5", "Floor Heating 1 Room 5 P2")
        floor_heating2_room5 = create_bus_and_connect(self.net,floor_heating_controller_room5, 0.015, "NYM_J_3x1.5", "Floor Heating 2 Room 5 P2")

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to UV2", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)
  

