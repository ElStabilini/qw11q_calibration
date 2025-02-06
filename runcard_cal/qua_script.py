
# Single QUA script generated at 2025-02-06 08:04:17.474980
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
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-5234921574303221643", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("4630193170221495589", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-3037161886300054780", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-8583341086461291681", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-3963489644278208305", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-1859550052235727563", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-6164087339259409570", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("2041441949967582209", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-3578549427883133921", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("1985741605750295243", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-5779147122864335186", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-8131512791626629406", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-8752838559513322950", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("1500054408384503068", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-824503673702333385", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("6271673824348679399", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("3919308155586385179", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("-1100374995284676493", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("5937570594762831758", "B4/drive")
        wait(11, "B4/flux")
        play("1718710460605183914", "B4/flux")
        wait(46, "B4/drive")
        play("6698661223986393627", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4983337041304198942", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.9730343180892005)-(v3*-0.2306603906627328))>-0.0004384486988547942)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("4983337041304198942_B4|acquisition_shots")


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
                "-5234921574303221643": "-5234921574303221643",
                "4630193170221495589": "4630193170221495589",
                "-3037161886300054780": "-3037161886300054780",
                "-8583341086461291681": "-8583341086461291681",
                "-3963489644278208305": "-3963489644278208305",
                "-1859550052235727563": "-1859550052235727563",
                "-6164087339259409570": "-6164087339259409570",
                "2041441949967582209": "2041441949967582209",
                "-3578549427883133921": "-3578549427883133921",
                "1985741605750295243": "1985741605750295243",
                "-5779147122864335186": "-5779147122864335186",
                "-8131512791626629406": "-8131512791626629406",
                "-8752838559513322950": "-8752838559513322950",
                "1500054408384503068": "1500054408384503068",
                "-824503673702333385": "-824503673702333385",
                "6271673824348679399": "6271673824348679399",
                "3919308155586385179": "3919308155586385179",
                "-1100374995284676493": "-1100374995284676493",
                "1718710460605183914": "1718710460605183914",
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
                "4983337041304198942": "4983337041304198942_B4/acquisition",
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
                "5937570594762831758": "5937570594762831758",
                "6698661223986393627": "6698661223986393627",
            },
        },
    },
    "pulses": {
        "5937570594762831758": {
            "length": 40,
            "waveforms": {
                "I": "5937570594762831758_i",
                "Q": "5937570594762831758_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4507736934933058392": {
            "length": 16,
            "waveforms": {
                "single": "-4507736934933058392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4983337041304198942_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "279758784901407420_i",
                "Q": "279758784901407420_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6271652082254942855": {
            "length": 16,
            "waveforms": {
                "single": "6271652082254942855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-606744932729748620": {
            "length": 16,
            "waveforms": {
                "single": "-606744932729748620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8469411770258109718": {
            "length": 16,
            "waveforms": {
                "single": "8469411770258109718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7321589953081240945": {
            "length": 16,
            "waveforms": {
                "single": "7321589953081240945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7543084012279956193": {
            "length": 16,
            "waveforms": {
                "single": "7543084012279956193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-221804716334674236": {
            "length": 16,
            "waveforms": {
                "single": "-221804716334674236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5342486317298754928": {
            "length": 16,
            "waveforms": {
                "single": "5342486317298754928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4898728467183804909": {
            "length": 16,
            "waveforms": {
                "single": "-4898728467183804909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3472690556399664214": {
            "length": 16,
            "waveforms": {
                "single": "-3472690556399664214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "334481349842959437": {
            "length": 16,
            "waveforms": {
                "single": "334481349842959437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1274930868396497351": {
            "length": 16,
            "waveforms": {
                "single": "-1274930868396497351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8025653920143159699": {
            "length": 16,
            "waveforms": {
                "single": "-8025653920143159699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2753735097044841548": {
            "length": 16,
            "waveforms": {
                "single": "2753735097044841548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7276052867134844864": {
            "length": 16,
            "waveforms": {
                "single": "7276052867134844864",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4951494785048008411": {
            "length": 16,
            "waveforms": {
                "single": "4951494785048008411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-668496592802707719": {
            "length": 20,
            "waveforms": {
                "single": "-668496592802707719",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3020862261565001939": {
            "length": 20,
            "waveforms": {
                "single": "-3020862261565001939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3739721701544775543": {
            "length": 20,
            "waveforms": {
                "single": "-3739721701544775543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5221459956546203204": {
            "length": 20,
            "waveforms": {
                "single": "-5221459956546203204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5842785724432896748": {
            "length": 24,
            "waveforms": {
                "single": "-5842785724432896748",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4410107243464929270": {
            "length": 24,
            "waveforms": {
                "single": "4410107243464929270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4631601302663644518": {
            "length": 24,
            "waveforms": {
                "single": "4631601302663644518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8311099245668239042": {
            "length": 24,
            "waveforms": {
                "single": "8311099245668239042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6829360990666811381": {
            "length": 28,
            "waveforms": {
                "single": "6829360990666811381",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6605667325214691137": {
            "length": 28,
            "waveforms": {
                "single": "-6605667325214691137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6384173266015975889": {
            "length": 28,
            "waveforms": {
                "single": "-6384173266015975889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6162679206817260641": {
            "length": 28,
            "waveforms": {
                "single": "-6162679206817260641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4186413578012809026": {
            "length": 32,
            "waveforms": {
                "single": "-4186413578012809026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3964919518814093778": {
            "length": 32,
            "waveforms": {
                "single": "-3964919518814093778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1046796239013955320": {
            "length": 32,
            "waveforms": {
                "single": "1046796239013955320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1268290298212670568": {
            "length": 32,
            "waveforms": {
                "single": "1268290298212670568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4184909426195611035": {
            "length": 36,
            "waveforms": {
                "single": "4184909426195611035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3466049986215837431": {
            "length": 36,
            "waveforms": {
                "single": "3466049986215837431",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1113684317453543211": {
            "length": 36,
            "waveforms": {
                "single": "1113684317453543211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6051587897592113080": {
            "length": 36,
            "waveforms": {
                "single": "6051587897592113080",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5885303733417719542": {
            "length": 40,
            "waveforms": {
                "single": "5885303733417719542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2308547372394006056": {
            "length": 40,
            "waveforms": {
                "single": "-2308547372394006056",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4072484261809627063": {
            "length": 40,
            "waveforms": {
                "single": "4072484261809627063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1720118593047332843": {
            "length": 40,
            "waveforms": {
                "single": "1720118593047332843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "110706374807876055": {
            "length": 44,
            "waveforms": {
                "single": "110706374807876055",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3917878281050499706": {
            "length": 44,
            "waveforms": {
                "single": "3917878281050499706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5343916191834640401": {
            "length": 44,
            "waveforms": {
                "single": "5343916191834640401",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9151088098077264052": {
            "length": 44,
            "waveforms": {
                "single": "9151088098077264052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7541675879837807264": {
            "length": 48,
            "waveforms": {
                "single": "7541675879837807264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7097896287629120701": {
            "length": 48,
            "waveforms": {
                "single": "-7097896287629120701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6876402228430405453": {
            "length": 48,
            "waveforms": {
                "single": "-6876402228430405453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2533670912382011773": {
            "length": 48,
            "waveforms": {
                "single": "2533670912382011773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2755164971580727021": {
            "length": 52,
            "waveforms": {
                "single": "2755164971580727021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5574250427470587428": {
            "length": 52,
            "waveforms": {
                "single": "5574250427470587428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "554567276599525756": {
            "length": 52,
            "waveforms": {
                "single": "554567276599525756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7639283829212199842": {
            "length": 52,
            "waveforms": {
                "single": "-7639283829212199842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8260609597098893386": {
            "length": 56,
            "waveforms": {
                "single": "-8260609597098893386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8704396221609230569": {
            "length": 56,
            "waveforms": {
                "single": "8704396221609230569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5220030082010317731": {
            "length": 56,
            "waveforms": {
                "single": "-5220030082010317731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5841355849897011275": {
            "length": 56,
            "waveforms": {
                "single": "-5841355849897011275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "13179735016446615": {
            "length": 60,
            "waveforms": {
                "single": "13179735016446615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7757118623180850379": {
            "length": 60,
            "waveforms": {
                "single": "7757118623180850379",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2089884287871674590": {
            "length": 60,
            "waveforms": {
                "single": "-2089884287871674590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2432433482218328726": {
            "length": 60,
            "waveforms": {
                "single": "2432433482218328726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5234921574303221643": {
            "length": 64,
            "waveforms": {
                "single": "-5234921574303221643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4630193170221495589": {
            "length": 64,
            "waveforms": {
                "single": "4630193170221495589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3037161886300054780": {
            "length": 64,
            "waveforms": {
                "single": "-3037161886300054780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8583341086461291681": {
            "length": 64,
            "waveforms": {
                "single": "-8583341086461291681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3963489644278208305": {
            "length": 68,
            "waveforms": {
                "single": "-3963489644278208305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1859550052235727563": {
            "length": 68,
            "waveforms": {
                "single": "-1859550052235727563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6164087339259409570": {
            "length": 68,
            "waveforms": {
                "single": "-6164087339259409570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2041441949967582209": {
            "length": 68,
            "waveforms": {
                "single": "2041441949967582209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3578549427883133921": {
            "length": 72,
            "waveforms": {
                "single": "-3578549427883133921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1985741605750295243": {
            "length": 72,
            "waveforms": {
                "single": "1985741605750295243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5779147122864335186": {
            "length": 72,
            "waveforms": {
                "single": "-5779147122864335186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8131512791626629406": {
            "length": 72,
            "waveforms": {
                "single": "-8131512791626629406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8752838559513322950": {
            "length": 76,
            "waveforms": {
                "single": "-8752838559513322950",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1500054408384503068": {
            "length": 76,
            "waveforms": {
                "single": "1500054408384503068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-824503673702333385": {
            "length": 76,
            "waveforms": {
                "single": "-824503673702333385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6271673824348679399": {
            "length": 76,
            "waveforms": {
                "single": "6271673824348679399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3919308155586385179": {
            "length": 80,
            "waveforms": {
                "single": "3919308155586385179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1100374995284676493": {
            "length": 80,
            "waveforms": {
                "single": "-1100374995284676493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1718710460605183914": {
            "length": 80,
            "waveforms": {
                "single": "1718710460605183914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6698661223986393627": {
            "length": 40,
            "waveforms": {
                "I": "6698661223986393627_i",
                "Q": "6698661223986393627_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5937570594762831758_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "5937570594762831758_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-4507736934933058392": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "279758784901407420_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "279758784901407420_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6271652082254942855": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-606744932729748620": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "8469411770258109718": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "7321589953081240945": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "7543084012279956193": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-221804716334674236": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "5342486317298754928": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-4898728467183804909": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-3472690556399664214": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "334481349842959437": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-1274930868396497351": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8025653920143159699": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2753735097044841548": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7276052867134844864": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "4951494785048008411": {
            "sample": 0.25,
            "type": "constant",
        },
        "-668496592802707719": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3020862261565001939": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3739721701544775543": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5221459956546203204": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5842785724432896748": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4410107243464929270": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4631601302663644518": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "8311099245668239042": {
            "sample": 0.25,
            "type": "constant",
        },
        "6829360990666811381": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6605667325214691137": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6384173266015975889": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-6162679206817260641": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4186413578012809026": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3964919518814093778": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1046796239013955320": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "1268290298212670568": {
            "sample": 0.25,
            "type": "constant",
        },
        "4184909426195611035": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3466049986215837431": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1113684317453543211": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "6051587897592113080": {
            "sample": 0.25,
            "type": "constant",
        },
        "5885303733417719542": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2308547372394006056": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4072484261809627063": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "1720118593047332843": {
            "sample": 0.25,
            "type": "constant",
        },
        "110706374807876055": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3917878281050499706": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5343916191834640401": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "9151088098077264052": {
            "sample": 0.25,
            "type": "constant",
        },
        "7541675879837807264": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7097896287629120701": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6876402228430405453": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "2533670912382011773": {
            "sample": 0.25,
            "type": "constant",
        },
        "2755164971580727021": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5574250427470587428": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "554567276599525756": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-7639283829212199842": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8260609597098893386": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8704396221609230569": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5220030082010317731": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-5841355849897011275": {
            "sample": 0.25,
            "type": "constant",
        },
        "13179735016446615": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7757118623180850379": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2089884287871674590": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "2432433482218328726": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5234921574303221643": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4630193170221495589": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3037161886300054780": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-8583341086461291681": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3963489644278208305": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1859550052235727563": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6164087339259409570": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "2041441949967582209": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3578549427883133921": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1985741605750295243": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5779147122864335186": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-8131512791626629406": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8752838559513322950": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1500054408384503068": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-824503673702333385": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6271673824348679399": {
            "sample": 0.25,
            "type": "constant",
        },
        "3919308155586385179": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1100374995284676493": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1718710460605183914": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "6698661223986393627_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "6698661223986393627_q": {
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
                "-5234921574303221643": "-5234921574303221643",
                "4630193170221495589": "4630193170221495589",
                "-3037161886300054780": "-3037161886300054780",
                "-8583341086461291681": "-8583341086461291681",
                "-3963489644278208305": "-3963489644278208305",
                "-1859550052235727563": "-1859550052235727563",
                "-6164087339259409570": "-6164087339259409570",
                "2041441949967582209": "2041441949967582209",
                "-3578549427883133921": "-3578549427883133921",
                "1985741605750295243": "1985741605750295243",
                "-5779147122864335186": "-5779147122864335186",
                "-8131512791626629406": "-8131512791626629406",
                "-8752838559513322950": "-8752838559513322950",
                "1500054408384503068": "1500054408384503068",
                "-824503673702333385": "-824503673702333385",
                "6271673824348679399": "6271673824348679399",
                "3919308155586385179": "3919308155586385179",
                "-1100374995284676493": "-1100374995284676493",
                "1718710460605183914": "1718710460605183914",
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
                "4983337041304198942": "4983337041304198942_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_5a9",
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
                "5937570594762831758": "5937570594762831758",
                "6698661223986393627": "6698661223986393627",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_719",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "5937570594762831758": {
            "length": 40,
            "waveforms": {
                "I": "5937570594762831758_i",
                "Q": "5937570594762831758_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4507736934933058392": {
            "length": 16,
            "waveforms": {
                "single": "-4507736934933058392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4983337041304198942_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "279758784901407420_i",
                "Q": "279758784901407420_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "6271652082254942855": {
            "length": 16,
            "waveforms": {
                "single": "6271652082254942855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-606744932729748620": {
            "length": 16,
            "waveforms": {
                "single": "-606744932729748620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8469411770258109718": {
            "length": 16,
            "waveforms": {
                "single": "8469411770258109718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7321589953081240945": {
            "length": 16,
            "waveforms": {
                "single": "7321589953081240945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7543084012279956193": {
            "length": 16,
            "waveforms": {
                "single": "7543084012279956193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-221804716334674236": {
            "length": 16,
            "waveforms": {
                "single": "-221804716334674236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5342486317298754928": {
            "length": 16,
            "waveforms": {
                "single": "5342486317298754928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4898728467183804909": {
            "length": 16,
            "waveforms": {
                "single": "-4898728467183804909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3472690556399664214": {
            "length": 16,
            "waveforms": {
                "single": "-3472690556399664214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "334481349842959437": {
            "length": 16,
            "waveforms": {
                "single": "334481349842959437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1274930868396497351": {
            "length": 16,
            "waveforms": {
                "single": "-1274930868396497351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8025653920143159699": {
            "length": 16,
            "waveforms": {
                "single": "-8025653920143159699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2753735097044841548": {
            "length": 16,
            "waveforms": {
                "single": "2753735097044841548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7276052867134844864": {
            "length": 16,
            "waveforms": {
                "single": "7276052867134844864",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4951494785048008411": {
            "length": 16,
            "waveforms": {
                "single": "4951494785048008411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-668496592802707719": {
            "length": 20,
            "waveforms": {
                "single": "-668496592802707719",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3020862261565001939": {
            "length": 20,
            "waveforms": {
                "single": "-3020862261565001939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3739721701544775543": {
            "length": 20,
            "waveforms": {
                "single": "-3739721701544775543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5221459956546203204": {
            "length": 20,
            "waveforms": {
                "single": "-5221459956546203204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5842785724432896748": {
            "length": 24,
            "waveforms": {
                "single": "-5842785724432896748",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4410107243464929270": {
            "length": 24,
            "waveforms": {
                "single": "4410107243464929270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4631601302663644518": {
            "length": 24,
            "waveforms": {
                "single": "4631601302663644518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8311099245668239042": {
            "length": 24,
            "waveforms": {
                "single": "8311099245668239042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6829360990666811381": {
            "length": 28,
            "waveforms": {
                "single": "6829360990666811381",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6605667325214691137": {
            "length": 28,
            "waveforms": {
                "single": "-6605667325214691137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6384173266015975889": {
            "length": 28,
            "waveforms": {
                "single": "-6384173266015975889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6162679206817260641": {
            "length": 28,
            "waveforms": {
                "single": "-6162679206817260641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4186413578012809026": {
            "length": 32,
            "waveforms": {
                "single": "-4186413578012809026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3964919518814093778": {
            "length": 32,
            "waveforms": {
                "single": "-3964919518814093778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1046796239013955320": {
            "length": 32,
            "waveforms": {
                "single": "1046796239013955320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1268290298212670568": {
            "length": 32,
            "waveforms": {
                "single": "1268290298212670568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4184909426195611035": {
            "length": 36,
            "waveforms": {
                "single": "4184909426195611035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3466049986215837431": {
            "length": 36,
            "waveforms": {
                "single": "3466049986215837431",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1113684317453543211": {
            "length": 36,
            "waveforms": {
                "single": "1113684317453543211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6051587897592113080": {
            "length": 36,
            "waveforms": {
                "single": "6051587897592113080",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5885303733417719542": {
            "length": 40,
            "waveforms": {
                "single": "5885303733417719542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2308547372394006056": {
            "length": 40,
            "waveforms": {
                "single": "-2308547372394006056",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4072484261809627063": {
            "length": 40,
            "waveforms": {
                "single": "4072484261809627063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1720118593047332843": {
            "length": 40,
            "waveforms": {
                "single": "1720118593047332843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "110706374807876055": {
            "length": 44,
            "waveforms": {
                "single": "110706374807876055",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3917878281050499706": {
            "length": 44,
            "waveforms": {
                "single": "3917878281050499706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5343916191834640401": {
            "length": 44,
            "waveforms": {
                "single": "5343916191834640401",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9151088098077264052": {
            "length": 44,
            "waveforms": {
                "single": "9151088098077264052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7541675879837807264": {
            "length": 48,
            "waveforms": {
                "single": "7541675879837807264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7097896287629120701": {
            "length": 48,
            "waveforms": {
                "single": "-7097896287629120701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6876402228430405453": {
            "length": 48,
            "waveforms": {
                "single": "-6876402228430405453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2533670912382011773": {
            "length": 48,
            "waveforms": {
                "single": "2533670912382011773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2755164971580727021": {
            "length": 52,
            "waveforms": {
                "single": "2755164971580727021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5574250427470587428": {
            "length": 52,
            "waveforms": {
                "single": "5574250427470587428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "554567276599525756": {
            "length": 52,
            "waveforms": {
                "single": "554567276599525756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7639283829212199842": {
            "length": 52,
            "waveforms": {
                "single": "-7639283829212199842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8260609597098893386": {
            "length": 56,
            "waveforms": {
                "single": "-8260609597098893386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8704396221609230569": {
            "length": 56,
            "waveforms": {
                "single": "8704396221609230569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5220030082010317731": {
            "length": 56,
            "waveforms": {
                "single": "-5220030082010317731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5841355849897011275": {
            "length": 56,
            "waveforms": {
                "single": "-5841355849897011275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "13179735016446615": {
            "length": 60,
            "waveforms": {
                "single": "13179735016446615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7757118623180850379": {
            "length": 60,
            "waveforms": {
                "single": "7757118623180850379",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2089884287871674590": {
            "length": 60,
            "waveforms": {
                "single": "-2089884287871674590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2432433482218328726": {
            "length": 60,
            "waveforms": {
                "single": "2432433482218328726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5234921574303221643": {
            "length": 64,
            "waveforms": {
                "single": "-5234921574303221643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4630193170221495589": {
            "length": 64,
            "waveforms": {
                "single": "4630193170221495589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3037161886300054780": {
            "length": 64,
            "waveforms": {
                "single": "-3037161886300054780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8583341086461291681": {
            "length": 64,
            "waveforms": {
                "single": "-8583341086461291681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3963489644278208305": {
            "length": 68,
            "waveforms": {
                "single": "-3963489644278208305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1859550052235727563": {
            "length": 68,
            "waveforms": {
                "single": "-1859550052235727563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6164087339259409570": {
            "length": 68,
            "waveforms": {
                "single": "-6164087339259409570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2041441949967582209": {
            "length": 68,
            "waveforms": {
                "single": "2041441949967582209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3578549427883133921": {
            "length": 72,
            "waveforms": {
                "single": "-3578549427883133921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1985741605750295243": {
            "length": 72,
            "waveforms": {
                "single": "1985741605750295243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5779147122864335186": {
            "length": 72,
            "waveforms": {
                "single": "-5779147122864335186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8131512791626629406": {
            "length": 72,
            "waveforms": {
                "single": "-8131512791626629406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8752838559513322950": {
            "length": 76,
            "waveforms": {
                "single": "-8752838559513322950",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1500054408384503068": {
            "length": 76,
            "waveforms": {
                "single": "1500054408384503068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-824503673702333385": {
            "length": 76,
            "waveforms": {
                "single": "-824503673702333385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6271673824348679399": {
            "length": 76,
            "waveforms": {
                "single": "6271673824348679399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3919308155586385179": {
            "length": 80,
            "waveforms": {
                "single": "3919308155586385179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1100374995284676493": {
            "length": 80,
            "waveforms": {
                "single": "-1100374995284676493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1718710460605183914": {
            "length": 80,
            "waveforms": {
                "single": "1718710460605183914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6698661223986393627": {
            "length": 40,
            "waveforms": {
                "I": "6698661223986393627_i",
                "Q": "6698661223986393627_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5937570594762831758_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5937570594762831758_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4507736934933058392": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "279758784901407420_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "279758784901407420_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6271652082254942855": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-606744932729748620": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8469411770258109718": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7321589953081240945": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7543084012279956193": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-221804716334674236": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5342486317298754928": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4898728467183804909": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3472690556399664214": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "334481349842959437": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1274930868396497351": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8025653920143159699": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2753735097044841548": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7276052867134844864": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4951494785048008411": {
            "sample": 0.25,
            "type": "constant",
        },
        "-668496592802707719": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3020862261565001939": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3739721701544775543": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5221459956546203204": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5842785724432896748": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4410107243464929270": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4631601302663644518": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8311099245668239042": {
            "sample": 0.25,
            "type": "constant",
        },
        "6829360990666811381": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6605667325214691137": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6384173266015975889": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6162679206817260641": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4186413578012809026": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3964919518814093778": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1046796239013955320": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1268290298212670568": {
            "sample": 0.25,
            "type": "constant",
        },
        "4184909426195611035": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3466049986215837431": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1113684317453543211": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6051587897592113080": {
            "sample": 0.25,
            "type": "constant",
        },
        "5885303733417719542": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2308547372394006056": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4072484261809627063": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1720118593047332843": {
            "sample": 0.25,
            "type": "constant",
        },
        "110706374807876055": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3917878281050499706": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5343916191834640401": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9151088098077264052": {
            "sample": 0.25,
            "type": "constant",
        },
        "7541675879837807264": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7097896287629120701": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6876402228430405453": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2533670912382011773": {
            "sample": 0.25,
            "type": "constant",
        },
        "2755164971580727021": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5574250427470587428": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "554567276599525756": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7639283829212199842": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8260609597098893386": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8704396221609230569": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5220030082010317731": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5841355849897011275": {
            "sample": 0.25,
            "type": "constant",
        },
        "13179735016446615": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7757118623180850379": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2089884287871674590": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2432433482218328726": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5234921574303221643": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4630193170221495589": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3037161886300054780": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8583341086461291681": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3963489644278208305": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1859550052235727563": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6164087339259409570": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2041441949967582209": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3578549427883133921": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1985741605750295243": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5779147122864335186": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8131512791626629406": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8752838559513322950": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1500054408384503068": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-824503673702333385": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6271673824348679399": {
            "sample": 0.25,
            "type": "constant",
        },
        "3919308155586385179": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1100374995284676493": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1718710460605183914": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6698661223986393627_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6698661223986393627_q": {
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
        "B4/acquisition_mixer_5a9": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_719": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

