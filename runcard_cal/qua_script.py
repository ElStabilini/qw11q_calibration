
# Single QUA script generated at 2024-11-28 08:15:20.706003
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(int, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "D1/acquisition")
    with for_(v1,0,(v1<1024),(v1+1)):
        with for_(v4,0.0,(v4<2.000050505050505),(v4+0.0201010101010101)):
            with for_(v5,-241729925,(v5<=-43729925),(v5+2000000)):
                update_frequency("D1/drive", v5, "Hz", False)
                align()
                play("5767322910915911634"*amp(v4), "D1/drive")
                wait(11, "D1/acquisition")
                measure("6130916834242668600", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                r1 = declare_stream()
                save(v2, r1)
                r2 = declare_stream()
                save(v3, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(100).buffer(100).average().save("6130916834242668600_D1|acquisition_I")
        r2.buffer(100).buffer(100).average().save("6130916834242668600_D1|acquisition_Q")


config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
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
        "con6": {
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
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "1": {},
                "3": {},
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
    },
    "octaves": {
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D4/flux": {
            "singleInput": {
                "port": ('con9', 6),
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
        "D1/acquisition": {
            "RF_inputs": {
                "port": ('octave5', 1),
            },
            "RF_outputs": {
                "port": ('octave5', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -312359338.83203506,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "6130916834242668600": "6130916834242668600_D1/acquisition",
            },
        },
        "D1/drive": {
            "RF_inputs": {
                "port": ('octave5', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-1683035313063582543": "-1683035313063582543",
                "5767322910915911634": "5767322910915911634",
            },
        },
    },
    "pulses": {
        "6130916834242668600_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8455068447658117415_i",
                "Q": "-8455068447658117415_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "-1683035313063582543": {
            "length": 40,
            "waveforms": {
                "I": "-1683035313063582543_i",
                "Q": "-1683035313063582543_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5767322910915911634": {
            "length": 40,
            "waveforms": {
                "I": "5767322910915911634_i",
                "Q": "5767322910915911634_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8455068447658117415_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-8455068447658117415_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1683035313063582543_i": {
            "samples": [0.002132055157310482, 0.002868993803335302, 0.0038007992635461685, 0.004957176760299966, 0.006365140955238952, 0.00804629210406868, 0.010013772316473034, 0.012269130313650718, 0.01479939611841342, 0.017574717737766116, 0.020546926693444746, 0.023649367659241707, 0.02679824437907837, 0.029895601935751654, 0.03283389536659392, 0.03550190571409452, 0.03779158191367791, 0.03960523779750896, 0.040862443000014154] + [0.04150593284451844] * 2 + [0.040862443000014154, 0.03960523779750896, 0.03779158191367791, 0.03550190571409452, 0.03283389536659392, 0.029895601935751654, 0.02679824437907837, 0.023649367659241707, 0.020546926693444746, 0.017574717737766116, 0.01479939611841342, 0.012269130313650718, 0.010013772316473034, 0.00804629210406868, 0.006365140955238952, 0.004957176760299966, 0.0038007992635461685, 0.002868993803335302, 0.002132055157310482],
            "type": "arbitrary",
        },
        "-1683035313063582543_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "5767322910915911634_i": {
            "samples": [0.005100962599693585, 0.006864095443021811, 0.009093449025375556, 0.011860093378755864, 0.015228661342612523, 0.01925083173778656, 0.023958047188897096, 0.02935401302640185, 0.035407698454343425, 0.042047682290548435, 0.049158720984554975, 0.056581341023264856, 0.06411505905295913, 0.0715255169861391, 0.07855541245871156, 0.08493865303836143, 0.09041672550728236, 0.09475591476343967, 0.09776379037872578] + [0.09930334605993978] * 2 + [0.09776379037872578, 0.09475591476343967, 0.09041672550728236, 0.08493865303836143, 0.07855541245871156, 0.0715255169861391, 0.06411505905295913, 0.056581341023264856, 0.049158720984554975, 0.042047682290548435, 0.035407698454343425, 0.02935401302640185, 0.023958047188897096, 0.01925083173778656, 0.015228661342612523, 0.011860093378755864, 0.009093449025375556, 0.006864095443021811, 0.005100962599693585],
            "type": "arbitrary",
        },
        "5767322910915911634_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
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
        "con6": {
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
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
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
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
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
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "D1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con6', 1),
                "out2": ('con6', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": -312359338.83203506,
            "operations": {
                "6130916834242668600": "6130916834242668600_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_ecb",
                "lo_frequency": 7450000000.0,
            },
        },
        "D1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-1683035313063582543": "-1683035313063582543",
                "5767322910915911634": "5767322910915911634",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_30e",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "6130916834242668600_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8455068447658117415_i",
                "Q": "-8455068447658117415_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "-1683035313063582543": {
            "length": 40,
            "waveforms": {
                "I": "-1683035313063582543_i",
                "Q": "-1683035313063582543_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5767322910915911634": {
            "length": 40,
            "waveforms": {
                "I": "5767322910915911634_i",
                "Q": "5767322910915911634_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8455068447658117415_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-8455068447658117415_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1683035313063582543_i": {
            "samples": [0.002132055157310482, 0.002868993803335302, 0.0038007992635461685, 0.004957176760299966, 0.006365140955238952, 0.00804629210406868, 0.010013772316473034, 0.012269130313650718, 0.01479939611841342, 0.017574717737766116, 0.020546926693444746, 0.023649367659241707, 0.02679824437907837, 0.029895601935751654, 0.03283389536659392, 0.03550190571409452, 0.03779158191367791, 0.03960523779750896, 0.040862443000014154] + [0.04150593284451844] * 2 + [0.040862443000014154, 0.03960523779750896, 0.03779158191367791, 0.03550190571409452, 0.03283389536659392, 0.029895601935751654, 0.02679824437907837, 0.023649367659241707, 0.020546926693444746, 0.017574717737766116, 0.01479939611841342, 0.012269130313650718, 0.010013772316473034, 0.00804629210406868, 0.006365140955238952, 0.004957176760299966, 0.0038007992635461685, 0.002868993803335302, 0.002132055157310482],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1683035313063582543_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5767322910915911634_i": {
            "samples": [0.005100962599693585, 0.006864095443021811, 0.009093449025375556, 0.011860093378755864, 0.015228661342612523, 0.01925083173778656, 0.023958047188897096, 0.02935401302640185, 0.035407698454343425, 0.042047682290548435, 0.049158720984554975, 0.056581341023264856, 0.06411505905295913, 0.0715255169861391, 0.07855541245871156, 0.08493865303836143, 0.09041672550728236, 0.09475591476343967, 0.09776379037872578] + [0.09930334605993978] * 2 + [0.09776379037872578, 0.09475591476343967, 0.09041672550728236, 0.08493865303836143, 0.07855541245871156, 0.0715255169861391, 0.06411505905295913, 0.056581341023264856, 0.049158720984554975, 0.042047682290548435, 0.035407698454343425, 0.02935401302640185, 0.023958047188897096, 0.01925083173778656, 0.015228661342612523, 0.011860093378755864, 0.009093449025375556, 0.006864095443021811, 0.005100962599693585],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5767322910915911634_q": {
            "samples": [0.0] * 40,
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "D1/acquisition_mixer_ecb": [{'intermediate_frequency': -312359338.83203506, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_30e": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

