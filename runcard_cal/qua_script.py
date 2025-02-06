
# Single QUA script generated at 2025-02-06 16:19:46.966107
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("8799194169894379639", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("6474636087807543186", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("5326814270630674413", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("5548308329829389661", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-2216580398785240768", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("3347710634848188396", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-4319644421673361973", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("5933248546224464045", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("6154742605423179293", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("8131008234227630908", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("8352502293426346156", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("2806323093265109255", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-4861031963256441114", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-4639537904057725866", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-2663272275253274251", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-2441778216054559003", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-3589600033231427776", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("2791431600972205343", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("659901007629859579", "B4/drive")
        wait(11, "B4/flux")
        play("-5790197728212629041", "B4/flux")
        wait(46, "B4/drive")
        play("1420991636853421448", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-7050225023228966441", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-7050225023228966441_B4|acquisition_shots")


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
                    "output_mode": "triggered",
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
                "8799194169894379639": "8799194169894379639",
                "6474636087807543186": "6474636087807543186",
                "5326814270630674413": "5326814270630674413",
                "5548308329829389661": "5548308329829389661",
                "-2216580398785240768": "-2216580398785240768",
                "3347710634848188396": "3347710634848188396",
                "-4319644421673361973": "-4319644421673361973",
                "5933248546224464045": "5933248546224464045",
                "6154742605423179293": "6154742605423179293",
                "8131008234227630908": "8131008234227630908",
                "8352502293426346156": "8352502293426346156",
                "2806323093265109255": "2806323093265109255",
                "-4861031963256441114": "-4861031963256441114",
                "-4639537904057725866": "-4639537904057725866",
                "-2663272275253274251": "-2663272275253274251",
                "-2441778216054559003": "-2441778216054559003",
                "-3589600033231427776": "-3589600033231427776",
                "2791431600972205343": "2791431600972205343",
                "-5790197728212629041": "-5790197728212629041",
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
                "659901007629859579": "659901007629859579",
                "1420991636853421448": "1420991636853421448",
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
                "-7050225023228966441": "-7050225023228966441_B4/acquisition",
            },
        },
    },
    "pulses": {
        "659901007629859579": {
            "length": 40,
            "waveforms": {
                "I": "659901007629859579_i",
                "Q": "659901007629859579_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2401715869113018409": {
            "length": 16,
            "waveforms": {
                "single": "2401715869113018409",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7050225023228966441_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3717283734561976361_i",
                "Q": "-3717283734561976361_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "8905053041377849346": {
            "length": 16,
            "waveforms": {
                "single": "8905053041377849346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1237697984856298977": {
            "length": 16,
            "waveforms": {
                "single": "1237697984856298977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4056783440746159384": {
            "length": 16,
            "waveforms": {
                "single": "4056783440746159384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1391862087321997457": {
            "length": 16,
            "waveforms": {
                "single": "-1391862087321997457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6139104608147432921": {
            "length": 16,
            "waveforms": {
                "single": "-6139104608147432921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8935256756737912638": {
            "length": 16,
            "waveforms": {
                "single": "-8935256756737912638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4814093777169546724": {
            "length": 16,
            "waveforms": {
                "single": "-4814093777169546724",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6737497068734745775": {
            "length": 16,
            "waveforms": {
                "single": "-6737497068734745775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6260601476906649000": {
            "length": 16,
            "waveforms": {
                "single": "6260601476906649000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1513358956081213536": {
            "length": 16,
            "waveforms": {
                "single": "1513358956081213536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8458361164909815863": {
            "length": 16,
            "waveforms": {
                "single": "8458361164909815863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "693472436295185434": {
            "length": 16,
            "waveforms": {
                "single": "693472436295185434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5313323878478268810": {
            "length": 16,
            "waveforms": {
                "single": "5313323878478268810",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6867035752500438632": {
            "length": 16,
            "waveforms": {
                "single": "6867035752500438632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8843301381304890247": {
            "length": 16,
            "waveforms": {
                "single": "8843301381304890247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9064795440503605495": {
            "length": 20,
            "waveforms": {
                "single": "9064795440503605495",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5702450690201351597": {
            "length": 20,
            "waveforms": {
                "single": "-5702450690201351597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5480956631002636349": {
            "length": 20,
            "waveforms": {
                "single": "-5480956631002636349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8332010762379648031": {
            "length": 20,
            "waveforms": {
                "single": "-8332010762379648031",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1950979128176014912": {
            "length": 24,
            "waveforms": {
                "single": "-1950979128176014912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4303344796938309132": {
            "length": 24,
            "waveforms": {
                "single": "-4303344796938309132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1950012874027294860": {
            "length": 24,
            "waveforms": {
                "single": "1950012874027294860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "468274619025867199": {
            "length": 24,
            "waveforms": {
                "single": "468274619025867199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7725576486785858399": {
            "length": 28,
            "waveforms": {
                "single": "-7725576486785858399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3127624708091622077": {
            "length": 28,
            "waveforms": {
                "single": "3127624708091622077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8222941867566916755": {
            "length": 28,
            "waveforms": {
                "single": "-8222941867566916755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-17412578339924976": {
            "length": 28,
            "waveforms": {
                "single": "-17412578339924976",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5546878455293504188": {
            "length": 32,
            "waveforms": {
                "single": "5546878455293504188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-73112922557211942": {
            "length": 32,
            "waveforms": {
                "single": "-73112922557211942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3268298418404914954": {
            "length": 32,
            "waveforms": {
                "single": "-3268298418404914954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7172721112144941626": {
            "length": 32,
            "waveforms": {
                "single": "-7172721112144941626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5931818671688578572": {
            "length": 36,
            "waveforms": {
                "single": "5931818671688578572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7357856582472719267": {
            "length": 36,
            "waveforms": {
                "single": "7357856582472719267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8613933399817663272": {
            "length": 36,
            "waveforms": {
                "single": "-8613933399817663272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2661864142811125322": {
            "length": 36,
            "waveforms": {
                "single": "-2661864142811125322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7203250601713591910": {
            "length": 40,
            "waveforms": {
                "single": "7203250601713591910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-464104454807958459": {
            "length": 40,
            "waveforms": {
                "single": "-464104454807958459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-340144067702323271": {
            "length": 40,
            "waveforms": {
                "single": "-340144067702323271",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961469835589016815": {
            "length": 40,
            "waveforms": {
                "single": "-961469835589016815",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2443208090590444476": {
            "length": 44,
            "waveforms": {
                "single": "-2443208090590444476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3591029907767313249": {
            "length": 44,
            "waveforms": {
                "single": "-3591029907767313249",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7188359109420687998": {
            "length": 44,
            "waveforms": {
                "single": "7188359109420687998",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6736067194198860302": {
            "length": 44,
            "waveforms": {
                "single": "-6736067194198860302",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1171776160565431138": {
            "length": 48,
            "waveforms": {
                "single": "-1171776160565431138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3206089691372238865": {
            "length": 48,
            "waveforms": {
                "single": "-3206089691372238865",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2984595632173523617": {
            "length": 48,
            "waveforms": {
                "single": "-2984595632173523617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6179781128021226629": {
            "length": 48,
            "waveforms": {
                "single": "-6179781128021226629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "916396370029786155": {
            "length": 52,
            "waveforms": {
                "single": "916396370029786155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1408161712057050298": {
            "length": 52,
            "waveforms": {
                "single": "-1408161712057050298",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8844731255840775720": {
            "length": 52,
            "waveforms": {
                "single": "8844731255840775720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9066225315039490968": {
            "length": 52,
            "waveforms": {
                "single": "9066225315039490968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8347365875059717364": {
            "length": 56,
            "waveforms": {
                "single": "8347365875059717364",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6865627620058289703": {
            "length": 56,
            "waveforms": {
                "single": "6865627620058289703",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3375587164424270134": {
            "length": 56,
            "waveforms": {
                "single": "-3375587164424270134",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1949549253640129439": {
            "length": 56,
            "waveforms": {
                "single": "-1949549253640129439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1857622652602494212": {
            "length": 60,
            "waveforms": {
                "single": "1857622652602494212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "248210434363037424": {
            "length": 60,
            "waveforms": {
                "single": "248210434363037424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6502512617383624924": {
            "length": 60,
            "waveforms": {
                "single": "-6502512617383624924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4276876399804376323": {
            "length": 60,
            "waveforms": {
                "single": "4276876399804376323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8799194169894379639": {
            "length": 64,
            "waveforms": {
                "single": "8799194169894379639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6474636087807543186": {
            "length": 64,
            "waveforms": {
                "single": "6474636087807543186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5326814270630674413": {
            "length": 64,
            "waveforms": {
                "single": "5326814270630674413",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5548308329829389661": {
            "length": 64,
            "waveforms": {
                "single": "5548308329829389661",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2216580398785240768": {
            "length": 68,
            "waveforms": {
                "single": "-2216580398785240768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3347710634848188396": {
            "length": 68,
            "waveforms": {
                "single": "3347710634848188396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4319644421673361973": {
            "length": 68,
            "waveforms": {
                "single": "-4319644421673361973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5933248546224464045": {
            "length": 68,
            "waveforms": {
                "single": "5933248546224464045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6154742605423179293": {
            "length": 72,
            "waveforms": {
                "single": "6154742605423179293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8131008234227630908": {
            "length": 72,
            "waveforms": {
                "single": "8131008234227630908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8352502293426346156": {
            "length": 72,
            "waveforms": {
                "single": "8352502293426346156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2806323093265109255": {
            "length": 72,
            "waveforms": {
                "single": "2806323093265109255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4861031963256441114": {
            "length": 76,
            "waveforms": {
                "single": "-4861031963256441114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4639537904057725866": {
            "length": 76,
            "waveforms": {
                "single": "-4639537904057725866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2663272275253274251": {
            "length": 76,
            "waveforms": {
                "single": "-2663272275253274251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2441778216054559003": {
            "length": 76,
            "waveforms": {
                "single": "-2441778216054559003",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3589600033231427776": {
            "length": 80,
            "waveforms": {
                "single": "-3589600033231427776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2791431600972205343": {
            "length": 80,
            "waveforms": {
                "single": "2791431600972205343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5790197728212629041": {
            "length": 80,
            "waveforms": {
                "single": "-5790197728212629041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1420991636853421448": {
            "length": 40,
            "waveforms": {
                "I": "1420991636853421448_i",
                "Q": "1420991636853421448_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "659901007629859579_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "659901007629859579_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "2401715869113018409": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-3717283734561976361_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-3717283734561976361_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8905053041377849346": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "1237697984856298977": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "4056783440746159384": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-1391862087321997457": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-6139104608147432921": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-8935256756737912638": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-4814093777169546724": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-6737497068734745775": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "6260601476906649000": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "1513358956081213536": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8458361164909815863": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "693472436295185434": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5313323878478268810": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6867035752500438632": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "8843301381304890247": {
            "sample": 0.25,
            "type": "constant",
        },
        "9064795440503605495": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5702450690201351597": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5480956631002636349": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-8332010762379648031": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1950979128176014912": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4303344796938309132": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1950012874027294860": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "468274619025867199": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7725576486785858399": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3127624708091622077": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8222941867566916755": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-17412578339924976": {
            "sample": 0.25,
            "type": "constant",
        },
        "5546878455293504188": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-73112922557211942": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3268298418404914954": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-7172721112144941626": {
            "sample": 0.25,
            "type": "constant",
        },
        "5931818671688578572": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7357856582472719267": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8613933399817663272": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-2661864142811125322": {
            "sample": 0.25,
            "type": "constant",
        },
        "7203250601713591910": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-464104454807958459": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-340144067702323271": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-961469835589016815": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2443208090590444476": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3591029907767313249": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7188359109420687998": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-6736067194198860302": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1171776160565431138": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3206089691372238865": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2984595632173523617": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-6179781128021226629": {
            "sample": 0.25,
            "type": "constant",
        },
        "916396370029786155": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1408161712057050298": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8844731255840775720": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "9066225315039490968": {
            "sample": 0.25,
            "type": "constant",
        },
        "8347365875059717364": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6865627620058289703": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3375587164424270134": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-1949549253640129439": {
            "sample": 0.25,
            "type": "constant",
        },
        "1857622652602494212": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "248210434363037424": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6502512617383624924": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "4276876399804376323": {
            "sample": 0.25,
            "type": "constant",
        },
        "8799194169894379639": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6474636087807543186": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5326814270630674413": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "5548308329829389661": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2216580398785240768": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3347710634848188396": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4319644421673361973": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5933248546224464045": {
            "sample": 0.25,
            "type": "constant",
        },
        "6154742605423179293": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8131008234227630908": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8352502293426346156": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "2806323093265109255": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4861031963256441114": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4639537904057725866": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2663272275253274251": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-2441778216054559003": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3589600033231427776": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2791431600972205343": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5790197728212629041": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "1420991636853421448_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "1420991636853421448_q": {
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
                "8799194169894379639": "8799194169894379639",
                "6474636087807543186": "6474636087807543186",
                "5326814270630674413": "5326814270630674413",
                "5548308329829389661": "5548308329829389661",
                "-2216580398785240768": "-2216580398785240768",
                "3347710634848188396": "3347710634848188396",
                "-4319644421673361973": "-4319644421673361973",
                "5933248546224464045": "5933248546224464045",
                "6154742605423179293": "6154742605423179293",
                "8131008234227630908": "8131008234227630908",
                "8352502293426346156": "8352502293426346156",
                "2806323093265109255": "2806323093265109255",
                "-4861031963256441114": "-4861031963256441114",
                "-4639537904057725866": "-4639537904057725866",
                "-2663272275253274251": "-2663272275253274251",
                "-2441778216054559003": "-2441778216054559003",
                "-3589600033231427776": "-3589600033231427776",
                "2791431600972205343": "2791431600972205343",
                "-5790197728212629041": "-5790197728212629041",
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
            "intermediate_frequency": 109615374.0,
            "operations": {
                "659901007629859579": "659901007629859579",
                "1420991636853421448": "1420991636853421448",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_c45",
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
            "intermediate_frequency": 330300527.0,
            "operations": {
                "-7050225023228966441": "-7050225023228966441_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_534",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "659901007629859579": {
            "length": 40,
            "waveforms": {
                "I": "659901007629859579_i",
                "Q": "659901007629859579_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2401715869113018409": {
            "length": 16,
            "waveforms": {
                "single": "2401715869113018409",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7050225023228966441_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3717283734561976361_i",
                "Q": "-3717283734561976361_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "8905053041377849346": {
            "length": 16,
            "waveforms": {
                "single": "8905053041377849346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1237697984856298977": {
            "length": 16,
            "waveforms": {
                "single": "1237697984856298977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4056783440746159384": {
            "length": 16,
            "waveforms": {
                "single": "4056783440746159384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1391862087321997457": {
            "length": 16,
            "waveforms": {
                "single": "-1391862087321997457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6139104608147432921": {
            "length": 16,
            "waveforms": {
                "single": "-6139104608147432921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8935256756737912638": {
            "length": 16,
            "waveforms": {
                "single": "-8935256756737912638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4814093777169546724": {
            "length": 16,
            "waveforms": {
                "single": "-4814093777169546724",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6737497068734745775": {
            "length": 16,
            "waveforms": {
                "single": "-6737497068734745775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6260601476906649000": {
            "length": 16,
            "waveforms": {
                "single": "6260601476906649000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1513358956081213536": {
            "length": 16,
            "waveforms": {
                "single": "1513358956081213536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8458361164909815863": {
            "length": 16,
            "waveforms": {
                "single": "8458361164909815863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "693472436295185434": {
            "length": 16,
            "waveforms": {
                "single": "693472436295185434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5313323878478268810": {
            "length": 16,
            "waveforms": {
                "single": "5313323878478268810",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6867035752500438632": {
            "length": 16,
            "waveforms": {
                "single": "6867035752500438632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8843301381304890247": {
            "length": 16,
            "waveforms": {
                "single": "8843301381304890247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9064795440503605495": {
            "length": 20,
            "waveforms": {
                "single": "9064795440503605495",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5702450690201351597": {
            "length": 20,
            "waveforms": {
                "single": "-5702450690201351597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5480956631002636349": {
            "length": 20,
            "waveforms": {
                "single": "-5480956631002636349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8332010762379648031": {
            "length": 20,
            "waveforms": {
                "single": "-8332010762379648031",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1950979128176014912": {
            "length": 24,
            "waveforms": {
                "single": "-1950979128176014912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4303344796938309132": {
            "length": 24,
            "waveforms": {
                "single": "-4303344796938309132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1950012874027294860": {
            "length": 24,
            "waveforms": {
                "single": "1950012874027294860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "468274619025867199": {
            "length": 24,
            "waveforms": {
                "single": "468274619025867199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7725576486785858399": {
            "length": 28,
            "waveforms": {
                "single": "-7725576486785858399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3127624708091622077": {
            "length": 28,
            "waveforms": {
                "single": "3127624708091622077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8222941867566916755": {
            "length": 28,
            "waveforms": {
                "single": "-8222941867566916755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-17412578339924976": {
            "length": 28,
            "waveforms": {
                "single": "-17412578339924976",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5546878455293504188": {
            "length": 32,
            "waveforms": {
                "single": "5546878455293504188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-73112922557211942": {
            "length": 32,
            "waveforms": {
                "single": "-73112922557211942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3268298418404914954": {
            "length": 32,
            "waveforms": {
                "single": "-3268298418404914954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7172721112144941626": {
            "length": 32,
            "waveforms": {
                "single": "-7172721112144941626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5931818671688578572": {
            "length": 36,
            "waveforms": {
                "single": "5931818671688578572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7357856582472719267": {
            "length": 36,
            "waveforms": {
                "single": "7357856582472719267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8613933399817663272": {
            "length": 36,
            "waveforms": {
                "single": "-8613933399817663272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2661864142811125322": {
            "length": 36,
            "waveforms": {
                "single": "-2661864142811125322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7203250601713591910": {
            "length": 40,
            "waveforms": {
                "single": "7203250601713591910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-464104454807958459": {
            "length": 40,
            "waveforms": {
                "single": "-464104454807958459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-340144067702323271": {
            "length": 40,
            "waveforms": {
                "single": "-340144067702323271",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961469835589016815": {
            "length": 40,
            "waveforms": {
                "single": "-961469835589016815",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2443208090590444476": {
            "length": 44,
            "waveforms": {
                "single": "-2443208090590444476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3591029907767313249": {
            "length": 44,
            "waveforms": {
                "single": "-3591029907767313249",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7188359109420687998": {
            "length": 44,
            "waveforms": {
                "single": "7188359109420687998",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6736067194198860302": {
            "length": 44,
            "waveforms": {
                "single": "-6736067194198860302",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1171776160565431138": {
            "length": 48,
            "waveforms": {
                "single": "-1171776160565431138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3206089691372238865": {
            "length": 48,
            "waveforms": {
                "single": "-3206089691372238865",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2984595632173523617": {
            "length": 48,
            "waveforms": {
                "single": "-2984595632173523617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6179781128021226629": {
            "length": 48,
            "waveforms": {
                "single": "-6179781128021226629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "916396370029786155": {
            "length": 52,
            "waveforms": {
                "single": "916396370029786155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1408161712057050298": {
            "length": 52,
            "waveforms": {
                "single": "-1408161712057050298",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8844731255840775720": {
            "length": 52,
            "waveforms": {
                "single": "8844731255840775720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9066225315039490968": {
            "length": 52,
            "waveforms": {
                "single": "9066225315039490968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8347365875059717364": {
            "length": 56,
            "waveforms": {
                "single": "8347365875059717364",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6865627620058289703": {
            "length": 56,
            "waveforms": {
                "single": "6865627620058289703",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3375587164424270134": {
            "length": 56,
            "waveforms": {
                "single": "-3375587164424270134",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1949549253640129439": {
            "length": 56,
            "waveforms": {
                "single": "-1949549253640129439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1857622652602494212": {
            "length": 60,
            "waveforms": {
                "single": "1857622652602494212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "248210434363037424": {
            "length": 60,
            "waveforms": {
                "single": "248210434363037424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6502512617383624924": {
            "length": 60,
            "waveforms": {
                "single": "-6502512617383624924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4276876399804376323": {
            "length": 60,
            "waveforms": {
                "single": "4276876399804376323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8799194169894379639": {
            "length": 64,
            "waveforms": {
                "single": "8799194169894379639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6474636087807543186": {
            "length": 64,
            "waveforms": {
                "single": "6474636087807543186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5326814270630674413": {
            "length": 64,
            "waveforms": {
                "single": "5326814270630674413",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5548308329829389661": {
            "length": 64,
            "waveforms": {
                "single": "5548308329829389661",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2216580398785240768": {
            "length": 68,
            "waveforms": {
                "single": "-2216580398785240768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3347710634848188396": {
            "length": 68,
            "waveforms": {
                "single": "3347710634848188396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4319644421673361973": {
            "length": 68,
            "waveforms": {
                "single": "-4319644421673361973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5933248546224464045": {
            "length": 68,
            "waveforms": {
                "single": "5933248546224464045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6154742605423179293": {
            "length": 72,
            "waveforms": {
                "single": "6154742605423179293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8131008234227630908": {
            "length": 72,
            "waveforms": {
                "single": "8131008234227630908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8352502293426346156": {
            "length": 72,
            "waveforms": {
                "single": "8352502293426346156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2806323093265109255": {
            "length": 72,
            "waveforms": {
                "single": "2806323093265109255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4861031963256441114": {
            "length": 76,
            "waveforms": {
                "single": "-4861031963256441114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4639537904057725866": {
            "length": 76,
            "waveforms": {
                "single": "-4639537904057725866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2663272275253274251": {
            "length": 76,
            "waveforms": {
                "single": "-2663272275253274251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2441778216054559003": {
            "length": 76,
            "waveforms": {
                "single": "-2441778216054559003",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3589600033231427776": {
            "length": 80,
            "waveforms": {
                "single": "-3589600033231427776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2791431600972205343": {
            "length": 80,
            "waveforms": {
                "single": "2791431600972205343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5790197728212629041": {
            "length": 80,
            "waveforms": {
                "single": "-5790197728212629041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1420991636853421448": {
            "length": 40,
            "waveforms": {
                "I": "1420991636853421448_i",
                "Q": "1420991636853421448_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "659901007629859579_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "659901007629859579_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2401715869113018409": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3717283734561976361_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-3717283734561976361_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8905053041377849346": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1237697984856298977": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4056783440746159384": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1391862087321997457": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6139104608147432921": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8935256756737912638": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4814093777169546724": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6737497068734745775": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6260601476906649000": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1513358956081213536": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8458361164909815863": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "693472436295185434": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5313323878478268810": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6867035752500438632": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8843301381304890247": {
            "sample": 0.25,
            "type": "constant",
        },
        "9064795440503605495": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5702450690201351597": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5480956631002636349": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8332010762379648031": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1950979128176014912": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4303344796938309132": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1950012874027294860": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "468274619025867199": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7725576486785858399": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3127624708091622077": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8222941867566916755": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-17412578339924976": {
            "sample": 0.25,
            "type": "constant",
        },
        "5546878455293504188": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-73112922557211942": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3268298418404914954": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7172721112144941626": {
            "sample": 0.25,
            "type": "constant",
        },
        "5931818671688578572": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7357856582472719267": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8613933399817663272": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2661864142811125322": {
            "sample": 0.25,
            "type": "constant",
        },
        "7203250601713591910": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-464104454807958459": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-340144067702323271": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-961469835589016815": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2443208090590444476": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3591029907767313249": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7188359109420687998": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6736067194198860302": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1171776160565431138": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3206089691372238865": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2984595632173523617": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6179781128021226629": {
            "sample": 0.25,
            "type": "constant",
        },
        "916396370029786155": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1408161712057050298": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8844731255840775720": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9066225315039490968": {
            "sample": 0.25,
            "type": "constant",
        },
        "8347365875059717364": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6865627620058289703": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3375587164424270134": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1949549253640129439": {
            "sample": 0.25,
            "type": "constant",
        },
        "1857622652602494212": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "248210434363037424": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6502512617383624924": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4276876399804376323": {
            "sample": 0.25,
            "type": "constant",
        },
        "8799194169894379639": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6474636087807543186": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5326814270630674413": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5548308329829389661": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2216580398785240768": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3347710634848188396": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4319644421673361973": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5933248546224464045": {
            "sample": 0.25,
            "type": "constant",
        },
        "6154742605423179293": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8131008234227630908": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8352502293426346156": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2806323093265109255": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4861031963256441114": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4639537904057725866": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2663272275253274251": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2441778216054559003": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3589600033231427776": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2791431600972205343": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5790197728212629041": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1420991636853421448_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1420991636853421448_q": {
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
        "B4/drive_mixer_c45": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_534": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

