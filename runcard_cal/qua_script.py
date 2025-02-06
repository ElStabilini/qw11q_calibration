
# Single QUA script generated at 2025-02-06 16:12:02.462785
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
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("2624843220373211171", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("2846337279571926419", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("1698515462395057646", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("8079547096598690765", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-7548111521221000444", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-8169437289107693988", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("7924941115839563408", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("2304949737988847278", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-5750183541905811877", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("4502709425992014141", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-3090833452840056999", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("4005344045210955785", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-6235870739271604052", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-671579705638174888", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-6291571083488891018", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-2484399177246267367", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("2037918592843735949", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-286639489243100504", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("-3415895905877943771", "B4/drive")
        wait(11, "B4/flux")
        play("-65145430044385256", "B4/flux")
        wait(46, "B4/drive")
        play("-2654805276654381902", "B4/drive")
        wait(66, "B4/acquisition")
        measure("457828904132122927", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("457828904132122927_B4|acquisition_shots")


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
                "2624843220373211171": "2624843220373211171",
                "2846337279571926419": "2846337279571926419",
                "1698515462395057646": "1698515462395057646",
                "8079547096598690765": "8079547096598690765",
                "-7548111521221000444": "-7548111521221000444",
                "-8169437289107693988": "-8169437289107693988",
                "7924941115839563408": "7924941115839563408",
                "2304949737988847278": "2304949737988847278",
                "-5750183541905811877": "-5750183541905811877",
                "4502709425992014141": "4502709425992014141",
                "-3090833452840056999": "-3090833452840056999",
                "4005344045210955785": "4005344045210955785",
                "-6235870739271604052": "-6235870739271604052",
                "-671579705638174888": "-671579705638174888",
                "-6291571083488891018": "-6291571083488891018",
                "-2484399177246267367": "-2484399177246267367",
                "2037918592843735949": "2037918592843735949",
                "-286639489243100504": "-286639489243100504",
                "-65145430044385256": "-65145430044385256",
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
                "457828904132122927": "457828904132122927_B4/acquisition",
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
                "-3415895905877943771": "-3415895905877943771",
                "-2654805276654381902": "-2654805276654381902",
            },
        },
    },
    "pulses": {
        "-3415895905877943771": {
            "length": 40,
            "waveforms": {
                "I": "-3415895905877943771_i",
                "Q": "-3415895905877943771_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1026877093097855471": {
            "length": 16,
            "waveforms": {
                "single": "1026877093097855471",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "457828904132122927_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5370586333104135786_i",
                "Q": "5370586333104135786_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "7407908727301488590": {
            "length": 16,
            "waveforms": {
                "single": "7407908727301488590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4093833137579460699": {
            "length": 16,
            "waveforms": {
                "single": "-4093833137579460699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "428484632510542617": {
            "length": 16,
            "waveforms": {
                "single": "428484632510542617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-192841135376150927": {
            "length": 16,
            "waveforms": {
                "single": "-192841135376150927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8679340657326501928": {
            "length": 16,
            "waveforms": {
                "single": "8679340657326501928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3337136367450470510": {
            "length": 16,
            "waveforms": {
                "single": "3337136367450470510",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7569643728379882825": {
            "length": 16,
            "waveforms": {
                "single": "-7569643728379882825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1617574471373344875": {
            "length": 16,
            "waveforms": {
                "single": "-1617574471373344875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2160266587743370763": {
            "length": 16,
            "waveforms": {
                "single": "-2160266587743370763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2437460991159372977": {
            "length": 16,
            "waveforms": {
                "single": "-2437460991159372977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4360864282724572028": {
            "length": 16,
            "waveforms": {
                "single": "-4360864282724572028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "82819835848763632": {
            "length": 16,
            "waveforms": {
                "single": "82819835848763632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3889991742091387283": {
            "length": 16,
            "waveforms": {
                "single": "3889991742091387283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7611750122789562006": {
            "length": 16,
            "waveforms": {
                "single": "-7611750122789562006",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5215002573069273480": {
            "length": 16,
            "waveforms": {
                "single": "5215002573069273480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7689956664488442557": {
            "length": 20,
            "waveforms": {
                "single": "7689956664488442557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1884605616518456204": {
            "length": 20,
            "waveforms": {
                "single": "-1884605616518456204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7226809906394487622": {
            "length": 20,
            "waveforms": {
                "single": "-7226809906394487622",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6915396880291381987": {
            "length": 20,
            "waveforms": {
                "single": "6915396880291381987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4563031211529087767": {
            "length": 24,
            "waveforms": {
                "single": "4563031211529087767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3104323844992462602": {
            "length": 24,
            "waveforms": {
                "single": "-3104323844992462602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5767857947710190253": {
            "length": 24,
            "waveforms": {
                "single": "5767857947710190253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4824011040818526963": {
            "length": 24,
            "waveforms": {
                "single": "4824011040818526963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4947971427924162151": {
            "length": 28,
            "waveforms": {
                "single": "4947971427924162151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8878921203602306089": {
            "length": 28,
            "waveforms": {
                "single": "-8878921203602306089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5247916620969430154": {
            "length": 28,
            "waveforms": {
                "single": "-5247916620969430154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1697085587859172173": {
            "length": 28,
            "waveforms": {
                "single": "1697085587859172173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5970269468662378196": {
            "length": 32,
            "waveforms": {
                "single": "-5970269468662378196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1447951698572374880": {
            "length": 32,
            "waveforms": {
                "single": "-1447951698572374880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4933079935631258239": {
            "length": 32,
            "waveforms": {
                "single": "4933079935631258239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2082025804254246557": {
            "length": 32,
            "waveforms": {
                "single": "2082025804254246557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2303519863452961805": {
            "length": 36,
            "waveforms": {
                "single": "2303519863452961805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-891665632394741207": {
            "length": 36,
            "waveforms": {
                "single": "-891665632394741207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6204511865656271577": {
            "length": 36,
            "waveforms": {
                "single": "6204511865656271577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4722773610654843916": {
            "length": 36,
            "waveforms": {
                "single": "4722773610654843916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4313897322242290474": {
            "length": 40,
            "waveforms": {
                "single": "-4313897322242290474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4092403263043575226": {
            "length": 40,
            "waveforms": {
                "single": "-4092403263043575226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4779778529659077629": {
            "length": 40,
            "waveforms": {
                "single": "4779778529659077629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6293000958024776491": {
            "length": 40,
            "waveforms": {
                "single": "-6293000958024776491",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1912528331202215288": {
            "length": 44,
            "waveforms": {
                "single": "1912528331202215288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3338566241986355983": {
            "length": 44,
            "waveforms": {
                "single": "3338566241986355983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1415162950421156932": {
            "length": 44,
            "waveforms": {
                "single": "1415162950421156932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5536325929989522846": {
            "length": 44,
            "waveforms": {
                "single": "5536325929989522846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1214397121757139502": {
            "length": 48,
            "waveforms": {
                "single": "-1214397121757139502",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8166606314431310206": {
            "length": 48,
            "waveforms": {
                "single": "-8166606314431310206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4359434408188686555": {
            "length": 48,
            "waveforms": {
                "single": "-4359434408188686555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4980760176075380099": {
            "length": 48,
            "waveforms": {
                "single": "-4980760176075380099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7831814307452391781": {
            "length": 52,
            "waveforms": {
                "single": "-7831814307452391781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7610320248253676533": {
            "length": 52,
            "waveforms": {
                "single": "-7610320248253676533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3071535096841244654": {
            "length": 52,
            "waveforms": {
                "single": "3071535096841244654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3293029156039959902": {
            "length": 52,
            "waveforms": {
                "single": "3293029156039959902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3015834752623957688": {
            "length": 56,
            "waveforms": {
                "single": "3015834752623957688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7225380031858602149": {
            "length": 56,
            "waveforms": {
                "single": "-7225380031858602149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7003885972659886901": {
            "length": 56,
            "waveforms": {
                "single": "-7003885972659886901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7722745412639660505": {
            "length": 56,
            "waveforms": {
                "single": "-7722745412639660505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4806126284656720038": {
            "length": 60,
            "waveforms": {
                "single": "-4806126284656720038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8094438588891594677": {
            "length": 60,
            "waveforms": {
                "single": "8094438588891594677",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "427083532370044308": {
            "length": 60,
            "waveforms": {
                "single": "427083532370044308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "648577591568759556": {
            "length": 60,
            "waveforms": {
                "single": "648577591568759556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2624843220373211171": {
            "length": 64,
            "waveforms": {
                "single": "2624843220373211171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2846337279571926419": {
            "length": 64,
            "waveforms": {
                "single": "2846337279571926419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1698515462395057646": {
            "length": 64,
            "waveforms": {
                "single": "1698515462395057646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8079547096598690765": {
            "length": 64,
            "waveforms": {
                "single": "8079547096598690765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7548111521221000444": {
            "length": 68,
            "waveforms": {
                "single": "-7548111521221000444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8169437289107693988": {
            "length": 68,
            "waveforms": {
                "single": "-8169437289107693988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7924941115839563408": {
            "length": 68,
            "waveforms": {
                "single": "7924941115839563408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304949737988847278": {
            "length": 68,
            "waveforms": {
                "single": "2304949737988847278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5750183541905811877": {
            "length": 72,
            "waveforms": {
                "single": "-5750183541905811877",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4502709425992014141": {
            "length": 72,
            "waveforms": {
                "single": "4502709425992014141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3090833452840056999": {
            "length": 72,
            "waveforms": {
                "single": "-3090833452840056999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4005344045210955785": {
            "length": 72,
            "waveforms": {
                "single": "4005344045210955785",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6235870739271604052": {
            "length": 76,
            "waveforms": {
                "single": "-6235870739271604052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-671579705638174888": {
            "length": 76,
            "waveforms": {
                "single": "-671579705638174888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6291571083488891018": {
            "length": 76,
            "waveforms": {
                "single": "-6291571083488891018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2484399177246267367": {
            "length": 76,
            "waveforms": {
                "single": "-2484399177246267367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2037918592843735949": {
            "length": 80,
            "waveforms": {
                "single": "2037918592843735949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-286639489243100504": {
            "length": 80,
            "waveforms": {
                "single": "-286639489243100504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-65145430044385256": {
            "length": 80,
            "waveforms": {
                "single": "-65145430044385256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2654805276654381902": {
            "length": 40,
            "waveforms": {
                "I": "-2654805276654381902_i",
                "Q": "-2654805276654381902_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-3415895905877943771_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-3415895905877943771_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "1026877093097855471": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "5370586333104135786_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "5370586333104135786_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7407908727301488590": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-4093833137579460699": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "428484632510542617": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-192841135376150927": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "8679340657326501928": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3337136367450470510": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-7569643728379882825": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-1617574471373344875": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-2160266587743370763": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-2437460991159372977": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-4360864282724572028": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "82819835848763632": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3889991742091387283": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7611750122789562006": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "5215002573069273480": {
            "sample": 0.25,
            "type": "constant",
        },
        "7689956664488442557": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1884605616518456204": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7226809906394487622": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6915396880291381987": {
            "sample": 0.25,
            "type": "constant",
        },
        "4563031211529087767": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3104323844992462602": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5767857947710190253": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "4824011040818526963": {
            "sample": 0.25,
            "type": "constant",
        },
        "4947971427924162151": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8878921203602306089": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5247916620969430154": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1697085587859172173": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5970269468662378196": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1447951698572374880": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4933079935631258239": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "2082025804254246557": {
            "sample": 0.25,
            "type": "constant",
        },
        "2303519863452961805": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-891665632394741207": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6204511865656271577": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "4722773610654843916": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4313897322242290474": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4092403263043575226": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4779778529659077629": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-6293000958024776491": {
            "sample": 0.25,
            "type": "constant",
        },
        "1912528331202215288": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3338566241986355983": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1415162950421156932": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "5536325929989522846": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1214397121757139502": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8166606314431310206": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4359434408188686555": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-4980760176075380099": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7831814307452391781": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7610320248253676533": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3071535096841244654": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "3293029156039959902": {
            "sample": 0.25,
            "type": "constant",
        },
        "3015834752623957688": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7225380031858602149": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7003885972659886901": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-7722745412639660505": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4806126284656720038": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8094438588891594677": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "427083532370044308": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "648577591568759556": {
            "sample": 0.25,
            "type": "constant",
        },
        "2624843220373211171": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2846337279571926419": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1698515462395057646": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "8079547096598690765": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7548111521221000444": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8169437289107693988": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7924941115839563408": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "2304949737988847278": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5750183541905811877": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4502709425992014141": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3090833452840056999": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "4005344045210955785": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6235870739271604052": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-671579705638174888": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6291571083488891018": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-2484399177246267367": {
            "sample": 0.25,
            "type": "constant",
        },
        "2037918592843735949": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-286639489243100504": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-65145430044385256": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-2654805276654381902_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-2654805276654381902_q": {
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
                "2624843220373211171": "2624843220373211171",
                "2846337279571926419": "2846337279571926419",
                "1698515462395057646": "1698515462395057646",
                "8079547096598690765": "8079547096598690765",
                "-7548111521221000444": "-7548111521221000444",
                "-8169437289107693988": "-8169437289107693988",
                "7924941115839563408": "7924941115839563408",
                "2304949737988847278": "2304949737988847278",
                "-5750183541905811877": "-5750183541905811877",
                "4502709425992014141": "4502709425992014141",
                "-3090833452840056999": "-3090833452840056999",
                "4005344045210955785": "4005344045210955785",
                "-6235870739271604052": "-6235870739271604052",
                "-671579705638174888": "-671579705638174888",
                "-6291571083488891018": "-6291571083488891018",
                "-2484399177246267367": "-2484399177246267367",
                "2037918592843735949": "2037918592843735949",
                "-286639489243100504": "-286639489243100504",
                "-65145430044385256": "-65145430044385256",
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
                "457828904132122927": "457828904132122927_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_024",
                "lo_frequency": 7370000000.0,
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
                "-3415895905877943771": "-3415895905877943771",
                "-2654805276654381902": "-2654805276654381902",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_a0a",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "-3415895905877943771": {
            "length": 40,
            "waveforms": {
                "I": "-3415895905877943771_i",
                "Q": "-3415895905877943771_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1026877093097855471": {
            "length": 16,
            "waveforms": {
                "single": "1026877093097855471",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "457828904132122927_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5370586333104135786_i",
                "Q": "5370586333104135786_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "7407908727301488590": {
            "length": 16,
            "waveforms": {
                "single": "7407908727301488590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4093833137579460699": {
            "length": 16,
            "waveforms": {
                "single": "-4093833137579460699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "428484632510542617": {
            "length": 16,
            "waveforms": {
                "single": "428484632510542617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-192841135376150927": {
            "length": 16,
            "waveforms": {
                "single": "-192841135376150927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8679340657326501928": {
            "length": 16,
            "waveforms": {
                "single": "8679340657326501928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3337136367450470510": {
            "length": 16,
            "waveforms": {
                "single": "3337136367450470510",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7569643728379882825": {
            "length": 16,
            "waveforms": {
                "single": "-7569643728379882825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1617574471373344875": {
            "length": 16,
            "waveforms": {
                "single": "-1617574471373344875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2160266587743370763": {
            "length": 16,
            "waveforms": {
                "single": "-2160266587743370763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2437460991159372977": {
            "length": 16,
            "waveforms": {
                "single": "-2437460991159372977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4360864282724572028": {
            "length": 16,
            "waveforms": {
                "single": "-4360864282724572028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "82819835848763632": {
            "length": 16,
            "waveforms": {
                "single": "82819835848763632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3889991742091387283": {
            "length": 16,
            "waveforms": {
                "single": "3889991742091387283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7611750122789562006": {
            "length": 16,
            "waveforms": {
                "single": "-7611750122789562006",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5215002573069273480": {
            "length": 16,
            "waveforms": {
                "single": "5215002573069273480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7689956664488442557": {
            "length": 20,
            "waveforms": {
                "single": "7689956664488442557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1884605616518456204": {
            "length": 20,
            "waveforms": {
                "single": "-1884605616518456204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7226809906394487622": {
            "length": 20,
            "waveforms": {
                "single": "-7226809906394487622",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6915396880291381987": {
            "length": 20,
            "waveforms": {
                "single": "6915396880291381987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4563031211529087767": {
            "length": 24,
            "waveforms": {
                "single": "4563031211529087767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3104323844992462602": {
            "length": 24,
            "waveforms": {
                "single": "-3104323844992462602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5767857947710190253": {
            "length": 24,
            "waveforms": {
                "single": "5767857947710190253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4824011040818526963": {
            "length": 24,
            "waveforms": {
                "single": "4824011040818526963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4947971427924162151": {
            "length": 28,
            "waveforms": {
                "single": "4947971427924162151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8878921203602306089": {
            "length": 28,
            "waveforms": {
                "single": "-8878921203602306089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5247916620969430154": {
            "length": 28,
            "waveforms": {
                "single": "-5247916620969430154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1697085587859172173": {
            "length": 28,
            "waveforms": {
                "single": "1697085587859172173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5970269468662378196": {
            "length": 32,
            "waveforms": {
                "single": "-5970269468662378196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1447951698572374880": {
            "length": 32,
            "waveforms": {
                "single": "-1447951698572374880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4933079935631258239": {
            "length": 32,
            "waveforms": {
                "single": "4933079935631258239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2082025804254246557": {
            "length": 32,
            "waveforms": {
                "single": "2082025804254246557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2303519863452961805": {
            "length": 36,
            "waveforms": {
                "single": "2303519863452961805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-891665632394741207": {
            "length": 36,
            "waveforms": {
                "single": "-891665632394741207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6204511865656271577": {
            "length": 36,
            "waveforms": {
                "single": "6204511865656271577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4722773610654843916": {
            "length": 36,
            "waveforms": {
                "single": "4722773610654843916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4313897322242290474": {
            "length": 40,
            "waveforms": {
                "single": "-4313897322242290474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4092403263043575226": {
            "length": 40,
            "waveforms": {
                "single": "-4092403263043575226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4779778529659077629": {
            "length": 40,
            "waveforms": {
                "single": "4779778529659077629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6293000958024776491": {
            "length": 40,
            "waveforms": {
                "single": "-6293000958024776491",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1912528331202215288": {
            "length": 44,
            "waveforms": {
                "single": "1912528331202215288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3338566241986355983": {
            "length": 44,
            "waveforms": {
                "single": "3338566241986355983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1415162950421156932": {
            "length": 44,
            "waveforms": {
                "single": "1415162950421156932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5536325929989522846": {
            "length": 44,
            "waveforms": {
                "single": "5536325929989522846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1214397121757139502": {
            "length": 48,
            "waveforms": {
                "single": "-1214397121757139502",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8166606314431310206": {
            "length": 48,
            "waveforms": {
                "single": "-8166606314431310206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4359434408188686555": {
            "length": 48,
            "waveforms": {
                "single": "-4359434408188686555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4980760176075380099": {
            "length": 48,
            "waveforms": {
                "single": "-4980760176075380099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7831814307452391781": {
            "length": 52,
            "waveforms": {
                "single": "-7831814307452391781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7610320248253676533": {
            "length": 52,
            "waveforms": {
                "single": "-7610320248253676533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3071535096841244654": {
            "length": 52,
            "waveforms": {
                "single": "3071535096841244654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3293029156039959902": {
            "length": 52,
            "waveforms": {
                "single": "3293029156039959902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3015834752623957688": {
            "length": 56,
            "waveforms": {
                "single": "3015834752623957688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7225380031858602149": {
            "length": 56,
            "waveforms": {
                "single": "-7225380031858602149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7003885972659886901": {
            "length": 56,
            "waveforms": {
                "single": "-7003885972659886901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7722745412639660505": {
            "length": 56,
            "waveforms": {
                "single": "-7722745412639660505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4806126284656720038": {
            "length": 60,
            "waveforms": {
                "single": "-4806126284656720038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8094438588891594677": {
            "length": 60,
            "waveforms": {
                "single": "8094438588891594677",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "427083532370044308": {
            "length": 60,
            "waveforms": {
                "single": "427083532370044308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "648577591568759556": {
            "length": 60,
            "waveforms": {
                "single": "648577591568759556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2624843220373211171": {
            "length": 64,
            "waveforms": {
                "single": "2624843220373211171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2846337279571926419": {
            "length": 64,
            "waveforms": {
                "single": "2846337279571926419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1698515462395057646": {
            "length": 64,
            "waveforms": {
                "single": "1698515462395057646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8079547096598690765": {
            "length": 64,
            "waveforms": {
                "single": "8079547096598690765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7548111521221000444": {
            "length": 68,
            "waveforms": {
                "single": "-7548111521221000444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8169437289107693988": {
            "length": 68,
            "waveforms": {
                "single": "-8169437289107693988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7924941115839563408": {
            "length": 68,
            "waveforms": {
                "single": "7924941115839563408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304949737988847278": {
            "length": 68,
            "waveforms": {
                "single": "2304949737988847278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5750183541905811877": {
            "length": 72,
            "waveforms": {
                "single": "-5750183541905811877",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4502709425992014141": {
            "length": 72,
            "waveforms": {
                "single": "4502709425992014141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3090833452840056999": {
            "length": 72,
            "waveforms": {
                "single": "-3090833452840056999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4005344045210955785": {
            "length": 72,
            "waveforms": {
                "single": "4005344045210955785",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6235870739271604052": {
            "length": 76,
            "waveforms": {
                "single": "-6235870739271604052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-671579705638174888": {
            "length": 76,
            "waveforms": {
                "single": "-671579705638174888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6291571083488891018": {
            "length": 76,
            "waveforms": {
                "single": "-6291571083488891018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2484399177246267367": {
            "length": 76,
            "waveforms": {
                "single": "-2484399177246267367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2037918592843735949": {
            "length": 80,
            "waveforms": {
                "single": "2037918592843735949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-286639489243100504": {
            "length": 80,
            "waveforms": {
                "single": "-286639489243100504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-65145430044385256": {
            "length": 80,
            "waveforms": {
                "single": "-65145430044385256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2654805276654381902": {
            "length": 40,
            "waveforms": {
                "I": "-2654805276654381902_i",
                "Q": "-2654805276654381902_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-3415895905877943771_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3415895905877943771_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1026877093097855471": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5370586333104135786_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "5370586333104135786_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7407908727301488590": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4093833137579460699": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "428484632510542617": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-192841135376150927": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8679340657326501928": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3337136367450470510": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7569643728379882825": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1617574471373344875": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2160266587743370763": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2437460991159372977": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4360864282724572028": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "82819835848763632": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3889991742091387283": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7611750122789562006": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5215002573069273480": {
            "sample": 0.25,
            "type": "constant",
        },
        "7689956664488442557": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1884605616518456204": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7226809906394487622": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6915396880291381987": {
            "sample": 0.25,
            "type": "constant",
        },
        "4563031211529087767": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3104323844992462602": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5767857947710190253": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4824011040818526963": {
            "sample": 0.25,
            "type": "constant",
        },
        "4947971427924162151": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8878921203602306089": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5247916620969430154": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1697085587859172173": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5970269468662378196": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1447951698572374880": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4933079935631258239": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2082025804254246557": {
            "sample": 0.25,
            "type": "constant",
        },
        "2303519863452961805": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-891665632394741207": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6204511865656271577": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4722773610654843916": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4313897322242290474": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4092403263043575226": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4779778529659077629": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6293000958024776491": {
            "sample": 0.25,
            "type": "constant",
        },
        "1912528331202215288": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3338566241986355983": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1415162950421156932": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5536325929989522846": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1214397121757139502": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8166606314431310206": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4359434408188686555": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4980760176075380099": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7831814307452391781": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7610320248253676533": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3071535096841244654": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3293029156039959902": {
            "sample": 0.25,
            "type": "constant",
        },
        "3015834752623957688": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7225380031858602149": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7003885972659886901": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7722745412639660505": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4806126284656720038": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8094438588891594677": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "427083532370044308": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "648577591568759556": {
            "sample": 0.25,
            "type": "constant",
        },
        "2624843220373211171": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2846337279571926419": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1698515462395057646": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8079547096598690765": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7548111521221000444": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8169437289107693988": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7924941115839563408": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2304949737988847278": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5750183541905811877": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4502709425992014141": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3090833452840056999": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4005344045210955785": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6235870739271604052": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-671579705638174888": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6291571083488891018": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2484399177246267367": {
            "sample": 0.25,
            "type": "constant",
        },
        "2037918592843735949": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-286639489243100504": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-65145430044385256": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2654805276654381902_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2654805276654381902_q": {
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
        "B4/acquisition_mixer_024": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_a0a": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

