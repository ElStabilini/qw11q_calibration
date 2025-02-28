
# Single QUA script generated at 2025-02-28 10:25:56.595605
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
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("6832890114326973325", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-931998614287657104", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-6380644142355813945", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("4853786478544487308", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-4182884454352647082", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-3961390395153931834", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("6720464949940989353", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-1763630707150764971", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("4090904877762692919", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-3576450178758857450", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("3691073169074714623", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("6510158624964575030", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-1157196431556975339", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-6703375631718212240", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("4076013385469789007", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("-4505615943715045377", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("6273773073472955870", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("6495267132671671118", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        play("-489531609513980131", "B4/drive")
        wait(11, "B4/flux")
        play("5347445315494802345", "B4/flux")
        wait(46, "B4/drive")
        play("271559019709581738", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-8313996170767310540", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-8313996170767310540_B4|acquisition_shots")


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
                "6832890114326973325": "6832890114326973325",
                "-931998614287657104": "-931998614287657104",
                "-6380644142355813945": "-6380644142355813945",
                "4853786478544487308": "4853786478544487308",
                "-4182884454352647082": "-4182884454352647082",
                "-3961390395153931834": "-3961390395153931834",
                "6720464949940989353": "6720464949940989353",
                "-1763630707150764971": "-1763630707150764971",
                "4090904877762692919": "4090904877762692919",
                "-3576450178758857450": "-3576450178758857450",
                "3691073169074714623": "3691073169074714623",
                "6510158624964575030": "6510158624964575030",
                "-1157196431556975339": "-1157196431556975339",
                "-6703375631718212240": "-6703375631718212240",
                "4076013385469789007": "4076013385469789007",
                "-4505615943715045377": "-4505615943715045377",
                "6273773073472955870": "6273773073472955870",
                "6495267132671671118": "6495267132671671118",
                "5347445315494802345": "5347445315494802345",
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
                "-489531609513980131": "-489531609513980131",
                "271559019709581738": "271559019709581738",
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
                "-8313996170767310540": "-8313996170767310540_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-489531609513980131": {
            "length": 40,
            "waveforms": {
                "I": "-489531609513980131_i",
                "Q": "-489531609513980131_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2245085365937880427": {
            "length": 16,
            "waveforms": {
                "single": "2245085365937880427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8313996170767310540_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8378712858913607894_i",
                "Q": "-8378712858913607894_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-107280302824413793": {
            "length": 16,
            "waveforms": {
                "single": "-107280302824413793",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7107982855870303086": {
            "length": 16,
            "waveforms": {
                "single": "-7107982855870303086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8143575721991545518": {
            "length": 16,
            "waveforms": {
                "single": "8143575721991545518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4910223167867136223": {
            "length": 16,
            "waveforms": {
                "single": "-4910223167867136223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7323689202205517416": {
            "length": 16,
            "waveforms": {
                "single": "7323689202205517416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7545183261404232664": {
            "length": 16,
            "waveforms": {
                "single": "7545183261404232664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2029379019602666097": {
            "length": 16,
            "waveforms": {
                "single": "-2029379019602666097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8703801124302152089": {
            "length": 16,
            "waveforms": {
                "single": "-8703801124302152089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "168380668400500766": {
            "length": 16,
            "waveforms": {
                "single": "168380668400500766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3470591307275387743": {
            "length": 16,
            "waveforms": {
                "single": "-3470591307275387743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2976656618031046287": {
            "length": 16,
            "waveforms": {
                "single": "-2976656618031046287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1272831619272220880": {
            "length": 16,
            "waveforms": {
                "single": "-1272831619272220880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1051337560073505632": {
            "length": 16,
            "waveforms": {
                "single": "-1051337560073505632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7820844232629147223": {
            "length": 16,
            "waveforms": {
                "single": "7820844232629147223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "153489176107596854": {
            "length": 16,
            "waveforms": {
                "single": "153489176107596854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4675806946197600170": {
            "length": 20,
            "waveforms": {
                "single": "4675806946197600170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-666397343678431248": {
            "length": 20,
            "waveforms": {
                "single": "-666397343678431248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-444903284479716000": {
            "length": 20,
            "waveforms": {
                "single": "-444903284479716000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8427278508222936855": {
            "length": 20,
            "waveforms": {
                "single": "8427278508222936855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5232093012375233843": {
            "length": 24,
            "waveforms": {
                "single": "5232093012375233843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "605034586346582090": {
            "length": 24,
            "waveforms": {
                "single": "605034586346582090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6986066220550215209": {
            "length": 24,
            "waveforms": {
                "single": "6986066220550215209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1809861322527684576": {
            "length": 24,
            "waveforms": {
                "single": "1809861322527684576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2031355381726399824": {
            "length": 28,
            "waveforms": {
                "single": "2031355381726399824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6831460239791087852": {
            "length": 28,
            "waveforms": {
                "single": "6831460239791087852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8257498150575228547": {
            "length": 28,
            "waveforms": {
                "single": "8257498150575228547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6382074016891699418": {
            "length": 28,
            "waveforms": {
                "single": "-6382074016891699418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8984419186953220583": {
            "length": 32,
            "waveforms": {
                "single": "-8984419186953220583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4184314328888532555": {
            "length": 32,
            "waveforms": {
                "single": "-4184314328888532555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1102189616770211897": {
            "length": 32,
            "waveforms": {
                "single": "1102189616770211897",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6290072698208008711": {
            "length": 32,
            "waveforms": {
                "single": "6290072698208008711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5668746930321315167": {
            "length": 36,
            "waveforms": {
                "single": "5668746930321315167",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7385051959537366574": {
            "length": 36,
            "waveforms": {
                "single": "-7385051959537366574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3468149235340113902": {
            "length": 36,
            "waveforms": {
                "single": "3468149235340113902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1708055662682416731": {
            "length": 36,
            "waveforms": {
                "single": "-1708055662682416731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4504207811272896448": {
            "length": 40,
            "waveforms": {
                "single": "-4504207811272896448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5887402982541996013": {
            "length": 40,
            "waveforms": {
                "single": "5887402982541996013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2306448123269729585": {
            "length": 40,
            "waveforms": {
                "single": "-2306448123269729585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8472940893918271662": {
            "length": 40,
            "waveforms": {
                "single": "8472940893918271662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1101621387088627099": {
            "length": 44,
            "waveforms": {
                "single": "-1101621387088627099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3148255752955750009": {
            "length": 44,
            "waveforms": {
                "single": "3148255752955750009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5124521381760201624": {
            "length": 44,
            "waveforms": {
                "single": "5124521381760201624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5346015440958916872": {
            "length": 44,
            "waveforms": {
                "single": "5346015440958916872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2321339615562633497": {
            "length": 48,
            "waveforms": {
                "single": "-2321339615562633497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6550842177140019358": {
            "length": 48,
            "waveforms": {
                "single": "6550842177140019358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7765269188160798983": {
            "length": 48,
            "waveforms": {
                "single": "7765269188160798983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5730955657353991256": {
            "length": 48,
            "waveforms": {
                "single": "5730955657353991256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5448265068521988287": {
            "length": 52,
            "waveforms": {
                "single": "-5448265068521988287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7822274107165032696": {
            "length": 52,
            "waveforms": {
                "single": "7822274107165032696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8150209404555873367": {
            "length": 52,
            "waveforms": {
                "single": "8150209404555873367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4955023908708170355": {
            "length": 52,
            "waveforms": {
                "single": "4955023908708170355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-664967469142545775": {
            "length": 56,
            "waveforms": {
                "single": "-664967469142545775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7415690520889208123": {
            "length": 56,
            "waveforms": {
                "single": "-7415690520889208123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9025102739128664911": {
            "length": 56,
            "waveforms": {
                "single": "-9025102739128664911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1754286278059336336": {
            "length": 56,
            "waveforms": {
                "single": "1754286278059336336",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3791892922101900565": {
            "length": 60,
            "waveforms": {
                "single": "-3791892922101900565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4413636367125091214": {
            "length": 60,
            "waveforms": {
                "single": "4413636367125091214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2798677085684159149": {
            "length": 60,
            "waveforms": {
                "single": "-2798677085684159149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1372639174900018454": {
            "length": 60,
            "waveforms": {
                "single": "-1372639174900018454",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6832890114326973325": {
            "length": 64,
            "waveforms": {
                "single": "6832890114326973325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-931998614287657104": {
            "length": 64,
            "waveforms": {
                "single": "-931998614287657104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6380644142355813945": {
            "length": 64,
            "waveforms": {
                "single": "-6380644142355813945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4853786478544487308": {
            "length": 64,
            "waveforms": {
                "single": "4853786478544487308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4182884454352647082": {
            "length": 68,
            "waveforms": {
                "single": "-4182884454352647082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3961390395153931834": {
            "length": 68,
            "waveforms": {
                "single": "-3961390395153931834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6720464949940989353": {
            "length": 68,
            "waveforms": {
                "single": "6720464949940989353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1763630707150764971": {
            "length": 68,
            "waveforms": {
                "single": "-1763630707150764971",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4090904877762692919": {
            "length": 72,
            "waveforms": {
                "single": "4090904877762692919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3576450178758857450": {
            "length": 72,
            "waveforms": {
                "single": "-3576450178758857450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3691073169074714623": {
            "length": 72,
            "waveforms": {
                "single": "3691073169074714623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6510158624964575030": {
            "length": 72,
            "waveforms": {
                "single": "6510158624964575030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1157196431556975339": {
            "length": 76,
            "waveforms": {
                "single": "-1157196431556975339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6703375631718212240": {
            "length": 76,
            "waveforms": {
                "single": "-6703375631718212240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4076013385469789007": {
            "length": 76,
            "waveforms": {
                "single": "4076013385469789007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4505615943715045377": {
            "length": 76,
            "waveforms": {
                "single": "-4505615943715045377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6273773073472955870": {
            "length": 80,
            "waveforms": {
                "single": "6273773073472955870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6495267132671671118": {
            "length": 80,
            "waveforms": {
                "single": "6495267132671671118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5347445315494802345": {
            "length": 80,
            "waveforms": {
                "single": "5347445315494802345",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "271559019709581738": {
            "length": 40,
            "waveforms": {
                "I": "271559019709581738_i",
                "Q": "271559019709581738_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-489531609513980131_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-489531609513980131_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "2245085365937880427": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-8378712858913607894_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-8378712858913607894_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-107280302824413793": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-7107982855870303086": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "8143575721991545518": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-4910223167867136223": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "7323689202205517416": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "7545183261404232664": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-2029379019602666097": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8703801124302152089": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "168380668400500766": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-3470591307275387743": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-2976656618031046287": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-1272831619272220880": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1051337560073505632": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7820844232629147223": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "153489176107596854": {
            "sample": 0.25,
            "type": "constant",
        },
        "4675806946197600170": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-666397343678431248": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-444903284479716000": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "8427278508222936855": {
            "sample": 0.25,
            "type": "constant",
        },
        "5232093012375233843": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "605034586346582090": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6986066220550215209": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "1809861322527684576": {
            "sample": 0.25,
            "type": "constant",
        },
        "2031355381726399824": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6831460239791087852": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8257498150575228547": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-6382074016891699418": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8984419186953220583": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4184314328888532555": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1102189616770211897": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "6290072698208008711": {
            "sample": 0.25,
            "type": "constant",
        },
        "5668746930321315167": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7385051959537366574": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3468149235340113902": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-1708055662682416731": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4504207811272896448": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5887402982541996013": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2306448123269729585": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "8472940893918271662": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1101621387088627099": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3148255752955750009": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5124521381760201624": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "5346015440958916872": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2321339615562633497": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6550842177140019358": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7765269188160798983": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "5730955657353991256": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5448265068521988287": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7822274107165032696": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8150209404555873367": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "4955023908708170355": {
            "sample": 0.25,
            "type": "constant",
        },
        "-664967469142545775": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7415690520889208123": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9025102739128664911": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "1754286278059336336": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3791892922101900565": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4413636367125091214": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2798677085684159149": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-1372639174900018454": {
            "sample": 0.25,
            "type": "constant",
        },
        "6832890114326973325": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-931998614287657104": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6380644142355813945": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "4853786478544487308": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4182884454352647082": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3961390395153931834": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6720464949940989353": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-1763630707150764971": {
            "sample": 0.25,
            "type": "constant",
        },
        "4090904877762692919": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3576450178758857450": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3691073169074714623": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "6510158624964575030": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1157196431556975339": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6703375631718212240": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4076013385469789007": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-4505615943715045377": {
            "sample": 0.25,
            "type": "constant",
        },
        "6273773073472955870": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6495267132671671118": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5347445315494802345": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "271559019709581738_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "271559019709581738_q": {
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
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "6832890114326973325": "6832890114326973325",
                "-931998614287657104": "-931998614287657104",
                "-6380644142355813945": "-6380644142355813945",
                "4853786478544487308": "4853786478544487308",
                "-4182884454352647082": "-4182884454352647082",
                "-3961390395153931834": "-3961390395153931834",
                "6720464949940989353": "6720464949940989353",
                "-1763630707150764971": "-1763630707150764971",
                "4090904877762692919": "4090904877762692919",
                "-3576450178758857450": "-3576450178758857450",
                "3691073169074714623": "3691073169074714623",
                "6510158624964575030": "6510158624964575030",
                "-1157196431556975339": "-1157196431556975339",
                "-6703375631718212240": "-6703375631718212240",
                "4076013385469789007": "4076013385469789007",
                "-4505615943715045377": "-4505615943715045377",
                "6273773073472955870": "6273773073472955870",
                "6495267132671671118": "6495267132671671118",
                "5347445315494802345": "5347445315494802345",
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
                "-489531609513980131": "-489531609513980131",
                "271559019709581738": "271559019709581738",
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
                "mixer": "B4/drive_mixer_712",
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
                "-8313996170767310540": "-8313996170767310540_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_06a",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "-489531609513980131": {
            "length": 40,
            "waveforms": {
                "I": "-489531609513980131_i",
                "Q": "-489531609513980131_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2245085365937880427": {
            "length": 16,
            "waveforms": {
                "single": "2245085365937880427",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8313996170767310540_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8378712858913607894_i",
                "Q": "-8378712858913607894_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-107280302824413793": {
            "length": 16,
            "waveforms": {
                "single": "-107280302824413793",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7107982855870303086": {
            "length": 16,
            "waveforms": {
                "single": "-7107982855870303086",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8143575721991545518": {
            "length": 16,
            "waveforms": {
                "single": "8143575721991545518",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4910223167867136223": {
            "length": 16,
            "waveforms": {
                "single": "-4910223167867136223",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7323689202205517416": {
            "length": 16,
            "waveforms": {
                "single": "7323689202205517416",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7545183261404232664": {
            "length": 16,
            "waveforms": {
                "single": "7545183261404232664",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2029379019602666097": {
            "length": 16,
            "waveforms": {
                "single": "-2029379019602666097",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8703801124302152089": {
            "length": 16,
            "waveforms": {
                "single": "-8703801124302152089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "168380668400500766": {
            "length": 16,
            "waveforms": {
                "single": "168380668400500766",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3470591307275387743": {
            "length": 16,
            "waveforms": {
                "single": "-3470591307275387743",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2976656618031046287": {
            "length": 16,
            "waveforms": {
                "single": "-2976656618031046287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1272831619272220880": {
            "length": 16,
            "waveforms": {
                "single": "-1272831619272220880",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1051337560073505632": {
            "length": 16,
            "waveforms": {
                "single": "-1051337560073505632",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7820844232629147223": {
            "length": 16,
            "waveforms": {
                "single": "7820844232629147223",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "153489176107596854": {
            "length": 16,
            "waveforms": {
                "single": "153489176107596854",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4675806946197600170": {
            "length": 20,
            "waveforms": {
                "single": "4675806946197600170",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-666397343678431248": {
            "length": 20,
            "waveforms": {
                "single": "-666397343678431248",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-444903284479716000": {
            "length": 20,
            "waveforms": {
                "single": "-444903284479716000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8427278508222936855": {
            "length": 20,
            "waveforms": {
                "single": "8427278508222936855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5232093012375233843": {
            "length": 24,
            "waveforms": {
                "single": "5232093012375233843",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "605034586346582090": {
            "length": 24,
            "waveforms": {
                "single": "605034586346582090",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6986066220550215209": {
            "length": 24,
            "waveforms": {
                "single": "6986066220550215209",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1809861322527684576": {
            "length": 24,
            "waveforms": {
                "single": "1809861322527684576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2031355381726399824": {
            "length": 28,
            "waveforms": {
                "single": "2031355381726399824",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6831460239791087852": {
            "length": 28,
            "waveforms": {
                "single": "6831460239791087852",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8257498150575228547": {
            "length": 28,
            "waveforms": {
                "single": "8257498150575228547",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6382074016891699418": {
            "length": 28,
            "waveforms": {
                "single": "-6382074016891699418",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8984419186953220583": {
            "length": 32,
            "waveforms": {
                "single": "-8984419186953220583",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4184314328888532555": {
            "length": 32,
            "waveforms": {
                "single": "-4184314328888532555",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1102189616770211897": {
            "length": 32,
            "waveforms": {
                "single": "1102189616770211897",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6290072698208008711": {
            "length": 32,
            "waveforms": {
                "single": "6290072698208008711",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5668746930321315167": {
            "length": 36,
            "waveforms": {
                "single": "5668746930321315167",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7385051959537366574": {
            "length": 36,
            "waveforms": {
                "single": "-7385051959537366574",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3468149235340113902": {
            "length": 36,
            "waveforms": {
                "single": "3468149235340113902",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1708055662682416731": {
            "length": 36,
            "waveforms": {
                "single": "-1708055662682416731",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4504207811272896448": {
            "length": 40,
            "waveforms": {
                "single": "-4504207811272896448",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5887402982541996013": {
            "length": 40,
            "waveforms": {
                "single": "5887402982541996013",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2306448123269729585": {
            "length": 40,
            "waveforms": {
                "single": "-2306448123269729585",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8472940893918271662": {
            "length": 40,
            "waveforms": {
                "single": "8472940893918271662",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1101621387088627099": {
            "length": 44,
            "waveforms": {
                "single": "-1101621387088627099",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3148255752955750009": {
            "length": 44,
            "waveforms": {
                "single": "3148255752955750009",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5124521381760201624": {
            "length": 44,
            "waveforms": {
                "single": "5124521381760201624",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5346015440958916872": {
            "length": 44,
            "waveforms": {
                "single": "5346015440958916872",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2321339615562633497": {
            "length": 48,
            "waveforms": {
                "single": "-2321339615562633497",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6550842177140019358": {
            "length": 48,
            "waveforms": {
                "single": "6550842177140019358",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7765269188160798983": {
            "length": 48,
            "waveforms": {
                "single": "7765269188160798983",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5730955657353991256": {
            "length": 48,
            "waveforms": {
                "single": "5730955657353991256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5448265068521988287": {
            "length": 52,
            "waveforms": {
                "single": "-5448265068521988287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7822274107165032696": {
            "length": 52,
            "waveforms": {
                "single": "7822274107165032696",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8150209404555873367": {
            "length": 52,
            "waveforms": {
                "single": "8150209404555873367",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4955023908708170355": {
            "length": 52,
            "waveforms": {
                "single": "4955023908708170355",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-664967469142545775": {
            "length": 56,
            "waveforms": {
                "single": "-664967469142545775",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7415690520889208123": {
            "length": 56,
            "waveforms": {
                "single": "-7415690520889208123",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9025102739128664911": {
            "length": 56,
            "waveforms": {
                "single": "-9025102739128664911",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1754286278059336336": {
            "length": 56,
            "waveforms": {
                "single": "1754286278059336336",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3791892922101900565": {
            "length": 60,
            "waveforms": {
                "single": "-3791892922101900565",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4413636367125091214": {
            "length": 60,
            "waveforms": {
                "single": "4413636367125091214",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2798677085684159149": {
            "length": 60,
            "waveforms": {
                "single": "-2798677085684159149",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1372639174900018454": {
            "length": 60,
            "waveforms": {
                "single": "-1372639174900018454",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6832890114326973325": {
            "length": 64,
            "waveforms": {
                "single": "6832890114326973325",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-931998614287657104": {
            "length": 64,
            "waveforms": {
                "single": "-931998614287657104",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6380644142355813945": {
            "length": 64,
            "waveforms": {
                "single": "-6380644142355813945",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4853786478544487308": {
            "length": 64,
            "waveforms": {
                "single": "4853786478544487308",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4182884454352647082": {
            "length": 68,
            "waveforms": {
                "single": "-4182884454352647082",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3961390395153931834": {
            "length": 68,
            "waveforms": {
                "single": "-3961390395153931834",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6720464949940989353": {
            "length": 68,
            "waveforms": {
                "single": "6720464949940989353",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1763630707150764971": {
            "length": 68,
            "waveforms": {
                "single": "-1763630707150764971",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4090904877762692919": {
            "length": 72,
            "waveforms": {
                "single": "4090904877762692919",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3576450178758857450": {
            "length": 72,
            "waveforms": {
                "single": "-3576450178758857450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3691073169074714623": {
            "length": 72,
            "waveforms": {
                "single": "3691073169074714623",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6510158624964575030": {
            "length": 72,
            "waveforms": {
                "single": "6510158624964575030",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1157196431556975339": {
            "length": 76,
            "waveforms": {
                "single": "-1157196431556975339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6703375631718212240": {
            "length": 76,
            "waveforms": {
                "single": "-6703375631718212240",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4076013385469789007": {
            "length": 76,
            "waveforms": {
                "single": "4076013385469789007",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4505615943715045377": {
            "length": 76,
            "waveforms": {
                "single": "-4505615943715045377",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6273773073472955870": {
            "length": 80,
            "waveforms": {
                "single": "6273773073472955870",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6495267132671671118": {
            "length": 80,
            "waveforms": {
                "single": "6495267132671671118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5347445315494802345": {
            "length": 80,
            "waveforms": {
                "single": "5347445315494802345",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "271559019709581738": {
            "length": 40,
            "waveforms": {
                "I": "271559019709581738_i",
                "Q": "271559019709581738_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-489531609513980131_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-489531609513980131_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2245085365937880427": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8378712858913607894_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-8378712858913607894_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-107280302824413793": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7107982855870303086": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8143575721991545518": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4910223167867136223": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7323689202205517416": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7545183261404232664": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2029379019602666097": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8703801124302152089": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "168380668400500766": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3470591307275387743": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2976656618031046287": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1272831619272220880": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1051337560073505632": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7820844232629147223": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "153489176107596854": {
            "type": "constant",
            "sample": 0.25,
        },
        "4675806946197600170": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-666397343678431248": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-444903284479716000": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8427278508222936855": {
            "type": "constant",
            "sample": 0.25,
        },
        "5232093012375233843": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "605034586346582090": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6986066220550215209": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1809861322527684576": {
            "type": "constant",
            "sample": 0.25,
        },
        "2031355381726399824": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6831460239791087852": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8257498150575228547": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6382074016891699418": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8984419186953220583": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4184314328888532555": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1102189616770211897": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6290072698208008711": {
            "type": "constant",
            "sample": 0.25,
        },
        "5668746930321315167": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7385051959537366574": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3468149235340113902": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1708055662682416731": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4504207811272896448": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5887402982541996013": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2306448123269729585": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8472940893918271662": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1101621387088627099": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3148255752955750009": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5124521381760201624": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5346015440958916872": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2321339615562633497": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6550842177140019358": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7765269188160798983": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5730955657353991256": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5448265068521988287": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7822274107165032696": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8150209404555873367": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4955023908708170355": {
            "type": "constant",
            "sample": 0.25,
        },
        "-664967469142545775": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7415690520889208123": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9025102739128664911": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1754286278059336336": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3791892922101900565": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4413636367125091214": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2798677085684159149": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1372639174900018454": {
            "type": "constant",
            "sample": 0.25,
        },
        "6832890114326973325": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-931998614287657104": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6380644142355813945": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4853786478544487308": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4182884454352647082": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3961390395153931834": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6720464949940989353": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1763630707150764971": {
            "type": "constant",
            "sample": 0.25,
        },
        "4090904877762692919": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3576450178758857450": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3691073169074714623": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6510158624964575030": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1157196431556975339": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6703375631718212240": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4076013385469789007": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4505615943715045377": {
            "type": "constant",
            "sample": 0.25,
        },
        "6273773073472955870": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6495267132671671118": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5347445315494802345": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "271559019709581738_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "271559019709581738_q": {
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
        "B4/drive_mixer_712": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_06a": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

