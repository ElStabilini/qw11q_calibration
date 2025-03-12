
# Single QUA script generated at 2025-03-12 13:59:30.667253
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
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
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("76342838186428103", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-3118842657661274909", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-2897348598462559661", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("1624969171627443655", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-699588910459392798", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("5154946674454065092", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-2512408382067485277", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("2009909388022518039", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("7574200421655947203", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-93154634865603166", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-1240976452042471939", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("5140055182161161180", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-8784371121458387120", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("1178277295159410172", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-856036235647397555", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("6411487112186174518", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("-8228085055280753447", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("1563217511554484556", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("8319816774687419796", "B4/drive")
        wait(11, "B4/flux")
        play("8830740859388056629", "B4/flux")
        wait(46, "B4/drive")
        play("9080907403910981665", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6914001376397344256", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-6914001376397344256_B4|acquisition_shots")


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
                "76342838186428103": "76342838186428103",
                "-3118842657661274909": "-3118842657661274909",
                "-2897348598462559661": "-2897348598462559661",
                "1624969171627443655": "1624969171627443655",
                "-699588910459392798": "-699588910459392798",
                "5154946674454065092": "5154946674454065092",
                "-2512408382067485277": "-2512408382067485277",
                "2009909388022518039": "2009909388022518039",
                "7574200421655947203": "7574200421655947203",
                "-93154634865603166": "-93154634865603166",
                "-1240976452042471939": "-1240976452042471939",
                "5140055182161161180": "5140055182161161180",
                "-8784371121458387120": "-8784371121458387120",
                "1178277295159410172": "1178277295159410172",
                "-856036235647397555": "-856036235647397555",
                "6411487112186174518": "6411487112186174518",
                "-8228085055280753447": "-8228085055280753447",
                "1563217511554484556": "1563217511554484556",
                "8830740859388056629": "8830740859388056629",
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
            "intermediate_frequency": 330300527.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-6914001376397344256": "-6914001376397344256_B4/acquisition",
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
                "8319816774687419796": "8319816774687419796",
                "9080907403910981665": "9080907403910981665",
            },
        },
    },
    "pulses": {
        "8319816774687419796": {
            "length": 40,
            "waveforms": {
                "I": "8319816774687419796_i",
                "Q": "8319816774687419796_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2188275792564588673": {
            "length": 16,
            "waveforms": {
                "single": "-2188275792564588673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6914001376397344256_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6505297470054341181_i",
                "Q": "6505297470054341181_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-7734454992725825574": {
            "length": 16,
            "waveforms": {
                "single": "-7734454992725825574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4388873487545789938": {
            "length": 16,
            "waveforms": {
                "single": "-4388873487545789938",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2962835576761649243": {
            "length": 16,
            "waveforms": {
                "single": "-2962835576761649243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5315201245523943463": {
            "length": 16,
            "waveforms": {
                "single": "-5315201245523943463",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5464187771664057784": {
            "length": 16,
            "waveforms": {
                "single": "5464187771664057784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3117441557520776600": {
            "length": 16,
            "waveforms": {
                "single": "-3117441557520776600",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7661947459667224647": {
            "length": 16,
            "waveforms": {
                "single": "7661947459667224647",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2115768259505987746": {
            "length": 16,
            "waveforms": {
                "single": "2115768259505987746",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2337262318704702994": {
            "length": 16,
            "waveforms": {
                "single": "2337262318704702994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4313527947509154609": {
            "length": 16,
            "waveforms": {
                "single": "4313527947509154609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4535022006707869857": {
            "length": 16,
            "waveforms": {
                "single": "4535022006707869857",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3132333049813680512": {
            "length": 16,
            "waveforms": {
                "single": "-3132333049813680512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7120559918084145506": {
            "length": 16,
            "waveforms": {
                "single": "7120559918084145506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5761893121991976946": {
            "length": 16,
            "waveforms": {
                "single": "-5761893121991976946",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4919962223102944241": {
            "length": 16,
            "waveforms": {
                "single": "4919962223102944241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5141456282301659489": {
            "length": 20,
            "waveforms": {
                "single": "5141456282301659489",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1946270786453956477": {
            "length": 20,
            "waveforms": {
                "single": "1946270786453956477",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1669076383037954263": {
            "length": 20,
            "waveforms": {
                "single": "1669076383037954263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1890570442236669511": {
            "length": 20,
            "waveforms": {
                "single": "1890570442236669511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1475960903393592790": {
            "length": 24,
            "waveforms": {
                "single": "-1475960903393592790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1254466844194877542": {
            "length": 24,
            "waveforms": {
                "single": "-1254466844194877542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3757248913633171556": {
            "length": 24,
            "waveforms": {
                "single": "3757248913633171556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2275510658631743895": {
            "length": 24,
            "waveforms": {
                "single": "2275510658631743895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-919674837215959117": {
            "length": 28,
            "waveforms": {
                "single": "-919674837215959117",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6176502660835053667": {
            "length": 28,
            "waveforms": {
                "single": "6176502660835053667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3824136992072759447": {
            "length": 28,
            "waveforms": {
                "single": "3824136992072759447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8740263910047876512": {
            "length": 28,
            "waveforms": {
                "single": "-8740263910047876512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1623539297091558182": {
            "length": 32,
            "waveforms": {
                "single": "1623539297091558182",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3996452080759157948": {
            "length": 32,
            "waveforms": {
                "single": "-3996452080759157948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7191637576606860960": {
            "length": 32,
            "waveforms": {
                "single": "-7191637576606860960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8673375831608288621": {
            "length": 32,
            "waveforms": {
                "single": "-8673375831608288621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4993877888603694097": {
            "length": 36,
            "waveforms": {
                "single": "-4993877888603694097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4772383829404978849": {
            "length": 36,
            "waveforms": {
                "single": "-4772383829404978849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6806697360211786576": {
            "length": 36,
            "waveforms": {
                "single": "-6806697360211786576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1242406326578357412": {
            "length": 36,
            "waveforms": {
                "single": "-1242406326578357412",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5853771171472655372": {
            "length": 40,
            "waveforms": {
                "single": "5853771171472655372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4387443613009904465": {
            "length": 40,
            "waveforms": {
                "single": "-4387443613009904465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4165949553811189217": {
            "length": 40,
            "waveforms": {
                "single": "-4165949553811189217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6188563178451573797": {
            "length": 40,
            "waveforms": {
                "single": "6188563178451573797",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6410057237650289045": {
            "length": 44,
            "waveforms": {
                "single": "6410057237650289045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7514369065969259255": {
            "length": 44,
            "waveforms": {
                "single": "-7514369065969259255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3265019951218741992": {
            "length": 44,
            "waveforms": {
                "single": "3265019951218741992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8829310984852171156": {
            "length": 44,
            "waveforms": {
                "single": "8829310984852171156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7253389236679820059": {
            "length": 48,
            "waveforms": {
                "single": "-7253389236679820059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7031895177481104811": {
            "length": 48,
            "waveforms": {
                "single": "-7031895177481104811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4536451881243755330": {
            "length": 48,
            "waveforms": {
                "single": "4536451881243755330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7529260558262163167": {
            "length": 48,
            "waveforms": {
                "single": "-7529260558262163167",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8066429384070376767": {
            "length": 52,
            "waveforms": {
                "single": "8066429384070376767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "399074327548826398": {
            "length": 52,
            "waveforms": {
                "single": "399074327548826398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1953291341213467822": {
            "length": 52,
            "waveforms": {
                "single": "-1953291341213467822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5142886156837544962": {
            "length": 52,
            "waveforms": {
                "single": "5142886156837544962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2818328074750708509": {
            "length": 56,
            "waveforms": {
                "single": "2818328074750708509",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2727851125410528392": {
            "length": 56,
            "waveforms": {
                "single": "-2727851125410528392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-252897033991359315": {
            "length": 56,
            "waveforms": {
                "single": "-252897033991359315",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5872888411842075445": {
            "length": 56,
            "waveforms": {
                "single": "-5872888411842075445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-308597378208646281": {
            "length": 60,
            "waveforms": {
                "single": "-308597378208646281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7896931911018345498": {
            "length": 60,
            "waveforms": {
                "single": "7896931911018345498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6027494392601202802": {
            "length": 60,
            "waveforms": {
                "single": "-6027494392601202802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "353537241602430317": {
            "length": 60,
            "waveforms": {
                "single": "353537241602430317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "76342838186428103": {
            "length": 64,
            "waveforms": {
                "single": "76342838186428103",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3118842657661274909": {
            "length": 64,
            "waveforms": {
                "single": "-3118842657661274909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2897348598462559661": {
            "length": 64,
            "waveforms": {
                "single": "-2897348598462559661",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1624969171627443655": {
            "length": 64,
            "waveforms": {
                "single": "1624969171627443655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-699588910459392798": {
            "length": 68,
            "waveforms": {
                "single": "-699588910459392798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5154946674454065092": {
            "length": 68,
            "waveforms": {
                "single": "5154946674454065092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2512408382067485277": {
            "length": 68,
            "waveforms": {
                "single": "-2512408382067485277",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2009909388022518039": {
            "length": 68,
            "waveforms": {
                "single": "2009909388022518039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7574200421655947203": {
            "length": 72,
            "waveforms": {
                "single": "7574200421655947203",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-93154634865603166": {
            "length": 72,
            "waveforms": {
                "single": "-93154634865603166",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1240976452042471939": {
            "length": 72,
            "waveforms": {
                "single": "-1240976452042471939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5140055182161161180": {
            "length": 72,
            "waveforms": {
                "single": "5140055182161161180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8784371121458387120": {
            "length": 76,
            "waveforms": {
                "single": "-8784371121458387120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1178277295159410172": {
            "length": 76,
            "waveforms": {
                "single": "1178277295159410172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-856036235647397555": {
            "length": 76,
            "waveforms": {
                "single": "-856036235647397555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6411487112186174518": {
            "length": 76,
            "waveforms": {
                "single": "6411487112186174518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8228085055280753447": {
            "length": 80,
            "waveforms": {
                "single": "-8228085055280753447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1563217511554484556": {
            "length": 80,
            "waveforms": {
                "single": "1563217511554484556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8830740859388056629": {
            "length": 80,
            "waveforms": {
                "single": "8830740859388056629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9080907403910981665": {
            "length": 40,
            "waveforms": {
                "I": "9080907403910981665_i",
                "Q": "9080907403910981665_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8319816774687419796_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "8319816774687419796_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-2188275792564588673": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "6505297470054341181_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "6505297470054341181_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7734454992725825574": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-4388873487545789938": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-2962835576761649243": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5315201245523943463": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "5464187771664057784": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-3117441557520776600": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "7661947459667224647": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "2115768259505987746": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "2337262318704702994": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "4313527947509154609": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "4535022006707869857": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-3132333049813680512": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7120559918084145506": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5761893121991976946": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "4919962223102944241": {
            "sample": 0.25,
            "type": "constant",
        },
        "5141456282301659489": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1946270786453956477": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1669076383037954263": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "1890570442236669511": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1475960903393592790": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1254466844194877542": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3757248913633171556": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "2275510658631743895": {
            "sample": 0.25,
            "type": "constant",
        },
        "-919674837215959117": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6176502660835053667": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3824136992072759447": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-8740263910047876512": {
            "sample": 0.25,
            "type": "constant",
        },
        "1623539297091558182": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3996452080759157948": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7191637576606860960": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-8673375831608288621": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4993877888603694097": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4772383829404978849": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6806697360211786576": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-1242406326578357412": {
            "sample": 0.25,
            "type": "constant",
        },
        "5853771171472655372": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4387443613009904465": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4165949553811189217": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6188563178451573797": {
            "sample": 0.25,
            "type": "constant",
        },
        "6410057237650289045": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7514369065969259255": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3265019951218741992": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "8829310984852171156": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7253389236679820059": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7031895177481104811": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4536451881243755330": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-7529260558262163167": {
            "sample": 0.25,
            "type": "constant",
        },
        "8066429384070376767": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "399074327548826398": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1953291341213467822": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "5142886156837544962": {
            "sample": 0.25,
            "type": "constant",
        },
        "2818328074750708509": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2727851125410528392": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-252897033991359315": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-5872888411842075445": {
            "sample": 0.25,
            "type": "constant",
        },
        "-308597378208646281": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7896931911018345498": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6027494392601202802": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "353537241602430317": {
            "sample": 0.25,
            "type": "constant",
        },
        "76342838186428103": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3118842657661274909": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2897348598462559661": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "1624969171627443655": {
            "sample": 0.25,
            "type": "constant",
        },
        "-699588910459392798": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5154946674454065092": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2512408382067485277": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "2009909388022518039": {
            "sample": 0.25,
            "type": "constant",
        },
        "7574200421655947203": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-93154634865603166": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1240976452042471939": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "5140055182161161180": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8784371121458387120": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1178277295159410172": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-856036235647397555": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6411487112186174518": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8228085055280753447": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1563217511554484556": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8830740859388056629": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "9080907403910981665_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "9080907403910981665_q": {
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
                "76342838186428103": "76342838186428103",
                "-3118842657661274909": "-3118842657661274909",
                "-2897348598462559661": "-2897348598462559661",
                "1624969171627443655": "1624969171627443655",
                "-699588910459392798": "-699588910459392798",
                "5154946674454065092": "5154946674454065092",
                "-2512408382067485277": "-2512408382067485277",
                "2009909388022518039": "2009909388022518039",
                "7574200421655947203": "7574200421655947203",
                "-93154634865603166": "-93154634865603166",
                "-1240976452042471939": "-1240976452042471939",
                "5140055182161161180": "5140055182161161180",
                "-8784371121458387120": "-8784371121458387120",
                "1178277295159410172": "1178277295159410172",
                "-856036235647397555": "-856036235647397555",
                "6411487112186174518": "6411487112186174518",
                "-8228085055280753447": "-8228085055280753447",
                "1563217511554484556": "1563217511554484556",
                "8830740859388056629": "8830740859388056629",
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
                "-6914001376397344256": "-6914001376397344256_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_faa",
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
                "8319816774687419796": "8319816774687419796",
                "9080907403910981665": "9080907403910981665",
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
                "mixer": "B4/drive_mixer_8ab",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "8319816774687419796": {
            "length": 40,
            "waveforms": {
                "I": "8319816774687419796_i",
                "Q": "8319816774687419796_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2188275792564588673": {
            "length": 16,
            "waveforms": {
                "single": "-2188275792564588673",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6914001376397344256_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6505297470054341181_i",
                "Q": "6505297470054341181_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-7734454992725825574": {
            "length": 16,
            "waveforms": {
                "single": "-7734454992725825574",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4388873487545789938": {
            "length": 16,
            "waveforms": {
                "single": "-4388873487545789938",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2962835576761649243": {
            "length": 16,
            "waveforms": {
                "single": "-2962835576761649243",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5315201245523943463": {
            "length": 16,
            "waveforms": {
                "single": "-5315201245523943463",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5464187771664057784": {
            "length": 16,
            "waveforms": {
                "single": "5464187771664057784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3117441557520776600": {
            "length": 16,
            "waveforms": {
                "single": "-3117441557520776600",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7661947459667224647": {
            "length": 16,
            "waveforms": {
                "single": "7661947459667224647",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2115768259505987746": {
            "length": 16,
            "waveforms": {
                "single": "2115768259505987746",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2337262318704702994": {
            "length": 16,
            "waveforms": {
                "single": "2337262318704702994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4313527947509154609": {
            "length": 16,
            "waveforms": {
                "single": "4313527947509154609",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4535022006707869857": {
            "length": 16,
            "waveforms": {
                "single": "4535022006707869857",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3132333049813680512": {
            "length": 16,
            "waveforms": {
                "single": "-3132333049813680512",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7120559918084145506": {
            "length": 16,
            "waveforms": {
                "single": "7120559918084145506",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5761893121991976946": {
            "length": 16,
            "waveforms": {
                "single": "-5761893121991976946",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4919962223102944241": {
            "length": 16,
            "waveforms": {
                "single": "4919962223102944241",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5141456282301659489": {
            "length": 20,
            "waveforms": {
                "single": "5141456282301659489",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1946270786453956477": {
            "length": 20,
            "waveforms": {
                "single": "1946270786453956477",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1669076383037954263": {
            "length": 20,
            "waveforms": {
                "single": "1669076383037954263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1890570442236669511": {
            "length": 20,
            "waveforms": {
                "single": "1890570442236669511",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1475960903393592790": {
            "length": 24,
            "waveforms": {
                "single": "-1475960903393592790",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1254466844194877542": {
            "length": 24,
            "waveforms": {
                "single": "-1254466844194877542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3757248913633171556": {
            "length": 24,
            "waveforms": {
                "single": "3757248913633171556",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2275510658631743895": {
            "length": 24,
            "waveforms": {
                "single": "2275510658631743895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-919674837215959117": {
            "length": 28,
            "waveforms": {
                "single": "-919674837215959117",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6176502660835053667": {
            "length": 28,
            "waveforms": {
                "single": "6176502660835053667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3824136992072759447": {
            "length": 28,
            "waveforms": {
                "single": "3824136992072759447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8740263910047876512": {
            "length": 28,
            "waveforms": {
                "single": "-8740263910047876512",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1623539297091558182": {
            "length": 32,
            "waveforms": {
                "single": "1623539297091558182",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3996452080759157948": {
            "length": 32,
            "waveforms": {
                "single": "-3996452080759157948",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7191637576606860960": {
            "length": 32,
            "waveforms": {
                "single": "-7191637576606860960",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8673375831608288621": {
            "length": 32,
            "waveforms": {
                "single": "-8673375831608288621",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4993877888603694097": {
            "length": 36,
            "waveforms": {
                "single": "-4993877888603694097",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4772383829404978849": {
            "length": 36,
            "waveforms": {
                "single": "-4772383829404978849",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6806697360211786576": {
            "length": 36,
            "waveforms": {
                "single": "-6806697360211786576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1242406326578357412": {
            "length": 36,
            "waveforms": {
                "single": "-1242406326578357412",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5853771171472655372": {
            "length": 40,
            "waveforms": {
                "single": "5853771171472655372",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4387443613009904465": {
            "length": 40,
            "waveforms": {
                "single": "-4387443613009904465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4165949553811189217": {
            "length": 40,
            "waveforms": {
                "single": "-4165949553811189217",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6188563178451573797": {
            "length": 40,
            "waveforms": {
                "single": "6188563178451573797",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6410057237650289045": {
            "length": 44,
            "waveforms": {
                "single": "6410057237650289045",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7514369065969259255": {
            "length": 44,
            "waveforms": {
                "single": "-7514369065969259255",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3265019951218741992": {
            "length": 44,
            "waveforms": {
                "single": "3265019951218741992",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8829310984852171156": {
            "length": 44,
            "waveforms": {
                "single": "8829310984852171156",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7253389236679820059": {
            "length": 48,
            "waveforms": {
                "single": "-7253389236679820059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7031895177481104811": {
            "length": 48,
            "waveforms": {
                "single": "-7031895177481104811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4536451881243755330": {
            "length": 48,
            "waveforms": {
                "single": "4536451881243755330",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7529260558262163167": {
            "length": 48,
            "waveforms": {
                "single": "-7529260558262163167",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8066429384070376767": {
            "length": 52,
            "waveforms": {
                "single": "8066429384070376767",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "399074327548826398": {
            "length": 52,
            "waveforms": {
                "single": "399074327548826398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1953291341213467822": {
            "length": 52,
            "waveforms": {
                "single": "-1953291341213467822",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5142886156837544962": {
            "length": 52,
            "waveforms": {
                "single": "5142886156837544962",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2818328074750708509": {
            "length": 56,
            "waveforms": {
                "single": "2818328074750708509",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2727851125410528392": {
            "length": 56,
            "waveforms": {
                "single": "-2727851125410528392",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-252897033991359315": {
            "length": 56,
            "waveforms": {
                "single": "-252897033991359315",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5872888411842075445": {
            "length": 56,
            "waveforms": {
                "single": "-5872888411842075445",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-308597378208646281": {
            "length": 60,
            "waveforms": {
                "single": "-308597378208646281",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7896931911018345498": {
            "length": 60,
            "waveforms": {
                "single": "7896931911018345498",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6027494392601202802": {
            "length": 60,
            "waveforms": {
                "single": "-6027494392601202802",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "353537241602430317": {
            "length": 60,
            "waveforms": {
                "single": "353537241602430317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "76342838186428103": {
            "length": 64,
            "waveforms": {
                "single": "76342838186428103",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3118842657661274909": {
            "length": 64,
            "waveforms": {
                "single": "-3118842657661274909",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2897348598462559661": {
            "length": 64,
            "waveforms": {
                "single": "-2897348598462559661",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1624969171627443655": {
            "length": 64,
            "waveforms": {
                "single": "1624969171627443655",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-699588910459392798": {
            "length": 68,
            "waveforms": {
                "single": "-699588910459392798",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5154946674454065092": {
            "length": 68,
            "waveforms": {
                "single": "5154946674454065092",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2512408382067485277": {
            "length": 68,
            "waveforms": {
                "single": "-2512408382067485277",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2009909388022518039": {
            "length": 68,
            "waveforms": {
                "single": "2009909388022518039",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7574200421655947203": {
            "length": 72,
            "waveforms": {
                "single": "7574200421655947203",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-93154634865603166": {
            "length": 72,
            "waveforms": {
                "single": "-93154634865603166",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1240976452042471939": {
            "length": 72,
            "waveforms": {
                "single": "-1240976452042471939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5140055182161161180": {
            "length": 72,
            "waveforms": {
                "single": "5140055182161161180",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8784371121458387120": {
            "length": 76,
            "waveforms": {
                "single": "-8784371121458387120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1178277295159410172": {
            "length": 76,
            "waveforms": {
                "single": "1178277295159410172",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-856036235647397555": {
            "length": 76,
            "waveforms": {
                "single": "-856036235647397555",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6411487112186174518": {
            "length": 76,
            "waveforms": {
                "single": "6411487112186174518",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8228085055280753447": {
            "length": 80,
            "waveforms": {
                "single": "-8228085055280753447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1563217511554484556": {
            "length": 80,
            "waveforms": {
                "single": "1563217511554484556",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8830740859388056629": {
            "length": 80,
            "waveforms": {
                "single": "8830740859388056629",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9080907403910981665": {
            "length": 40,
            "waveforms": {
                "I": "9080907403910981665_i",
                "Q": "9080907403910981665_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "8319816774687419796_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8319816774687419796_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2188275792564588673": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6505297470054341181_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "6505297470054341181_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7734454992725825574": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4388873487545789938": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2962835576761649243": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5315201245523943463": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5464187771664057784": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3117441557520776600": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7661947459667224647": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2115768259505987746": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2337262318704702994": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4313527947509154609": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4535022006707869857": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3132333049813680512": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7120559918084145506": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5761893121991976946": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4919962223102944241": {
            "type": "constant",
            "sample": 0.25,
        },
        "5141456282301659489": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1946270786453956477": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1669076383037954263": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1890570442236669511": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1475960903393592790": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1254466844194877542": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3757248913633171556": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2275510658631743895": {
            "type": "constant",
            "sample": 0.25,
        },
        "-919674837215959117": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6176502660835053667": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3824136992072759447": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8740263910047876512": {
            "type": "constant",
            "sample": 0.25,
        },
        "1623539297091558182": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3996452080759157948": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7191637576606860960": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8673375831608288621": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4993877888603694097": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4772383829404978849": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6806697360211786576": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1242406326578357412": {
            "type": "constant",
            "sample": 0.25,
        },
        "5853771171472655372": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4387443613009904465": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4165949553811189217": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6188563178451573797": {
            "type": "constant",
            "sample": 0.25,
        },
        "6410057237650289045": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7514369065969259255": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3265019951218741992": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8829310984852171156": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7253389236679820059": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7031895177481104811": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4536451881243755330": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7529260558262163167": {
            "type": "constant",
            "sample": 0.25,
        },
        "8066429384070376767": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "399074327548826398": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1953291341213467822": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5142886156837544962": {
            "type": "constant",
            "sample": 0.25,
        },
        "2818328074750708509": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2727851125410528392": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-252897033991359315": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5872888411842075445": {
            "type": "constant",
            "sample": 0.25,
        },
        "-308597378208646281": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7896931911018345498": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6027494392601202802": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "353537241602430317": {
            "type": "constant",
            "sample": 0.25,
        },
        "76342838186428103": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3118842657661274909": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2897348598462559661": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1624969171627443655": {
            "type": "constant",
            "sample": 0.25,
        },
        "-699588910459392798": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5154946674454065092": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2512408382067485277": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2009909388022518039": {
            "type": "constant",
            "sample": 0.25,
        },
        "7574200421655947203": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-93154634865603166": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1240976452042471939": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5140055182161161180": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8784371121458387120": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1178277295159410172": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-856036235647397555": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6411487112186174518": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8228085055280753447": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1563217511554484556": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8830740859388056629": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9080907403910981665_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9080907403910981665_q": {
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
        "B4/acquisition_mixer_faa": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_8ab": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

