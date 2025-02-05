
# Single QUA script generated at 2025-02-05 18:54:01.550801
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
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("9081578952441008474", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("7599840697439580813", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25540, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-6324585606179967487", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25540, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-1215336176258838329", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25540, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-1091375789153203141", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25539, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-3415933871240039594", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25539, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("1106383898849963722", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25539, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-4342261629218193119", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25539, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-8913336826433880867", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25538, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-9190531229849883081", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25538, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("1662669965027597395", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25538, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("8758847463078610179", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25538, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-1482367321403949658", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25537, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("4081923712229479506", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25537, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-4111927393582246092", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25537, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("6667461623605755155", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25537, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("-4609292774363304448", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25536, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("4466863928624553890", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25536, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        play("6662083640586049351", "B1/drive")
        wait(11, "B1/flux")
        play("5892901839408694585", "B1/flux")
        wait(46, "B1/drive")
        play("7423174269809611220", "B1/drive")
        wait(66, "B1/acquisition")
        measure("2047853911291155102", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        wait(25536, "B1/flux")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("2047853911291155102_B1|acquisition_shots")


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
                "9081578952441008474": "9081578952441008474",
                "7599840697439580813": "7599840697439580813",
                "-6324585606179967487": "-6324585606179967487",
                "-1215336176258838329": "-1215336176258838329",
                "-1091375789153203141": "-1091375789153203141",
                "-3415933871240039594": "-3415933871240039594",
                "1106383898849963722": "1106383898849963722",
                "-4342261629218193119": "-4342261629218193119",
                "-8913336826433880867": "-8913336826433880867",
                "-9190531229849883081": "-9190531229849883081",
                "1662669965027597395": "1662669965027597395",
                "8758847463078610179": "8758847463078610179",
                "-1482367321403949658": "-1482367321403949658",
                "4081923712229479506": "4081923712229479506",
                "-4111927393582246092": "-4111927393582246092",
                "6667461623605755155": "6667461623605755155",
                "-4609292774363304448": "-4609292774363304448",
                "4466863928624553890": "4466863928624553890",
                "5892901839408694585": "5892901839408694585",
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
                "6662083640586049351": "6662083640586049351",
                "7423174269809611220": "7423174269809611220",
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
                "2047853911291155102": "2047853911291155102_B1/acquisition",
            },
        },
    },
    "pulses": {
        "6662083640586049351": {
            "length": 40,
            "waveforms": {
                "I": "6662083640586049351_i",
                "Q": "6662083640586049351_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8637980481898379891": {
            "length": 16,
            "waveforms": {
                "single": "-8637980481898379891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2047853911291155102_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7117175930128154682_i",
                "Q": "7117175930128154682_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "2141408535289621356": {
            "length": 16,
            "waveforms": {
                "single": "2141408535289621356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "659670280288193695": {
            "length": 16,
            "waveforms": {
                "single": "659670280288193695",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4339168223292788219": {
            "length": 16,
            "waveforms": {
                "single": "4339168223292788219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4560662282491503467": {
            "length": 16,
            "waveforms": {
                "single": "4560662282491503467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3633188823320222131": {
            "length": 16,
            "waveforms": {
                "single": "-3633188823320222131",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8090639785318124904": {
            "length": 16,
            "waveforms": {
                "single": "8090639785318124904",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5833786518301423396": {
            "length": 16,
            "waveforms": {
                "single": "-5833786518301423396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6455112286188116940": {
            "length": 16,
            "waveforms": {
                "single": "-6455112286188116940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8807477954950411160": {
            "length": 16,
            "waveforms": {
                "single": "-8807477954950411160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3414532771099541285": {
            "length": 16,
            "waveforms": {
                "single": "-3414532771099541285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6609718266947244297": {
            "length": 16,
            "waveforms": {
                "single": "-6609718266947244297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6217034428911591189": {
            "length": 16,
            "waveforms": {
                "single": "6217034428911591189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8422537738555336776": {
            "length": 16,
            "waveforms": {
                "single": "-8422537738555336776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6996499827771196081": {
            "length": 16,
            "waveforms": {
                "single": "-6996499827771196081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4237930793129105172": {
            "length": 16,
            "waveforms": {
                "single": "4237930793129105172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6003283991353454665": {
            "length": 20,
            "waveforms": {
                "single": "-6003283991353454665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7151105808530323438": {
            "length": 20,
            "waveforms": {
                "single": "-7151105808530323438",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-770074174326690319": {
            "length": 20,
            "waveforms": {
                "single": "-770074174326690319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2379486392566147107": {
            "length": 20,
            "waveforms": {
                "single": "-2379486392566147107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1427685513676476544": {
            "length": 24,
            "waveforms": {
                "single": "1427685513676476544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "279863696499607771": {
            "length": 24,
            "waveforms": {
                "single": "279863696499607771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "501357755698323019": {
            "length": 24,
            "waveforms": {
                "single": "501357755698323019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8869229615023370259": {
            "length": 24,
            "waveforms": {
                "single": "-8869229615023370259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2699117443701489882": {
            "length": 28,
            "waveforms": {
                "single": "2699117443701489882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9080149077905123001": {
            "length": 28,
            "waveforms": {
                "single": "9080149077905123001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "886297972093397403": {
            "length": 28,
            "waveforms": {
                "single": "886297972093397403",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6450589005726826567": {
            "length": 28,
            "waveforms": {
                "single": "6450589005726826567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216766050794723802": {
            "length": 32,
            "waveforms": {
                "single": "-1216766050794723802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3305551719295279514": {
            "length": 32,
            "waveforms": {
                "single": "3305551719295279514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2684225951408585970": {
            "length": 32,
            "waveforms": {
                "single": "2684225951408585970",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5503311407298446377": {
            "length": 32,
            "waveforms": {
                "single": "5503311407298446377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "54665879230289536": {
            "length": 36,
            "waveforms": {
                "single": "54665879230289536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7710222849384340893": {
            "length": 36,
            "waveforms": {
                "single": "-7710222849384340893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7488728790185625645": {
            "length": 36,
            "waveforms": {
                "single": "-7488728790185625645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8633457201437089518": {
            "length": 36,
            "waveforms": {
                "single": "8633457201437089518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5290969102182458782": {
            "length": 40,
            "waveforms": {
                "single": "-5290969102182458782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "661100154824079168": {
            "length": 40,
            "waveforms": {
                "single": "661100154824079168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-57759285155694436": {
            "length": 40,
            "waveforms": {
                "single": "-57759285155694436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2410124953917988656": {
            "length": 40,
            "waveforms": {
                "single": "-2410124953917988656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8417894555141813572": {
            "length": 44,
            "waveforms": {
                "single": "-8417894555141813572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8092069659854010377": {
            "length": 44,
            "waveforms": {
                "single": "8092069659854010377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7879720322436372162": {
            "length": 44,
            "waveforms": {
                "single": "-7879720322436372162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2025184737522914272": {
            "length": 44,
            "waveforms": {
                "single": "-2025184737522914272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7937463679094883020": {
            "length": 48,
            "waveforms": {
                "single": "7937463679094883020",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3413102896563655812": {
            "length": 48,
            "waveforms": {
                "single": "-3413102896563655812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7440098298313824664": {
            "length": 48,
            "waveforms": {
                "single": "7440098298313824664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-227256758207725705": {
            "length": 48,
            "waveforms": {
                "single": "-227256758207725705",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3078310889584737387": {
            "length": 52,
            "waveforms": {
                "single": "-3078310889584737387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2856816830386022139": {
            "length": 52,
            "waveforms": {
                "single": "-2856816830386022139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7825038514708899048": {
            "length": 52,
            "waveforms": {
                "single": "7825038514708899048",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8046532573907614296": {
            "length": 52,
            "waveforms": {
                "single": "8046532573907614296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6279048520233571406": {
            "length": 56,
            "waveforms": {
                "single": "-6279048520233571406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2471876613990947755": {
            "length": 56,
            "waveforms": {
                "single": "-2471876613990947755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4795646733842624318": {
            "length": 56,
            "waveforms": {
                "single": "4795646733842624318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1429115388212362017": {
            "length": 56,
            "waveforms": {
                "single": "1429115388212362017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6993406421845791181": {
            "length": 60,
            "waveforms": {
                "single": "6993406421845791181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6931019881773757119": {
            "length": 60,
            "waveforms": {
                "single": "-6931019881773757119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5180586950237698702": {
            "length": 60,
            "waveforms": {
                "single": "5180586950237698702",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8743839353381849598": {
            "length": 60,
            "waveforms": {
                "single": "-8743839353381849598",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9081578952441008474": {
            "length": 64,
            "waveforms": {
                "single": "9081578952441008474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7599840697439580813": {
            "length": 64,
            "waveforms": {
                "single": "7599840697439580813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6324585606179967487": {
            "length": 64,
            "waveforms": {
                "single": "-6324585606179967487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1215336176258838329": {
            "length": 64,
            "waveforms": {
                "single": "-1215336176258838329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1091375789153203141": {
            "length": 68,
            "waveforms": {
                "single": "-1091375789153203141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3415933871240039594": {
            "length": 68,
            "waveforms": {
                "single": "-3415933871240039594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1106383898849963722": {
            "length": 68,
            "waveforms": {
                "single": "1106383898849963722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4342261629218193119": {
            "length": 68,
            "waveforms": {
                "single": "-4342261629218193119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8913336826433880867": {
            "length": 72,
            "waveforms": {
                "single": "-8913336826433880867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9190531229849883081": {
            "length": 72,
            "waveforms": {
                "single": "-9190531229849883081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1662669965027597395": {
            "length": 72,
            "waveforms": {
                "single": "1662669965027597395",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8758847463078610179": {
            "length": 72,
            "waveforms": {
                "single": "8758847463078610179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1482367321403949658": {
            "length": 76,
            "waveforms": {
                "single": "-1482367321403949658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4081923712229479506": {
            "length": 76,
            "waveforms": {
                "single": "4081923712229479506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4111927393582246092": {
            "length": 76,
            "waveforms": {
                "single": "-4111927393582246092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6667461623605755155": {
            "length": 76,
            "waveforms": {
                "single": "6667461623605755155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4609292774363304448": {
            "length": 80,
            "waveforms": {
                "single": "-4609292774363304448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4466863928624553890": {
            "length": 80,
            "waveforms": {
                "single": "4466863928624553890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5892901839408694585": {
            "length": 80,
            "waveforms": {
                "single": "5892901839408694585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7423174269809611220": {
            "length": 40,
            "waveforms": {
                "I": "7423174269809611220_i",
                "Q": "7423174269809611220_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6662083640586049351_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "6662083640586049351_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-8637980481898379891": {
            "samples": [0.35] + [0.0] * 15,
            "type": "arbitrary",
        },
        "7117175930128154682_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "7117175930128154682_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2141408535289621356": {
            "samples": [0.35] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "659670280288193695": {
            "samples": [0.35] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "4339168223292788219": {
            "samples": [0.35] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "4560662282491503467": {
            "samples": [0.35] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-3633188823320222131": {
            "samples": [0.35] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8090639785318124904": {
            "samples": [0.35] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-5833786518301423396": {
            "samples": [0.35] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-6455112286188116940": {
            "samples": [0.35] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8807477954950411160": {
            "samples": [0.35] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-3414532771099541285": {
            "samples": [0.35] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-6609718266947244297": {
            "samples": [0.35] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "6217034428911591189": {
            "samples": [0.35] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8422537738555336776": {
            "samples": [0.35] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6996499827771196081": {
            "samples": [0.35] * 15 + [0.0],
            "type": "arbitrary",
        },
        "4237930793129105172": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6003283991353454665": {
            "samples": [0.35] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7151105808530323438": {
            "samples": [0.35] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-770074174326690319": {
            "samples": [0.35] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2379486392566147107": {
            "sample": 0.35,
            "type": "constant",
        },
        "1427685513676476544": {
            "samples": [0.35] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "279863696499607771": {
            "samples": [0.35] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "501357755698323019": {
            "samples": [0.35] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8869229615023370259": {
            "sample": 0.35,
            "type": "constant",
        },
        "2699117443701489882": {
            "samples": [0.35] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9080149077905123001": {
            "samples": [0.35] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "886297972093397403": {
            "samples": [0.35] * 27 + [0.0],
            "type": "arbitrary",
        },
        "6450589005726826567": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1216766050794723802": {
            "samples": [0.35] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3305551719295279514": {
            "samples": [0.35] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2684225951408585970": {
            "samples": [0.35] * 31 + [0.0],
            "type": "arbitrary",
        },
        "5503311407298446377": {
            "sample": 0.35,
            "type": "constant",
        },
        "54665879230289536": {
            "samples": [0.35] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7710222849384340893": {
            "samples": [0.35] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7488728790185625645": {
            "samples": [0.35] * 35 + [0.0],
            "type": "arbitrary",
        },
        "8633457201437089518": {
            "sample": 0.35,
            "type": "constant",
        },
        "-5290969102182458782": {
            "samples": [0.35] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "661100154824079168": {
            "samples": [0.35] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-57759285155694436": {
            "samples": [0.35] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-2410124953917988656": {
            "sample": 0.35,
            "type": "constant",
        },
        "-8417894555141813572": {
            "samples": [0.35] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8092069659854010377": {
            "samples": [0.35] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7879720322436372162": {
            "samples": [0.35] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-2025184737522914272": {
            "sample": 0.35,
            "type": "constant",
        },
        "7937463679094883020": {
            "samples": [0.35] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3413102896563655812": {
            "samples": [0.35] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7440098298313824664": {
            "samples": [0.35] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-227256758207725705": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3078310889584737387": {
            "samples": [0.35] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2856816830386022139": {
            "samples": [0.35] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7825038514708899048": {
            "samples": [0.35] * 51 + [0.0],
            "type": "arbitrary",
        },
        "8046532573907614296": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6279048520233571406": {
            "samples": [0.35] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2471876613990947755": {
            "samples": [0.35] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4795646733842624318": {
            "samples": [0.35] * 55 + [0.0],
            "type": "arbitrary",
        },
        "1429115388212362017": {
            "sample": 0.35,
            "type": "constant",
        },
        "6993406421845791181": {
            "samples": [0.35] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6931019881773757119": {
            "samples": [0.35] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5180586950237698702": {
            "samples": [0.35] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-8743839353381849598": {
            "sample": 0.35,
            "type": "constant",
        },
        "9081578952441008474": {
            "samples": [0.35] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7599840697439580813": {
            "samples": [0.35] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6324585606179967487": {
            "samples": [0.35] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-1215336176258838329": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1091375789153203141": {
            "samples": [0.35] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3415933871240039594": {
            "samples": [0.35] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1106383898849963722": {
            "samples": [0.35] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-4342261629218193119": {
            "sample": 0.35,
            "type": "constant",
        },
        "-8913336826433880867": {
            "samples": [0.35] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9190531229849883081": {
            "samples": [0.35] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1662669965027597395": {
            "samples": [0.35] * 71 + [0.0],
            "type": "arbitrary",
        },
        "8758847463078610179": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1482367321403949658": {
            "samples": [0.35] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4081923712229479506": {
            "samples": [0.35] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4111927393582246092": {
            "samples": [0.35] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6667461623605755155": {
            "sample": 0.35,
            "type": "constant",
        },
        "-4609292774363304448": {
            "samples": [0.35] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4466863928624553890": {
            "samples": [0.35] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5892901839408694585": {
            "samples": [0.35] * 79 + [0.0],
            "type": "arbitrary",
        },
        "7423174269809611220_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "7423174269809611220_q": {
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "9081578952441008474": "9081578952441008474",
                "7599840697439580813": "7599840697439580813",
                "-6324585606179967487": "-6324585606179967487",
                "-1215336176258838329": "-1215336176258838329",
                "-1091375789153203141": "-1091375789153203141",
                "-3415933871240039594": "-3415933871240039594",
                "1106383898849963722": "1106383898849963722",
                "-4342261629218193119": "-4342261629218193119",
                "-8913336826433880867": "-8913336826433880867",
                "-9190531229849883081": "-9190531229849883081",
                "1662669965027597395": "1662669965027597395",
                "8758847463078610179": "8758847463078610179",
                "-1482367321403949658": "-1482367321403949658",
                "4081923712229479506": "4081923712229479506",
                "-4111927393582246092": "-4111927393582246092",
                "6667461623605755155": "6667461623605755155",
                "-4609292774363304448": "-4609292774363304448",
                "4466863928624553890": "4466863928624553890",
                "5892901839408694585": "5892901839408694585",
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
                "6662083640586049351": "6662083640586049351",
                "7423174269809611220": "7423174269809611220",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_17b",
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
                "2047853911291155102": "2047853911291155102_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_c3b",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "6662083640586049351": {
            "length": 40,
            "waveforms": {
                "I": "6662083640586049351_i",
                "Q": "6662083640586049351_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8637980481898379891": {
            "length": 16,
            "waveforms": {
                "single": "-8637980481898379891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2047853911291155102_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7117175930128154682_i",
                "Q": "7117175930128154682_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "2141408535289621356": {
            "length": 16,
            "waveforms": {
                "single": "2141408535289621356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "659670280288193695": {
            "length": 16,
            "waveforms": {
                "single": "659670280288193695",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4339168223292788219": {
            "length": 16,
            "waveforms": {
                "single": "4339168223292788219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4560662282491503467": {
            "length": 16,
            "waveforms": {
                "single": "4560662282491503467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3633188823320222131": {
            "length": 16,
            "waveforms": {
                "single": "-3633188823320222131",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8090639785318124904": {
            "length": 16,
            "waveforms": {
                "single": "8090639785318124904",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5833786518301423396": {
            "length": 16,
            "waveforms": {
                "single": "-5833786518301423396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6455112286188116940": {
            "length": 16,
            "waveforms": {
                "single": "-6455112286188116940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8807477954950411160": {
            "length": 16,
            "waveforms": {
                "single": "-8807477954950411160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3414532771099541285": {
            "length": 16,
            "waveforms": {
                "single": "-3414532771099541285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6609718266947244297": {
            "length": 16,
            "waveforms": {
                "single": "-6609718266947244297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6217034428911591189": {
            "length": 16,
            "waveforms": {
                "single": "6217034428911591189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8422537738555336776": {
            "length": 16,
            "waveforms": {
                "single": "-8422537738555336776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6996499827771196081": {
            "length": 16,
            "waveforms": {
                "single": "-6996499827771196081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4237930793129105172": {
            "length": 16,
            "waveforms": {
                "single": "4237930793129105172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6003283991353454665": {
            "length": 20,
            "waveforms": {
                "single": "-6003283991353454665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7151105808530323438": {
            "length": 20,
            "waveforms": {
                "single": "-7151105808530323438",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-770074174326690319": {
            "length": 20,
            "waveforms": {
                "single": "-770074174326690319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2379486392566147107": {
            "length": 20,
            "waveforms": {
                "single": "-2379486392566147107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1427685513676476544": {
            "length": 24,
            "waveforms": {
                "single": "1427685513676476544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "279863696499607771": {
            "length": 24,
            "waveforms": {
                "single": "279863696499607771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "501357755698323019": {
            "length": 24,
            "waveforms": {
                "single": "501357755698323019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8869229615023370259": {
            "length": 24,
            "waveforms": {
                "single": "-8869229615023370259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2699117443701489882": {
            "length": 28,
            "waveforms": {
                "single": "2699117443701489882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9080149077905123001": {
            "length": 28,
            "waveforms": {
                "single": "9080149077905123001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "886297972093397403": {
            "length": 28,
            "waveforms": {
                "single": "886297972093397403",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6450589005726826567": {
            "length": 28,
            "waveforms": {
                "single": "6450589005726826567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216766050794723802": {
            "length": 32,
            "waveforms": {
                "single": "-1216766050794723802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3305551719295279514": {
            "length": 32,
            "waveforms": {
                "single": "3305551719295279514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2684225951408585970": {
            "length": 32,
            "waveforms": {
                "single": "2684225951408585970",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5503311407298446377": {
            "length": 32,
            "waveforms": {
                "single": "5503311407298446377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "54665879230289536": {
            "length": 36,
            "waveforms": {
                "single": "54665879230289536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7710222849384340893": {
            "length": 36,
            "waveforms": {
                "single": "-7710222849384340893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7488728790185625645": {
            "length": 36,
            "waveforms": {
                "single": "-7488728790185625645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8633457201437089518": {
            "length": 36,
            "waveforms": {
                "single": "8633457201437089518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5290969102182458782": {
            "length": 40,
            "waveforms": {
                "single": "-5290969102182458782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "661100154824079168": {
            "length": 40,
            "waveforms": {
                "single": "661100154824079168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-57759285155694436": {
            "length": 40,
            "waveforms": {
                "single": "-57759285155694436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2410124953917988656": {
            "length": 40,
            "waveforms": {
                "single": "-2410124953917988656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8417894555141813572": {
            "length": 44,
            "waveforms": {
                "single": "-8417894555141813572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8092069659854010377": {
            "length": 44,
            "waveforms": {
                "single": "8092069659854010377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7879720322436372162": {
            "length": 44,
            "waveforms": {
                "single": "-7879720322436372162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2025184737522914272": {
            "length": 44,
            "waveforms": {
                "single": "-2025184737522914272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7937463679094883020": {
            "length": 48,
            "waveforms": {
                "single": "7937463679094883020",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3413102896563655812": {
            "length": 48,
            "waveforms": {
                "single": "-3413102896563655812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7440098298313824664": {
            "length": 48,
            "waveforms": {
                "single": "7440098298313824664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-227256758207725705": {
            "length": 48,
            "waveforms": {
                "single": "-227256758207725705",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3078310889584737387": {
            "length": 52,
            "waveforms": {
                "single": "-3078310889584737387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2856816830386022139": {
            "length": 52,
            "waveforms": {
                "single": "-2856816830386022139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7825038514708899048": {
            "length": 52,
            "waveforms": {
                "single": "7825038514708899048",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8046532573907614296": {
            "length": 52,
            "waveforms": {
                "single": "8046532573907614296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6279048520233571406": {
            "length": 56,
            "waveforms": {
                "single": "-6279048520233571406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2471876613990947755": {
            "length": 56,
            "waveforms": {
                "single": "-2471876613990947755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4795646733842624318": {
            "length": 56,
            "waveforms": {
                "single": "4795646733842624318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1429115388212362017": {
            "length": 56,
            "waveforms": {
                "single": "1429115388212362017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6993406421845791181": {
            "length": 60,
            "waveforms": {
                "single": "6993406421845791181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6931019881773757119": {
            "length": 60,
            "waveforms": {
                "single": "-6931019881773757119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5180586950237698702": {
            "length": 60,
            "waveforms": {
                "single": "5180586950237698702",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8743839353381849598": {
            "length": 60,
            "waveforms": {
                "single": "-8743839353381849598",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9081578952441008474": {
            "length": 64,
            "waveforms": {
                "single": "9081578952441008474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7599840697439580813": {
            "length": 64,
            "waveforms": {
                "single": "7599840697439580813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6324585606179967487": {
            "length": 64,
            "waveforms": {
                "single": "-6324585606179967487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1215336176258838329": {
            "length": 64,
            "waveforms": {
                "single": "-1215336176258838329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1091375789153203141": {
            "length": 68,
            "waveforms": {
                "single": "-1091375789153203141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3415933871240039594": {
            "length": 68,
            "waveforms": {
                "single": "-3415933871240039594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1106383898849963722": {
            "length": 68,
            "waveforms": {
                "single": "1106383898849963722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4342261629218193119": {
            "length": 68,
            "waveforms": {
                "single": "-4342261629218193119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8913336826433880867": {
            "length": 72,
            "waveforms": {
                "single": "-8913336826433880867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9190531229849883081": {
            "length": 72,
            "waveforms": {
                "single": "-9190531229849883081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1662669965027597395": {
            "length": 72,
            "waveforms": {
                "single": "1662669965027597395",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8758847463078610179": {
            "length": 72,
            "waveforms": {
                "single": "8758847463078610179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1482367321403949658": {
            "length": 76,
            "waveforms": {
                "single": "-1482367321403949658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4081923712229479506": {
            "length": 76,
            "waveforms": {
                "single": "4081923712229479506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4111927393582246092": {
            "length": 76,
            "waveforms": {
                "single": "-4111927393582246092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6667461623605755155": {
            "length": 76,
            "waveforms": {
                "single": "6667461623605755155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4609292774363304448": {
            "length": 80,
            "waveforms": {
                "single": "-4609292774363304448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4466863928624553890": {
            "length": 80,
            "waveforms": {
                "single": "4466863928624553890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5892901839408694585": {
            "length": 80,
            "waveforms": {
                "single": "5892901839408694585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7423174269809611220": {
            "length": 40,
            "waveforms": {
                "I": "7423174269809611220_i",
                "Q": "7423174269809611220_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6662083640586049351_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6662083640586049351_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8637980481898379891": {
            "samples": [0.35] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7117175930128154682_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "7117175930128154682_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2141408535289621356": {
            "samples": [0.35] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "659670280288193695": {
            "samples": [0.35] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4339168223292788219": {
            "samples": [0.35] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4560662282491503467": {
            "samples": [0.35] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3633188823320222131": {
            "samples": [0.35] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8090639785318124904": {
            "samples": [0.35] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5833786518301423396": {
            "samples": [0.35] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6455112286188116940": {
            "samples": [0.35] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8807477954950411160": {
            "samples": [0.35] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3414532771099541285": {
            "samples": [0.35] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6609718266947244297": {
            "samples": [0.35] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6217034428911591189": {
            "samples": [0.35] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8422537738555336776": {
            "samples": [0.35] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6996499827771196081": {
            "samples": [0.35] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4237930793129105172": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6003283991353454665": {
            "samples": [0.35] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7151105808530323438": {
            "samples": [0.35] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-770074174326690319": {
            "samples": [0.35] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2379486392566147107": {
            "sample": 0.35,
            "type": "constant",
        },
        "1427685513676476544": {
            "samples": [0.35] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "279863696499607771": {
            "samples": [0.35] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "501357755698323019": {
            "samples": [0.35] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8869229615023370259": {
            "sample": 0.35,
            "type": "constant",
        },
        "2699117443701489882": {
            "samples": [0.35] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9080149077905123001": {
            "samples": [0.35] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "886297972093397403": {
            "samples": [0.35] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6450589005726826567": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1216766050794723802": {
            "samples": [0.35] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3305551719295279514": {
            "samples": [0.35] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2684225951408585970": {
            "samples": [0.35] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5503311407298446377": {
            "sample": 0.35,
            "type": "constant",
        },
        "54665879230289536": {
            "samples": [0.35] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7710222849384340893": {
            "samples": [0.35] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7488728790185625645": {
            "samples": [0.35] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8633457201437089518": {
            "sample": 0.35,
            "type": "constant",
        },
        "-5290969102182458782": {
            "samples": [0.35] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "661100154824079168": {
            "samples": [0.35] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-57759285155694436": {
            "samples": [0.35] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2410124953917988656": {
            "sample": 0.35,
            "type": "constant",
        },
        "-8417894555141813572": {
            "samples": [0.35] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8092069659854010377": {
            "samples": [0.35] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7879720322436372162": {
            "samples": [0.35] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2025184737522914272": {
            "sample": 0.35,
            "type": "constant",
        },
        "7937463679094883020": {
            "samples": [0.35] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3413102896563655812": {
            "samples": [0.35] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7440098298313824664": {
            "samples": [0.35] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-227256758207725705": {
            "sample": 0.35,
            "type": "constant",
        },
        "-3078310889584737387": {
            "samples": [0.35] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2856816830386022139": {
            "samples": [0.35] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7825038514708899048": {
            "samples": [0.35] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8046532573907614296": {
            "sample": 0.35,
            "type": "constant",
        },
        "-6279048520233571406": {
            "samples": [0.35] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2471876613990947755": {
            "samples": [0.35] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4795646733842624318": {
            "samples": [0.35] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1429115388212362017": {
            "sample": 0.35,
            "type": "constant",
        },
        "6993406421845791181": {
            "samples": [0.35] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6931019881773757119": {
            "samples": [0.35] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5180586950237698702": {
            "samples": [0.35] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8743839353381849598": {
            "sample": 0.35,
            "type": "constant",
        },
        "9081578952441008474": {
            "samples": [0.35] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7599840697439580813": {
            "samples": [0.35] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6324585606179967487": {
            "samples": [0.35] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1215336176258838329": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1091375789153203141": {
            "samples": [0.35] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3415933871240039594": {
            "samples": [0.35] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1106383898849963722": {
            "samples": [0.35] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4342261629218193119": {
            "sample": 0.35,
            "type": "constant",
        },
        "-8913336826433880867": {
            "samples": [0.35] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9190531229849883081": {
            "samples": [0.35] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1662669965027597395": {
            "samples": [0.35] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8758847463078610179": {
            "sample": 0.35,
            "type": "constant",
        },
        "-1482367321403949658": {
            "samples": [0.35] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4081923712229479506": {
            "samples": [0.35] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4111927393582246092": {
            "samples": [0.35] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6667461623605755155": {
            "sample": 0.35,
            "type": "constant",
        },
        "-4609292774363304448": {
            "samples": [0.35] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4466863928624553890": {
            "samples": [0.35] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5892901839408694585": {
            "samples": [0.35] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7423174269809611220_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7423174269809611220_q": {
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
        "B1/drive_mixer_17b": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/acquisition_mixer_c3b": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

