
# Single QUA script generated at 2025-01-16 13:35:57.525440
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("B1/flux", "single", 0.0)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", -0.2819)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.0307)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", -0.215)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", 0.074)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("-2495876712483290473", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("-3683483636528736372", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("483469096122360432", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("-6733102705546705039", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("5404024229475802753", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("-8623264463752678999", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("6806830676905174253", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("-7768797683739252343", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("5790388531379201073", "B4/drive")
        wait(11, "B4/flux")
        play("5383240440623005631", "B4/flux")
        wait(36, "B4/drive")
        play("6551479160602762942", "B4/drive")
        wait(56, "B4/acquisition")
        measure("3145045913763548875", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(9).average().save("3145045913763548875_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": -0.2819,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                "-2495876712483290473": "-2495876712483290473",
                "-3683483636528736372": "-3683483636528736372",
                "483469096122360432": "483469096122360432",
                "-6733102705546705039": "-6733102705546705039",
                "5404024229475802753": "5404024229475802753",
                "-8623264463752678999": "-8623264463752678999",
                "6806830676905174253": "6806830676905174253",
                "-7768797683739252343": "-7768797683739252343",
                "5383240440623005631": "5383240440623005631",
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
            "intermediate_frequency": 331181947.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "3145045913763548875": "3145045913763548875_B4/acquisition",
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
            "intermediate_frequency": 109610828.0,
            "operations": {
                "5790388531379201073": "5790388531379201073",
                "6551479160602762942": "6551479160602762942",
            },
        },
    },
    "pulses": {
        "5790388531379201073": {
            "length": 40,
            "waveforms": {
                "I": "5790388531379201073_i",
                "Q": "5790388531379201073_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2819759947859458392": {
            "length": 16,
            "waveforms": {
                "single": "2819759947859458392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3145045913763548875_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4639839693332261731_i",
                "Q": "-4639839693332261731_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6299967408365906614": {
            "length": 16,
            "waveforms": {
                "single": "6299967408365906614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2541101791305568453": {
            "length": 16,
            "waveforms": {
                "single": "2541101791305568453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2881127648079073812": {
            "length": 16,
            "waveforms": {
                "single": "-2881127648079073812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9079765792605373225": {
            "length": 16,
            "waveforms": {
                "single": "9079765792605373225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3615426828842972155": {
            "length": 16,
            "waveforms": {
                "single": "-3615426828842972155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6111778514309644377": {
            "length": 16,
            "waveforms": {
                "single": "6111778514309644377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3607084826925714733": {
            "length": 16,
            "waveforms": {
                "single": "-3607084826925714733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5379475238506312608": {
            "length": 16,
            "waveforms": {
                "single": "-5379475238506312608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8592731363638353818": {
            "length": 16,
            "waveforms": {
                "single": "-8592731363638353818",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-983553819105467332": {
            "length": 16,
            "waveforms": {
                "single": "-983553819105467332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7021322285449085602": {
            "length": 16,
            "waveforms": {
                "single": "7021322285449085602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8260171019355854025": {
            "length": 16,
            "waveforms": {
                "single": "-8260171019355854025",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9203692114884420005": {
            "length": 16,
            "waveforms": {
                "single": "9203692114884420005",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4964789238988757285": {
            "length": 16,
            "waveforms": {
                "single": "-4964789238988757285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5769799950093468227": {
            "length": 16,
            "waveforms": {
                "single": "5769799950093468227",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7931478661092483650": {
            "length": 20,
            "waveforms": {
                "single": "-7931478661092483650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5033068484977701874": {
            "length": 20,
            "waveforms": {
                "single": "5033068484977701874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8302307529682565296": {
            "length": 20,
            "waveforms": {
                "single": "8302307529682565296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2112612246947823681": {
            "length": 20,
            "waveforms": {
                "single": "-2112612246947823681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6160066357068347516": {
            "length": 24,
            "waveforms": {
                "single": "6160066357068347516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9060468647872206534": {
            "length": 24,
            "waveforms": {
                "single": "9060468647872206534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7771838518426283482": {
            "length": 24,
            "waveforms": {
                "single": "-7771838518426283482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7543754440534977295": {
            "length": 24,
            "waveforms": {
                "single": "-7543754440534977295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5235484997126175567": {
            "length": 28,
            "waveforms": {
                "single": "-5235484997126175567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7865178113154847446": {
            "length": 28,
            "waveforms": {
                "single": "-7865178113154847446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4762447451255905991": {
            "length": 28,
            "waveforms": {
                "single": "4762447451255905991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6889530105815379174": {
            "length": 28,
            "waveforms": {
                "single": "-6889530105815379174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-681571873306000513": {
            "length": 32,
            "waveforms": {
                "single": "-681571873306000513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5934026713616119760": {
            "length": 32,
            "waveforms": {
                "single": "5934026713616119760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2495876712483290473": {
            "length": 32,
            "waveforms": {
                "single": "-2495876712483290473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3683483636528736372": {
            "length": 32,
            "waveforms": {
                "single": "-3683483636528736372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "483469096122360432": {
            "length": 36,
            "waveforms": {
                "single": "483469096122360432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6733102705546705039": {
            "length": 36,
            "waveforms": {
                "single": "-6733102705546705039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5404024229475802753": {
            "length": 36,
            "waveforms": {
                "single": "5404024229475802753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8623264463752678999": {
            "length": 36,
            "waveforms": {
                "single": "-8623264463752678999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6806830676905174253": {
            "length": 40,
            "waveforms": {
                "single": "6806830676905174253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7768797683739252343": {
            "length": 40,
            "waveforms": {
                "single": "-7768797683739252343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5383240440623005631": {
            "length": 40,
            "waveforms": {
                "single": "5383240440623005631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6551479160602762942": {
            "length": 40,
            "waveforms": {
                "I": "6551479160602762942_i",
                "Q": "6551479160602762942_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5790388531379201073_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
        },
        "5790388531379201073_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "2819759947859458392": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4639839693332261731_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-4639839693332261731_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6299967408365906614": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2541101791305568453": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-2881127648079073812": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "9079765792605373225": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-3615426828842972155": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "6111778514309644377": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-3607084826925714733": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5379475238506312608": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8592731363638353818": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-983553819105467332": {
            "samples": [0.0] * 10 + [0.15] + [0.0] * 5,
            "type": "arbitrary",
        },
        "7021322285449085602": {
            "samples": [0.0] * 10 + [0.15] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8260171019355854025": {
            "samples": [0.0] * 10 + [0.15] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9203692114884420005": {
            "samples": [0.0] * 10 + [0.15] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4964789238988757285": {
            "samples": [0.0] * 10 + [0.15] * 5 + [0.0],
            "type": "arbitrary",
        },
        "5769799950093468227": {
            "samples": [0.0] * 10 + [0.15] * 6,
            "type": "arbitrary",
        },
        "-7931478661092483650": {
            "samples": [0.0] * 10 + [0.15] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5033068484977701874": {
            "samples": [0.0] * 10 + [0.15] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8302307529682565296": {
            "samples": [0.0] * 10 + [0.15] * 9 + [0.0],
            "type": "arbitrary",
        },
        "-2112612246947823681": {
            "samples": [0.0] * 10 + [0.15] * 10,
            "type": "arbitrary",
        },
        "6160066357068347516": {
            "samples": [0.0] * 10 + [0.15] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9060468647872206534": {
            "samples": [0.0] * 10 + [0.15] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7771838518426283482": {
            "samples": [0.0] * 10 + [0.15] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-7543754440534977295": {
            "samples": [0.0] * 10 + [0.15] * 14,
            "type": "arbitrary",
        },
        "-5235484997126175567": {
            "samples": [0.0] * 10 + [0.15] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7865178113154847446": {
            "samples": [0.0] * 10 + [0.15] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4762447451255905991": {
            "samples": [0.0] * 10 + [0.15] * 17 + [0.0],
            "type": "arbitrary",
        },
        "-6889530105815379174": {
            "samples": [0.0] * 10 + [0.15] * 18,
            "type": "arbitrary",
        },
        "-681571873306000513": {
            "samples": [0.0] * 10 + [0.15] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5934026713616119760": {
            "samples": [0.0] * 10 + [0.15] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2495876712483290473": {
            "samples": [0.0] * 10 + [0.15] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-3683483636528736372": {
            "samples": [0.0] * 10 + [0.15] * 22,
            "type": "arbitrary",
        },
        "483469096122360432": {
            "samples": [0.0] * 10 + [0.15] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6733102705546705039": {
            "samples": [0.0] * 10 + [0.15] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5404024229475802753": {
            "samples": [0.0] * 10 + [0.15] * 25 + [0.0],
            "type": "arbitrary",
        },
        "-8623264463752678999": {
            "samples": [0.0] * 10 + [0.15] * 26,
            "type": "arbitrary",
        },
        "6806830676905174253": {
            "samples": [0.0] * 10 + [0.15] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7768797683739252343": {
            "samples": [0.0] * 10 + [0.15] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5383240440623005631": {
            "samples": [0.0] * 10 + [0.15] * 29 + [0.0],
            "type": "arbitrary",
        },
        "6551479160602762942_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "6551479160602762942_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
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
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": -0.2819,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                "-2495876712483290473": "-2495876712483290473",
                "-3683483636528736372": "-3683483636528736372",
                "483469096122360432": "483469096122360432",
                "-6733102705546705039": "-6733102705546705039",
                "5404024229475802753": "5404024229475802753",
                "-8623264463752678999": "-8623264463752678999",
                "6806830676905174253": "6806830676905174253",
                "-7768797683739252343": "-7768797683739252343",
                "5383240440623005631": "5383240440623005631",
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
            "intermediate_frequency": 331181947.0,
            "operations": {
                "3145045913763548875": "3145045913763548875_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_4b7",
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
            "intermediate_frequency": 109610828.0,
            "operations": {
                "5790388531379201073": "5790388531379201073",
                "6551479160602762942": "6551479160602762942",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_928",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "5790388531379201073": {
            "length": 40,
            "waveforms": {
                "I": "5790388531379201073_i",
                "Q": "5790388531379201073_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2819759947859458392": {
            "length": 16,
            "waveforms": {
                "single": "2819759947859458392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3145045913763548875_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4639839693332261731_i",
                "Q": "-4639839693332261731_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "6299967408365906614": {
            "length": 16,
            "waveforms": {
                "single": "6299967408365906614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2541101791305568453": {
            "length": 16,
            "waveforms": {
                "single": "2541101791305568453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2881127648079073812": {
            "length": 16,
            "waveforms": {
                "single": "-2881127648079073812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9079765792605373225": {
            "length": 16,
            "waveforms": {
                "single": "9079765792605373225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3615426828842972155": {
            "length": 16,
            "waveforms": {
                "single": "-3615426828842972155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6111778514309644377": {
            "length": 16,
            "waveforms": {
                "single": "6111778514309644377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3607084826925714733": {
            "length": 16,
            "waveforms": {
                "single": "-3607084826925714733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5379475238506312608": {
            "length": 16,
            "waveforms": {
                "single": "-5379475238506312608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8592731363638353818": {
            "length": 16,
            "waveforms": {
                "single": "-8592731363638353818",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-983553819105467332": {
            "length": 16,
            "waveforms": {
                "single": "-983553819105467332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7021322285449085602": {
            "length": 16,
            "waveforms": {
                "single": "7021322285449085602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8260171019355854025": {
            "length": 16,
            "waveforms": {
                "single": "-8260171019355854025",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9203692114884420005": {
            "length": 16,
            "waveforms": {
                "single": "9203692114884420005",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4964789238988757285": {
            "length": 16,
            "waveforms": {
                "single": "-4964789238988757285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5769799950093468227": {
            "length": 16,
            "waveforms": {
                "single": "5769799950093468227",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7931478661092483650": {
            "length": 20,
            "waveforms": {
                "single": "-7931478661092483650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5033068484977701874": {
            "length": 20,
            "waveforms": {
                "single": "5033068484977701874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8302307529682565296": {
            "length": 20,
            "waveforms": {
                "single": "8302307529682565296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2112612246947823681": {
            "length": 20,
            "waveforms": {
                "single": "-2112612246947823681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6160066357068347516": {
            "length": 24,
            "waveforms": {
                "single": "6160066357068347516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9060468647872206534": {
            "length": 24,
            "waveforms": {
                "single": "9060468647872206534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7771838518426283482": {
            "length": 24,
            "waveforms": {
                "single": "-7771838518426283482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7543754440534977295": {
            "length": 24,
            "waveforms": {
                "single": "-7543754440534977295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5235484997126175567": {
            "length": 28,
            "waveforms": {
                "single": "-5235484997126175567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7865178113154847446": {
            "length": 28,
            "waveforms": {
                "single": "-7865178113154847446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4762447451255905991": {
            "length": 28,
            "waveforms": {
                "single": "4762447451255905991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6889530105815379174": {
            "length": 28,
            "waveforms": {
                "single": "-6889530105815379174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-681571873306000513": {
            "length": 32,
            "waveforms": {
                "single": "-681571873306000513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5934026713616119760": {
            "length": 32,
            "waveforms": {
                "single": "5934026713616119760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2495876712483290473": {
            "length": 32,
            "waveforms": {
                "single": "-2495876712483290473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3683483636528736372": {
            "length": 32,
            "waveforms": {
                "single": "-3683483636528736372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "483469096122360432": {
            "length": 36,
            "waveforms": {
                "single": "483469096122360432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6733102705546705039": {
            "length": 36,
            "waveforms": {
                "single": "-6733102705546705039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5404024229475802753": {
            "length": 36,
            "waveforms": {
                "single": "5404024229475802753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8623264463752678999": {
            "length": 36,
            "waveforms": {
                "single": "-8623264463752678999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6806830676905174253": {
            "length": 40,
            "waveforms": {
                "single": "6806830676905174253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7768797683739252343": {
            "length": 40,
            "waveforms": {
                "single": "-7768797683739252343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5383240440623005631": {
            "length": 40,
            "waveforms": {
                "single": "5383240440623005631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6551479160602762942": {
            "length": 40,
            "waveforms": {
                "I": "6551479160602762942_i",
                "Q": "6551479160602762942_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5790388531379201073_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5790388531379201073_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2819759947859458392": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4639839693332261731_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-4639839693332261731_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6299967408365906614": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2541101791305568453": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2881127648079073812": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9079765792605373225": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3615426828842972155": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6111778514309644377": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3607084826925714733": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5379475238506312608": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8592731363638353818": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-983553819105467332": {
            "samples": [0.0] * 10 + [0.15] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7021322285449085602": {
            "samples": [0.0] * 10 + [0.15] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8260171019355854025": {
            "samples": [0.0] * 10 + [0.15] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9203692114884420005": {
            "samples": [0.0] * 10 + [0.15] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4964789238988757285": {
            "samples": [0.0] * 10 + [0.15] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5769799950093468227": {
            "samples": [0.0] * 10 + [0.15] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7931478661092483650": {
            "samples": [0.0] * 10 + [0.15] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5033068484977701874": {
            "samples": [0.0] * 10 + [0.15] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8302307529682565296": {
            "samples": [0.0] * 10 + [0.15] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2112612246947823681": {
            "samples": [0.0] * 10 + [0.15] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6160066357068347516": {
            "samples": [0.0] * 10 + [0.15] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9060468647872206534": {
            "samples": [0.0] * 10 + [0.15] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7771838518426283482": {
            "samples": [0.0] * 10 + [0.15] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7543754440534977295": {
            "samples": [0.0] * 10 + [0.15] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5235484997126175567": {
            "samples": [0.0] * 10 + [0.15] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7865178113154847446": {
            "samples": [0.0] * 10 + [0.15] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4762447451255905991": {
            "samples": [0.0] * 10 + [0.15] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6889530105815379174": {
            "samples": [0.0] * 10 + [0.15] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-681571873306000513": {
            "samples": [0.0] * 10 + [0.15] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5934026713616119760": {
            "samples": [0.0] * 10 + [0.15] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2495876712483290473": {
            "samples": [0.0] * 10 + [0.15] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3683483636528736372": {
            "samples": [0.0] * 10 + [0.15] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "483469096122360432": {
            "samples": [0.0] * 10 + [0.15] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6733102705546705039": {
            "samples": [0.0] * 10 + [0.15] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5404024229475802753": {
            "samples": [0.0] * 10 + [0.15] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8623264463752678999": {
            "samples": [0.0] * 10 + [0.15] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6806830676905174253": {
            "samples": [0.0] * 10 + [0.15] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7768797683739252343": {
            "samples": [0.0] * 10 + [0.15] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5383240440623005631": {
            "samples": [0.0] * 10 + [0.15] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6551479160602762942_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6551479160602762942_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
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
        "B4/acquisition_mixer_4b7": [{'intermediate_frequency': 331181947.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_928": [{'intermediate_frequency': 109610828.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

