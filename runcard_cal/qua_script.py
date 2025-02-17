
# Single QUA script generated at 2025-02-17 10:30:40.955648
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
        play("-2354613406783457647", "B1/drive")
        wait(11, "B1/flux")
        play("-5164231575784986073", "B1/flux")
        wait(46, "B1/drive")
        play("-1593522777559895778", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-4747100868628417094", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5483356870324712)-(v3*0.8362583179416679))>0.00093444036162157)))
        r1 = declare_stream()
        save(v4, r1)
        play("-6711479644690923573", "B2/drive")
        wait(11, "B2/flux")
        play("-5164231575784986073", "B2/flux")
        wait(46, "B2/drive")
        play("-5950389015467361704", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-252215646423150043", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.09731529092164046)-(v6*0.9952536029338636))>0.0025353352631284497)))
        r2 = declare_stream()
        save(v7, r2)
        play("-7998235934773781925", "B3/drive")
        wait(11, "B3/flux")
        play("-5164231575784986073", "B3/flux")
        wait(46, "B3/drive")
        play("-7237145305550220056", "B3/drive")
        wait(66, "B3/acquisition")
        measure("723928482234017084", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*0.8469578382341241)-(v9*-0.5316600608036861))>0.002688936097532602)))
        r3 = declare_stream()
        save(v10, r3)
        play("7907183805157722526", "B4/drive")
        wait(11, "B4/flux")
        play("-5164231575784986073", "B4/flux")
        wait(46, "B4/drive")
        play("8668274434381284395", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2368003860432725605", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.6950813396651986)-(v12*0.7189311032701484))>-0.0004550735732190301)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B1/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B1/drive")
        wait(25501, "B3/drive")
        play("-2354613406783457647", "B1/drive")
        wait(11, "B1/flux")
        play("-641913805694982757", "B1/flux")
        wait(46, "B1/drive")
        play("-1593522777559895778", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-4747100868628417094", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.5483356870324712)-(v3*0.8362583179416679))>0.00093444036162157)))
        save(v4, r1)
        play("-6711479644690923573", "B2/drive")
        wait(11, "B2/flux")
        play("-641913805694982757", "B2/flux")
        wait(46, "B2/drive")
        play("-5950389015467361704", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-252215646423150043", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.09731529092164046)-(v6*0.9952536029338636))>0.0025353352631284497)))
        save(v7, r2)
        play("-7998235934773781925", "B3/drive")
        wait(11, "B3/flux")
        play("-641913805694982757", "B3/flux")
        wait(46, "B3/drive")
        play("-7237145305550220056", "B3/drive")
        wait(66, "B3/acquisition")
        measure("723928482234017084", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*0.8469578382341241)-(v9*-0.5316600608036861))>0.002688936097532602)))
        save(v10, r3)
        play("7907183805157722526", "B4/drive")
        wait(11, "B4/flux")
        play("-641913805694982757", "B4/flux")
        wait(46, "B4/drive")
        play("8668274434381284395", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2368003860432725605", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.6950813396651986)-(v12*0.7189311032701484))>-0.0004550735732190301)))
        save(v13, r4)
        wait(25001, "B1/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B1/drive")
        wait(25501, "B3/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-4747100868628417094_B1|acquisition_shots")
        r2.buffer(2).average().save("-252215646423150043_B2|acquisition_shots")
        r3.buffer(2).average().save("723928482234017084_B3|acquisition_shots")
        r4.buffer(2).average().save("2368003860432725605_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.25498290735703955,
                    "filter": {
                        "feedforward": [1.073483674412824, -0.9746605178140618, -0.0005788121721606197, -0.0005721086498367392, -0.00045443584023824486, -0.004385146292438151, -0.0025823342372732812, 0.0030451940282361792, -0.001889700339078247, -0.00024717946201970216, 0.007068307691352314, 0.009978794061989404, -0.00010513400279432011, -0.002614914077736264, 0.002338930951969912, -0.00529420329574229, -0.0016563838124200722, -0.008053296545058214, 0.007450077876681683, -0.014781690950292945, 0.012738238811147029],
                        "feedback": [0.9999990463256836, 0.9016625898347228],
                    },
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "filter": {
                        "feedforward": [1.088324875299155, -1.0164205342656114, -0.0007502647105687493, -0.0007354293190837552, 0.00991238072185233, 0.005063423434729827, -0.0014738157055065914, 0.0024660816656615105, -0.012117818907241985, -0.010220102284259746, 0.010487410137584807, 0.006648401372432607, 0.005352068597347453, -0.004142720995940829, -0.0006688401531800611, -0.0028563864805521448, -0.004221372854370943, 0.008828629616057402, -0.002310917744312047, -0.007238419763223331, 0.005032962739300176],
                        "feedback": [0.9999990463256836, 0.9210366888588019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.084296032734946, -1.0068513117441202, -0.00011751784507496414, -0.00011716241209727696, -0.0006355881231904486, -0.006276728889771731, -0.0013607849913455736, 0.0001990771227722227, -0.0032340324425182117, 0.002921659167825443, 0.007588935697048313, 0.006062187980381663, -0.003970953526987554, -0.0035207933459697736, -0.0017826743719087418, -0.0009701548898494506, 0.001772569719450058, -0.003656489437504755, 0.0006423297740897412, -0.0002075748179280728, 0.0021702433977156136],
                        "feedback": [0.9999990463256836, 0.9270242438207087],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.100843885357922, -1.03567888499675, -0.00039222873265418645, -0.000387591295622141, 0.003280224313272736, 8.076075459067492e-05, -0.001368773718612303, -0.002417052276795175, 0.0015183799834316324, -0.0031017183385372567, 0.004918021217332064, 0.006177230532258125, -0.0019391675279114519, -0.0010308933365407152, -0.0023096178494393903, -0.0040692577023951, -0.0011838933990946628, -0.001984322318792394, 0.002298375648484165, 0.002800590335001515, -8.035179671661598e-05],
                        "feedback": [0.9999990463256836, 0.9340137153866903],
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
            "operations": {
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-4747100868628417094": "-4747100868628417094_B1/acquisition",
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
                "-6711479644690923573": "-6711479644690923573",
                "-5950389015467361704": "-5950389015467361704",
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
                "-252215646423150043": "-252215646423150043_B2/acquisition",
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
                "723928482234017084": "723928482234017084_B3/acquisition",
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
                "7907183805157722526": "7907183805157722526",
                "8668274434381284395": "8668274434381284395",
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
                "2368003860432725605": "2368003860432725605_B4/acquisition",
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
                "-2354613406783457647": "-2354613406783457647",
                "-1593522777559895778": "-1593522777559895778",
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
                "-7998235934773781925": "-7998235934773781925",
                "-7237145305550220056": "-7237145305550220056",
            },
        },
    },
    "pulses": {
        "-2354613406783457647": {
            "length": 40,
            "waveforms": {
                "I": "-2354613406783457647_i",
                "Q": "-2354613406783457647_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3744273755251904675": {
            "length": 16,
            "waveforms": {
                "single": "-3744273755251904675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4747100868628417094_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "724180164444884114_i",
                "Q": "724180164444884114_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-6711479644690923573": {
            "length": 40,
            "waveforms": {
                "I": "-6711479644690923573_i",
                "Q": "-6711479644690923573_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-252215646423150043_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8912155245327493631_i",
                "Q": "8912155245327493631_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-7998235934773781925": {
            "length": 40,
            "waveforms": {
                "I": "-7998235934773781925_i",
                "Q": "-7998235934773781925_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "723928482234017084_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1071482118739431084_i",
                "Q": "1071482118739431084_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "7907183805157722526": {
            "length": 40,
            "waveforms": {
                "I": "7907183805157722526_i",
                "Q": "7907183805157722526_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2368003860432725605_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8477029476590526748_i",
                "Q": "8477029476590526748_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-3522779696053189427": {
            "length": 16,
            "waveforms": {
                "single": "-3522779696053189427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1488936061774859671": {
            "length": 16,
            "waveforms": {
                "single": "1488936061774859671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6108787503957943047": {
            "length": 16,
            "waveforms": {
                "single": "6108787503957943047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2472841825226891337": {
            "length": 16,
            "waveforms": {
                "single": "-2472841825226891337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3908189808976741782": {
            "length": 16,
            "waveforms": {
                "single": "3908189808976741782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8528041251159825158": {
            "length": 16,
            "waveforms": {
                "single": "8528041251159825158",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4906987064721677360": {
            "length": 16,
            "waveforms": {
                "single": "-4906987064721677360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6327443556178623893": {
            "length": 16,
            "waveforms": {
                "single": "6327443556178623893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1866407549633101705": {
            "length": 16,
            "waveforms": {
                "single": "-1866407549633101705",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2487733317519795249": {
            "length": 16,
            "waveforms": {
                "single": "-2487733317519795249",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3366802267393662641": {
            "length": 16,
            "waveforms": {
                "single": "3366802267393662641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "552846197568780406": {
            "length": 16,
            "waveforms": {
                "single": "552846197568780406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7040696681263290734": {
            "length": 16,
            "waveforms": {
                "single": "-7040696681263290734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5786056014595544752": {
            "length": 16,
            "waveforms": {
                "single": "5786056014595544752",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4455158769887015085": {
            "length": 16,
            "waveforms": {
                "single": "-4455158769887015085",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7983815702598711615": {
            "length": 20,
            "waveforms": {
                "single": "7983815702598711615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6655756464868216350": {
            "length": 20,
            "waveforms": {
                "single": "-6655756464868216350",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5010124265949723851": {
            "length": 20,
            "waveforms": {
                "single": "5010124265949723851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2975810735142916124": {
            "length": 20,
            "waveforms": {
                "single": "2975810735142916124",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8540101768776345288": {
            "length": 24,
            "waveforms": {
                "single": "8540101768776345288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5384324534843203012": {
            "length": 24,
            "waveforms": {
                "single": "-5384324534843203012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5395064482344798235": {
            "length": 24,
            "waveforms": {
                "single": "5395064482344798235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-151114717816438666": {
            "length": 24,
            "waveforms": {
                "single": "-151114717816438666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2965070787641320901": {
            "length": 28,
            "waveforms": {
                "single": "-2965070787641320901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9146536044370134920": {
            "length": 28,
            "waveforms": {
                "single": "9146536044370134920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2268139029385443445": {
            "length": 28,
            "waveforms": {
                "single": "2268139029385443445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5399216027136106924": {
            "length": 28,
            "waveforms": {
                "single": "-5399216027136106924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4853676940761719094": {
            "length": 32,
            "waveforms": {
                "single": "4853676940761719094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3201456339132940061": {
            "length": 32,
            "waveforms": {
                "single": "-3201456339132940061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2653079245780517829": {
            "length": 32,
            "waveforms": {
                "single": "2653079245780517829",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2874573304979233077": {
            "length": 32,
            "waveforms": {
                "single": "2874573304979233077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2253247537092539533": {
            "length": 36,
            "waveforms": {
                "single": "2253247537092539533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5072332992982399940": {
            "length": 36,
            "waveforms": {
                "single": "5072332992982399940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4451007225095706396": {
            "length": 36,
            "waveforms": {
                "single": "4451007225095706396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3742843880716019202": {
            "length": 36,
            "waveforms": {
                "single": "-3742843880716019202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3521349821517303954": {
            "length": 40,
            "waveforms": {
                "single": "-3521349821517303954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5943441575697220467": {
            "length": 40,
            "waveforms": {
                "single": "-5943441575697220467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1323590133514137091": {
            "length": 40,
            "waveforms": {
                "single": "-1323590133514137091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2483581772728486560": {
            "length": 40,
            "waveforms": {
                "single": "2483581772728486560",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3909619683512627255": {
            "length": 44,
            "waveforms": {
                "single": "3909619683512627255",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2427881428511199594": {
            "length": 44,
            "waveforms": {
                "single": "2427881428511199594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6107379371515794118": {
            "length": 44,
            "waveforms": {
                "single": "6107379371515794118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-643343680230868230": {
            "length": 44,
            "waveforms": {
                "single": "-643343680230868230",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8310698736752418599": {
            "length": 48,
            "waveforms": {
                "single": "-8310698736752418599",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8587893140168420813": {
            "length": 48,
            "waveforms": {
                "single": "-8587893140168420813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-382363850941429034": {
            "length": 48,
            "waveforms": {
                "single": "-382363850941429034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4686901137965111041": {
            "length": 48,
            "waveforms": {
                "single": "-4686901137965111041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7039266806727405261": {
            "length": 52,
            "waveforms": {
                "single": "-7039266806727405261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9073580337534212988": {
            "length": 52,
            "waveforms": {
                "single": "-9073580337534212988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4841507118724238398": {
            "length": 52,
            "waveforms": {
                "single": "-4841507118724238398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7270099713287217423": {
            "length": 52,
            "waveforms": {
                "single": "7270099713287217423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6654326590332330877": {
            "length": 56,
            "waveforms": {
                "single": "-6654326590332330877",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6432832531133615629": {
            "length": 56,
            "waveforms": {
                "single": "-6432832531133615629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4456566902329164014": {
            "length": 56,
            "waveforms": {
                "single": "-4456566902329164014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4235072843130448766": {
            "length": 56,
            "waveforms": {
                "single": "-4235072843130448766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8665492030417865949": {
            "length": 60,
            "waveforms": {
                "single": "8665492030417865949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "998136973896315580": {
            "length": 60,
            "waveforms": {
                "single": "998136973896315580",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6562428007529744744": {
            "length": 60,
            "waveforms": {
                "single": "6562428007529744744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3195896661899482443": {
            "length": 60,
            "waveforms": {
                "single": "3195896661899482443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3417390721098197691": {
            "length": 64,
            "waveforms": {
                "single": "3417390721098197691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2269568903921328918": {
            "length": 64,
            "waveforms": {
                "single": "2269568903921328918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7101018466800364360": {
            "length": 64,
            "waveforms": {
                "single": "-7101018466800364360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6879524407601649112": {
            "length": 64,
            "waveforms": {
                "single": "-6879524407601649112",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7598383847581422716": {
            "length": 68,
            "waveforms": {
                "single": "-7598383847581422716",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8495994557365834680": {
            "length": 68,
            "waveforms": {
                "single": "8495994557365834680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8218800153949832466": {
            "length": 68,
            "waveforms": {
                "single": "8218800153949832466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "551445097428282097": {
            "length": 68,
            "waveforms": {
                "single": "551445097428282097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5073762867518285413": {
            "length": 72,
            "waveforms": {
                "single": "5073762867518285413",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4452437099631591869": {
            "length": 72,
            "waveforms": {
                "single": "4452437099631591869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4001518266315213388": {
            "length": 72,
            "waveforms": {
                "single": "-4001518266315213388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2575480355531072693": {
            "length": 72,
            "waveforms": {
                "single": "-2575480355531072693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5630048933695919086": {
            "length": 76,
            "waveforms": {
                "single": "5630048933695919086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5720517641962619746": {
            "length": 76,
            "waveforms": {
                "single": "-5720517641962619746",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1913345735719996095": {
            "length": 76,
            "waveforms": {
                "single": "-1913345735719996095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2207817243848369819": {
            "length": 76,
            "waveforms": {
                "single": "2207817243848369819",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "284413952283170768": {
            "length": 80,
            "waveforms": {
                "single": "284413952283170768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5164231575784986073": {
            "length": 80,
            "waveforms": {
                "single": "-5164231575784986073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-641913805694982757": {
            "length": 80,
            "waveforms": {
                "single": "-641913805694982757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1593522777559895778": {
            "length": 40,
            "waveforms": {
                "I": "-1593522777559895778_i",
                "Q": "-1593522777559895778_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5950389015467361704": {
            "length": 40,
            "waveforms": {
                "I": "-5950389015467361704_i",
                "Q": "-5950389015467361704_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7237145305550220056": {
            "length": 40,
            "waveforms": {
                "I": "-7237145305550220056_i",
                "Q": "-7237145305550220056_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8668274434381284395": {
            "length": 40,
            "waveforms": {
                "I": "8668274434381284395_i",
                "Q": "8668274434381284395_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2354613406783457647_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-2354613406783457647_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-3744273755251904675": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "724180164444884114_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "724180164444884114_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6711479644690923573_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-6711479644690923573_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "8912155245327493631_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "8912155245327493631_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7998235934773781925_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-7998235934773781925_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "1071482118739431084_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "1071482118739431084_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7907183805157722526_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "7907183805157722526_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "8477029476590526748_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "8477029476590526748_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3522779696053189427": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "1488936061774859671": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "6108787503957943047": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-2472841825226891337": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "3908189808976741782": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8528041251159825158": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-4906987064721677360": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "6327443556178623893": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-1866407549633101705": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-2487733317519795249": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "3366802267393662641": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "552846197568780406": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7040696681263290734": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5786056014595544752": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-4455158769887015085": {
            "sample": 0.25,
            "type": "constant",
        },
        "7983815702598711615": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6655756464868216350": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5010124265949723851": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "2975810735142916124": {
            "sample": 0.25,
            "type": "constant",
        },
        "8540101768776345288": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5384324534843203012": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5395064482344798235": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-151114717816438666": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2965070787641320901": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9146536044370134920": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2268139029385443445": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5399216027136106924": {
            "sample": 0.25,
            "type": "constant",
        },
        "4853676940761719094": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3201456339132940061": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2653079245780517829": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "2874573304979233077": {
            "sample": 0.25,
            "type": "constant",
        },
        "2253247537092539533": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5072332992982399940": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4451007225095706396": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-3742843880716019202": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3521349821517303954": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5943441575697220467": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1323590133514137091": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "2483581772728486560": {
            "sample": 0.25,
            "type": "constant",
        },
        "3909619683512627255": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2427881428511199594": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6107379371515794118": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-643343680230868230": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8310698736752418599": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8587893140168420813": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-382363850941429034": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-4686901137965111041": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7039266806727405261": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9073580337534212988": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4841507118724238398": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "7270099713287217423": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6654326590332330877": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6432832531133615629": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4456566902329164014": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-4235072843130448766": {
            "sample": 0.25,
            "type": "constant",
        },
        "8665492030417865949": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "998136973896315580": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6562428007529744744": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "3195896661899482443": {
            "sample": 0.25,
            "type": "constant",
        },
        "3417390721098197691": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2269568903921328918": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7101018466800364360": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-6879524407601649112": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7598383847581422716": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8495994557365834680": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8218800153949832466": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "551445097428282097": {
            "sample": 0.25,
            "type": "constant",
        },
        "5073762867518285413": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4452437099631591869": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4001518266315213388": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-2575480355531072693": {
            "sample": 0.25,
            "type": "constant",
        },
        "5630048933695919086": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5720517641962619746": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1913345735719996095": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "2207817243848369819": {
            "sample": 0.25,
            "type": "constant",
        },
        "284413952283170768": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5164231575784986073": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-641913805694982757": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-1593522777559895778_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-1593522777559895778_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-5950389015467361704_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-5950389015467361704_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-7237145305550220056_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-7237145305550220056_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "8668274434381284395_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "8668274434381284395_q": {
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
                        "feedforward": [1.073483674412824, -0.9746605178140618, -0.0005788121721606197, -0.0005721086498367392, -0.00045443584023824486, -0.004385146292438151, -0.0025823342372732812, 0.0030451940282361792, -0.001889700339078247, -0.00024717946201970216, 0.007068307691352314, 0.009978794061989404, -0.00010513400279432011, -0.002614914077736264, 0.002338930951969912, -0.00529420329574229, -0.0016563838124200722, -0.008053296545058214, 0.007450077876681683, -0.014781690950292945, 0.012738238811147029],
                        "feedback": [0.9999990463256836, 0.9016625898347228],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.088324875299155, -1.0164205342656114, -0.0007502647105687493, -0.0007354293190837552, 0.00991238072185233, 0.005063423434729827, -0.0014738157055065914, 0.0024660816656615105, -0.012117818907241985, -0.010220102284259746, 0.010487410137584807, 0.006648401372432607, 0.005352068597347453, -0.004142720995940829, -0.0006688401531800611, -0.0028563864805521448, -0.004221372854370943, 0.008828629616057402, -0.002310917744312047, -0.007238419763223331, 0.005032962739300176],
                        "feedback": [0.9999990463256836, 0.9210366888588019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.084296032734946, -1.0068513117441202, -0.00011751784507496414, -0.00011716241209727696, -0.0006355881231904486, -0.006276728889771731, -0.0013607849913455736, 0.0001990771227722227, -0.0032340324425182117, 0.002921659167825443, 0.007588935697048313, 0.006062187980381663, -0.003970953526987554, -0.0035207933459697736, -0.0017826743719087418, -0.0009701548898494506, 0.001772569719450058, -0.003656489437504755, 0.0006423297740897412, -0.0002075748179280728, 0.0021702433977156136],
                        "feedback": [0.9999990463256836, 0.9270242438207087],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.100843885357922, -1.03567888499675, -0.00039222873265418645, -0.000387591295622141, 0.003280224313272736, 8.076075459067492e-05, -0.001368773718612303, -0.002417052276795175, 0.0015183799834316324, -0.0031017183385372567, 0.004918021217332064, 0.006177230532258125, -0.0019391675279114519, -0.0010308933365407152, -0.0023096178494393903, -0.0040692577023951, -0.0011838933990946628, -0.001984322318792394, 0.002298375648484165, 0.002800590335001515, -8.035179671661598e-05],
                        "feedback": [0.9999990463256836, 0.9340137153866903],
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
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
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
                "3": {
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
            "operations": {
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
            "operations": {
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
                "-5164231575784986073": "-5164231575784986073",
                "-641913805694982757": "-641913805694982757",
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
        "B1/acquisition": {
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
                "-4747100868628417094": "-4747100868628417094_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_a15",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-6711479644690923573": "-6711479644690923573",
                "-5950389015467361704": "-5950389015467361704",
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
                "mixer": "B2/drive_mixer_e4c",
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
                "-252215646423150043": "-252215646423150043_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_7f9",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
        "B3/acquisition": {
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
                "723928482234017084": "723928482234017084_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_be4",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "7907183805157722526": "7907183805157722526",
                "8668274434381284395": "8668274434381284395",
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
                "mixer": "B4/drive_mixer_604",
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
                "2368003860432725605": "2368003860432725605_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e7c",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
        "B1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-2354613406783457647": "-2354613406783457647",
                "-1593522777559895778": "-1593522777559895778",
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
                "I": ('con2', 1, 3),
                "Q": ('con2', 1, 4),
                "mixer": "B1/drive_mixer_444",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
        "B3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-7998235934773781925": "-7998235934773781925",
                "-7237145305550220056": "-7237145305550220056",
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
                "I": ('con3', 1, 1),
                "Q": ('con3', 1, 2),
                "mixer": "B3/drive_mixer_db8",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
    },
    "pulses": {
        "-2354613406783457647": {
            "length": 40,
            "waveforms": {
                "I": "-2354613406783457647_i",
                "Q": "-2354613406783457647_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3744273755251904675": {
            "length": 16,
            "waveforms": {
                "single": "-3744273755251904675",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4747100868628417094_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "724180164444884114_i",
                "Q": "724180164444884114_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6711479644690923573": {
            "length": 40,
            "waveforms": {
                "I": "-6711479644690923573_i",
                "Q": "-6711479644690923573_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-252215646423150043_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8912155245327493631_i",
                "Q": "8912155245327493631_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-7998235934773781925": {
            "length": 40,
            "waveforms": {
                "I": "-7998235934773781925_i",
                "Q": "-7998235934773781925_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "723928482234017084_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1071482118739431084_i",
                "Q": "1071482118739431084_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7907183805157722526": {
            "length": 40,
            "waveforms": {
                "I": "7907183805157722526_i",
                "Q": "7907183805157722526_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2368003860432725605_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8477029476590526748_i",
                "Q": "8477029476590526748_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-3522779696053189427": {
            "length": 16,
            "waveforms": {
                "single": "-3522779696053189427",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1488936061774859671": {
            "length": 16,
            "waveforms": {
                "single": "1488936061774859671",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6108787503957943047": {
            "length": 16,
            "waveforms": {
                "single": "6108787503957943047",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2472841825226891337": {
            "length": 16,
            "waveforms": {
                "single": "-2472841825226891337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3908189808976741782": {
            "length": 16,
            "waveforms": {
                "single": "3908189808976741782",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8528041251159825158": {
            "length": 16,
            "waveforms": {
                "single": "8528041251159825158",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4906987064721677360": {
            "length": 16,
            "waveforms": {
                "single": "-4906987064721677360",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6327443556178623893": {
            "length": 16,
            "waveforms": {
                "single": "6327443556178623893",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1866407549633101705": {
            "length": 16,
            "waveforms": {
                "single": "-1866407549633101705",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2487733317519795249": {
            "length": 16,
            "waveforms": {
                "single": "-2487733317519795249",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3366802267393662641": {
            "length": 16,
            "waveforms": {
                "single": "3366802267393662641",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "552846197568780406": {
            "length": 16,
            "waveforms": {
                "single": "552846197568780406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7040696681263290734": {
            "length": 16,
            "waveforms": {
                "single": "-7040696681263290734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5786056014595544752": {
            "length": 16,
            "waveforms": {
                "single": "5786056014595544752",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4455158769887015085": {
            "length": 16,
            "waveforms": {
                "single": "-4455158769887015085",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7983815702598711615": {
            "length": 20,
            "waveforms": {
                "single": "7983815702598711615",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6655756464868216350": {
            "length": 20,
            "waveforms": {
                "single": "-6655756464868216350",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5010124265949723851": {
            "length": 20,
            "waveforms": {
                "single": "5010124265949723851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2975810735142916124": {
            "length": 20,
            "waveforms": {
                "single": "2975810735142916124",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8540101768776345288": {
            "length": 24,
            "waveforms": {
                "single": "8540101768776345288",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5384324534843203012": {
            "length": 24,
            "waveforms": {
                "single": "-5384324534843203012",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5395064482344798235": {
            "length": 24,
            "waveforms": {
                "single": "5395064482344798235",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-151114717816438666": {
            "length": 24,
            "waveforms": {
                "single": "-151114717816438666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2965070787641320901": {
            "length": 28,
            "waveforms": {
                "single": "-2965070787641320901",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9146536044370134920": {
            "length": 28,
            "waveforms": {
                "single": "9146536044370134920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2268139029385443445": {
            "length": 28,
            "waveforms": {
                "single": "2268139029385443445",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5399216027136106924": {
            "length": 28,
            "waveforms": {
                "single": "-5399216027136106924",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4853676940761719094": {
            "length": 32,
            "waveforms": {
                "single": "4853676940761719094",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3201456339132940061": {
            "length": 32,
            "waveforms": {
                "single": "-3201456339132940061",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2653079245780517829": {
            "length": 32,
            "waveforms": {
                "single": "2653079245780517829",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2874573304979233077": {
            "length": 32,
            "waveforms": {
                "single": "2874573304979233077",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2253247537092539533": {
            "length": 36,
            "waveforms": {
                "single": "2253247537092539533",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5072332992982399940": {
            "length": 36,
            "waveforms": {
                "single": "5072332992982399940",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4451007225095706396": {
            "length": 36,
            "waveforms": {
                "single": "4451007225095706396",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3742843880716019202": {
            "length": 36,
            "waveforms": {
                "single": "-3742843880716019202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3521349821517303954": {
            "length": 40,
            "waveforms": {
                "single": "-3521349821517303954",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5943441575697220467": {
            "length": 40,
            "waveforms": {
                "single": "-5943441575697220467",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1323590133514137091": {
            "length": 40,
            "waveforms": {
                "single": "-1323590133514137091",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2483581772728486560": {
            "length": 40,
            "waveforms": {
                "single": "2483581772728486560",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3909619683512627255": {
            "length": 44,
            "waveforms": {
                "single": "3909619683512627255",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2427881428511199594": {
            "length": 44,
            "waveforms": {
                "single": "2427881428511199594",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6107379371515794118": {
            "length": 44,
            "waveforms": {
                "single": "6107379371515794118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-643343680230868230": {
            "length": 44,
            "waveforms": {
                "single": "-643343680230868230",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8310698736752418599": {
            "length": 48,
            "waveforms": {
                "single": "-8310698736752418599",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8587893140168420813": {
            "length": 48,
            "waveforms": {
                "single": "-8587893140168420813",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-382363850941429034": {
            "length": 48,
            "waveforms": {
                "single": "-382363850941429034",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4686901137965111041": {
            "length": 48,
            "waveforms": {
                "single": "-4686901137965111041",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7039266806727405261": {
            "length": 52,
            "waveforms": {
                "single": "-7039266806727405261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9073580337534212988": {
            "length": 52,
            "waveforms": {
                "single": "-9073580337534212988",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4841507118724238398": {
            "length": 52,
            "waveforms": {
                "single": "-4841507118724238398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7270099713287217423": {
            "length": 52,
            "waveforms": {
                "single": "7270099713287217423",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6654326590332330877": {
            "length": 56,
            "waveforms": {
                "single": "-6654326590332330877",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6432832531133615629": {
            "length": 56,
            "waveforms": {
                "single": "-6432832531133615629",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4456566902329164014": {
            "length": 56,
            "waveforms": {
                "single": "-4456566902329164014",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4235072843130448766": {
            "length": 56,
            "waveforms": {
                "single": "-4235072843130448766",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8665492030417865949": {
            "length": 60,
            "waveforms": {
                "single": "8665492030417865949",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "998136973896315580": {
            "length": 60,
            "waveforms": {
                "single": "998136973896315580",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6562428007529744744": {
            "length": 60,
            "waveforms": {
                "single": "6562428007529744744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3195896661899482443": {
            "length": 60,
            "waveforms": {
                "single": "3195896661899482443",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3417390721098197691": {
            "length": 64,
            "waveforms": {
                "single": "3417390721098197691",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2269568903921328918": {
            "length": 64,
            "waveforms": {
                "single": "2269568903921328918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7101018466800364360": {
            "length": 64,
            "waveforms": {
                "single": "-7101018466800364360",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6879524407601649112": {
            "length": 64,
            "waveforms": {
                "single": "-6879524407601649112",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7598383847581422716": {
            "length": 68,
            "waveforms": {
                "single": "-7598383847581422716",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8495994557365834680": {
            "length": 68,
            "waveforms": {
                "single": "8495994557365834680",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8218800153949832466": {
            "length": 68,
            "waveforms": {
                "single": "8218800153949832466",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "551445097428282097": {
            "length": 68,
            "waveforms": {
                "single": "551445097428282097",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5073762867518285413": {
            "length": 72,
            "waveforms": {
                "single": "5073762867518285413",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4452437099631591869": {
            "length": 72,
            "waveforms": {
                "single": "4452437099631591869",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4001518266315213388": {
            "length": 72,
            "waveforms": {
                "single": "-4001518266315213388",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2575480355531072693": {
            "length": 72,
            "waveforms": {
                "single": "-2575480355531072693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5630048933695919086": {
            "length": 76,
            "waveforms": {
                "single": "5630048933695919086",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5720517641962619746": {
            "length": 76,
            "waveforms": {
                "single": "-5720517641962619746",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1913345735719996095": {
            "length": 76,
            "waveforms": {
                "single": "-1913345735719996095",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2207817243848369819": {
            "length": 76,
            "waveforms": {
                "single": "2207817243848369819",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "284413952283170768": {
            "length": 80,
            "waveforms": {
                "single": "284413952283170768",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5164231575784986073": {
            "length": 80,
            "waveforms": {
                "single": "-5164231575784986073",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-641913805694982757": {
            "length": 80,
            "waveforms": {
                "single": "-641913805694982757",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1593522777559895778": {
            "length": 40,
            "waveforms": {
                "I": "-1593522777559895778_i",
                "Q": "-1593522777559895778_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5950389015467361704": {
            "length": 40,
            "waveforms": {
                "I": "-5950389015467361704_i",
                "Q": "-5950389015467361704_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7237145305550220056": {
            "length": 40,
            "waveforms": {
                "I": "-7237145305550220056_i",
                "Q": "-7237145305550220056_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8668274434381284395": {
            "length": 40,
            "waveforms": {
                "I": "8668274434381284395_i",
                "Q": "8668274434381284395_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-2354613406783457647_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2354613406783457647_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3744273755251904675": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "724180164444884114_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "724180164444884114_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6711479644690923573_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6711479644690923573_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8912155245327493631_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "8912155245327493631_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7998235934773781925_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7998235934773781925_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1071482118739431084_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "1071482118739431084_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7907183805157722526_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7907183805157722526_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8477029476590526748_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "8477029476590526748_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-3522779696053189427": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1488936061774859671": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6108787503957943047": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2472841825226891337": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3908189808976741782": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8528041251159825158": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4906987064721677360": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6327443556178623893": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1866407549633101705": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2487733317519795249": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3366802267393662641": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "552846197568780406": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7040696681263290734": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5786056014595544752": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4455158769887015085": {
            "type": "constant",
            "sample": 0.25,
        },
        "7983815702598711615": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6655756464868216350": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5010124265949723851": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2975810735142916124": {
            "type": "constant",
            "sample": 0.25,
        },
        "8540101768776345288": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5384324534843203012": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5395064482344798235": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-151114717816438666": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2965070787641320901": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9146536044370134920": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2268139029385443445": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5399216027136106924": {
            "type": "constant",
            "sample": 0.25,
        },
        "4853676940761719094": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3201456339132940061": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2653079245780517829": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2874573304979233077": {
            "type": "constant",
            "sample": 0.25,
        },
        "2253247537092539533": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5072332992982399940": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4451007225095706396": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3742843880716019202": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3521349821517303954": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5943441575697220467": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1323590133514137091": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2483581772728486560": {
            "type": "constant",
            "sample": 0.25,
        },
        "3909619683512627255": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2427881428511199594": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6107379371515794118": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-643343680230868230": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8310698736752418599": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8587893140168420813": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-382363850941429034": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4686901137965111041": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7039266806727405261": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9073580337534212988": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4841507118724238398": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7270099713287217423": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6654326590332330877": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6432832531133615629": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4456566902329164014": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4235072843130448766": {
            "type": "constant",
            "sample": 0.25,
        },
        "8665492030417865949": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "998136973896315580": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6562428007529744744": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3195896661899482443": {
            "type": "constant",
            "sample": 0.25,
        },
        "3417390721098197691": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2269568903921328918": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7101018466800364360": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6879524407601649112": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7598383847581422716": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8495994557365834680": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8218800153949832466": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "551445097428282097": {
            "type": "constant",
            "sample": 0.25,
        },
        "5073762867518285413": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4452437099631591869": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4001518266315213388": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2575480355531072693": {
            "type": "constant",
            "sample": 0.25,
        },
        "5630048933695919086": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5720517641962619746": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1913345735719996095": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2207817243848369819": {
            "type": "constant",
            "sample": 0.25,
        },
        "284413952283170768": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5164231575784986073": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-641913805694982757": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1593522777559895778_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1593522777559895778_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5950389015467361704_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5950389015467361704_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7237145305550220056_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7237145305550220056_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8668274434381284395_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8668274434381284395_q": {
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
        "cosine_weights_B1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
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
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B3/acquisition": {
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
        "B1/acquisition_mixer_a15": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_e4c": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_7f9": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_be4": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_604": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e7c": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_444": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_db8": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

