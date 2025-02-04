
# Single QUA script generated at 2025-02-04 15:03:52.933120
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
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
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("297752393869757198", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25540, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-2026805688217079255", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25540, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-7646797066067795385", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25540, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("2717006141071639309", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25540, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("7826255570992768467", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25539, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-7801403046826922742", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25539, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("2977985970361078505", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25539, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-8298768427607981098", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25539, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-3678916985424897722", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25538, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-7093941691426878612", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25538, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-148939482598276285", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25538, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-7816294539119826654", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25538, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-3293976769029823338", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25537, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("3973546578803748735", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25537, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("7282030022431654924", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25537, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("7503524081630370172", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25537, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-2737690702852189665", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("4358486795198823119", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        play("-5416059360774458179", "B1/drive")
        wait(11, "B1/flux")
        play("-8523966244877299333", "B1/flux")
        wait(46, "B1/drive")
        play("-4654968731550896310", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-5615552642377102198", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9979139295843761)-(v3*0.06455841650372783))>0.0008879953521066911)))
        save(v4, r1)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-5615552642377102198_B1|acquisition_shots")


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
            },
            "digital_outputs": {
                "3": {},
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
                "297752393869757198": "297752393869757198",
                "-2026805688217079255": "-2026805688217079255",
                "-7646797066067795385": "-7646797066067795385",
                "2717006141071639309": "2717006141071639309",
                "7826255570992768467": "7826255570992768467",
                "-7801403046826922742": "-7801403046826922742",
                "2977985970361078505": "2977985970361078505",
                "-8298768427607981098": "-8298768427607981098",
                "-3678916985424897722": "-3678916985424897722",
                "-7093941691426878612": "-7093941691426878612",
                "-148939482598276285": "-148939482598276285",
                "-7816294539119826654": "-7816294539119826654",
                "-3293976769029823338": "-3293976769029823338",
                "3973546578803748735": "3973546578803748735",
                "7282030022431654924": "7282030022431654924",
                "7503524081630370172": "7503524081630370172",
                "-2737690702852189665": "-2737690702852189665",
                "4358486795198823119": "4358486795198823119",
                "-8523966244877299333": "-8523966244877299333",
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
                "-5416059360774458179": "-5416059360774458179",
                "-4654968731550896310": "-4654968731550896310",
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
                "-5615552642377102198": "-5615552642377102198_B1/acquisition",
            },
        },
    },
    "pulses": {
        "-5416059360774458179": {
            "length": 40,
            "waveforms": {
                "I": "-5416059360774458179_i",
                "Q": "-5416059360774458179_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5949790465514463806": {
            "length": 16,
            "waveforms": {
                "single": "5949790465514463806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5615552642377102198_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1569116956350016534_i",
                "Q": "-1569116956350016534_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-3624771815492434955": {
            "length": 16,
            "waveforms": {
                "single": "-3624771815492434955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7154617201695566292": {
            "length": 16,
            "waveforms": {
                "single": "7154617201695566292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6877422798279564078": {
            "length": 16,
            "waveforms": {
                "single": "6877422798279564078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4223164276079747809": {
            "length": 16,
            "waveforms": {
                "single": "-4223164276079747809",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6825509446141268974": {
            "length": 16,
            "waveforms": {
                "single": "-6825509446141268974",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4027691748736211502": {
            "length": 16,
            "waveforms": {
                "single": "4027691748736211502",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3083844841844548212": {
            "length": 16,
            "waveforms": {
                "single": "3083844841844548212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-820577851895478460": {
            "length": 16,
            "waveforms": {
                "single": "-820577851895478460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6269223379963635301": {
            "length": 16,
            "waveforms": {
                "single": "-6269223379963635301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8810989348115654014": {
            "length": 16,
            "waveforms": {
                "single": "8810989348115654014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5627058976152065511": {
            "length": 16,
            "waveforms": {
                "single": "5627058976152065511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3690279117438337844": {
            "length": 16,
            "waveforms": {
                "single": "3690279117438337844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6831885712333167997": {
            "length": 16,
            "waveforms": {
                "single": "6831885712333167997",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1383240184265011156": {
            "length": 16,
            "waveforms": {
                "single": "1383240184265011156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-990358209543186768": {
            "length": 16,
            "waveforms": {
                "single": "-990358209543186768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-768864150344471520": {
            "length": 20,
            "waveforms": {
                "single": "-768864150344471520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8103317642358181335": {
            "length": 20,
            "waveforms": {
                "single": "8103317642358181335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "435962585836630966": {
            "length": 20,
            "waveforms": {
                "single": "435962585836630966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2982607411680865165": {
            "length": 20,
            "waveforms": {
                "single": "2982607411680865165",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-383923933949397136": {
            "length": 24,
            "waveforms": {
                "single": "-383923933949397136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-162429874750681888": {
            "length": 24,
            "waveforms": {
                "single": "-162429874750681888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2690962867122723824": {
            "length": 24,
            "waveforms": {
                "single": "-2690962867122723824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5514566422104267955": {
            "length": 24,
            "waveforms": {
                "single": "5514566422104267955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5237372018688265741": {
            "length": 28,
            "waveforms": {
                "single": "5237372018688265741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7268539630279249321": {
            "length": 28,
            "waveforms": {
                "single": "7268539630279249321",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2972675154203310516": {
            "length": 28,
            "waveforms": {
                "single": "-2972675154203310516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2313828791455433936": {
            "length": 28,
            "waveforms": {
                "single": "2313828791455433936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5602235226381606950": {
            "length": 32,
            "waveforms": {
                "single": "-5602235226381606950",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5843806294282055373": {
            "length": 32,
            "waveforms": {
                "single": "5843806294282055373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6099600607162665306": {
            "length": 32,
            "waveforms": {
                "single": "-6099600607162665306",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4679788410025335941": {
            "length": 32,
            "waveforms": {
                "single": "4679788410025335941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3901840919159498443": {
            "length": 36,
            "waveforms": {
                "single": "-3901840919159498443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2050228337847039507": {
            "length": 36,
            "waveforms": {
                "single": "2050228337847039507",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5191834932741869660": {
            "length": 36,
            "waveforms": {
                "single": "5191834932741869660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1552862957065981151": {
            "length": 36,
            "waveforms": {
                "single": "1552862957065981151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5674025936634347065": {
            "length": 40,
            "waveforms": {
                "single": "5674025936634347065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3750622645069148014": {
            "length": 40,
            "waveforms": {
                "single": "3750622645069148014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8744052171633865652": {
            "length": 40,
            "waveforms": {
                "single": "-8744052171633865652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1204088193754667371": {
            "length": 40,
            "waveforms": {
                "single": "-1204088193754667371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6546292483630698789": {
            "length": 44,
            "waveforms": {
                "single": "-6546292483630698789",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2023974713540695473": {
            "length": 44,
            "waveforms": {
                "single": "-2023974713540695473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4357056920662937646": {
            "length": 44,
            "waveforms": {
                "single": "4357056920662937646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-819147977359592987": {
            "length": 44,
            "waveforms": {
                "single": "-819147977359592987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-597653918160877739": {
            "length": 48,
            "waveforms": {
                "single": "-597653918160877739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1106171080597947668": {
            "length": 48,
            "waveforms": {
                "single": "1106171080597947668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5628488850687950984": {
            "length": 48,
            "waveforms": {
                "single": "5628488850687950984",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2038866205833599385": {
            "length": 48,
            "waveforms": {
                "single": "-2038866205833599385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6833315586869053470": {
            "length": 52,
            "waveforms": {
                "single": "6833315586869053470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1491111296993022052": {
            "length": 52,
            "waveforms": {
                "single": "1491111296993022052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6013429067083025368": {
            "length": 52,
            "waveforms": {
                "single": "6013429067083025368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5165791658792954175": {
            "length": 52,
            "waveforms": {
                "single": "-5165791658792954175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3039737630434037604": {
            "length": 56,
            "waveforms": {
                "single": "3039737630434037604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2762543227018035390": {
            "length": 56,
            "waveforms": {
                "single": "2762543227018035390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6569715133260659041": {
            "length": 56,
            "waveforms": {
                "single": "6569715133260659041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4780851442397879791": {
            "length": 56,
            "waveforms": {
                "single": "-4780851442397879791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3424677846829111988": {
            "length": 60,
            "waveforms": {
                "single": "3424677846829111988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8988968880462541152": {
            "length": 60,
            "waveforms": {
                "single": "8988968880462541152",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8031737282462869769": {
            "length": 60,
            "waveforms": {
                "single": "-8031737282462869769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "173792006764122010": {
            "length": 60,
            "waveforms": {
                "single": "173792006764122010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "297752393869757198": {
            "length": 64,
            "waveforms": {
                "single": "297752393869757198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2026805688217079255": {
            "length": 64,
            "waveforms": {
                "single": "-2026805688217079255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7646797066067795385": {
            "length": 64,
            "waveforms": {
                "single": "-7646797066067795385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2717006141071639309": {
            "length": 64,
            "waveforms": {
                "single": "2717006141071639309",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7826255570992768467": {
            "length": 68,
            "waveforms": {
                "single": "7826255570992768467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7801403046826922742": {
            "length": 68,
            "waveforms": {
                "single": "-7801403046826922742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2977985970361078505": {
            "length": 68,
            "waveforms": {
                "single": "2977985970361078505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8298768427607981098": {
            "length": 68,
            "waveforms": {
                "single": "-8298768427607981098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3678916985424897722": {
            "length": 72,
            "waveforms": {
                "single": "-3678916985424897722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7093941691426878612": {
            "length": 72,
            "waveforms": {
                "single": "-7093941691426878612",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-148939482598276285": {
            "length": 72,
            "waveforms": {
                "single": "-148939482598276285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7816294539119826654": {
            "length": 72,
            "waveforms": {
                "single": "-7816294539119826654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3293976769029823338": {
            "length": 76,
            "waveforms": {
                "single": "-3293976769029823338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3973546578803748735": {
            "length": 76,
            "waveforms": {
                "single": "3973546578803748735",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7282030022431654924": {
            "length": 76,
            "waveforms": {
                "single": "7282030022431654924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7503524081630370172": {
            "length": 76,
            "waveforms": {
                "single": "7503524081630370172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2737690702852189665": {
            "length": 80,
            "waveforms": {
                "single": "-2737690702852189665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4358486795198823119": {
            "length": 80,
            "waveforms": {
                "single": "4358486795198823119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8523966244877299333": {
            "length": 80,
            "waveforms": {
                "single": "-8523966244877299333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4654968731550896310": {
            "length": 40,
            "waveforms": {
                "I": "-4654968731550896310_i",
                "Q": "-4654968731550896310_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-5416059360774458179_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-5416059360774458179_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "5949790465514463806": {
            "samples": [0.35] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-1569116956350016534_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-1569116956350016534_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3624771815492434955": {
            "samples": [0.35] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "7154617201695566292": {
            "samples": [0.35] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "6877422798279564078": {
            "samples": [0.35] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-4223164276079747809": {
            "samples": [0.35] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-6825509446141268974": {
            "samples": [0.35] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "4027691748736211502": {
            "samples": [0.35] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "3083844841844548212": {
            "samples": [0.35] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-820577851895478460": {
            "samples": [0.35] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-6269223379963635301": {
            "samples": [0.35] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8810989348115654014": {
            "samples": [0.35] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5627058976152065511": {
            "samples": [0.35] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "3690279117438337844": {
            "samples": [0.35] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6831885712333167997": {
            "samples": [0.35] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1383240184265011156": {
            "samples": [0.35] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-990358209543186768": {
            "sample": 0.35,
            "type": "constant",
        },
        "-768864150344471520": {
            "samples": [0.35] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8103317642358181335": {
            "samples": [0.35] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "435962585836630966": {
            "samples": [0.35] * 19 + [0.0],
            "type": "arbitrary",
        },
        "2982607411680865165": {
            "sample": 0.35,
            "type": "constant",
        },
        "-383923933949397136": {
            "samples": [0.35] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-162429874750681888": {
            "samples": [0.35] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2690962867122723824": {
            "samples": [0.35] * 23 + [0.0],
            "type": "arbitrary",
        },
        "5514566422104267955": {
            "sample": 0.35,
            "type": "constant",
        },
        "5237372018688265741": {
            "samples": [0.35] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7268539630279249321": {
            "samples": [0.35] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2972675154203310516": {
            "samples": [0.35] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2313828791455433936": {
            "sample": 0.35,
            "type": "constant",
        },
        "-5602235226381606950": {
            "samples": [0.35] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5843806294282055373": {
            "samples": [0.35] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6099600607162665306": {
            "samples": [0.35] * 31 + [0.0],
            "type": "arbitrary",
        },
        "4679788410025335941": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3901840919159498443": {
            "samples": [0.35] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2050228337847039507": {
            "samples": [0.35] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5191834932741869660": {
            "samples": [0.35] * 35 + [0.0],
            "type": "arbitrary",
        },
        "1552862957065981151": {
            "sample": 0.35,
            "type": "constant",
        },
        "5674025936634347065": {
            "samples": [0.35] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3750622645069148014": {
            "samples": [0.35] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8744052171633865652": {
            "samples": [0.35] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1204088193754667371": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6546292483630698789": {
            "samples": [0.35] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2023974713540695473": {
            "samples": [0.35] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4357056920662937646": {
            "samples": [0.35] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-819147977359592987": {
            "sample": 0.35,
            "type": "constant",
        },
        "-597653918160877739": {
            "samples": [0.35] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1106171080597947668": {
            "samples": [0.35] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5628488850687950984": {
            "samples": [0.35] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2038866205833599385": {
            "sample": 0.35,
            "type": "constant",
        },
        "6833315586869053470": {
            "samples": [0.35] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1491111296993022052": {
            "samples": [0.35] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6013429067083025368": {
            "samples": [0.35] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-5165791658792954175": {
            "sample": 0.35,
            "type": "constant",
        },
        "3039737630434037604": {
            "samples": [0.35] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2762543227018035390": {
            "samples": [0.35] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6569715133260659041": {
            "samples": [0.35] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-4780851442397879791": {
            "sample": 0.35,
            "type": "constant",
        },
        "3424677846829111988": {
            "samples": [0.35] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8988968880462541152": {
            "samples": [0.35] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8031737282462869769": {
            "samples": [0.35] * 59 + [0.0],
            "type": "arbitrary",
        },
        "173792006764122010": {
            "sample": 0.35,
            "type": "constant",
        },
        "297752393869757198": {
            "samples": [0.35] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2026805688217079255": {
            "samples": [0.35] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7646797066067795385": {
            "samples": [0.35] * 63 + [0.0],
            "type": "arbitrary",
        },
        "2717006141071639309": {
            "sample": 0.35,
            "type": "constant",
        },
        "7826255570992768467": {
            "samples": [0.35] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7801403046826922742": {
            "samples": [0.35] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2977985970361078505": {
            "samples": [0.35] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-8298768427607981098": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3678916985424897722": {
            "samples": [0.35] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7093941691426878612": {
            "samples": [0.35] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-148939482598276285": {
            "samples": [0.35] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-7816294539119826654": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3293976769029823338": {
            "samples": [0.35] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3973546578803748735": {
            "samples": [0.35] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7282030022431654924": {
            "samples": [0.35] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7503524081630370172": {
            "sample": 0.35,
            "type": "constant",
        },
        "-2737690702852189665": {
            "samples": [0.35] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4358486795198823119": {
            "samples": [0.35] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8523966244877299333": {
            "samples": [0.35] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-4654968731550896310_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-4654968731550896310_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
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
                    "offset": -0.25498290735703955,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                    "offset": -0.4530870218982913,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": 0.05418914676504196,
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
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
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
            "operations": {
                "297752393869757198": "297752393869757198",
                "-2026805688217079255": "-2026805688217079255",
                "-7646797066067795385": "-7646797066067795385",
                "2717006141071639309": "2717006141071639309",
                "7826255570992768467": "7826255570992768467",
                "-7801403046826922742": "-7801403046826922742",
                "2977985970361078505": "2977985970361078505",
                "-8298768427607981098": "-8298768427607981098",
                "-3678916985424897722": "-3678916985424897722",
                "-7093941691426878612": "-7093941691426878612",
                "-148939482598276285": "-148939482598276285",
                "-7816294539119826654": "-7816294539119826654",
                "-3293976769029823338": "-3293976769029823338",
                "3973546578803748735": "3973546578803748735",
                "7282030022431654924": "7282030022431654924",
                "7503524081630370172": "7503524081630370172",
                "-2737690702852189665": "-2737690702852189665",
                "4358486795198823119": "4358486795198823119",
                "-8523966244877299333": "-8523966244877299333",
            },
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
        "B1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 100388701.0,
            "operations": {
                "-5416059360774458179": "-5416059360774458179",
                "-4654968731550896310": "-4654968731550896310",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_3f3",
                "lo_frequency": 4900000000.0,
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
            "intermediate_frequency": -237451236.0,
            "operations": {
                "-5615552642377102198": "-5615552642377102198_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_fd0",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-5416059360774458179": {
            "length": 40,
            "waveforms": {
                "I": "-5416059360774458179_i",
                "Q": "-5416059360774458179_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5949790465514463806": {
            "length": 16,
            "waveforms": {
                "single": "5949790465514463806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5615552642377102198_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1569116956350016534_i",
                "Q": "-1569116956350016534_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "-3624771815492434955": {
            "length": 16,
            "waveforms": {
                "single": "-3624771815492434955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7154617201695566292": {
            "length": 16,
            "waveforms": {
                "single": "7154617201695566292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6877422798279564078": {
            "length": 16,
            "waveforms": {
                "single": "6877422798279564078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4223164276079747809": {
            "length": 16,
            "waveforms": {
                "single": "-4223164276079747809",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6825509446141268974": {
            "length": 16,
            "waveforms": {
                "single": "-6825509446141268974",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4027691748736211502": {
            "length": 16,
            "waveforms": {
                "single": "4027691748736211502",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3083844841844548212": {
            "length": 16,
            "waveforms": {
                "single": "3083844841844548212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-820577851895478460": {
            "length": 16,
            "waveforms": {
                "single": "-820577851895478460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6269223379963635301": {
            "length": 16,
            "waveforms": {
                "single": "-6269223379963635301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8810989348115654014": {
            "length": 16,
            "waveforms": {
                "single": "8810989348115654014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5627058976152065511": {
            "length": 16,
            "waveforms": {
                "single": "5627058976152065511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3690279117438337844": {
            "length": 16,
            "waveforms": {
                "single": "3690279117438337844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6831885712333167997": {
            "length": 16,
            "waveforms": {
                "single": "6831885712333167997",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1383240184265011156": {
            "length": 16,
            "waveforms": {
                "single": "1383240184265011156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-990358209543186768": {
            "length": 16,
            "waveforms": {
                "single": "-990358209543186768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-768864150344471520": {
            "length": 20,
            "waveforms": {
                "single": "-768864150344471520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8103317642358181335": {
            "length": 20,
            "waveforms": {
                "single": "8103317642358181335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "435962585836630966": {
            "length": 20,
            "waveforms": {
                "single": "435962585836630966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2982607411680865165": {
            "length": 20,
            "waveforms": {
                "single": "2982607411680865165",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-383923933949397136": {
            "length": 24,
            "waveforms": {
                "single": "-383923933949397136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-162429874750681888": {
            "length": 24,
            "waveforms": {
                "single": "-162429874750681888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2690962867122723824": {
            "length": 24,
            "waveforms": {
                "single": "-2690962867122723824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5514566422104267955": {
            "length": 24,
            "waveforms": {
                "single": "5514566422104267955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5237372018688265741": {
            "length": 28,
            "waveforms": {
                "single": "5237372018688265741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7268539630279249321": {
            "length": 28,
            "waveforms": {
                "single": "7268539630279249321",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2972675154203310516": {
            "length": 28,
            "waveforms": {
                "single": "-2972675154203310516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2313828791455433936": {
            "length": 28,
            "waveforms": {
                "single": "2313828791455433936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5602235226381606950": {
            "length": 32,
            "waveforms": {
                "single": "-5602235226381606950",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5843806294282055373": {
            "length": 32,
            "waveforms": {
                "single": "5843806294282055373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6099600607162665306": {
            "length": 32,
            "waveforms": {
                "single": "-6099600607162665306",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4679788410025335941": {
            "length": 32,
            "waveforms": {
                "single": "4679788410025335941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3901840919159498443": {
            "length": 36,
            "waveforms": {
                "single": "-3901840919159498443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2050228337847039507": {
            "length": 36,
            "waveforms": {
                "single": "2050228337847039507",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5191834932741869660": {
            "length": 36,
            "waveforms": {
                "single": "5191834932741869660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1552862957065981151": {
            "length": 36,
            "waveforms": {
                "single": "1552862957065981151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5674025936634347065": {
            "length": 40,
            "waveforms": {
                "single": "5674025936634347065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3750622645069148014": {
            "length": 40,
            "waveforms": {
                "single": "3750622645069148014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8744052171633865652": {
            "length": 40,
            "waveforms": {
                "single": "-8744052171633865652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1204088193754667371": {
            "length": 40,
            "waveforms": {
                "single": "-1204088193754667371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6546292483630698789": {
            "length": 44,
            "waveforms": {
                "single": "-6546292483630698789",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2023974713540695473": {
            "length": 44,
            "waveforms": {
                "single": "-2023974713540695473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4357056920662937646": {
            "length": 44,
            "waveforms": {
                "single": "4357056920662937646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-819147977359592987": {
            "length": 44,
            "waveforms": {
                "single": "-819147977359592987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-597653918160877739": {
            "length": 48,
            "waveforms": {
                "single": "-597653918160877739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1106171080597947668": {
            "length": 48,
            "waveforms": {
                "single": "1106171080597947668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5628488850687950984": {
            "length": 48,
            "waveforms": {
                "single": "5628488850687950984",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2038866205833599385": {
            "length": 48,
            "waveforms": {
                "single": "-2038866205833599385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6833315586869053470": {
            "length": 52,
            "waveforms": {
                "single": "6833315586869053470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1491111296993022052": {
            "length": 52,
            "waveforms": {
                "single": "1491111296993022052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6013429067083025368": {
            "length": 52,
            "waveforms": {
                "single": "6013429067083025368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5165791658792954175": {
            "length": 52,
            "waveforms": {
                "single": "-5165791658792954175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3039737630434037604": {
            "length": 56,
            "waveforms": {
                "single": "3039737630434037604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2762543227018035390": {
            "length": 56,
            "waveforms": {
                "single": "2762543227018035390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6569715133260659041": {
            "length": 56,
            "waveforms": {
                "single": "6569715133260659041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4780851442397879791": {
            "length": 56,
            "waveforms": {
                "single": "-4780851442397879791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3424677846829111988": {
            "length": 60,
            "waveforms": {
                "single": "3424677846829111988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8988968880462541152": {
            "length": 60,
            "waveforms": {
                "single": "8988968880462541152",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8031737282462869769": {
            "length": 60,
            "waveforms": {
                "single": "-8031737282462869769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "173792006764122010": {
            "length": 60,
            "waveforms": {
                "single": "173792006764122010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "297752393869757198": {
            "length": 64,
            "waveforms": {
                "single": "297752393869757198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2026805688217079255": {
            "length": 64,
            "waveforms": {
                "single": "-2026805688217079255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7646797066067795385": {
            "length": 64,
            "waveforms": {
                "single": "-7646797066067795385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2717006141071639309": {
            "length": 64,
            "waveforms": {
                "single": "2717006141071639309",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7826255570992768467": {
            "length": 68,
            "waveforms": {
                "single": "7826255570992768467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7801403046826922742": {
            "length": 68,
            "waveforms": {
                "single": "-7801403046826922742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2977985970361078505": {
            "length": 68,
            "waveforms": {
                "single": "2977985970361078505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8298768427607981098": {
            "length": 68,
            "waveforms": {
                "single": "-8298768427607981098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3678916985424897722": {
            "length": 72,
            "waveforms": {
                "single": "-3678916985424897722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7093941691426878612": {
            "length": 72,
            "waveforms": {
                "single": "-7093941691426878612",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-148939482598276285": {
            "length": 72,
            "waveforms": {
                "single": "-148939482598276285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7816294539119826654": {
            "length": 72,
            "waveforms": {
                "single": "-7816294539119826654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3293976769029823338": {
            "length": 76,
            "waveforms": {
                "single": "-3293976769029823338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3973546578803748735": {
            "length": 76,
            "waveforms": {
                "single": "3973546578803748735",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7282030022431654924": {
            "length": 76,
            "waveforms": {
                "single": "7282030022431654924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7503524081630370172": {
            "length": 76,
            "waveforms": {
                "single": "7503524081630370172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2737690702852189665": {
            "length": 80,
            "waveforms": {
                "single": "-2737690702852189665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4358486795198823119": {
            "length": 80,
            "waveforms": {
                "single": "4358486795198823119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8523966244877299333": {
            "length": 80,
            "waveforms": {
                "single": "-8523966244877299333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4654968731550896310": {
            "length": 40,
            "waveforms": {
                "I": "-4654968731550896310_i",
                "Q": "-4654968731550896310_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-5416059360774458179_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5416059360774458179_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5949790465514463806": {
            "samples": [0.35] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1569116956350016534_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-1569116956350016534_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3624771815492434955": {
            "samples": [0.35] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7154617201695566292": {
            "samples": [0.35] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6877422798279564078": {
            "samples": [0.35] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4223164276079747809": {
            "samples": [0.35] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6825509446141268974": {
            "samples": [0.35] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4027691748736211502": {
            "samples": [0.35] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3083844841844548212": {
            "samples": [0.35] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-820577851895478460": {
            "samples": [0.35] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6269223379963635301": {
            "samples": [0.35] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8810989348115654014": {
            "samples": [0.35] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5627058976152065511": {
            "samples": [0.35] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3690279117438337844": {
            "samples": [0.35] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6831885712333167997": {
            "samples": [0.35] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1383240184265011156": {
            "samples": [0.35] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-990358209543186768": {
            "sample": 0.35,
            "type": "constant",
        },
        "-768864150344471520": {
            "samples": [0.35] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8103317642358181335": {
            "samples": [0.35] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "435962585836630966": {
            "samples": [0.35] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2982607411680865165": {
            "sample": 0.35,
            "type": "constant",
        },
        "-383923933949397136": {
            "samples": [0.35] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-162429874750681888": {
            "samples": [0.35] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2690962867122723824": {
            "samples": [0.35] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5514566422104267955": {
            "sample": 0.35,
            "type": "constant",
        },
        "5237372018688265741": {
            "samples": [0.35] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7268539630279249321": {
            "samples": [0.35] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2972675154203310516": {
            "samples": [0.35] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2313828791455433936": {
            "sample": 0.35,
            "type": "constant",
        },
        "-5602235226381606950": {
            "samples": [0.35] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5843806294282055373": {
            "samples": [0.35] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6099600607162665306": {
            "samples": [0.35] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4679788410025335941": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3901840919159498443": {
            "samples": [0.35] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2050228337847039507": {
            "samples": [0.35] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5191834932741869660": {
            "samples": [0.35] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1552862957065981151": {
            "sample": 0.35,
            "type": "constant",
        },
        "5674025936634347065": {
            "samples": [0.35] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3750622645069148014": {
            "samples": [0.35] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8744052171633865652": {
            "samples": [0.35] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1204088193754667371": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6546292483630698789": {
            "samples": [0.35] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2023974713540695473": {
            "samples": [0.35] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4357056920662937646": {
            "samples": [0.35] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-819147977359592987": {
            "sample": 0.35,
            "type": "constant",
        },
        "-597653918160877739": {
            "samples": [0.35] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1106171080597947668": {
            "samples": [0.35] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5628488850687950984": {
            "samples": [0.35] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2038866205833599385": {
            "sample": 0.35,
            "type": "constant",
        },
        "6833315586869053470": {
            "samples": [0.35] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1491111296993022052": {
            "samples": [0.35] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6013429067083025368": {
            "samples": [0.35] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5165791658792954175": {
            "sample": 0.35,
            "type": "constant",
        },
        "3039737630434037604": {
            "samples": [0.35] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2762543227018035390": {
            "samples": [0.35] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6569715133260659041": {
            "samples": [0.35] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4780851442397879791": {
            "sample": 0.35,
            "type": "constant",
        },
        "3424677846829111988": {
            "samples": [0.35] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8988968880462541152": {
            "samples": [0.35] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8031737282462869769": {
            "samples": [0.35] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "173792006764122010": {
            "sample": 0.35,
            "type": "constant",
        },
        "297752393869757198": {
            "samples": [0.35] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2026805688217079255": {
            "samples": [0.35] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7646797066067795385": {
            "samples": [0.35] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2717006141071639309": {
            "sample": 0.35,
            "type": "constant",
        },
        "7826255570992768467": {
            "samples": [0.35] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7801403046826922742": {
            "samples": [0.35] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2977985970361078505": {
            "samples": [0.35] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8298768427607981098": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3678916985424897722": {
            "samples": [0.35] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7093941691426878612": {
            "samples": [0.35] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-148939482598276285": {
            "samples": [0.35] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7816294539119826654": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3293976769029823338": {
            "samples": [0.35] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3973546578803748735": {
            "samples": [0.35] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7282030022431654924": {
            "samples": [0.35] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7503524081630370172": {
            "sample": 0.35,
            "type": "constant",
        },
        "-2737690702852189665": {
            "samples": [0.35] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4358486795198823119": {
            "samples": [0.35] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8523966244877299333": {
            "samples": [0.35] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4654968731550896310_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4654968731550896310_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
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
        "B1/drive_mixer_3f3": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/acquisition_mixer_fd0": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

