# model of main distributer sub-part 1 (red sockets and technic IT)
import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
) 

class HV1_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # access to public network, page 8/10 
        self.b0 =  create_bus(self.net, "ExternalGrid")

        # Separate the phases virtually by creating 3 busses and connecting them to the grid connection with lines
        # On those busses, only the respective phase is loaded with create_asymmetric_load()
        b1_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 1 Bus 0")
        b2_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 2 Bus 0")
        b3_0 = create_bus_and_connect(self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 3 Bus 0")

        # page 13/15 UV2
        b1_1 = create_bus_and_connect(self.net, b1_0, 0.001, "NYM_J_5x6", "Phase 1 Bus 1")
        b2_1 = create_bus_and_connect(self.net, b2_0, 0.001, "NYM_J_5x6", "Phase 2 Bus 1")
        b3_1 = create_bus_and_connect(self.net, b3_0, 0.001, "NYM_J_5x6", "Phase 3 Bus 1")

        # 1 Bus for the door bell and 2 door openers, all of them need very little power
        doorbell_and_dooropeners = create_bus_and_connect(self.net, b1_1, 0.02, "NYM_J_5x1.5", "DoorbellAndOpener P1")

        # page 14/16 
        # create new phase buses
        b1_2 = create_bus_and_connect(self.net, b1_1, 0.001, "NYM_J_5x6", "Phase 1 Bus 2")
        b2_2 = create_bus_and_connect(self.net, b2_1, 0.001, "NYM_J_5x6", "Phase 2 Bus 2")
        b3_2 = create_bus_and_connect(self.net, b3_1, 0.001, "NYM_J_5x6", "Phase 3 Bus 2")

        # lighting outside
        lighting_1_outside = create_bus_and_connect(self.net, b2_2, 0.04, "NYM_J_3x1.5", "OutsideLight 1 P2")
        lighting_2_outside = create_bus_and_connect(self.net, b2_2, 0.04, "NYM_J_3x1.5", "OutsideLight 2 P2")

        # emergency lighting
        emergency_lighting = create_bus_and_connect(self.net, b3_2, 0.05, "NYM_J_3x1.5", "EmergencyLight P3")

        # Model of page 15/17: we do not model the SV Beckhoffs as their power consumption is overall low

        # page 16/18, 17/19, 18/20
        # create new phase buses
        b1_3 = create_bus_and_connect(self.net, b1_2, 0.001, "NYM_J_5x6", "Phase 1 Bus 3")
        b2_3 = create_bus_and_connect(self.net, b2_2, 0.001, "NYM_J_5x6", "Phase 2 Bus 3")
        b3_3 = create_bus_and_connect(self.net, b3_2, 0.001, "NYM_J_5x6", "Phase 3 Bus 3")

        # Sockets 1 on phase 1 (technic IT)
        self.sockets1_technicIT = create_bus_and_connect(self.net, b1_3, 0.028, "NYM_J_3x2.5", "Outlets 1 HeaterRoom IT P1")

        # Sockets 2 on phase 2 (technic IT)
        self.sockets2_technicIT = create_bus_and_connect(self.net, b2_3, 0.030, "NYM_J_3x2.5", "Outlets 2 HeaterRoom IT P2")

        # Sockets 3 on phase 3 (technic IT)
        self.sockets3_technicIT = create_bus_and_connect(self.net, b3_3, 0.032, "NYM_J_3x2.5", "Outlets 3 HeaterRoom IT P3")

        # Sockets 4 on phase 1 (technic IT)
        self.sockets4_technicIT = create_bus_and_connect(self.net, b1_3, 0.035, "NYM_J_3x2.5", "Outlets 4 HeaterRoom IT P1")

        # Sockets technic outdoors and room 2 outdoors
        self.sockets_technic_outdoors =  create_bus_and_connect(self.net, b2_3, 0.04, "NYM_J_3x2.5", "Outlets HeaterRoom outside P2")
        self.sockets_room2_outdoors = create_bus_and_connect(self.net, b2_3, 0.04, "NYM_J_3x2.5", "Outlets Room 2 outside P2")

        # Sockets on phase 3 
        self.sockets_kitchen = create_bus_and_connect(self.net, b3_3, 0.024, "NYM_J_3x2.5", "Outlets Kitchen P3")
        self.sockets_restroom = create_bus_and_connect(self.net, b3_3, 0.024, "NYM_J_3x2.5", "Outlets Restroom P3")
        self.sockets_technic = create_bus_and_connect(self.net, b3_3, 0.024, "NYM_J_3x2.5", "Outlets HeaterRoom P3")
        self.sockets1_groundfloor_hallway = create_bus_and_connect(self.net, b3_3, 0.025, "NYM_J_3x2.5", "Outlets 1 Hallway Groundfloor P3")
        self.sockets2_groundfloor_hallway = create_bus_and_connect(self.net, b3_3, 0.025, "NYM_J_3x2.5", "Outlets 2 Hallway Groundfloor P3")
        self.sockets1_room1 = create_bus_and_connect(self.net, b3_3, 0.025, "NYM_J_3x2.5", "Outlets 1 Room 1 P3")
        self.sockets2_room1 = create_bus_and_connect(self.net, b3_3, 0.03, "NYM_J_3x2.5", "Outlets 2 Room 1 P3")
        self.sockets_room2 = create_bus_and_connect(self.net, b3_3, 0.03, "NYM_J_3x2.5", "Outlets Room 2 P3")

        # Sockets on phase 1
        self.sockets_room3 = create_bus_and_connect(self.net, b1_3, 0.04, "NYM_J_3x2.5", "Outlets Room 3 P1")
        self.sockets_room4 = create_bus_and_connect(self.net, b1_3, 0.04, "NYM_J_3x2.5", "Outlets Room 4 P1")
        line_u_sensors = create_bus_and_connect(self.net, b1_3, 0.05, "NYM_J_3x2.5", "Connection and Sensors P1")
        self.sockets_firstfloor_hallway= create_bus_and_connect(self.net, b1_3, 0.02, "NYM_J_3x2.5", "Outlets Hallway Upstairs P1")
        self.sockets_room5 = create_bus_and_connect(self.net, b1_3, 0.012, "NYM_J_3x2.5", "Outlets Room 5 P1")

        # until including page 18/20

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to HV1", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)

