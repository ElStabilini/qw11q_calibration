
# Single QUA script generated at 2024-11-28 14:18:16.311640
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        play("-1275875444307453744", "D1/drive")
        wait(25000, )


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
                "3": {},
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
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {},
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
                "-1275875444307453744": "-1275875444307453744",
            },
        },
    },
    "pulses": {
        "-1275875444307453744": {
            "length": 40,
            "waveforms": {
                "I": "-1275875444307453744_i",
                "Q": "-1275875444307453744_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1275875444307453744_i": {
            "samples": [0.0010505616076154085, 0.0014136851628513737, 0.0018728285573866342, 0.002442628920118544, 0.0031363976169687413, 0.003964778087100196, 0.004934246052226588, 0.006045564638492511, 0.007292342941779484, 0.008659871512548243, 0.010124415526777958, 0.011653130840443228, 0.013204727185233571, 0.014730937669489142, 0.01617876994520072, 0.01749342131817015, 0.018621650060707682, 0.01951532170632413, 0.020134804515724063] + [0.020451881549687568] * 2 + [0.020134804515724063, 0.01951532170632413, 0.018621650060707682, 0.01749342131817015, 0.01617876994520072, 0.014730937669489142, 0.013204727185233571, 0.011653130840443228, 0.010124415526777958, 0.008659871512548243, 0.007292342941779484, 0.006045564638492511, 0.004934246052226588, 0.003964778087100196, 0.0031363976169687413, 0.002442628920118544, 0.0018728285573866342, 0.0014136851628513737, 0.0010505616076154085],
            "type": "arbitrary",
        },
        "-1275875444307453744_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {},
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
                "-1275875444307453744": "-1275875444307453744",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_04d",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "-1275875444307453744": {
            "length": 40,
            "waveforms": {
                "I": "-1275875444307453744_i",
                "Q": "-1275875444307453744_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1275875444307453744_i": {
            "samples": [0.0010505616076154085, 0.0014136851628513737, 0.0018728285573866342, 0.002442628920118544, 0.0031363976169687413, 0.003964778087100196, 0.004934246052226588, 0.006045564638492511, 0.007292342941779484, 0.008659871512548243, 0.010124415526777958, 0.011653130840443228, 0.013204727185233571, 0.014730937669489142, 0.01617876994520072, 0.01749342131817015, 0.018621650060707682, 0.01951532170632413, 0.020134804515724063] + [0.020451881549687568] * 2 + [0.020134804515724063, 0.01951532170632413, 0.018621650060707682, 0.01749342131817015, 0.01617876994520072, 0.014730937669489142, 0.013204727185233571, 0.011653130840443228, 0.010124415526777958, 0.008659871512548243, 0.007292342941779484, 0.006045564638492511, 0.004934246052226588, 0.003964778087100196, 0.0031363976169687413, 0.002442628920118544, 0.0018728285573866342, 0.0014136851628513737, 0.0010505616076154085],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1275875444307453744_q": {
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
    "integration_weights": {},
    "mixers": {
        "D1/drive_mixer_04d": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

