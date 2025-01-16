
# Single QUA script generated at 2025-01-16 15:28:08.326894
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
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
        with for_(v5,0.0,(v5<1.9919939879759516),(v5+0.003987975951903807)):
            align()
            play("9109360731330410398", "B4/drive")
            wait(11, "B4/flux")
            play("-7471724943378752292"*amp(v5), "B4/flux")
            wait(16, "B4/drive")
            play("-8576292713155579349", "B4/drive")
            wait(36, "B4/acquisition")
            measure("1400016999807034203", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
            r1 = declare_stream()
            save(v4, r1)
            wait(25000, )
    with stream_processing():
        r1.buffer(500).average().save("1400016999807034203_B4|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                        "feedforward": [],
                        "feedback": [],
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
    },
    "octaves": {
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
                "-5495384506990519887": "-5495384506990519887",
                "-7471724943378752292": "-7471724943378752292",
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
                "9109360731330410398": "9109360731330410398",
                "-8576292713155579349": "-8576292713155579349",
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
            "intermediate_frequency": 331181947.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1400016999807034203": "1400016999807034203_B4/acquisition",
            },
        },
    },
    "pulses": {
        "9109360731330410398": {
            "length": 40,
            "waveforms": {
                "I": "9109360731330410398_i",
                "Q": "9109360731330410398_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5495384506990519887": {
            "length": 60,
            "waveforms": {
                "single": "-5495384506990519887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1400016999807034203_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8680293469056421257_i",
                "Q": "-8680293469056421257_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-7471724943378752292": {
            "length": 60,
            "waveforms": {
                "single": "-7471724943378752292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8576292713155579349": {
            "length": 40,
            "waveforms": {
                "I": "-8576292713155579349_i",
                "Q": "-8576292713155579349_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "9109360731330410398_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
        },
        "9109360731330410398_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "-5495384506990519887": {
            "sample": 0.125,
            "type": "constant",
        },
        "-8680293469056421257_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-8680293469056421257_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7471724943378752292": {
            "sample": 0.12537688442211056,
            "type": "constant",
        },
        "-8576292713155579349_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "-8576292713155579349_q": {
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                        "feedforward": [],
                        "feedback": [],
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
                "-5495384506990519887": "-5495384506990519887",
                "-7471724943378752292": "-7471724943378752292",
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
                "9109360731330410398": "9109360731330410398",
                "-8576292713155579349": "-8576292713155579349",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_56c",
                "lo_frequency": 6700000000.0,
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
                "1400016999807034203": "1400016999807034203_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_d0c",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "9109360731330410398": {
            "length": 40,
            "waveforms": {
                "I": "9109360731330410398_i",
                "Q": "9109360731330410398_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5495384506990519887": {
            "length": 60,
            "waveforms": {
                "single": "-5495384506990519887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1400016999807034203_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8680293469056421257_i",
                "Q": "-8680293469056421257_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-7471724943378752292": {
            "length": 60,
            "waveforms": {
                "single": "-7471724943378752292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8576292713155579349": {
            "length": 40,
            "waveforms": {
                "I": "-8576292713155579349_i",
                "Q": "-8576292713155579349_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "9109360731330410398_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9109360731330410398_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5495384506990519887": {
            "sample": 0.125,
            "type": "constant",
        },
        "-8680293469056421257_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-8680293469056421257_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7471724943378752292": {
            "sample": 0.12537688442211056,
            "type": "constant",
        },
        "-8576292713155579349_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8576292713155579349_q": {
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
        "B4/drive_mixer_56c": [{'intermediate_frequency': 109610828.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_d0c": [{'intermediate_frequency': 331181947.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

