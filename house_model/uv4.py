# model of sub-distributer 4 (technical room and WC)

import pandapower as pp
from house_model.utils.modeling_methods import (
    create_std_types,
    create_bus,
    create_bus_and_connect,
)


class UV4_Model:
    def __init__(self):
        self.net = pp.create_empty_network(name="empty")
        create_std_types(self.net)

        # page 4/6 of UV4
        # Grid connection of UV4
        self.b0 = create_bus(self.net, "ExternalGrid UV4")

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

        # Socket 1 and 2 on phase 1 (technical room TR)
        self.socket1_TR = create_bus_and_connect(
            self.net, b1_0, 0.008, "NYM_J_3x2.5", "Outlet 1 HeaterRoom P1"
        )
        self.socket2_TR = create_bus_and_connect(
            self.net, b1_0, 0.012, "NYM_J_3x2.5", "Outlet 2 HeaterRoom P1"
        )

        # Socket 3 (technical room) and socket (2+3) Restroom on phase 2
        self.socket3_TR = create_bus_and_connect(
            self.net, b2_0, 0.018, "NYM_J_3x2.5", "Outlet 3 HeaterRoom P2"
        )
        self.socket2and3_restroom = create_bus_and_connect(
            self.net, b2_0, 0.01, "NYM_J_3x2.5", "Outlet 2+3 Restroom P2"
        )

        # Fan Heating (WC)
        fan_heating_restroom = create_bus_and_connect(
            self.net, b3_0, 0.01, "NYM_J_3x2.5", "Heater Restroom P3"
        )

        # Infrared Heating (WC)
        infrared_heating_restroom = create_bus_and_connect(
            self.net, b1_0, 0.01, "NYM_J_3x2.5", "Infraredheater Restroom P1"
        )

        # page 5/7 of UV4
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

        # lighting for Restroom and technical room
        lighting_1_restroom = create_bus_and_connect(
            self.net, b1_1, 0.02, "NYM_J_3x1.5", "Lighting 1 Restroom P1"
        )
        lighting_2_restroom = create_bus_and_connect(
            self.net, b1_1, 0.02, "NYM_J_3x1.5", "Lighting 2 Restroom P1"
        )
        lighting_1_TR = create_bus_and_connect(
            self.net, b1_1, 0.02, "NYM_J_3x1.5", "Lighting TR P1"
        )

        # armatures in restroom
        washingfaucet1_restroom = create_bus_and_connect(
            self.net, b2_1, 0.025, "NYM_J_3x1.5", "Faucet 1 Restroom P2"
        )
        showerfaucet1_restroom = create_bus_and_connect(
            self.net, b2_1, 0.025, "NYM_J_3x1.5", "Shower faucet Restroom P2"
        )
        washingfaucet2_restroom = create_bus_and_connect(
            self.net, b2_1, 0.025, "NYM_J_3x1.5", "Faucet 2 Restroom P2"
        )

        # Floor heating (restroom)
        floor_heating_controller_restroom = create_bus_and_connect(
            self.net, b3_1, 0.025, "NYM_J_5x1.5", "Controller Floor Heating Restroom P3"
        )
        floor_heating_restroom = create_bus_and_connect(
            self.net,
            floor_heating_controller_restroom,
            0.005,
            "NYM_J_3x1.5",
            "Floor Heating Restroom P3",
        )

        # end of model

        # external grid for pandapower merge function
        pp.create_ext_grid(self.net, bus=self.b0, vm_pu = 1.00, name="Grid to UV4", s_sc_max_mva=1000, rx_max=0.1, r0x0_max=0.1, x0x_max=1.0)

