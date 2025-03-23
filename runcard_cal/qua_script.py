
# Single QUA script generated at 2025-03-23 18:46:42.753060
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("2031895376907812398", "B2/drive")
        wait(11, "B2/flux")
        play("8292331557236670004", "B2/flux")
        wait(46, "B2/drive")
        play("2792986006131374267", "B2/drive")
        wait(66, "B2/acquisition")
        measure("417140197167284145", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.6396323988896735)-(v3*0.7686809444045309))>0.002593462025505251)))
        r1 = declare_stream()
        save(v4, r1)
        play("6325376375890920099", "B4/drive")
        wait(11, "B4/flux")
        play("8292331557236670004", "B4/flux")
        wait(46, "B4/drive")
        play("7086467005114481968", "B4/drive")
        wait(66, "B4/acquisition")
        measure("5212033345519105269", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36225808599348724)-(v6*0.9320778289028954))>-0.0006247539974722703)))
        r2 = declare_stream()
        save(v7, r2)
        wait(25001, "B2/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B2/drive")
        wait(25537, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("2031895376907812398", "B2/drive")
        wait(11, "B2/flux")
        play("624976500715119635", "B2/flux")
        wait(46, "B2/drive")
        play("2792986006131374267", "B2/drive")
        wait(66, "B2/acquisition")
        measure("417140197167284145", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.6396323988896735)-(v3*0.7686809444045309))>0.002593462025505251)))
        save(v4, r1)
        play("6325376375890920099", "B4/drive")
        wait(11, "B4/flux")
        play("624976500715119635", "B4/flux")
        wait(46, "B4/drive")
        play("7086467005114481968", "B4/drive")
        wait(66, "B4/acquisition")
        measure("5212033345519105269", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36225808599348724)-(v6*0.9320778289028954))>-0.0006247539974722703)))
        save(v7, r2)
        wait(25001, "B2/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("2031895376907812398", "B2/drive")
        wait(11, "B2/flux")
        play("-1727389168047174585", "B2/flux")
        wait(46, "B2/drive")
        play("2792986006131374267", "B2/drive")
        wait(66, "B2/acquisition")
        measure("417140197167284145", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.6396323988896735)-(v3*0.7686809444045309))>0.002593462025505251)))
        save(v4, r1)
        play("6325376375890920099", "B4/drive")
        wait(11, "B4/flux")
        play("-1727389168047174585", "B4/flux")
        wait(46, "B4/drive")
        play("7086467005114481968", "B4/drive")
        wait(66, "B4/acquisition")
        measure("5212033345519105269", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36225808599348724)-(v6*0.9320778289028954))>-0.0006247539974722703)))
        save(v7, r2)
        wait(25001, "B2/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("2031895376907812398", "B2/drive")
        wait(11, "B2/flux")
        play("5858186317741883981", "B2/flux")
        wait(46, "B2/drive")
        play("2792986006131374267", "B2/drive")
        wait(66, "B2/acquisition")
        measure("417140197167284145", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.6396323988896735)-(v3*0.7686809444045309))>0.002593462025505251)))
        save(v4, r1)
        play("6325376375890920099", "B4/drive")
        wait(11, "B4/flux")
        play("5858186317741883981", "B4/flux")
        wait(46, "B4/drive")
        play("7086467005114481968", "B4/drive")
        wait(66, "B4/acquisition")
        measure("5212033345519105269", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36225808599348724)-(v6*0.9320778289028954))>-0.0006247539974722703)))
        save(v7, r2)
        wait(25001, "B2/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(4).average().save("417140197167284145_B2|acquisition_shots")
        r2.buffer(4).average().save("5212033345519105269_B4|acquisition_shots")


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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
            "operations": {
                "8292331557236670004": "8292331557236670004",
                "624976500715119635": "624976500715119635",
                "-1727389168047174585": "-1727389168047174585",
                "5858186317741883981": "5858186317741883981",
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
                "8292331557236670004": "8292331557236670004",
                "624976500715119635": "624976500715119635",
                "-1727389168047174585": "-1727389168047174585",
                "5858186317741883981": "5858186317741883981",
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
                "417140197167284145": "417140197167284145_B2/acquisition",
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
                "2031895376907812398": "2031895376907812398",
                "2792986006131374267": "2792986006131374267",
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
                "5212033345519105269": "5212033345519105269_B4/acquisition",
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
                "6325376375890920099": "6325376375890920099",
                "7086467005114481968": "7086467005114481968",
            },
        },
    },
    "pulses": {
        "2031895376907812398": {
            "length": 40,
            "waveforms": {
                "I": "2031895376907812398_i",
                "Q": "2031895376907812398_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5977570934780965276": {
            "length": 16,
            "waveforms": {
                "single": "-5977570934780965276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "417140197167284145_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1747882398031596958_i",
                "Q": "-1747882398031596958_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "6325376375890920099": {
            "length": 40,
            "waveforms": {
                "I": "6325376375890920099_i",
                "Q": "6325376375890920099_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5212033345519105269_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4419234642038107487_i",
                "Q": "4419234642038107487_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-5756076875582250028": {
            "length": 16,
            "waveforms": {
                "single": "-5756076875582250028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9171101581584230918": {
            "length": 16,
            "waveforms": {
                "single": "-9171101581584230918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2494779149233709283": {
            "length": 16,
            "waveforms": {
                "single": "2494779149233709283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6530636659779310598": {
            "length": 16,
            "waveforms": {
                "single": "-6530636659779310598",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1674892629447681181": {
            "length": 16,
            "waveforms": {
                "single": "1674892629447681181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1896386688646396429": {
            "length": 16,
            "waveforms": {
                "single": "1896386688646396429",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2879719365628783667": {
            "length": 16,
            "waveforms": {
                "single": "2879719365628783667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4094146376649563292": {
            "length": 16,
            "waveforms": {
                "single": "4094146376649563292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9105862134477612390": {
            "length": 16,
            "waveforms": {
                "single": "9105862134477612390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9119387880033223978": {
            "length": 16,
            "waveforms": {
                "single": "-9119387880033223978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-247206087330571123": {
            "length": 16,
            "waveforms": {
                "single": "-247206087330571123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6921628192030057115": {
            "length": 16,
            "waveforms": {
                "single": "-6921628192030057115",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6700134132831341867": {
            "length": 16,
            "waveforms": {
                "single": "-6700134132831341867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8734447663638149594": {
            "length": 16,
            "waveforms": {
                "single": "-8734447663638149594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8512953604439434346": {
            "length": 16,
            "waveforms": {
                "single": "-8512953604439434346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1352161140085282886": {
            "length": 20,
            "waveforms": {
                "single": "1352161140085282886",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6315193916436267483": {
            "length": 20,
            "waveforms": {
                "single": "-6315193916436267483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2556987876266385372": {
            "length": 20,
            "waveforms": {
                "single": "2556987876266385372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1081984099409503137": {
            "length": 20,
            "waveforms": {
                "single": "-1081984099409503137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4766567582995251931": {
            "length": 24,
            "waveforms": {
                "single": "-4766567582995251931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5043761986411254145": {
            "length": 24,
            "waveforms": {
                "single": "-5043761986411254145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1236590080168630494": {
            "length": 24,
            "waveforms": {
                "single": "-1236590080168630494",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3838935250230151659": {
            "length": 24,
            "waveforms": {
                "single": "-3838935250230151659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2664401922034679278": {
            "length": 28,
            "waveforms": {
                "single": "2664401922034679278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1182663667033251617": {
            "length": 28,
            "waveforms": {
                "single": "1182663667033251617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2608701577817392312": {
            "length": 28,
            "waveforms": {
                "single": "2608701577817392312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6415873484060015963": {
            "length": 28,
            "waveforms": {
                "single": "6415873484060015963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1239668586037485330": {
            "length": 32,
            "waveforms": {
                "single": "1239668586037485330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8613633172063182826": {
            "length": 32,
            "waveforms": {
                "single": "8613633172063182826",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2993641794212466696": {
            "length": 32,
            "waveforms": {
                "single": "2993641794212466696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4599901084619604444": {
            "length": 32,
            "waveforms": {
                "single": "-4599901084619604444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "19950357563478932": {
            "length": 36,
            "waveforms": {
                "single": "19950357563478932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2839035813453339339": {
            "length": 36,
            "waveforms": {
                "single": "2839035813453339339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2180647337417722333": {
            "length": 36,
            "waveforms": {
                "single": "-2180647337417722333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8072245630480103685": {
            "length": 36,
            "waveforms": {
                "single": "8072245630480103685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "404890573958553316": {
            "length": 40,
            "waveforms": {
                "single": "404890573958553316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8176738755226281068": {
            "length": 40,
            "waveforms": {
                "single": "-8176738755226281068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7955244696027565820": {
            "length": 40,
            "waveforms": {
                "single": "-7955244696027565820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2824144321160435427": {
            "length": 40,
            "waveforms": {
                "single": "2824144321160435427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2722034879000801474": {
            "length": 44,
            "waveforms": {
                "single": "-2722034879000801474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "623546626179234162": {
            "length": 44,
            "waveforms": {
                "single": "623546626179234162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-524275190997634611": {
            "length": 44,
            "waveforms": {
                "single": "-524275190997634611",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-302781131798919363": {
            "length": 44,
            "waveforms": {
                "single": "-302781131798919363",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7902748157428072416": {
            "length": 48,
            "waveforms": {
                "single": "7902748157428072416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9117958005497338505": {
            "length": 48,
            "waveforms": {
                "single": "-9117958005497338505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5772376500317302869": {
            "length": 48,
            "waveforms": {
                "single": "-5772376500317302869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "82159084596155021": {
            "length": 48,
            "waveforms": {
                "single": "82159084596155021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7349682432429727094": {
            "length": 52,
            "waveforms": {
                "single": "7349682432429727094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8333015109412114332": {
            "length": 52,
            "waveforms": {
                "single": "8333015109412114332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8899301953276657659": {
            "length": 52,
            "waveforms": {
                "single": "-8899301953276657659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-693772664049665880": {
            "length": 52,
            "waveforms": {
                "single": "-693772664049665880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6313764041900382010": {
            "length": 56,
            "waveforms": {
                "single": "-6313764041900382010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2506592135657758359": {
            "length": 56,
            "waveforms": {
                "single": "-2506592135657758359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8514361736881583275": {
            "length": 56,
            "waveforms": {
                "single": "-8514361736881583275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7580016668065674121": {
            "length": 56,
            "waveforms": {
                "single": "7580016668065674121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9006054578849814816": {
            "length": 60,
            "waveforms": {
                "single": "9006054578849814816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1235160205632745021": {
            "length": 60,
            "waveforms": {
                "single": "-1235160205632745021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2110421299547290615": {
            "length": 60,
            "waveforms": {
                "single": "2110421299547290615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3435757900613946286": {
            "length": 60,
            "waveforms": {
                "single": "-3435757900613946286",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3214263841415231038": {
            "length": 64,
            "waveforms": {
                "single": "-3214263841415231038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6195809299397186188": {
            "length": 64,
            "waveforms": {
                "single": "6195809299397186188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1016504153412064175": {
            "length": 64,
            "waveforms": {
                "single": "-1016504153412064175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9210355259223789773": {
            "length": 64,
            "waveforms": {
                "single": "-9210355259223789773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8615063046599068299": {
            "length": 68,
            "waveforms": {
                "single": "8615063046599068299",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8836557105797783547": {
            "length": 68,
            "waveforms": {
                "single": "8836557105797783547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6414465351617867034": {
            "length": 68,
            "waveforms": {
                "single": "6414465351617867034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7412427279908601206": {
            "length": 68,
            "waveforms": {
                "single": "-7412427279908601206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1557891694995143316": {
            "length": 72,
            "waveforms": {
                "single": "-1557891694995143316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9221497322192857931": {
            "length": 72,
            "waveforms": {
                "single": "9221497322192857931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1957723403683121612": {
            "length": 72,
            "waveforms": {
                "single": "-1957723403683121612",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7027487063513526822": {
            "length": 72,
            "waveforms": {
                "single": "-7027487063513526822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6805993004314811574": {
            "length": 76,
            "waveforms": {
                "single": "-6805993004314811574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6094571869233503141": {
            "length": 76,
            "waveforms": {
                "single": "6094571869233503141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1572783187288047228": {
            "length": 76,
            "waveforms": {
                "single": "-1572783187288047228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8292331557236670004": {
            "length": 76,
            "waveforms": {
                "single": "8292331557236670004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "624976500715119635": {
            "length": 80,
            "waveforms": {
                "single": "624976500715119635",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1727389168047174585": {
            "length": 80,
            "waveforms": {
                "single": "-1727389168047174585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5858186317741883981": {
            "length": 80,
            "waveforms": {
                "single": "5858186317741883981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2792986006131374267": {
            "length": 40,
            "waveforms": {
                "I": "2792986006131374267_i",
                "Q": "2792986006131374267_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7086467005114481968": {
            "length": 40,
            "waveforms": {
                "I": "7086467005114481968_i",
                "Q": "7086467005114481968_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "2031895376907812398_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "2031895376907812398_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-5977570934780965276": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-1747882398031596958_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1747882398031596958_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6325376375890920099_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "6325376375890920099_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "4419234642038107487_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4419234642038107487_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5756076875582250028": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-9171101581584230918": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2494779149233709283": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-6530636659779310598": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "1674892629447681181": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "1896386688646396429": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "2879719365628783667": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "4094146376649563292": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "9105862134477612390": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-9119387880033223978": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-247206087330571123": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-6921628192030057115": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6700134132831341867": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8734447663638149594": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8512953604439434346": {
            "sample": 0.25,
            "type": "constant",
        },
        "1352161140085282886": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6315193916436267483": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2556987876266385372": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-1081984099409503137": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4766567582995251931": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5043761986411254145": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1236590080168630494": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3838935250230151659": {
            "sample": 0.25,
            "type": "constant",
        },
        "2664401922034679278": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1182663667033251617": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2608701577817392312": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "6415873484060015963": {
            "sample": 0.25,
            "type": "constant",
        },
        "1239668586037485330": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8613633172063182826": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2993641794212466696": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-4599901084619604444": {
            "sample": 0.25,
            "type": "constant",
        },
        "19950357563478932": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2839035813453339339": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2180647337417722333": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "8072245630480103685": {
            "sample": 0.25,
            "type": "constant",
        },
        "404890573958553316": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8176738755226281068": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7955244696027565820": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "2824144321160435427": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2722034879000801474": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "623546626179234162": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-524275190997634611": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-302781131798919363": {
            "sample": 0.25,
            "type": "constant",
        },
        "7902748157428072416": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9117958005497338505": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5772376500317302869": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "82159084596155021": {
            "sample": 0.25,
            "type": "constant",
        },
        "7349682432429727094": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8333015109412114332": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8899301953276657659": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-693772664049665880": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6313764041900382010": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2506592135657758359": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8514361736881583275": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "7580016668065674121": {
            "sample": 0.25,
            "type": "constant",
        },
        "9006054578849814816": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1235160205632745021": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2110421299547290615": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-3435757900613946286": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3214263841415231038": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6195809299397186188": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1016504153412064175": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-9210355259223789773": {
            "sample": 0.25,
            "type": "constant",
        },
        "8615063046599068299": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8836557105797783547": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6414465351617867034": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-7412427279908601206": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1557891694995143316": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9221497322192857931": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1957723403683121612": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-7027487063513526822": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6805993004314811574": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6094571869233503141": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1572783187288047228": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "8292331557236670004": {
            "sample": 0.25,
            "type": "constant",
        },
        "624976500715119635": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1727389168047174585": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5858186317741883981": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2792986006131374267_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "2792986006131374267_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "7086467005114481968_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "7086467005114481968_q": {
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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                "8292331557236670004": "8292331557236670004",
                "624976500715119635": "624976500715119635",
                "-1727389168047174585": "-1727389168047174585",
                "5858186317741883981": "5858186317741883981",
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
                "8292331557236670004": "8292331557236670004",
                "624976500715119635": "624976500715119635",
                "-1727389168047174585": "-1727389168047174585",
                "5858186317741883981": "5858186317741883981",
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
                "417140197167284145": "417140197167284145_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_a96",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "2031895376907812398": "2031895376907812398",
                "2792986006131374267": "2792986006131374267",
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
                "mixer": "B2/drive_mixer_10a",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "5212033345519105269": "5212033345519105269_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_43c",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "6325376375890920099": "6325376375890920099",
                "7086467005114481968": "7086467005114481968",
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
                "mixer": "B4/drive_mixer_dfb",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "2031895376907812398": {
            "length": 40,
            "waveforms": {
                "I": "2031895376907812398_i",
                "Q": "2031895376907812398_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5977570934780965276": {
            "length": 16,
            "waveforms": {
                "single": "-5977570934780965276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "417140197167284145_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1747882398031596958_i",
                "Q": "-1747882398031596958_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6325376375890920099": {
            "length": 40,
            "waveforms": {
                "I": "6325376375890920099_i",
                "Q": "6325376375890920099_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5212033345519105269_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4419234642038107487_i",
                "Q": "4419234642038107487_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5756076875582250028": {
            "length": 16,
            "waveforms": {
                "single": "-5756076875582250028",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9171101581584230918": {
            "length": 16,
            "waveforms": {
                "single": "-9171101581584230918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2494779149233709283": {
            "length": 16,
            "waveforms": {
                "single": "2494779149233709283",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6530636659779310598": {
            "length": 16,
            "waveforms": {
                "single": "-6530636659779310598",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1674892629447681181": {
            "length": 16,
            "waveforms": {
                "single": "1674892629447681181",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1896386688646396429": {
            "length": 16,
            "waveforms": {
                "single": "1896386688646396429",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2879719365628783667": {
            "length": 16,
            "waveforms": {
                "single": "2879719365628783667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4094146376649563292": {
            "length": 16,
            "waveforms": {
                "single": "4094146376649563292",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9105862134477612390": {
            "length": 16,
            "waveforms": {
                "single": "9105862134477612390",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9119387880033223978": {
            "length": 16,
            "waveforms": {
                "single": "-9119387880033223978",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-247206087330571123": {
            "length": 16,
            "waveforms": {
                "single": "-247206087330571123",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6921628192030057115": {
            "length": 16,
            "waveforms": {
                "single": "-6921628192030057115",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6700134132831341867": {
            "length": 16,
            "waveforms": {
                "single": "-6700134132831341867",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8734447663638149594": {
            "length": 16,
            "waveforms": {
                "single": "-8734447663638149594",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8512953604439434346": {
            "length": 16,
            "waveforms": {
                "single": "-8512953604439434346",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1352161140085282886": {
            "length": 20,
            "waveforms": {
                "single": "1352161140085282886",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6315193916436267483": {
            "length": 20,
            "waveforms": {
                "single": "-6315193916436267483",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2556987876266385372": {
            "length": 20,
            "waveforms": {
                "single": "2556987876266385372",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1081984099409503137": {
            "length": 20,
            "waveforms": {
                "single": "-1081984099409503137",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4766567582995251931": {
            "length": 24,
            "waveforms": {
                "single": "-4766567582995251931",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5043761986411254145": {
            "length": 24,
            "waveforms": {
                "single": "-5043761986411254145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1236590080168630494": {
            "length": 24,
            "waveforms": {
                "single": "-1236590080168630494",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3838935250230151659": {
            "length": 24,
            "waveforms": {
                "single": "-3838935250230151659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2664401922034679278": {
            "length": 28,
            "waveforms": {
                "single": "2664401922034679278",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1182663667033251617": {
            "length": 28,
            "waveforms": {
                "single": "1182663667033251617",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2608701577817392312": {
            "length": 28,
            "waveforms": {
                "single": "2608701577817392312",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6415873484060015963": {
            "length": 28,
            "waveforms": {
                "single": "6415873484060015963",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1239668586037485330": {
            "length": 32,
            "waveforms": {
                "single": "1239668586037485330",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8613633172063182826": {
            "length": 32,
            "waveforms": {
                "single": "8613633172063182826",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2993641794212466696": {
            "length": 32,
            "waveforms": {
                "single": "2993641794212466696",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4599901084619604444": {
            "length": 32,
            "waveforms": {
                "single": "-4599901084619604444",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "19950357563478932": {
            "length": 36,
            "waveforms": {
                "single": "19950357563478932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2839035813453339339": {
            "length": 36,
            "waveforms": {
                "single": "2839035813453339339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2180647337417722333": {
            "length": 36,
            "waveforms": {
                "single": "-2180647337417722333",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8072245630480103685": {
            "length": 36,
            "waveforms": {
                "single": "8072245630480103685",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "404890573958553316": {
            "length": 40,
            "waveforms": {
                "single": "404890573958553316",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8176738755226281068": {
            "length": 40,
            "waveforms": {
                "single": "-8176738755226281068",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7955244696027565820": {
            "length": 40,
            "waveforms": {
                "single": "-7955244696027565820",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2824144321160435427": {
            "length": 40,
            "waveforms": {
                "single": "2824144321160435427",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2722034879000801474": {
            "length": 44,
            "waveforms": {
                "single": "-2722034879000801474",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "623546626179234162": {
            "length": 44,
            "waveforms": {
                "single": "623546626179234162",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-524275190997634611": {
            "length": 44,
            "waveforms": {
                "single": "-524275190997634611",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-302781131798919363": {
            "length": 44,
            "waveforms": {
                "single": "-302781131798919363",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7902748157428072416": {
            "length": 48,
            "waveforms": {
                "single": "7902748157428072416",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9117958005497338505": {
            "length": 48,
            "waveforms": {
                "single": "-9117958005497338505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5772376500317302869": {
            "length": 48,
            "waveforms": {
                "single": "-5772376500317302869",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "82159084596155021": {
            "length": 48,
            "waveforms": {
                "single": "82159084596155021",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7349682432429727094": {
            "length": 52,
            "waveforms": {
                "single": "7349682432429727094",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8333015109412114332": {
            "length": 52,
            "waveforms": {
                "single": "8333015109412114332",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8899301953276657659": {
            "length": 52,
            "waveforms": {
                "single": "-8899301953276657659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-693772664049665880": {
            "length": 52,
            "waveforms": {
                "single": "-693772664049665880",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6313764041900382010": {
            "length": 56,
            "waveforms": {
                "single": "-6313764041900382010",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2506592135657758359": {
            "length": 56,
            "waveforms": {
                "single": "-2506592135657758359",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8514361736881583275": {
            "length": 56,
            "waveforms": {
                "single": "-8514361736881583275",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7580016668065674121": {
            "length": 56,
            "waveforms": {
                "single": "7580016668065674121",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9006054578849814816": {
            "length": 60,
            "waveforms": {
                "single": "9006054578849814816",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1235160205632745021": {
            "length": 60,
            "waveforms": {
                "single": "-1235160205632745021",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2110421299547290615": {
            "length": 60,
            "waveforms": {
                "single": "2110421299547290615",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3435757900613946286": {
            "length": 60,
            "waveforms": {
                "single": "-3435757900613946286",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3214263841415231038": {
            "length": 64,
            "waveforms": {
                "single": "-3214263841415231038",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6195809299397186188": {
            "length": 64,
            "waveforms": {
                "single": "6195809299397186188",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1016504153412064175": {
            "length": 64,
            "waveforms": {
                "single": "-1016504153412064175",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9210355259223789773": {
            "length": 64,
            "waveforms": {
                "single": "-9210355259223789773",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8615063046599068299": {
            "length": 68,
            "waveforms": {
                "single": "8615063046599068299",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8836557105797783547": {
            "length": 68,
            "waveforms": {
                "single": "8836557105797783547",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6414465351617867034": {
            "length": 68,
            "waveforms": {
                "single": "6414465351617867034",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7412427279908601206": {
            "length": 68,
            "waveforms": {
                "single": "-7412427279908601206",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1557891694995143316": {
            "length": 72,
            "waveforms": {
                "single": "-1557891694995143316",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9221497322192857931": {
            "length": 72,
            "waveforms": {
                "single": "9221497322192857931",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1957723403683121612": {
            "length": 72,
            "waveforms": {
                "single": "-1957723403683121612",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7027487063513526822": {
            "length": 72,
            "waveforms": {
                "single": "-7027487063513526822",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6805993004314811574": {
            "length": 76,
            "waveforms": {
                "single": "-6805993004314811574",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6094571869233503141": {
            "length": 76,
            "waveforms": {
                "single": "6094571869233503141",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1572783187288047228": {
            "length": 76,
            "waveforms": {
                "single": "-1572783187288047228",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8292331557236670004": {
            "length": 76,
            "waveforms": {
                "single": "8292331557236670004",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "624976500715119635": {
            "length": 80,
            "waveforms": {
                "single": "624976500715119635",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1727389168047174585": {
            "length": 80,
            "waveforms": {
                "single": "-1727389168047174585",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5858186317741883981": {
            "length": 80,
            "waveforms": {
                "single": "5858186317741883981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2792986006131374267": {
            "length": 40,
            "waveforms": {
                "I": "2792986006131374267_i",
                "Q": "2792986006131374267_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7086467005114481968": {
            "length": 40,
            "waveforms": {
                "I": "7086467005114481968_i",
                "Q": "7086467005114481968_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "2031895376907812398_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2031895376907812398_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5977570934780965276": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1747882398031596958_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-1747882398031596958_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6325376375890920099_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6325376375890920099_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4419234642038107487_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "4419234642038107487_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5756076875582250028": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9171101581584230918": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2494779149233709283": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6530636659779310598": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1674892629447681181": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1896386688646396429": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2879719365628783667": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4094146376649563292": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9105862134477612390": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9119387880033223978": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-247206087330571123": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6921628192030057115": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6700134132831341867": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8734447663638149594": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8512953604439434346": {
            "type": "constant",
            "sample": 0.25,
        },
        "1352161140085282886": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6315193916436267483": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2556987876266385372": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1081984099409503137": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4766567582995251931": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5043761986411254145": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1236590080168630494": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3838935250230151659": {
            "type": "constant",
            "sample": 0.25,
        },
        "2664401922034679278": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1182663667033251617": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2608701577817392312": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6415873484060015963": {
            "type": "constant",
            "sample": 0.25,
        },
        "1239668586037485330": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8613633172063182826": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2993641794212466696": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4599901084619604444": {
            "type": "constant",
            "sample": 0.25,
        },
        "19950357563478932": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2839035813453339339": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2180647337417722333": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8072245630480103685": {
            "type": "constant",
            "sample": 0.25,
        },
        "404890573958553316": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8176738755226281068": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7955244696027565820": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2824144321160435427": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2722034879000801474": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "623546626179234162": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-524275190997634611": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-302781131798919363": {
            "type": "constant",
            "sample": 0.25,
        },
        "7902748157428072416": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9117958005497338505": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5772376500317302869": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "82159084596155021": {
            "type": "constant",
            "sample": 0.25,
        },
        "7349682432429727094": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8333015109412114332": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8899301953276657659": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-693772664049665880": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6313764041900382010": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2506592135657758359": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8514361736881583275": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7580016668065674121": {
            "type": "constant",
            "sample": 0.25,
        },
        "9006054578849814816": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1235160205632745021": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2110421299547290615": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3435757900613946286": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3214263841415231038": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6195809299397186188": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1016504153412064175": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9210355259223789773": {
            "type": "constant",
            "sample": 0.25,
        },
        "8615063046599068299": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8836557105797783547": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6414465351617867034": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7412427279908601206": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1557891694995143316": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9221497322192857931": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1957723403683121612": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7027487063513526822": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6805993004314811574": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6094571869233503141": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1572783187288047228": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8292331557236670004": {
            "type": "constant",
            "sample": 0.25,
        },
        "624976500715119635": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1727389168047174585": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5858186317741883981": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2792986006131374267_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2792986006131374267_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7086467005114481968_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7086467005114481968_q": {
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
        "B2/acquisition_mixer_a96": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_10a": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_43c": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_dfb": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

