
# Single QUA script generated at 2024-11-28 09:12:46.971502
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "D1/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-6469620949598768737", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        play("6974012229421481353", "D1/drive")
        wait(391, "D1/acquisition")
        measure("3063999928834269729", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9832190513468051)-(v3*-0.1824288822217816))>0.0011543927554382514)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25000, )
    with stream_processing():
        r1.buffer(2048).save("3063999928834269729_D1|acquisition_shots")


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
            "intermediate_frequency": -312360584.50398064,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "3063999928834269729": "3063999928834269729_D1/acquisition",
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
                "-6469620949598768737": "-6469620949598768737",
                "6974012229421481353": "6974012229421481353",
            },
        },
    },
    "pulses": {
        "-6469620949598768737": {
            "length": 40,
            "waveforms": {
                "I": "-6469620949598768737_i",
                "Q": "-6469620949598768737_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3063999928834269729_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5250681747155127690_i",
                "Q": "-5250681747155127690_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "6974012229421481353": {
            "length": 40,
            "waveforms": {
                "I": "6974012229421481353_i",
                "Q": "6974012229421481353_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6469620949598768737_i": {
            "samples": [0.0010505616076154085, 0.0014136851628513737, 0.0018728285573866342, 0.002442628920118544, 0.0031363976169687413, 0.003964778087100196, 0.004934246052226588, 0.006045564638492511, 0.007292342941779484, 0.008659871512548243, 0.010124415526777958, 0.011653130840443228, 0.013204727185233571, 0.014730937669489142, 0.01617876994520072, 0.01749342131817015, 0.018621650060707682, 0.01951532170632413, 0.020134804515724063] + [0.020451881549687568] * 2 + [0.020134804515724063, 0.01951532170632413, 0.018621650060707682, 0.01749342131817015, 0.01617876994520072, 0.014730937669489142, 0.013204727185233571, 0.011653130840443228, 0.010124415526777958, 0.008659871512548243, 0.007292342941779484, 0.006045564638492511, 0.004934246052226588, 0.003964778087100196, 0.0031363976169687413, 0.002442628920118544, 0.0018728285573866342, 0.0014136851628513737, 0.0010505616076154085],
            "type": "arbitrary",
        },
        "-6469620949598768737_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-5250681747155127690_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-5250681747155127690_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6974012229421481353_i": {
            "samples": [0.0021335931748216017, 0.002871063432112819, 0.00380354107620685, 0.004960752758152045, 0.0063697326273710435, 0.008052096521516892, 0.010020996030701203, 0.01227798099333595, 0.014810072075977685, 0.01758739575106281, 0.020561748792650696, 0.02366642779085327, 0.02681757604082313, 0.029917167962842932, 0.032857581013683745, 0.035527516004934874, 0.03781884392636874, 0.03963380814150582, 0.04089192026408289] + [0.041535874307951665] * 2 + [0.04089192026408289, 0.03963380814150582, 0.03781884392636874, 0.035527516004934874, 0.032857581013683745, 0.029917167962842932, 0.02681757604082313, 0.02366642779085327, 0.020561748792650696, 0.01758739575106281, 0.014810072075977685, 0.01227798099333595, 0.010020996030701203, 0.008052096521516892, 0.0063697326273710435, 0.004960752758152045, 0.00380354107620685, 0.002871063432112819, 0.0021335931748216017],
            "type": "arbitrary",
        },
        "6974012229421481353_q": {
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
            "intermediate_frequency": -312360584.50398064,
            "operations": {
                "3063999928834269729": "3063999928834269729_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_5f0",
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
                "-6469620949598768737": "-6469620949598768737",
                "6974012229421481353": "6974012229421481353",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_534",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "-6469620949598768737": {
            "length": 40,
            "waveforms": {
                "I": "-6469620949598768737_i",
                "Q": "-6469620949598768737_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3063999928834269729_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5250681747155127690_i",
                "Q": "-5250681747155127690_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "6974012229421481353": {
            "length": 40,
            "waveforms": {
                "I": "6974012229421481353_i",
                "Q": "6974012229421481353_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6469620949598768737_i": {
            "samples": [0.0010505616076154085, 0.0014136851628513737, 0.0018728285573866342, 0.002442628920118544, 0.0031363976169687413, 0.003964778087100196, 0.004934246052226588, 0.006045564638492511, 0.007292342941779484, 0.008659871512548243, 0.010124415526777958, 0.011653130840443228, 0.013204727185233571, 0.014730937669489142, 0.01617876994520072, 0.01749342131817015, 0.018621650060707682, 0.01951532170632413, 0.020134804515724063] + [0.020451881549687568] * 2 + [0.020134804515724063, 0.01951532170632413, 0.018621650060707682, 0.01749342131817015, 0.01617876994520072, 0.014730937669489142, 0.013204727185233571, 0.011653130840443228, 0.010124415526777958, 0.008659871512548243, 0.007292342941779484, 0.006045564638492511, 0.004934246052226588, 0.003964778087100196, 0.0031363976169687413, 0.002442628920118544, 0.0018728285573866342, 0.0014136851628513737, 0.0010505616076154085],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6469620949598768737_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5250681747155127690_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-5250681747155127690_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6974012229421481353_i": {
            "samples": [0.0021335931748216017, 0.002871063432112819, 0.00380354107620685, 0.004960752758152045, 0.0063697326273710435, 0.008052096521516892, 0.010020996030701203, 0.01227798099333595, 0.014810072075977685, 0.01758739575106281, 0.020561748792650696, 0.02366642779085327, 0.02681757604082313, 0.029917167962842932, 0.032857581013683745, 0.035527516004934874, 0.03781884392636874, 0.03963380814150582, 0.04089192026408289] + [0.041535874307951665] * 2 + [0.04089192026408289, 0.03963380814150582, 0.03781884392636874, 0.035527516004934874, 0.032857581013683745, 0.029917167962842932, 0.02681757604082313, 0.02366642779085327, 0.020561748792650696, 0.01758739575106281, 0.014810072075977685, 0.01227798099333595, 0.010020996030701203, 0.008052096521516892, 0.0063697326273710435, 0.004960752758152045, 0.00380354107620685, 0.002871063432112819, 0.0021335931748216017],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6974012229421481353_q": {
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
        "D1/acquisition_mixer_5f0": [{'intermediate_frequency': -312360584.50398064, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_534": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

