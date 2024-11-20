
# Single QUA script generated at 2024-11-20 04:55:04.899955
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "D1/acquisition")
    with for_(v1,0,(v1<1024),(v1+1)):
        with for_(v4,0.39799999999999996,(v4<2.189),(v4+0.39799999999999996)):
            align()
            play("8015364393562791533"*amp(v4), "D1/drive")
            wait(11, "D1/acquisition")
            measure("5126245981370379969", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            r1 = declare_stream()
            save(v2, r1)
            r2 = declare_stream()
            save(v3, r2)
            wait(12500, )
    with stream_processing():
        r1.buffer(5).average().save("5126245981370379969_D1|acquisition_I")
        r2.buffer(5).average().save("5126245981370379969_D1|acquisition_Q")


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
            "intermediate_frequency": -312366349.1484003,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "5126245981370379969": "5126245981370379969_D1/acquisition",
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
                "-2948274449737909540": "-2948274449737909540",
                "8015364393562791533": "8015364393562791533",
            },
        },
    },
    "pulses": {
        "5126245981370379969_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6728385057935643481_i",
                "Q": "6728385057935643481_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "-2948274449737909540": {
            "length": 40,
            "waveforms": {
                "I": "-2948274449737909540_i",
                "Q": "-2948274449737909540_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8015364393562791533": {
            "length": 40,
            "waveforms": {
                "I": "8015364393562791533_i",
                "Q": "8015364393562791533_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6728385057935643481_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "6728385057935643481_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2948274449737909540_i": {
            "samples": [0.002124816438085273, 0.002859253041924886, 0.003787894851291235, 0.004940346233850168, 0.006343530131501176, 0.00801897346311061, 0.009979773718483872, 0.012227474360626477, 0.014749149447807123, 0.017515048340035116, 0.02047716609988561, 0.023569073708237673, 0.02670725941270753, 0.029794100871044445, 0.03272241825550056, 0.03538137021737297, 0.03766327254531491, 0.0394707707339901, 0.040723707493702806] + [0.04136501257188307] * 2 + [0.040723707493702806, 0.0394707707339901, 0.03766327254531491, 0.03538137021737297, 0.03272241825550056, 0.029794100871044445, 0.02670725941270753, 0.023569073708237673, 0.02047716609988561, 0.017515048340035116, 0.014749149447807123, 0.012227474360626477, 0.009979773718483872, 0.00801897346311061, 0.006343530131501176, 0.004940346233850168, 0.003787894851291235, 0.002859253041924886, 0.002124816438085273],
            "type": "arbitrary",
        },
        "-2948274449737909540_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "8015364393562791533_i": {
            "samples": [0.0006440609343047456, 0.000866678717553259, 0.0011481627557292367, 0.0014974865377217, 0.0019228107755823892, 0.0024306605729528486, 0.0030250059581940773, 0.0037063147760608398, 0.004470668996760533, 0.005309050794261166, 0.006206909215221587, 0.007144108715058693, 0.00809533573900999, 0.009030999619462007, 0.009918612684180752, 0.010724577403833514, 0.011416253220616459, 0.011964130651949453, 0.01234391292660679] + [0.012538301270194417] * 2 + [0.01234391292660679, 0.011964130651949453, 0.011416253220616459, 0.010724577403833514, 0.009918612684180752, 0.009030999619462007, 0.00809533573900999, 0.007144108715058693, 0.006206909215221587, 0.005309050794261166, 0.004470668996760533, 0.0037063147760608398, 0.0030250059581940773, 0.0024306605729528486, 0.0019228107755823892, 0.0014974865377217, 0.0011481627557292367, 0.000866678717553259, 0.0006440609343047456],
            "type": "arbitrary",
        },
        "8015364393562791533_q": {
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
            "intermediate_frequency": -312366349.1484003,
            "operations": {
                "5126245981370379969": "5126245981370379969_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_9bb",
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
                "-2948274449737909540": "-2948274449737909540",
                "8015364393562791533": "8015364393562791533",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_6e6",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "5126245981370379969_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6728385057935643481_i",
                "Q": "6728385057935643481_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "-2948274449737909540": {
            "length": 40,
            "waveforms": {
                "I": "-2948274449737909540_i",
                "Q": "-2948274449737909540_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8015364393562791533": {
            "length": 40,
            "waveforms": {
                "I": "8015364393562791533_i",
                "Q": "8015364393562791533_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6728385057935643481_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "6728385057935643481_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2948274449737909540_i": {
            "samples": [0.002124816438085273, 0.002859253041924886, 0.003787894851291235, 0.004940346233850168, 0.006343530131501176, 0.00801897346311061, 0.009979773718483872, 0.012227474360626477, 0.014749149447807123, 0.017515048340035116, 0.02047716609988561, 0.023569073708237673, 0.02670725941270753, 0.029794100871044445, 0.03272241825550056, 0.03538137021737297, 0.03766327254531491, 0.0394707707339901, 0.040723707493702806] + [0.04136501257188307] * 2 + [0.040723707493702806, 0.0394707707339901, 0.03766327254531491, 0.03538137021737297, 0.03272241825550056, 0.029794100871044445, 0.02670725941270753, 0.023569073708237673, 0.02047716609988561, 0.017515048340035116, 0.014749149447807123, 0.012227474360626477, 0.009979773718483872, 0.00801897346311061, 0.006343530131501176, 0.004940346233850168, 0.003787894851291235, 0.002859253041924886, 0.002124816438085273],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2948274449737909540_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8015364393562791533_i": {
            "samples": [0.0006440609343047456, 0.000866678717553259, 0.0011481627557292367, 0.0014974865377217, 0.0019228107755823892, 0.0024306605729528486, 0.0030250059581940773, 0.0037063147760608398, 0.004470668996760533, 0.005309050794261166, 0.006206909215221587, 0.007144108715058693, 0.00809533573900999, 0.009030999619462007, 0.009918612684180752, 0.010724577403833514, 0.011416253220616459, 0.011964130651949453, 0.01234391292660679] + [0.012538301270194417] * 2 + [0.01234391292660679, 0.011964130651949453, 0.011416253220616459, 0.010724577403833514, 0.009918612684180752, 0.009030999619462007, 0.00809533573900999, 0.007144108715058693, 0.006206909215221587, 0.005309050794261166, 0.004470668996760533, 0.0037063147760608398, 0.0030250059581940773, 0.0024306605729528486, 0.0019228107755823892, 0.0014974865377217, 0.0011481627557292367, 0.000866678717553259, 0.0006440609343047456],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8015364393562791533_q": {
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
        "D1/acquisition_mixer_9bb": [{'intermediate_frequency': -312366349.1484003, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_6e6": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

