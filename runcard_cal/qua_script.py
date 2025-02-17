
# Single QUA script generated at 2025-02-17 10:48:35.694948
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
    v8 = declare(int, )
    v9 = declare(fixed, )
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
    with for_(v1,0,(v1<256),(v1+1)):
        with for_(v8,0,(v8<=29),(v8+1)):
            with for_(v9,-1.99,(v9<-1.7503877551020408),(v9+0.00812244897959169)):
                align()
                play("-6505792225122809895", "B2/drive")
                play("985987783117036846", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("8822842886667096148"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("6470477217904801928"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("462707616680977012"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("4269879522923600663"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("5695917433707741358"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-4545297350774818479"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-6027035605776246140"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-2347537662771651616"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("-2126043603572936368"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("3728491981340521522"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("3107166213453827978"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("1625427958452400317"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("5304925901456994841"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("5526419960655710089"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-2667431145156015509"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("9056397463482331526"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-4868028840137216774"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("5911360177050784473"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("3558994508288490253"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-2448775092935334663"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("2660474336985794495"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("7182792107075797811"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-4882920332430120686"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("4982194412094596546"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-8844698219431871694"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-5037526313189248043"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-3611488402405107348"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-1507548810362626606"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-8459758003036797310"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("2393443191840683166"*amp(v9), "B4/flux")
                wait(11, "B2/acquisition")
                wait(11, "B4/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B2/acquisition")
                with else_():
                    wait((v8/4), "B2/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B4/acquisition")
                with else_():
                    wait((v8/4), "B4/acquisition")
                wait(4, "B2/acquisition")
                wait(4, "B4/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B4/drive")
                with else_():
                    wait((v8/4), "B4/drive")
                wait(4, "B4/drive")
                wait(11, "B2/acquisition")
                wait(11, "B4/acquisition")
                play("985987783117036846", "B4/drive")
                measure("6365126356243713246", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("3197038210510779678", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(30).buffer(30).average().save("6365126356243713246_B2|acquisition_shots")
        r2.buffer(30).buffer(30).average().save("3197038210510779678_B4|acquisition_shots")


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
                "4529252647436585271": "4529252647436585271",
                "-3226548186010032964": "-3226548186010032964",
                "8822842886667096148": "8822842886667096148",
                "6470477217904801928": "6470477217904801928",
                "462707616680977012": "462707616680977012",
                "4269879522923600663": "4269879522923600663",
                "5695917433707741358": "5695917433707741358",
                "-4545297350774818479": "-4545297350774818479",
                "-6027035605776246140": "-6027035605776246140",
                "-2347537662771651616": "-2347537662771651616",
                "-2126043603572936368": "-2126043603572936368",
                "3728491981340521522": "3728491981340521522",
                "3107166213453827978": "3107166213453827978",
                "1625427958452400317": "1625427958452400317",
                "5304925901456994841": "5304925901456994841",
                "5526419960655710089": "5526419960655710089",
                "-2667431145156015509": "-2667431145156015509",
                "9056397463482331526": "9056397463482331526",
                "-4868028840137216774": "-4868028840137216774",
                "5911360177050784473": "5911360177050784473",
                "3558994508288490253": "3558994508288490253",
                "-2448775092935334663": "-2448775092935334663",
                "2660474336985794495": "2660474336985794495",
                "7182792107075797811": "7182792107075797811",
                "-4882920332430120686": "-4882920332430120686",
                "4982194412094596546": "4982194412094596546",
                "-8844698219431871694": "-8844698219431871694",
                "-5037526313189248043": "-5037526313189248043",
                "-3611488402405107348": "-3611488402405107348",
                "-1507548810362626606": "-1507548810362626606",
                "-8459758003036797310": "-8459758003036797310",
                "2393443191840683166": "2393443191840683166",
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
                "3197038210510779678": "3197038210510779678_B4/acquisition",
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
                "-6505792225122809895": "-6505792225122809895",
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
                "6365126356243713246": "6365126356243713246_B2/acquisition",
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
                "985987783117036846": "985987783117036846",
            },
        },
    },
    "pulses": {
        "-6505792225122809895": {
            "length": 40,
            "waveforms": {
                "I": "-6505792225122809895_i",
                "Q": "-6505792225122809895_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "985987783117036846": {
            "length": 40,
            "waveforms": {
                "I": "985987783117036846_i",
                "Q": "985987783117036846_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4529252647436585271": {
            "length": 32,
            "waveforms": {
                "single": "4529252647436585271",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6365126356243713246_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3493967330597264733_i",
                "Q": "-3493967330597264733_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "3197038210510779678_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1741046487932640473_i",
                "Q": "1741046487932640473_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-3226548186010032964": {
            "length": 32,
            "waveforms": {
                "single": "-3226548186010032964",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8822842886667096148": {
            "length": 16,
            "waveforms": {
                "single": "8822842886667096148",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6470477217904801928": {
            "length": 16,
            "waveforms": {
                "single": "6470477217904801928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "462707616680977012": {
            "length": 16,
            "waveforms": {
                "single": "462707616680977012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4269879522923600663": {
            "length": 16,
            "waveforms": {
                "single": "4269879522923600663",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5695917433707741358": {
            "length": 16,
            "waveforms": {
                "single": "5695917433707741358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4545297350774818479": {
            "length": 16,
            "waveforms": {
                "single": "-4545297350774818479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6027035605776246140": {
            "length": 16,
            "waveforms": {
                "single": "-6027035605776246140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2347537662771651616": {
            "length": 16,
            "waveforms": {
                "single": "-2347537662771651616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2126043603572936368": {
            "length": 16,
            "waveforms": {
                "single": "-2126043603572936368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3728491981340521522": {
            "length": 16,
            "waveforms": {
                "single": "3728491981340521522",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3107166213453827978": {
            "length": 16,
            "waveforms": {
                "single": "3107166213453827978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1625427958452400317": {
            "length": 16,
            "waveforms": {
                "single": "1625427958452400317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5304925901456994841": {
            "length": 16,
            "waveforms": {
                "single": "5304925901456994841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5526419960655710089": {
            "length": 16,
            "waveforms": {
                "single": "5526419960655710089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2667431145156015509": {
            "length": 16,
            "waveforms": {
                "single": "-2667431145156015509",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9056397463482331526": {
            "length": 16,
            "waveforms": {
                "single": "9056397463482331526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4868028840137216774": {
            "length": 16,
            "waveforms": {
                "single": "-4868028840137216774",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5911360177050784473": {
            "length": 20,
            "waveforms": {
                "single": "5911360177050784473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3558994508288490253": {
            "length": 20,
            "waveforms": {
                "single": "3558994508288490253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2448775092935334663": {
            "length": 20,
            "waveforms": {
                "single": "-2448775092935334663",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2660474336985794495": {
            "length": 20,
            "waveforms": {
                "single": "2660474336985794495",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7182792107075797811": {
            "length": 24,
            "waveforms": {
                "single": "7182792107075797811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4882920332430120686": {
            "length": 24,
            "waveforms": {
                "single": "-4882920332430120686",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4982194412094596546": {
            "length": 24,
            "waveforms": {
                "single": "4982194412094596546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8844698219431871694": {
            "length": 24,
            "waveforms": {
                "single": "-8844698219431871694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5037526313189248043": {
            "length": 28,
            "waveforms": {
                "single": "-5037526313189248043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3611488402405107348": {
            "length": 28,
            "waveforms": {
                "single": "-3611488402405107348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1507548810362626606": {
            "length": 28,
            "waveforms": {
                "single": "-1507548810362626606",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8459758003036797310": {
            "length": 28,
            "waveforms": {
                "single": "-8459758003036797310",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2393443191840683166": {
            "length": 32,
            "waveforms": {
                "single": "2393443191840683166",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6505792225122809895_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-6505792225122809895_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "985987783117036846_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "985987783117036846_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "4529252647436585271": {
            "samples": [-0.2388] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3493967330597264733_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-3493967330597264733_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1741046487932640473_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1741046487932640473_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3226548186010032964": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8822842886667096148": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "6470477217904801928": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "462707616680977012": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4269879522923600663": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "5695917433707741358": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-4545297350774818479": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-6027035605776246140": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-2347537662771651616": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-2126043603572936368": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3728491981340521522": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3107166213453827978": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "1625427958452400317": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5304925901456994841": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "5526419960655710089": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2667431145156015509": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9056397463482331526": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-4868028840137216774": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5911360177050784473": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3558994508288490253": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2448775092935334663": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "2660474336985794495": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7182792107075797811": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4882920332430120686": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4982194412094596546": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8844698219431871694": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5037526313189248043": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3611488402405107348": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1507548810362626606": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-8459758003036797310": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2393443191840683166": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
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
                "4529252647436585271": "4529252647436585271",
                "-3226548186010032964": "-3226548186010032964",
                "8822842886667096148": "8822842886667096148",
                "6470477217904801928": "6470477217904801928",
                "462707616680977012": "462707616680977012",
                "4269879522923600663": "4269879522923600663",
                "5695917433707741358": "5695917433707741358",
                "-4545297350774818479": "-4545297350774818479",
                "-6027035605776246140": "-6027035605776246140",
                "-2347537662771651616": "-2347537662771651616",
                "-2126043603572936368": "-2126043603572936368",
                "3728491981340521522": "3728491981340521522",
                "3107166213453827978": "3107166213453827978",
                "1625427958452400317": "1625427958452400317",
                "5304925901456994841": "5304925901456994841",
                "5526419960655710089": "5526419960655710089",
                "-2667431145156015509": "-2667431145156015509",
                "9056397463482331526": "9056397463482331526",
                "-4868028840137216774": "-4868028840137216774",
                "5911360177050784473": "5911360177050784473",
                "3558994508288490253": "3558994508288490253",
                "-2448775092935334663": "-2448775092935334663",
                "2660474336985794495": "2660474336985794495",
                "7182792107075797811": "7182792107075797811",
                "-4882920332430120686": "-4882920332430120686",
                "4982194412094596546": "4982194412094596546",
                "-8844698219431871694": "-8844698219431871694",
                "-5037526313189248043": "-5037526313189248043",
                "-3611488402405107348": "-3611488402405107348",
                "-1507548810362626606": "-1507548810362626606",
                "-8459758003036797310": "-8459758003036797310",
                "2393443191840683166": "2393443191840683166",
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
                "3197038210510779678": "3197038210510779678_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_b03",
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
                "-6505792225122809895": "-6505792225122809895",
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
                "mixer": "B2/drive_mixer_c97",
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
                "6365126356243713246": "6365126356243713246_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_511",
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
                "985987783117036846": "985987783117036846",
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
                "mixer": "B4/drive_mixer_2a0",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "-6505792225122809895": {
            "length": 40,
            "waveforms": {
                "I": "-6505792225122809895_i",
                "Q": "-6505792225122809895_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "985987783117036846": {
            "length": 40,
            "waveforms": {
                "I": "985987783117036846_i",
                "Q": "985987783117036846_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4529252647436585271": {
            "length": 32,
            "waveforms": {
                "single": "4529252647436585271",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6365126356243713246_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3493967330597264733_i",
                "Q": "-3493967330597264733_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3197038210510779678_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1741046487932640473_i",
                "Q": "1741046487932640473_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-3226548186010032964": {
            "length": 32,
            "waveforms": {
                "single": "-3226548186010032964",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8822842886667096148": {
            "length": 16,
            "waveforms": {
                "single": "8822842886667096148",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6470477217904801928": {
            "length": 16,
            "waveforms": {
                "single": "6470477217904801928",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "462707616680977012": {
            "length": 16,
            "waveforms": {
                "single": "462707616680977012",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4269879522923600663": {
            "length": 16,
            "waveforms": {
                "single": "4269879522923600663",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5695917433707741358": {
            "length": 16,
            "waveforms": {
                "single": "5695917433707741358",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4545297350774818479": {
            "length": 16,
            "waveforms": {
                "single": "-4545297350774818479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6027035605776246140": {
            "length": 16,
            "waveforms": {
                "single": "-6027035605776246140",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2347537662771651616": {
            "length": 16,
            "waveforms": {
                "single": "-2347537662771651616",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2126043603572936368": {
            "length": 16,
            "waveforms": {
                "single": "-2126043603572936368",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3728491981340521522": {
            "length": 16,
            "waveforms": {
                "single": "3728491981340521522",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3107166213453827978": {
            "length": 16,
            "waveforms": {
                "single": "3107166213453827978",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1625427958452400317": {
            "length": 16,
            "waveforms": {
                "single": "1625427958452400317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5304925901456994841": {
            "length": 16,
            "waveforms": {
                "single": "5304925901456994841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5526419960655710089": {
            "length": 16,
            "waveforms": {
                "single": "5526419960655710089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2667431145156015509": {
            "length": 16,
            "waveforms": {
                "single": "-2667431145156015509",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9056397463482331526": {
            "length": 16,
            "waveforms": {
                "single": "9056397463482331526",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4868028840137216774": {
            "length": 16,
            "waveforms": {
                "single": "-4868028840137216774",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5911360177050784473": {
            "length": 20,
            "waveforms": {
                "single": "5911360177050784473",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3558994508288490253": {
            "length": 20,
            "waveforms": {
                "single": "3558994508288490253",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2448775092935334663": {
            "length": 20,
            "waveforms": {
                "single": "-2448775092935334663",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2660474336985794495": {
            "length": 20,
            "waveforms": {
                "single": "2660474336985794495",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7182792107075797811": {
            "length": 24,
            "waveforms": {
                "single": "7182792107075797811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4882920332430120686": {
            "length": 24,
            "waveforms": {
                "single": "-4882920332430120686",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4982194412094596546": {
            "length": 24,
            "waveforms": {
                "single": "4982194412094596546",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8844698219431871694": {
            "length": 24,
            "waveforms": {
                "single": "-8844698219431871694",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5037526313189248043": {
            "length": 28,
            "waveforms": {
                "single": "-5037526313189248043",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3611488402405107348": {
            "length": 28,
            "waveforms": {
                "single": "-3611488402405107348",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1507548810362626606": {
            "length": 28,
            "waveforms": {
                "single": "-1507548810362626606",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8459758003036797310": {
            "length": 28,
            "waveforms": {
                "single": "-8459758003036797310",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2393443191840683166": {
            "length": 32,
            "waveforms": {
                "single": "2393443191840683166",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6505792225122809895_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6505792225122809895_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "985987783117036846_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "985987783117036846_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4529252647436585271": {
            "type": "arbitrary",
            "samples": [-0.2388] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3493967330597264733_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-3493967330597264733_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "1741046487932640473_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "1741046487932640473_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-3226548186010032964": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8822842886667096148": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6470477217904801928": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "462707616680977012": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4269879522923600663": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5695917433707741358": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4545297350774818479": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6027035605776246140": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2347537662771651616": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2126043603572936368": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3728491981340521522": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3107166213453827978": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1625427958452400317": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5304925901456994841": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5526419960655710089": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2667431145156015509": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9056397463482331526": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4868028840137216774": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "5911360177050784473": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3558994508288490253": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2448775092935334663": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2660474336985794495": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "7182792107075797811": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4882920332430120686": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4982194412094596546": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8844698219431871694": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-5037526313189248043": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3611488402405107348": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1507548810362626606": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8459758003036797310": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2393443191840683166": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
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
        "B4/acquisition_mixer_b03": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_c97": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_511": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_2a0": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

