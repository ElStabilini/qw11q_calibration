
# Single QUA script generated at 2025-02-06 17:56:11.297129
# QUA library version: 1.1.6

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
        play("-2789151136112917978", "B1/drive")
        wait(11, "B1/flux")
        play("-1216547638615726142", "B1/flux")
        wait(46, "B1/drive")
        play("-2028060506889356109", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3262269342322283058", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        r1 = declare_stream()
        save(v4, r1)
        play("-2102571296432918254", "B2/drive")
        wait(11, "B2/flux")
        play("-1216547638615726142", "B2/flux")
        wait(46, "B2/drive")
        play("-1341480667209356385", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-5813413408751872832", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
        assign(v7, Cast.to_int((((v5*-0.19080553858813715)-(v6*-0.9816278553729467))>0.0026123324466526855)))
        r2 = declare_stream()
        save(v7, r2)
        play("3582889524429600990", "B3/drive")
        wait(11, "B3/flux")
        play("-1216547638615726142", "B3/flux")
        wait(46, "B3/drive")
        play("4343980153653162859", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-163478762525443495", "B3/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v8), dual_demod.full("minus_sin", "out1", "cos", "out2", v9))
        assign(v10, Cast.to_int((((v8*0.49095249936396523)-(v9*0.8711863425055949))>0.0026888725240183766)))
        r3 = declare_stream()
        save(v10, r3)
        play("-1532294537309455643", "B4/drive")
        wait(11, "B4/flux")
        play("-1216547638615726142", "B4/flux")
        wait(46, "B4/drive")
        play("-771203908085893774", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1131075789643953645", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v11), dual_demod.full("minus_sin", "out1", "cos", "out2", v12))
        assign(v13, Cast.to_int((((v11*0.9730343180892005)-(v12*-0.2306603906627328))>-0.0004384486988547942)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B1/flux")
        wait(25501, "B4/drive")
        wait(25001, "B3/acquisition")
        wait(25536, "B3/flux")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B2/flux")
        wait(25001, "B1/acquisition")
        play("-2789151136112917978", "B1/drive")
        wait(11, "B1/flux")
        play("-995053579417010894", "B1/flux")
        wait(46, "B1/drive")
        play("-2028060506889356109", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3262269342322283058", "B1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.9979082255587788)-(v3*-0.06464652629592395))>0.00099163965831088)))
        save(v4, r1)
        play("-2102571296432918254", "B2/drive")
        wait(11, "B2/flux")
        play("-995053579417010894", "B2/flux")
        wait(46, "B2/drive")
        play("-1341480667209356385", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-5813413408751872832", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
        assign(v7, Cast.to_int((((v5*-0.19080553858813715)-(v6*-0.9816278553729467))>0.0026123324466526855)))
        save(v7, r2)
        play("3582889524429600990", "B3/drive")
        wait(11, "B3/flux")
        play("-995053579417010894", "B3/flux")
        wait(46, "B3/drive")
        play("4343980153653162859", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-163478762525443495", "B3/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v8), dual_demod.full("minus_sin", "out1", "cos", "out2", v9))
        assign(v10, Cast.to_int((((v8*0.49095249936396523)-(v9*0.8711863425055949))>0.0026888725240183766)))
        save(v10, r3)
        play("-1532294537309455643", "B4/drive")
        wait(11, "B4/flux")
        play("-995053579417010894", "B4/flux")
        wait(46, "B4/drive")
        play("-771203908085893774", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1131075789643953645", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v11), dual_demod.full("minus_sin", "out1", "cos", "out2", v12))
        assign(v13, Cast.to_int((((v11*0.9730343180892005)-(v12*-0.2306603906627328))>-0.0004384486988547942)))
        save(v13, r4)
        wait(25536, "B1/flux")
        wait(25501, "B4/drive")
        wait(25001, "B3/acquisition")
        wait(25536, "B3/flux")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B2/flux")
        wait(25001, "B1/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-3262269342322283058_B1|acquisition_shots")
        r2.buffer(2).average().save("-5813413408751872832_B2|acquisition_shots")
        r3.buffer(2).average().save("-163478762525443495_B3|acquisition_shots")
        r4.buffer(2).average().save("-1131075789643953645_B4|acquisition_shots")


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
    },
    "elements": {
        "B1/flux": {
            "singleInput": {
                "port": ('con4', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
                "-1532294537309455643": "-1532294537309455643",
                "-771203908085893774": "-771203908085893774",
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
                "-163478762525443495": "-163478762525443495_B3/acquisition",
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
                "-1131075789643953645": "-1131075789643953645_B4/acquisition",
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
                "3582889524429600990": "3582889524429600990",
                "4343980153653162859": "4343980153653162859",
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
                "-2102571296432918254": "-2102571296432918254",
                "-1341480667209356385": "-1341480667209356385",
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
                "-5813413408751872832": "-5813413408751872832_B2/acquisition",
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
                "-2789151136112917978": "-2789151136112917978",
                "-2028060506889356109": "-2028060506889356109",
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
                "-3262269342322283058": "-3262269342322283058_B1/acquisition",
            },
        },
    },
    "pulses": {
        "-2789151136112917978": {
            "length": 40,
            "waveforms": {
                "I": "-2789151136112917978_i",
                "Q": "-2789151136112917978_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8092259297637620873": {
            "length": 16,
            "waveforms": {
                "single": "8092259297637620873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3262269342322283058_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4671864101614144045_i",
                "Q": "4671864101614144045_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-2102571296432918254": {
            "length": 40,
            "waveforms": {
                "I": "-2102571296432918254_i",
                "Q": "-2102571296432918254_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5813413408751872832_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5586904891212798054_i",
                "Q": "-5586904891212798054_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "3582889524429600990": {
            "length": 40,
            "waveforms": {
                "I": "3582889524429600990_i",
                "Q": "3582889524429600990_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-163478762525443495_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "590668381779373820_i",
                "Q": "590668381779373820_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-1532294537309455643": {
            "length": 40,
            "waveforms": {
                "I": "-1532294537309455643_i",
                "Q": "-1532294537309455643_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1131075789643953645_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5179210832864356145_i",
                "Q": "-5179210832864356145_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "424904241116070504": {
            "length": 16,
            "waveforms": {
                "single": "424904241116070504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "646398300314785752": {
            "length": 16,
            "waveforms": {
                "single": "646398300314785752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8390272632582348638": {
            "length": 16,
            "waveforms": {
                "single": "-8390272632582348638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8168778573383633390": {
            "length": 16,
            "waveforms": {
                "single": "-8168778573383633390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1696336171141083842": {
            "length": 16,
            "waveforms": {
                "single": "1696336171141083842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8077367805344716961": {
            "length": 16,
            "waveforms": {
                "single": "8077367805344716961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6929545988167848188": {
            "length": 16,
            "waveforms": {
                "single": "6929545988167848188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-737809068353702181": {
            "length": 16,
            "waveforms": {
                "single": "-737809068353702181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2219547323355129842": {
            "length": 16,
            "waveforms": {
                "single": "-2219547323355129842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9097944338339821317": {
            "length": 16,
            "waveforms": {
                "single": "-9097944338339821317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5290772432097197666": {
            "length": 16,
            "waveforms": {
                "single": "-5290772432097197666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7535980263761637820": {
            "length": 16,
            "waveforms": {
                "single": "7535980263761637820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6678690591137939206": {
            "length": 16,
            "waveforms": {
                "single": "-6678690591137939206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2871518684895315555": {
            "length": 16,
            "waveforms": {
                "single": "-2871518684895315555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8491510062746031685": {
            "length": 16,
            "waveforms": {
                "single": "-8491510062746031685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6760048515115816919": {
            "length": 20,
            "waveforms": {
                "single": "6760048515115816919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6293750374742864822": {
            "length": 20,
            "waveforms": {
                "single": "-6293750374742864822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1911778914484126957": {
            "length": 20,
            "waveforms": {
                "single": "1911778914484126957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1060540557716100476": {
            "length": 20,
            "waveforms": {
                "single": "-1060540557716100476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7144988731510891303": {
            "length": 24,
            "waveforms": {
                "single": "7144988731510891303",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5737464308565231149": {
            "length": 24,
            "waveforms": {
                "single": "-5737464308565231149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1215146538475227833": {
            "length": 24,
            "waveforms": {
                "single": "-1215146538475227833",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8882501594996778202": {
            "length": 24,
            "waveforms": {
                "single": "-8882501594996778202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4018063278551536513": {
            "length": 28,
            "waveforms": {
                "single": "4018063278551536513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6934682406534476980": {
            "length": 28,
            "waveforms": {
                "single": "6934682406534476980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6215822966554703376": {
            "length": 28,
            "waveforms": {
                "single": "6215822966554703376",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6437317025753418624": {
            "length": 28,
            "waveforms": {
                "single": "6437317025753418624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1230038030768131745": {
            "length": 32,
            "waveforms": {
                "single": "-1230038030768131745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9022854937129694273": {
            "length": 32,
            "waveforms": {
                "single": "9022854937129694273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3859598102946428179": {
            "length": 32,
            "waveforms": {
                "single": "-3859598102946428179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6822257242148493008": {
            "length": 32,
            "waveforms": {
                "single": "6822257242148493008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "41393899256881593": {
            "length": 36,
            "waveforms": {
                "single": "41393899256881593",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3848565805499505244": {
            "length": 36,
            "waveforms": {
                "single": "3848565805499505244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9205233084359176497": {
            "length": 36,
            "waveforms": {
                "single": "-9205233084359176497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3792865461282218278": {
            "length": 36,
            "waveforms": {
                "single": "3792865461282218278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "426334115651955977": {
            "length": 40,
            "waveforms": {
                "single": "426334115651955977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4233506021894579628": {
            "length": 40,
            "waveforms": {
                "single": "4233506021894579628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2624093803655122840": {
            "length": 40,
            "waveforms": {
                "single": "2624093803655122840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2845587862853838088": {
            "length": 40,
            "waveforms": {
                "single": "2845587862853838088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6652759769096461739": {
            "length": 44,
            "waveforms": {
                "single": "6652759769096461739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8078797679880602434": {
            "length": 44,
            "waveforms": {
                "single": "8078797679880602434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4023199696918165305": {
            "length": 44,
            "waveforms": {
                "single": "4023199696918165305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8170186705825782319": {
            "length": 44,
            "waveforms": {
                "single": "-8170186705825782319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7924191699121475077": {
            "length": 48,
            "waveforms": {
                "single": "7924191699121475077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304200321270758947": {
            "length": 48,
            "waveforms": {
                "single": "2304200321270758947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4418715143800445634": {
            "length": 48,
            "waveforms": {
                "single": "-4418715143800445634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6771080812562739854": {
            "length": 48,
            "waveforms": {
                "single": "-6771080812562739854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3091582869558145330": {
            "length": 52,
            "waveforms": {
                "single": "-3091582869558145330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2870088810359430082": {
            "length": 52,
            "waveforms": {
                "single": "-2870088810359430082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3147283213775432296": {
            "length": 52,
            "waveforms": {
                "single": "-3147283213775432296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "659888692467191355": {
            "length": 52,
            "waveforms": {
                "single": "659888692467191355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5182206462557194671": {
            "length": 56,
            "waveforms": {
                "single": "5182206462557194671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2485148593964355698": {
            "length": 56,
            "waveforms": {
                "single": "-2485148593964355698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4782374753869216375": {
            "length": 56,
            "waveforms": {
                "single": "4782374753869216375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-287388905961188835": {
            "length": 56,
            "waveforms": {
                "single": "-287388905961188835",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5736034434029345676": {
            "length": 60,
            "waveforms": {
                "single": "-5736034434029345676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1213716663939342360": {
            "length": 60,
            "waveforms": {
                "single": "-1213716663939342360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5167314970264290759": {
            "length": 60,
            "waveforms": {
                "single": "5167314970264290759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3316780686827463565": {
            "length": 60,
            "waveforms": {
                "single": "-3316780686827463565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7365074658267457622": {
            "length": 64,
            "waveforms": {
                "single": "7365074658267457622",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5129600158435556044": {
            "length": 64,
            "waveforms": {
                "single": "-5129600158435556044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6438746900289304097": {
            "length": 64,
            "waveforms": {
                "single": "6438746900289304097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2931840470432389181": {
            "length": 64,
            "waveforms": {
                "single": "-2931840470432389181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8636506588292470960": {
            "length": 68,
            "waveforms": {
                "single": "8636506588292470960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3429205851213447537": {
            "length": 68,
            "waveforms": {
                "single": "-3429205851213447537",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5781571519975741757": {
            "length": 68,
            "waveforms": {
                "single": "-5781571519975741757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6058765923391743971": {
            "length": 68,
            "waveforms": {
                "single": "-6058765923391743971",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4720623093796257276": {
            "length": 72,
            "waveforms": {
                "single": "4720623093796257276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9203803209823291024": {
            "length": 72,
            "waveforms": {
                "single": "-9203803209823291024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1649397985054189452": {
            "length": 72,
            "waveforms": {
                "single": "1649397985054189452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1372203581638187238": {
            "length": 72,
            "waveforms": {
                "single": "1372203581638187238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5992055023821270614": {
            "length": 76,
            "waveforms": {
                "single": "5992055023821270614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8647517143645657351": {
            "length": 76,
            "waveforms": {
                "single": "-8647517143645657351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4125199373555654035": {
            "length": 76,
            "waveforms": {
                "single": "-4125199373555654035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6654189643632347212": {
            "length": 76,
            "waveforms": {
                "single": "6654189643632347212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6376995240216344998": {
            "length": 80,
            "waveforms": {
                "single": "6376995240216344998",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216547638615726142": {
            "length": 80,
            "waveforms": {
                "single": "-1216547638615726142",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-995053579417010894": {
            "length": 80,
            "waveforms": {
                "single": "-995053579417010894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2028060506889356109": {
            "length": 40,
            "waveforms": {
                "I": "-2028060506889356109_i",
                "Q": "-2028060506889356109_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1341480667209356385": {
            "length": 40,
            "waveforms": {
                "I": "-1341480667209356385_i",
                "Q": "-1341480667209356385_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4343980153653162859": {
            "length": 40,
            "waveforms": {
                "I": "4343980153653162859_i",
                "Q": "4343980153653162859_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-771203908085893774": {
            "length": 40,
            "waveforms": {
                "I": "-771203908085893774_i",
                "Q": "-771203908085893774_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2789151136112917978_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-2789151136112917978_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "8092259297637620873": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "4671864101614144045_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "4671864101614144045_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2102571296432918254_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-2102571296432918254_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-5586904891212798054_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-5586904891212798054_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3582889524429600990_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "3582889524429600990_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "590668381779373820_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "590668381779373820_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1532294537309455643_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-1532294537309455643_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-5179210832864356145_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5179210832864356145_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "424904241116070504": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "646398300314785752": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-8390272632582348638": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-8168778573383633390": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "1696336171141083842": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8077367805344716961": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "6929545988167848188": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-737809068353702181": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-2219547323355129842": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-9097944338339821317": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-5290772432097197666": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "7535980263761637820": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6678690591137939206": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2871518684895315555": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8491510062746031685": {
            "sample": 0.25,
            "type": "constant",
        },
        "6760048515115816919": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6293750374742864822": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1911778914484126957": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-1060540557716100476": {
            "sample": 0.25,
            "type": "constant",
        },
        "7144988731510891303": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5737464308565231149": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1215146538475227833": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8882501594996778202": {
            "sample": 0.25,
            "type": "constant",
        },
        "4018063278551536513": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6934682406534476980": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6215822966554703376": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "6437317025753418624": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1230038030768131745": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9022854937129694273": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3859598102946428179": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "6822257242148493008": {
            "sample": 0.25,
            "type": "constant",
        },
        "41393899256881593": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3848565805499505244": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9205233084359176497": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "3792865461282218278": {
            "sample": 0.25,
            "type": "constant",
        },
        "426334115651955977": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4233506021894579628": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2624093803655122840": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "2845587862853838088": {
            "sample": 0.25,
            "type": "constant",
        },
        "6652759769096461739": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8078797679880602434": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4023199696918165305": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8170186705825782319": {
            "sample": 0.25,
            "type": "constant",
        },
        "7924191699121475077": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2304200321270758947": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4418715143800445634": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-6771080812562739854": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3091582869558145330": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2870088810359430082": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3147283213775432296": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "659888692467191355": {
            "sample": 0.25,
            "type": "constant",
        },
        "5182206462557194671": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2485148593964355698": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4782374753869216375": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-287388905961188835": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5736034434029345676": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1213716663939342360": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5167314970264290759": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-3316780686827463565": {
            "sample": 0.25,
            "type": "constant",
        },
        "7365074658267457622": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5129600158435556044": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6438746900289304097": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-2931840470432389181": {
            "sample": 0.25,
            "type": "constant",
        },
        "8636506588292470960": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3429205851213447537": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5781571519975741757": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-6058765923391743971": {
            "sample": 0.25,
            "type": "constant",
        },
        "4720623093796257276": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9203803209823291024": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1649397985054189452": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "1372203581638187238": {
            "sample": 0.25,
            "type": "constant",
        },
        "5992055023821270614": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8647517143645657351": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4125199373555654035": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6654189643632347212": {
            "sample": 0.25,
            "type": "constant",
        },
        "6376995240216344998": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1216547638615726142": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-995053579417010894": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-2028060506889356109_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-2028060506889356109_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-1341480667209356385_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-1341480667209356385_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "4343980153653162859_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "4343980153653162859_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-771203908085893774_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-771203908085893774_q": {
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
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "operations": {
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
            "operations": {
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
            },
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
            "operations": {
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
            },
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
                "-1216547638615726142": "-1216547638615726142",
                "-995053579417010894": "-995053579417010894",
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
                "-1532294537309455643": "-1532294537309455643",
                "-771203908085893774": "-771203908085893774",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_a43",
                "lo_frequency": 6700000000.0,
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
                "-163478762525443495": "-163478762525443495_B3/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B3/acquisition_mixer_e0d",
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
                "-1131075789643953645": "-1131075789643953645_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_ddf",
                "lo_frequency": 7370000000.0,
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
                "3582889524429600990": "3582889524429600990",
                "4343980153653162859": "4343980153653162859",
            },
            "mixInputs": {
                "I": ('con3', 1),
                "Q": ('con3', 2),
                "mixer": "B3/drive_mixer_d45",
                "lo_frequency": 5800000000.0,
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
                "-2102571296432918254": "-2102571296432918254",
                "-1341480667209356385": "-1341480667209356385",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_d55",
                "lo_frequency": 5900000000.0,
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
                "-5813413408751872832": "-5813413408751872832_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_ed3",
                "lo_frequency": 7370000000.0,
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
                "-2789151136112917978": "-2789151136112917978",
                "-2028060506889356109": "-2028060506889356109",
            },
            "mixInputs": {
                "I": ('con2', 3),
                "Q": ('con2', 4),
                "mixer": "B1/drive_mixer_e2b",
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
                "-3262269342322283058": "-3262269342322283058_B1/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B1/acquisition_mixer_ba2",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-2789151136112917978": {
            "length": 40,
            "waveforms": {
                "I": "-2789151136112917978_i",
                "Q": "-2789151136112917978_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8092259297637620873": {
            "length": 16,
            "waveforms": {
                "single": "8092259297637620873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3262269342322283058_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4671864101614144045_i",
                "Q": "4671864101614144045_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
        },
        "-2102571296432918254": {
            "length": 40,
            "waveforms": {
                "I": "-2102571296432918254_i",
                "Q": "-2102571296432918254_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5813413408751872832_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5586904891212798054_i",
                "Q": "-5586904891212798054_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "3582889524429600990": {
            "length": 40,
            "waveforms": {
                "I": "3582889524429600990_i",
                "Q": "3582889524429600990_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-163478762525443495_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "590668381779373820_i",
                "Q": "590668381779373820_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
        },
        "-1532294537309455643": {
            "length": 40,
            "waveforms": {
                "I": "-1532294537309455643_i",
                "Q": "-1532294537309455643_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1131075789643953645_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5179210832864356145_i",
                "Q": "-5179210832864356145_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "424904241116070504": {
            "length": 16,
            "waveforms": {
                "single": "424904241116070504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "646398300314785752": {
            "length": 16,
            "waveforms": {
                "single": "646398300314785752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8390272632582348638": {
            "length": 16,
            "waveforms": {
                "single": "-8390272632582348638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8168778573383633390": {
            "length": 16,
            "waveforms": {
                "single": "-8168778573383633390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1696336171141083842": {
            "length": 16,
            "waveforms": {
                "single": "1696336171141083842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8077367805344716961": {
            "length": 16,
            "waveforms": {
                "single": "8077367805344716961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6929545988167848188": {
            "length": 16,
            "waveforms": {
                "single": "6929545988167848188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-737809068353702181": {
            "length": 16,
            "waveforms": {
                "single": "-737809068353702181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2219547323355129842": {
            "length": 16,
            "waveforms": {
                "single": "-2219547323355129842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9097944338339821317": {
            "length": 16,
            "waveforms": {
                "single": "-9097944338339821317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5290772432097197666": {
            "length": 16,
            "waveforms": {
                "single": "-5290772432097197666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7535980263761637820": {
            "length": 16,
            "waveforms": {
                "single": "7535980263761637820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6678690591137939206": {
            "length": 16,
            "waveforms": {
                "single": "-6678690591137939206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2871518684895315555": {
            "length": 16,
            "waveforms": {
                "single": "-2871518684895315555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8491510062746031685": {
            "length": 16,
            "waveforms": {
                "single": "-8491510062746031685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6760048515115816919": {
            "length": 20,
            "waveforms": {
                "single": "6760048515115816919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6293750374742864822": {
            "length": 20,
            "waveforms": {
                "single": "-6293750374742864822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1911778914484126957": {
            "length": 20,
            "waveforms": {
                "single": "1911778914484126957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1060540557716100476": {
            "length": 20,
            "waveforms": {
                "single": "-1060540557716100476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7144988731510891303": {
            "length": 24,
            "waveforms": {
                "single": "7144988731510891303",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5737464308565231149": {
            "length": 24,
            "waveforms": {
                "single": "-5737464308565231149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1215146538475227833": {
            "length": 24,
            "waveforms": {
                "single": "-1215146538475227833",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8882501594996778202": {
            "length": 24,
            "waveforms": {
                "single": "-8882501594996778202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4018063278551536513": {
            "length": 28,
            "waveforms": {
                "single": "4018063278551536513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6934682406534476980": {
            "length": 28,
            "waveforms": {
                "single": "6934682406534476980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6215822966554703376": {
            "length": 28,
            "waveforms": {
                "single": "6215822966554703376",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6437317025753418624": {
            "length": 28,
            "waveforms": {
                "single": "6437317025753418624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1230038030768131745": {
            "length": 32,
            "waveforms": {
                "single": "-1230038030768131745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9022854937129694273": {
            "length": 32,
            "waveforms": {
                "single": "9022854937129694273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3859598102946428179": {
            "length": 32,
            "waveforms": {
                "single": "-3859598102946428179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6822257242148493008": {
            "length": 32,
            "waveforms": {
                "single": "6822257242148493008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "41393899256881593": {
            "length": 36,
            "waveforms": {
                "single": "41393899256881593",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3848565805499505244": {
            "length": 36,
            "waveforms": {
                "single": "3848565805499505244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9205233084359176497": {
            "length": 36,
            "waveforms": {
                "single": "-9205233084359176497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3792865461282218278": {
            "length": 36,
            "waveforms": {
                "single": "3792865461282218278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "426334115651955977": {
            "length": 40,
            "waveforms": {
                "single": "426334115651955977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4233506021894579628": {
            "length": 40,
            "waveforms": {
                "single": "4233506021894579628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2624093803655122840": {
            "length": 40,
            "waveforms": {
                "single": "2624093803655122840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2845587862853838088": {
            "length": 40,
            "waveforms": {
                "single": "2845587862853838088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6652759769096461739": {
            "length": 44,
            "waveforms": {
                "single": "6652759769096461739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8078797679880602434": {
            "length": 44,
            "waveforms": {
                "single": "8078797679880602434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4023199696918165305": {
            "length": 44,
            "waveforms": {
                "single": "4023199696918165305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8170186705825782319": {
            "length": 44,
            "waveforms": {
                "single": "-8170186705825782319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7924191699121475077": {
            "length": 48,
            "waveforms": {
                "single": "7924191699121475077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304200321270758947": {
            "length": 48,
            "waveforms": {
                "single": "2304200321270758947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4418715143800445634": {
            "length": 48,
            "waveforms": {
                "single": "-4418715143800445634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6771080812562739854": {
            "length": 48,
            "waveforms": {
                "single": "-6771080812562739854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3091582869558145330": {
            "length": 52,
            "waveforms": {
                "single": "-3091582869558145330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2870088810359430082": {
            "length": 52,
            "waveforms": {
                "single": "-2870088810359430082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3147283213775432296": {
            "length": 52,
            "waveforms": {
                "single": "-3147283213775432296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "659888692467191355": {
            "length": 52,
            "waveforms": {
                "single": "659888692467191355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5182206462557194671": {
            "length": 56,
            "waveforms": {
                "single": "5182206462557194671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2485148593964355698": {
            "length": 56,
            "waveforms": {
                "single": "-2485148593964355698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4782374753869216375": {
            "length": 56,
            "waveforms": {
                "single": "4782374753869216375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-287388905961188835": {
            "length": 56,
            "waveforms": {
                "single": "-287388905961188835",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5736034434029345676": {
            "length": 60,
            "waveforms": {
                "single": "-5736034434029345676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1213716663939342360": {
            "length": 60,
            "waveforms": {
                "single": "-1213716663939342360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5167314970264290759": {
            "length": 60,
            "waveforms": {
                "single": "5167314970264290759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3316780686827463565": {
            "length": 60,
            "waveforms": {
                "single": "-3316780686827463565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7365074658267457622": {
            "length": 64,
            "waveforms": {
                "single": "7365074658267457622",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5129600158435556044": {
            "length": 64,
            "waveforms": {
                "single": "-5129600158435556044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6438746900289304097": {
            "length": 64,
            "waveforms": {
                "single": "6438746900289304097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2931840470432389181": {
            "length": 64,
            "waveforms": {
                "single": "-2931840470432389181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8636506588292470960": {
            "length": 68,
            "waveforms": {
                "single": "8636506588292470960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3429205851213447537": {
            "length": 68,
            "waveforms": {
                "single": "-3429205851213447537",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5781571519975741757": {
            "length": 68,
            "waveforms": {
                "single": "-5781571519975741757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6058765923391743971": {
            "length": 68,
            "waveforms": {
                "single": "-6058765923391743971",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4720623093796257276": {
            "length": 72,
            "waveforms": {
                "single": "4720623093796257276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9203803209823291024": {
            "length": 72,
            "waveforms": {
                "single": "-9203803209823291024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1649397985054189452": {
            "length": 72,
            "waveforms": {
                "single": "1649397985054189452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1372203581638187238": {
            "length": 72,
            "waveforms": {
                "single": "1372203581638187238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5992055023821270614": {
            "length": 76,
            "waveforms": {
                "single": "5992055023821270614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8647517143645657351": {
            "length": 76,
            "waveforms": {
                "single": "-8647517143645657351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4125199373555654035": {
            "length": 76,
            "waveforms": {
                "single": "-4125199373555654035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6654189643632347212": {
            "length": 76,
            "waveforms": {
                "single": "6654189643632347212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6376995240216344998": {
            "length": 80,
            "waveforms": {
                "single": "6376995240216344998",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216547638615726142": {
            "length": 80,
            "waveforms": {
                "single": "-1216547638615726142",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-995053579417010894": {
            "length": 80,
            "waveforms": {
                "single": "-995053579417010894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2028060506889356109": {
            "length": 40,
            "waveforms": {
                "I": "-2028060506889356109_i",
                "Q": "-2028060506889356109_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1341480667209356385": {
            "length": 40,
            "waveforms": {
                "I": "-1341480667209356385_i",
                "Q": "-1341480667209356385_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4343980153653162859": {
            "length": 40,
            "waveforms": {
                "I": "4343980153653162859_i",
                "Q": "4343980153653162859_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-771203908085893774": {
            "length": 40,
            "waveforms": {
                "I": "-771203908085893774_i",
                "Q": "-771203908085893774_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2789151136112917978_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2789151136112917978_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8092259297637620873": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4671864101614144045_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "4671864101614144045_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2102571296432918254_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2102571296432918254_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5586904891212798054_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-5586904891212798054_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3582889524429600990_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3582889524429600990_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "590668381779373820_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "590668381779373820_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1532294537309455643_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1532294537309455643_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5179210832864356145_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5179210832864356145_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "424904241116070504": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "646398300314785752": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8390272632582348638": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8168778573383633390": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1696336171141083842": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8077367805344716961": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6929545988167848188": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-737809068353702181": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2219547323355129842": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9097944338339821317": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5290772432097197666": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7535980263761637820": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6678690591137939206": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2871518684895315555": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8491510062746031685": {
            "sample": 0.25,
            "type": "constant",
        },
        "6760048515115816919": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6293750374742864822": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1911778914484126957": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1060540557716100476": {
            "sample": 0.25,
            "type": "constant",
        },
        "7144988731510891303": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5737464308565231149": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1215146538475227833": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8882501594996778202": {
            "sample": 0.25,
            "type": "constant",
        },
        "4018063278551536513": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6934682406534476980": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6215822966554703376": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6437317025753418624": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1230038030768131745": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9022854937129694273": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3859598102946428179": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6822257242148493008": {
            "sample": 0.25,
            "type": "constant",
        },
        "41393899256881593": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3848565805499505244": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9205233084359176497": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3792865461282218278": {
            "sample": 0.25,
            "type": "constant",
        },
        "426334115651955977": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4233506021894579628": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2624093803655122840": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2845587862853838088": {
            "sample": 0.25,
            "type": "constant",
        },
        "6652759769096461739": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8078797679880602434": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4023199696918165305": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8170186705825782319": {
            "sample": 0.25,
            "type": "constant",
        },
        "7924191699121475077": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2304200321270758947": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4418715143800445634": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6771080812562739854": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3091582869558145330": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2870088810359430082": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3147283213775432296": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "659888692467191355": {
            "sample": 0.25,
            "type": "constant",
        },
        "5182206462557194671": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2485148593964355698": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4782374753869216375": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-287388905961188835": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5736034434029345676": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1213716663939342360": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5167314970264290759": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3316780686827463565": {
            "sample": 0.25,
            "type": "constant",
        },
        "7365074658267457622": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5129600158435556044": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6438746900289304097": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2931840470432389181": {
            "sample": 0.25,
            "type": "constant",
        },
        "8636506588292470960": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3429205851213447537": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5781571519975741757": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6058765923391743971": {
            "sample": 0.25,
            "type": "constant",
        },
        "4720623093796257276": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9203803209823291024": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1649397985054189452": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1372203581638187238": {
            "sample": 0.25,
            "type": "constant",
        },
        "5992055023821270614": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8647517143645657351": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4125199373555654035": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6654189643632347212": {
            "sample": 0.25,
            "type": "constant",
        },
        "6376995240216344998": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1216547638615726142": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-995053579417010894": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2028060506889356109_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2028060506889356109_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1341480667209356385_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1341480667209356385_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4343980153653162859_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4343980153653162859_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-771203908085893774_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-771203908085893774_q": {
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
        "B4/drive_mixer_a43": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/acquisition_mixer_e0d": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_ddf": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B3/drive_mixer_d45": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_d55": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_ed3": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/drive_mixer_e2b": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B1/acquisition_mixer_ba2": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

