
# Single QUA script generated at 2025-02-05 16:06:31.583200
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
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
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B1/acquisition")
    wait((4+(0*(Cast.to_int(v4)+Cast.to_int(v5)))), "B2/acquisition")
    wait((4+(0*(Cast.to_int(v6)+Cast.to_int(v7)))), "B3/acquisition")
    wait((4+(0*(Cast.to_int(v8)+Cast.to_int(v9)))), "B4/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("-3587104139085357431", "B1/drive")
        play("6526116396539916645", "B2/drive")
        play("-1223803104563100095", "B3/drive")
        play("-5434532197284690668", "B4/drive")
        wait(11, "B4/acquisition")
        wait(11, "B3/acquisition")
        wait(11, "B1/acquisition")
        wait(11, "B2/acquisition")
        measure("-4513132739480156056", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        measure("-18247517274889005", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v4), dual_demod.full("minus_sin", "out1", "cos", "out2", v5))
        r3 = declare_stream()
        save(v4, r3)
        r4 = declare_stream()
        save(v5, r4)
        measure("-8330697210254322400", "B3/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v6), dual_demod.full("minus_sin", "out1", "cos", "out2", v7))
        r5 = declare_stream()
        save(v6, r5)
        r6 = declare_stream()
        save(v7, r6)
        measure("-7253294833940737992", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v8), dual_demod.full("minus_sin", "out1", "cos", "out2", v9))
        r7 = declare_stream()
        save(v8, r7)
        r8 = declare_stream()
        save(v9, r8)
        wait(25000, )
    with stream_processing():
        r1.buffer(5000).save("-4513132739480156056_B1|acquisition_I")
        r2.buffer(5000).save("-4513132739480156056_B1|acquisition_Q")
        r3.buffer(5000).save("-18247517274889005_B2|acquisition_I")
        r4.buffer(5000).save("-18247517274889005_B2|acquisition_Q")
        r5.buffer(5000).save("-8330697210254322400_B3|acquisition_I")
        r6.buffer(5000).save("-8330697210254322400_B3|acquisition_Q")
        r7.buffer(5000).save("-7253294833940737992_B4|acquisition_I")
        r8.buffer(5000).save("-7253294833940737992_B4|acquisition_Q")


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
                "-4513132739480156056": "-4513132739480156056_B1/acquisition",
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
                "-8330697210254322400": "-8330697210254322400_B3/acquisition",
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
                "-18247517274889005": "-18247517274889005_B2/acquisition",
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
                "-7253294833940737992": "-7253294833940737992_B4/acquisition",
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
                "6526116396539916645": "6526116396539916645",
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
                "-3587104139085357431": "-3587104139085357431",
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
                "-5434532197284690668": "-5434532197284690668",
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
                "-1223803104563100095": "-1223803104563100095",
            },
        },
    },
    "pulses": {
        "-4513132739480156056_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8678929857681733262_i",
                "Q": "8678929857681733262_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-18247517274889005_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1579839135145208837_i",
                "Q": "-1579839135145208837_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-8330697210254322400_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6846652533772261916_i",
                "Q": "-6846652533772261916_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-7253294833940737992_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5430097732009904400_i",
                "Q": "5430097732009904400_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-3587104139085357431": {
            "length": 40,
            "waveforms": {
                "I": "-3587104139085357431_i",
                "Q": "-3587104139085357431_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6526116396539916645": {
            "length": 40,
            "waveforms": {
                "I": "6526116396539916645_i",
                "Q": "6526116396539916645_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1223803104563100095": {
            "length": 40,
            "waveforms": {
                "I": "-1223803104563100095_i",
                "Q": "-1223803104563100095_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5434532197284690668": {
            "length": 40,
            "waveforms": {
                "I": "-5434532197284690668_i",
                "Q": "-5434532197284690668_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8678929857681733262_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "8678929857681733262_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1579839135145208837_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1579839135145208837_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6846652533772261916_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-6846652533772261916_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5430097732009904400_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "5430097732009904400_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3587104139085357431_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "-3587104139085357431_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "6526116396539916645_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "6526116396539916645_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-1223803104563100095_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "-1223803104563100095_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "-5434532197284690668_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-5434532197284690668_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
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
                "-4513132739480156056": "-4513132739480156056_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_6c7",
                "lo_frequency": 7370000000.0,
            },
        },
        "B3/acquisition": {
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
            "intermediate_frequency": 110622376.0,
            "operations": {
                "-8330697210254322400": "-8330697210254322400_B3/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B3/acquisition_mixer_b9f",
                "lo_frequency": 7370000000.0,
            },
        },
        "B2/acquisition": {
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
            "intermediate_frequency": 10040944.0,
            "operations": {
                "-18247517274889005": "-18247517274889005_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_a1a",
                "lo_frequency": 7370000000.0,
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
                "-7253294833940737992": "-7253294833940737992_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_cf3",
                "lo_frequency": 7370000000.0,
            },
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 63761228.0,
            "operations": {
                "6526116396539916645": "6526116396539916645",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_4ff",
                "lo_frequency": 5900000000.0,
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
                "-3587104139085357431": "-3587104139085357431",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_70e",
                "lo_frequency": 4900000000.0,
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
                "-5434532197284690668": "-5434532197284690668",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_a75",
                "lo_frequency": 6700000000.0,
            },
        },
        "B3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -115376210.0,
            "operations": {
                "-1223803104563100095": "-1223803104563100095",
            },
            "mixInputs": {
                "I": ('con3', 1),
                "Q": ('con3', 2),
                "mixer": "B3/drive_mixer_708",
                "lo_frequency": 5800000000.0,
            },
        },
    },
    "pulses": {
        "-4513132739480156056_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8678929857681733262_i",
                "Q": "8678929857681733262_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "-18247517274889005_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1579839135145208837_i",
                "Q": "-1579839135145208837_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-8330697210254322400_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6846652533772261916_i",
                "Q": "-6846652533772261916_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
        },
        "-7253294833940737992_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5430097732009904400_i",
                "Q": "5430097732009904400_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-3587104139085357431": {
            "length": 40,
            "waveforms": {
                "I": "-3587104139085357431_i",
                "Q": "-3587104139085357431_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6526116396539916645": {
            "length": 40,
            "waveforms": {
                "I": "6526116396539916645_i",
                "Q": "6526116396539916645_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1223803104563100095": {
            "length": 40,
            "waveforms": {
                "I": "-1223803104563100095_i",
                "Q": "-1223803104563100095_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5434532197284690668": {
            "length": 40,
            "waveforms": {
                "I": "-5434532197284690668_i",
                "Q": "-5434532197284690668_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8678929857681733262_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "8678929857681733262_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1579839135145208837_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1579839135145208837_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6846652533772261916_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-6846652533772261916_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5430097732009904400_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "5430097732009904400_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3587104139085357431_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3587104139085357431_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6526116396539916645_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6526116396539916645_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1223803104563100095_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1223803104563100095_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5434532197284690668_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5434532197284690668_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
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
        "B1/acquisition_mixer_6c7": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/acquisition_mixer_b9f": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_a1a": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_cf3": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_4ff": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/drive_mixer_70e": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_a75": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/drive_mixer_708": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

