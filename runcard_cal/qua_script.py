
# Single QUA script generated at 2025-01-16 18:02:48.317843
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
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("3156537187182049586", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-3006964711487707951", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-8644130658994366847", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-6641055880276876591", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-6189706011665842524", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-6910451042641001121", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("5130283345921138476", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("4511180424104023973", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-769121735380718368", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("7753513100815522267", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("3663775962863379232", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-5090218847060725109", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("2915794005675956746", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-961675388024279594", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("4824670335971508242", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-2998786616390532222", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-3152942340854612480", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("-8736235562549571685", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("5768984935637455340", "B4/drive")
        wait(11, "B4/flux")
        play("5577879488735641037", "B4/flux")
        wait(46, "B4/drive")
        play("6530075564861017209", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4853314269389355911", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-4853314269389355911_B4|acquisition_shots")


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
                "3156537187182049586": "3156537187182049586",
                "-3006964711487707951": "-3006964711487707951",
                "-8644130658994366847": "-8644130658994366847",
                "-6641055880276876591": "-6641055880276876591",
                "-6189706011665842524": "-6189706011665842524",
                "-6910451042641001121": "-6910451042641001121",
                "5130283345921138476": "5130283345921138476",
                "4511180424104023973": "4511180424104023973",
                "-769121735380718368": "-769121735380718368",
                "7753513100815522267": "7753513100815522267",
                "3663775962863379232": "3663775962863379232",
                "-5090218847060725109": "-5090218847060725109",
                "2915794005675956746": "2915794005675956746",
                "-961675388024279594": "-961675388024279594",
                "4824670335971508242": "4824670335971508242",
                "-2998786616390532222": "-2998786616390532222",
                "-3152942340854612480": "-3152942340854612480",
                "-8736235562549571685": "-8736235562549571685",
                "5577879488735641037": "5577879488735641037",
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
                "5768984935637455340": "5768984935637455340",
                "6530075564861017209": "6530075564861017209",
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
                "-4853314269389355911": "-4853314269389355911_B4/acquisition",
            },
        },
    },
    "pulses": {
        "5768984935637455340": {
            "length": 40,
            "waveforms": {
                "I": "5768984935637455340_i",
                "Q": "5768984935637455340_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1894624465798050520": {
            "length": 16,
            "waveforms": {
                "single": "-1894624465798050520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4853314269389355911_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3111256994499612400_i",
                "Q": "3111256994499612400_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-8905611921397003541": {
            "length": 16,
            "waveforms": {
                "single": "-8905611921397003541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3948932196926256474": {
            "length": 16,
            "waveforms": {
                "single": "3948932196926256474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2392626175211919587": {
            "length": 16,
            "waveforms": {
                "single": "-2392626175211919587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8912907796944588464": {
            "length": 16,
            "waveforms": {
                "single": "-8912907796944588464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8705805477324620638": {
            "length": 16,
            "waveforms": {
                "single": "8705805477324620638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2171663417922936030": {
            "length": 16,
            "waveforms": {
                "single": "-2171663417922936030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "639513639873253775": {
            "length": 16,
            "waveforms": {
                "single": "639513639873253775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2261954252634175992": {
            "length": 16,
            "waveforms": {
                "single": "2261954252634175992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1529292652562975756": {
            "length": 16,
            "waveforms": {
                "single": "-1529292652562975756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5931024266079283349": {
            "length": 16,
            "waveforms": {
                "single": "-5931024266079283349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1758236855566439260": {
            "length": 16,
            "waveforms": {
                "single": "1758236855566439260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4811580070983064894": {
            "length": 16,
            "waveforms": {
                "single": "4811580070983064894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-582965775796792609": {
            "length": 16,
            "waveforms": {
                "single": "-582965775796792609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7913931117279680775": {
            "length": 16,
            "waveforms": {
                "single": "-7913931117279680775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7485788586787290790": {
            "length": 16,
            "waveforms": {
                "single": "7485788586787290790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8451652854074328113": {
            "length": 20,
            "waveforms": {
                "single": "-8451652854074328113",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4127475510279854921": {
            "length": 20,
            "waveforms": {
                "single": "4127475510279854921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6657776858694524933": {
            "length": 20,
            "waveforms": {
                "single": "-6657776858694524933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1821707190996781634": {
            "length": 20,
            "waveforms": {
                "single": "1821707190996781634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8793261206792041533": {
            "length": 24,
            "waveforms": {
                "single": "8793261206792041533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "149547951838695764": {
            "length": 24,
            "waveforms": {
                "single": "149547951838695764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3249594470613168163": {
            "length": 24,
            "waveforms": {
                "single": "-3249594470613168163",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-474409651410814366": {
            "length": 24,
            "waveforms": {
                "single": "-474409651410814366",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3202461600531702189": {
            "length": 28,
            "waveforms": {
                "single": "3202461600531702189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6792931611002674823": {
            "length": 28,
            "waveforms": {
                "single": "-6792931611002674823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4942970502713269017": {
            "length": 28,
            "waveforms": {
                "single": "-4942970502713269017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1776764749347898693": {
            "length": 28,
            "waveforms": {
                "single": "-1776764749347898693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8350580332288086722": {
            "length": 32,
            "waveforms": {
                "single": "-8350580332288086722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-239997002764588087": {
            "length": 32,
            "waveforms": {
                "single": "-239997002764588087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7964278730132437752": {
            "length": 32,
            "waveforms": {
                "single": "7964278730132437752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4468399919177942688": {
            "length": 32,
            "waveforms": {
                "single": "-4468399919177942688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-218476210012461883": {
            "length": 36,
            "waveforms": {
                "single": "-218476210012461883",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9035515965810224838": {
            "length": 36,
            "waveforms": {
                "single": "-9035515965810224838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6087552347148650472": {
            "length": 36,
            "waveforms": {
                "single": "-6087552347148650472",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9161239723667284581": {
            "length": 36,
            "waveforms": {
                "single": "-9161239723667284581",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "989567022953791873": {
            "length": 40,
            "waveforms": {
                "single": "989567022953791873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4944148193040397083": {
            "length": 40,
            "waveforms": {
                "single": "-4944148193040397083",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4101389175827130184": {
            "length": 40,
            "waveforms": {
                "single": "-4101389175827130184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8557299167751876859": {
            "length": 40,
            "waveforms": {
                "single": "-8557299167751876859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8990894448998286000": {
            "length": 44,
            "waveforms": {
                "single": "-8990894448998286000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2553960296845298351": {
            "length": 44,
            "waveforms": {
                "single": "-2553960296845298351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-35886269242960186": {
            "length": 44,
            "waveforms": {
                "single": "-35886269242960186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2857506449220518873": {
            "length": 44,
            "waveforms": {
                "single": "-2857506449220518873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1546248089306994470": {
            "length": 48,
            "waveforms": {
                "single": "1546248089306994470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6473401833186242911": {
            "length": 48,
            "waveforms": {
                "single": "6473401833186242911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5287013475055139759": {
            "length": 48,
            "waveforms": {
                "single": "5287013475055139759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "471902259270851268": {
            "length": 48,
            "waveforms": {
                "single": "471902259270851268",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2850379103610640311": {
            "length": 52,
            "waveforms": {
                "single": "2850379103610640311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2075321820283126993": {
            "length": 52,
            "waveforms": {
                "single": "2075321820283126993",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4644837052496854747": {
            "length": 52,
            "waveforms": {
                "single": "-4644837052496854747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9138080126313010958": {
            "length": 52,
            "waveforms": {
                "single": "9138080126313010958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1889232698674416720": {
            "length": 56,
            "waveforms": {
                "single": "-1889232698674416720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6018248492196121883": {
            "length": 56,
            "waveforms": {
                "single": "-6018248492196121883",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "230115908245255764": {
            "length": 56,
            "waveforms": {
                "single": "230115908245255764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3389691347575590706": {
            "length": 56,
            "waveforms": {
                "single": "-3389691347575590706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6228851645577224214": {
            "length": 60,
            "waveforms": {
                "single": "-6228851645577224214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2141018351744030551": {
            "length": 60,
            "waveforms": {
                "single": "2141018351744030551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6669018619016968039": {
            "length": 60,
            "waveforms": {
                "single": "-6669018619016968039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7573389716891963722": {
            "length": 60,
            "waveforms": {
                "single": "-7573389716891963722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3156537187182049586": {
            "length": 64,
            "waveforms": {
                "single": "3156537187182049586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3006964711487707951": {
            "length": 64,
            "waveforms": {
                "single": "-3006964711487707951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8644130658994366847": {
            "length": 64,
            "waveforms": {
                "single": "-8644130658994366847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6641055880276876591": {
            "length": 64,
            "waveforms": {
                "single": "-6641055880276876591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6189706011665842524": {
            "length": 68,
            "waveforms": {
                "single": "-6189706011665842524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6910451042641001121": {
            "length": 68,
            "waveforms": {
                "single": "-6910451042641001121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5130283345921138476": {
            "length": 68,
            "waveforms": {
                "single": "5130283345921138476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4511180424104023973": {
            "length": 68,
            "waveforms": {
                "single": "4511180424104023973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-769121735380718368": {
            "length": 72,
            "waveforms": {
                "single": "-769121735380718368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7753513100815522267": {
            "length": 72,
            "waveforms": {
                "single": "7753513100815522267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3663775962863379232": {
            "length": 72,
            "waveforms": {
                "single": "3663775962863379232",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5090218847060725109": {
            "length": 72,
            "waveforms": {
                "single": "-5090218847060725109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2915794005675956746": {
            "length": 76,
            "waveforms": {
                "single": "2915794005675956746",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961675388024279594": {
            "length": 76,
            "waveforms": {
                "single": "-961675388024279594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4824670335971508242": {
            "length": 76,
            "waveforms": {
                "single": "4824670335971508242",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2998786616390532222": {
            "length": 76,
            "waveforms": {
                "single": "-2998786616390532222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3152942340854612480": {
            "length": 80,
            "waveforms": {
                "single": "-3152942340854612480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8736235562549571685": {
            "length": 80,
            "waveforms": {
                "single": "-8736235562549571685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5577879488735641037": {
            "length": 80,
            "waveforms": {
                "single": "5577879488735641037",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6530075564861017209": {
            "length": 40,
            "waveforms": {
                "I": "6530075564861017209_i",
                "Q": "6530075564861017209_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5768984935637455340_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
        },
        "5768984935637455340_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "-1894624465798050520": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "3111256994499612400_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3111256994499612400_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8905611921397003541": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "3948932196926256474": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-2392626175211919587": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8912907796944588464": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8705805477324620638": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-2171663417922936030": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "639513639873253775": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2261954252634175992": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1529292652562975756": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5931024266079283349": {
            "samples": [0.0] * 10 + [0.3] + [0.0] * 5,
            "type": "arbitrary",
        },
        "1758236855566439260": {
            "samples": [0.0] * 10 + [0.3] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "4811580070983064894": {
            "samples": [0.0] * 10 + [0.3] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-582965775796792609": {
            "samples": [0.0] * 10 + [0.3] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7913931117279680775": {
            "samples": [0.0] * 10 + [0.3] * 5 + [0.0],
            "type": "arbitrary",
        },
        "7485788586787290790": {
            "samples": [0.0] * 10 + [0.3] * 6,
            "type": "arbitrary",
        },
        "-8451652854074328113": {
            "samples": [0.0] * 10 + [0.3] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4127475510279854921": {
            "samples": [0.0] * 10 + [0.3] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6657776858694524933": {
            "samples": [0.0] * 10 + [0.3] * 9 + [0.0],
            "type": "arbitrary",
        },
        "1821707190996781634": {
            "samples": [0.0] * 10 + [0.3] * 10,
            "type": "arbitrary",
        },
        "8793261206792041533": {
            "samples": [0.0] * 10 + [0.3] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "149547951838695764": {
            "samples": [0.0] * 10 + [0.3] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3249594470613168163": {
            "samples": [0.0] * 10 + [0.3] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-474409651410814366": {
            "samples": [0.0] * 10 + [0.3] * 14,
            "type": "arbitrary",
        },
        "3202461600531702189": {
            "samples": [0.0] * 10 + [0.3] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6792931611002674823": {
            "samples": [0.0] * 10 + [0.3] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4942970502713269017": {
            "samples": [0.0] * 10 + [0.3] * 17 + [0.0],
            "type": "arbitrary",
        },
        "-1776764749347898693": {
            "samples": [0.0] * 10 + [0.3] * 18,
            "type": "arbitrary",
        },
        "-8350580332288086722": {
            "samples": [0.0] * 10 + [0.3] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-239997002764588087": {
            "samples": [0.0] * 10 + [0.3] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7964278730132437752": {
            "samples": [0.0] * 10 + [0.3] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-4468399919177942688": {
            "samples": [0.0] * 10 + [0.3] * 22,
            "type": "arbitrary",
        },
        "-218476210012461883": {
            "samples": [0.0] * 10 + [0.3] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9035515965810224838": {
            "samples": [0.0] * 10 + [0.3] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6087552347148650472": {
            "samples": [0.0] * 10 + [0.3] * 25 + [0.0],
            "type": "arbitrary",
        },
        "-9161239723667284581": {
            "samples": [0.0] * 10 + [0.3] * 26,
            "type": "arbitrary",
        },
        "989567022953791873": {
            "samples": [0.0] * 10 + [0.3] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4944148193040397083": {
            "samples": [0.0] * 10 + [0.3] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4101389175827130184": {
            "samples": [0.0] * 10 + [0.3] * 29 + [0.0],
            "type": "arbitrary",
        },
        "-8557299167751876859": {
            "samples": [0.0] * 10 + [0.3] * 30,
            "type": "arbitrary",
        },
        "-8990894448998286000": {
            "samples": [0.0] * 10 + [0.3] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2553960296845298351": {
            "samples": [0.0] * 10 + [0.3] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-35886269242960186": {
            "samples": [0.0] * 10 + [0.3] * 33 + [0.0],
            "type": "arbitrary",
        },
        "-2857506449220518873": {
            "samples": [0.0] * 10 + [0.3] * 34,
            "type": "arbitrary",
        },
        "1546248089306994470": {
            "samples": [0.0] * 10 + [0.3] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6473401833186242911": {
            "samples": [0.0] * 10 + [0.3] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5287013475055139759": {
            "samples": [0.0] * 10 + [0.3] * 37 + [0.0],
            "type": "arbitrary",
        },
        "471902259270851268": {
            "samples": [0.0] * 10 + [0.3] * 38,
            "type": "arbitrary",
        },
        "2850379103610640311": {
            "samples": [0.0] * 10 + [0.3] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2075321820283126993": {
            "samples": [0.0] * 10 + [0.3] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4644837052496854747": {
            "samples": [0.0] * 10 + [0.3] * 41 + [0.0],
            "type": "arbitrary",
        },
        "9138080126313010958": {
            "samples": [0.0] * 10 + [0.3] * 42,
            "type": "arbitrary",
        },
        "-1889232698674416720": {
            "samples": [0.0] * 10 + [0.3] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6018248492196121883": {
            "samples": [0.0] * 10 + [0.3] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "230115908245255764": {
            "samples": [0.0] * 10 + [0.3] * 45 + [0.0],
            "type": "arbitrary",
        },
        "-3389691347575590706": {
            "samples": [0.0] * 10 + [0.3] * 46,
            "type": "arbitrary",
        },
        "-6228851645577224214": {
            "samples": [0.0] * 10 + [0.3] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2141018351744030551": {
            "samples": [0.0] * 10 + [0.3] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6669018619016968039": {
            "samples": [0.0] * 10 + [0.3] * 49 + [0.0],
            "type": "arbitrary",
        },
        "-7573389716891963722": {
            "samples": [0.0] * 10 + [0.3] * 50,
            "type": "arbitrary",
        },
        "3156537187182049586": {
            "samples": [0.0] * 10 + [0.3] * 51 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3006964711487707951": {
            "samples": [0.0] * 10 + [0.3] * 52 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8644130658994366847": {
            "samples": [0.0] * 10 + [0.3] * 53 + [0.0],
            "type": "arbitrary",
        },
        "-6641055880276876591": {
            "samples": [0.0] * 10 + [0.3] * 54,
            "type": "arbitrary",
        },
        "-6189706011665842524": {
            "samples": [0.0] * 10 + [0.3] * 55 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6910451042641001121": {
            "samples": [0.0] * 10 + [0.3] * 56 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5130283345921138476": {
            "samples": [0.0] * 10 + [0.3] * 57 + [0.0],
            "type": "arbitrary",
        },
        "4511180424104023973": {
            "samples": [0.0] * 10 + [0.3] * 58,
            "type": "arbitrary",
        },
        "-769121735380718368": {
            "samples": [0.0] * 10 + [0.3] * 59 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7753513100815522267": {
            "samples": [0.0] * 10 + [0.3] * 60 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3663775962863379232": {
            "samples": [0.0] * 10 + [0.3] * 61 + [0.0],
            "type": "arbitrary",
        },
        "-5090218847060725109": {
            "samples": [0.0] * 10 + [0.3] * 62,
            "type": "arbitrary",
        },
        "2915794005675956746": {
            "samples": [0.0] * 10 + [0.3] * 63 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-961675388024279594": {
            "samples": [0.0] * 10 + [0.3] * 64 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4824670335971508242": {
            "samples": [0.0] * 10 + [0.3] * 65 + [0.0],
            "type": "arbitrary",
        },
        "-2998786616390532222": {
            "samples": [0.0] * 10 + [0.3] * 66,
            "type": "arbitrary",
        },
        "-3152942340854612480": {
            "samples": [0.0] * 10 + [0.3] * 67 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8736235562549571685": {
            "samples": [0.0] * 10 + [0.3] * 68 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5577879488735641037": {
            "samples": [0.0] * 10 + [0.3] * 69 + [0.0],
            "type": "arbitrary",
        },
        "6530075564861017209_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "6530075564861017209_q": {
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
                "3156537187182049586": "3156537187182049586",
                "-3006964711487707951": "-3006964711487707951",
                "-8644130658994366847": "-8644130658994366847",
                "-6641055880276876591": "-6641055880276876591",
                "-6189706011665842524": "-6189706011665842524",
                "-6910451042641001121": "-6910451042641001121",
                "5130283345921138476": "5130283345921138476",
                "4511180424104023973": "4511180424104023973",
                "-769121735380718368": "-769121735380718368",
                "7753513100815522267": "7753513100815522267",
                "3663775962863379232": "3663775962863379232",
                "-5090218847060725109": "-5090218847060725109",
                "2915794005675956746": "2915794005675956746",
                "-961675388024279594": "-961675388024279594",
                "4824670335971508242": "4824670335971508242",
                "-2998786616390532222": "-2998786616390532222",
                "-3152942340854612480": "-3152942340854612480",
                "-8736235562549571685": "-8736235562549571685",
                "5577879488735641037": "5577879488735641037",
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
                "5768984935637455340": "5768984935637455340",
                "6530075564861017209": "6530075564861017209",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_309",
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
                "-4853314269389355911": "-4853314269389355911_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_af8",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "5768984935637455340": {
            "length": 40,
            "waveforms": {
                "I": "5768984935637455340_i",
                "Q": "5768984935637455340_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1894624465798050520": {
            "length": 16,
            "waveforms": {
                "single": "-1894624465798050520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4853314269389355911_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3111256994499612400_i",
                "Q": "3111256994499612400_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-8905611921397003541": {
            "length": 16,
            "waveforms": {
                "single": "-8905611921397003541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3948932196926256474": {
            "length": 16,
            "waveforms": {
                "single": "3948932196926256474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2392626175211919587": {
            "length": 16,
            "waveforms": {
                "single": "-2392626175211919587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8912907796944588464": {
            "length": 16,
            "waveforms": {
                "single": "-8912907796944588464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8705805477324620638": {
            "length": 16,
            "waveforms": {
                "single": "8705805477324620638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2171663417922936030": {
            "length": 16,
            "waveforms": {
                "single": "-2171663417922936030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "639513639873253775": {
            "length": 16,
            "waveforms": {
                "single": "639513639873253775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2261954252634175992": {
            "length": 16,
            "waveforms": {
                "single": "2261954252634175992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1529292652562975756": {
            "length": 16,
            "waveforms": {
                "single": "-1529292652562975756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5931024266079283349": {
            "length": 16,
            "waveforms": {
                "single": "-5931024266079283349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1758236855566439260": {
            "length": 16,
            "waveforms": {
                "single": "1758236855566439260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4811580070983064894": {
            "length": 16,
            "waveforms": {
                "single": "4811580070983064894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-582965775796792609": {
            "length": 16,
            "waveforms": {
                "single": "-582965775796792609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7913931117279680775": {
            "length": 16,
            "waveforms": {
                "single": "-7913931117279680775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7485788586787290790": {
            "length": 16,
            "waveforms": {
                "single": "7485788586787290790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8451652854074328113": {
            "length": 20,
            "waveforms": {
                "single": "-8451652854074328113",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4127475510279854921": {
            "length": 20,
            "waveforms": {
                "single": "4127475510279854921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6657776858694524933": {
            "length": 20,
            "waveforms": {
                "single": "-6657776858694524933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1821707190996781634": {
            "length": 20,
            "waveforms": {
                "single": "1821707190996781634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8793261206792041533": {
            "length": 24,
            "waveforms": {
                "single": "8793261206792041533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "149547951838695764": {
            "length": 24,
            "waveforms": {
                "single": "149547951838695764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3249594470613168163": {
            "length": 24,
            "waveforms": {
                "single": "-3249594470613168163",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-474409651410814366": {
            "length": 24,
            "waveforms": {
                "single": "-474409651410814366",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3202461600531702189": {
            "length": 28,
            "waveforms": {
                "single": "3202461600531702189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6792931611002674823": {
            "length": 28,
            "waveforms": {
                "single": "-6792931611002674823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4942970502713269017": {
            "length": 28,
            "waveforms": {
                "single": "-4942970502713269017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1776764749347898693": {
            "length": 28,
            "waveforms": {
                "single": "-1776764749347898693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8350580332288086722": {
            "length": 32,
            "waveforms": {
                "single": "-8350580332288086722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-239997002764588087": {
            "length": 32,
            "waveforms": {
                "single": "-239997002764588087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7964278730132437752": {
            "length": 32,
            "waveforms": {
                "single": "7964278730132437752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4468399919177942688": {
            "length": 32,
            "waveforms": {
                "single": "-4468399919177942688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-218476210012461883": {
            "length": 36,
            "waveforms": {
                "single": "-218476210012461883",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9035515965810224838": {
            "length": 36,
            "waveforms": {
                "single": "-9035515965810224838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6087552347148650472": {
            "length": 36,
            "waveforms": {
                "single": "-6087552347148650472",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9161239723667284581": {
            "length": 36,
            "waveforms": {
                "single": "-9161239723667284581",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "989567022953791873": {
            "length": 40,
            "waveforms": {
                "single": "989567022953791873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4944148193040397083": {
            "length": 40,
            "waveforms": {
                "single": "-4944148193040397083",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4101389175827130184": {
            "length": 40,
            "waveforms": {
                "single": "-4101389175827130184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8557299167751876859": {
            "length": 40,
            "waveforms": {
                "single": "-8557299167751876859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8990894448998286000": {
            "length": 44,
            "waveforms": {
                "single": "-8990894448998286000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2553960296845298351": {
            "length": 44,
            "waveforms": {
                "single": "-2553960296845298351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-35886269242960186": {
            "length": 44,
            "waveforms": {
                "single": "-35886269242960186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2857506449220518873": {
            "length": 44,
            "waveforms": {
                "single": "-2857506449220518873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1546248089306994470": {
            "length": 48,
            "waveforms": {
                "single": "1546248089306994470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6473401833186242911": {
            "length": 48,
            "waveforms": {
                "single": "6473401833186242911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5287013475055139759": {
            "length": 48,
            "waveforms": {
                "single": "5287013475055139759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "471902259270851268": {
            "length": 48,
            "waveforms": {
                "single": "471902259270851268",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2850379103610640311": {
            "length": 52,
            "waveforms": {
                "single": "2850379103610640311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2075321820283126993": {
            "length": 52,
            "waveforms": {
                "single": "2075321820283126993",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4644837052496854747": {
            "length": 52,
            "waveforms": {
                "single": "-4644837052496854747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9138080126313010958": {
            "length": 52,
            "waveforms": {
                "single": "9138080126313010958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1889232698674416720": {
            "length": 56,
            "waveforms": {
                "single": "-1889232698674416720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6018248492196121883": {
            "length": 56,
            "waveforms": {
                "single": "-6018248492196121883",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "230115908245255764": {
            "length": 56,
            "waveforms": {
                "single": "230115908245255764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3389691347575590706": {
            "length": 56,
            "waveforms": {
                "single": "-3389691347575590706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6228851645577224214": {
            "length": 60,
            "waveforms": {
                "single": "-6228851645577224214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2141018351744030551": {
            "length": 60,
            "waveforms": {
                "single": "2141018351744030551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6669018619016968039": {
            "length": 60,
            "waveforms": {
                "single": "-6669018619016968039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7573389716891963722": {
            "length": 60,
            "waveforms": {
                "single": "-7573389716891963722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3156537187182049586": {
            "length": 64,
            "waveforms": {
                "single": "3156537187182049586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3006964711487707951": {
            "length": 64,
            "waveforms": {
                "single": "-3006964711487707951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8644130658994366847": {
            "length": 64,
            "waveforms": {
                "single": "-8644130658994366847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6641055880276876591": {
            "length": 64,
            "waveforms": {
                "single": "-6641055880276876591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6189706011665842524": {
            "length": 68,
            "waveforms": {
                "single": "-6189706011665842524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6910451042641001121": {
            "length": 68,
            "waveforms": {
                "single": "-6910451042641001121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5130283345921138476": {
            "length": 68,
            "waveforms": {
                "single": "5130283345921138476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4511180424104023973": {
            "length": 68,
            "waveforms": {
                "single": "4511180424104023973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-769121735380718368": {
            "length": 72,
            "waveforms": {
                "single": "-769121735380718368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7753513100815522267": {
            "length": 72,
            "waveforms": {
                "single": "7753513100815522267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3663775962863379232": {
            "length": 72,
            "waveforms": {
                "single": "3663775962863379232",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5090218847060725109": {
            "length": 72,
            "waveforms": {
                "single": "-5090218847060725109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2915794005675956746": {
            "length": 76,
            "waveforms": {
                "single": "2915794005675956746",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961675388024279594": {
            "length": 76,
            "waveforms": {
                "single": "-961675388024279594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4824670335971508242": {
            "length": 76,
            "waveforms": {
                "single": "4824670335971508242",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2998786616390532222": {
            "length": 76,
            "waveforms": {
                "single": "-2998786616390532222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3152942340854612480": {
            "length": 80,
            "waveforms": {
                "single": "-3152942340854612480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8736235562549571685": {
            "length": 80,
            "waveforms": {
                "single": "-8736235562549571685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5577879488735641037": {
            "length": 80,
            "waveforms": {
                "single": "5577879488735641037",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6530075564861017209": {
            "length": 40,
            "waveforms": {
                "I": "6530075564861017209_i",
                "Q": "6530075564861017209_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5768984935637455340_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5768984935637455340_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1894624465798050520": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3111256994499612400_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3111256994499612400_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8905611921397003541": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3948932196926256474": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2392626175211919587": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8912907796944588464": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8705805477324620638": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2171663417922936030": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "639513639873253775": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2261954252634175992": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1529292652562975756": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5931024266079283349": {
            "samples": [0.0] * 10 + [0.3] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1758236855566439260": {
            "samples": [0.0] * 10 + [0.3] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4811580070983064894": {
            "samples": [0.0] * 10 + [0.3] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-582965775796792609": {
            "samples": [0.0] * 10 + [0.3] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7913931117279680775": {
            "samples": [0.0] * 10 + [0.3] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7485788586787290790": {
            "samples": [0.0] * 10 + [0.3] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8451652854074328113": {
            "samples": [0.0] * 10 + [0.3] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4127475510279854921": {
            "samples": [0.0] * 10 + [0.3] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6657776858694524933": {
            "samples": [0.0] * 10 + [0.3] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1821707190996781634": {
            "samples": [0.0] * 10 + [0.3] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8793261206792041533": {
            "samples": [0.0] * 10 + [0.3] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "149547951838695764": {
            "samples": [0.0] * 10 + [0.3] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3249594470613168163": {
            "samples": [0.0] * 10 + [0.3] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-474409651410814366": {
            "samples": [0.0] * 10 + [0.3] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3202461600531702189": {
            "samples": [0.0] * 10 + [0.3] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6792931611002674823": {
            "samples": [0.0] * 10 + [0.3] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4942970502713269017": {
            "samples": [0.0] * 10 + [0.3] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1776764749347898693": {
            "samples": [0.0] * 10 + [0.3] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8350580332288086722": {
            "samples": [0.0] * 10 + [0.3] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-239997002764588087": {
            "samples": [0.0] * 10 + [0.3] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7964278730132437752": {
            "samples": [0.0] * 10 + [0.3] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4468399919177942688": {
            "samples": [0.0] * 10 + [0.3] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-218476210012461883": {
            "samples": [0.0] * 10 + [0.3] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9035515965810224838": {
            "samples": [0.0] * 10 + [0.3] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6087552347148650472": {
            "samples": [0.0] * 10 + [0.3] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9161239723667284581": {
            "samples": [0.0] * 10 + [0.3] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "989567022953791873": {
            "samples": [0.0] * 10 + [0.3] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4944148193040397083": {
            "samples": [0.0] * 10 + [0.3] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4101389175827130184": {
            "samples": [0.0] * 10 + [0.3] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8557299167751876859": {
            "samples": [0.0] * 10 + [0.3] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8990894448998286000": {
            "samples": [0.0] * 10 + [0.3] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2553960296845298351": {
            "samples": [0.0] * 10 + [0.3] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-35886269242960186": {
            "samples": [0.0] * 10 + [0.3] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2857506449220518873": {
            "samples": [0.0] * 10 + [0.3] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1546248089306994470": {
            "samples": [0.0] * 10 + [0.3] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6473401833186242911": {
            "samples": [0.0] * 10 + [0.3] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5287013475055139759": {
            "samples": [0.0] * 10 + [0.3] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "471902259270851268": {
            "samples": [0.0] * 10 + [0.3] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2850379103610640311": {
            "samples": [0.0] * 10 + [0.3] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2075321820283126993": {
            "samples": [0.0] * 10 + [0.3] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4644837052496854747": {
            "samples": [0.0] * 10 + [0.3] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9138080126313010958": {
            "samples": [0.0] * 10 + [0.3] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1889232698674416720": {
            "samples": [0.0] * 10 + [0.3] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6018248492196121883": {
            "samples": [0.0] * 10 + [0.3] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "230115908245255764": {
            "samples": [0.0] * 10 + [0.3] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3389691347575590706": {
            "samples": [0.0] * 10 + [0.3] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6228851645577224214": {
            "samples": [0.0] * 10 + [0.3] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2141018351744030551": {
            "samples": [0.0] * 10 + [0.3] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6669018619016968039": {
            "samples": [0.0] * 10 + [0.3] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7573389716891963722": {
            "samples": [0.0] * 10 + [0.3] * 50,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3156537187182049586": {
            "samples": [0.0] * 10 + [0.3] * 51 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3006964711487707951": {
            "samples": [0.0] * 10 + [0.3] * 52 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8644130658994366847": {
            "samples": [0.0] * 10 + [0.3] * 53 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6641055880276876591": {
            "samples": [0.0] * 10 + [0.3] * 54,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6189706011665842524": {
            "samples": [0.0] * 10 + [0.3] * 55 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6910451042641001121": {
            "samples": [0.0] * 10 + [0.3] * 56 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5130283345921138476": {
            "samples": [0.0] * 10 + [0.3] * 57 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4511180424104023973": {
            "samples": [0.0] * 10 + [0.3] * 58,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-769121735380718368": {
            "samples": [0.0] * 10 + [0.3] * 59 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7753513100815522267": {
            "samples": [0.0] * 10 + [0.3] * 60 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3663775962863379232": {
            "samples": [0.0] * 10 + [0.3] * 61 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5090218847060725109": {
            "samples": [0.0] * 10 + [0.3] * 62,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2915794005675956746": {
            "samples": [0.0] * 10 + [0.3] * 63 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-961675388024279594": {
            "samples": [0.0] * 10 + [0.3] * 64 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4824670335971508242": {
            "samples": [0.0] * 10 + [0.3] * 65 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2998786616390532222": {
            "samples": [0.0] * 10 + [0.3] * 66,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3152942340854612480": {
            "samples": [0.0] * 10 + [0.3] * 67 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8736235562549571685": {
            "samples": [0.0] * 10 + [0.3] * 68 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5577879488735641037": {
            "samples": [0.0] * 10 + [0.3] * 69 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6530075564861017209_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6530075564861017209_q": {
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
        "B4/drive_mixer_309": [{'intermediate_frequency': 109610828.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_af8": [{'intermediate_frequency': 331181947.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

