# model of sub-distributer 3 (room 3 and 4)

import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
)

class UV3_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # page 4/6 of UV3

        # Grid connection of uv3
        self.b0 = create_bus(self.net, "ExternalGrid UV3")

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

        # Socket (1+2), (3+4), (5+6) on phase 1 (room 3)
        self.socket1and2_R3 = create_bus_and_connect(
            self.net, b1_0, 0.012, "NYM_J_3x2.5", "Outlet 1+2 Room 3 P1"
        )
        self.socket3and4_R3 = create_bus_and_connect(
            self.net, b1_0, 0.015, "NYM_J_3x2.5", "Outlet 3+4 Room 3 P1"
        )
        self.socket5and6_R3 = create_bus_and_connect(
            self.net, b1_0, 0.025, "NYM_J_3x2.5", "Outlet 5+6 Room 3 P1"
        )

        # Socket (1+2), (3+4), (5+6) on phase 2 (room 4)
        self.socket1and2_R4 = create_bus_and_connect(
            self.net, b2_0, 0.012, "NYM_J_3x2.5", "Outlet 1+2 Room 4 P2"
        )
        self.socket3and4_R4 = create_bus_and_connect(
            self.net, b2_0, 0.016, "NYM_J_3x2.5", "Outlet 3+4 Room 4 P2"
        )
        self.socket5and6_R4 = create_bus_and_connect(
            self.net, b2_0, 0.020, "NYM_J_3x2.5", "Outlet 5+6 Room 4 P2"
        )

        # page 5/7 of UV3

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

        # lighting for room 3
        lighting_1_R3 = create_bus_and_connect(
            self.net, b1_1, 0.02, "NYM_J_3x1.5", "Lighting 1 Room 3 P1"
        )
        lighting_2_R3 = create_bus_and_connect(
            self.net, b1_1, 0.02, "NYM_J_3x1.5", "Lighting 2 Room 3 P1"
        )

        # lighting for room 4
        lighting_1_R4 = create_bus_and_connect(
            self.net, b2_1, 0.025, "NYM_J_3x1.5", "Lighting 1 Room 4 P2"
        )
        lighting_2_R4 = create_bus_and_connect(
            self.net, b2_1, 0.025, "NYM_J_3x1.5", "Lighting 2 Room 4 P2"
        )

        # electric shutters (room 3)
        shutter_1_R3 = create_bus_and_connect(
            self.net, b3_1, 0.03, "NYM_J_5x1.5", "Shades 1 Room 3 P3"
        )
        shutter_2_R3 = create_bus_and_connect(
            self.net, b3_1, 0.03, "NYM_J_5x1.5", "Shades 2 Room 3 P3"
        )

        # electric shutters (room 4)
        shutter_1_R4 = create_bus_and_connect(
            self.net, b3_1, 0.03, "NYM_J_5x1.5", "Shades 1 Room 4 P3"
        )
        shutter_2_R4 = create_bus_and_connect(
            self.net, b3_1, 0.03, "NYM_J_5x1.5", "Shades 2 Room 4 P3"
        )

        # page 6/8 of UV3
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

        # Floor heating (room 3)
        floor_heating_controller_R3 = create_bus_and_connect(
            self.net, b1_2, 0.015, "NYM_J_5x1.5", "Controller Floor Heating Room 3 P1"
        )
        floor_heating_R3 = create_bus_and_connect(
            self.net,
            floor_heating_controller_R3,
            0.01,
            "NYM_J_3x1.5",
            "Floor Heating Room 3 P1",
        )

        # Floor heating (room 4)
        floor_heating_controller_R4 = create_bus_and_connect(
            self.net, b2_2, 0.002, "NYM_J_5x1.5", "Controller Floor Heating Room 4 P2"
        )
        floor_heating_1_R4 = create_bus_and_connect(
            self.net,
            floor_heating_controller_R4,
            0.015,
            "NYM_J_3x1.5",
            "Floor Heating 1 Room 4 P2",
        )
        floor_heating_2_R4 = create_bus_and_connect(
            self.net,
            floor_heating_controller_R4,
            0.015,
            "NYM_J_3x1.5",
            "Floor Heating 2 Room 4 P2",
        )

        # Door (room 4)
        door_R4 = create_bus_and_connect(
            self.net, b3_2, 0.015, "NYM_J_5x1.5", "Door Room 4 P3"
        )

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to UV3", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)

