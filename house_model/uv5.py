# model of sub-distributer 5 (kitchen and ground floor hallway)

import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
)

class UV5_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # page 4/6 of UV5
        # Grid connection of UV5
        self.b0 = create_bus(self.net, "ExternalGrid UV5")

        # Separate the phases virtually by creating 3 busses and connecting them to the grid connection with lines
        # On those busses, only the respective phase is loaded with create_asymmetric_load()
        # supply line is a NYM_J_5x6 cable
        b1_0 = create_bus_and_connect(
            self.net,
            self.b0,
            0.025,
            "NYM_J_5x6",
            "Phase 1 Bus 0 Kitchen",
        )
        b2_0 = create_bus_and_connect(
            self.net,
            self.b0,
            0.025,
            "NYM_J_5x6",
            "Phase 2 Bus 0 Kitchen",
        )
        b3_0 = create_bus_and_connect(
            self.net,
            self.b0,
            0.025,
            "NYM_J_5x6",
            "Phase 3 Bus 0 Kitchen",
        )

        # Socket 1 on phase 1 (kitchen)
        self.socket1_kitchen = create_bus_and_connect(
            self.net,
            b1_0,
            0.032,
            "NYM_J_3x2.5",
            "Outlet 1 Kitchen P1",
        )

        # Socket 4, 5, 6 on phase 2 (kitchen)
        self.socket4_kitchen = create_bus_and_connect(
            self.net,
            b2_0,
            0.032,
            "NYM_J_3x2.5",
            "Outlet 4 Kitchen P2",
        )
        self.socket5_kitchen = create_bus_and_connect(
            self.net,
            b2_0,
            0.032,
            "NYM_J_3x2.5",
            "Outlet 5 Kitchen P2",
        )
        self.socket6_kitchen = create_bus_and_connect(
            self.net,
            b2_0,
            0.032,
            "NYM_J_3x2.5",
            "Outlet 6 Kitchen P2",
        )

        # create new phase buses
        b1_1 = create_bus_and_connect(
            self.net,
            b1_0,
            0.001,
            "NYM_J_5x6",
            "Phase 1 Bus 1",
        )
        b2_1 = create_bus_and_connect(
            self.net,
            b2_0,
            0.001,
            "NYM_J_5x6",
            "Phase 2 Bus 1",
        )
        b3_1 = create_bus_and_connect(
            self.net,
            b3_0,
            0.001,
            "NYM_J_5x6",
            "Phase 3 Bus 1",
        )

        # Socket (2+3), (7+8), (9+10) on phase 3 (kitchen)
        self.socket2and3_kitchen = create_bus_and_connect(
            self.net,
            b3_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 2+3 Kitchen P3",
        )
        self.socket7and8_kitchen = create_bus_and_connect(
            self.net,
            b3_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 7+8 Kitchen P3",
        )
        self.socket9and10_kitchen = create_bus_and_connect(
            self.net,
            b3_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 9+10 Kitchen P3",
        )

        # Socket 11 (kitchen)
        self.socket11_kitchen = create_bus_and_connect(
            self.net,
            b1_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 11 Kitchen P1",
        )

        # Socket 12 (kitchen)
        self.socket12_kitchen = create_bus_and_connect(
            self.net,
            b2_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 12 Kitchen P2",
        )

        # Socket 13 (kitchen)
        self.socket13_kitchen = create_bus_and_connect(
            self.net,
            b3_1,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 13 Kitchen P3",
        )

        # create new phase buses
        b1_2 = create_bus_and_connect(
            self.net,
            b1_1,
            0.001,
            "NYM_J_5x6",
            "Phase 1 Bus 2",
        )
        b2_2 = create_bus_and_connect(
            self.net,
            b2_1,
            0.001,
            "NYM_J_5x6",
            "Phase 2 Bus 2",
        )
        b3_2 = create_bus_and_connect(
            self.net,
            b3_1,
            0.001,
            "NYM_J_5x6",
            "Phase 3 Bus 2",
        )

        # Socket 14 on phase 1 (kitchen)
        self.socket14_kitchen = create_bus_and_connect(
            self.net,
            b1_2,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 14 Kitchen P1",
        )

        # Socket (15+16) on phase 2 (kitchen)
        self.socket15and16_kitchen = create_bus_and_connect(
            self.net,
            b2_2,
            0.024,
            "NYM_J_3x2.5",
            "Outlet 15+16 Kitchen P2",
        )

        # Socket 1 and 2 on ground floor hallway
        self.socket1_hallway = create_bus_and_connect(
            self.net,
            b3_2,
            0.036,
            "NYM_J_3x2.5",
            "Outlet 1 Hallway Groundfloor P3",
        )
        self.socket2_hallway = create_bus_and_connect(
            self.net,
            b3_2,
            0.035,
            "NYM_J_3x2.5",
            "Outlet 2 Hallway Groundfloor P3",
        )

        # create new phase buses
        b1_3 = create_bus_and_connect(
            self.net,
            b1_2,
            0.001,
            "NYM_J_5x6",
            "Phase 1 Bus 3",
        )
        b2_3 = create_bus_and_connect(
            self.net,
            b2_2,
            0.001,
            "NYM_J_5x6",
            "Phase 2 Bus 3",
        )
        b3_3 = create_bus_and_connect(
            self.net,
            b3_2,
            0.001,
            "NYM_J_5x6",
            "Phase 3 Bus 3",
        )

        # electric stove (on all 3 phases)
        self.electricstove_p1 = create_bus_and_connect(
            self.net,
            b1_3,
            0.024,
            "NYM_J_5x2.5",
            "Stove P1",
        )
        self.electricstove_p2 = create_bus_and_connect(
            self.net,
            b2_3,
            0.024,
            "NYM_J_5x2.5",
            "Stove P2",
        )
        self.electricstove_p3 = create_bus_and_connect(
            self.net,
            b3_3,
            0.024,
            "NYM_J_5x2.5",
            "Stove P3",
        )

        # lighting for kitchen and ground floor hallway
        self.lighting_1_kitchen = create_bus_and_connect(
            self.net,
            b1_3,
            0.02,
            "NYM_J_3x1.5",
            "Lighting 1 Kitchen P1",
        )
        self.lighting_1_hallway = create_bus_and_connect(
            self.net,
            b1_3,
            0.03,
            "NYM_J_3x1.5",
            "Lighting 1 Hallway Groundfloor P1",
        )
        self.lighting_2_hallway = create_bus_and_connect(
            self.net,
            b1_3,
            0.03,
            "NYM_J_3x1.5",
            "Lighting 2 Hallway Groundfloor P1",
        )

        # create new phase buses
        b1_4 = create_bus_and_connect(
            self.net,
            b1_3,
            0.001,
            "NYM_J_5x6",
            "Phase 1 Bus 4",
        )
        b2_4 = create_bus_and_connect(
            self.net,
            b2_3,
            0.001,
            "NYM_J_5x6",
            "Phase 2 Bus 4",
        )
        b3_4 = create_bus_and_connect(
            self.net,
            b3_3,
            0.001,
            "NYM_J_5x6",
            "Phase 3 Bus 4",
        )

        # Door 1 (kitchen)
        self.door1_kitchen = create_bus_and_connect(
            self.net,
            b1_4,
            0.036,
            "NYM_J_5x1.5",
            "Door 1 Kitchen P1",
        )

        # Door 2 (kitchen)
        self.door2_kitchen = create_bus_and_connect(
            self.net,
            b2_4,
            0.036,
            "NYM_J_5x1.5",
            "Door 2 Kitchen P2",
        )

        # Floor heating (kitchen)
        floor_heating_controller_kitchen = create_bus_and_connect(
            self.net,
            b3_4,
            0.03,
            "NYM_J_5x1.5",
            "Controller Floor Heating Kitchen P3",
        )
        self.floor_heating_kitchen = create_bus_and_connect(
            self.net,
            floor_heating_controller_kitchen,
            0.01,
            "NYM_J_3x1.5",
            "Floor Heating Kitchen P3",
        )

        # Floor heating (ground floor hallway)
        floor_heating_controller_hallway = create_bus_and_connect(
            self.net,
            b1_4,
            0.036,
            "NYM_J_5x1.5",
            "Controller Floor Heating Hallway Groundfloor P1",
        )
        self.floor_heating_hallway = create_bus_and_connect(
            self.net,
            floor_heating_controller_hallway,
            0.01,
            "NYM_J_3x1.5",
            "Floor Heating Hallway Groundfloor P1",
        )

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to UV5", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)
