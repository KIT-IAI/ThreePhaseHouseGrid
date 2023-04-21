import pandapower as pp
import numpy as np
import json
from house_model.hardware_data.const import line_name_mapping
from os import path
import importlib.resources as rs

# create a bus
def create_bus(net, bus_name):
    return pp.create_bus(
        net,
        vn_kv=0.4,
        min_vm_pu=0.95,
        max_vm_pu=1.05,
        name=bus_name,
    )


# create a line
def create_line(net, from_bus, to_bus, length_km, line_type, line_name):
    pp.create_line(
        net,
        from_bus=from_bus,
        to_bus=to_bus,
        length_km=length_km,
        std_type=line_type,
        name=line_name + " (" + line_type + ")",
    )


# create a bus and connect it to another bus with a line
def create_bus_and_connect(net, from_bus, length_km, line_type, line_name):
    new_bus = create_bus(net, line_name)
    create_line(net, from_bus, new_bus, length_km, line_type, line_name)
    return new_bus


def create_std_types(net):
    std_lines = json.loads(rs.read_text("house_model.hardware_data", "cable_types.json"))

    # create standard types for all cable types
    for line_type in line_name_mapping:
        pp.create_std_type(
            net,
            {
                "r0_ohm_per_km": std_lines[line_name_mapping[line_type]][
                    "r_ohm_per_km"
                ],
                "x0_ohm_per_km": std_lines[line_name_mapping[line_type]][
                    "x_ohm_per_km"
                ],
                "c0_nf_per_km": std_lines[line_name_mapping[line_type]][
                    "c_nf_per_km"
                ],
                "max_i_ka": std_lines[line_name_mapping[line_type]][
                    "max_i_ka"
                ],
                "r_ohm_per_km": std_lines[line_name_mapping[line_type]][
                    "r_ohm_per_km"
                ],
                "x_ohm_per_km": std_lines[line_name_mapping[line_type]][
                    "x_ohm_per_km"
                ],
                "c_nf_per_km": std_lines[line_name_mapping[line_type]][
                    "c_nf_per_km"
                ],
                "type": "cs",
            },
            line_type,
        )


def create_load(uv, bus, p_mw, q_mvar, phase):
    if hasattr(uv, bus):
        bus = getattr(uv, bus)
    else:
        raise TypeError("Wrong bus")

    if phase == 1:
        pp.create_asymmetric_load(uv.net, bus, p_a_mw=p_mw, q_a_mvar=q_mvar)
    elif phase == 2:
        pp.create_asymmetric_load(uv.net, bus, p_b_mw=p_mw, q_b_mvar=q_mvar)
    elif phase == 3:
        pp.create_asymmetric_load(uv.net, bus, p_c_mw=p_mw, q_c_mvar=q_mvar)


def get_phase_of_consumer(sub_distributor, bus_name):
    if hasattr(sub_distributor, bus_name):
        bus_id = getattr(sub_distributor, bus_name)
    else:
        raise ValueError("Wrong bus name")

    line_id = np.where(sub_distributor.net.line.to_bus == bus_id)[0][0]
    from_bus = sub_distributor.net.line.from_bus[line_id]
    consumer_name = sub_distributor.net.bus.name[from_bus]

    if consumer_name[:7] == "Regler ":
        line_id = np.where(sub_distributor.net.line.to_bus == from_bus)[0][0]
        from_bus = sub_distributor.net.line.from_bus[line_id]
        consumer_name = sub_distributor.net.bus.name[from_bus]

    return consumer_name[:7]
