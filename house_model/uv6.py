# model of sub-distributer 6 (room 1 and 2)

import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
)

class UV6_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # page 4/6 of UV6

        # Grid connection of UV6
        self.b0 = create_bus(self.net, "ExternalGrid UV6")

        # Separate the phases virtually by creating 3 busses and connecting them to the grid connection with lines
        # On those busses, only the respective phase is loaded with create_asymmetric_load()
        # supply line is a NYM_J_5x6 cable
        b1_0 = create_bus_and_connect(
            self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 1 Bus 0"
        )
        b2_0 = create_bus_and_connect(
            self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 2 Bus 0"
        )
        b3_0 = create_bus_and_connect(
            self.net, self.b0, 0.001, "NYM_J_5x6", "Phase 3 Bus 0"
        )

        # socket (1+2) (room 1) and socket outdoors
        self.socket1and2_R1 = create_bus_and_connect(
            self.net, b1_0, 0.013, "NYM_J_3x2.5", "Outlet 1+2 Room 1 P1"
        )
        self.socket_outdoors = create_bus_and_connect(
            self.net, b1_0, 0.025, "NYM_J_3x2.5", "Outlet outside P1"
        )

        # socket (1+2) and (3+4) (room 2)
        self.socket1and2_R2 = create_bus_and_connect(
            self.net, b2_0, 0.015, "NYM_J_3x2.5", "Outlet 1+2 Room 2 P2"
        )
        self.socket3and4_R2 = create_bus_and_connect(
            self.net, b2_0, 0.017, "NYM_J_3x2.5", "Outlet 3+4 Room 2 P2"
        )

        # page 5/7 of UV6

        # create new phase buses
        b1_1 = create_bus_and_connect(
            self.net, b1_0, 0.001, "NYM_J_5x6", "Phase 1 Bus 1"
        )
        b2_1 = create_bus_and_connect(
            self.net, b2_0, 0.001, "NYM_J_5x6", "Phase 2 Bus 1"
        )
        b3_1 = create_bus_and_connect(
            self.net, b3_0, 0.001, "NYM_J_5x6", "Phase 3 Bus 1"
        )

        # electric shutters (room 1)
        shutter_1_R1 = create_bus_and_connect(
            self.net, b1_1, 0.04, "NYM_J_5x1.5", "Shades 1 Room 1 P1"
        )
        shutter_2_R1 = create_bus_and_connect(
            self.net, b1_1, 0.04, "NYM_J_5x1.5", "Shades 2 Room 1 P1"
        )

        # electric shutters (room 2)
        shutter_1_R2 = create_bus_and_connect(
            self.net, b1_1, 0.05, "NYM_J_5x1.5", "Shades 1 Room 2 P1"
        )
        shutter_2_R2 = create_bus_and_connect(
            self.net, b1_1, 0.05, "NYM_J_5x1.5", "Shades 2 Room 2 P1"
        )

        # lighting for room 1 and 2
        lighting_1_R1 = create_bus_and_connect(
            self.net, b2_1, 0.02, "NYM_J_3x1.5", "Lighting Room 1 P2"
        )
        lighting_1_R2 = create_bus_and_connect(
            self.net, b2_1, 0.02, "NYM_J_3x1.5", "Lighting Room 2 P2"
        )

        # page 7/9 of UV6

        # create new phase buses
        b1_2 = create_bus_and_connect(
            self.net, b1_1, 0.001, "NYM_J_5x6", "Phase 1 Bus 2"
        )
        b2_2 = create_bus_and_connect(
            self.net, b2_1, 0.001, "NYM_J_5x6", "Phase 2 Bus 2"
        )
        b3_2 = create_bus_and_connect(
            self.net, b3_1, 0.001, "NYM_J_5x6", "Phase 3 Bus 2"
        )

        # Floor heating (room 1)
        floor_heating_controller_R1 = create_bus_and_connect(
            self.net, b2_2, 0.015, "NYM_J_5x1.5", "Controller Floor Heating Room 1 P2"
        )
        floor_heating_R1 = create_bus_and_connect(
            self.net,
            floor_heating_controller_R1,
            0.005,
            "NYM_J_3x1.5",
            "Floor Heating Room 1 P2",
        )

        # Floor heating (room 2)
        floor_heating_controller_R2 = create_bus_and_connect(
            self.net, b3_2, 0.04, "NYM_J_5x1.5", "Controller Floor Heating Room 2 P3"
        )
        floor_heating_R2 = create_bus_and_connect(
            self.net,
            floor_heating_controller_R2,
            0.015,
            "NYM_J_3x1.5",
            "Floor Heating Room 2 P3",
        )

        # Door (room 1)
        door_R1 = create_bus_and_connect(
            self.net, b1_2, 0.015, "NYM_J_5x1.5", "Door Room 1 P1"
        )

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to UV6", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)
