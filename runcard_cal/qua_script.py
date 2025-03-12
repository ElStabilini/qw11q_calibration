
# Single QUA script generated at 2025-03-12 16:25:29.705873
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
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-7390657512199220417", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("5436095183659615069", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-2157447695172456071", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("7633854871662781932", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("883131819916119584", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("2309169730700260279", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("4784123822119429356", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("2459565740032592903", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-3160425637818123227", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-5512791306580417447", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-6231650746560191051", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-7713389001561618712", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-6287351090777478017", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("1918178198449513762", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("2139672257648229010", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-5625216470966401419", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("4337431945651395873", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-8254776543144697853", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-2851884526843234130", "B4/drive")
        wait(11, "B4/flux")
        play("-8876102311031391397", "B4/flux")
        wait(46, "B4/drive")
        play("-2090793897619672261", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-3666682820856938268", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.42477383735093954)-(v3*0.9052995013265818))>-0.0005556861492047521)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-3666682820856938268_B4|acquisition_shots")


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
                "-7390657512199220417": "-7390657512199220417",
                "5436095183659615069": "5436095183659615069",
                "-2157447695172456071": "-2157447695172456071",
                "7633854871662781932": "7633854871662781932",
                "883131819916119584": "883131819916119584",
                "2309169730700260279": "2309169730700260279",
                "4784123822119429356": "4784123822119429356",
                "2459565740032592903": "2459565740032592903",
                "-3160425637818123227": "-3160425637818123227",
                "-5512791306580417447": "-5512791306580417447",
                "-6231650746560191051": "-6231650746560191051",
                "-7713389001561618712": "-7713389001561618712",
                "-6287351090777478017": "-6287351090777478017",
                "1918178198449513762": "1918178198449513762",
                "2139672257648229010": "2139672257648229010",
                "-5625216470966401419": "-5625216470966401419",
                "4337431945651395873": "4337431945651395873",
                "-8254776543144697853": "-8254776543144697853",
                "-8876102311031391397": "-8876102311031391397",
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
                "-2851884526843234130": "-2851884526843234130",
                "-2090793897619672261": "-2090793897619672261",
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
                "-3666682820856938268": "-3666682820856938268_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-2851884526843234130": {
            "length": 40,
            "waveforms": {
                "I": "-2851884526843234130_i",
                "Q": "-2851884526843234130_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "308744238116320430": {
            "length": 16,
            "waveforms": {
                "single": "308744238116320430",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3666682820856938268_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1085660798339526900_i",
                "Q": "1085660798339526900_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-7456144490498309999": {
            "length": 16,
            "waveforms": {
                "single": "-7456144490498309999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7234650431299594751": {
            "length": 16,
            "waveforms": {
                "single": "-7234650431299594751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8016908146562253853": {
            "length": 16,
            "waveforms": {
                "single": "8016908146562253853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1016205593516364560": {
            "length": 16,
            "waveforms": {
                "single": "1016205593516364560",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7961207802344966887": {
            "length": 16,
            "waveforms": {
                "single": "7961207802344966887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "196319073730336458": {
            "length": 16,
            "waveforms": {
                "single": "196319073730336458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2156046595031957762": {
            "length": 16,
            "waveforms": {
                "single": "-2156046595031957762",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8623342422156043485": {
            "length": 16,
            "waveforms": {
                "single": "8623342422156043485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8346148018740041271": {
            "length": 16,
            "waveforms": {
                "single": "8346148018740041271",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5993782349977747051": {
            "length": 16,
            "waveforms": {
                "single": "5993782349977747051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5274922909997973447": {
            "length": 16,
            "waveforms": {
                "single": "5274922909997973447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5496416969196688695": {
            "length": 16,
            "waveforms": {
                "single": "5496416969196688695",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8829164124944497007": {
            "length": 16,
            "waveforms": {
                "single": "-8829164124944497007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7694176657199855558": {
            "length": 16,
            "waveforms": {
                "single": "7694176657199855558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4800498159503158108": {
            "length": 16,
            "waveforms": {
                "single": "-4800498159503158108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8167029505133420409": {
            "length": 20,
            "waveforms": {
                "single": "-8167029505133420409",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2602738471499991245": {
            "length": 20,
            "waveforms": {
                "single": "-2602738471499991245",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8079116873594929942": {
            "length": 20,
            "waveforms": {
                "single": "8079116873594929942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8300610932793645190": {
            "length": 20,
            "waveforms": {
                "single": "8300610932793645190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7152789115616776417": {
            "length": 24,
            "waveforms": {
                "single": "7152789115616776417",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4828231033529939964": {
            "length": 24,
            "waveforms": {
                "single": "4828231033529939964",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5049725092728655212": {
            "length": 24,
            "waveforms": {
                "single": "5049725092728655212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1683193747098392911": {
            "length": 24,
            "waveforms": {
                "single": "1683193747098392911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1904687806297108159": {
            "length": 28,
            "waveforms": {
                "single": "1904687806297108159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-946366325079903523": {
            "length": 28,
            "waveforms": {
                "single": "-946366325079903523",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5434665309123729596": {
            "length": 28,
            "waveforms": {
                "single": "5434665309123729596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1443731705860961879": {
            "length": 28,
            "waveforms": {
                "single": "-1443731705860961879",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9111086762382512248": {
            "length": 32,
            "waveforms": {
                "single": "-9111086762382512248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6983291642564745148": {
            "length": 32,
            "waveforms": {
                "single": "6983291642564745148",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6706097239148742934": {
            "length": 32,
            "waveforms": {
                "single": "6706097239148742934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961257817372807435": {
            "length": 32,
            "waveforms": {
                "single": "-961257817372807435",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-837297430267172247": {
            "length": 36,
            "waveforms": {
                "single": "-837297430267172247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4032482926114875259": {
            "length": 36,
            "waveforms": {
                "single": "-4032482926114875259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5514221181116302920": {
            "length": 36,
            "waveforms": {
                "single": "-5514221181116302920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4088183270332162225": {
            "length": 36,
            "waveforms": {
                "single": "-4088183270332162225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4117346018894829554": {
            "length": 40,
            "waveforms": {
                "single": "4117346018894829554",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7233220556763709278": {
            "length": 40,
            "waveforms": {
                "single": "-7233220556763709278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1916748323913628289": {
            "length": 40,
            "waveforms": {
                "single": "1916748323913628289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3703243053937087841": {
            "length": 40,
            "waveforms": {
                "single": "-3703243053937087841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1228288962517918764": {
            "length": 44,
            "waveforms": {
                "single": "-1228288962517918764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6676934490586075605": {
            "length": 44,
            "waveforms": {
                "single": "-6676934490586075605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1283989306735205730": {
            "length": 44,
            "waveforms": {
                "single": "-1283989306735205730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4479174802582908742": {
            "length": 44,
            "waveforms": {
                "single": "-4479174802582908742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4355214415477273554": {
            "length": 48,
            "waveforms": {
                "single": "-4355214415477273554",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6424174601710727693": {
            "length": 48,
            "waveforms": {
                "single": "6424174601710727693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6146980198294725479": {
            "length": 48,
            "waveforms": {
                "single": "6146980198294725479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3794614529532431259": {
            "length": 48,
            "waveforms": {
                "single": "3794614529532431259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3872740526989119110": {
            "length": 52,
            "waveforms": {
                "single": "-3872740526989119110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7695606531735741031": {
            "length": 52,
            "waveforms": {
                "single": "7695606531735741031",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1674980838985952247": {
            "length": 52,
            "waveforms": {
                "single": "-1674980838985952247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7221160039147189148": {
            "length": 52,
            "waveforms": {
                "single": "-7221160039147189148",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6999665979948473900": {
            "length": 56,
            "waveforms": {
                "single": "-6999665979948473900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3779723037239527347": {
            "length": 56,
            "waveforms": {
                "single": "3779723037239527347",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8302040807329530663": {
            "length": 56,
            "waveforms": {
                "single": "8302040807329530663",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5977482725242694210": {
            "length": 56,
            "waveforms": {
                "single": "5977482725242694210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4829660908065825437": {
            "length": 60,
            "waveforms": {
                "single": "4829660908065825437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5051154967264540685": {
            "length": 60,
            "waveforms": {
                "single": "5051154967264540685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2713733761350089744": {
            "length": 60,
            "waveforms": {
                "single": "-2713733761350089744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2850557272283339420": {
            "length": 60,
            "waveforms": {
                "single": "2850557272283339420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7390657512199220417": {
            "length": 64,
            "waveforms": {
                "single": "-7390657512199220417",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5436095183659615069": {
            "length": 64,
            "waveforms": {
                "single": "5436095183659615069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2157447695172456071": {
            "length": 64,
            "waveforms": {
                "single": "-2157447695172456071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7633854871662781932": {
            "length": 64,
            "waveforms": {
                "single": "7633854871662781932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "883131819916119584": {
            "length": 68,
            "waveforms": {
                "single": "883131819916119584",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2309169730700260279": {
            "length": 68,
            "waveforms": {
                "single": "2309169730700260279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4784123822119429356": {
            "length": 68,
            "waveforms": {
                "single": "4784123822119429356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2459565740032592903": {
            "length": 68,
            "waveforms": {
                "single": "2459565740032592903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3160425637818123227": {
            "length": 72,
            "waveforms": {
                "single": "-3160425637818123227",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5512791306580417447": {
            "length": 72,
            "waveforms": {
                "single": "-5512791306580417447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6231650746560191051": {
            "length": 72,
            "waveforms": {
                "single": "-6231650746560191051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7713389001561618712": {
            "length": 72,
            "waveforms": {
                "single": "-7713389001561618712",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6287351090777478017": {
            "length": 76,
            "waveforms": {
                "single": "-6287351090777478017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1918178198449513762": {
            "length": 76,
            "waveforms": {
                "single": "1918178198449513762",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2139672257648229010": {
            "length": 76,
            "waveforms": {
                "single": "2139672257648229010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5625216470966401419": {
            "length": 76,
            "waveforms": {
                "single": "-5625216470966401419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4337431945651395873": {
            "length": 80,
            "waveforms": {
                "single": "4337431945651395873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8254776543144697853": {
            "length": 80,
            "waveforms": {
                "single": "-8254776543144697853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8876102311031391397": {
            "length": 80,
            "waveforms": {
                "single": "-8876102311031391397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2090793897619672261": {
            "length": 40,
            "waveforms": {
                "I": "-2090793897619672261_i",
                "Q": "-2090793897619672261_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2851884526843234130_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-2851884526843234130_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "308744238116320430": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "1085660798339526900_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1085660798339526900_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7456144490498309999": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-7234650431299594751": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "8016908146562253853": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1016205593516364560": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "7961207802344966887": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "196319073730336458": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-2156046595031957762": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "8623342422156043485": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "8346148018740041271": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "5993782349977747051": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5274922909997973447": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "5496416969196688695": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8829164124944497007": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7694176657199855558": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-4800498159503158108": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8167029505133420409": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2602738471499991245": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8079116873594929942": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "8300610932793645190": {
            "sample": 0.25,
            "type": "constant",
        },
        "7152789115616776417": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4828231033529939964": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5049725092728655212": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "1683193747098392911": {
            "sample": 0.25,
            "type": "constant",
        },
        "1904687806297108159": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-946366325079903523": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5434665309123729596": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-1443731705860961879": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9111086762382512248": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6983291642564745148": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6706097239148742934": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-961257817372807435": {
            "sample": 0.25,
            "type": "constant",
        },
        "-837297430267172247": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4032482926114875259": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5514221181116302920": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-4088183270332162225": {
            "sample": 0.25,
            "type": "constant",
        },
        "4117346018894829554": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7233220556763709278": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1916748323913628289": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-3703243053937087841": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1228288962517918764": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6676934490586075605": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1283989306735205730": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-4479174802582908742": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4355214415477273554": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6424174601710727693": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6146980198294725479": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "3794614529532431259": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3872740526989119110": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7695606531735741031": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1674980838985952247": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-7221160039147189148": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6999665979948473900": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3779723037239527347": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8302040807329530663": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "5977482725242694210": {
            "sample": 0.25,
            "type": "constant",
        },
        "4829660908065825437": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5051154967264540685": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2713733761350089744": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "2850557272283339420": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7390657512199220417": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5436095183659615069": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2157447695172456071": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "7633854871662781932": {
            "sample": 0.25,
            "type": "constant",
        },
        "883131819916119584": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2309169730700260279": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4784123822119429356": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "2459565740032592903": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3160425637818123227": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5512791306580417447": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6231650746560191051": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-7713389001561618712": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6287351090777478017": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1918178198449513762": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2139672257648229010": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-5625216470966401419": {
            "sample": 0.25,
            "type": "constant",
        },
        "4337431945651395873": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8254776543144697853": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8876102311031391397": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-2090793897619672261_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-2090793897619672261_q": {
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
                "-7390657512199220417": "-7390657512199220417",
                "5436095183659615069": "5436095183659615069",
                "-2157447695172456071": "-2157447695172456071",
                "7633854871662781932": "7633854871662781932",
                "883131819916119584": "883131819916119584",
                "2309169730700260279": "2309169730700260279",
                "4784123822119429356": "4784123822119429356",
                "2459565740032592903": "2459565740032592903",
                "-3160425637818123227": "-3160425637818123227",
                "-5512791306580417447": "-5512791306580417447",
                "-6231650746560191051": "-6231650746560191051",
                "-7713389001561618712": "-7713389001561618712",
                "-6287351090777478017": "-6287351090777478017",
                "1918178198449513762": "1918178198449513762",
                "2139672257648229010": "2139672257648229010",
                "-5625216470966401419": "-5625216470966401419",
                "4337431945651395873": "4337431945651395873",
                "-8254776543144697853": "-8254776543144697853",
                "-8876102311031391397": "-8876102311031391397",
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
                "-2851884526843234130": "-2851884526843234130",
                "-2090793897619672261": "-2090793897619672261",
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
                "mixer": "B4/drive_mixer_e91",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-3666682820856938268": "-3666682820856938268_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e4d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "-2851884526843234130": {
            "length": 40,
            "waveforms": {
                "I": "-2851884526843234130_i",
                "Q": "-2851884526843234130_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "308744238116320430": {
            "length": 16,
            "waveforms": {
                "single": "308744238116320430",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3666682820856938268_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1085660798339526900_i",
                "Q": "1085660798339526900_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-7456144490498309999": {
            "length": 16,
            "waveforms": {
                "single": "-7456144490498309999",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7234650431299594751": {
            "length": 16,
            "waveforms": {
                "single": "-7234650431299594751",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8016908146562253853": {
            "length": 16,
            "waveforms": {
                "single": "8016908146562253853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1016205593516364560": {
            "length": 16,
            "waveforms": {
                "single": "1016205593516364560",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7961207802344966887": {
            "length": 16,
            "waveforms": {
                "single": "7961207802344966887",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "196319073730336458": {
            "length": 16,
            "waveforms": {
                "single": "196319073730336458",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2156046595031957762": {
            "length": 16,
            "waveforms": {
                "single": "-2156046595031957762",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8623342422156043485": {
            "length": 16,
            "waveforms": {
                "single": "8623342422156043485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8346148018740041271": {
            "length": 16,
            "waveforms": {
                "single": "8346148018740041271",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5993782349977747051": {
            "length": 16,
            "waveforms": {
                "single": "5993782349977747051",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5274922909997973447": {
            "length": 16,
            "waveforms": {
                "single": "5274922909997973447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5496416969196688695": {
            "length": 16,
            "waveforms": {
                "single": "5496416969196688695",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8829164124944497007": {
            "length": 16,
            "waveforms": {
                "single": "-8829164124944497007",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7694176657199855558": {
            "length": 16,
            "waveforms": {
                "single": "7694176657199855558",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4800498159503158108": {
            "length": 16,
            "waveforms": {
                "single": "-4800498159503158108",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8167029505133420409": {
            "length": 20,
            "waveforms": {
                "single": "-8167029505133420409",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2602738471499991245": {
            "length": 20,
            "waveforms": {
                "single": "-2602738471499991245",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8079116873594929942": {
            "length": 20,
            "waveforms": {
                "single": "8079116873594929942",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8300610932793645190": {
            "length": 20,
            "waveforms": {
                "single": "8300610932793645190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7152789115616776417": {
            "length": 24,
            "waveforms": {
                "single": "7152789115616776417",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4828231033529939964": {
            "length": 24,
            "waveforms": {
                "single": "4828231033529939964",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5049725092728655212": {
            "length": 24,
            "waveforms": {
                "single": "5049725092728655212",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1683193747098392911": {
            "length": 24,
            "waveforms": {
                "single": "1683193747098392911",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1904687806297108159": {
            "length": 28,
            "waveforms": {
                "single": "1904687806297108159",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-946366325079903523": {
            "length": 28,
            "waveforms": {
                "single": "-946366325079903523",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5434665309123729596": {
            "length": 28,
            "waveforms": {
                "single": "5434665309123729596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1443731705860961879": {
            "length": 28,
            "waveforms": {
                "single": "-1443731705860961879",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9111086762382512248": {
            "length": 32,
            "waveforms": {
                "single": "-9111086762382512248",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6983291642564745148": {
            "length": 32,
            "waveforms": {
                "single": "6983291642564745148",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6706097239148742934": {
            "length": 32,
            "waveforms": {
                "single": "6706097239148742934",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-961257817372807435": {
            "length": 32,
            "waveforms": {
                "single": "-961257817372807435",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-837297430267172247": {
            "length": 36,
            "waveforms": {
                "single": "-837297430267172247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4032482926114875259": {
            "length": 36,
            "waveforms": {
                "single": "-4032482926114875259",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5514221181116302920": {
            "length": 36,
            "waveforms": {
                "single": "-5514221181116302920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4088183270332162225": {
            "length": 36,
            "waveforms": {
                "single": "-4088183270332162225",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4117346018894829554": {
            "length": 40,
            "waveforms": {
                "single": "4117346018894829554",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7233220556763709278": {
            "length": 40,
            "waveforms": {
                "single": "-7233220556763709278",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1916748323913628289": {
            "length": 40,
            "waveforms": {
                "single": "1916748323913628289",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3703243053937087841": {
            "length": 40,
            "waveforms": {
                "single": "-3703243053937087841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1228288962517918764": {
            "length": 44,
            "waveforms": {
                "single": "-1228288962517918764",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6676934490586075605": {
            "length": 44,
            "waveforms": {
                "single": "-6676934490586075605",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1283989306735205730": {
            "length": 44,
            "waveforms": {
                "single": "-1283989306735205730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4479174802582908742": {
            "length": 44,
            "waveforms": {
                "single": "-4479174802582908742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4355214415477273554": {
            "length": 48,
            "waveforms": {
                "single": "-4355214415477273554",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6424174601710727693": {
            "length": 48,
            "waveforms": {
                "single": "6424174601710727693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6146980198294725479": {
            "length": 48,
            "waveforms": {
                "single": "6146980198294725479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3794614529532431259": {
            "length": 48,
            "waveforms": {
                "single": "3794614529532431259",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3872740526989119110": {
            "length": 52,
            "waveforms": {
                "single": "-3872740526989119110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7695606531735741031": {
            "length": 52,
            "waveforms": {
                "single": "7695606531735741031",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1674980838985952247": {
            "length": 52,
            "waveforms": {
                "single": "-1674980838985952247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7221160039147189148": {
            "length": 52,
            "waveforms": {
                "single": "-7221160039147189148",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6999665979948473900": {
            "length": 56,
            "waveforms": {
                "single": "-6999665979948473900",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3779723037239527347": {
            "length": 56,
            "waveforms": {
                "single": "3779723037239527347",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8302040807329530663": {
            "length": 56,
            "waveforms": {
                "single": "8302040807329530663",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5977482725242694210": {
            "length": 56,
            "waveforms": {
                "single": "5977482725242694210",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4829660908065825437": {
            "length": 60,
            "waveforms": {
                "single": "4829660908065825437",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5051154967264540685": {
            "length": 60,
            "waveforms": {
                "single": "5051154967264540685",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2713733761350089744": {
            "length": 60,
            "waveforms": {
                "single": "-2713733761350089744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2850557272283339420": {
            "length": 60,
            "waveforms": {
                "single": "2850557272283339420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7390657512199220417": {
            "length": 64,
            "waveforms": {
                "single": "-7390657512199220417",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5436095183659615069": {
            "length": 64,
            "waveforms": {
                "single": "5436095183659615069",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2157447695172456071": {
            "length": 64,
            "waveforms": {
                "single": "-2157447695172456071",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7633854871662781932": {
            "length": 64,
            "waveforms": {
                "single": "7633854871662781932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "883131819916119584": {
            "length": 68,
            "waveforms": {
                "single": "883131819916119584",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2309169730700260279": {
            "length": 68,
            "waveforms": {
                "single": "2309169730700260279",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4784123822119429356": {
            "length": 68,
            "waveforms": {
                "single": "4784123822119429356",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2459565740032592903": {
            "length": 68,
            "waveforms": {
                "single": "2459565740032592903",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3160425637818123227": {
            "length": 72,
            "waveforms": {
                "single": "-3160425637818123227",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5512791306580417447": {
            "length": 72,
            "waveforms": {
                "single": "-5512791306580417447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6231650746560191051": {
            "length": 72,
            "waveforms": {
                "single": "-6231650746560191051",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7713389001561618712": {
            "length": 72,
            "waveforms": {
                "single": "-7713389001561618712",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6287351090777478017": {
            "length": 76,
            "waveforms": {
                "single": "-6287351090777478017",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1918178198449513762": {
            "length": 76,
            "waveforms": {
                "single": "1918178198449513762",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2139672257648229010": {
            "length": 76,
            "waveforms": {
                "single": "2139672257648229010",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5625216470966401419": {
            "length": 76,
            "waveforms": {
                "single": "-5625216470966401419",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4337431945651395873": {
            "length": 80,
            "waveforms": {
                "single": "4337431945651395873",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8254776543144697853": {
            "length": 80,
            "waveforms": {
                "single": "-8254776543144697853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8876102311031391397": {
            "length": 80,
            "waveforms": {
                "single": "-8876102311031391397",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2090793897619672261": {
            "length": 40,
            "waveforms": {
                "I": "-2090793897619672261_i",
                "Q": "-2090793897619672261_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-2851884526843234130_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2851884526843234130_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "308744238116320430": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1085660798339526900_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "1085660798339526900_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7456144490498309999": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7234650431299594751": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8016908146562253853": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1016205593516364560": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7961207802344966887": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "196319073730336458": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2156046595031957762": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8623342422156043485": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8346148018740041271": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5993782349977747051": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5274922909997973447": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5496416969196688695": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8829164124944497007": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7694176657199855558": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4800498159503158108": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8167029505133420409": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2602738471499991245": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8079116873594929942": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8300610932793645190": {
            "type": "constant",
            "sample": 0.25,
        },
        "7152789115616776417": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4828231033529939964": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5049725092728655212": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1683193747098392911": {
            "type": "constant",
            "sample": 0.25,
        },
        "1904687806297108159": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-946366325079903523": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5434665309123729596": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1443731705860961879": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9111086762382512248": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6983291642564745148": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6706097239148742934": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-961257817372807435": {
            "type": "constant",
            "sample": 0.25,
        },
        "-837297430267172247": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4032482926114875259": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5514221181116302920": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4088183270332162225": {
            "type": "constant",
            "sample": 0.25,
        },
        "4117346018894829554": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7233220556763709278": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1916748323913628289": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3703243053937087841": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1228288962517918764": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6676934490586075605": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1283989306735205730": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4479174802582908742": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4355214415477273554": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6424174601710727693": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6146980198294725479": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3794614529532431259": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3872740526989119110": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7695606531735741031": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1674980838985952247": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7221160039147189148": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6999665979948473900": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3779723037239527347": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8302040807329530663": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5977482725242694210": {
            "type": "constant",
            "sample": 0.25,
        },
        "4829660908065825437": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5051154967264540685": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2713733761350089744": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2850557272283339420": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7390657512199220417": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5436095183659615069": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2157447695172456071": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7633854871662781932": {
            "type": "constant",
            "sample": 0.25,
        },
        "883131819916119584": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2309169730700260279": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4784123822119429356": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2459565740032592903": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3160425637818123227": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5512791306580417447": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6231650746560191051": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7713389001561618712": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6287351090777478017": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1918178198449513762": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2139672257648229010": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5625216470966401419": {
            "type": "constant",
            "sample": 0.25,
        },
        "4337431945651395873": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8254776543144697853": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8876102311031391397": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2090793897619672261_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2090793897619672261_q": {
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
        "B4/drive_mixer_e91": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e4d": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

