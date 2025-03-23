
# Single QUA script generated at 2025-03-23 19:00:56.936777
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(int, )
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-1069109754447709049", "B2/drive")
        wait(11, "B2/flux")
        play("5149159374505047244", "B2/flux")
        wait(46, "B2/drive")
        play("-308019125224147180", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6494524314438032883", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.64974092063167)-(v3*0.7601557314502798))>0.0024960151101936427)))
        r1 = declare_stream()
        save(v4, r1)
        play("7424997495037455510", "B4/drive")
        wait(11, "B4/flux")
        play("5149159374505047244", "B4/flux")
        wait(46, "B4/drive")
        play("8186088124261017379", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4554039990346288644", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.3668872881069954)-(v6*0.9302654018211656))>-0.0006690936940747121)))
        r2 = declare_stream()
        save(v7, r2)
        wait(25537, "B2/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        play("-1069109754447709049", "B2/drive")
        wait(11, "B2/flux")
        play("-6030061351370932299", "B2/flux")
        wait(46, "B2/drive")
        play("-308019125224147180", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6494524314438032883", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.64974092063167)-(v3*0.7601557314502798))>0.0024960151101936427)))
        save(v4, r1)
        play("7424997495037455510", "B4/drive")
        wait(11, "B4/flux")
        play("-6030061351370932299", "B4/flux")
        wait(46, "B4/drive")
        play("8186088124261017379", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4554039990346288644", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.3668872881069954)-(v6*0.9302654018211656))>-0.0006690936940747121)))
        save(v7, r2)
        wait(25536, "B2/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        play("-1069109754447709049", "B2/drive")
        wait(11, "B2/flux")
        play("-1507743581280928983", "B2/flux")
        wait(46, "B2/drive")
        play("-308019125224147180", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6494524314438032883", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.64974092063167)-(v3*0.7601557314502798))>0.0024960151101936427)))
        save(v4, r1)
        play("7424997495037455510", "B4/drive")
        wait(11, "B4/flux")
        play("-1507743581280928983", "B4/flux")
        wait(46, "B4/drive")
        play("8186088124261017379", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4554039990346288644", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.3668872881069954)-(v6*0.9302654018211656))>-0.0006690936940747121)))
        save(v7, r2)
        wait(25536, "B2/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        play("-1069109754447709049", "B2/drive")
        wait(11, "B2/flux")
        play("-7842880822979024778", "B2/flux")
        wait(46, "B2/drive")
        play("-308019125224147180", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6494524314438032883", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.64974092063167)-(v3*0.7601557314502798))>0.0024960151101936427)))
        save(v4, r1)
        play("7424997495037455510", "B4/drive")
        wait(11, "B4/flux")
        play("-7842880822979024778", "B4/flux")
        wait(46, "B4/drive")
        play("8186088124261017379", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-4554039990346288644", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.3668872881069954)-(v6*0.9302654018211656))>-0.0006690936940747121)))
        save(v7, r2)
        wait(25536, "B2/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(4).average().save("6494524314438032883_B2|acquisition_shots")
        r2.buffer(4).average().save("-4554039990346288644_B4|acquisition_shots")


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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                "1": {},
                "7": {},
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
                "4": {
                    "LO_frequency": 5900000000.0,
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
            "operations": {
                "5149159374505047244": "5149159374505047244",
                "-6030061351370932299": "-6030061351370932299",
                "-1507743581280928983": "-1507743581280928983",
                "-7842880822979024778": "-7842880822979024778",
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
                "5149159374505047244": "5149159374505047244",
                "-6030061351370932299": "-6030061351370932299",
                "-1507743581280928983": "-1507743581280928983",
                "-7842880822979024778": "-7842880822979024778",
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
                "7424997495037455510": "7424997495037455510",
                "8186088124261017379": "8186088124261017379",
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
                "-4554039990346288644": "-4554039990346288644_B4/acquisition",
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
                "6494524314438032883": "6494524314438032883_B2/acquisition",
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
                "-1069109754447709049": "-1069109754447709049",
                "-308019125224147180": "-308019125224147180",
            },
        },
    },
    "pulses": {
        "-1069109754447709049": {
            "length": 40,
            "waveforms": {
                "I": "-1069109754447709049_i",
                "Q": "-1069109754447709049_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1341965726168687049": {
            "length": 16,
            "waveforms": {
                "single": "1341965726168687049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6494524314438032883_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6593246697725380560_i",
                "Q": "-6593246697725380560_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "7424997495037455510": {
            "length": 40,
            "waveforms": {
                "I": "7424997495037455510_i",
                "Q": "7424997495037455510_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4554039990346288644_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3434336377218927642_i",
                "Q": "3434336377218927642_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "623106286188913445": {
            "length": 16,
            "waveforms": {
                "single": "623106286188913445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "844600345387628693": {
            "length": 16,
            "waveforms": {
                "single": "844600345387628693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9050129634614620472": {
            "length": 16,
            "waveforms": {
                "single": "9050129634614620472",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3042360033390795556": {
            "length": 16,
            "waveforms": {
                "single": "3042360033390795556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "689994364628501336": {
            "length": 16,
            "waveforms": {
                "single": "689994364628501336",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8275569850417559902": {
            "length": 16,
            "waveforms": {
                "single": "8275569850417559902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5923204181655265682": {
            "length": 16,
            "waveforms": {
                "single": "5923204181655265682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3447383189066427596": {
            "length": 16,
            "waveforms": {
                "single": "-3447383189066427596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8120963869658432545": {
            "length": 16,
            "waveforms": {
                "single": "8120963869658432545",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8342457928857147793": {
            "length": 16,
            "waveforms": {
                "single": "8342457928857147793",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6308144398050340066": {
            "length": 16,
            "waveforms": {
                "single": "6308144398050340066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6529638457249055314": {
            "length": 16,
            "waveforms": {
                "single": "6529638457249055314",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8505904086053506929": {
            "length": 16,
            "waveforms": {
                "single": "8505904086053506929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8727398145252222177": {
            "length": 16,
            "waveforms": {
                "single": "8727398145252222177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8948892204450937425": {
            "length": 16,
            "waveforms": {
                "single": "8948892204450937425",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-87778728446196965": {
            "length": 20,
            "waveforms": {
                "single": "-87778728446196965",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5476512305187232199": {
            "length": 20,
            "waveforms": {
                "single": "5476512305187232199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2288376423427398230": {
            "length": 20,
            "waveforms": {
                "single": "-2288376423427398230",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2066882364228682982": {
            "length": 20,
            "waveforms": {
                "single": "-2066882364228682982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3214704181405551755": {
            "length": 24,
            "waveforms": {
                "single": "-3214704181405551755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "130877323774483881": {
            "length": 24,
            "waveforms": {
                "single": "130877323774483881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6082946580781021831": {
            "length": 24,
            "waveforms": {
                "single": "6082946580781021831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8684299549923935261": {
            "length": 24,
            "waveforms": {
                "single": "-8684299549923935261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8462805490725220013": {
            "length": 28,
            "waveforms": {
                "single": "-8462805490725220013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1402309253799497219": {
            "length": 28,
            "waveforms": {
                "single": "1402309253799497219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4932827987898598576": {
            "length": 28,
            "waveforms": {
                "single": "-4932827987898598576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-410510217808595260": {
            "length": 28,
            "waveforms": {
                "single": "-410510217808595260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1031835985695288804": {
            "length": 32,
            "waveforms": {
                "single": "-1031835985695288804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5087433968657725933": {
            "length": 32,
            "waveforms": {
                "single": "-5087433968657725933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2008743529393286851": {
            "length": 32,
            "waveforms": {
                "single": "2008743529393286851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5584799349438784289": {
            "length": 32,
            "waveforms": {
                "single": "-5584799349438784289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7241953346420051197": {
            "length": 36,
            "waveforms": {
                "single": "7241953346420051197",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4917395264333214744": {
            "length": 36,
            "waveforms": {
                "single": "4917395264333214744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2565029595570920524": {
            "length": 36,
            "waveforms": {
                "single": "2565029595570920524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-801501750059341777": {
            "length": 36,
            "waveforms": {
                "single": "-801501750059341777",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-580007690860626529": {
            "length": 40,
            "waveforms": {
                "single": "-580007690860626529",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6126186891021863430": {
            "length": 40,
            "waveforms": {
                "single": "-6126186891021863430",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8450744973108699883": {
            "length": 40,
            "waveforms": {
                "single": "-8450744973108699883",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1354567475057687099": {
            "length": 40,
            "waveforms": {
                "single": "-1354567475057687099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6850961814169304680": {
            "length": 44,
            "waveforms": {
                "single": "6850961814169304680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7072455873368019928": {
            "length": 44,
            "waveforms": {
                "single": "7072455873368019928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1509173455816814456": {
            "length": 44,
            "waveforms": {
                "single": "-1509173455816814456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3445953314530542123": {
            "length": 44,
            "waveforms": {
                "single": "-3445953314530542123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3724036361209949890": {
            "length": 48,
            "waveforms": {
                "single": "3724036361209949890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3943318695311600479": {
            "length": 48,
            "waveforms": {
                "single": "-3943318695311600479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1124233239421740072": {
            "length": 48,
            "waveforms": {
                "single": "-1124233239421740072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6143290108411832001": {
            "length": 48,
            "waveforms": {
                "single": "6143290108411832001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4206510249698104334": {
            "length": 52,
            "waveforms": {
                "single": "4206510249698104334",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8728828019788107650": {
            "length": 52,
            "waveforms": {
                "single": "8728828019788107650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6404269937701271197": {
            "length": 52,
            "waveforms": {
                "single": "6404269937701271197",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6528230324806906385": {
            "length": 52,
            "waveforms": {
                "single": "6528230324806906385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1079584796738749544": {
            "length": 56,
            "waveforms": {
                "single": "1079584796738749544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3554538888157918621": {
            "length": 56,
            "waveforms": {
                "single": "3554538888157918621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3277344484741916407": {
            "length": 56,
            "waveforms": {
                "single": "3277344484741916407",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4390010571779633962": {
            "length": 56,
            "waveforms": {
                "single": "-4390010571779633962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "132307198310369354": {
            "length": 60,
            "waveforms": {
                "single": "132307198310369354",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3939479104552993005": {
            "length": 60,
            "waveforms": {
                "single": "3939479104552993005",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5365517015337133700": {
            "length": 60,
            "waveforms": {
                "single": "5365517015337133700",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3883778760335706039": {
            "length": 60,
            "waveforms": {
                "single": "3883778760335706039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "688593264488003027": {
            "length": 64,
            "waveforms": {
                "single": "688593264488003027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7784770762539015811": {
            "length": 64,
            "waveforms": {
                "single": "7784770762539015811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6854801404927912154": {
            "length": 64,
            "waveforms": {
                "single": "-6854801404927912154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2733638425359546240": {
            "length": 64,
            "waveforms": {
                "single": "-2733638425359546240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8962382596603343028": {
            "length": 68,
            "waveforms": {
                "single": "8962382596603343028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2010173403929172324": {
            "length": 68,
            "waveforms": {
                "single": "2010173403929172324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5583369474902898816": {
            "length": 68,
            "waveforms": {
                "single": "-5583369474902898816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3492787228084959522": {
            "length": 68,
            "waveforms": {
                "single": "3492787228084959522",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8015104998174962838": {
            "length": 72,
            "waveforms": {
                "single": "8015104998174962838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2566459470106805997": {
            "length": 72,
            "waveforms": {
                "single": "2566459470106805997",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5198429258507824432": {
            "length": 72,
            "waveforms": {
                "single": "-5198429258507824432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "365861775125604732": {
            "length": 72,
            "waveforms": {
                "single": "365861775125604732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4888179545215608048": {
            "length": 76,
            "waveforms": {
                "single": "4888179545215608048",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2951399686501880381": {
            "length": 76,
            "waveforms": {
                "single": "2951399686501880381",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8227821039374099162": {
            "length": 76,
            "waveforms": {
                "single": "-8227821039374099162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5149159374505047244": {
            "length": 76,
            "waveforms": {
                "single": "5149159374505047244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6030061351370932299": {
            "length": 80,
            "waveforms": {
                "single": "-6030061351370932299",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1507743581280928983": {
            "length": 80,
            "waveforms": {
                "single": "-1507743581280928983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7842880822979024778": {
            "length": 80,
            "waveforms": {
                "single": "-7842880822979024778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-308019125224147180": {
            "length": 40,
            "waveforms": {
                "I": "-308019125224147180_i",
                "Q": "-308019125224147180_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8186088124261017379": {
            "length": 40,
            "waveforms": {
                "I": "8186088124261017379_i",
                "Q": "8186088124261017379_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1069109754447709049_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-1069109754447709049_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "1341965726168687049": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6593246697725380560_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-6593246697725380560_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7424997495037455510_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "7424997495037455510_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3434336377218927642_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3434336377218927642_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "623106286188913445": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "844600345387628693": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "9050129634614620472": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "3042360033390795556": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "689994364628501336": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8275569850417559902": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "5923204181655265682": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-3447383189066427596": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "8120963869658432545": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8342457928857147793": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "6308144398050340066": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "6529638457249055314": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8505904086053506929": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8727398145252222177": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "8948892204450937425": {
            "sample": 0.25,
            "type": "constant",
        },
        "-87778728446196965": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5476512305187232199": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2288376423427398230": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2066882364228682982": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3214704181405551755": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "130877323774483881": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6082946580781021831": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8684299549923935261": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8462805490725220013": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1402309253799497219": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4932827987898598576": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-410510217808595260": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1031835985695288804": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5087433968657725933": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2008743529393286851": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5584799349438784289": {
            "sample": 0.25,
            "type": "constant",
        },
        "7241953346420051197": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4917395264333214744": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2565029595570920524": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-801501750059341777": {
            "sample": 0.25,
            "type": "constant",
        },
        "-580007690860626529": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6126186891021863430": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8450744973108699883": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1354567475057687099": {
            "sample": 0.25,
            "type": "constant",
        },
        "6850961814169304680": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7072455873368019928": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1509173455816814456": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-3445953314530542123": {
            "sample": 0.25,
            "type": "constant",
        },
        "3724036361209949890": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3943318695311600479": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1124233239421740072": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "6143290108411832001": {
            "sample": 0.25,
            "type": "constant",
        },
        "4206510249698104334": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8728828019788107650": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6404269937701271197": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "6528230324806906385": {
            "sample": 0.25,
            "type": "constant",
        },
        "1079584796738749544": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3554538888157918621": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3277344484741916407": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-4390010571779633962": {
            "sample": 0.25,
            "type": "constant",
        },
        "132307198310369354": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3939479104552993005": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5365517015337133700": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "3883778760335706039": {
            "sample": 0.25,
            "type": "constant",
        },
        "688593264488003027": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7784770762539015811": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6854801404927912154": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-2733638425359546240": {
            "sample": 0.25,
            "type": "constant",
        },
        "8962382596603343028": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2010173403929172324": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5583369474902898816": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "3492787228084959522": {
            "sample": 0.25,
            "type": "constant",
        },
        "8015104998174962838": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2566459470106805997": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5198429258507824432": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "365861775125604732": {
            "sample": 0.25,
            "type": "constant",
        },
        "4888179545215608048": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2951399686501880381": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8227821039374099162": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "5149159374505047244": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6030061351370932299": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1507743581280928983": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7842880822979024778": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-308019125224147180_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-308019125224147180_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "8186088124261017379_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "8186088124261017379_q": {
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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
            "operations": {
                "5149159374505047244": "5149159374505047244",
                "-6030061351370932299": "-6030061351370932299",
                "-1507743581280928983": "-1507743581280928983",
                "-7842880822979024778": "-7842880822979024778",
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
                "5149159374505047244": "5149159374505047244",
                "-6030061351370932299": "-6030061351370932299",
                "-1507743581280928983": "-1507743581280928983",
                "-7842880822979024778": "-7842880822979024778",
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
                "7424997495037455510": "7424997495037455510",
                "8186088124261017379": "8186088124261017379",
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
                "mixer": "B4/drive_mixer_326",
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
                "-4554039990346288644": "-4554039990346288644_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e8f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
        "B2/acquisition": {
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
                "6494524314438032883": "6494524314438032883_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_f88",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-1069109754447709049": "-1069109754447709049",
                "-308019125224147180": "-308019125224147180",
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
                "I": ('con2', 1, 7),
                "Q": ('con2', 1, 8),
                "mixer": "B2/drive_mixer_3ce",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
    },
    "pulses": {
        "-1069109754447709049": {
            "length": 40,
            "waveforms": {
                "I": "-1069109754447709049_i",
                "Q": "-1069109754447709049_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1341965726168687049": {
            "length": 16,
            "waveforms": {
                "single": "1341965726168687049",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6494524314438032883_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6593246697725380560_i",
                "Q": "-6593246697725380560_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7424997495037455510": {
            "length": 40,
            "waveforms": {
                "I": "7424997495037455510_i",
                "Q": "7424997495037455510_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4554039990346288644_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3434336377218927642_i",
                "Q": "3434336377218927642_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "623106286188913445": {
            "length": 16,
            "waveforms": {
                "single": "623106286188913445",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "844600345387628693": {
            "length": 16,
            "waveforms": {
                "single": "844600345387628693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9050129634614620472": {
            "length": 16,
            "waveforms": {
                "single": "9050129634614620472",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3042360033390795556": {
            "length": 16,
            "waveforms": {
                "single": "3042360033390795556",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "689994364628501336": {
            "length": 16,
            "waveforms": {
                "single": "689994364628501336",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8275569850417559902": {
            "length": 16,
            "waveforms": {
                "single": "8275569850417559902",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5923204181655265682": {
            "length": 16,
            "waveforms": {
                "single": "5923204181655265682",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3447383189066427596": {
            "length": 16,
            "waveforms": {
                "single": "-3447383189066427596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8120963869658432545": {
            "length": 16,
            "waveforms": {
                "single": "8120963869658432545",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8342457928857147793": {
            "length": 16,
            "waveforms": {
                "single": "8342457928857147793",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6308144398050340066": {
            "length": 16,
            "waveforms": {
                "single": "6308144398050340066",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6529638457249055314": {
            "length": 16,
            "waveforms": {
                "single": "6529638457249055314",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8505904086053506929": {
            "length": 16,
            "waveforms": {
                "single": "8505904086053506929",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8727398145252222177": {
            "length": 16,
            "waveforms": {
                "single": "8727398145252222177",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8948892204450937425": {
            "length": 16,
            "waveforms": {
                "single": "8948892204450937425",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-87778728446196965": {
            "length": 20,
            "waveforms": {
                "single": "-87778728446196965",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5476512305187232199": {
            "length": 20,
            "waveforms": {
                "single": "5476512305187232199",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2288376423427398230": {
            "length": 20,
            "waveforms": {
                "single": "-2288376423427398230",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2066882364228682982": {
            "length": 20,
            "waveforms": {
                "single": "-2066882364228682982",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3214704181405551755": {
            "length": 24,
            "waveforms": {
                "single": "-3214704181405551755",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "130877323774483881": {
            "length": 24,
            "waveforms": {
                "single": "130877323774483881",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6082946580781021831": {
            "length": 24,
            "waveforms": {
                "single": "6082946580781021831",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8684299549923935261": {
            "length": 24,
            "waveforms": {
                "single": "-8684299549923935261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8462805490725220013": {
            "length": 28,
            "waveforms": {
                "single": "-8462805490725220013",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1402309253799497219": {
            "length": 28,
            "waveforms": {
                "single": "1402309253799497219",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4932827987898598576": {
            "length": 28,
            "waveforms": {
                "single": "-4932827987898598576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-410510217808595260": {
            "length": 28,
            "waveforms": {
                "single": "-410510217808595260",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1031835985695288804": {
            "length": 32,
            "waveforms": {
                "single": "-1031835985695288804",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5087433968657725933": {
            "length": 32,
            "waveforms": {
                "single": "-5087433968657725933",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2008743529393286851": {
            "length": 32,
            "waveforms": {
                "single": "2008743529393286851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5584799349438784289": {
            "length": 32,
            "waveforms": {
                "single": "-5584799349438784289",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7241953346420051197": {
            "length": 36,
            "waveforms": {
                "single": "7241953346420051197",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4917395264333214744": {
            "length": 36,
            "waveforms": {
                "single": "4917395264333214744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2565029595570920524": {
            "length": 36,
            "waveforms": {
                "single": "2565029595570920524",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-801501750059341777": {
            "length": 36,
            "waveforms": {
                "single": "-801501750059341777",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-580007690860626529": {
            "length": 40,
            "waveforms": {
                "single": "-580007690860626529",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6126186891021863430": {
            "length": 40,
            "waveforms": {
                "single": "-6126186891021863430",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8450744973108699883": {
            "length": 40,
            "waveforms": {
                "single": "-8450744973108699883",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1354567475057687099": {
            "length": 40,
            "waveforms": {
                "single": "-1354567475057687099",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6850961814169304680": {
            "length": 44,
            "waveforms": {
                "single": "6850961814169304680",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7072455873368019928": {
            "length": 44,
            "waveforms": {
                "single": "7072455873368019928",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1509173455816814456": {
            "length": 44,
            "waveforms": {
                "single": "-1509173455816814456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3445953314530542123": {
            "length": 44,
            "waveforms": {
                "single": "-3445953314530542123",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3724036361209949890": {
            "length": 48,
            "waveforms": {
                "single": "3724036361209949890",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3943318695311600479": {
            "length": 48,
            "waveforms": {
                "single": "-3943318695311600479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1124233239421740072": {
            "length": 48,
            "waveforms": {
                "single": "-1124233239421740072",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6143290108411832001": {
            "length": 48,
            "waveforms": {
                "single": "6143290108411832001",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4206510249698104334": {
            "length": 52,
            "waveforms": {
                "single": "4206510249698104334",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8728828019788107650": {
            "length": 52,
            "waveforms": {
                "single": "8728828019788107650",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6404269937701271197": {
            "length": 52,
            "waveforms": {
                "single": "6404269937701271197",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6528230324806906385": {
            "length": 52,
            "waveforms": {
                "single": "6528230324806906385",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1079584796738749544": {
            "length": 56,
            "waveforms": {
                "single": "1079584796738749544",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3554538888157918621": {
            "length": 56,
            "waveforms": {
                "single": "3554538888157918621",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3277344484741916407": {
            "length": 56,
            "waveforms": {
                "single": "3277344484741916407",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4390010571779633962": {
            "length": 56,
            "waveforms": {
                "single": "-4390010571779633962",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "132307198310369354": {
            "length": 60,
            "waveforms": {
                "single": "132307198310369354",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3939479104552993005": {
            "length": 60,
            "waveforms": {
                "single": "3939479104552993005",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5365517015337133700": {
            "length": 60,
            "waveforms": {
                "single": "5365517015337133700",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3883778760335706039": {
            "length": 60,
            "waveforms": {
                "single": "3883778760335706039",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "688593264488003027": {
            "length": 64,
            "waveforms": {
                "single": "688593264488003027",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7784770762539015811": {
            "length": 64,
            "waveforms": {
                "single": "7784770762539015811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6854801404927912154": {
            "length": 64,
            "waveforms": {
                "single": "-6854801404927912154",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2733638425359546240": {
            "length": 64,
            "waveforms": {
                "single": "-2733638425359546240",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8962382596603343028": {
            "length": 68,
            "waveforms": {
                "single": "8962382596603343028",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2010173403929172324": {
            "length": 68,
            "waveforms": {
                "single": "2010173403929172324",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5583369474902898816": {
            "length": 68,
            "waveforms": {
                "single": "-5583369474902898816",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3492787228084959522": {
            "length": 68,
            "waveforms": {
                "single": "3492787228084959522",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8015104998174962838": {
            "length": 72,
            "waveforms": {
                "single": "8015104998174962838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2566459470106805997": {
            "length": 72,
            "waveforms": {
                "single": "2566459470106805997",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5198429258507824432": {
            "length": 72,
            "waveforms": {
                "single": "-5198429258507824432",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "365861775125604732": {
            "length": 72,
            "waveforms": {
                "single": "365861775125604732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4888179545215608048": {
            "length": 76,
            "waveforms": {
                "single": "4888179545215608048",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2951399686501880381": {
            "length": 76,
            "waveforms": {
                "single": "2951399686501880381",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8227821039374099162": {
            "length": 76,
            "waveforms": {
                "single": "-8227821039374099162",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5149159374505047244": {
            "length": 76,
            "waveforms": {
                "single": "5149159374505047244",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6030061351370932299": {
            "length": 80,
            "waveforms": {
                "single": "-6030061351370932299",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1507743581280928983": {
            "length": 80,
            "waveforms": {
                "single": "-1507743581280928983",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7842880822979024778": {
            "length": 80,
            "waveforms": {
                "single": "-7842880822979024778",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-308019125224147180": {
            "length": 40,
            "waveforms": {
                "I": "-308019125224147180_i",
                "Q": "-308019125224147180_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8186088124261017379": {
            "length": 40,
            "waveforms": {
                "I": "8186088124261017379_i",
                "Q": "8186088124261017379_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-1069109754447709049_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1069109754447709049_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1341965726168687049": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6593246697725380560_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-6593246697725380560_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7424997495037455510_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7424997495037455510_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3434336377218927642_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "3434336377218927642_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "623106286188913445": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "844600345387628693": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9050129634614620472": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3042360033390795556": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "689994364628501336": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8275569850417559902": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5923204181655265682": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3447383189066427596": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8120963869658432545": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8342457928857147793": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6308144398050340066": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6529638457249055314": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8505904086053506929": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8727398145252222177": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8948892204450937425": {
            "type": "constant",
            "sample": 0.25,
        },
        "-87778728446196965": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5476512305187232199": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2288376423427398230": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2066882364228682982": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3214704181405551755": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "130877323774483881": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6082946580781021831": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8684299549923935261": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8462805490725220013": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1402309253799497219": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4932827987898598576": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-410510217808595260": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1031835985695288804": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5087433968657725933": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2008743529393286851": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5584799349438784289": {
            "type": "constant",
            "sample": 0.25,
        },
        "7241953346420051197": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4917395264333214744": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2565029595570920524": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-801501750059341777": {
            "type": "constant",
            "sample": 0.25,
        },
        "-580007690860626529": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6126186891021863430": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8450744973108699883": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1354567475057687099": {
            "type": "constant",
            "sample": 0.25,
        },
        "6850961814169304680": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7072455873368019928": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1509173455816814456": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3445953314530542123": {
            "type": "constant",
            "sample": 0.25,
        },
        "3724036361209949890": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3943318695311600479": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1124233239421740072": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6143290108411832001": {
            "type": "constant",
            "sample": 0.25,
        },
        "4206510249698104334": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8728828019788107650": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6404269937701271197": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6528230324806906385": {
            "type": "constant",
            "sample": 0.25,
        },
        "1079584796738749544": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3554538888157918621": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3277344484741916407": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4390010571779633962": {
            "type": "constant",
            "sample": 0.25,
        },
        "132307198310369354": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3939479104552993005": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5365517015337133700": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3883778760335706039": {
            "type": "constant",
            "sample": 0.25,
        },
        "688593264488003027": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7784770762539015811": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6854801404927912154": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2733638425359546240": {
            "type": "constant",
            "sample": 0.25,
        },
        "8962382596603343028": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2010173403929172324": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5583369474902898816": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3492787228084959522": {
            "type": "constant",
            "sample": 0.25,
        },
        "8015104998174962838": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2566459470106805997": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5198429258507824432": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "365861775125604732": {
            "type": "constant",
            "sample": 0.25,
        },
        "4888179545215608048": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2951399686501880381": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8227821039374099162": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5149159374505047244": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6030061351370932299": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1507743581280928983": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7842880822979024778": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-308019125224147180_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-308019125224147180_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8186088124261017379_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8186088124261017379_q": {
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
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
        "B4/drive_mixer_326": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e8f": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_f88": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_3ce": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

