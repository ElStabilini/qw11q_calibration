
# Single QUA script generated at 2025-02-16 08:12:06.283857
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
        play("5306296781589065929", "B1/drive")
        wait(11, "B1/flux")
        play("-1301237734329662651", "B1/flux")
        wait(46, "B1/drive")
        play("6067387410812627798", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-4113404676282318805", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        r1 = declare_stream()
        save(v4, r1)
        play("3847979270505151354", "B2/drive")
        wait(11, "B2/flux")
        play("-1301237734329662651", "B2/flux")
        wait(46, "B2/drive")
        play("9007427282713081351", "B2/drive")
        wait(66, "B2/acquisition")
        measure("381480545922948246", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        r2 = declare_stream()
        save(v7, r2)
        play("-2296237070904119362", "B3/drive")
        wait(11, "B3/flux")
        play("-1301237734329662651", "B3/flux")
        wait(46, "B3/drive")
        play("-8581175730315414318", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-5577647268963356641", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        r3 = declare_stream()
        save(v10, r3)
        play("832578182584705562", "B4/drive")
        wait(11, "B4/flux")
        play("-1301237734329662651", "B4/flux")
        wait(46, "B4/drive")
        play("1593668811808267431", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1154509030118257397", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B2/drive")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25001, "B4/acquisition")
        wait(25536, "B2/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        play("5306296781589065929", "B1/drive")
        wait(11, "B1/flux")
        play("9090373059485229810", "B1/flux")
        wait(46, "B1/drive")
        play("6067387410812627798", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-4113404676282318805", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        save(v4, r1)
        play("3847979270505151354", "B2/drive")
        wait(11, "B2/flux")
        play("9090373059485229810", "B2/flux")
        wait(46, "B2/drive")
        play("9007427282713081351", "B2/drive")
        wait(66, "B2/acquisition")
        measure("381480545922948246", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        save(v7, r2)
        play("-2296237070904119362", "B3/drive")
        wait(11, "B3/flux")
        play("9090373059485229810", "B3/flux")
        wait(46, "B3/drive")
        play("-8581175730315414318", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-5577647268963356641", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        save(v10, r3)
        play("832578182584705562", "B4/drive")
        wait(11, "B4/flux")
        play("9090373059485229810", "B4/flux")
        wait(46, "B4/drive")
        play("1593668811808267431", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1154509030118257397", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        save(v13, r4)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B2/drive")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25001, "B4/acquisition")
        wait(25536, "B2/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-4113404676282318805_B1|acquisition_shots")
        r2.buffer(2).average().save("381480545922948246_B2|acquisition_shots")
        r3.buffer(2).average().save("-5577647268963356641_B3|acquisition_shots")
        r4.buffer(2).average().save("1154509030118257397_B4|acquisition_shots")


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
    },
    "octaves": {
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
    },
    "elements": {
        "B1/flux": {
            "singleInput": {
                "port": ('con4', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
            "intermediate_frequency": 109615374.0,
            "operations": {
                "832578182584705562": "832578182584705562",
                "1593668811808267431": "1593668811808267431",
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
                "5306296781589065929": "5306296781589065929",
                "6067387410812627798": "6067387410812627798",
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
                "-4113404676282318805": "-4113404676282318805_B1/acquisition",
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
                "3847979270505151354": "3847979270505151354",
                "9007427282713081351": "9007427282713081351",
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
                "-5577647268963356641": "-5577647268963356641_B3/acquisition",
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
                "1154509030118257397": "1154509030118257397_B4/acquisition",
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
                "381480545922948246": "381480545922948246_B2/acquisition",
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
                "-2296237070904119362": "-2296237070904119362",
                "-8581175730315414318": "-8581175730315414318",
            },
        },
    },
    "pulses": {
        "5306296781589065929": {
            "length": 40,
            "waveforms": {
                "I": "5306296781589065929_i",
                "Q": "5306296781589065929_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7164749374838275572": {
            "length": 16,
            "waveforms": {
                "single": "7164749374838275572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4113404676282318805_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8516773093374630164_i",
                "Q": "-8516773093374630164_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3847979270505151354": {
            "length": 40,
            "waveforms": {
                "I": "3847979270505151354_i",
                "Q": "3847979270505151354_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "381480545922948246_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-328798012492020647_i",
                "Q": "-328798012492020647_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-2296237070904119362": {
            "length": 40,
            "waveforms": {
                "I": "-2296237070904119362_i",
                "Q": "-2296237070904119362_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5577647268963356641_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4546697736821645720_i",
                "Q": "4546697736821645720_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "832578182584705562": {
            "length": 40,
            "waveforms": {
                "I": "832578182584705562_i",
                "Q": "832578182584705562_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1154509030118257397_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7553887711688373256_i",
                "Q": "7553887711688373256_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "7386243434036990820": {
            "length": 16,
            "waveforms": {
                "single": "7386243434036990820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5061685351950154367": {
            "length": 16,
            "waveforms": {
                "single": "5061685351950154367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5185645739055789555": {
            "length": 16,
            "waveforms": {
                "single": "5185645739055789555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5055569045426770282": {
            "length": 16,
            "waveforms": {
                "single": "-5055569045426770282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3629531134642629587": {
            "length": 16,
            "waveforms": {
                "single": "-3629531134642629587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "177640771599994064": {
            "length": 16,
            "waveforms": {
                "single": "177640771599994064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1431771446639462724": {
            "length": 16,
            "waveforms": {
                "single": "-1431771446639462724",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8182494498386125072": {
            "length": 16,
            "waveforms": {
                "single": "-8182494498386125072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2596894518801876175": {
            "length": 16,
            "waveforms": {
                "single": "2596894518801876175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5596956587009849423": {
            "length": 16,
            "waveforms": {
                "single": "-5596956587009849423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7921514669096685876": {
            "length": 16,
            "waveforms": {
                "single": "-7921514669096685876",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6220692117589183733": {
            "length": 16,
            "waveforms": {
                "single": "6220692117589183733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3868326448826889513": {
            "length": 16,
            "waveforms": {
                "single": "3868326448826889513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8197385990679028984": {
            "length": 16,
            "waveforms": {
                "single": "-8197385990679028984",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5378300534789168577": {
            "length": 16,
            "waveforms": {
                "single": "-5378300534789168577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-269051104868039419": {
            "length": 20,
            "waveforms": {
                "single": "-269051104868039419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4253266665221963897": {
            "length": 20,
            "waveforms": {
                "single": "4253266665221963897",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4474760724420679145": {
            "length": 20,
            "waveforms": {
                "single": "4474760724420679145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6451026353225130760": {
            "length": 20,
            "waveforms": {
                "single": "6451026353225130760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6672520412423846008": {
            "length": 24,
            "waveforms": {
                "single": "6672520412423846008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7383412459360607038": {
            "length": 24,
            "waveforms": {
                "single": "7383412459360607038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6541013844258941262": {
            "length": 24,
            "waveforms": {
                "single": "-6541013844258941262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-976722810625512098": {
            "length": 24,
            "waveforms": {
                "single": "-976722810625512098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4343254156255774399": {
            "length": 28,
            "waveforms": {
                "single": "-4343254156255774399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4121760097057059151": {
            "length": 28,
            "waveforms": {
                "single": "-4121760097057059151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "889955660770989947": {
            "length": 28,
            "waveforms": {
                "single": "889955660770989947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1111449719969705195": {
            "length": 28,
            "waveforms": {
                "single": "1111449719969705195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4028068847952645662": {
            "length": 32,
            "waveforms": {
                "single": "4028068847952645662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3309209407972872058": {
            "length": 32,
            "waveforms": {
                "single": "3309209407972872058",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "956843739210577838": {
            "length": 32,
            "waveforms": {
                "single": "956843739210577838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5894747319349147707": {
            "length": 32,
            "waveforms": {
                "single": "5894747319349147707",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6987705720726974745": {
            "length": 36,
            "waveforms": {
                "single": "-6987705720726974745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3180533814484351094": {
            "length": 36,
            "waveforms": {
                "single": "-3180533814484351094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7485071101508033101": {
            "length": 36,
            "waveforms": {
                "single": "-7485071101508033101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8609307303439224295": {
            "length": 36,
            "waveforms": {
                "single": "8609307303439224295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1286083611388365256": {
            "length": 40,
            "waveforms": {
                "single": "1286083611388365256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1909101884459337756": {
            "length": 40,
            "waveforms": {
                "single": "-1909101884459337756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5187075613591675028": {
            "length": 40,
            "waveforms": {
                "single": "5187075613591675028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8994247519834298679": {
            "length": 40,
            "waveforms": {
                "single": "8994247519834298679",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "510151862742544355": {
            "length": 44,
            "waveforms": {
                "single": "510151862742544355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7254736865872086074": {
            "length": 44,
            "waveforms": {
                "single": "-7254736865872086074",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1302667608865548124": {
            "length": 44,
            "waveforms": {
                "single": "-1302667608865548124",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2376830334139046400": {
            "length": 44,
            "waveforms": {
                "single": "2376830334139046400",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "895092079137618739": {
            "length": 48,
            "waveforms": {
                "single": "895092079137618739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5983304935847072736": {
            "length": 48,
            "waveforms": {
                "single": "-5983304935847072736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "397726698356560383": {
            "length": 48,
            "waveforms": {
                "single": "397726698356560383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6349795955363098333": {
            "length": 48,
            "waveforms": {
                "single": "6349795955363098333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2231833373821736051": {
            "length": 52,
            "waveforms": {
                "single": "-2231833373821736051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8547555643366265196": {
            "length": 52,
            "waveforms": {
                "single": "8547555643366265196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5376870660253283104": {
            "length": 52,
            "waveforms": {
                "single": "-5376870660253283104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-267621230332153946": {
            "length": 52,
            "waveforms": {
                "single": "-267621230332153946",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-143660843226518758": {
            "length": 56,
            "waveforms": {
                "single": "-143660843226518758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8627756500318273082": {
            "length": 56,
            "waveforms": {
                "single": "-8627756500318273082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2246724866114639963": {
            "length": 56,
            "waveforms": {
                "single": "-2246724866114639963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2275592903975363353": {
            "length": 56,
            "waveforms": {
                "single": "2275592903975363353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7384842333896492511": {
            "length": 60,
            "waveforms": {
                "single": "7384842333896492511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8242816283923198698": {
            "length": 60,
            "waveforms": {
                "single": "-8242816283923198698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8021322224724483450": {
            "length": 60,
            "waveforms": {
                "single": "-8021322224724483450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2831878970152997026": {
            "length": 60,
            "waveforms": {
                "single": "2831878970152997026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4120330222521173678": {
            "length": 64,
            "waveforms": {
                "single": "-4120330222521173678",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5029638658156163889": {
            "length": 64,
            "waveforms": {
                "single": "5029638658156163889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-590352719694552241": {
            "length": 64,
            "waveforms": {
                "single": "-590352719694552241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7615176569532439538": {
            "length": 64,
            "waveforms": {
                "single": "7615176569532439538",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3310639282508757531": {
            "length": 68,
            "waveforms": {
                "single": "3310639282508757531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1828901027507329870": {
            "length": 68,
            "waveforms": {
                "single": "1828901027507329870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5636072933749953521": {
            "length": 68,
            "waveforms": {
                "single": "5636072933749953521",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1242324081234737954": {
            "length": 68,
            "waveforms": {
                "single": "-1242324081234737954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3179103939948465621": {
            "length": 72,
            "waveforms": {
                "single": "-3179103939948465621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9186873541172290537": {
            "length": 72,
            "waveforms": {
                "single": "-9186873541172290537",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6907504863774966859": {
            "length": 72,
            "waveforms": {
                "single": "6907504863774966859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "444693658838841937": {
            "length": 72,
            "waveforms": {
                "single": "444693658838841937",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3762467577343419806": {
            "length": 76,
            "waveforms": {
                "single": "3762467577343419806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2960447887727784775": {
            "length": 76,
            "waveforms": {
                "single": "-2960447887727784775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4108269704904653548": {
            "length": 76,
            "waveforms": {
                "single": "-4108269704904653548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3886775645705938300": {
            "length": 76,
            "waveforms": {
                "single": "-3886775645705938300",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7253306991336200601": {
            "length": 80,
            "waveforms": {
                "single": "-7253306991336200601",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1301237734329662651": {
            "length": 80,
            "waveforms": {
                "single": "-1301237734329662651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9090373059485229810": {
            "length": 80,
            "waveforms": {
                "single": "9090373059485229810",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6067387410812627798": {
            "length": 40,
            "waveforms": {
                "I": "6067387410812627798_i",
                "Q": "6067387410812627798_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9007427282713081351": {
            "length": 40,
            "waveforms": {
                "I": "9007427282713081351_i",
                "Q": "9007427282713081351_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8581175730315414318": {
            "length": 40,
            "waveforms": {
                "I": "-8581175730315414318_i",
                "Q": "-8581175730315414318_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1593668811808267431": {
            "length": 40,
            "waveforms": {
                "I": "1593668811808267431_i",
                "Q": "1593668811808267431_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5306296781589065929_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "5306296781589065929_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "7164749374838275572": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-8516773093374630164_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-8516773093374630164_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3847979270505151354_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "3847979270505151354_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-328798012492020647_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-328798012492020647_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2296237070904119362_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-2296237070904119362_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "4546697736821645720_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "4546697736821645720_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "832578182584705562_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "832578182584705562_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "7553887711688373256_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "7553887711688373256_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7386243434036990820": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "5061685351950154367": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "5185645739055789555": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5055569045426770282": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-3629531134642629587": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "177640771599994064": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-1431771446639462724": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8182494498386125072": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "2596894518801876175": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-5596956587009849423": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-7921514669096685876": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "6220692117589183733": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3868326448826889513": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8197385990679028984": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-5378300534789168577": {
            "sample": 0.25,
            "type": "constant",
        },
        "-269051104868039419": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4253266665221963897": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4474760724420679145": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6451026353225130760": {
            "sample": 0.25,
            "type": "constant",
        },
        "6672520412423846008": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7383412459360607038": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6541013844258941262": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-976722810625512098": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4343254156255774399": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4121760097057059151": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "889955660770989947": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1111449719969705195": {
            "sample": 0.25,
            "type": "constant",
        },
        "4028068847952645662": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3309209407972872058": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "956843739210577838": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "5894747319349147707": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6987705720726974745": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3180533814484351094": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7485071101508033101": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "8609307303439224295": {
            "sample": 0.25,
            "type": "constant",
        },
        "1286083611388365256": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1909101884459337756": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5187075613591675028": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "8994247519834298679": {
            "sample": 0.25,
            "type": "constant",
        },
        "510151862742544355": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7254736865872086074": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1302667608865548124": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "2376830334139046400": {
            "sample": 0.25,
            "type": "constant",
        },
        "895092079137618739": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5983304935847072736": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "397726698356560383": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "6349795955363098333": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2231833373821736051": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8547555643366265196": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5376870660253283104": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-267621230332153946": {
            "sample": 0.25,
            "type": "constant",
        },
        "-143660843226518758": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8627756500318273082": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2246724866114639963": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "2275592903975363353": {
            "sample": 0.25,
            "type": "constant",
        },
        "7384842333896492511": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8242816283923198698": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8021322224724483450": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "2831878970152997026": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4120330222521173678": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5029638658156163889": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-590352719694552241": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "7615176569532439538": {
            "sample": 0.25,
            "type": "constant",
        },
        "3310639282508757531": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1828901027507329870": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5636072933749953521": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-1242324081234737954": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3179103939948465621": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9186873541172290537": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6907504863774966859": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "444693658838841937": {
            "sample": 0.25,
            "type": "constant",
        },
        "3762467577343419806": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2960447887727784775": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4108269704904653548": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-3886775645705938300": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7253306991336200601": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1301237734329662651": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9090373059485229810": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "6067387410812627798_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "6067387410812627798_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "9007427282713081351_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "9007427282713081351_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-8581175730315414318_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-8581175730315414318_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "1593668811808267431_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "1593668811808267431_q": {
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
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "-1301237734329662651": "-1301237734329662651",
                "9090373059485229810": "9090373059485229810",
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
                "832578182584705562": "832578182584705562",
                "1593668811808267431": "1593668811808267431",
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
                "mixer": "B4/drive_mixer_7bf",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "5306296781589065929": "5306296781589065929",
                "6067387410812627798": "6067387410812627798",
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
                "mixer": "B1/drive_mixer_4a0",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-4113404676282318805": "-4113404676282318805_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_fc6",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "3847979270505151354": "3847979270505151354",
                "9007427282713081351": "9007427282713081351",
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
                "mixer": "B2/drive_mixer_1ea",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-5577647268963356641": "-5577647268963356641_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_2a7",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "1154509030118257397": "1154509030118257397_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_04e",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "381480545922948246": "381480545922948246_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_daf",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-2296237070904119362": "-2296237070904119362",
                "-8581175730315414318": "-8581175730315414318",
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
                "mixer": "B3/drive_mixer_61f",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
    },
    "pulses": {
        "5306296781589065929": {
            "length": 40,
            "waveforms": {
                "I": "5306296781589065929_i",
                "Q": "5306296781589065929_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7164749374838275572": {
            "length": 16,
            "waveforms": {
                "single": "7164749374838275572",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4113404676282318805_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8516773093374630164_i",
                "Q": "-8516773093374630164_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3847979270505151354": {
            "length": 40,
            "waveforms": {
                "I": "3847979270505151354_i",
                "Q": "3847979270505151354_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "381480545922948246_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-328798012492020647_i",
                "Q": "-328798012492020647_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2296237070904119362": {
            "length": 40,
            "waveforms": {
                "I": "-2296237070904119362_i",
                "Q": "-2296237070904119362_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5577647268963356641_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4546697736821645720_i",
                "Q": "4546697736821645720_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "832578182584705562": {
            "length": 40,
            "waveforms": {
                "I": "832578182584705562_i",
                "Q": "832578182584705562_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1154509030118257397_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7553887711688373256_i",
                "Q": "7553887711688373256_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7386243434036990820": {
            "length": 16,
            "waveforms": {
                "single": "7386243434036990820",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5061685351950154367": {
            "length": 16,
            "waveforms": {
                "single": "5061685351950154367",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5185645739055789555": {
            "length": 16,
            "waveforms": {
                "single": "5185645739055789555",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5055569045426770282": {
            "length": 16,
            "waveforms": {
                "single": "-5055569045426770282",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3629531134642629587": {
            "length": 16,
            "waveforms": {
                "single": "-3629531134642629587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "177640771599994064": {
            "length": 16,
            "waveforms": {
                "single": "177640771599994064",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1431771446639462724": {
            "length": 16,
            "waveforms": {
                "single": "-1431771446639462724",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8182494498386125072": {
            "length": 16,
            "waveforms": {
                "single": "-8182494498386125072",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2596894518801876175": {
            "length": 16,
            "waveforms": {
                "single": "2596894518801876175",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5596956587009849423": {
            "length": 16,
            "waveforms": {
                "single": "-5596956587009849423",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7921514669096685876": {
            "length": 16,
            "waveforms": {
                "single": "-7921514669096685876",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6220692117589183733": {
            "length": 16,
            "waveforms": {
                "single": "6220692117589183733",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3868326448826889513": {
            "length": 16,
            "waveforms": {
                "single": "3868326448826889513",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8197385990679028984": {
            "length": 16,
            "waveforms": {
                "single": "-8197385990679028984",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5378300534789168577": {
            "length": 16,
            "waveforms": {
                "single": "-5378300534789168577",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-269051104868039419": {
            "length": 20,
            "waveforms": {
                "single": "-269051104868039419",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4253266665221963897": {
            "length": 20,
            "waveforms": {
                "single": "4253266665221963897",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4474760724420679145": {
            "length": 20,
            "waveforms": {
                "single": "4474760724420679145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6451026353225130760": {
            "length": 20,
            "waveforms": {
                "single": "6451026353225130760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6672520412423846008": {
            "length": 24,
            "waveforms": {
                "single": "6672520412423846008",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7383412459360607038": {
            "length": 24,
            "waveforms": {
                "single": "7383412459360607038",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6541013844258941262": {
            "length": 24,
            "waveforms": {
                "single": "-6541013844258941262",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-976722810625512098": {
            "length": 24,
            "waveforms": {
                "single": "-976722810625512098",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4343254156255774399": {
            "length": 28,
            "waveforms": {
                "single": "-4343254156255774399",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4121760097057059151": {
            "length": 28,
            "waveforms": {
                "single": "-4121760097057059151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "889955660770989947": {
            "length": 28,
            "waveforms": {
                "single": "889955660770989947",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1111449719969705195": {
            "length": 28,
            "waveforms": {
                "single": "1111449719969705195",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4028068847952645662": {
            "length": 32,
            "waveforms": {
                "single": "4028068847952645662",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3309209407972872058": {
            "length": 32,
            "waveforms": {
                "single": "3309209407972872058",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "956843739210577838": {
            "length": 32,
            "waveforms": {
                "single": "956843739210577838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5894747319349147707": {
            "length": 32,
            "waveforms": {
                "single": "5894747319349147707",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6987705720726974745": {
            "length": 36,
            "waveforms": {
                "single": "-6987705720726974745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3180533814484351094": {
            "length": 36,
            "waveforms": {
                "single": "-3180533814484351094",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7485071101508033101": {
            "length": 36,
            "waveforms": {
                "single": "-7485071101508033101",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8609307303439224295": {
            "length": 36,
            "waveforms": {
                "single": "8609307303439224295",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1286083611388365256": {
            "length": 40,
            "waveforms": {
                "single": "1286083611388365256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1909101884459337756": {
            "length": 40,
            "waveforms": {
                "single": "-1909101884459337756",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5187075613591675028": {
            "length": 40,
            "waveforms": {
                "single": "5187075613591675028",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8994247519834298679": {
            "length": 40,
            "waveforms": {
                "single": "8994247519834298679",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "510151862742544355": {
            "length": 44,
            "waveforms": {
                "single": "510151862742544355",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7254736865872086074": {
            "length": 44,
            "waveforms": {
                "single": "-7254736865872086074",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1302667608865548124": {
            "length": 44,
            "waveforms": {
                "single": "-1302667608865548124",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2376830334139046400": {
            "length": 44,
            "waveforms": {
                "single": "2376830334139046400",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "895092079137618739": {
            "length": 48,
            "waveforms": {
                "single": "895092079137618739",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5983304935847072736": {
            "length": 48,
            "waveforms": {
                "single": "-5983304935847072736",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "397726698356560383": {
            "length": 48,
            "waveforms": {
                "single": "397726698356560383",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6349795955363098333": {
            "length": 48,
            "waveforms": {
                "single": "6349795955363098333",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2231833373821736051": {
            "length": 52,
            "waveforms": {
                "single": "-2231833373821736051",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8547555643366265196": {
            "length": 52,
            "waveforms": {
                "single": "8547555643366265196",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5376870660253283104": {
            "length": 52,
            "waveforms": {
                "single": "-5376870660253283104",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-267621230332153946": {
            "length": 52,
            "waveforms": {
                "single": "-267621230332153946",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-143660843226518758": {
            "length": 56,
            "waveforms": {
                "single": "-143660843226518758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8627756500318273082": {
            "length": 56,
            "waveforms": {
                "single": "-8627756500318273082",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2246724866114639963": {
            "length": 56,
            "waveforms": {
                "single": "-2246724866114639963",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2275592903975363353": {
            "length": 56,
            "waveforms": {
                "single": "2275592903975363353",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7384842333896492511": {
            "length": 60,
            "waveforms": {
                "single": "7384842333896492511",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8242816283923198698": {
            "length": 60,
            "waveforms": {
                "single": "-8242816283923198698",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8021322224724483450": {
            "length": 60,
            "waveforms": {
                "single": "-8021322224724483450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2831878970152997026": {
            "length": 60,
            "waveforms": {
                "single": "2831878970152997026",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4120330222521173678": {
            "length": 64,
            "waveforms": {
                "single": "-4120330222521173678",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5029638658156163889": {
            "length": 64,
            "waveforms": {
                "single": "5029638658156163889",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-590352719694552241": {
            "length": 64,
            "waveforms": {
                "single": "-590352719694552241",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7615176569532439538": {
            "length": 64,
            "waveforms": {
                "single": "7615176569532439538",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3310639282508757531": {
            "length": 68,
            "waveforms": {
                "single": "3310639282508757531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1828901027507329870": {
            "length": 68,
            "waveforms": {
                "single": "1828901027507329870",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5636072933749953521": {
            "length": 68,
            "waveforms": {
                "single": "5636072933749953521",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1242324081234737954": {
            "length": 68,
            "waveforms": {
                "single": "-1242324081234737954",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3179103939948465621": {
            "length": 72,
            "waveforms": {
                "single": "-3179103939948465621",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9186873541172290537": {
            "length": 72,
            "waveforms": {
                "single": "-9186873541172290537",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6907504863774966859": {
            "length": 72,
            "waveforms": {
                "single": "6907504863774966859",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "444693658838841937": {
            "length": 72,
            "waveforms": {
                "single": "444693658838841937",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3762467577343419806": {
            "length": 76,
            "waveforms": {
                "single": "3762467577343419806",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2960447887727784775": {
            "length": 76,
            "waveforms": {
                "single": "-2960447887727784775",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4108269704904653548": {
            "length": 76,
            "waveforms": {
                "single": "-4108269704904653548",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3886775645705938300": {
            "length": 76,
            "waveforms": {
                "single": "-3886775645705938300",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7253306991336200601": {
            "length": 80,
            "waveforms": {
                "single": "-7253306991336200601",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1301237734329662651": {
            "length": 80,
            "waveforms": {
                "single": "-1301237734329662651",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9090373059485229810": {
            "length": 80,
            "waveforms": {
                "single": "9090373059485229810",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6067387410812627798": {
            "length": 40,
            "waveforms": {
                "I": "6067387410812627798_i",
                "Q": "6067387410812627798_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9007427282713081351": {
            "length": 40,
            "waveforms": {
                "I": "9007427282713081351_i",
                "Q": "9007427282713081351_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8581175730315414318": {
            "length": 40,
            "waveforms": {
                "I": "-8581175730315414318_i",
                "Q": "-8581175730315414318_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1593668811808267431": {
            "length": 40,
            "waveforms": {
                "I": "1593668811808267431_i",
                "Q": "1593668811808267431_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "5306296781589065929_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5306296781589065929_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7164749374838275572": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8516773093374630164_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-8516773093374630164_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3847979270505151354_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3847979270505151354_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-328798012492020647_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-328798012492020647_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2296237070904119362_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2296237070904119362_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4546697736821645720_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "4546697736821645720_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "832578182584705562_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "832578182584705562_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7553887711688373256_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "7553887711688373256_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7386243434036990820": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5061685351950154367": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5185645739055789555": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5055569045426770282": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3629531134642629587": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "177640771599994064": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1431771446639462724": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8182494498386125072": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2596894518801876175": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5596956587009849423": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7921514669096685876": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6220692117589183733": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3868326448826889513": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8197385990679028984": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5378300534789168577": {
            "type": "constant",
            "sample": 0.25,
        },
        "-269051104868039419": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4253266665221963897": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4474760724420679145": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6451026353225130760": {
            "type": "constant",
            "sample": 0.25,
        },
        "6672520412423846008": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7383412459360607038": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6541013844258941262": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-976722810625512098": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4343254156255774399": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4121760097057059151": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "889955660770989947": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1111449719969705195": {
            "type": "constant",
            "sample": 0.25,
        },
        "4028068847952645662": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3309209407972872058": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "956843739210577838": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5894747319349147707": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6987705720726974745": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3180533814484351094": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7485071101508033101": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8609307303439224295": {
            "type": "constant",
            "sample": 0.25,
        },
        "1286083611388365256": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1909101884459337756": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5187075613591675028": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8994247519834298679": {
            "type": "constant",
            "sample": 0.25,
        },
        "510151862742544355": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7254736865872086074": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1302667608865548124": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2376830334139046400": {
            "type": "constant",
            "sample": 0.25,
        },
        "895092079137618739": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5983304935847072736": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "397726698356560383": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6349795955363098333": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2231833373821736051": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8547555643366265196": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5376870660253283104": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-267621230332153946": {
            "type": "constant",
            "sample": 0.25,
        },
        "-143660843226518758": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8627756500318273082": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2246724866114639963": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2275592903975363353": {
            "type": "constant",
            "sample": 0.25,
        },
        "7384842333896492511": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8242816283923198698": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8021322224724483450": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2831878970152997026": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4120330222521173678": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5029638658156163889": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-590352719694552241": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7615176569532439538": {
            "type": "constant",
            "sample": 0.25,
        },
        "3310639282508757531": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1828901027507329870": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5636072933749953521": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1242324081234737954": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3179103939948465621": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9186873541172290537": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6907504863774966859": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "444693658838841937": {
            "type": "constant",
            "sample": 0.25,
        },
        "3762467577343419806": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2960447887727784775": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4108269704904653548": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3886775645705938300": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7253306991336200601": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1301237734329662651": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9090373059485229810": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6067387410812627798_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6067387410812627798_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9007427282713081351_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9007427282713081351_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8581175730315414318_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8581175730315414318_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1593668811808267431_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1593668811808267431_q": {
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
        "B4/drive_mixer_7bf": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_4a0": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_fc6": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_1ea": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_2a7": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_04e": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_daf": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_61f": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

