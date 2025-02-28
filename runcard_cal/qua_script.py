
# Single QUA script generated at 2025-02-28 09:31:17.415291
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
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("6737115084334736122", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("6958609143533451370", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("7941941820515838608", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("9156368831536618233", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-5483203335930309732", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("7343549359928525754", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("4148363864080822742", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-2852338688965066551", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-8683940966579143751", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("6567617611282704853", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-7356808692336843447", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("4754798139674612374", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-1252971461549212542", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-3605337130311506762", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-2622004453329119524", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("295654871891803010", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("-9074932498829890268", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("3825632374718424447", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("-9124086554666520236", "B4/drive")
        wait(11, "B4/flux")
        play("4047126433917139695", "B4/flux")
        wait(46, "B4/drive")
        play("3037718859631736424", "B4/drive")
        wait(66, "B4/acquisition")
        measure("4827992721943324115", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5795859846190058)-(v3*0.8149110911217355))>-0.00034206752375852233)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("4827992721943324115_B4|acquisition_shots")


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
                "6737115084334736122": "6737115084334736122",
                "6958609143533451370": "6958609143533451370",
                "7941941820515838608": "7941941820515838608",
                "9156368831536618233": "9156368831536618233",
                "-5483203335930309732": "-5483203335930309732",
                "7343549359928525754": "7343549359928525754",
                "4148363864080822742": "4148363864080822742",
                "-2852338688965066551": "-2852338688965066551",
                "-8683940966579143751": "-8683940966579143751",
                "6567617611282704853": "6567617611282704853",
                "-7356808692336843447": "-7356808692336843447",
                "4754798139674612374": "4754798139674612374",
                "-1252971461549212542": "-1252971461549212542",
                "-3605337130311506762": "-3605337130311506762",
                "-2622004453329119524": "-2622004453329119524",
                "295654871891803010": "295654871891803010",
                "-9074932498829890268": "-9074932498829890268",
                "3825632374718424447": "3825632374718424447",
                "4047126433917139695": "4047126433917139695",
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
                "4827992721943324115": "4827992721943324115_B4/acquisition",
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
                "-9124086554666520236": "-9124086554666520236",
                "3037718859631736424": "3037718859631736424",
            },
        },
    },
    "pulses": {
        "-9124086554666520236": {
            "length": 40,
            "waveforms": {
                "I": "-9124086554666520236_i",
                "Q": "-9124086554666520236_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7050523869552173263": {
            "length": 16,
            "waveforms": {
                "single": "-7050523869552173263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4827992721943324115_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5280674357506902416_i",
                "Q": "-5280674357506902416_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4231438413662312856": {
            "length": 16,
            "waveforms": {
                "single": "-4231438413662312856",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3036084934171259217": {
            "length": 16,
            "waveforms": {
                "single": "3036084934171259217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4728803794443371212": {
            "length": 16,
            "waveforms": {
                "single": "-4728803794443371212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-108952352260287836": {
            "length": 16,
            "waveforms": {
                "single": "-108952352260287836",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8025016370097328722": {
            "length": 16,
            "waveforms": {
                "single": "-8025016370097328722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3421025150566333601": {
            "length": 16,
            "waveforms": {
                "single": "3421025150566333601",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7228197056808957252": {
            "length": 16,
            "waveforms": {
                "single": "7228197056808957252",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7322017152769643373": {
            "length": 16,
            "waveforms": {
                "single": "7322017152769643373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8578082095095674044": {
            "length": 16,
            "waveforms": {
                "single": "-8578082095095674044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4692457080591346939": {
            "length": 16,
            "waveforms": {
                "single": "4692457080591346939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2769053789026147888": {
            "length": 16,
            "waveforms": {
                "single": "2769053789026147888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "832273930312420221": {
            "length": 16,
            "waveforms": {
                "single": "832273930312420221",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5175495670911404695": {
            "length": 16,
            "waveforms": {
                "single": "-5175495670911404695",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7901236526246657736": {
            "length": 16,
            "waveforms": {
                "single": "7901236526246657736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5298891356185136571": {
            "length": 16,
            "waveforms": {
                "single": "5298891356185136571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7773845447604305648": {
            "length": 20,
            "waveforms": {
                "single": "7773845447604305648",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2227666247443068747": {
            "length": 20,
            "waveforms": {
                "single": "2227666247443068747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-96891834643767706": {
            "length": 20,
            "waveforms": {
                "single": "-96891834643767706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7664850974755038576": {
            "length": 20,
            "waveforms": {
                "single": "7664850974755038576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3241929121075314759": {
            "length": 24,
            "waveforms": {
                "single": "-3241929121075314759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2710140135931223191": {
            "length": 24,
            "waveforms": {
                "single": "2710140135931223191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5871489193253611193": {
            "length": 24,
            "waveforms": {
                "single": "-5871489193253611193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "509542440950021926": {
            "length": 24,
            "waveforms": {
                "single": "509542440950021926",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3129429534725866583": {
            "length": 28,
            "waveforms": {
                "single": "-3129429534725866583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4410534443153331698": {
            "length": 28,
            "waveforms": {
                "single": "4410534443153331698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7091207421727617591": {
            "length": 28,
            "waveforms": {
                "single": "-7091207421727617591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1780974370975035264": {
            "length": 28,
            "waveforms": {
                "single": "1780974370975035264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5886380685546515105": {
            "length": 32,
            "waveforms": {
                "single": "-5886380685546515105",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5762420298440879917": {
            "length": 32,
            "waveforms": {
                "single": "-5762420298440879917",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "339762083302313618": {
            "length": 32,
            "waveforms": {
                "single": "339762083302313618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "561256142501028866": {
            "length": 32,
            "waveforms": {
                "single": "561256142501028866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9013306138505869895": {
            "length": 36,
            "waveforms": {
                "single": "-9013306138505869895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-807776849278878116": {
            "length": 36,
            "waveforms": {
                "single": "-807776849278878116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8613551415417653619": {
            "length": 36,
            "waveforms": {
                "single": "8613551415417653619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "946196358896103250": {
            "length": 36,
            "waveforms": {
                "single": "946196358896103250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8628365922110795511": {
            "length": 40,
            "waveforms": {
                "single": "-8628365922110795511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8406871862912080263": {
            "length": 40,
            "waveforms": {
                "single": "-8406871862912080263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "791590378136975893": {
            "length": 40,
            "waveforms": {
                "single": "791590378136975893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2217628288921116588": {
            "length": 40,
            "waveforms": {
                "single": "2217628288921116588",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6024800195163740239": {
            "length": 44,
            "waveforms": {
                "single": "6024800195163740239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3422455025102219074": {
            "length": 44,
            "waveforms": {
                "single": "3422455025102219074",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1499051733537020023": {
            "length": 44,
            "waveforms": {
                "single": "1499051733537020023",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1221857330121017809": {
            "length": 44,
            "waveforms": {
                "single": "1221857330121017809",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "679165213750991921": {
            "length": 48,
            "waveforms": {
                "single": "679165213750991921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4769480314317164920": {
            "length": 48,
            "waveforms": {
                "single": "-4769480314317164920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2770483663562033361": {
            "length": 48,
            "waveforms": {
                "single": "2770483663562033361",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2571720626313998057": {
            "length": 48,
            "waveforms": {
                "single": "-2571720626313998057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6300461166388654798": {
            "length": 52,
            "waveforms": {
                "single": "6300461166388654798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5716757912745545110": {
            "length": 52,
            "waveforms": {
                "single": "-5716757912745545110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7281340632895849665": {
            "length": 52,
            "waveforms": {
                "single": "7281340632895849665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8346317984923841544": {
            "length": 52,
            "waveforms": {
                "single": "-8346317984923841544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1965286350720208425": {
            "length": 56,
            "waveforms": {
                "single": "-1965286350720208425",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-95461960107882233": {
            "length": 56,
            "waveforms": {
                "single": "-95461960107882233",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "126032099090833015": {
            "length": 56,
            "waveforms": {
                "single": "126032099090833015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-915348479893910335": {
            "length": 56,
            "waveforms": {
                "single": "-915348479893910335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-693854420695195087": {
            "length": 60,
            "waveforms": {
                "single": "-693854420695195087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8361209477216745456": {
            "length": 60,
            "waveforms": {
                "single": "-8361209477216745456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "510972315485907399": {
            "length": 60,
            "waveforms": {
                "single": "510972315485907399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7884936901511604895": {
            "length": 60,
            "waveforms": {
                "single": "7884936901511604895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6737115084334736122": {
            "length": 64,
            "waveforms": {
                "single": "6737115084334736122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6958609143533451370": {
            "length": 64,
            "waveforms": {
                "single": "6958609143533451370",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7941941820515838608": {
            "length": 64,
            "waveforms": {
                "single": "7941941820515838608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9156368831536618233": {
            "length": 64,
            "waveforms": {
                "single": "9156368831536618233",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5483203335930309732": {
            "length": 68,
            "waveforms": {
                "single": "-5483203335930309732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7343549359928525754": {
            "length": 68,
            "waveforms": {
                "single": "7343549359928525754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4148363864080822742": {
            "length": 68,
            "waveforms": {
                "single": "4148363864080822742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2852338688965066551": {
            "length": 68,
            "waveforms": {
                "single": "-2852338688965066551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8683940966579143751": {
            "length": 72,
            "waveforms": {
                "single": "-8683940966579143751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6567617611282704853": {
            "length": 72,
            "waveforms": {
                "single": "6567617611282704853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7356808692336843447": {
            "length": 72,
            "waveforms": {
                "single": "-7356808692336843447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4754798139674612374": {
            "length": 72,
            "waveforms": {
                "single": "4754798139674612374",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1252971461549212542": {
            "length": 76,
            "waveforms": {
                "single": "-1252971461549212542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3605337130311506762": {
            "length": 76,
            "waveforms": {
                "single": "-3605337130311506762",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2622004453329119524": {
            "length": 76,
            "waveforms": {
                "single": "-2622004453329119524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "295654871891803010": {
            "length": 76,
            "waveforms": {
                "single": "295654871891803010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9074932498829890268": {
            "length": 80,
            "waveforms": {
                "single": "-9074932498829890268",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3825632374718424447": {
            "length": 80,
            "waveforms": {
                "single": "3825632374718424447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4047126433917139695": {
            "length": 80,
            "waveforms": {
                "single": "4047126433917139695",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3037718859631736424": {
            "length": 40,
            "waveforms": {
                "I": "3037718859631736424_i",
                "Q": "3037718859631736424_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-9124086554666520236_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-9124086554666520236_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-7050523869552173263": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-5280674357506902416_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5280674357506902416_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4231438413662312856": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "3036084934171259217": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-4728803794443371212": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-108952352260287836": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-8025016370097328722": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3421025150566333601": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "7228197056808957252": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "7322017152769643373": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8578082095095674044": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "4692457080591346939": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "2769053789026147888": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "832273930312420221": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5175495670911404695": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7901236526246657736": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "5298891356185136571": {
            "sample": 0.25,
            "type": "constant",
        },
        "7773845447604305648": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2227666247443068747": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-96891834643767706": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7664850974755038576": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3241929121075314759": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2710140135931223191": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5871489193253611193": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "509542440950021926": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3129429534725866583": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4410534443153331698": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7091207421727617591": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1780974370975035264": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5886380685546515105": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5762420298440879917": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "339762083302313618": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "561256142501028866": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9013306138505869895": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-807776849278878116": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8613551415417653619": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "946196358896103250": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8628365922110795511": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8406871862912080263": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "791590378136975893": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "2217628288921116588": {
            "sample": 0.25,
            "type": "constant",
        },
        "6024800195163740239": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3422455025102219074": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1499051733537020023": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1221857330121017809": {
            "sample": 0.25,
            "type": "constant",
        },
        "679165213750991921": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4769480314317164920": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2770483663562033361": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2571720626313998057": {
            "sample": 0.25,
            "type": "constant",
        },
        "6300461166388654798": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5716757912745545110": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7281340632895849665": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-8346317984923841544": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1965286350720208425": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-95461960107882233": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "126032099090833015": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-915348479893910335": {
            "sample": 0.25,
            "type": "constant",
        },
        "-693854420695195087": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8361209477216745456": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "510972315485907399": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "7884936901511604895": {
            "sample": 0.25,
            "type": "constant",
        },
        "6737115084334736122": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6958609143533451370": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7941941820515838608": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "9156368831536618233": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5483203335930309732": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7343549359928525754": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4148363864080822742": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-2852338688965066551": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8683940966579143751": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6567617611282704853": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7356808692336843447": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "4754798139674612374": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1252971461549212542": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3605337130311506762": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2622004453329119524": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "295654871891803010": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9074932498829890268": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3825632374718424447": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4047126433917139695": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "3037718859631736424_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3037718859631736424_q": {
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
                "6737115084334736122": "6737115084334736122",
                "6958609143533451370": "6958609143533451370",
                "7941941820515838608": "7941941820515838608",
                "9156368831536618233": "9156368831536618233",
                "-5483203335930309732": "-5483203335930309732",
                "7343549359928525754": "7343549359928525754",
                "4148363864080822742": "4148363864080822742",
                "-2852338688965066551": "-2852338688965066551",
                "-8683940966579143751": "-8683940966579143751",
                "6567617611282704853": "6567617611282704853",
                "-7356808692336843447": "-7356808692336843447",
                "4754798139674612374": "4754798139674612374",
                "-1252971461549212542": "-1252971461549212542",
                "-3605337130311506762": "-3605337130311506762",
                "-2622004453329119524": "-2622004453329119524",
                "295654871891803010": "295654871891803010",
                "-9074932498829890268": "-9074932498829890268",
                "3825632374718424447": "3825632374718424447",
                "4047126433917139695": "4047126433917139695",
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
                "4827992721943324115": "4827992721943324115_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_323",
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
                "-9124086554666520236": "-9124086554666520236",
                "3037718859631736424": "3037718859631736424",
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
                "mixer": "B4/drive_mixer_03e",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "-9124086554666520236": {
            "length": 40,
            "waveforms": {
                "I": "-9124086554666520236_i",
                "Q": "-9124086554666520236_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7050523869552173263": {
            "length": 16,
            "waveforms": {
                "single": "-7050523869552173263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4827992721943324115_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5280674357506902416_i",
                "Q": "-5280674357506902416_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4231438413662312856": {
            "length": 16,
            "waveforms": {
                "single": "-4231438413662312856",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3036084934171259217": {
            "length": 16,
            "waveforms": {
                "single": "3036084934171259217",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4728803794443371212": {
            "length": 16,
            "waveforms": {
                "single": "-4728803794443371212",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-108952352260287836": {
            "length": 16,
            "waveforms": {
                "single": "-108952352260287836",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8025016370097328722": {
            "length": 16,
            "waveforms": {
                "single": "-8025016370097328722",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3421025150566333601": {
            "length": 16,
            "waveforms": {
                "single": "3421025150566333601",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7228197056808957252": {
            "length": 16,
            "waveforms": {
                "single": "7228197056808957252",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7322017152769643373": {
            "length": 16,
            "waveforms": {
                "single": "7322017152769643373",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8578082095095674044": {
            "length": 16,
            "waveforms": {
                "single": "-8578082095095674044",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4692457080591346939": {
            "length": 16,
            "waveforms": {
                "single": "4692457080591346939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2769053789026147888": {
            "length": 16,
            "waveforms": {
                "single": "2769053789026147888",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "832273930312420221": {
            "length": 16,
            "waveforms": {
                "single": "832273930312420221",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5175495670911404695": {
            "length": 16,
            "waveforms": {
                "single": "-5175495670911404695",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7901236526246657736": {
            "length": 16,
            "waveforms": {
                "single": "7901236526246657736",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5298891356185136571": {
            "length": 16,
            "waveforms": {
                "single": "5298891356185136571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7773845447604305648": {
            "length": 20,
            "waveforms": {
                "single": "7773845447604305648",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2227666247443068747": {
            "length": 20,
            "waveforms": {
                "single": "2227666247443068747",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-96891834643767706": {
            "length": 20,
            "waveforms": {
                "single": "-96891834643767706",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7664850974755038576": {
            "length": 20,
            "waveforms": {
                "single": "7664850974755038576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3241929121075314759": {
            "length": 24,
            "waveforms": {
                "single": "-3241929121075314759",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2710140135931223191": {
            "length": 24,
            "waveforms": {
                "single": "2710140135931223191",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5871489193253611193": {
            "length": 24,
            "waveforms": {
                "single": "-5871489193253611193",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "509542440950021926": {
            "length": 24,
            "waveforms": {
                "single": "509542440950021926",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3129429534725866583": {
            "length": 28,
            "waveforms": {
                "single": "-3129429534725866583",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4410534443153331698": {
            "length": 28,
            "waveforms": {
                "single": "4410534443153331698",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7091207421727617591": {
            "length": 28,
            "waveforms": {
                "single": "-7091207421727617591",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1780974370975035264": {
            "length": 28,
            "waveforms": {
                "single": "1780974370975035264",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5886380685546515105": {
            "length": 32,
            "waveforms": {
                "single": "-5886380685546515105",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5762420298440879917": {
            "length": 32,
            "waveforms": {
                "single": "-5762420298440879917",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "339762083302313618": {
            "length": 32,
            "waveforms": {
                "single": "339762083302313618",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "561256142501028866": {
            "length": 32,
            "waveforms": {
                "single": "561256142501028866",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9013306138505869895": {
            "length": 36,
            "waveforms": {
                "single": "-9013306138505869895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-807776849278878116": {
            "length": 36,
            "waveforms": {
                "single": "-807776849278878116",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8613551415417653619": {
            "length": 36,
            "waveforms": {
                "single": "8613551415417653619",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "946196358896103250": {
            "length": 36,
            "waveforms": {
                "single": "946196358896103250",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8628365922110795511": {
            "length": 40,
            "waveforms": {
                "single": "-8628365922110795511",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8406871862912080263": {
            "length": 40,
            "waveforms": {
                "single": "-8406871862912080263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "791590378136975893": {
            "length": 40,
            "waveforms": {
                "single": "791590378136975893",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2217628288921116588": {
            "length": 40,
            "waveforms": {
                "single": "2217628288921116588",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6024800195163740239": {
            "length": 44,
            "waveforms": {
                "single": "6024800195163740239",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3422455025102219074": {
            "length": 44,
            "waveforms": {
                "single": "3422455025102219074",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1499051733537020023": {
            "length": 44,
            "waveforms": {
                "single": "1499051733537020023",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1221857330121017809": {
            "length": 44,
            "waveforms": {
                "single": "1221857330121017809",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "679165213750991921": {
            "length": 48,
            "waveforms": {
                "single": "679165213750991921",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4769480314317164920": {
            "length": 48,
            "waveforms": {
                "single": "-4769480314317164920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2770483663562033361": {
            "length": 48,
            "waveforms": {
                "single": "2770483663562033361",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2571720626313998057": {
            "length": 48,
            "waveforms": {
                "single": "-2571720626313998057",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6300461166388654798": {
            "length": 52,
            "waveforms": {
                "single": "6300461166388654798",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5716757912745545110": {
            "length": 52,
            "waveforms": {
                "single": "-5716757912745545110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7281340632895849665": {
            "length": 52,
            "waveforms": {
                "single": "7281340632895849665",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8346317984923841544": {
            "length": 52,
            "waveforms": {
                "single": "-8346317984923841544",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1965286350720208425": {
            "length": 56,
            "waveforms": {
                "single": "-1965286350720208425",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-95461960107882233": {
            "length": 56,
            "waveforms": {
                "single": "-95461960107882233",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "126032099090833015": {
            "length": 56,
            "waveforms": {
                "single": "126032099090833015",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-915348479893910335": {
            "length": 56,
            "waveforms": {
                "single": "-915348479893910335",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-693854420695195087": {
            "length": 60,
            "waveforms": {
                "single": "-693854420695195087",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8361209477216745456": {
            "length": 60,
            "waveforms": {
                "single": "-8361209477216745456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "510972315485907399": {
            "length": 60,
            "waveforms": {
                "single": "510972315485907399",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7884936901511604895": {
            "length": 60,
            "waveforms": {
                "single": "7884936901511604895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6737115084334736122": {
            "length": 64,
            "waveforms": {
                "single": "6737115084334736122",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6958609143533451370": {
            "length": 64,
            "waveforms": {
                "single": "6958609143533451370",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7941941820515838608": {
            "length": 64,
            "waveforms": {
                "single": "7941941820515838608",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9156368831536618233": {
            "length": 64,
            "waveforms": {
                "single": "9156368831536618233",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5483203335930309732": {
            "length": 68,
            "waveforms": {
                "single": "-5483203335930309732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7343549359928525754": {
            "length": 68,
            "waveforms": {
                "single": "7343549359928525754",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4148363864080822742": {
            "length": 68,
            "waveforms": {
                "single": "4148363864080822742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2852338688965066551": {
            "length": 68,
            "waveforms": {
                "single": "-2852338688965066551",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8683940966579143751": {
            "length": 72,
            "waveforms": {
                "single": "-8683940966579143751",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6567617611282704853": {
            "length": 72,
            "waveforms": {
                "single": "6567617611282704853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7356808692336843447": {
            "length": 72,
            "waveforms": {
                "single": "-7356808692336843447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4754798139674612374": {
            "length": 72,
            "waveforms": {
                "single": "4754798139674612374",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1252971461549212542": {
            "length": 76,
            "waveforms": {
                "single": "-1252971461549212542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3605337130311506762": {
            "length": 76,
            "waveforms": {
                "single": "-3605337130311506762",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2622004453329119524": {
            "length": 76,
            "waveforms": {
                "single": "-2622004453329119524",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "295654871891803010": {
            "length": 76,
            "waveforms": {
                "single": "295654871891803010",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9074932498829890268": {
            "length": 80,
            "waveforms": {
                "single": "-9074932498829890268",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3825632374718424447": {
            "length": 80,
            "waveforms": {
                "single": "3825632374718424447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4047126433917139695": {
            "length": 80,
            "waveforms": {
                "single": "4047126433917139695",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3037718859631736424": {
            "length": 40,
            "waveforms": {
                "I": "3037718859631736424_i",
                "Q": "3037718859631736424_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-9124086554666520236_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9124086554666520236_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7050523869552173263": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5280674357506902416_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-5280674357506902416_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4231438413662312856": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3036084934171259217": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4728803794443371212": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-108952352260287836": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8025016370097328722": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3421025150566333601": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7228197056808957252": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7322017152769643373": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8578082095095674044": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4692457080591346939": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2769053789026147888": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "832273930312420221": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5175495670911404695": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7901236526246657736": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5298891356185136571": {
            "type": "constant",
            "sample": 0.25,
        },
        "7773845447604305648": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2227666247443068747": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-96891834643767706": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7664850974755038576": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3241929121075314759": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2710140135931223191": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5871489193253611193": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "509542440950021926": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3129429534725866583": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4410534443153331698": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7091207421727617591": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1780974370975035264": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5886380685546515105": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5762420298440879917": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "339762083302313618": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "561256142501028866": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9013306138505869895": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-807776849278878116": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8613551415417653619": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "946196358896103250": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8628365922110795511": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8406871862912080263": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "791590378136975893": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2217628288921116588": {
            "type": "constant",
            "sample": 0.25,
        },
        "6024800195163740239": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3422455025102219074": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1499051733537020023": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1221857330121017809": {
            "type": "constant",
            "sample": 0.25,
        },
        "679165213750991921": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4769480314317164920": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2770483663562033361": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2571720626313998057": {
            "type": "constant",
            "sample": 0.25,
        },
        "6300461166388654798": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5716757912745545110": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7281340632895849665": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8346317984923841544": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1965286350720208425": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-95461960107882233": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "126032099090833015": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-915348479893910335": {
            "type": "constant",
            "sample": 0.25,
        },
        "-693854420695195087": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8361209477216745456": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "510972315485907399": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7884936901511604895": {
            "type": "constant",
            "sample": 0.25,
        },
        "6737115084334736122": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6958609143533451370": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7941941820515838608": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9156368831536618233": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5483203335930309732": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7343549359928525754": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4148363864080822742": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2852338688965066551": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8683940966579143751": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6567617611282704853": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7356808692336843447": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4754798139674612374": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1252971461549212542": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3605337130311506762": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2622004453329119524": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "295654871891803010": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9074932498829890268": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3825632374718424447": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4047126433917139695": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3037718859631736424_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3037718859631736424_q": {
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
        "B4/acquisition_mixer_323": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_03e": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

