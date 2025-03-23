
# Single QUA script generated at 2025-03-23 18:20:16.302376
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
        play("-8251465818161859114", "B2/drive")
        wait(11, "B2/flux")
        play("476887738981696889", "B2/flux")
        wait(46, "B2/drive")
        play("-7490375188938297245", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8005566326149944339", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.663072853982161)-(v3*0.7485548679368479))>0.002610420407489984)))
        r1 = declare_stream()
        save(v4, r1)
        play("-6803387857311551380", "B4/drive")
        wait(11, "B4/flux")
        play("476887738981696889", "B4/flux")
        wait(46, "B4/drive")
        play("-6042297228087989511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5269791880379929998", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36609480278683737)-(v6*0.9305775601058015))>-0.0006796068024900747)))
        r2 = declare_stream()
        save(v7, r2)
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25537, "B2/flux")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("-8251465818161859114", "B2/drive")
        wait(11, "B2/flux")
        play("698381798180412137", "B2/flux")
        wait(46, "B2/drive")
        play("-7490375188938297245", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8005566326149944339", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.663072853982161)-(v3*0.7485548679368479))>0.002610420407489984)))
        save(v4, r1)
        play("-6803387857311551380", "B4/drive")
        wait(11, "B4/flux")
        play("698381798180412137", "B4/flux")
        wait(46, "B4/drive")
        play("-6042297228087989511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5269791880379929998", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36609480278683737)-(v6*0.9305775601058015))>-0.0006796068024900747)))
        save(v7, r2)
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("-8251465818161859114", "B2/drive")
        wait(11, "B2/flux")
        play("421187394764409923", "B2/flux")
        wait(46, "B2/drive")
        play("-7490375188938297245", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8005566326149944339", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.663072853982161)-(v3*0.7485548679368479))>0.002610420407489984)))
        save(v4, r1)
        play("-6803387857311551380", "B4/drive")
        wait(11, "B4/flux")
        play("421187394764409923", "B4/flux")
        wait(46, "B4/drive")
        play("-6042297228087989511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5269791880379929998", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36609480278683737)-(v6*0.9305775601058015))>-0.0006796068024900747)))
        save(v7, r2)
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("-8251465818161859114", "B2/drive")
        wait(11, "B2/flux")
        play("4228359301007033574", "B2/flux")
        wait(46, "B2/drive")
        play("-7490375188938297245", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8005566326149944339", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.663072853982161)-(v3*0.7485548679368479))>0.002610420407489984)))
        save(v4, r1)
        play("-6803387857311551380", "B4/drive")
        wait(11, "B4/flux")
        play("4228359301007033574", "B4/flux")
        wait(46, "B4/drive")
        play("-6042297228087989511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-5269791880379929998", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.36609480278683737)-(v6*0.9305775601058015))>-0.0006796068024900747)))
        save(v7, r2)
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(4).average().save("8005566326149944339_B2|acquisition_shots")
        r2.buffer(4).average().save("-5269791880379929998_B4|acquisition_shots")


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
            "operations": {
                "476887738981696889": "476887738981696889",
                "698381798180412137": "698381798180412137",
                "421187394764409923": "421187394764409923",
                "4228359301007033574": "4228359301007033574",
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
                "476887738981696889": "476887738981696889",
                "698381798180412137": "698381798180412137",
                "421187394764409923": "421187394764409923",
                "4228359301007033574": "4228359301007033574",
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
                "-5269791880379929998": "-5269791880379929998_B4/acquisition",
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
                "-8251465818161859114": "-8251465818161859114",
                "-7490375188938297245": "-7490375188938297245",
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
                "8005566326149944339": "8005566326149944339_B2/acquisition",
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
                "-6803387857311551380": "-6803387857311551380",
                "-6042297228087989511": "-6042297228087989511",
            },
        },
    },
    "pulses": {
        "-8251465818161859114": {
            "length": 40,
            "waveforms": {
                "I": "-8251465818161859114_i",
                "Q": "-8251465818161859114_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7728663292339031434": {
            "length": 16,
            "waveforms": {
                "single": "-7728663292339031434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8005566326149944339_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7622890777024592091_i",
                "Q": "7622890777024592091_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6803387857311551380": {
            "length": 40,
            "waveforms": {
                "I": "-6803387857311551380_i",
                "Q": "-6803387857311551380_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5269791880379929998_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2941167572504565622_i",
                "Q": "-2941167572504565622_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4049165349334436910": {
            "length": 16,
            "waveforms": {
                "single": "-4049165349334436910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5530903604335864571": {
            "length": 16,
            "waveforms": {
                "single": "-5530903604335864571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5309409545137149323": {
            "length": 16,
            "waveforms": {
                "single": "-5309409545137149323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4100663595675267903": {
            "length": 16,
            "waveforms": {
                "single": "4100663595675267903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4322157654873983151": {
            "length": 16,
            "waveforms": {
                "single": "4322157654873983151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4259471674310851233": {
            "length": 16,
            "waveforms": {
                "single": "-4259471674310851233",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6519917342877150014": {
            "length": 16,
            "waveforms": {
                "single": "6519917342877150014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8119654824589777951": {
            "length": 16,
            "waveforms": {
                "single": "-8119654824589777951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6693616913805637256": {
            "length": 16,
            "waveforms": {
                "single": "-6693616913805637256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8175355168807064917": {
            "length": 16,
            "waveforms": {
                "single": "-8175355168807064917",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3653037398717061601": {
            "length": 16,
            "waveforms": {
                "single": "-3653037398717061601",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7200163796160418875": {
            "length": 16,
            "waveforms": {
                "single": "7200163796160418875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1580172418309702745": {
            "length": 16,
            "waveforms": {
                "single": "1580172418309702745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-744385663777133708": {
            "length": 16,
            "waveforms": {
                "single": "-744385663777133708",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8827326530347250630": {
            "length": 16,
            "waveforms": {
                "single": "-8827326530347250630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6463282678169690229": {
            "length": 20,
            "waveforms": {
                "single": "-6463282678169690229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6241788618970974981": {
            "length": 20,
            "waveforms": {
                "single": "-6241788618970974981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6197185853514751719": {
            "length": 20,
            "waveforms": {
                "single": "6197185853514751719",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4044028930967808118": {
            "length": 20,
            "waveforms": {
                "single": "-4044028930967808118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7016348403168035551": {
            "length": 24,
            "waveforms": {
                "single": "-7016348403168035551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1189180886058956228": {
            "length": 24,
            "waveforms": {
                "single": "1189180886058956228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6753471919692385392": {
            "length": 24,
            "waveforms": {
                "single": "6753471919692385392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7170954383927162908": {
            "length": 24,
            "waveforms": {
                "single": "-7170954383927162908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3608434633260838339": {
            "length": 28,
            "waveforms": {
                "single": "3608434633260838339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8983773855535255387": {
            "length": 28,
            "waveforms": {
                "single": "-8983773855535255387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8841644450287602685": {
            "length": 28,
            "waveforms": {
                "single": "8841644450287602685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7359906195286175024": {
            "length": 28,
            "waveforms": {
                "single": "7359906195286175024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6564520108333373276": {
            "length": 32,
            "waveforms": {
                "single": "-6564520108333373276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7185845876220066820": {
            "length": 32,
            "waveforms": {
                "single": "-7185845876220066820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3067047091677759198": {
            "length": 32,
            "waveforms": {
                "single": "3067047091677759198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "742489009590922745": {
            "length": 32,
            "waveforms": {
                "single": "742489009590922745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "866449396696557933": {
            "length": 36,
            "waveforms": {
                "single": "866449396696557933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5486300838879641309": {
            "length": 36,
            "waveforms": {
                "single": "5486300838879641309",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2107242039952429831": {
            "length": 36,
            "waveforms": {
                "single": "-2107242039952429831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3285703143898440044": {
            "length": 36,
            "waveforms": {
                "single": "3285703143898440044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8394952573819569202": {
            "length": 40,
            "waveforms": {
                "single": "8394952573819569202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5529473729799979098": {
            "length": 40,
            "waveforms": {
                "single": "-5529473729799979098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1722301823557355447": {
            "length": 40,
            "waveforms": {
                "single": "-1722301823557355447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3331714041796812235": {
            "length": 40,
            "waveforms": {
                "single": "-3331714041796812235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1778002167774642413": {
            "length": 44,
            "waveforms": {
                "single": "-1778002167774642413",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "696951923644526664": {
            "length": 44,
            "waveforms": {
                "single": "696951923644526664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2122989834428667359": {
            "length": 44,
            "waveforms": {
                "single": "2122989834428667359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8625286809455516229": {
            "length": 44,
            "waveforms": {
                "single": "8625286809455516229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4320749522431834222": {
            "length": 48,
            "waveforms": {
                "single": "4320749522431834222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1968383853669540002": {
            "length": 48,
            "waveforms": {
                "single": "1968383853669540002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2507930050823741743": {
            "length": 48,
            "waveforms": {
                "single": "2507930050823741743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "155564382061447523": {
            "length": 48,
            "waveforms": {
                "single": "155564382061447523",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2168993700025388930": {
            "length": 52,
            "waveforms": {
                "single": "-2168993700025388930",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2353324070064614386": {
            "length": 52,
            "waveforms": {
                "single": "2353324070064614386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1731998302177920842": {
            "length": 52,
            "waveforms": {
                "single": "1731998302177920842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7586533887091378732": {
            "length": 52,
            "waveforms": {
                "single": "7586533887091378732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5295919152984743720": {
            "length": 56,
            "waveforms": {
                "single": "-5295919152984743720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5483469864203257527": {
            "length": 56,
            "waveforms": {
                "single": "5483469864203257527",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8440956439416290773": {
            "length": 56,
            "waveforms": {
                "single": "-8440956439416290773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9062282207302984317": {
            "length": 56,
            "waveforms": {
                "single": "-9062282207302984317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6243196751413123910": {
            "length": 60,
            "waveforms": {
                "single": "-6243196751413123910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-291127494406585960": {
            "length": 60,
            "waveforms": {
                "single": "-291127494406585960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1009986934386359564": {
            "length": 60,
            "waveforms": {
                "single": "-1009986934386359564",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-788492875187644316": {
            "length": 60,
            "waveforms": {
                "single": "-788492875187644316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2128126252795296151": {
            "length": 64,
            "waveforms": {
                "single": "2128126252795296151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7139842010623345249": {
            "length": 64,
            "waveforms": {
                "single": "7139842010623345249",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7361336069822060497": {
            "length": 64,
            "waveforms": {
                "single": "7361336069822060497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6642476629842286893": {
            "length": 64,
            "waveforms": {
                "single": "6642476629842286893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8887648315884324256": {
            "length": 68,
            "waveforms": {
                "single": "-8887648315884324256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4365330545794320940": {
            "length": 68,
            "waveforms": {
                "single": "-4365330545794320940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3654438498857559910": {
            "length": 68,
            "waveforms": {
                "single": "-3654438498857559910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1179484407438390833": {
            "length": 68,
            "waveforms": {
                "single": "-1179484407438390833",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1456678810854393047": {
            "length": 72,
            "waveforms": {
                "single": "-1456678810854393047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3809044479616687267": {
            "length": 72,
            "waveforms": {
                "single": "-3809044479616687267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3287133018434325517": {
            "length": 72,
            "waveforms": {
                "single": "3287133018434325517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7094304924676949168": {
            "length": 72,
            "waveforms": {
                "single": "7094304924676949168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6472979156790255624": {
            "length": 76,
            "waveforms": {
                "single": "6472979156790255624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6195784753374253410": {
            "length": 76,
            "waveforms": {
                "single": "6195784753374253410",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3843419084611959190": {
            "length": 76,
            "waveforms": {
                "single": "3843419084611959190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "476887738981696889": {
            "length": 76,
            "waveforms": {
                "single": "476887738981696889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "698381798180412137": {
            "length": 80,
            "waveforms": {
                "single": "698381798180412137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "421187394764409923": {
            "length": 80,
            "waveforms": {
                "single": "421187394764409923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4228359301007033574": {
            "length": 80,
            "waveforms": {
                "single": "4228359301007033574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7490375188938297245": {
            "length": 40,
            "waveforms": {
                "I": "-7490375188938297245_i",
                "Q": "-7490375188938297245_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6042297228087989511": {
            "length": 40,
            "waveforms": {
                "I": "-6042297228087989511_i",
                "Q": "-6042297228087989511_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8251465818161859114_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-8251465818161859114_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-7728663292339031434": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "7622890777024592091_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "7622890777024592091_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6803387857311551380_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-6803387857311551380_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-2941167572504565622_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-2941167572504565622_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4049165349334436910": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-5530903604335864571": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-5309409545137149323": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "4100663595675267903": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "4322157654873983151": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-4259471674310851233": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "6519917342877150014": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8119654824589777951": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-6693616913805637256": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-8175355168807064917": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-3653037398717061601": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "7200163796160418875": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1580172418309702745": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-744385663777133708": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8827326530347250630": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6463282678169690229": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6241788618970974981": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6197185853514751719": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-4044028930967808118": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7016348403168035551": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1189180886058956228": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6753471919692385392": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-7170954383927162908": {
            "sample": 0.25,
            "type": "constant",
        },
        "3608434633260838339": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8983773855535255387": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8841644450287602685": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "7359906195286175024": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6564520108333373276": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7185845876220066820": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3067047091677759198": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "742489009590922745": {
            "sample": 0.25,
            "type": "constant",
        },
        "866449396696557933": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5486300838879641309": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2107242039952429831": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "3285703143898440044": {
            "sample": 0.25,
            "type": "constant",
        },
        "8394952573819569202": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5529473729799979098": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1722301823557355447": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-3331714041796812235": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1778002167774642413": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "696951923644526664": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2122989834428667359": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "8625286809455516229": {
            "sample": 0.25,
            "type": "constant",
        },
        "4320749522431834222": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1968383853669540002": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2507930050823741743": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "155564382061447523": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2168993700025388930": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2353324070064614386": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1731998302177920842": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "7586533887091378732": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5295919152984743720": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5483469864203257527": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8440956439416290773": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-9062282207302984317": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6243196751413123910": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-291127494406585960": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1009986934386359564": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-788492875187644316": {
            "sample": 0.25,
            "type": "constant",
        },
        "2128126252795296151": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7139842010623345249": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7361336069822060497": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "6642476629842286893": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8887648315884324256": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4365330545794320940": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3654438498857559910": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-1179484407438390833": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1456678810854393047": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3809044479616687267": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3287133018434325517": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "7094304924676949168": {
            "sample": 0.25,
            "type": "constant",
        },
        "6472979156790255624": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6195784753374253410": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3843419084611959190": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "476887738981696889": {
            "sample": 0.25,
            "type": "constant",
        },
        "698381798180412137": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "421187394764409923": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4228359301007033574": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-7490375188938297245_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-7490375188938297245_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-6042297228087989511_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-6042297228087989511_q": {
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
            "operations": {
                "476887738981696889": "476887738981696889",
                "698381798180412137": "698381798180412137",
                "421187394764409923": "421187394764409923",
                "4228359301007033574": "4228359301007033574",
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
                "476887738981696889": "476887738981696889",
                "698381798180412137": "698381798180412137",
                "421187394764409923": "421187394764409923",
                "4228359301007033574": "4228359301007033574",
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
                "-5269791880379929998": "-5269791880379929998_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_1bf",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-8251465818161859114": "-8251465818161859114",
                "-7490375188938297245": "-7490375188938297245",
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
                "mixer": "B2/drive_mixer_a8f",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "8005566326149944339": "8005566326149944339_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_4b8",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-6803387857311551380": "-6803387857311551380",
                "-6042297228087989511": "-6042297228087989511",
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
                "mixer": "B4/drive_mixer_941",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "-8251465818161859114": {
            "length": 40,
            "waveforms": {
                "I": "-8251465818161859114_i",
                "Q": "-8251465818161859114_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7728663292339031434": {
            "length": 16,
            "waveforms": {
                "single": "-7728663292339031434",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8005566326149944339_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7622890777024592091_i",
                "Q": "7622890777024592091_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6803387857311551380": {
            "length": 40,
            "waveforms": {
                "I": "-6803387857311551380_i",
                "Q": "-6803387857311551380_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5269791880379929998_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2941167572504565622_i",
                "Q": "-2941167572504565622_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4049165349334436910": {
            "length": 16,
            "waveforms": {
                "single": "-4049165349334436910",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5530903604335864571": {
            "length": 16,
            "waveforms": {
                "single": "-5530903604335864571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5309409545137149323": {
            "length": 16,
            "waveforms": {
                "single": "-5309409545137149323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4100663595675267903": {
            "length": 16,
            "waveforms": {
                "single": "4100663595675267903",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4322157654873983151": {
            "length": 16,
            "waveforms": {
                "single": "4322157654873983151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4259471674310851233": {
            "length": 16,
            "waveforms": {
                "single": "-4259471674310851233",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6519917342877150014": {
            "length": 16,
            "waveforms": {
                "single": "6519917342877150014",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8119654824589777951": {
            "length": 16,
            "waveforms": {
                "single": "-8119654824589777951",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6693616913805637256": {
            "length": 16,
            "waveforms": {
                "single": "-6693616913805637256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8175355168807064917": {
            "length": 16,
            "waveforms": {
                "single": "-8175355168807064917",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3653037398717061601": {
            "length": 16,
            "waveforms": {
                "single": "-3653037398717061601",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7200163796160418875": {
            "length": 16,
            "waveforms": {
                "single": "7200163796160418875",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1580172418309702745": {
            "length": 16,
            "waveforms": {
                "single": "1580172418309702745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-744385663777133708": {
            "length": 16,
            "waveforms": {
                "single": "-744385663777133708",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8827326530347250630": {
            "length": 16,
            "waveforms": {
                "single": "-8827326530347250630",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6463282678169690229": {
            "length": 20,
            "waveforms": {
                "single": "-6463282678169690229",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6241788618970974981": {
            "length": 20,
            "waveforms": {
                "single": "-6241788618970974981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6197185853514751719": {
            "length": 20,
            "waveforms": {
                "single": "6197185853514751719",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4044028930967808118": {
            "length": 20,
            "waveforms": {
                "single": "-4044028930967808118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7016348403168035551": {
            "length": 24,
            "waveforms": {
                "single": "-7016348403168035551",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1189180886058956228": {
            "length": 24,
            "waveforms": {
                "single": "1189180886058956228",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6753471919692385392": {
            "length": 24,
            "waveforms": {
                "single": "6753471919692385392",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7170954383927162908": {
            "length": 24,
            "waveforms": {
                "single": "-7170954383927162908",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3608434633260838339": {
            "length": 28,
            "waveforms": {
                "single": "3608434633260838339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8983773855535255387": {
            "length": 28,
            "waveforms": {
                "single": "-8983773855535255387",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8841644450287602685": {
            "length": 28,
            "waveforms": {
                "single": "8841644450287602685",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7359906195286175024": {
            "length": 28,
            "waveforms": {
                "single": "7359906195286175024",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6564520108333373276": {
            "length": 32,
            "waveforms": {
                "single": "-6564520108333373276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7185845876220066820": {
            "length": 32,
            "waveforms": {
                "single": "-7185845876220066820",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3067047091677759198": {
            "length": 32,
            "waveforms": {
                "single": "3067047091677759198",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "742489009590922745": {
            "length": 32,
            "waveforms": {
                "single": "742489009590922745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "866449396696557933": {
            "length": 36,
            "waveforms": {
                "single": "866449396696557933",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5486300838879641309": {
            "length": 36,
            "waveforms": {
                "single": "5486300838879641309",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2107242039952429831": {
            "length": 36,
            "waveforms": {
                "single": "-2107242039952429831",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3285703143898440044": {
            "length": 36,
            "waveforms": {
                "single": "3285703143898440044",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8394952573819569202": {
            "length": 40,
            "waveforms": {
                "single": "8394952573819569202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5529473729799979098": {
            "length": 40,
            "waveforms": {
                "single": "-5529473729799979098",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1722301823557355447": {
            "length": 40,
            "waveforms": {
                "single": "-1722301823557355447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3331714041796812235": {
            "length": 40,
            "waveforms": {
                "single": "-3331714041796812235",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1778002167774642413": {
            "length": 44,
            "waveforms": {
                "single": "-1778002167774642413",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "696951923644526664": {
            "length": 44,
            "waveforms": {
                "single": "696951923644526664",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2122989834428667359": {
            "length": 44,
            "waveforms": {
                "single": "2122989834428667359",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8625286809455516229": {
            "length": 44,
            "waveforms": {
                "single": "8625286809455516229",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4320749522431834222": {
            "length": 48,
            "waveforms": {
                "single": "4320749522431834222",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1968383853669540002": {
            "length": 48,
            "waveforms": {
                "single": "1968383853669540002",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2507930050823741743": {
            "length": 48,
            "waveforms": {
                "single": "2507930050823741743",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "155564382061447523": {
            "length": 48,
            "waveforms": {
                "single": "155564382061447523",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2168993700025388930": {
            "length": 52,
            "waveforms": {
                "single": "-2168993700025388930",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2353324070064614386": {
            "length": 52,
            "waveforms": {
                "single": "2353324070064614386",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1731998302177920842": {
            "length": 52,
            "waveforms": {
                "single": "1731998302177920842",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7586533887091378732": {
            "length": 52,
            "waveforms": {
                "single": "7586533887091378732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5295919152984743720": {
            "length": 56,
            "waveforms": {
                "single": "-5295919152984743720",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5483469864203257527": {
            "length": 56,
            "waveforms": {
                "single": "5483469864203257527",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8440956439416290773": {
            "length": 56,
            "waveforms": {
                "single": "-8440956439416290773",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9062282207302984317": {
            "length": 56,
            "waveforms": {
                "single": "-9062282207302984317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6243196751413123910": {
            "length": 60,
            "waveforms": {
                "single": "-6243196751413123910",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-291127494406585960": {
            "length": 60,
            "waveforms": {
                "single": "-291127494406585960",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1009986934386359564": {
            "length": 60,
            "waveforms": {
                "single": "-1009986934386359564",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-788492875187644316": {
            "length": 60,
            "waveforms": {
                "single": "-788492875187644316",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2128126252795296151": {
            "length": 64,
            "waveforms": {
                "single": "2128126252795296151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7139842010623345249": {
            "length": 64,
            "waveforms": {
                "single": "7139842010623345249",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7361336069822060497": {
            "length": 64,
            "waveforms": {
                "single": "7361336069822060497",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6642476629842286893": {
            "length": 64,
            "waveforms": {
                "single": "6642476629842286893",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8887648315884324256": {
            "length": 68,
            "waveforms": {
                "single": "-8887648315884324256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4365330545794320940": {
            "length": 68,
            "waveforms": {
                "single": "-4365330545794320940",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3654438498857559910": {
            "length": 68,
            "waveforms": {
                "single": "-3654438498857559910",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1179484407438390833": {
            "length": 68,
            "waveforms": {
                "single": "-1179484407438390833",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1456678810854393047": {
            "length": 72,
            "waveforms": {
                "single": "-1456678810854393047",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3809044479616687267": {
            "length": 72,
            "waveforms": {
                "single": "-3809044479616687267",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3287133018434325517": {
            "length": 72,
            "waveforms": {
                "single": "3287133018434325517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7094304924676949168": {
            "length": 72,
            "waveforms": {
                "single": "7094304924676949168",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6472979156790255624": {
            "length": 76,
            "waveforms": {
                "single": "6472979156790255624",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6195784753374253410": {
            "length": 76,
            "waveforms": {
                "single": "6195784753374253410",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3843419084611959190": {
            "length": 76,
            "waveforms": {
                "single": "3843419084611959190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "476887738981696889": {
            "length": 76,
            "waveforms": {
                "single": "476887738981696889",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "698381798180412137": {
            "length": 80,
            "waveforms": {
                "single": "698381798180412137",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "421187394764409923": {
            "length": 80,
            "waveforms": {
                "single": "421187394764409923",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4228359301007033574": {
            "length": 80,
            "waveforms": {
                "single": "4228359301007033574",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7490375188938297245": {
            "length": 40,
            "waveforms": {
                "I": "-7490375188938297245_i",
                "Q": "-7490375188938297245_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6042297228087989511": {
            "length": 40,
            "waveforms": {
                "I": "-6042297228087989511_i",
                "Q": "-6042297228087989511_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-8251465818161859114_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8251465818161859114_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7728663292339031434": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7622890777024592091_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "7622890777024592091_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6803387857311551380_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6803387857311551380_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2941167572504565622_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-2941167572504565622_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4049165349334436910": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5530903604335864571": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5309409545137149323": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4100663595675267903": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4322157654873983151": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4259471674310851233": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6519917342877150014": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8119654824589777951": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6693616913805637256": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8175355168807064917": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3653037398717061601": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7200163796160418875": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1580172418309702745": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-744385663777133708": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8827326530347250630": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6463282678169690229": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6241788618970974981": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6197185853514751719": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4044028930967808118": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7016348403168035551": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1189180886058956228": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6753471919692385392": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7170954383927162908": {
            "type": "constant",
            "sample": 0.25,
        },
        "3608434633260838339": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8983773855535255387": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8841644450287602685": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7359906195286175024": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6564520108333373276": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7185845876220066820": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3067047091677759198": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "742489009590922745": {
            "type": "constant",
            "sample": 0.25,
        },
        "866449396696557933": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5486300838879641309": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2107242039952429831": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3285703143898440044": {
            "type": "constant",
            "sample": 0.25,
        },
        "8394952573819569202": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5529473729799979098": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1722301823557355447": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3331714041796812235": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1778002167774642413": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "696951923644526664": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2122989834428667359": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8625286809455516229": {
            "type": "constant",
            "sample": 0.25,
        },
        "4320749522431834222": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1968383853669540002": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2507930050823741743": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "155564382061447523": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2168993700025388930": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2353324070064614386": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1731998302177920842": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7586533887091378732": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5295919152984743720": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5483469864203257527": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8440956439416290773": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9062282207302984317": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6243196751413123910": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-291127494406585960": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1009986934386359564": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-788492875187644316": {
            "type": "constant",
            "sample": 0.25,
        },
        "2128126252795296151": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7139842010623345249": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7361336069822060497": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6642476629842286893": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8887648315884324256": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4365330545794320940": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3654438498857559910": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1179484407438390833": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1456678810854393047": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3809044479616687267": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3287133018434325517": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7094304924676949168": {
            "type": "constant",
            "sample": 0.25,
        },
        "6472979156790255624": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6195784753374253410": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3843419084611959190": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "476887738981696889": {
            "type": "constant",
            "sample": 0.25,
        },
        "698381798180412137": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "421187394764409923": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4228359301007033574": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7490375188938297245_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7490375188938297245_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6042297228087989511_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6042297228087989511_q": {
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
        "B4/acquisition_mixer_1bf": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_a8f": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_4b8": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_941": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

