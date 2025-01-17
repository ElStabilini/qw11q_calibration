
# Single QUA script generated at 2025-01-17 18:05:03.078128
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    set_dc_offset("B1/flux", "single", -0.08233987198571363)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", 0.30438797397930567)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.34274625187777014)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", 0.30347347513189465)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", -0.2839878581260484)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        with for_(v5,0.0,(v5<1.9924937343358393),(v5+0.004987468671679198)):
            align()
            play("8826301506390161185", "B4/drive")
            wait(11, "B4/flux")
            play("5073282938335323174"*amp(v5), "B4/flux")
            wait(16, "B4/drive")
            play("-8859351938095828562", "B4/drive")
            wait(36, "B4/acquisition")
            measure("8565979434463953312", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
            r1 = declare_stream()
            save(v4, r1)
            wait(25000, )
    with stream_processing():
        r1.buffer(400).average().save("8565979434463953312_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.08233987198571363,
                    "filter": {},
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.21674190528643072,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
                "7": {
                    "offset": -0.04,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
        "con2": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "1": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                },
            },
        },
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "7": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
    },
    "octaves": {
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "4": {
                    "LO_frequency": 6700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {},
        },
    },
    "elements": {
        "B1/flux": {
            "singleInput": {
                "port": ('con4', 1),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B2/flux": {
            "singleInput": {
                "port": ('con4', 2),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D2/flux": {
            "singleInput": {
                "port": ('con9', 4),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B3/flux": {
            "singleInput": {
                "port": ('con4', 3),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B4/flux": {
            "singleInput": {
                "port": ('con4', 4),
            },
            "intermediate_frequency": 0,
            "operations": {
                "722788905596101028": "722788905596101028",
                "5073282938335323174": "5073282938335323174",
            },
        },
        "D4/flux": {
            "singleInput": {
                "port": ('con9', 6),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B5/flux": {
            "singleInput": {
                "port": ('con4', 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D5/flux": {
            "singleInput": {
                "port": ('con9', 7),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B4/acquisition": {
            "RF_inputs": {
                "port": ('octave2', 1),
            },
            "RF_outputs": {
                "port": ('octave2', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 330298316.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "8565979434463953312": "8565979434463953312_B4/acquisition",
            },
        },
        "B4/drive": {
            "RF_inputs": {
                "port": ('octave3', 4),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 7),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 109678455.0,
            "operations": {
                "8826301506390161185": "8826301506390161185",
                "-8859351938095828562": "-8859351938095828562",
            },
        },
    },
    "pulses": {
        "8826301506390161185": {
            "length": 40,
            "waveforms": {
                "I": "8826301506390161185_i",
                "Q": "8826301506390161185_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "722788905596101028": {
            "length": 60,
            "waveforms": {
                "single": "722788905596101028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8565979434463953312_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4459496686098595328_i",
                "Q": "4459496686098595328_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "5073282938335323174": {
            "length": 60,
            "waveforms": {
                "single": "5073282938335323174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8859351938095828562": {
            "length": 40,
            "waveforms": {
                "I": "-8859351938095828562_i",
                "Q": "-8859351938095828562_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8826301506390161185_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
        },
        "8826301506390161185_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "722788905596101028": {
            "sample": 0.1,
            "type": "constant",
        },
        "4459496686098595328_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4459496686098595328_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5073282938335323174": {
            "sample": 0.10025125628140705,
            "type": "constant",
        },
        "-8859351938095828562_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "-8859351938095828562_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.08233987198571363,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.21674190528643072,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": -0.04,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con2": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 1),
            },
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 2),
            },
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 4),
            },
        },
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 3),
            },
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
            },
        },
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "operations": {
                "722788905596101028": "722788905596101028",
                "5073282938335323174": "5073282938335323174",
            },
            "singleInput": {
                "port": ('con4', 4),
            },
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 6),
            },
        },
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 5),
            },
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "B4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1),
                "out2": ('con2', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": 330298316.0,
            "operations": {
                "8565979434463953312": "8565979434463953312_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_f13",
                "lo_frequency": 7370000000.0,
            },
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109678455.0,
            "operations": {
                "8826301506390161185": "8826301506390161185",
                "-8859351938095828562": "-8859351938095828562",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_813",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "8826301506390161185": {
            "length": 40,
            "waveforms": {
                "I": "8826301506390161185_i",
                "Q": "8826301506390161185_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "722788905596101028": {
            "length": 60,
            "waveforms": {
                "single": "722788905596101028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8565979434463953312_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4459496686098595328_i",
                "Q": "4459496686098595328_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "5073282938335323174": {
            "length": 60,
            "waveforms": {
                "single": "5073282938335323174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8859351938095828562": {
            "length": 40,
            "waveforms": {
                "I": "-8859351938095828562_i",
                "Q": "-8859351938095828562_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8826301506390161185_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8826301506390161185_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "722788905596101028": {
            "sample": 0.1,
            "type": "constant",
        },
        "4459496686098595328_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4459496686098595328_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5073282938335323174": {
            "sample": 0.10025125628140705,
            "type": "constant",
        },
        "-8859351938095828562_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8859351938095828562_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B4/acquisition_mixer_f13": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_813": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

