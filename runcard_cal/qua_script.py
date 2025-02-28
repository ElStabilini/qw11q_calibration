
# Single QUA script generated at 2025-02-28 09:16:25.903957
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
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-7223596750433082289", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-7178270014844114757", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("1027259274382877022", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("7408290908586510141", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-6516135395033038159", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-7459982301924701449", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("8458228779412808231", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("8679722838611523479", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("1012367782089973110", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-7569261547094861274", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("192481262303945008", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("9064663055006597863", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-9160586959504238505", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("704527785020478727", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-6962827271501071642", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("7844944826532591465", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-1729617454474307296", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-515190443453527671", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-6332067404946392545", "B4/drive")
        wait(11, "B4/flux")
        play("-5691395341476058304", "B4/flux")
        wait(46, "B4/drive")
        play("-5570976775722830676", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5252659246345018449", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("-5252659246345018449_B4|acquisition_shots")


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
                "-7223596750433082289": "-7223596750433082289",
                "-7178270014844114757": "-7178270014844114757",
                "1027259274382877022": "1027259274382877022",
                "7408290908586510141": "7408290908586510141",
                "-6516135395033038159": "-6516135395033038159",
                "-7459982301924701449": "-7459982301924701449",
                "8458228779412808231": "8458228779412808231",
                "8679722838611523479": "8679722838611523479",
                "1012367782089973110": "1012367782089973110",
                "-7569261547094861274": "-7569261547094861274",
                "192481262303945008": "192481262303945008",
                "9064663055006597863": "9064663055006597863",
                "-9160586959504238505": "-9160586959504238505",
                "704527785020478727": "704527785020478727",
                "-6962827271501071642": "-6962827271501071642",
                "7844944826532591465": "7844944826532591465",
                "-1729617454474307296": "-1729617454474307296",
                "-515190443453527671": "-515190443453527671",
                "-5691395341476058304": "-5691395341476058304",
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
                "-6332067404946392545": "-6332067404946392545",
                "-5570976775722830676": "-5570976775722830676",
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
                "-5252659246345018449": "-5252659246345018449_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-6332067404946392545": {
            "length": 40,
            "waveforms": {
                "I": "-6332067404946392545_i",
                "Q": "-6332067404946392545_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7090522976832837313": {
            "length": 16,
            "waveforms": {
                "single": "-7090522976832837313",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5252659246345018449_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-970809442174916927_i",
                "Q": "-970809442174916927_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "4605498045130051955": {
            "length": 16,
            "waveforms": {
                "single": "4605498045130051955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4328303641714049741": {
            "length": 16,
            "waveforms": {
                "single": "4328303641714049741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5912911142768510096": {
            "length": 16,
            "waveforms": {
                "single": "-5912911142768510096",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4866477874419491151": {
            "length": 16,
            "waveforms": {
                "single": "4866477874419491151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2011919140565200324": {
            "length": 16,
            "waveforms": {
                "single": "-2011919140565200324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3493657395566627985": {
            "length": 16,
            "waveforms": {
                "single": "-3493657395566627985",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7188197949528293202": {
            "length": 16,
            "waveforms": {
                "single": "7188197949528293202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1739552421460136361": {
            "length": 16,
            "waveforms": {
                "single": "1739552421460136361",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1626978924170125940": {
            "length": 16,
            "waveforms": {
                "single": "-1626978924170125940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3937312109463303224": {
            "length": 16,
            "waveforms": {
                "single": "3937312109463303224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4158806168662018472": {
            "length": 16,
            "waveforms": {
                "single": "4158806168662018472",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "792274823031756171": {
            "length": 16,
            "waveforms": {
                "single": "792274823031756171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9054728088020768798": {
            "length": 16,
            "waveforms": {
                "single": "-9054728088020768798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6025484640058520517": {
            "length": 16,
            "waveforms": {
                "single": "6025484640058520517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6856968400017601935": {
            "length": 16,
            "waveforms": {
                "single": "-6856968400017601935",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2334650629927598619": {
            "length": 20,
            "waveforms": {
                "single": "-2334650629927598619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4271430488641326286": {
            "length": 20,
            "waveforms": {
                "single": "-4271430488641326286",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6092372718498108408": {
            "length": 20,
            "waveforms": {
                "single": "6092372718498108408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5815178315082106194": {
            "length": 20,
            "waveforms": {
                "single": "5815178315082106194",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6250534124423812303": {
            "length": 24,
            "waveforms": {
                "single": "-6250534124423812303",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1728216354333808987": {
            "length": 24,
            "waveforms": {
                "single": "-1728216354333808987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3381033075587320171": {
            "length": 24,
            "waveforms": {
                "single": "3381033075587320171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6405140105182939660": {
            "length": 24,
            "waveforms": {
                "single": "-6405140105182939660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4979102194398798965": {
            "length": 28,
            "waveforms": {
                "single": "-4979102194398798965",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1171930288156175314": {
            "length": 28,
            "waveforms": {
                "single": "-1171930288156175314",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8124139480830346018": {
            "length": 28,
            "waveforms": {
                "single": "-8124139480830346018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1025829399846991549": {
            "length": 28,
            "waveforms": {
                "single": "1025829399846991549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4594161978003724581": {
            "length": 32,
            "waveforms": {
                "single": "-4594161978003724581",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7789347473851427593": {
            "length": 32,
            "waveforms": {
                "single": "-7789347473851427593",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7567853414652712345": {
            "length": 32,
            "waveforms": {
                "single": "-7567853414652712345",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2174908230801842470": {
            "length": 32,
            "waveforms": {
                "single": "-2174908230801842470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8678292964075638006": {
            "length": 36,
            "waveforms": {
                "single": "8678292964075638006",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5246133339543910294": {
            "length": 36,
            "waveforms": {
                "single": "-5246133339543910294",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7182913198257637961": {
            "length": 36,
            "waveforms": {
                "single": "-7182913198257637961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5256061274228088739": {
            "length": 36,
            "waveforms": {
                "single": "5256061274228088739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2903695605465794519": {
            "length": 40,
            "waveforms": {
                "single": "2903695605465794519",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4763659451055755850": {
            "length": 40,
            "waveforms": {
                "single": "-4763659451055755850",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6804687607669104291": {
            "length": 40,
            "waveforms": {
                "single": "6804687607669104291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "469550365971008496": {
            "length": 40,
            "waveforms": {
                "single": "469550365971008496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8112078963213825888": {
            "length": 44,
            "waveforms": {
                "single": "-8112078963213825888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2667310053974175359": {
            "length": 44,
            "waveforms": {
                "single": "2667310053974175359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2888804113172890607": {
            "length": 44,
            "waveforms": {
                "single": "2888804113172890607",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1740982295996021834": {
            "length": 44,
            "waveforms": {
                "single": "1740982295996021834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5086563801176057470": {
            "length": 48,
            "waveforms": {
                "single": "5086563801176057470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-459615398985179431": {
            "length": 48,
            "waveforms": {
                "single": "-459615398985179431",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8126970455506729800": {
            "length": 48,
            "waveforms": {
                "single": "-8126970455506729800",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3604652685416726484": {
            "length": 48,
            "waveforms": {
                "single": "-3604652685416726484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1959638348216702680": {
            "length": 52,
            "waveforms": {
                "single": "1959638348216702680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8281576436265857157": {
            "length": 52,
            "waveforms": {
                "single": "-8281576436265857157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4545176259592978329": {
            "length": 52,
            "waveforms": {
                "single": "4545176259592978329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3048366619239092811": {
            "length": 52,
            "waveforms": {
                "single": "-3048366619239092811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2344578564611777064": {
            "length": 56,
            "waveforms": {
                "single": "2344578564611777064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6964430006794860440": {
            "length": 56,
            "waveforms": {
                "single": "6964430006794860440",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6470598309086642078": {
            "length": 56,
            "waveforms": {
                "single": "-6470598309086642078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8822963977848936298": {
            "length": 56,
            "waveforms": {
                "single": "-8822963977848936298",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1448999391823238802": {
            "length": 60,
            "waveforms": {
                "single": "-1448999391823238802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4051344561884759967": {
            "length": 60,
            "waveforms": {
                "single": "-4051344561884759967",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-244172655642136316": {
            "length": 60,
            "waveforms": {
                "single": "-244172655642136316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7122569670626827791": {
            "length": 60,
            "waveforms": {
                "single": "-7122569670626827791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7223596750433082289": {
            "length": 64,
            "waveforms": {
                "single": "-7223596750433082289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7178270014844114757": {
            "length": 64,
            "waveforms": {
                "single": "-7178270014844114757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1027259274382877022": {
            "length": 64,
            "waveforms": {
                "single": "1027259274382877022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7408290908586510141": {
            "length": 64,
            "waveforms": {
                "single": "7408290908586510141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6516135395033038159": {
            "length": 68,
            "waveforms": {
                "single": "-6516135395033038159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7459982301924701449": {
            "length": 68,
            "waveforms": {
                "single": "-7459982301924701449",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8458228779412808231": {
            "length": 68,
            "waveforms": {
                "single": "8458228779412808231",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8679722838611523479": {
            "length": 68,
            "waveforms": {
                "single": "8679722838611523479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1012367782089973110": {
            "length": 72,
            "waveforms": {
                "single": "1012367782089973110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7569261547094861274": {
            "length": 72,
            "waveforms": {
                "single": "-7569261547094861274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "192481262303945008": {
            "length": 72,
            "waveforms": {
                "single": "192481262303945008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9064663055006597863": {
            "length": 72,
            "waveforms": {
                "single": "9064663055006597863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9160586959504238505": {
            "length": 76,
            "waveforms": {
                "single": "-9160586959504238505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "704527785020478727": {
            "length": 76,
            "waveforms": {
                "single": "704527785020478727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6962827271501071642": {
            "length": 76,
            "waveforms": {
                "single": "-6962827271501071642",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7844944826532591465": {
            "length": 76,
            "waveforms": {
                "single": "7844944826532591465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1729617454474307296": {
            "length": 80,
            "waveforms": {
                "single": "-1729617454474307296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-515190443453527671": {
            "length": 80,
            "waveforms": {
                "single": "-515190443453527671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5691395341476058304": {
            "length": 80,
            "waveforms": {
                "single": "-5691395341476058304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5570976775722830676": {
            "length": 40,
            "waveforms": {
                "I": "-5570976775722830676_i",
                "Q": "-5570976775722830676_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6332067404946392545_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-6332067404946392545_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-7090522976832837313": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-970809442174916927_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-970809442174916927_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4605498045130051955": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4328303641714049741": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-5912911142768510096": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "4866477874419491151": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-2011919140565200324": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-3493657395566627985": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "7188197949528293202": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "1739552421460136361": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-1626978924170125940": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "3937312109463303224": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "4158806168662018472": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "792274823031756171": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9054728088020768798": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6025484640058520517": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-6856968400017601935": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2334650629927598619": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4271430488641326286": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6092372718498108408": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "5815178315082106194": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6250534124423812303": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1728216354333808987": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3381033075587320171": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-6405140105182939660": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4979102194398798965": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1171930288156175314": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8124139480830346018": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1025829399846991549": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4594161978003724581": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7789347473851427593": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7567853414652712345": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-2174908230801842470": {
            "sample": 0.25,
            "type": "constant",
        },
        "8678292964075638006": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5246133339543910294": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7182913198257637961": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "5256061274228088739": {
            "sample": 0.25,
            "type": "constant",
        },
        "2903695605465794519": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4763659451055755850": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6804687607669104291": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "469550365971008496": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8112078963213825888": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2667310053974175359": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2888804113172890607": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1740982295996021834": {
            "sample": 0.25,
            "type": "constant",
        },
        "5086563801176057470": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-459615398985179431": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8126970455506729800": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-3604652685416726484": {
            "sample": 0.25,
            "type": "constant",
        },
        "1959638348216702680": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8281576436265857157": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4545176259592978329": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-3048366619239092811": {
            "sample": 0.25,
            "type": "constant",
        },
        "2344578564611777064": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6964430006794860440": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6470598309086642078": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-8822963977848936298": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1448999391823238802": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4051344561884759967": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-244172655642136316": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-7122569670626827791": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7223596750433082289": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7178270014844114757": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1027259274382877022": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "7408290908586510141": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6516135395033038159": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7459982301924701449": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8458228779412808231": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "8679722838611523479": {
            "sample": 0.25,
            "type": "constant",
        },
        "1012367782089973110": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7569261547094861274": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "192481262303945008": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "9064663055006597863": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9160586959504238505": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "704527785020478727": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6962827271501071642": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7844944826532591465": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1729617454474307296": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-515190443453527671": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5691395341476058304": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-5570976775722830676_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-5570976775722830676_q": {
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
                "-7223596750433082289": "-7223596750433082289",
                "-7178270014844114757": "-7178270014844114757",
                "1027259274382877022": "1027259274382877022",
                "7408290908586510141": "7408290908586510141",
                "-6516135395033038159": "-6516135395033038159",
                "-7459982301924701449": "-7459982301924701449",
                "8458228779412808231": "8458228779412808231",
                "8679722838611523479": "8679722838611523479",
                "1012367782089973110": "1012367782089973110",
                "-7569261547094861274": "-7569261547094861274",
                "192481262303945008": "192481262303945008",
                "9064663055006597863": "9064663055006597863",
                "-9160586959504238505": "-9160586959504238505",
                "704527785020478727": "704527785020478727",
                "-6962827271501071642": "-6962827271501071642",
                "7844944826532591465": "7844944826532591465",
                "-1729617454474307296": "-1729617454474307296",
                "-515190443453527671": "-515190443453527671",
                "-5691395341476058304": "-5691395341476058304",
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
                "-6332067404946392545": "-6332067404946392545",
                "-5570976775722830676": "-5570976775722830676",
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
                "mixer": "B4/drive_mixer_dd9",
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
                "-5252659246345018449": "-5252659246345018449_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_30f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "-6332067404946392545": {
            "length": 40,
            "waveforms": {
                "I": "-6332067404946392545_i",
                "Q": "-6332067404946392545_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7090522976832837313": {
            "length": 16,
            "waveforms": {
                "single": "-7090522976832837313",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5252659246345018449_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-970809442174916927_i",
                "Q": "-970809442174916927_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "4605498045130051955": {
            "length": 16,
            "waveforms": {
                "single": "4605498045130051955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4328303641714049741": {
            "length": 16,
            "waveforms": {
                "single": "4328303641714049741",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5912911142768510096": {
            "length": 16,
            "waveforms": {
                "single": "-5912911142768510096",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4866477874419491151": {
            "length": 16,
            "waveforms": {
                "single": "4866477874419491151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2011919140565200324": {
            "length": 16,
            "waveforms": {
                "single": "-2011919140565200324",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3493657395566627985": {
            "length": 16,
            "waveforms": {
                "single": "-3493657395566627985",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7188197949528293202": {
            "length": 16,
            "waveforms": {
                "single": "7188197949528293202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1739552421460136361": {
            "length": 16,
            "waveforms": {
                "single": "1739552421460136361",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1626978924170125940": {
            "length": 16,
            "waveforms": {
                "single": "-1626978924170125940",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3937312109463303224": {
            "length": 16,
            "waveforms": {
                "single": "3937312109463303224",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4158806168662018472": {
            "length": 16,
            "waveforms": {
                "single": "4158806168662018472",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "792274823031756171": {
            "length": 16,
            "waveforms": {
                "single": "792274823031756171",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9054728088020768798": {
            "length": 16,
            "waveforms": {
                "single": "-9054728088020768798",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6025484640058520517": {
            "length": 16,
            "waveforms": {
                "single": "6025484640058520517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6856968400017601935": {
            "length": 16,
            "waveforms": {
                "single": "-6856968400017601935",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2334650629927598619": {
            "length": 20,
            "waveforms": {
                "single": "-2334650629927598619",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4271430488641326286": {
            "length": 20,
            "waveforms": {
                "single": "-4271430488641326286",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6092372718498108408": {
            "length": 20,
            "waveforms": {
                "single": "6092372718498108408",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5815178315082106194": {
            "length": 20,
            "waveforms": {
                "single": "5815178315082106194",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6250534124423812303": {
            "length": 24,
            "waveforms": {
                "single": "-6250534124423812303",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1728216354333808987": {
            "length": 24,
            "waveforms": {
                "single": "-1728216354333808987",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3381033075587320171": {
            "length": 24,
            "waveforms": {
                "single": "3381033075587320171",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6405140105182939660": {
            "length": 24,
            "waveforms": {
                "single": "-6405140105182939660",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4979102194398798965": {
            "length": 28,
            "waveforms": {
                "single": "-4979102194398798965",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1171930288156175314": {
            "length": 28,
            "waveforms": {
                "single": "-1171930288156175314",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8124139480830346018": {
            "length": 28,
            "waveforms": {
                "single": "-8124139480830346018",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1025829399846991549": {
            "length": 28,
            "waveforms": {
                "single": "1025829399846991549",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4594161978003724581": {
            "length": 32,
            "waveforms": {
                "single": "-4594161978003724581",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7789347473851427593": {
            "length": 32,
            "waveforms": {
                "single": "-7789347473851427593",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7567853414652712345": {
            "length": 32,
            "waveforms": {
                "single": "-7567853414652712345",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2174908230801842470": {
            "length": 32,
            "waveforms": {
                "single": "-2174908230801842470",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8678292964075638006": {
            "length": 36,
            "waveforms": {
                "single": "8678292964075638006",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5246133339543910294": {
            "length": 36,
            "waveforms": {
                "single": "-5246133339543910294",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7182913198257637961": {
            "length": 36,
            "waveforms": {
                "single": "-7182913198257637961",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5256061274228088739": {
            "length": 36,
            "waveforms": {
                "single": "5256061274228088739",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2903695605465794519": {
            "length": 40,
            "waveforms": {
                "single": "2903695605465794519",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4763659451055755850": {
            "length": 40,
            "waveforms": {
                "single": "-4763659451055755850",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6804687607669104291": {
            "length": 40,
            "waveforms": {
                "single": "6804687607669104291",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "469550365971008496": {
            "length": 40,
            "waveforms": {
                "single": "469550365971008496",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8112078963213825888": {
            "length": 44,
            "waveforms": {
                "single": "-8112078963213825888",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2667310053974175359": {
            "length": 44,
            "waveforms": {
                "single": "2667310053974175359",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2888804113172890607": {
            "length": 44,
            "waveforms": {
                "single": "2888804113172890607",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1740982295996021834": {
            "length": 44,
            "waveforms": {
                "single": "1740982295996021834",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5086563801176057470": {
            "length": 48,
            "waveforms": {
                "single": "5086563801176057470",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-459615398985179431": {
            "length": 48,
            "waveforms": {
                "single": "-459615398985179431",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8126970455506729800": {
            "length": 48,
            "waveforms": {
                "single": "-8126970455506729800",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3604652685416726484": {
            "length": 48,
            "waveforms": {
                "single": "-3604652685416726484",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1959638348216702680": {
            "length": 52,
            "waveforms": {
                "single": "1959638348216702680",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8281576436265857157": {
            "length": 52,
            "waveforms": {
                "single": "-8281576436265857157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4545176259592978329": {
            "length": 52,
            "waveforms": {
                "single": "4545176259592978329",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3048366619239092811": {
            "length": 52,
            "waveforms": {
                "single": "-3048366619239092811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2344578564611777064": {
            "length": 56,
            "waveforms": {
                "single": "2344578564611777064",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6964430006794860440": {
            "length": 56,
            "waveforms": {
                "single": "6964430006794860440",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6470598309086642078": {
            "length": 56,
            "waveforms": {
                "single": "-6470598309086642078",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8822963977848936298": {
            "length": 56,
            "waveforms": {
                "single": "-8822963977848936298",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1448999391823238802": {
            "length": 60,
            "waveforms": {
                "single": "-1448999391823238802",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4051344561884759967": {
            "length": 60,
            "waveforms": {
                "single": "-4051344561884759967",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-244172655642136316": {
            "length": 60,
            "waveforms": {
                "single": "-244172655642136316",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7122569670626827791": {
            "length": 60,
            "waveforms": {
                "single": "-7122569670626827791",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7223596750433082289": {
            "length": 64,
            "waveforms": {
                "single": "-7223596750433082289",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7178270014844114757": {
            "length": 64,
            "waveforms": {
                "single": "-7178270014844114757",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1027259274382877022": {
            "length": 64,
            "waveforms": {
                "single": "1027259274382877022",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7408290908586510141": {
            "length": 64,
            "waveforms": {
                "single": "7408290908586510141",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6516135395033038159": {
            "length": 68,
            "waveforms": {
                "single": "-6516135395033038159",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7459982301924701449": {
            "length": 68,
            "waveforms": {
                "single": "-7459982301924701449",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8458228779412808231": {
            "length": 68,
            "waveforms": {
                "single": "8458228779412808231",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8679722838611523479": {
            "length": 68,
            "waveforms": {
                "single": "8679722838611523479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1012367782089973110": {
            "length": 72,
            "waveforms": {
                "single": "1012367782089973110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7569261547094861274": {
            "length": 72,
            "waveforms": {
                "single": "-7569261547094861274",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "192481262303945008": {
            "length": 72,
            "waveforms": {
                "single": "192481262303945008",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9064663055006597863": {
            "length": 72,
            "waveforms": {
                "single": "9064663055006597863",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9160586959504238505": {
            "length": 76,
            "waveforms": {
                "single": "-9160586959504238505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "704527785020478727": {
            "length": 76,
            "waveforms": {
                "single": "704527785020478727",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6962827271501071642": {
            "length": 76,
            "waveforms": {
                "single": "-6962827271501071642",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7844944826532591465": {
            "length": 76,
            "waveforms": {
                "single": "7844944826532591465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1729617454474307296": {
            "length": 80,
            "waveforms": {
                "single": "-1729617454474307296",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-515190443453527671": {
            "length": 80,
            "waveforms": {
                "single": "-515190443453527671",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5691395341476058304": {
            "length": 80,
            "waveforms": {
                "single": "-5691395341476058304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5570976775722830676": {
            "length": 40,
            "waveforms": {
                "I": "-5570976775722830676_i",
                "Q": "-5570976775722830676_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6332067404946392545_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6332067404946392545_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7090522976832837313": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-970809442174916927_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-970809442174916927_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "4605498045130051955": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4328303641714049741": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5912911142768510096": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4866477874419491151": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2011919140565200324": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3493657395566627985": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7188197949528293202": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1739552421460136361": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1626978924170125940": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3937312109463303224": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4158806168662018472": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "792274823031756171": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9054728088020768798": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6025484640058520517": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6856968400017601935": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2334650629927598619": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4271430488641326286": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6092372718498108408": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5815178315082106194": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6250534124423812303": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1728216354333808987": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3381033075587320171": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6405140105182939660": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4979102194398798965": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1171930288156175314": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8124139480830346018": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1025829399846991549": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4594161978003724581": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7789347473851427593": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7567853414652712345": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2174908230801842470": {
            "type": "constant",
            "sample": 0.25,
        },
        "8678292964075638006": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5246133339543910294": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7182913198257637961": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5256061274228088739": {
            "type": "constant",
            "sample": 0.25,
        },
        "2903695605465794519": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4763659451055755850": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6804687607669104291": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "469550365971008496": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8112078963213825888": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2667310053974175359": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2888804113172890607": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1740982295996021834": {
            "type": "constant",
            "sample": 0.25,
        },
        "5086563801176057470": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-459615398985179431": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8126970455506729800": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3604652685416726484": {
            "type": "constant",
            "sample": 0.25,
        },
        "1959638348216702680": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8281576436265857157": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4545176259592978329": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3048366619239092811": {
            "type": "constant",
            "sample": 0.25,
        },
        "2344578564611777064": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6964430006794860440": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6470598309086642078": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8822963977848936298": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1448999391823238802": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4051344561884759967": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-244172655642136316": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7122569670626827791": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7223596750433082289": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7178270014844114757": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1027259274382877022": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7408290908586510141": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6516135395033038159": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7459982301924701449": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8458228779412808231": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8679722838611523479": {
            "type": "constant",
            "sample": 0.25,
        },
        "1012367782089973110": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7569261547094861274": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "192481262303945008": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9064663055006597863": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9160586959504238505": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "704527785020478727": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6962827271501071642": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7844944826532591465": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1729617454474307296": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-515190443453527671": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5691395341476058304": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5570976775722830676_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5570976775722830676_q": {
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
        "B4/drive_mixer_dd9": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_30f": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

