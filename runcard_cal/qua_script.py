
# Single QUA script generated at 2025-04-30 15:35:50.667501
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
        play("-686552758779339543", "B1/drive")
        wait(11, "B1/flux")
        play("7207437942329892343", "B1/flux")
        wait(46, "B1/drive")
        play("74537870444222326", "B1/drive")
        wait(66, "B1/acquisition")
        measure("6124919402453170307", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*-0.9988127626748439)-(v3*-0.04871411620717457))>0.0006911113845537218)))
        r1 = declare_stream()
        save(v4, r1)
        play("-6173253350708915978", "B2/drive")
        wait(11, "B2/flux")
        play("7207437942329892343", "B2/flux")
        wait(46, "B2/drive")
        play("-5412162721485354109", "B2/drive")
        wait(66, "B2/acquisition")
        measure("5635893448275624072", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*-0.195212174212656)-(v6*-0.9807610346252382))>0.002446646735995352)))
        r2 = declare_stream()
        save(v7, r2)
        play("6558236758788460091", "B3/drive")
        wait(11, "B3/flux")
        play("7207437942329892343", "B3/flux")
        wait(46, "B3/drive")
        play("7319327388012021960", "B3/drive")
        wait(66, "B3/acquisition")
        measure("7197591370331236357", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*0.48537056842023735)-(v9*0.8743085332486558))>0.0027410836483659383)))
        r3 = declare_stream()
        save(v10, r3)
        play("-381444957973955202", "B4/drive")
        wait(11, "B4/flux")
        play("7207437942329892343", "B4/flux")
        wait(46, "B4/drive")
        play("379645671249606667", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1911671288928356579", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.9741380753686336)-(v12*-0.2259535574340316))>-0.0004858665884025214)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B1/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        play("-686552758779339543", "B1/drive")
        wait(11, "B1/flux")
        play("-8420220675489798866", "B1/flux")
        wait(46, "B1/drive")
        play("74537870444222326", "B1/drive")
        wait(66, "B1/acquisition")
        measure("6124919402453170307", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*-0.9988127626748439)-(v3*-0.04871411620717457))>0.0006911113845537218)))
        save(v4, r1)
        play("-6173253350708915978", "B2/drive")
        wait(11, "B2/flux")
        play("-8420220675489798866", "B2/flux")
        wait(46, "B2/drive")
        play("-5412162721485354109", "B2/drive")
        wait(66, "B2/acquisition")
        measure("5635893448275624072", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*-0.195212174212656)-(v6*-0.9807610346252382))>0.002446646735995352)))
        save(v7, r2)
        play("6558236758788460091", "B3/drive")
        wait(11, "B3/flux")
        play("-8420220675489798866", "B3/flux")
        wait(46, "B3/drive")
        play("7319327388012021960", "B3/drive")
        wait(66, "B3/acquisition")
        measure("7197591370331236357", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*0.48537056842023735)-(v9*0.8743085332486558))>0.0027410836483659383)))
        save(v10, r3)
        play("-381444957973955202", "B4/drive")
        wait(11, "B4/flux")
        play("-8420220675489798866", "B4/flux")
        wait(46, "B4/drive")
        play("379645671249606667", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1911671288928356579", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.9741380753686336)-(v12*-0.2259535574340316))>-0.0004858665884025214)))
        save(v13, r4)
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B1/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("6124919402453170307_B1|acquisition_shots")
        r2.buffer(2).average().save("5635893448275624072_B2|acquisition_shots")
        r3.buffer(2).average().save("7197591370331236357_B3|acquisition_shots")
        r4.buffer(2).average().save("-1911671288928356579_B4|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "7": {},
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
                "2": {
                    "LO_frequency": 4900000000.0,
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
                "1": {
                    "LO_frequency": 5800000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
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
            "operations": {
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7197591370331236357": "7197591370331236357_B3/acquisition",
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
                "-6173253350708915978": "-6173253350708915978",
                "-5412162721485354109": "-5412162721485354109",
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
                "6124919402453170307": "6124919402453170307_B1/acquisition",
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
                "6558236758788460091": "6558236758788460091",
                "7319327388012021960": "7319327388012021960",
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
            "intermediate_frequency": 100388701.0,
            "operations": {
                "-686552758779339543": "-686552758779339543",
                "74537870444222326": "74537870444222326",
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
                "5635893448275624072": "5635893448275624072_B2/acquisition",
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
                "-1911671288928356579": "-1911671288928356579_B4/acquisition",
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
                "-381444957973955202": "-381444957973955202",
                "379645671249606667": "379645671249606667",
            },
        },
    },
    "pulses": {
        "-686552758779339543": {
            "length": 40,
            "waveforms": {
                "I": "-686552758779339543_i",
                "Q": "-686552758779339543_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6817722210470705409": {
            "length": 16,
            "waveforms": {
                "single": "6817722210470705409",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6124919402453170307_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8740123988881942497_i",
                "Q": "8740123988881942497_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-6173253350708915978": {
            "length": 40,
            "waveforms": {
                "I": "-6173253350708915978_i",
                "Q": "-6173253350708915978_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5635893448275624072_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-675825176859590810_i",
                "Q": "-675825176859590810_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "6558236758788460091": {
            "length": 40,
            "waveforms": {
                "I": "6558236758788460091_i",
                "Q": "6558236758788460091_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7197591370331236357_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "9087425943176489467_i",
                "Q": "9087425943176489467_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-381444957973955202": {
            "length": 40,
            "waveforms": {
                "I": "-381444957973955202_i",
                "Q": "-381444957973955202_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1911671288928356579_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8587571722515976256_i",
                "Q": "8587571722515976256_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-849632846050844960": {
            "length": 16,
            "waveforms": {
                "single": "-849632846050844960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6395812046212081861": {
            "length": 16,
            "waveforms": {
                "single": "-6395812046212081861",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3479192918229141394": {
            "length": 16,
            "waveforms": {
                "single": "-3479192918229141394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5402596209794340445": {
            "length": 16,
            "waveforms": {
                "single": "-5402596209794340445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3976558299010199750": {
            "length": 16,
            "waveforms": {
                "single": "-3976558299010199750",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4228970990216792029": {
            "length": 16,
            "waveforms": {
                "single": "4228970990216792029",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1778798611007032887": {
            "length": 16,
            "waveforms": {
                "single": "-1778798611007032887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2028373295235590764": {
            "length": 16,
            "waveforms": {
                "single": "2028373295235590764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3454411206019731459": {
            "length": 16,
            "waveforms": {
                "single": "3454411206019731459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1102045537257437239": {
            "length": 16,
            "waveforms": {
                "single": "1102045537257437239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5828338217632646038": {
            "length": 16,
            "waveforms": {
                "single": "5828338217632646038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3746224063374252723": {
            "length": 16,
            "waveforms": {
                "single": "-3746224063374252723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4367549831260946267": {
            "length": 16,
            "waveforms": {
                "single": "-4367549831260946267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1486985753652511623": {
            "length": 16,
            "waveforms": {
                "single": "1486985753652511623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6997109903439242701": {
            "length": 16,
            "waveforms": {
                "single": "-6997109903439242701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6258605169616687954": {
            "length": 20,
            "waveforms": {
                "single": "6258605169616687954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3906239500854393734": {
            "length": 20,
            "waveforms": {
                "single": "3906239500854393734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3284913732967700190": {
            "length": 20,
            "waveforms": {
                "single": "3284913732967700190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4908937372844025408": {
            "length": 20,
            "waveforms": {
                "single": "-4908937372844025408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "655353660789403756": {
            "length": 24,
            "waveforms": {
                "single": "655353660789403756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7109535067825226673": {
            "length": 24,
            "waveforms": {
                "single": "-7109535067825226673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2489683625642143297": {
            "length": 24,
            "waveforms": {
                "single": "-2489683625642143297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3891348008561489822": {
            "length": 24,
            "waveforms": {
                "single": "3891348008561489822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1040293877184478140": {
            "length": 28,
            "waveforms": {
                "single": "1040293877184478140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1261787936383193388": {
            "length": 28,
            "waveforms": {
                "single": "1261787936383193388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4941285879387787912": {
            "length": 28,
            "waveforms": {
                "single": "4941285879387787912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5162779938586503160": {
            "length": 28,
            "waveforms": {
                "single": "5162779938586503160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2740688184406586647": {
            "length": 32,
            "waveforms": {
                "single": "2740688184406586647",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8692757441413124597": {
            "length": 32,
            "waveforms": {
                "single": "8692757441413124597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7279032540877257942": {
            "length": 32,
            "waveforms": {
                "single": "-7279032540877257942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5852994630093117247": {
            "length": 32,
            "waveforms": {
                "single": "-5852994630093117247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5954021709899371745": {
            "length": 36,
            "waveforms": {
                "single": "-5954021709899371745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7745479842984744407": {
            "length": 36,
            "waveforms": {
                "single": "7745479842984744407",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5393114174222450187": {
            "length": 36,
            "waveforms": {
                "single": "5393114174222450187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2420794702022222754": {
            "length": 36,
            "waveforms": {
                "single": "2420794702022222754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1476947795130559464": {
            "length": 40,
            "waveforms": {
                "single": "1476947795130559464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-446455496434639587": {
            "length": 40,
            "waveforms": {
                "single": "-446455496434639587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3048800666496160752": {
            "length": 40,
            "waveforms": {
                "single": "-3048800666496160752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5401166335258454972": {
            "length": 40,
            "waveforms": {
                "single": "-5401166335258454972",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5678360738674457186": {
            "length": 44,
            "waveforms": {
                "single": "-5678360738674457186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "824976433590373751": {
            "length": 44,
            "waveforms": {
                "single": "824976433590373751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1777368736471147414": {
            "length": 44,
            "waveforms": {
                "single": "-1777368736471147414",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2029803169771476237": {
            "length": 44,
            "waveforms": {
                "single": "2029803169771476237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2251297228970191485": {
            "length": 48,
            "waveforms": {
                "single": "2251297228970191485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5559780672598097674": {
            "length": 48,
            "waveforms": {
                "single": "5559780672598097674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1431410709184163383": {
            "length": 48,
            "waveforms": {
                "single": "1431410709184163383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8143151571822735378": {
            "length": 48,
            "waveforms": {
                "single": "-8143151571822735378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8764477339709428922": {
            "length": 52,
            "waveforms": {
                "single": "-8764477339709428922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1819475130880826595": {
            "length": 52,
            "waveforms": {
                "single": "-1819475130880826595",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-836142453898439357": {
            "length": 52,
            "waveforms": {
                "single": "-836142453898439357",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-614648394699724109": {
            "length": 52,
            "waveforms": {
                "single": "-614648394699724109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3907669375390279207": {
            "length": 56,
            "waveforms": {
                "single": "3907669375390279207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1434534914485752211": {
            "length": 56,
            "waveforms": {
                "single": "-1434534914485752211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6105429063393446070": {
            "length": 56,
            "waveforms": {
                "single": "6105429063393446070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6816321110330207100": {
            "length": 56,
            "waveforms": {
                "single": "6816321110330207100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8312649044874766647": {
            "length": 60,
            "waveforms": {
                "single": "-8312649044874766647",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "265859392736356296": {
            "length": 60,
            "waveforms": {
                "single": "265859392736356296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6217928649742894246": {
            "length": 60,
            "waveforms": {
                "single": "6217928649742894246",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4688851446087459089": {
            "length": 60,
            "waveforms": {
                "single": "-4688851446087459089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7422755385923996732": {
            "length": 64,
            "waveforms": {
                "single": "7422755385923996732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1158873943260837652": {
            "length": 64,
            "waveforms": {
                "single": "-1158873943260837652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4797845918936726161": {
            "length": 64,
            "waveforms": {
                "single": "-4797845918936726161",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2918285382552219836": {
            "length": 64,
            "waveforms": {
                "single": "2918285382552219836",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2963612118141187368": {
            "length": 68,
            "waveforms": {
                "single": "2963612118141187368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7277602666341372469": {
            "length": 68,
            "waveforms": {
                "single": "-7277602666341372469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7554797069757374683": {
            "length": 68,
            "waveforms": {
                "single": "-7554797069757374683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8097489186127400571": {
            "length": 68,
            "waveforms": {
                "single": "-8097489186127400571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7875995126928685323": {
            "length": 72,
            "waveforms": {
                "single": "-7875995126928685323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "996186665773967532": {
            "length": 72,
            "waveforms": {
                "single": "996186665773967532",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4346017624102063886": {
            "length": 72,
            "waveforms": {
                "single": "-4346017624102063886",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2476193233489737694": {
            "length": 72,
            "waveforms": {
                "single": "-2476193233489737694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-445025621898754114": {
            "length": 76,
            "waveforms": {
                "single": "-445025621898754114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8427156170803898741": {
            "length": 76,
            "waveforms": {
                "single": "8427156170803898741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7483309263912235451": {
            "length": 76,
            "waveforms": {
                "single": "7483309263912235451",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7704803323110950699": {
            "length": 76,
            "waveforms": {
                "single": "7704803323110950699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1869758957895948062": {
            "length": 80,
            "waveforms": {
                "single": "-1869758957895948062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7207437942329892343": {
            "length": 80,
            "waveforms": {
                "single": "7207437942329892343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8420220675489798866": {
            "length": 80,
            "waveforms": {
                "single": "-8420220675489798866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "74537870444222326": {
            "length": 40,
            "waveforms": {
                "I": "74537870444222326_i",
                "Q": "74537870444222326_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5412162721485354109": {
            "length": 40,
            "waveforms": {
                "I": "-5412162721485354109_i",
                "Q": "-5412162721485354109_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7319327388012021960": {
            "length": 40,
            "waveforms": {
                "I": "7319327388012021960_i",
                "Q": "7319327388012021960_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "379645671249606667": {
            "length": 40,
            "waveforms": {
                "I": "379645671249606667_i",
                "Q": "379645671249606667_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-686552758779339543_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-686552758779339543_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "6817722210470705409": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "8740123988881942497_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "8740123988881942497_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6173253350708915978_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-6173253350708915978_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-675825176859590810_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-675825176859590810_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6558236758788460091_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "6558236758788460091_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "9087425943176489467_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "9087425943176489467_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-381444957973955202_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-381444957973955202_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "8587571722515976256_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "8587571722515976256_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-849632846050844960": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-6395812046212081861": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-3479192918229141394": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5402596209794340445": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-3976558299010199750": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "4228970990216792029": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-1778798611007032887": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "2028373295235590764": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3454411206019731459": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "1102045537257437239": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5828338217632646038": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-3746224063374252723": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4367549831260946267": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1486985753652511623": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-6997109903439242701": {
            "sample": 0.25,
            "type": "constant",
        },
        "6258605169616687954": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3906239500854393734": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3284913732967700190": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-4908937372844025408": {
            "sample": 0.25,
            "type": "constant",
        },
        "655353660789403756": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7109535067825226673": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2489683625642143297": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "3891348008561489822": {
            "sample": 0.25,
            "type": "constant",
        },
        "1040293877184478140": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1261787936383193388": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4941285879387787912": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "5162779938586503160": {
            "sample": 0.25,
            "type": "constant",
        },
        "2740688184406586647": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8692757441413124597": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7279032540877257942": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5852994630093117247": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5954021709899371745": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7745479842984744407": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5393114174222450187": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "2420794702022222754": {
            "sample": 0.25,
            "type": "constant",
        },
        "1476947795130559464": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-446455496434639587": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3048800666496160752": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-5401166335258454972": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5678360738674457186": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "824976433590373751": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1777368736471147414": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "2029803169771476237": {
            "sample": 0.25,
            "type": "constant",
        },
        "2251297228970191485": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5559780672598097674": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1431410709184163383": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-8143151571822735378": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8764477339709428922": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1819475130880826595": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-836142453898439357": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-614648394699724109": {
            "sample": 0.25,
            "type": "constant",
        },
        "3907669375390279207": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1434534914485752211": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6105429063393446070": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "6816321110330207100": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8312649044874766647": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "265859392736356296": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6217928649742894246": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-4688851446087459089": {
            "sample": 0.25,
            "type": "constant",
        },
        "7422755385923996732": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1158873943260837652": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4797845918936726161": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "2918285382552219836": {
            "sample": 0.25,
            "type": "constant",
        },
        "2963612118141187368": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7277602666341372469": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7554797069757374683": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-8097489186127400571": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7875995126928685323": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "996186665773967532": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4346017624102063886": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-2476193233489737694": {
            "sample": 0.25,
            "type": "constant",
        },
        "-445025621898754114": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8427156170803898741": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7483309263912235451": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7704803323110950699": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1869758957895948062": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7207437942329892343": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8420220675489798866": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "74537870444222326_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "74537870444222326_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-5412162721485354109_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-5412162721485354109_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "7319327388012021960_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "7319327388012021960_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "379645671249606667_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "379645671249606667_q": {
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
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "3": {
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
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7207437942329892343": "7207437942329892343",
                "-8420220675489798866": "-8420220675489798866",
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
                "7197591370331236357": "7197591370331236357_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_cdf",
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
                "-6173253350708915978": "-6173253350708915978",
                "-5412162721485354109": "-5412162721485354109",
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
                "mixer": "B2/drive_mixer_e75",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "6124919402453170307": "6124919402453170307_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_e84",
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
                "6558236758788460091": "6558236758788460091",
                "7319327388012021960": "7319327388012021960",
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
                "mixer": "B3/drive_mixer_11c",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-686552758779339543": "-686552758779339543",
                "74537870444222326": "74537870444222326",
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
                "mixer": "B1/drive_mixer_3e6",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "5635893448275624072": "5635893448275624072_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_674",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-1911671288928356579": "-1911671288928356579_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e25",
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
                "-381444957973955202": "-381444957973955202",
                "379645671249606667": "379645671249606667",
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
                "mixer": "B4/drive_mixer_611",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "-686552758779339543": {
            "length": 40,
            "waveforms": {
                "I": "-686552758779339543_i",
                "Q": "-686552758779339543_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6817722210470705409": {
            "length": 16,
            "waveforms": {
                "single": "6817722210470705409",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6124919402453170307_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8740123988881942497_i",
                "Q": "8740123988881942497_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6173253350708915978": {
            "length": 40,
            "waveforms": {
                "I": "-6173253350708915978_i",
                "Q": "-6173253350708915978_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5635893448275624072_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-675825176859590810_i",
                "Q": "-675825176859590810_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6558236758788460091": {
            "length": 40,
            "waveforms": {
                "I": "6558236758788460091_i",
                "Q": "6558236758788460091_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7197591370331236357_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "9087425943176489467_i",
                "Q": "9087425943176489467_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-381444957973955202": {
            "length": 40,
            "waveforms": {
                "I": "-381444957973955202_i",
                "Q": "-381444957973955202_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1911671288928356579_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8587571722515976256_i",
                "Q": "8587571722515976256_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-849632846050844960": {
            "length": 16,
            "waveforms": {
                "single": "-849632846050844960",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6395812046212081861": {
            "length": 16,
            "waveforms": {
                "single": "-6395812046212081861",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3479192918229141394": {
            "length": 16,
            "waveforms": {
                "single": "-3479192918229141394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5402596209794340445": {
            "length": 16,
            "waveforms": {
                "single": "-5402596209794340445",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3976558299010199750": {
            "length": 16,
            "waveforms": {
                "single": "-3976558299010199750",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4228970990216792029": {
            "length": 16,
            "waveforms": {
                "single": "4228970990216792029",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1778798611007032887": {
            "length": 16,
            "waveforms": {
                "single": "-1778798611007032887",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2028373295235590764": {
            "length": 16,
            "waveforms": {
                "single": "2028373295235590764",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3454411206019731459": {
            "length": 16,
            "waveforms": {
                "single": "3454411206019731459",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1102045537257437239": {
            "length": 16,
            "waveforms": {
                "single": "1102045537257437239",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5828338217632646038": {
            "length": 16,
            "waveforms": {
                "single": "5828338217632646038",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3746224063374252723": {
            "length": 16,
            "waveforms": {
                "single": "-3746224063374252723",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4367549831260946267": {
            "length": 16,
            "waveforms": {
                "single": "-4367549831260946267",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1486985753652511623": {
            "length": 16,
            "waveforms": {
                "single": "1486985753652511623",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6997109903439242701": {
            "length": 16,
            "waveforms": {
                "single": "-6997109903439242701",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6258605169616687954": {
            "length": 20,
            "waveforms": {
                "single": "6258605169616687954",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3906239500854393734": {
            "length": 20,
            "waveforms": {
                "single": "3906239500854393734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3284913732967700190": {
            "length": 20,
            "waveforms": {
                "single": "3284913732967700190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4908937372844025408": {
            "length": 20,
            "waveforms": {
                "single": "-4908937372844025408",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "655353660789403756": {
            "length": 24,
            "waveforms": {
                "single": "655353660789403756",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7109535067825226673": {
            "length": 24,
            "waveforms": {
                "single": "-7109535067825226673",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2489683625642143297": {
            "length": 24,
            "waveforms": {
                "single": "-2489683625642143297",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3891348008561489822": {
            "length": 24,
            "waveforms": {
                "single": "3891348008561489822",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1040293877184478140": {
            "length": 28,
            "waveforms": {
                "single": "1040293877184478140",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1261787936383193388": {
            "length": 28,
            "waveforms": {
                "single": "1261787936383193388",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4941285879387787912": {
            "length": 28,
            "waveforms": {
                "single": "4941285879387787912",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5162779938586503160": {
            "length": 28,
            "waveforms": {
                "single": "5162779938586503160",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2740688184406586647": {
            "length": 32,
            "waveforms": {
                "single": "2740688184406586647",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8692757441413124597": {
            "length": 32,
            "waveforms": {
                "single": "8692757441413124597",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7279032540877257942": {
            "length": 32,
            "waveforms": {
                "single": "-7279032540877257942",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5852994630093117247": {
            "length": 32,
            "waveforms": {
                "single": "-5852994630093117247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5954021709899371745": {
            "length": 36,
            "waveforms": {
                "single": "-5954021709899371745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7745479842984744407": {
            "length": 36,
            "waveforms": {
                "single": "7745479842984744407",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5393114174222450187": {
            "length": 36,
            "waveforms": {
                "single": "5393114174222450187",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2420794702022222754": {
            "length": 36,
            "waveforms": {
                "single": "2420794702022222754",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1476947795130559464": {
            "length": 40,
            "waveforms": {
                "single": "1476947795130559464",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-446455496434639587": {
            "length": 40,
            "waveforms": {
                "single": "-446455496434639587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3048800666496160752": {
            "length": 40,
            "waveforms": {
                "single": "-3048800666496160752",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5401166335258454972": {
            "length": 40,
            "waveforms": {
                "single": "-5401166335258454972",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5678360738674457186": {
            "length": 44,
            "waveforms": {
                "single": "-5678360738674457186",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "824976433590373751": {
            "length": 44,
            "waveforms": {
                "single": "824976433590373751",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1777368736471147414": {
            "length": 44,
            "waveforms": {
                "single": "-1777368736471147414",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2029803169771476237": {
            "length": 44,
            "waveforms": {
                "single": "2029803169771476237",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2251297228970191485": {
            "length": 48,
            "waveforms": {
                "single": "2251297228970191485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5559780672598097674": {
            "length": 48,
            "waveforms": {
                "single": "5559780672598097674",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1431410709184163383": {
            "length": 48,
            "waveforms": {
                "single": "1431410709184163383",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8143151571822735378": {
            "length": 48,
            "waveforms": {
                "single": "-8143151571822735378",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8764477339709428922": {
            "length": 52,
            "waveforms": {
                "single": "-8764477339709428922",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1819475130880826595": {
            "length": 52,
            "waveforms": {
                "single": "-1819475130880826595",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-836142453898439357": {
            "length": 52,
            "waveforms": {
                "single": "-836142453898439357",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-614648394699724109": {
            "length": 52,
            "waveforms": {
                "single": "-614648394699724109",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3907669375390279207": {
            "length": 56,
            "waveforms": {
                "single": "3907669375390279207",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1434534914485752211": {
            "length": 56,
            "waveforms": {
                "single": "-1434534914485752211",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6105429063393446070": {
            "length": 56,
            "waveforms": {
                "single": "6105429063393446070",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6816321110330207100": {
            "length": 56,
            "waveforms": {
                "single": "6816321110330207100",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8312649044874766647": {
            "length": 60,
            "waveforms": {
                "single": "-8312649044874766647",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "265859392736356296": {
            "length": 60,
            "waveforms": {
                "single": "265859392736356296",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6217928649742894246": {
            "length": 60,
            "waveforms": {
                "single": "6217928649742894246",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4688851446087459089": {
            "length": 60,
            "waveforms": {
                "single": "-4688851446087459089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7422755385923996732": {
            "length": 64,
            "waveforms": {
                "single": "7422755385923996732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1158873943260837652": {
            "length": 64,
            "waveforms": {
                "single": "-1158873943260837652",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4797845918936726161": {
            "length": 64,
            "waveforms": {
                "single": "-4797845918936726161",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2918285382552219836": {
            "length": 64,
            "waveforms": {
                "single": "2918285382552219836",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2963612118141187368": {
            "length": 68,
            "waveforms": {
                "single": "2963612118141187368",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7277602666341372469": {
            "length": 68,
            "waveforms": {
                "single": "-7277602666341372469",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7554797069757374683": {
            "length": 68,
            "waveforms": {
                "single": "-7554797069757374683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8097489186127400571": {
            "length": 68,
            "waveforms": {
                "single": "-8097489186127400571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7875995126928685323": {
            "length": 72,
            "waveforms": {
                "single": "-7875995126928685323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "996186665773967532": {
            "length": 72,
            "waveforms": {
                "single": "996186665773967532",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4346017624102063886": {
            "length": 72,
            "waveforms": {
                "single": "-4346017624102063886",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2476193233489737694": {
            "length": 72,
            "waveforms": {
                "single": "-2476193233489737694",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-445025621898754114": {
            "length": 76,
            "waveforms": {
                "single": "-445025621898754114",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8427156170803898741": {
            "length": 76,
            "waveforms": {
                "single": "8427156170803898741",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7483309263912235451": {
            "length": 76,
            "waveforms": {
                "single": "7483309263912235451",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7704803323110950699": {
            "length": 76,
            "waveforms": {
                "single": "7704803323110950699",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1869758957895948062": {
            "length": 80,
            "waveforms": {
                "single": "-1869758957895948062",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7207437942329892343": {
            "length": 80,
            "waveforms": {
                "single": "7207437942329892343",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8420220675489798866": {
            "length": 80,
            "waveforms": {
                "single": "-8420220675489798866",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "74537870444222326": {
            "length": 40,
            "waveforms": {
                "I": "74537870444222326_i",
                "Q": "74537870444222326_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5412162721485354109": {
            "length": 40,
            "waveforms": {
                "I": "-5412162721485354109_i",
                "Q": "-5412162721485354109_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7319327388012021960": {
            "length": 40,
            "waveforms": {
                "I": "7319327388012021960_i",
                "Q": "7319327388012021960_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "379645671249606667": {
            "length": 40,
            "waveforms": {
                "I": "379645671249606667_i",
                "Q": "379645671249606667_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-686552758779339543_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-686552758779339543_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6817722210470705409": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8740123988881942497_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "8740123988881942497_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6173253350708915978_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6173253350708915978_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-675825176859590810_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-675825176859590810_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6558236758788460091_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6558236758788460091_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9087425943176489467_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "9087425943176489467_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-381444957973955202_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-381444957973955202_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8587571722515976256_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "8587571722515976256_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-849632846050844960": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6395812046212081861": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3479192918229141394": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5402596209794340445": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3976558299010199750": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4228970990216792029": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1778798611007032887": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2028373295235590764": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3454411206019731459": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1102045537257437239": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5828338217632646038": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3746224063374252723": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4367549831260946267": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1486985753652511623": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6997109903439242701": {
            "type": "constant",
            "sample": 0.25,
        },
        "6258605169616687954": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3906239500854393734": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3284913732967700190": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4908937372844025408": {
            "type": "constant",
            "sample": 0.25,
        },
        "655353660789403756": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7109535067825226673": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2489683625642143297": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3891348008561489822": {
            "type": "constant",
            "sample": 0.25,
        },
        "1040293877184478140": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1261787936383193388": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4941285879387787912": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5162779938586503160": {
            "type": "constant",
            "sample": 0.25,
        },
        "2740688184406586647": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8692757441413124597": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7279032540877257942": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5852994630093117247": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5954021709899371745": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7745479842984744407": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5393114174222450187": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2420794702022222754": {
            "type": "constant",
            "sample": 0.25,
        },
        "1476947795130559464": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-446455496434639587": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3048800666496160752": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5401166335258454972": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5678360738674457186": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "824976433590373751": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1777368736471147414": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2029803169771476237": {
            "type": "constant",
            "sample": 0.25,
        },
        "2251297228970191485": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5559780672598097674": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1431410709184163383": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8143151571822735378": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8764477339709428922": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1819475130880826595": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-836142453898439357": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-614648394699724109": {
            "type": "constant",
            "sample": 0.25,
        },
        "3907669375390279207": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1434534914485752211": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6105429063393446070": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6816321110330207100": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8312649044874766647": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "265859392736356296": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6217928649742894246": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4688851446087459089": {
            "type": "constant",
            "sample": 0.25,
        },
        "7422755385923996732": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1158873943260837652": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4797845918936726161": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2918285382552219836": {
            "type": "constant",
            "sample": 0.25,
        },
        "2963612118141187368": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7277602666341372469": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7554797069757374683": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8097489186127400571": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7875995126928685323": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "996186665773967532": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4346017624102063886": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2476193233489737694": {
            "type": "constant",
            "sample": 0.25,
        },
        "-445025621898754114": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8427156170803898741": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7483309263912235451": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7704803323110950699": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1869758957895948062": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7207437942329892343": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8420220675489798866": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "74537870444222326_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "74537870444222326_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5412162721485354109_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5412162721485354109_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7319327388012021960_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7319327388012021960_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "379645671249606667_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "379645671249606667_q": {
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
        "B3/acquisition_mixer_cdf": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_e75": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_e84": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_11c": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_3e6": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_674": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e25": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_611": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

