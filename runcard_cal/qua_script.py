
# Single QUA script generated at 2025-01-20 08:29:26.329136
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
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
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B1/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("-8379386416706536110", "B1/drive")
        wait(11, "B1/acquisition")
        measure("1264514087184868021", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        wait(25000, )
    with stream_processing():
        r1.buffer(5000).save("1264514087184868021_B1|acquisition_I")
        r2.buffer(5000).save("1264514087184868021_B1|acquisition_Q")


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
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
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
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "2": {
                    "LO_frequency": 4900000000.0,
                    "gain": 0.0,
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
            "operations": {},
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
        "B1/acquisition": {
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
            "intermediate_frequency": -237420286.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1264514087184868021": "1264514087184868021_B1/acquisition",
            },
        },
        "B1/drive": {
            "RF_inputs": {
                "port": ('octave2', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 100102567.0,
            "operations": {
                "-8379386416706536110": "-8379386416706536110",
            },
        },
    },
    "pulses": {
        "1264514087184868021_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-801188543633164349_i",
                "Q": "-801188543633164349_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-8379386416706536110": {
            "length": 40,
            "waveforms": {
                "I": "-8379386416706536110_i",
                "Q": "-8379386416706536110_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-801188543633164349_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-801188543633164349_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8379386416706536110_i": {
            "samples": [0.002242572339184566, 0.0030177109267510043, 0.00399781744200929, 0.005214136906814727, 0.006695084314439711, 0.008463379591148108, 0.010532846080841015, 0.012905112784207933, 0.015566537412501021, 0.01848572056522605, 0.021611996903540733, 0.024875255956662935, 0.02818735780693396, 0.031445269947406915, 0.034535872716205264, 0.037342182011463214, 0.03975054583510476, 0.041658214360439524, 0.042980588034567925] + [0.04365743380982069] * 2 + [0.042980588034567925, 0.041658214360439524, 0.03975054583510476, 0.037342182011463214, 0.034535872716205264, 0.031445269947406915, 0.02818735780693396, 0.024875255956662935, 0.021611996903540733, 0.01848572056522605, 0.015566537412501021, 0.012905112784207933, 0.010532846080841015, 0.008463379591148108, 0.006695084314439711, 0.005214136906814727, 0.00399781744200929, 0.0030177109267510043, 0.002242572339184566],
            "type": "arbitrary",
        },
        "-8379386416706536110_q": {
            "samples": [0.00044413444373694335, 0.0005669995920965754, 0.00071054958441962, 0.0008737752863373117, 0.001053952726062189, 0.0012463648851026706, 0.0014441519431153107, 0.0016383443964326477, 0.0018181229243507055, 0.0019713287946510594, 0.002085220013740063, 0.0021474342056337927, 0.0021470838954500476, 0.0020758791488717852, 0.0019291522650067786, 0.0017066544122426549, 0.0014130076839822393, 0.0010577280989955346, 0.0006547823958391207, 0.00022169790606549572, -0.00022169790606549572, -0.0006547823958391207, -0.0010577280989955346, -0.0014130076839822393, -0.0017066544122426549, -0.0019291522650067786, -0.0020758791488717852, -0.0021470838954500476, -0.0021474342056337927, -0.002085220013740063, -0.0019713287946510594, -0.0018181229243507055, -0.0016383443964326477, -0.0014441519431153107, -0.0012463648851026706, -0.001053952726062189, -0.0008737752863373117, -0.00071054958441962, -0.0005669995920965754, -0.00044413444373694335],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B1/acquisition": {
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
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
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
        "B1/acquisition": {
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
            "intermediate_frequency": -237420286.0,
            "operations": {
                "1264514087184868021": "1264514087184868021_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_539",
                "lo_frequency": 7370000000.0,
            },
        },
        "B1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 100102567.0,
            "operations": {
                "-8379386416706536110": "-8379386416706536110",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_47c",
                "lo_frequency": 4900000000.0,
            },
        },
    },
    "pulses": {
        "1264514087184868021_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-801188543633164349_i",
                "Q": "-801188543633164349_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "-8379386416706536110": {
            "length": 40,
            "waveforms": {
                "I": "-8379386416706536110_i",
                "Q": "-8379386416706536110_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-801188543633164349_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-801188543633164349_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8379386416706536110_i": {
            "samples": [0.002242572339184566, 0.0030177109267510043, 0.00399781744200929, 0.005214136906814727, 0.006695084314439711, 0.008463379591148108, 0.010532846080841015, 0.012905112784207933, 0.015566537412501021, 0.01848572056522605, 0.021611996903540733, 0.024875255956662935, 0.02818735780693396, 0.031445269947406915, 0.034535872716205264, 0.037342182011463214, 0.03975054583510476, 0.041658214360439524, 0.042980588034567925] + [0.04365743380982069] * 2 + [0.042980588034567925, 0.041658214360439524, 0.03975054583510476, 0.037342182011463214, 0.034535872716205264, 0.031445269947406915, 0.02818735780693396, 0.024875255956662935, 0.021611996903540733, 0.01848572056522605, 0.015566537412501021, 0.012905112784207933, 0.010532846080841015, 0.008463379591148108, 0.006695084314439711, 0.005214136906814727, 0.00399781744200929, 0.0030177109267510043, 0.002242572339184566],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8379386416706536110_q": {
            "samples": [0.00044413444373694335, 0.0005669995920965754, 0.00071054958441962, 0.0008737752863373117, 0.001053952726062189, 0.0012463648851026706, 0.0014441519431153107, 0.0016383443964326477, 0.0018181229243507055, 0.0019713287946510594, 0.002085220013740063, 0.0021474342056337927, 0.0021470838954500476, 0.0020758791488717852, 0.0019291522650067786, 0.0017066544122426549, 0.0014130076839822393, 0.0010577280989955346, 0.0006547823958391207, 0.00022169790606549572, -0.00022169790606549572, -0.0006547823958391207, -0.0010577280989955346, -0.0014130076839822393, -0.0017066544122426549, -0.0019291522650067786, -0.0020758791488717852, -0.0021470838954500476, -0.0021474342056337927, -0.002085220013740063, -0.0019713287946510594, -0.0018181229243507055, -0.0016383443964326477, -0.0014441519431153107, -0.0012463648851026706, -0.001053952726062189, -0.0008737752863373117, -0.00071054958441962, -0.0005669995920965754, -0.00044413444373694335],
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
        "cosine_weights_B1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B1/acquisition_mixer_539": [{'intermediate_frequency': -237420286.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/drive_mixer_47c": [{'intermediate_frequency': 100102567.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

