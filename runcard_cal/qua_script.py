
# Single QUA script generated at 2025-02-16 10:28:13.375118
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(int, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(int, )
    v11 = declare(fixed, )
    v12 = declare(fixed, )
    v13 = declare(int, )
    set_dc_offset("B1/flux", "single", -0.25498290735703955)
    set_dc_offset("D1/flux", "single", -0.4530870218982913)
    set_dc_offset("B2/flux", "single", 0.10729465913983083)
    set_dc_offset("D2/flux", "single", -0.2224873138863394)
    set_dc_offset("B3/flux", "single", 0.2226188560782865)
    set_dc_offset("D3/flux", "single", 0.05128942239382605)
    set_dc_offset("B4/flux", "single", 0.114743772754262)
    set_dc_offset("D4/flux", "single", -0.08416990010352905)
    set_dc_offset("B5/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", 0.05418914676504196)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B1/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v8)+Cast.to_int(v9))+Cast.to_int(v10)))), "B3/acquisition")
    wait((4+(0*((Cast.to_int(v11)+Cast.to_int(v12))+Cast.to_int(v13)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-8409682919003668174", "B1/drive")
        wait(11, "B1/flux")
        play("3248877355460422803", "B1/flux")
        wait(46, "B1/drive")
        play("-7648592289780106305", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3211167734745208851", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        r1 = declare_stream()
        save(v4, r1)
        play("-5326538865720618437", "B2/drive")
        wait(11, "B2/flux")
        play("3248877355460422803", "B2/flux")
        wait(46, "B2/drive")
        play("-4565448236497056568", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1283717487460058200", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        r2 = declare_stream()
        save(v7, r2)
        play("-2412668905301419931", "B3/drive")
        wait(11, "B3/flux")
        play("3248877355460422803", "B3/flux")
        wait(46, "B3/drive")
        play("-4299250181728346759", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-112377154948369288", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        r3 = declare_stream()
        save(v10, r3)
        play("8449304757042618870", "B4/drive")
        wait(11, "B4/flux")
        play("3248877355460422803", "B4/flux")
        wait(46, "B4/drive")
        play("2164366097631323914", "B4/drive")
        wait(66, "B4/acquisition")
        measure("3903936994315933848", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25001, "B4/acquisition")
        play("-8409682919003668174", "B1/drive")
        wait(11, "B1/flux")
        play("-3703331837213747901", "B1/flux")
        wait(46, "B1/drive")
        play("-7648592289780106305", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3211167734745208851", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        save(v4, r1)
        play("-5326538865720618437", "B2/drive")
        wait(11, "B2/flux")
        play("-3703331837213747901", "B2/flux")
        wait(46, "B2/drive")
        play("-4565448236497056568", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1283717487460058200", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        save(v7, r2)
        play("-2412668905301419931", "B3/drive")
        wait(11, "B3/flux")
        play("-3703331837213747901", "B3/flux")
        wait(46, "B3/drive")
        play("-4299250181728346759", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-112377154948369288", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        save(v10, r3)
        play("8449304757042618870", "B4/drive")
        wait(11, "B4/flux")
        play("-3703331837213747901", "B4/flux")
        wait(46, "B4/drive")
        play("2164366097631323914", "B4/drive")
        wait(66, "B4/acquisition")
        measure("3903936994315933848", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-3211167734745208851_B1|acquisition_shots")
        r2.buffer(2).average().save("1283717487460058200_B2|acquisition_shots")
        r3.buffer(2).average().save("-112377154948369288_B3|acquisition_shots")
        r4.buffer(2).average().save("3903936994315933848_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.25498290735703955,
                    "filter": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.0,
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
                    "offset": -0.4530870218982913,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "filter": {},
                },
                "7": {
                    "offset": 0.05418914676504196,
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
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
                    "offset": 0.0,
                    "filter": {},
                },
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
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
                "3": {},
                "1": {},
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
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "7": {},
                "1": {},
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
                "2": {
                    "LO_frequency": 4900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
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
                    "output_mode": "triggered",
                },
                "1": {
                    "LO_frequency": 5800000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
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
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
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
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
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
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
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
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
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
            "intermediate_frequency": 100388701.0,
            "operations": {
                "-8409682919003668174": "-8409682919003668174",
                "-7648592289780106305": "-7648592289780106305",
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
            "intermediate_frequency": 109615374.0,
            "operations": {
                "8449304757042618870": "8449304757042618870",
                "2164366097631323914": "2164366097631323914",
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
            "intermediate_frequency": 110622376.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-112377154948369288": "-112377154948369288_B3/acquisition",
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
            "intermediate_frequency": 63761228.0,
            "operations": {
                "-5326538865720618437": "-5326538865720618437",
                "-4565448236497056568": "-4565448236497056568",
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
            "intermediate_frequency": 10040944.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1283717487460058200": "1283717487460058200_B2/acquisition",
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
            "intermediate_frequency": -237451236.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-3211167734745208851": "-3211167734745208851_B1/acquisition",
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
            "intermediate_frequency": -115376210.0,
            "operations": {
                "-2412668905301419931": "-2412668905301419931",
                "-4299250181728346759": "-4299250181728346759",
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
            "intermediate_frequency": 330300527.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "3903936994315933848": "3903936994315933848_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-8409682919003668174": {
            "length": 40,
            "waveforms": {
                "I": "-8409682919003668174_i",
                "Q": "-8409682919003668174_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6372067490193647110": {
            "length": 16,
            "waveforms": {
                "single": "6372067490193647110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3211167734745208851_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "9137289095690292990_i",
                "Q": "9137289095690292990_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-5326538865720618437": {
            "length": 40,
            "waveforms": {
                "I": "-5326538865720618437_i",
                "Q": "-5326538865720618437_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1283717487460058200_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1121479897136649109_i",
                "Q": "-1121479897136649109_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-2412668905301419931": {
            "length": 40,
            "waveforms": {
                "I": "-2412668905301419931_i",
                "Q": "-2412668905301419931_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-112377154948369288_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5056093375855522765_i",
                "Q": "5056093375855522765_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "8449304757042618870": {
            "length": 40,
            "waveforms": {
                "I": "8449304757042618870_i",
                "Q": "8449304757042618870_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3903936994315933848_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1556605665873615992_i",
                "Q": "-1556605665873615992_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6593561549392362358": {
            "length": 16,
            "waveforms": {
                "single": "6593561549392362358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4146341697704914941": {
            "length": 16,
            "waveforms": {
                "single": "-4146341697704914941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3924847638506199693": {
            "length": 16,
            "waveforms": {
                "single": "-3924847638506199693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4643707078485973297": {
            "length": 16,
            "waveforms": {
                "single": "-4643707078485973297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4422213019287258049": {
            "length": 16,
            "waveforms": {
                "single": "-4422213019287258049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1505593891304317582": {
            "length": 16,
            "waveforms": {
                "single": "-1505593891304317582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3506121866523731516": {
            "length": 16,
            "waveforms": {
                "single": "3506121866523731516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3727615925722446764": {
            "length": 16,
            "waveforms": {
                "single": "3727615925722446764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7407113868727041288": {
            "length": 16,
            "waveforms": {
                "single": "7407113868727041288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5925375613725613627": {
            "length": 16,
            "waveforms": {
                "single": "5925375613725613627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4777553796548744854": {
            "length": 16,
            "waveforms": {
                "single": "4777553796548744854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7288158642957173643": {
            "length": 16,
            "waveforms": {
                "single": "-7288158642957173643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8806219761990083753": {
            "length": 16,
            "waveforms": {
                "single": "8806219761990083753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8013548144320830920": {
            "length": 16,
            "waveforms": {
                "single": "8013548144320830920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7442764623716301000": {
            "length": 16,
            "waveforms": {
                "single": "-7442764623716301000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5383988072142534486": {
            "length": 20,
            "waveforms": {
                "single": "5383988072142534486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3460584780577335435": {
            "length": 20,
            "waveforms": {
                "single": "3460584780577335435",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1988060747490821406": {
            "length": 20,
            "waveforms": {
                "single": "-1988060747490821406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7803241819344416597": {
            "length": 20,
            "waveforms": {
                "single": "7803241819344416597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "209698940512345457": {
            "length": 24,
            "waveforms": {
                "single": "209698940512345457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3156832405117916844": {
            "length": 24,
            "waveforms": {
                "single": "-3156832405117916844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2935338345919201596": {
            "length": 24,
            "waveforms": {
                "single": "-2935338345919201596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3212532749335203810": {
            "length": 24,
            "waveforms": {
                "single": "-3212532749335203810",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "594639156907419841": {
            "length": 28,
            "waveforms": {
                "single": "594639156907419841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "816133216106135089": {
            "length": 28,
            "waveforms": {
                "single": "816133216106135089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4495631159110729613": {
            "length": 28,
            "waveforms": {
                "single": "4495631159110729613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3013892904109301952": {
            "length": 28,
            "waveforms": {
                "single": "3013892904109301952",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1866071086932433179": {
            "length": 32,
            "waveforms": {
                "single": "1866071086932433179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5801283969589117190": {
            "length": 32,
            "waveforms": {
                "single": "-5801283969589117190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5677323582483482002": {
            "length": 32,
            "waveforms": {
                "single": "-5677323582483482002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4285324834134315290": {
            "length": 32,
            "waveforms": {
                "single": "4285324834134315290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7780387605371603207": {
            "length": 36,
            "waveforms": {
                "single": "-7780387605371603207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2472505362526222811": {
            "length": 36,
            "waveforms": {
                "single": "2472505362526222811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1851179594639529267": {
            "length": 36,
            "waveforms": {
                "single": "1851179594639529267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4670265050529389674": {
            "length": 36,
            "waveforms": {
                "single": "4670265050529389674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6508955675346589869": {
            "length": 40,
            "waveforms": {
                "single": "-6508955675346589869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2701783769103966218": {
            "length": 40,
            "waveforms": {
                "single": "-2701783769103966218",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8321775146954682348": {
            "length": 40,
            "waveforms": {
                "single": "-8321775146954682348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-116245857727690569": {
            "length": 40,
            "waveforms": {
                "single": "-116245857727690569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6124015458951515485": {
            "length": 44,
            "waveforms": {
                "single": "-6124015458951515485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5902521399752800237": {
            "length": 44,
            "waveforms": {
                "single": "-5902521399752800237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3507551741059616989": {
            "length": 44,
            "waveforms": {
                "single": "3507551741059616989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1584148449494417938": {
            "length": 44,
            "waveforms": {
                "single": "1584148449494417938",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "102410194492990277": {
            "length": 48,
            "waveforms": {
                "single": "102410194492990277",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1528448105277130972": {
            "length": 48,
            "waveforms": {
                "single": "1528448105277130972",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8712766679205428865": {
            "length": 48,
            "waveforms": {
                "single": "-8712766679205428865",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7286728768421288170": {
            "length": 48,
            "waveforms": {
                "single": "-7286728768421288170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1373842124518003615": {
            "length": 52,
            "waveforms": {
                "single": "1373842124518003615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5088969080418121307": {
            "length": 52,
            "waveforms": {
                "single": "-5088969080418121307",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6607051941544767961": {
            "length": 52,
            "waveforms": {
                "single": "6607051941544767961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1060303114976782408": {
            "length": 52,
            "waveforms": {
                "single": "-1060303114976782408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8804811629547934824": {
            "length": 56,
            "waveforms": {
                "single": "8804811629547934824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9026305688746650072": {
            "length": 56,
            "waveforms": {
                "single": "9026305688746650072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7056394532785341143": {
            "length": 56,
            "waveforms": {
                "single": "-7056394532785341143",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6834900473586625895": {
            "length": 56,
            "waveforms": {
                "single": "-6834900473586625895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5604073998899100805": {
            "length": 60,
            "waveforms": {
                "single": "5604073998899100805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9035498168567827160": {
            "length": 60,
            "waveforms": {
                "single": "-9035498168567827160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4415646726384743784": {
            "length": 60,
            "waveforms": {
                "single": "-4415646726384743784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "596069031443305314": {
            "length": 60,
            "waveforms": {
                "single": "596069031443305314",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6616244421365945049": {
            "length": 64,
            "waveforms": {
                "single": "-6616244421365945049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2793828719446472177": {
            "length": 64,
            "waveforms": {
                "single": "2793828719446472177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3015322778645187425": {
            "length": 64,
            "waveforms": {
                "single": "3015322778645187425",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2004360372225874247": {
            "length": 64,
            "waveforms": {
                "single": "-2004360372225874247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8248532595671951771": {
            "length": 68,
            "waveforms": {
                "single": "8248532595671951771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6766794340670524110": {
            "length": 68,
            "waveforms": {
                "single": "6766794340670524110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8000451790034432982": {
            "length": 68,
            "waveforms": {
                "single": "-8000451790034432982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7778957730835717734": {
            "length": 68,
            "waveforms": {
                "single": "-7778957730835717734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2473935237062108284": {
            "length": 72,
            "waveforms": {
                "single": "2473935237062108284",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5581198042832550871": {
            "length": 72,
            "waveforms": {
                "single": "-5581198042832550871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1774026136589927220": {
            "length": 72,
            "waveforms": {
                "single": "-1774026136589927220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-347988225805786525": {
            "length": 72,
            "waveforms": {
                "single": "-347988225805786525",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2700353894568080745": {
            "length": 76,
            "waveforms": {
                "single": "-2700353894568080745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2692591289282789130": {
            "length": 76,
            "waveforms": {
                "single": "2692591289282789130",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-502594206564913882": {
            "length": 76,
            "waveforms": {
                "single": "-502594206564913882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6122585584415630012": {
            "length": 76,
            "waveforms": {
                "single": "-6122585584415630012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2315413678173006361": {
            "length": 80,
            "waveforms": {
                "single": "-2315413678173006361",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3248877355460422803": {
            "length": 80,
            "waveforms": {
                "single": "3248877355460422803",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3703331837213747901": {
            "length": 80,
            "waveforms": {
                "single": "-3703331837213747901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7648592289780106305": {
            "length": 40,
            "waveforms": {
                "I": "-7648592289780106305_i",
                "Q": "-7648592289780106305_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4565448236497056568": {
            "length": 40,
            "waveforms": {
                "I": "-4565448236497056568_i",
                "Q": "-4565448236497056568_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4299250181728346759": {
            "length": 40,
            "waveforms": {
                "I": "-4299250181728346759_i",
                "Q": "-4299250181728346759_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2164366097631323914": {
            "length": 40,
            "waveforms": {
                "I": "2164366097631323914_i",
                "Q": "2164366097631323914_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8409682919003668174_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-8409682919003668174_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "6372067490193647110": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "9137289095690292990_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "9137289095690292990_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5326538865720618437_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-5326538865720618437_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-1121479897136649109_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1121479897136649109_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2412668905301419931_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-2412668905301419931_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "5056093375855522765_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "5056093375855522765_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8449304757042618870_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "8449304757042618870_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-1556605665873615992_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-1556605665873615992_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6593561549392362358": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-4146341697704914941": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-3924847638506199693": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-4643707078485973297": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-4422213019287258049": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-1505593891304317582": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "3506121866523731516": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3727615925722446764": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "7407113868727041288": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "5925375613725613627": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "4777553796548744854": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7288158642957173643": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8806219761990083753": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8013548144320830920": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-7442764623716301000": {
            "sample": 0.25,
            "type": "constant",
        },
        "5383988072142534486": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3460584780577335435": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1988060747490821406": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7803241819344416597": {
            "sample": 0.25,
            "type": "constant",
        },
        "209698940512345457": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3156832405117916844": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2935338345919201596": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3212532749335203810": {
            "sample": 0.25,
            "type": "constant",
        },
        "594639156907419841": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "816133216106135089": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4495631159110729613": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "3013892904109301952": {
            "sample": 0.25,
            "type": "constant",
        },
        "1866071086932433179": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5801283969589117190": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5677323582483482002": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "4285324834134315290": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7780387605371603207": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2472505362526222811": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1851179594639529267": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "4670265050529389674": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6508955675346589869": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2701783769103966218": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8321775146954682348": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-116245857727690569": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6124015458951515485": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5902521399752800237": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3507551741059616989": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1584148449494417938": {
            "sample": 0.25,
            "type": "constant",
        },
        "102410194492990277": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1528448105277130972": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8712766679205428865": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-7286728768421288170": {
            "sample": 0.25,
            "type": "constant",
        },
        "1373842124518003615": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5088969080418121307": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6607051941544767961": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-1060303114976782408": {
            "sample": 0.25,
            "type": "constant",
        },
        "8804811629547934824": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9026305688746650072": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7056394532785341143": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-6834900473586625895": {
            "sample": 0.25,
            "type": "constant",
        },
        "5604073998899100805": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9035498168567827160": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4415646726384743784": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "596069031443305314": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6616244421365945049": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2793828719446472177": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3015322778645187425": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-2004360372225874247": {
            "sample": 0.25,
            "type": "constant",
        },
        "8248532595671951771": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6766794340670524110": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8000451790034432982": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-7778957730835717734": {
            "sample": 0.25,
            "type": "constant",
        },
        "2473935237062108284": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5581198042832550871": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1774026136589927220": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-347988225805786525": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2700353894568080745": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2692591289282789130": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-502594206564913882": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-6122585584415630012": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2315413678173006361": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3248877355460422803": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3703331837213747901": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-7648592289780106305_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-7648592289780106305_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-4565448236497056568_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-4565448236497056568_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-4299250181728346759_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-4299250181728346759_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "2164366097631323914_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "2164366097631323914_q": {
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
                    "offset": -0.25498290735703955,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": -0.4530870218982913,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.05418914676504196,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
        "con2": {
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
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "1": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
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
                    "crosstalk": {},
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "1": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 2),
            },
            "intermediate_frequency": 0,
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "3248877355460422803": "3248877355460422803",
                "-3703331837213747901": "-3703331837213747901",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 6),
            },
            "intermediate_frequency": 0,
        },
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 7),
            },
            "intermediate_frequency": 0,
        },
        "B1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-8409682919003668174": "-8409682919003668174",
                "-7648592289780106305": "-7648592289780106305",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 3),
                "Q": ('con2', 1, 4),
                "mixer": "B1/drive_mixer_a25",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "8449304757042618870": "8449304757042618870",
                "2164366097631323914": "2164366097631323914",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con3', 1, 7),
                "Q": ('con3', 1, 8),
                "mixer": "B4/drive_mixer_0ae",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
        "B3/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "-112377154948369288": "-112377154948369288_B3/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B3/acquisition_mixer_ccf",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-5326538865720618437": "-5326538865720618437",
                "-4565448236497056568": "-4565448236497056568",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 7),
                "Q": ('con2', 1, 8),
                "mixer": "B2/drive_mixer_e4f",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
        "B2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "1283717487460058200": "1283717487460058200_B2/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B2/acquisition_mixer_e58",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
        "B1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "-3211167734745208851": "-3211167734745208851_B1/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B1/acquisition_mixer_2cb",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
        },
        "B3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-2412668905301419931": "-2412668905301419931",
                "-4299250181728346759": "-4299250181728346759",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con3', 1, 1),
                "Q": ('con3', 1, 2),
                "mixer": "B3/drive_mixer_f80",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
        "B4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "3903936994315933848": "3903936994315933848_B4/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B4/acquisition_mixer_77a",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "-8409682919003668174": {
            "length": 40,
            "waveforms": {
                "I": "-8409682919003668174_i",
                "Q": "-8409682919003668174_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6372067490193647110": {
            "length": 16,
            "waveforms": {
                "single": "6372067490193647110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3211167734745208851_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "9137289095690292990_i",
                "Q": "9137289095690292990_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5326538865720618437": {
            "length": 40,
            "waveforms": {
                "I": "-5326538865720618437_i",
                "Q": "-5326538865720618437_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1283717487460058200_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1121479897136649109_i",
                "Q": "-1121479897136649109_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2412668905301419931": {
            "length": 40,
            "waveforms": {
                "I": "-2412668905301419931_i",
                "Q": "-2412668905301419931_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-112377154948369288_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5056093375855522765_i",
                "Q": "5056093375855522765_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8449304757042618870": {
            "length": 40,
            "waveforms": {
                "I": "8449304757042618870_i",
                "Q": "8449304757042618870_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3903936994315933848_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1556605665873615992_i",
                "Q": "-1556605665873615992_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6593561549392362358": {
            "length": 16,
            "waveforms": {
                "single": "6593561549392362358",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4146341697704914941": {
            "length": 16,
            "waveforms": {
                "single": "-4146341697704914941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3924847638506199693": {
            "length": 16,
            "waveforms": {
                "single": "-3924847638506199693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4643707078485973297": {
            "length": 16,
            "waveforms": {
                "single": "-4643707078485973297",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4422213019287258049": {
            "length": 16,
            "waveforms": {
                "single": "-4422213019287258049",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1505593891304317582": {
            "length": 16,
            "waveforms": {
                "single": "-1505593891304317582",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3506121866523731516": {
            "length": 16,
            "waveforms": {
                "single": "3506121866523731516",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3727615925722446764": {
            "length": 16,
            "waveforms": {
                "single": "3727615925722446764",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7407113868727041288": {
            "length": 16,
            "waveforms": {
                "single": "7407113868727041288",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5925375613725613627": {
            "length": 16,
            "waveforms": {
                "single": "5925375613725613627",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4777553796548744854": {
            "length": 16,
            "waveforms": {
                "single": "4777553796548744854",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7288158642957173643": {
            "length": 16,
            "waveforms": {
                "single": "-7288158642957173643",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8806219761990083753": {
            "length": 16,
            "waveforms": {
                "single": "8806219761990083753",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8013548144320830920": {
            "length": 16,
            "waveforms": {
                "single": "8013548144320830920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7442764623716301000": {
            "length": 16,
            "waveforms": {
                "single": "-7442764623716301000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5383988072142534486": {
            "length": 20,
            "waveforms": {
                "single": "5383988072142534486",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3460584780577335435": {
            "length": 20,
            "waveforms": {
                "single": "3460584780577335435",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1988060747490821406": {
            "length": 20,
            "waveforms": {
                "single": "-1988060747490821406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7803241819344416597": {
            "length": 20,
            "waveforms": {
                "single": "7803241819344416597",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "209698940512345457": {
            "length": 24,
            "waveforms": {
                "single": "209698940512345457",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3156832405117916844": {
            "length": 24,
            "waveforms": {
                "single": "-3156832405117916844",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2935338345919201596": {
            "length": 24,
            "waveforms": {
                "single": "-2935338345919201596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3212532749335203810": {
            "length": 24,
            "waveforms": {
                "single": "-3212532749335203810",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "594639156907419841": {
            "length": 28,
            "waveforms": {
                "single": "594639156907419841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "816133216106135089": {
            "length": 28,
            "waveforms": {
                "single": "816133216106135089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4495631159110729613": {
            "length": 28,
            "waveforms": {
                "single": "4495631159110729613",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3013892904109301952": {
            "length": 28,
            "waveforms": {
                "single": "3013892904109301952",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1866071086932433179": {
            "length": 32,
            "waveforms": {
                "single": "1866071086932433179",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5801283969589117190": {
            "length": 32,
            "waveforms": {
                "single": "-5801283969589117190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5677323582483482002": {
            "length": 32,
            "waveforms": {
                "single": "-5677323582483482002",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4285324834134315290": {
            "length": 32,
            "waveforms": {
                "single": "4285324834134315290",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7780387605371603207": {
            "length": 36,
            "waveforms": {
                "single": "-7780387605371603207",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2472505362526222811": {
            "length": 36,
            "waveforms": {
                "single": "2472505362526222811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1851179594639529267": {
            "length": 36,
            "waveforms": {
                "single": "1851179594639529267",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4670265050529389674": {
            "length": 36,
            "waveforms": {
                "single": "4670265050529389674",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6508955675346589869": {
            "length": 40,
            "waveforms": {
                "single": "-6508955675346589869",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2701783769103966218": {
            "length": 40,
            "waveforms": {
                "single": "-2701783769103966218",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8321775146954682348": {
            "length": 40,
            "waveforms": {
                "single": "-8321775146954682348",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-116245857727690569": {
            "length": 40,
            "waveforms": {
                "single": "-116245857727690569",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6124015458951515485": {
            "length": 44,
            "waveforms": {
                "single": "-6124015458951515485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5902521399752800237": {
            "length": 44,
            "waveforms": {
                "single": "-5902521399752800237",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3507551741059616989": {
            "length": 44,
            "waveforms": {
                "single": "3507551741059616989",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1584148449494417938": {
            "length": 44,
            "waveforms": {
                "single": "1584148449494417938",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "102410194492990277": {
            "length": 48,
            "waveforms": {
                "single": "102410194492990277",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1528448105277130972": {
            "length": 48,
            "waveforms": {
                "single": "1528448105277130972",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8712766679205428865": {
            "length": 48,
            "waveforms": {
                "single": "-8712766679205428865",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7286728768421288170": {
            "length": 48,
            "waveforms": {
                "single": "-7286728768421288170",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1373842124518003615": {
            "length": 52,
            "waveforms": {
                "single": "1373842124518003615",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5088969080418121307": {
            "length": 52,
            "waveforms": {
                "single": "-5088969080418121307",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6607051941544767961": {
            "length": 52,
            "waveforms": {
                "single": "6607051941544767961",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1060303114976782408": {
            "length": 52,
            "waveforms": {
                "single": "-1060303114976782408",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8804811629547934824": {
            "length": 56,
            "waveforms": {
                "single": "8804811629547934824",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9026305688746650072": {
            "length": 56,
            "waveforms": {
                "single": "9026305688746650072",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7056394532785341143": {
            "length": 56,
            "waveforms": {
                "single": "-7056394532785341143",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6834900473586625895": {
            "length": 56,
            "waveforms": {
                "single": "-6834900473586625895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5604073998899100805": {
            "length": 60,
            "waveforms": {
                "single": "5604073998899100805",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9035498168567827160": {
            "length": 60,
            "waveforms": {
                "single": "-9035498168567827160",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4415646726384743784": {
            "length": 60,
            "waveforms": {
                "single": "-4415646726384743784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "596069031443305314": {
            "length": 60,
            "waveforms": {
                "single": "596069031443305314",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6616244421365945049": {
            "length": 64,
            "waveforms": {
                "single": "-6616244421365945049",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2793828719446472177": {
            "length": 64,
            "waveforms": {
                "single": "2793828719446472177",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3015322778645187425": {
            "length": 64,
            "waveforms": {
                "single": "3015322778645187425",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2004360372225874247": {
            "length": 64,
            "waveforms": {
                "single": "-2004360372225874247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8248532595671951771": {
            "length": 68,
            "waveforms": {
                "single": "8248532595671951771",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6766794340670524110": {
            "length": 68,
            "waveforms": {
                "single": "6766794340670524110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8000451790034432982": {
            "length": 68,
            "waveforms": {
                "single": "-8000451790034432982",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7778957730835717734": {
            "length": 68,
            "waveforms": {
                "single": "-7778957730835717734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2473935237062108284": {
            "length": 72,
            "waveforms": {
                "single": "2473935237062108284",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5581198042832550871": {
            "length": 72,
            "waveforms": {
                "single": "-5581198042832550871",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1774026136589927220": {
            "length": 72,
            "waveforms": {
                "single": "-1774026136589927220",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-347988225805786525": {
            "length": 72,
            "waveforms": {
                "single": "-347988225805786525",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2700353894568080745": {
            "length": 76,
            "waveforms": {
                "single": "-2700353894568080745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2692591289282789130": {
            "length": 76,
            "waveforms": {
                "single": "2692591289282789130",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-502594206564913882": {
            "length": 76,
            "waveforms": {
                "single": "-502594206564913882",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6122585584415630012": {
            "length": 76,
            "waveforms": {
                "single": "-6122585584415630012",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2315413678173006361": {
            "length": 80,
            "waveforms": {
                "single": "-2315413678173006361",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3248877355460422803": {
            "length": 80,
            "waveforms": {
                "single": "3248877355460422803",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3703331837213747901": {
            "length": 80,
            "waveforms": {
                "single": "-3703331837213747901",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7648592289780106305": {
            "length": 40,
            "waveforms": {
                "I": "-7648592289780106305_i",
                "Q": "-7648592289780106305_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4565448236497056568": {
            "length": 40,
            "waveforms": {
                "I": "-4565448236497056568_i",
                "Q": "-4565448236497056568_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4299250181728346759": {
            "length": 40,
            "waveforms": {
                "I": "-4299250181728346759_i",
                "Q": "-4299250181728346759_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2164366097631323914": {
            "length": 40,
            "waveforms": {
                "I": "2164366097631323914_i",
                "Q": "2164366097631323914_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-8409682919003668174_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8409682919003668174_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6372067490193647110": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9137289095690292990_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "9137289095690292990_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5326538865720618437_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5326538865720618437_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1121479897136649109_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-1121479897136649109_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2412668905301419931_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2412668905301419931_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5056093375855522765_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "5056093375855522765_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8449304757042618870_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8449304757042618870_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1556605665873615992_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-1556605665873615992_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6593561549392362358": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4146341697704914941": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3924847638506199693": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4643707078485973297": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4422213019287258049": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1505593891304317582": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3506121866523731516": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3727615925722446764": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7407113868727041288": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5925375613725613627": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4777553796548744854": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7288158642957173643": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8806219761990083753": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8013548144320830920": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7442764623716301000": {
            "type": "constant",
            "sample": 0.25,
        },
        "5383988072142534486": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3460584780577335435": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1988060747490821406": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7803241819344416597": {
            "type": "constant",
            "sample": 0.25,
        },
        "209698940512345457": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3156832405117916844": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2935338345919201596": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3212532749335203810": {
            "type": "constant",
            "sample": 0.25,
        },
        "594639156907419841": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "816133216106135089": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4495631159110729613": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3013892904109301952": {
            "type": "constant",
            "sample": 0.25,
        },
        "1866071086932433179": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5801283969589117190": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5677323582483482002": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4285324834134315290": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7780387605371603207": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2472505362526222811": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1851179594639529267": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4670265050529389674": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6508955675346589869": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2701783769103966218": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8321775146954682348": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-116245857727690569": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6124015458951515485": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5902521399752800237": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3507551741059616989": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1584148449494417938": {
            "type": "constant",
            "sample": 0.25,
        },
        "102410194492990277": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1528448105277130972": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8712766679205428865": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7286728768421288170": {
            "type": "constant",
            "sample": 0.25,
        },
        "1373842124518003615": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5088969080418121307": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6607051941544767961": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1060303114976782408": {
            "type": "constant",
            "sample": 0.25,
        },
        "8804811629547934824": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9026305688746650072": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7056394532785341143": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6834900473586625895": {
            "type": "constant",
            "sample": 0.25,
        },
        "5604073998899100805": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9035498168567827160": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4415646726384743784": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "596069031443305314": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6616244421365945049": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2793828719446472177": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3015322778645187425": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2004360372225874247": {
            "type": "constant",
            "sample": 0.25,
        },
        "8248532595671951771": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6766794340670524110": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8000451790034432982": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7778957730835717734": {
            "type": "constant",
            "sample": 0.25,
        },
        "2473935237062108284": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5581198042832550871": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1774026136589927220": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-347988225805786525": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2700353894568080745": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2692591289282789130": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-502594206564913882": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6122585584415630012": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2315413678173006361": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3248877355460422803": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3703331837213747901": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7648592289780106305_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7648592289780106305_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4565448236497056568_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4565448236497056568_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4299250181728346759_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4299250181728346759_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2164366097631323914_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2164366097631323914_q": {
            "type": "arbitrary",
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B1/drive_mixer_a25": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_0ae": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_ccf": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_e4f": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_e58": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_2cb": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_f80": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_77a": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

