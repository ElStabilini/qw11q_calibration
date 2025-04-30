
# Single QUA script generated at 2025-04-30 16:04:21.080434
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
        with for_(v8,0,(v8<=59),(v8+1)):
            with for_(v9,-1.9900000000000002,(v9<-1.79299),(v9+0.003980000000000095)):
                align()
                play("9127992669991711247", "B2/drive")
                play("2522892627134655911", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-7698920818626935174"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-7477426759428219926"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-8518807338412963276"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-8297313279214248028"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-7313980602231860790"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-7092486543033145542"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("6012053240800374656"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-866343774184316819"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("7339185515042674960"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("338482961996785667"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("7283485170825387994"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-2291077110181510767"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-259909498590527187"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-3455094994438230199"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("5417086798264422656"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-414515479349654544"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("5361386454047135690"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("4818694337677109802"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("2216349167615588637"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("7016454025680276665"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("7237948084878991913"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("8221280761861379151"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-1577228788819427229"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-3999320542999343742"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-3777826483800628494"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("2174242773205909456"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-2572999747619526008"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("4372002461209076319"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("1005471115578814018"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("8272994463412386091"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-1301567817594512670"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-6643772107470544088"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6422278048271828840"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("8657934679807460475"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("8879428739006175723"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-695133542000723038"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("1008691456758102369"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("5531009226848105685"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-2136345829673444684"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-4488711498435738904"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-4765905901851741118"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("-2290951810432572041"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-7910943188283288171"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("2942258006594192305"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("1460519751592764644"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("5140017694597359168"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-7354657122105654498"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-4213050527210824345"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("8891489256622695853"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("1939280063948525149"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("5746451970191148800"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("297806442122991959"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("3116891898012852366"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("2495566130126158822"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("7017883900216162138"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-5047828539289756359"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-7898882670666768041"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-7677388611468052793"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-8298714379354746337"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-3776396609264743021"*amp(v9), "B4/flux")
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
                play("2522892627134655911", "B4/drive")
                measure("-2291820121492901667", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("4123035581968125476", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("-2291820121492901667_B2|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("4123035581968125476_B4|acquisition_shots")


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
                "-3181386020522137583": "-3181386020522137583",
                "7002992407923258226": "7002992407923258226",
                "-7698920818626935174": "-7698920818626935174",
                "-7477426759428219926": "-7477426759428219926",
                "-8518807338412963276": "-8518807338412963276",
                "-8297313279214248028": "-8297313279214248028",
                "-7313980602231860790": "-7313980602231860790",
                "-7092486543033145542": "-7092486543033145542",
                "6012053240800374656": "6012053240800374656",
                "-866343774184316819": "-866343774184316819",
                "7339185515042674960": "7339185515042674960",
                "338482961996785667": "338482961996785667",
                "7283485170825387994": "7283485170825387994",
                "-2291077110181510767": "-2291077110181510767",
                "-259909498590527187": "-259909498590527187",
                "-3455094994438230199": "-3455094994438230199",
                "5417086798264422656": "5417086798264422656",
                "-414515479349654544": "-414515479349654544",
                "5361386454047135690": "5361386454047135690",
                "4818694337677109802": "4818694337677109802",
                "2216349167615588637": "2216349167615588637",
                "7016454025680276665": "7016454025680276665",
                "7237948084878991913": "7237948084878991913",
                "8221280761861379151": "8221280761861379151",
                "-1577228788819427229": "-1577228788819427229",
                "-3999320542999343742": "-3999320542999343742",
                "-3777826483800628494": "-3777826483800628494",
                "2174242773205909456": "2174242773205909456",
                "-2572999747619526008": "-2572999747619526008",
                "4372002461209076319": "4372002461209076319",
                "1005471115578814018": "1005471115578814018",
                "8272994463412386091": "8272994463412386091",
                "-1301567817594512670": "-1301567817594512670",
                "-6643772107470544088": "-6643772107470544088",
                "-6422278048271828840": "-6422278048271828840",
                "8657934679807460475": "8657934679807460475",
                "8879428739006175723": "8879428739006175723",
                "-695133542000723038": "-695133542000723038",
                "1008691456758102369": "1008691456758102369",
                "5531009226848105685": "5531009226848105685",
                "-2136345829673444684": "-2136345829673444684",
                "-4488711498435738904": "-4488711498435738904",
                "-4765905901851741118": "-4765905901851741118",
                "-2290951810432572041": "-2290951810432572041",
                "-7910943188283288171": "-7910943188283288171",
                "2942258006594192305": "2942258006594192305",
                "1460519751592764644": "1460519751592764644",
                "5140017694597359168": "5140017694597359168",
                "-7354657122105654498": "-7354657122105654498",
                "-4213050527210824345": "-4213050527210824345",
                "8891489256622695853": "8891489256622695853",
                "1939280063948525149": "1939280063948525149",
                "5746451970191148800": "5746451970191148800",
                "297806442122991959": "297806442122991959",
                "3116891898012852366": "3116891898012852366",
                "2495566130126158822": "2495566130126158822",
                "7017883900216162138": "7017883900216162138",
                "-5047828539289756359": "-5047828539289756359",
                "-7898882670666768041": "-7898882670666768041",
                "-7677388611468052793": "-7677388611468052793",
                "-8298714379354746337": "-8298714379354746337",
                "-3776396609264743021": "-3776396609264743021",
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
                "-2291820121492901667": "-2291820121492901667_B2/acquisition",
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
                "2522892627134655911": "2522892627134655911",
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
                "9127992669991711247": "9127992669991711247",
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
                "4123035581968125476": "4123035581968125476_B4/acquisition",
            },
        },
    },
    "pulses": {
        "9127992669991711247": {
            "length": 40,
            "waveforms": {
                "I": "9127992669991711247_i",
                "Q": "9127992669991711247_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2522892627134655911": {
            "length": 40,
            "waveforms": {
                "I": "2522892627134655911_i",
                "Q": "2522892627134655911_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3181386020522137583": {
            "length": 60,
            "waveforms": {
                "single": "-3181386020522137583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2291820121492901667_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5145608785012429593_i",
                "Q": "5145608785012429593_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "4123035581968125476_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2335546272359394115_i",
                "Q": "-2335546272359394115_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "7002992407923258226": {
            "length": 60,
            "waveforms": {
                "single": "7002992407923258226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7698920818626935174": {
            "length": 16,
            "waveforms": {
                "single": "-7698920818626935174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7477426759428219926": {
            "length": 16,
            "waveforms": {
                "single": "-7477426759428219926",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8518807338412963276": {
            "length": 16,
            "waveforms": {
                "single": "-8518807338412963276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8297313279214248028": {
            "length": 16,
            "waveforms": {
                "single": "-8297313279214248028",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7313980602231860790": {
            "length": 16,
            "waveforms": {
                "single": "-7313980602231860790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7092486543033145542": {
            "length": 16,
            "waveforms": {
                "single": "-7092486543033145542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6012053240800374656": {
            "length": 16,
            "waveforms": {
                "single": "6012053240800374656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-866343774184316819": {
            "length": 16,
            "waveforms": {
                "single": "-866343774184316819",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7339185515042674960": {
            "length": 16,
            "waveforms": {
                "single": "7339185515042674960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "338482961996785667": {
            "length": 16,
            "waveforms": {
                "single": "338482961996785667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7283485170825387994": {
            "length": 16,
            "waveforms": {
                "single": "7283485170825387994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2291077110181510767": {
            "length": 16,
            "waveforms": {
                "single": "-2291077110181510767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-259909498590527187": {
            "length": 16,
            "waveforms": {
                "single": "-259909498590527187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3455094994438230199": {
            "length": 16,
            "waveforms": {
                "single": "-3455094994438230199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5417086798264422656": {
            "length": 16,
            "waveforms": {
                "single": "5417086798264422656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-414515479349654544": {
            "length": 16,
            "waveforms": {
                "single": "-414515479349654544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5361386454047135690": {
            "length": 16,
            "waveforms": {
                "single": "5361386454047135690",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4818694337677109802": {
            "length": 20,
            "waveforms": {
                "single": "4818694337677109802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2216349167615588637": {
            "length": 20,
            "waveforms": {
                "single": "2216349167615588637",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7016454025680276665": {
            "length": 20,
            "waveforms": {
                "single": "7016454025680276665",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7237948084878991913": {
            "length": 20,
            "waveforms": {
                "single": "7237948084878991913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8221280761861379151": {
            "length": 24,
            "waveforms": {
                "single": "8221280761861379151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1577228788819427229": {
            "length": 24,
            "waveforms": {
                "single": "-1577228788819427229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3999320542999343742": {
            "length": 24,
            "waveforms": {
                "single": "-3999320542999343742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3777826483800628494": {
            "length": 24,
            "waveforms": {
                "single": "-3777826483800628494",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2174242773205909456": {
            "length": 28,
            "waveforms": {
                "single": "2174242773205909456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2572999747619526008": {
            "length": 28,
            "waveforms": {
                "single": "-2572999747619526008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4372002461209076319": {
            "length": 28,
            "waveforms": {
                "single": "4372002461209076319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1005471115578814018": {
            "length": 28,
            "waveforms": {
                "single": "1005471115578814018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8272994463412386091": {
            "length": 32,
            "waveforms": {
                "single": "8272994463412386091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1301567817594512670": {
            "length": 32,
            "waveforms": {
                "single": "-1301567817594512670",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6643772107470544088": {
            "length": 32,
            "waveforms": {
                "single": "-6643772107470544088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6422278048271828840": {
            "length": 32,
            "waveforms": {
                "single": "-6422278048271828840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8657934679807460475": {
            "length": 36,
            "waveforms": {
                "single": "8657934679807460475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8879428739006175723": {
            "length": 36,
            "waveforms": {
                "single": "8879428739006175723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-695133542000723038": {
            "length": 36,
            "waveforms": {
                "single": "-695133542000723038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1008691456758102369": {
            "length": 36,
            "waveforms": {
                "single": "1008691456758102369",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5531009226848105685": {
            "length": 40,
            "waveforms": {
                "single": "5531009226848105685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2136345829673444684": {
            "length": 40,
            "waveforms": {
                "single": "-2136345829673444684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4488711498435738904": {
            "length": 40,
            "waveforms": {
                "single": "-4488711498435738904",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4765905901851741118": {
            "length": 40,
            "waveforms": {
                "single": "-4765905901851741118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2290951810432572041": {
            "length": 44,
            "waveforms": {
                "single": "-2290951810432572041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7910943188283288171": {
            "length": 44,
            "waveforms": {
                "single": "-7910943188283288171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2942258006594192305": {
            "length": 44,
            "waveforms": {
                "single": "2942258006594192305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1460519751592764644": {
            "length": 44,
            "waveforms": {
                "single": "1460519751592764644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5140017694597359168": {
            "length": 48,
            "waveforms": {
                "single": "5140017694597359168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7354657122105654498": {
            "length": 48,
            "waveforms": {
                "single": "-7354657122105654498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4213050527210824345": {
            "length": 48,
            "waveforms": {
                "single": "-4213050527210824345",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8891489256622695853": {
            "length": 48,
            "waveforms": {
                "single": "8891489256622695853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1939280063948525149": {
            "length": 52,
            "waveforms": {
                "single": "1939280063948525149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5746451970191148800": {
            "length": 52,
            "waveforms": {
                "single": "5746451970191148800",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "297806442122991959": {
            "length": 52,
            "waveforms": {
                "single": "297806442122991959",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3116891898012852366": {
            "length": 52,
            "waveforms": {
                "single": "3116891898012852366",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2495566130126158822": {
            "length": 56,
            "waveforms": {
                "single": "2495566130126158822",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7017883900216162138": {
            "length": 56,
            "waveforms": {
                "single": "7017883900216162138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5047828539289756359": {
            "length": 56,
            "waveforms": {
                "single": "-5047828539289756359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7898882670666768041": {
            "length": 56,
            "waveforms": {
                "single": "-7898882670666768041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7677388611468052793": {
            "length": 60,
            "waveforms": {
                "single": "-7677388611468052793",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8298714379354746337": {
            "length": 60,
            "waveforms": {
                "single": "-8298714379354746337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3776396609264743021": {
            "length": 60,
            "waveforms": {
                "single": "-3776396609264743021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "9127992669991711247_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "9127992669991711247_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "2522892627134655911_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "2522892627134655911_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-3181386020522137583": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5145608785012429593_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5145608785012429593_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2335546272359394115_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-2335546272359394115_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7002992407923258226": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7698920818626935174": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-7477426759428219926": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-8518807338412963276": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-8297313279214248028": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-7313980602231860790": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-7092486543033145542": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "6012053240800374656": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-866343774184316819": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "7339185515042674960": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "338482961996785667": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "7283485170825387994": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-2291077110181510767": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-259909498590527187": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-3455094994438230199": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5417086798264422656": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-414515479349654544": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "5361386454047135690": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "4818694337677109802": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2216349167615588637": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7016454025680276665": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7237948084878991913": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8221280761861379151": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1577228788819427229": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3999320542999343742": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3777826483800628494": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2174242773205909456": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2572999747619526008": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4372002461209076319": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1005471115578814018": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8272994463412386091": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1301567817594512670": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6643772107470544088": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6422278048271828840": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8657934679807460475": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8879428739006175723": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-695133542000723038": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "1008691456758102369": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5531009226848105685": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2136345829673444684": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4488711498435738904": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-4765905901851741118": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-2290951810432572041": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7910943188283288171": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2942258006594192305": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1460519751592764644": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5140017694597359168": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7354657122105654498": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4213050527210824345": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "8891489256622695853": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1939280063948525149": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5746451970191148800": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "297806442122991959": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "3116891898012852366": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2495566130126158822": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7017883900216162138": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5047828539289756359": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-7898882670666768041": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7677388611468052793": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8298714379354746337": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3776396609264743021": {
            "samples": [0.12562814070351758] * 59 + [0.0],
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
                "-3181386020522137583": "-3181386020522137583",
                "7002992407923258226": "7002992407923258226",
                "-7698920818626935174": "-7698920818626935174",
                "-7477426759428219926": "-7477426759428219926",
                "-8518807338412963276": "-8518807338412963276",
                "-8297313279214248028": "-8297313279214248028",
                "-7313980602231860790": "-7313980602231860790",
                "-7092486543033145542": "-7092486543033145542",
                "6012053240800374656": "6012053240800374656",
                "-866343774184316819": "-866343774184316819",
                "7339185515042674960": "7339185515042674960",
                "338482961996785667": "338482961996785667",
                "7283485170825387994": "7283485170825387994",
                "-2291077110181510767": "-2291077110181510767",
                "-259909498590527187": "-259909498590527187",
                "-3455094994438230199": "-3455094994438230199",
                "5417086798264422656": "5417086798264422656",
                "-414515479349654544": "-414515479349654544",
                "5361386454047135690": "5361386454047135690",
                "4818694337677109802": "4818694337677109802",
                "2216349167615588637": "2216349167615588637",
                "7016454025680276665": "7016454025680276665",
                "7237948084878991913": "7237948084878991913",
                "8221280761861379151": "8221280761861379151",
                "-1577228788819427229": "-1577228788819427229",
                "-3999320542999343742": "-3999320542999343742",
                "-3777826483800628494": "-3777826483800628494",
                "2174242773205909456": "2174242773205909456",
                "-2572999747619526008": "-2572999747619526008",
                "4372002461209076319": "4372002461209076319",
                "1005471115578814018": "1005471115578814018",
                "8272994463412386091": "8272994463412386091",
                "-1301567817594512670": "-1301567817594512670",
                "-6643772107470544088": "-6643772107470544088",
                "-6422278048271828840": "-6422278048271828840",
                "8657934679807460475": "8657934679807460475",
                "8879428739006175723": "8879428739006175723",
                "-695133542000723038": "-695133542000723038",
                "1008691456758102369": "1008691456758102369",
                "5531009226848105685": "5531009226848105685",
                "-2136345829673444684": "-2136345829673444684",
                "-4488711498435738904": "-4488711498435738904",
                "-4765905901851741118": "-4765905901851741118",
                "-2290951810432572041": "-2290951810432572041",
                "-7910943188283288171": "-7910943188283288171",
                "2942258006594192305": "2942258006594192305",
                "1460519751592764644": "1460519751592764644",
                "5140017694597359168": "5140017694597359168",
                "-7354657122105654498": "-7354657122105654498",
                "-4213050527210824345": "-4213050527210824345",
                "8891489256622695853": "8891489256622695853",
                "1939280063948525149": "1939280063948525149",
                "5746451970191148800": "5746451970191148800",
                "297806442122991959": "297806442122991959",
                "3116891898012852366": "3116891898012852366",
                "2495566130126158822": "2495566130126158822",
                "7017883900216162138": "7017883900216162138",
                "-5047828539289756359": "-5047828539289756359",
                "-7898882670666768041": "-7898882670666768041",
                "-7677388611468052793": "-7677388611468052793",
                "-8298714379354746337": "-8298714379354746337",
                "-3776396609264743021": "-3776396609264743021",
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
                "-2291820121492901667": "-2291820121492901667_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_773",
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
                "2522892627134655911": "2522892627134655911",
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
                "mixer": "B4/drive_mixer_437",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "9127992669991711247": "9127992669991711247",
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
                "mixer": "B2/drive_mixer_fec",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "4123035581968125476": "4123035581968125476_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_772",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "9127992669991711247": {
            "length": 40,
            "waveforms": {
                "I": "9127992669991711247_i",
                "Q": "9127992669991711247_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2522892627134655911": {
            "length": 40,
            "waveforms": {
                "I": "2522892627134655911_i",
                "Q": "2522892627134655911_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3181386020522137583": {
            "length": 60,
            "waveforms": {
                "single": "-3181386020522137583",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2291820121492901667_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5145608785012429593_i",
                "Q": "5145608785012429593_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "4123035581968125476_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2335546272359394115_i",
                "Q": "-2335546272359394115_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7002992407923258226": {
            "length": 60,
            "waveforms": {
                "single": "7002992407923258226",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7698920818626935174": {
            "length": 16,
            "waveforms": {
                "single": "-7698920818626935174",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7477426759428219926": {
            "length": 16,
            "waveforms": {
                "single": "-7477426759428219926",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8518807338412963276": {
            "length": 16,
            "waveforms": {
                "single": "-8518807338412963276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8297313279214248028": {
            "length": 16,
            "waveforms": {
                "single": "-8297313279214248028",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7313980602231860790": {
            "length": 16,
            "waveforms": {
                "single": "-7313980602231860790",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7092486543033145542": {
            "length": 16,
            "waveforms": {
                "single": "-7092486543033145542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6012053240800374656": {
            "length": 16,
            "waveforms": {
                "single": "6012053240800374656",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-866343774184316819": {
            "length": 16,
            "waveforms": {
                "single": "-866343774184316819",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7339185515042674960": {
            "length": 16,
            "waveforms": {
                "single": "7339185515042674960",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "338482961996785667": {
            "length": 16,
            "waveforms": {
                "single": "338482961996785667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7283485170825387994": {
            "length": 16,
            "waveforms": {
                "single": "7283485170825387994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2291077110181510767": {
            "length": 16,
            "waveforms": {
                "single": "-2291077110181510767",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-259909498590527187": {
            "length": 16,
            "waveforms": {
                "single": "-259909498590527187",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3455094994438230199": {
            "length": 16,
            "waveforms": {
                "single": "-3455094994438230199",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5417086798264422656": {
            "length": 16,
            "waveforms": {
                "single": "5417086798264422656",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-414515479349654544": {
            "length": 16,
            "waveforms": {
                "single": "-414515479349654544",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5361386454047135690": {
            "length": 16,
            "waveforms": {
                "single": "5361386454047135690",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4818694337677109802": {
            "length": 20,
            "waveforms": {
                "single": "4818694337677109802",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2216349167615588637": {
            "length": 20,
            "waveforms": {
                "single": "2216349167615588637",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7016454025680276665": {
            "length": 20,
            "waveforms": {
                "single": "7016454025680276665",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7237948084878991913": {
            "length": 20,
            "waveforms": {
                "single": "7237948084878991913",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8221280761861379151": {
            "length": 24,
            "waveforms": {
                "single": "8221280761861379151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1577228788819427229": {
            "length": 24,
            "waveforms": {
                "single": "-1577228788819427229",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3999320542999343742": {
            "length": 24,
            "waveforms": {
                "single": "-3999320542999343742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3777826483800628494": {
            "length": 24,
            "waveforms": {
                "single": "-3777826483800628494",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2174242773205909456": {
            "length": 28,
            "waveforms": {
                "single": "2174242773205909456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2572999747619526008": {
            "length": 28,
            "waveforms": {
                "single": "-2572999747619526008",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4372002461209076319": {
            "length": 28,
            "waveforms": {
                "single": "4372002461209076319",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1005471115578814018": {
            "length": 28,
            "waveforms": {
                "single": "1005471115578814018",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8272994463412386091": {
            "length": 32,
            "waveforms": {
                "single": "8272994463412386091",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1301567817594512670": {
            "length": 32,
            "waveforms": {
                "single": "-1301567817594512670",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6643772107470544088": {
            "length": 32,
            "waveforms": {
                "single": "-6643772107470544088",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6422278048271828840": {
            "length": 32,
            "waveforms": {
                "single": "-6422278048271828840",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8657934679807460475": {
            "length": 36,
            "waveforms": {
                "single": "8657934679807460475",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8879428739006175723": {
            "length": 36,
            "waveforms": {
                "single": "8879428739006175723",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-695133542000723038": {
            "length": 36,
            "waveforms": {
                "single": "-695133542000723038",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1008691456758102369": {
            "length": 36,
            "waveforms": {
                "single": "1008691456758102369",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5531009226848105685": {
            "length": 40,
            "waveforms": {
                "single": "5531009226848105685",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2136345829673444684": {
            "length": 40,
            "waveforms": {
                "single": "-2136345829673444684",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4488711498435738904": {
            "length": 40,
            "waveforms": {
                "single": "-4488711498435738904",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4765905901851741118": {
            "length": 40,
            "waveforms": {
                "single": "-4765905901851741118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2290951810432572041": {
            "length": 44,
            "waveforms": {
                "single": "-2290951810432572041",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7910943188283288171": {
            "length": 44,
            "waveforms": {
                "single": "-7910943188283288171",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2942258006594192305": {
            "length": 44,
            "waveforms": {
                "single": "2942258006594192305",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1460519751592764644": {
            "length": 44,
            "waveforms": {
                "single": "1460519751592764644",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5140017694597359168": {
            "length": 48,
            "waveforms": {
                "single": "5140017694597359168",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7354657122105654498": {
            "length": 48,
            "waveforms": {
                "single": "-7354657122105654498",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4213050527210824345": {
            "length": 48,
            "waveforms": {
                "single": "-4213050527210824345",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8891489256622695853": {
            "length": 48,
            "waveforms": {
                "single": "8891489256622695853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1939280063948525149": {
            "length": 52,
            "waveforms": {
                "single": "1939280063948525149",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5746451970191148800": {
            "length": 52,
            "waveforms": {
                "single": "5746451970191148800",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "297806442122991959": {
            "length": 52,
            "waveforms": {
                "single": "297806442122991959",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3116891898012852366": {
            "length": 52,
            "waveforms": {
                "single": "3116891898012852366",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2495566130126158822": {
            "length": 56,
            "waveforms": {
                "single": "2495566130126158822",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7017883900216162138": {
            "length": 56,
            "waveforms": {
                "single": "7017883900216162138",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5047828539289756359": {
            "length": 56,
            "waveforms": {
                "single": "-5047828539289756359",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7898882670666768041": {
            "length": 56,
            "waveforms": {
                "single": "-7898882670666768041",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7677388611468052793": {
            "length": 60,
            "waveforms": {
                "single": "-7677388611468052793",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8298714379354746337": {
            "length": 60,
            "waveforms": {
                "single": "-8298714379354746337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3776396609264743021": {
            "length": 60,
            "waveforms": {
                "single": "-3776396609264743021",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "9127992669991711247_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9127992669991711247_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2522892627134655911_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2522892627134655911_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3181386020522137583": {
            "type": "constant",
            "sample": -0.2388,
        },
        "5145608785012429593_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5145608785012429593_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2335546272359394115_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-2335546272359394115_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7002992407923258226": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-7698920818626935174": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7477426759428219926": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8518807338412963276": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8297313279214248028": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7313980602231860790": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7092486543033145542": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6012053240800374656": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-866343774184316819": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7339185515042674960": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "338482961996785667": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7283485170825387994": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2291077110181510767": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-259909498590527187": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3455094994438230199": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5417086798264422656": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-414515479349654544": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5361386454047135690": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "4818694337677109802": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2216349167615588637": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7016454025680276665": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7237948084878991913": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8221280761861379151": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1577228788819427229": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3999320542999343742": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3777826483800628494": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "2174242773205909456": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2572999747619526008": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4372002461209076319": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1005471115578814018": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8272994463412386091": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1301567817594512670": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6643772107470544088": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6422278048271828840": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8657934679807460475": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8879428739006175723": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-695133542000723038": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1008691456758102369": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5531009226848105685": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2136345829673444684": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4488711498435738904": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4765905901851741118": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-2290951810432572041": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7910943188283288171": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2942258006594192305": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1460519751592764644": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5140017694597359168": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7354657122105654498": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4213050527210824345": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8891489256622695853": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1939280063948525149": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5746451970191148800": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "297806442122991959": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3116891898012852366": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "2495566130126158822": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7017883900216162138": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5047828539289756359": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7898882670666768041": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-7677388611468052793": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8298714379354746337": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3776396609264743021": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 59 + [0.0],
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
        "B2/acquisition_mixer_773": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_437": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_fec": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_772": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

