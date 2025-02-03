
# Single QUA script generated at 2025-02-03 10:05:16.327768
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    v11 = declare(fixed, )
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
    wait((4+(0*(Cast.to_int(v4)+Cast.to_int(v5)))), "B2/acquisition")
    wait((4+(0*(Cast.to_int(v6)+Cast.to_int(v7)))), "B3/acquisition")
    wait((4+(0*(Cast.to_int(v8)+Cast.to_int(v9)))), "B4/acquisition")
    wait((4+(0*(Cast.to_int(v10)+Cast.to_int(v11)))), "B5/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("1507396612219249840", "B1/drive")
        play("155077234215310193", "B2/drive")
        play("-6123160305497342597", "B3/drive")
        play("6172742878408295207", "B4/drive")
        play("4927193752293246976", "B5/drive")
        wait(11, "B5/acquisition")
        wait(11, "B2/acquisition")
        wait(11, "B1/acquisition")
        wait(11, "B4/acquisition")
        wait(11, "B3/acquisition")
        measure("8666640406112859505", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        measure("2450534381141969154", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v4), dual_demod.full("minus_sin", "out1", "cos", "out2", v5))
        r3 = declare_stream()
        save(v4, r3)
        r4 = declare_stream()
        save(v5, r4)
        measure("-6551638849736001630", "B3/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v6), dual_demod.full("minus_sin", "out1", "cos", "out2", v7))
        r5 = declare_stream()
        save(v6, r5)
        r6 = declare_stream()
        save(v7, r6)
        measure("-8073703712039372315", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v8), dual_demod.full("minus_sin", "out1", "cos", "out2", v9))
        r7 = declare_stream()
        save(v8, r7)
        r8 = declare_stream()
        save(v9, r8)
        measure("6777153843555164598", "B5/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v10), dual_demod.full("minus_sin", "out1", "cos", "out2", v11))
        r9 = declare_stream()
        save(v10, r9)
        r10 = declare_stream()
        save(v11, r10)
        wait(25000, )
    with stream_processing():
        r1.buffer(5000).save("8666640406112859505_B1|acquisition_I")
        r2.buffer(5000).save("8666640406112859505_B1|acquisition_Q")
        r3.buffer(5000).save("2450534381141969154_B2|acquisition_I")
        r4.buffer(5000).save("2450534381141969154_B2|acquisition_Q")
        r5.buffer(5000).save("-6551638849736001630_B3|acquisition_I")
        r6.buffer(5000).save("-6551638849736001630_B3|acquisition_Q")
        r7.buffer(5000).save("-8073703712039372315_B4|acquisition_I")
        r8.buffer(5000).save("-8073703712039372315_B4|acquisition_Q")
        r9.buffer(5000).save("6777153843555164598_B5|acquisition_I")
        r10.buffer(5000).save("6777153843555164598_B5|acquisition_Q")


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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "1": {},
                "3": {},
                "7": {},
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
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": 0.0,
                    "filter": {},
                },
                "5": {
                    "offset": 0.0,
                    "filter": {},
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "1": {},
                "5": {},
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
                "2": {
                    "LO_frequency": 4900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
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
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 5800000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "3": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
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
        "B5/acquisition": {
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
            "intermediate_frequency": 270679567.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "6777153843555164598": "6777153843555164598_B5/acquisition",
            },
        },
        "B2/acquisition": {
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
            "intermediate_frequency": 10073372.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "2450534381141969154": "2450534381141969154_B2/acquisition",
            },
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
                "8666640406112859505": "8666640406112859505_B1/acquisition",
            },
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
                "-8073703712039372315": "-8073703712039372315_B4/acquisition",
            },
        },
        "B3/acquisition": {
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
            "intermediate_frequency": 110355638.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-6551638849736001630": "-6551638849736001630_B3/acquisition",
            },
        },
        "B3/drive": {
            "RF_inputs": {
                "port": ('octave3', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -115416853.0,
            "operations": {
                "-6123160305497342597": "-6123160305497342597",
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
                "1507396612219249840": "1507396612219249840",
            },
        },
        "B5/drive": {
            "RF_inputs": {
                "port": ('octave3', 3),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 5),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -157953677.0,
            "operations": {
                "4927193752293246976": "4927193752293246976",
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
                "6172742878408295207": "6172742878408295207",
            },
        },
        "B2/drive": {
            "RF_inputs": {
                "port": ('octave2', 4),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 7),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 63748730.0,
            "operations": {
                "155077234215310193": "155077234215310193",
            },
        },
    },
    "pulses": {
        "8666640406112859505_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8001049185993685102_i",
                "Q": "8001049185993685102_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "2450534381141969154_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6656077189817625125_i",
                "Q": "-6656077189817625125_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6551638849736001630_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7524533205460310076_i",
                "Q": "-7524533205460310076_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-8073703712039372315_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5006741218331628322_i",
                "Q": "-5006741218331628322_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6777153843555164598_B5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1652249289170353816_i",
                "Q": "-1652249289170353816_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
        },
        "1507396612219249840": {
            "length": 40,
            "waveforms": {
                "I": "1507396612219249840_i",
                "Q": "1507396612219249840_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "155077234215310193": {
            "length": 40,
            "waveforms": {
                "I": "155077234215310193_i",
                "Q": "155077234215310193_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6123160305497342597": {
            "length": 40,
            "waveforms": {
                "I": "-6123160305497342597_i",
                "Q": "-6123160305497342597_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6172742878408295207": {
            "length": 40,
            "waveforms": {
                "I": "6172742878408295207_i",
                "Q": "6172742878408295207_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927193752293246976": {
            "length": 40,
            "waveforms": {
                "I": "4927193752293246976_i",
                "Q": "4927193752293246976_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8001049185993685102_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "8001049185993685102_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6656077189817625125_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-6656077189817625125_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7524533205460310076_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-7524533205460310076_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5006741218331628322_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5006741218331628322_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1652249289170353816_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "-1652249289170353816_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1507396612219249840_i": {
            "samples": [0.002242572339184566, 0.0030177109267510043, 0.00399781744200929, 0.005214136906814727, 0.006695084314439711, 0.008463379591148108, 0.010532846080841015, 0.012905112784207933, 0.015566537412501021, 0.01848572056522605, 0.021611996903540733, 0.024875255956662935, 0.02818735780693396, 0.031445269947406915, 0.034535872716205264, 0.037342182011463214, 0.03975054583510476, 0.041658214360439524, 0.042980588034567925] + [0.04365743380982069] * 2 + [0.042980588034567925, 0.041658214360439524, 0.03975054583510476, 0.037342182011463214, 0.034535872716205264, 0.031445269947406915, 0.02818735780693396, 0.024875255956662935, 0.021611996903540733, 0.01848572056522605, 0.015566537412501021, 0.012905112784207933, 0.010532846080841015, 0.008463379591148108, 0.006695084314439711, 0.005214136906814727, 0.00399781744200929, 0.0030177109267510043, 0.002242572339184566],
            "type": "arbitrary",
        },
        "1507396612219249840_q": {
            "samples": [0.00044413444373694335, 0.0005669995920965754, 0.00071054958441962, 0.0008737752863373117, 0.001053952726062189, 0.0012463648851026706, 0.0014441519431153107, 0.0016383443964326477, 0.0018181229243507055, 0.0019713287946510594, 0.002085220013740063, 0.0021474342056337927, 0.0021470838954500476, 0.0020758791488717852, 0.0019291522650067786, 0.0017066544122426549, 0.0014130076839822393, 0.0010577280989955346, 0.0006547823958391207, 0.00022169790606549572, -0.00022169790606549572, -0.0006547823958391207, -0.0010577280989955346, -0.0014130076839822393, -0.0017066544122426549, -0.0019291522650067786, -0.0020758791488717852, -0.0021470838954500476, -0.0021474342056337927, -0.002085220013740063, -0.0019713287946510594, -0.0018181229243507055, -0.0016383443964326477, -0.0014441519431153107, -0.0012463648851026706, -0.001053952726062189, -0.0008737752863373117, -0.00071054958441962, -0.0005669995920965754, -0.00044413444373694335],
            "type": "arbitrary",
        },
        "155077234215310193_i": {
            "samples": [0.0024925986638595224, 0.0033541581212354244, 0.004443537557379336, 0.005795465528587065, 0.007441525040243448, 0.0094069690827911, 0.011707162176667504, 0.014343914941254315, 0.017302064097262527, 0.020546709497949768, 0.024021537082139232, 0.027648619702179723, 0.03132999064495793, 0.03495113022044534, 0.0383863069580789, 0.04150549409755821, 0.04418236848149864, 0.04630272461639384, 0.04777253087221077] + [0.04852483876683479] * 2 + [0.04777253087221077, 0.04630272461639384, 0.04418236848149864, 0.04150549409755821, 0.0383863069580789, 0.03495113022044534, 0.03132999064495793, 0.027648619702179723, 0.024021537082139232, 0.020546709497949768, 0.017302064097262527, 0.014343914941254315, 0.011707162176667504, 0.0094069690827911, 0.007441525040243448, 0.005795465528587065, 0.004443537557379336, 0.0033541581212354244, 0.0024925986638595224],
            "type": "arbitrary",
        },
        "155077234215310193_q": {
            "samples": [-0.0003686717584838361, -0.00047066094428306214, -0.0005898204214332371, -0.0007253125171361231, -0.0008748760884357846, -0.0010345955833487737, -0.0011987767305467458, -0.001359974030730014, -0.0015092064691500395, -0.0016363811983568833, -0.0017309212112055156, -0.0017825646175018695, -0.0017822738283652083, -0.001723167448521017, -0.0016013708640538942, -0.0014166775222197443, -0.0011729241785927561, -0.0008780099894378274, -0.000543528610992501, -0.00018402931372231237, 0.00018402931372231237, 0.000543528610992501, 0.0008780099894378274, 0.0011729241785927561, 0.0014166775222197443, 0.0016013708640538942, 0.001723167448521017, 0.0017822738283652083, 0.0017825646175018695, 0.0017309212112055156, 0.0016363811983568833, 0.0015092064691500395, 0.001359974030730014, 0.0011987767305467458, 0.0010345955833487737, 0.0008748760884357846, 0.0007253125171361231, 0.0005898204214332371, 0.00047066094428306214, 0.0003686717584838361],
            "type": "arbitrary",
        },
        "-6123160305497342597_i": {
            "samples": [0.003273348626656013, 0.0044047720312634575, 0.005835374852693015, 0.007610763579347677, 0.009772413876283787, 0.012353488660092296, 0.0153741650385453, 0.018836820766454373, 0.022721543011418568, 0.026982499947775133, 0.0315457384127116, 0.036308922348104476, 0.04114339919127811, 0.04589877855828698, 0.05040994644884605, 0.054506148170902775, 0.05802149270488183, 0.06080600227828985, 0.06273619198700096] + [0.06372414325625063] * 2 + [0.06273619198700096, 0.06080600227828985, 0.05802149270488183, 0.054506148170902775, 0.05040994644884605, 0.04589877855828698, 0.04114339919127811, 0.036308922348104476, 0.0315457384127116, 0.026982499947775133, 0.022721543011418568, 0.018836820766454373, 0.0153741650385453, 0.012353488660092296, 0.009772413876283787, 0.007610763579347677, 0.005835374852693015, 0.0044047720312634575, 0.003273348626656013],
            "type": "arbitrary",
        },
        "-6123160305497342597_q": {
            "samples": [-0.0006018618660048793, -0.00076836065595798, -0.0009628901896676105, -0.0011840829544294545, -0.0014282476023508514, -0.0016889919393757963, -0.001957019986931616, -0.0022201768619855644, -0.002463800930792215, -0.00267141547697789, -0.002825753386611122, -0.002910061978644852, -0.0029095872612617665, -0.002813095259237756, -0.0026142606104925695, -0.0023127461147467504, -0.0019148153298024515, -0.0014333637401117716, -0.0008873181536451465, -0.0003004304604508088, 0.0003004304604508088, 0.0008873181536451465, 0.0014333637401117716, 0.0019148153298024515, 0.0023127461147467504, 0.0026142606104925695, 0.002813095259237756, 0.0029095872612617665, 0.002910061978644852, 0.002825753386611122, 0.00267141547697789, 0.002463800930792215, 0.0022201768619855644, 0.001957019986931616, 0.0016889919393757963, 0.0014282476023508514, 0.0011840829544294545, 0.0009628901896676105, 0.00076836065595798, 0.0006018618660048793],
            "type": "arbitrary",
        },
        "6172742878408295207_i": {
            "samples": [0.0038083195325510103, 0.005124654070297362, 0.006789063606087789, 0.008854608201775102, 0.011369541985890968, 0.014372447766872354, 0.017886800243690555, 0.021915365773102935, 0.02643497712264198, 0.03139231206580771, 0.0367013311040453, 0.04224297316153096, 0.04786755969093227, 0.05340012166144586, 0.05864856011139604, 0.06341421351609128, 0.0675040789045132, 0.07074366729135062, 0.0729893123501609] + [0.07413872677099383] * 2 + [0.0729893123501609, 0.07074366729135062, 0.0675040789045132, 0.06341421351609128, 0.05864856011139604, 0.05340012166144586, 0.04786755969093227, 0.04224297316153096, 0.0367013311040453, 0.03139231206580771, 0.02643497712264198, 0.021915365773102935, 0.017886800243690555, 0.014372447766872354, 0.011369541985890968, 0.008854608201775102, 0.006789063606087789, 0.005124654070297362, 0.0038083195325510103],
            "type": "arbitrary",
        },
        "6172742878408295207_q": {
            "samples": [-0.0006462252917696181, -0.0008249967594336925, -0.0010338651257147597, -0.001271362078120766, -0.0015335241783551608, -0.001813488061745398, -0.0021012725402403294, -0.0023838267905897615, -0.0026454084654543436, -0.0028683263445601235, -0.003034040549624977, -0.0031245635542594685, -0.0031240538453100888, -0.003020449387736937, -0.002806958575048987, -0.002483219351829067, -0.0020559569646774983, -0.0015390174282253184, -0.0009527226513586174, -0.0003225752833453825, 0.0003225752833453825, 0.0009527226513586174, 0.0015390174282253184, 0.0020559569646774983, 0.002483219351829067, 0.002806958575048987, 0.003020449387736937, 0.0031240538453100888, 0.0031245635542594685, 0.003034040549624977, 0.0028683263445601235, 0.0026454084654543436, 0.0023838267905897615, 0.0021012725402403294, 0.001813488061745398, 0.0015335241783551608, 0.001271362078120766, 0.0010338651257147597, 0.0008249967594336925, 0.0006462252917696181],
            "type": "arbitrary",
        },
        "4927193752293246976_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
        },
        "4927193752293246976_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
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
        "cosine_weights_B5/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B5/acquisition": {
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
        "con3": {
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
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
                "5": {
                    "shareable": False,
                    "inverted": False,
                },
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
        "B5/acquisition": {
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
            "intermediate_frequency": 270679567.0,
            "operations": {
                "6777153843555164598": "6777153843555164598_B5/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B5/acquisition_mixer_717",
                "lo_frequency": 7370000000.0,
            },
        },
        "B2/acquisition": {
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
            "intermediate_frequency": 10073372.0,
            "operations": {
                "2450534381141969154": "2450534381141969154_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_e3c",
                "lo_frequency": 7370000000.0,
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
                "8666640406112859505": "8666640406112859505_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_85c",
                "lo_frequency": 7370000000.0,
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
                "-8073703712039372315": "-8073703712039372315_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_006",
                "lo_frequency": 7370000000.0,
            },
        },
        "B3/acquisition": {
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
            "intermediate_frequency": 110355638.0,
            "operations": {
                "-6551638849736001630": "-6551638849736001630_B3/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B3/acquisition_mixer_7a2",
                "lo_frequency": 7370000000.0,
            },
        },
        "B3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -115416853.0,
            "operations": {
                "-6123160305497342597": "-6123160305497342597",
            },
            "mixInputs": {
                "I": ('con3', 1),
                "Q": ('con3', 2),
                "mixer": "B3/drive_mixer_5a8",
                "lo_frequency": 5800000000.0,
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
                "1507396612219249840": "1507396612219249840",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_ef4",
                "lo_frequency": 4900000000.0,
            },
        },
        "B5/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 5),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -157953677.0,
            "operations": {
                "4927193752293246976": "4927193752293246976",
            },
            "mixInputs": {
                "I": ('con3', 5),
                "Q": ('con3', 6),
                "mixer": "B5/drive_mixer_c32",
                "lo_frequency": 5900000000.0,
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
                "6172742878408295207": "6172742878408295207",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_d42",
                "lo_frequency": 6700000000.0,
            },
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 63748730.0,
            "operations": {
                "155077234215310193": "155077234215310193",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_363",
                "lo_frequency": 5900000000.0,
            },
        },
    },
    "pulses": {
        "8666640406112859505_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8001049185993685102_i",
                "Q": "8001049185993685102_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "2450534381141969154_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6656077189817625125_i",
                "Q": "-6656077189817625125_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-6551638849736001630_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7524533205460310076_i",
                "Q": "-7524533205460310076_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
        },
        "-8073703712039372315_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5006741218331628322_i",
                "Q": "-5006741218331628322_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "6777153843555164598_B5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1652249289170353816_i",
                "Q": "-1652249289170353816_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
            "operation": "measurement",
        },
        "1507396612219249840": {
            "length": 40,
            "waveforms": {
                "I": "1507396612219249840_i",
                "Q": "1507396612219249840_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "155077234215310193": {
            "length": 40,
            "waveforms": {
                "I": "155077234215310193_i",
                "Q": "155077234215310193_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6123160305497342597": {
            "length": 40,
            "waveforms": {
                "I": "-6123160305497342597_i",
                "Q": "-6123160305497342597_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6172742878408295207": {
            "length": 40,
            "waveforms": {
                "I": "6172742878408295207_i",
                "Q": "6172742878408295207_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927193752293246976": {
            "length": 40,
            "waveforms": {
                "I": "4927193752293246976_i",
                "Q": "4927193752293246976_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8001049185993685102_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "8001049185993685102_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6656077189817625125_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-6656077189817625125_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7524533205460310076_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-7524533205460310076_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5006741218331628322_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5006741218331628322_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1652249289170353816_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "-1652249289170353816_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1507396612219249840_i": {
            "samples": [0.002242572339184566, 0.0030177109267510043, 0.00399781744200929, 0.005214136906814727, 0.006695084314439711, 0.008463379591148108, 0.010532846080841015, 0.012905112784207933, 0.015566537412501021, 0.01848572056522605, 0.021611996903540733, 0.024875255956662935, 0.02818735780693396, 0.031445269947406915, 0.034535872716205264, 0.037342182011463214, 0.03975054583510476, 0.041658214360439524, 0.042980588034567925] + [0.04365743380982069] * 2 + [0.042980588034567925, 0.041658214360439524, 0.03975054583510476, 0.037342182011463214, 0.034535872716205264, 0.031445269947406915, 0.02818735780693396, 0.024875255956662935, 0.021611996903540733, 0.01848572056522605, 0.015566537412501021, 0.012905112784207933, 0.010532846080841015, 0.008463379591148108, 0.006695084314439711, 0.005214136906814727, 0.00399781744200929, 0.0030177109267510043, 0.002242572339184566],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1507396612219249840_q": {
            "samples": [0.00044413444373694335, 0.0005669995920965754, 0.00071054958441962, 0.0008737752863373117, 0.001053952726062189, 0.0012463648851026706, 0.0014441519431153107, 0.0016383443964326477, 0.0018181229243507055, 0.0019713287946510594, 0.002085220013740063, 0.0021474342056337927, 0.0021470838954500476, 0.0020758791488717852, 0.0019291522650067786, 0.0017066544122426549, 0.0014130076839822393, 0.0010577280989955346, 0.0006547823958391207, 0.00022169790606549572, -0.00022169790606549572, -0.0006547823958391207, -0.0010577280989955346, -0.0014130076839822393, -0.0017066544122426549, -0.0019291522650067786, -0.0020758791488717852, -0.0021470838954500476, -0.0021474342056337927, -0.002085220013740063, -0.0019713287946510594, -0.0018181229243507055, -0.0016383443964326477, -0.0014441519431153107, -0.0012463648851026706, -0.001053952726062189, -0.0008737752863373117, -0.00071054958441962, -0.0005669995920965754, -0.00044413444373694335],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "155077234215310193_i": {
            "samples": [0.0024925986638595224, 0.0033541581212354244, 0.004443537557379336, 0.005795465528587065, 0.007441525040243448, 0.0094069690827911, 0.011707162176667504, 0.014343914941254315, 0.017302064097262527, 0.020546709497949768, 0.024021537082139232, 0.027648619702179723, 0.03132999064495793, 0.03495113022044534, 0.0383863069580789, 0.04150549409755821, 0.04418236848149864, 0.04630272461639384, 0.04777253087221077] + [0.04852483876683479] * 2 + [0.04777253087221077, 0.04630272461639384, 0.04418236848149864, 0.04150549409755821, 0.0383863069580789, 0.03495113022044534, 0.03132999064495793, 0.027648619702179723, 0.024021537082139232, 0.020546709497949768, 0.017302064097262527, 0.014343914941254315, 0.011707162176667504, 0.0094069690827911, 0.007441525040243448, 0.005795465528587065, 0.004443537557379336, 0.0033541581212354244, 0.0024925986638595224],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "155077234215310193_q": {
            "samples": [-0.0003686717584838361, -0.00047066094428306214, -0.0005898204214332371, -0.0007253125171361231, -0.0008748760884357846, -0.0010345955833487737, -0.0011987767305467458, -0.001359974030730014, -0.0015092064691500395, -0.0016363811983568833, -0.0017309212112055156, -0.0017825646175018695, -0.0017822738283652083, -0.001723167448521017, -0.0016013708640538942, -0.0014166775222197443, -0.0011729241785927561, -0.0008780099894378274, -0.000543528610992501, -0.00018402931372231237, 0.00018402931372231237, 0.000543528610992501, 0.0008780099894378274, 0.0011729241785927561, 0.0014166775222197443, 0.0016013708640538942, 0.001723167448521017, 0.0017822738283652083, 0.0017825646175018695, 0.0017309212112055156, 0.0016363811983568833, 0.0015092064691500395, 0.001359974030730014, 0.0011987767305467458, 0.0010345955833487737, 0.0008748760884357846, 0.0007253125171361231, 0.0005898204214332371, 0.00047066094428306214, 0.0003686717584838361],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6123160305497342597_i": {
            "samples": [0.003273348626656013, 0.0044047720312634575, 0.005835374852693015, 0.007610763579347677, 0.009772413876283787, 0.012353488660092296, 0.0153741650385453, 0.018836820766454373, 0.022721543011418568, 0.026982499947775133, 0.0315457384127116, 0.036308922348104476, 0.04114339919127811, 0.04589877855828698, 0.05040994644884605, 0.054506148170902775, 0.05802149270488183, 0.06080600227828985, 0.06273619198700096] + [0.06372414325625063] * 2 + [0.06273619198700096, 0.06080600227828985, 0.05802149270488183, 0.054506148170902775, 0.05040994644884605, 0.04589877855828698, 0.04114339919127811, 0.036308922348104476, 0.0315457384127116, 0.026982499947775133, 0.022721543011418568, 0.018836820766454373, 0.0153741650385453, 0.012353488660092296, 0.009772413876283787, 0.007610763579347677, 0.005835374852693015, 0.0044047720312634575, 0.003273348626656013],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6123160305497342597_q": {
            "samples": [-0.0006018618660048793, -0.00076836065595798, -0.0009628901896676105, -0.0011840829544294545, -0.0014282476023508514, -0.0016889919393757963, -0.001957019986931616, -0.0022201768619855644, -0.002463800930792215, -0.00267141547697789, -0.002825753386611122, -0.002910061978644852, -0.0029095872612617665, -0.002813095259237756, -0.0026142606104925695, -0.0023127461147467504, -0.0019148153298024515, -0.0014333637401117716, -0.0008873181536451465, -0.0003004304604508088, 0.0003004304604508088, 0.0008873181536451465, 0.0014333637401117716, 0.0019148153298024515, 0.0023127461147467504, 0.0026142606104925695, 0.002813095259237756, 0.0029095872612617665, 0.002910061978644852, 0.002825753386611122, 0.00267141547697789, 0.002463800930792215, 0.0022201768619855644, 0.001957019986931616, 0.0016889919393757963, 0.0014282476023508514, 0.0011840829544294545, 0.0009628901896676105, 0.00076836065595798, 0.0006018618660048793],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6172742878408295207_i": {
            "samples": [0.0038083195325510103, 0.005124654070297362, 0.006789063606087789, 0.008854608201775102, 0.011369541985890968, 0.014372447766872354, 0.017886800243690555, 0.021915365773102935, 0.02643497712264198, 0.03139231206580771, 0.0367013311040453, 0.04224297316153096, 0.04786755969093227, 0.05340012166144586, 0.05864856011139604, 0.06341421351609128, 0.0675040789045132, 0.07074366729135062, 0.0729893123501609] + [0.07413872677099383] * 2 + [0.0729893123501609, 0.07074366729135062, 0.0675040789045132, 0.06341421351609128, 0.05864856011139604, 0.05340012166144586, 0.04786755969093227, 0.04224297316153096, 0.0367013311040453, 0.03139231206580771, 0.02643497712264198, 0.021915365773102935, 0.017886800243690555, 0.014372447766872354, 0.011369541985890968, 0.008854608201775102, 0.006789063606087789, 0.005124654070297362, 0.0038083195325510103],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6172742878408295207_q": {
            "samples": [-0.0006462252917696181, -0.0008249967594336925, -0.0010338651257147597, -0.001271362078120766, -0.0015335241783551608, -0.001813488061745398, -0.0021012725402403294, -0.0023838267905897615, -0.0026454084654543436, -0.0028683263445601235, -0.003034040549624977, -0.0031245635542594685, -0.0031240538453100888, -0.003020449387736937, -0.002806958575048987, -0.002483219351829067, -0.0020559569646774983, -0.0015390174282253184, -0.0009527226513586174, -0.0003225752833453825, 0.0003225752833453825, 0.0009527226513586174, 0.0015390174282253184, 0.0020559569646774983, 0.002483219351829067, 0.002806958575048987, 0.003020449387736937, 0.0031240538453100888, 0.0031245635542594685, 0.003034040549624977, 0.0028683263445601235, 0.0026454084654543436, 0.0023838267905897615, 0.0021012725402403294, 0.001813488061745398, 0.0015335241783551608, 0.001271362078120766, 0.0010338651257147597, 0.0008249967594336925, 0.0006462252917696181],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4927193752293246976_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4927193752293246976_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
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
        "cosine_weights_B5/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B5/acquisition_mixer_717": [{'intermediate_frequency': 270679567.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_e3c": [{'intermediate_frequency': 10073372.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/acquisition_mixer_85c": [{'intermediate_frequency': -237420286.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_006": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/acquisition_mixer_7a2": [{'intermediate_frequency': 110355638.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/drive_mixer_5a8": [{'intermediate_frequency': -115416853.0, 'lo_frequency': 5800000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/drive_mixer_ef4": [{'intermediate_frequency': 100102567.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B5/drive_mixer_c32": [{'intermediate_frequency': -157953677.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_d42": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_363": [{'intermediate_frequency': 63748730.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

