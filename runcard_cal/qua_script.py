
# Single QUA script generated at 2025-02-17 11:28:33.536076
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
            with for_(v9,-1.99,(v9<-1.7077448979591836),(v9+0.004061224489795734)):
                align()
                play("-6369944410664545010", "B2/drive")
                play("-7705019459538383592", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-5103138878160555687"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-8075458350360783120"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("130070938866208659"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("351564998064923907"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("1334897675047311145"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("2549324686068090770"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-5215564042546539659"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("7782534503094855116"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("-3124245592735498219"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-8466449882611529637"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-8244955823412814389"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-3233240065584765291"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-3011746006386050043"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-192660550496189636"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-813986318382883180"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-3166351987145177400"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("1771551592993392469"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("1605267428818998931"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-6588583676992726667"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-207552042789093548"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-5383756940811624181"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-4169329929790844556"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-362158023548220905"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("1063879887235919790"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("4871051793478543441"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("3261639575239086653"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("7068811481481710304"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("1448820103630994174"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-1746365392216708838"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-1524871333017993590"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("1294214122871866817"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("672888354985173273"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("796848742090808461"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-1139931116622919206"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("8725183627901798026"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("8946677687100513274"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("8325351919213819730"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-4266856569582273996"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("3477082318582129768"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-2069096881579107133"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-1847602822380391885"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("6357926466846599894"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("350156865622774978"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-7317198190898775391"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("5583366682649539324"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-8243525948876928916"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("7781126370652706187"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("8002620429851421435"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-2238594354631138402"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-7858585732481854532"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("2994615462395625944"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-5660826044478687669"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("6035194977484201599"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("7461232888268342294"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-2779981896214217543"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("7611628897600674918"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-4980579591195418808"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-360728149012335432"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-1079587588992109036"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-2561325843993536697"*amp(v9), "B4/flux")
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
                play("-7705019459538383592", "B4/drive")
                measure("8290881506853866473", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("9211743483824299527", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(70).buffer(60).average().save("8290881506853866473_B2|acquisition_shots")
        r2.buffer(70).buffer(60).average().save("9211743483824299527_B4|acquisition_shots")


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
                "-2472880067068468831": "-2472880067068468831",
                "8218063173194464550": "8218063173194464550",
                "-5103138878160555687": "-5103138878160555687",
                "-8075458350360783120": "-8075458350360783120",
                "130070938866208659": "130070938866208659",
                "351564998064923907": "351564998064923907",
                "1334897675047311145": "1334897675047311145",
                "2549324686068090770": "2549324686068090770",
                "-5215564042546539659": "-5215564042546539659",
                "7782534503094855116": "7782534503094855116",
                "-3124245592735498219": "-3124245592735498219",
                "-8466449882611529637": "-8466449882611529637",
                "-8244955823412814389": "-8244955823412814389",
                "-3233240065584765291": "-3233240065584765291",
                "-3011746006386050043": "-3011746006386050043",
                "-192660550496189636": "-192660550496189636",
                "-813986318382883180": "-813986318382883180",
                "-3166351987145177400": "-3166351987145177400",
                "1771551592993392469": "1771551592993392469",
                "1605267428818998931": "1605267428818998931",
                "-6588583676992726667": "-6588583676992726667",
                "-207552042789093548": "-207552042789093548",
                "-5383756940811624181": "-5383756940811624181",
                "-4169329929790844556": "-4169329929790844556",
                "-362158023548220905": "-362158023548220905",
                "1063879887235919790": "1063879887235919790",
                "4871051793478543441": "4871051793478543441",
                "3261639575239086653": "3261639575239086653",
                "7068811481481710304": "7068811481481710304",
                "1448820103630994174": "1448820103630994174",
                "-1746365392216708838": "-1746365392216708838",
                "-1524871333017993590": "-1524871333017993590",
                "1294214122871866817": "1294214122871866817",
                "672888354985173273": "672888354985173273",
                "796848742090808461": "796848742090808461",
                "-1139931116622919206": "-1139931116622919206",
                "8725183627901798026": "8725183627901798026",
                "8946677687100513274": "8946677687100513274",
                "8325351919213819730": "8325351919213819730",
                "-4266856569582273996": "-4266856569582273996",
                "3477082318582129768": "3477082318582129768",
                "-2069096881579107133": "-2069096881579107133",
                "-1847602822380391885": "-1847602822380391885",
                "6357926466846599894": "6357926466846599894",
                "350156865622774978": "350156865622774978",
                "-7317198190898775391": "-7317198190898775391",
                "5583366682649539324": "5583366682649539324",
                "-8243525948876928916": "-8243525948876928916",
                "7781126370652706187": "7781126370652706187",
                "8002620429851421435": "8002620429851421435",
                "-2238594354631138402": "-2238594354631138402",
                "-7858585732481854532": "-7858585732481854532",
                "2994615462395625944": "2994615462395625944",
                "-5660826044478687669": "-5660826044478687669",
                "6035194977484201599": "6035194977484201599",
                "7461232888268342294": "7461232888268342294",
                "-2779981896214217543": "-2779981896214217543",
                "7611628897600674918": "7611628897600674918",
                "-4980579591195418808": "-4980579591195418808",
                "-360728149012335432": "-360728149012335432",
                "-1079587588992109036": "-1079587588992109036",
                "-2561325843993536697": "-2561325843993536697",
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
                "-7705019459538383592": "-7705019459538383592",
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
                "9211743483824299527": "9211743483824299527_B4/acquisition",
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
                "-6369944410664545010": "-6369944410664545010",
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
                "8290881506853866473": "8290881506853866473_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-6369944410664545010": {
            "length": 40,
            "waveforms": {
                "I": "-6369944410664545010_i",
                "Q": "-6369944410664545010_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7705019459538383592": {
            "length": 40,
            "waveforms": {
                "I": "-7705019459538383592_i",
                "Q": "-7705019459538383592_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2472880067068468831": {
            "length": 60,
            "waveforms": {
                "single": "-2472880067068468831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8290881506853866473_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6908545465314868207_i",
                "Q": "6908545465314868207_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "9211743483824299527_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4697415401926261253_i",
                "Q": "4697415401926261253_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "8218063173194464550": {
            "length": 60,
            "waveforms": {
                "single": "8218063173194464550",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5103138878160555687": {
            "length": 16,
            "waveforms": {
                "single": "-5103138878160555687",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8075458350360783120": {
            "length": 16,
            "waveforms": {
                "single": "-8075458350360783120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "130070938866208659": {
            "length": 16,
            "waveforms": {
                "single": "130070938866208659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "351564998064923907": {
            "length": 16,
            "waveforms": {
                "single": "351564998064923907",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1334897675047311145": {
            "length": 16,
            "waveforms": {
                "single": "1334897675047311145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2549324686068090770": {
            "length": 16,
            "waveforms": {
                "single": "2549324686068090770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5215564042546539659": {
            "length": 16,
            "waveforms": {
                "single": "-5215564042546539659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7782534503094855116": {
            "length": 16,
            "waveforms": {
                "single": "7782534503094855116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3124245592735498219": {
            "length": 16,
            "waveforms": {
                "single": "-3124245592735498219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8466449882611529637": {
            "length": 16,
            "waveforms": {
                "single": "-8466449882611529637",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8244955823412814389": {
            "length": 16,
            "waveforms": {
                "single": "-8244955823412814389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3233240065584765291": {
            "length": 16,
            "waveforms": {
                "single": "-3233240065584765291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3011746006386050043": {
            "length": 16,
            "waveforms": {
                "single": "-3011746006386050043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-192660550496189636": {
            "length": 16,
            "waveforms": {
                "single": "-192660550496189636",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-813986318382883180": {
            "length": 16,
            "waveforms": {
                "single": "-813986318382883180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3166351987145177400": {
            "length": 16,
            "waveforms": {
                "single": "-3166351987145177400",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1771551592993392469": {
            "length": 16,
            "waveforms": {
                "single": "1771551592993392469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1605267428818998931": {
            "length": 20,
            "waveforms": {
                "single": "1605267428818998931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6588583676992726667": {
            "length": 20,
            "waveforms": {
                "single": "-6588583676992726667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-207552042789093548": {
            "length": 20,
            "waveforms": {
                "single": "-207552042789093548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5383756940811624181": {
            "length": 20,
            "waveforms": {
                "single": "-5383756940811624181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4169329929790844556": {
            "length": 24,
            "waveforms": {
                "single": "-4169329929790844556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-362158023548220905": {
            "length": 24,
            "waveforms": {
                "single": "-362158023548220905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1063879887235919790": {
            "length": 24,
            "waveforms": {
                "single": "1063879887235919790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4871051793478543441": {
            "length": 24,
            "waveforms": {
                "single": "4871051793478543441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3261639575239086653": {
            "length": 28,
            "waveforms": {
                "single": "3261639575239086653",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7068811481481710304": {
            "length": 28,
            "waveforms": {
                "single": "7068811481481710304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1448820103630994174": {
            "length": 28,
            "waveforms": {
                "single": "1448820103630994174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1746365392216708838": {
            "length": 28,
            "waveforms": {
                "single": "-1746365392216708838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1524871333017993590": {
            "length": 32,
            "waveforms": {
                "single": "-1524871333017993590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1294214122871866817": {
            "length": 32,
            "waveforms": {
                "single": "1294214122871866817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "672888354985173273": {
            "length": 32,
            "waveforms": {
                "single": "672888354985173273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "796848742090808461": {
            "length": 32,
            "waveforms": {
                "single": "796848742090808461",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1139931116622919206": {
            "length": 36,
            "waveforms": {
                "single": "-1139931116622919206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8725183627901798026": {
            "length": 36,
            "waveforms": {
                "single": "8725183627901798026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8946677687100513274": {
            "length": 36,
            "waveforms": {
                "single": "8946677687100513274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8325351919213819730": {
            "length": 36,
            "waveforms": {
                "single": "8325351919213819730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4266856569582273996": {
            "length": 40,
            "waveforms": {
                "single": "-4266856569582273996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3477082318582129768": {
            "length": 40,
            "waveforms": {
                "single": "3477082318582129768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2069096881579107133": {
            "length": 40,
            "waveforms": {
                "single": "-2069096881579107133",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1847602822380391885": {
            "length": 40,
            "waveforms": {
                "single": "-1847602822380391885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6357926466846599894": {
            "length": 44,
            "waveforms": {
                "single": "6357926466846599894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "350156865622774978": {
            "length": 44,
            "waveforms": {
                "single": "350156865622774978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7317198190898775391": {
            "length": 44,
            "waveforms": {
                "single": "-7317198190898775391",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5583366682649539324": {
            "length": 44,
            "waveforms": {
                "single": "5583366682649539324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8243525948876928916": {
            "length": 48,
            "waveforms": {
                "single": "-8243525948876928916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7781126370652706187": {
            "length": 48,
            "waveforms": {
                "single": "7781126370652706187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8002620429851421435": {
            "length": 48,
            "waveforms": {
                "single": "8002620429851421435",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2238594354631138402": {
            "length": 48,
            "waveforms": {
                "single": "-2238594354631138402",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7858585732481854532": {
            "length": 52,
            "waveforms": {
                "single": "-7858585732481854532",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2994615462395625944": {
            "length": 52,
            "waveforms": {
                "single": "2994615462395625944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5660826044478687669": {
            "length": 52,
            "waveforms": {
                "single": "-5660826044478687669",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6035194977484201599": {
            "length": 52,
            "waveforms": {
                "single": "6035194977484201599",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7461232888268342294": {
            "length": 56,
            "waveforms": {
                "single": "7461232888268342294",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2779981896214217543": {
            "length": 56,
            "waveforms": {
                "single": "-2779981896214217543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7611628897600674918": {
            "length": 56,
            "waveforms": {
                "single": "7611628897600674918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4980579591195418808": {
            "length": 56,
            "waveforms": {
                "single": "-4980579591195418808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-360728149012335432": {
            "length": 60,
            "waveforms": {
                "single": "-360728149012335432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1079587588992109036": {
            "length": 60,
            "waveforms": {
                "single": "-1079587588992109036",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2561325843993536697": {
            "length": 60,
            "waveforms": {
                "single": "-2561325843993536697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6369944410664545010_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-6369944410664545010_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-7705019459538383592_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-7705019459538383592_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-2472880067068468831": {
            "sample": -0.2388,
            "type": "constant",
        },
        "6908545465314868207_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "6908545465314868207_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4697415401926261253_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4697415401926261253_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8218063173194464550": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5103138878160555687": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8075458350360783120": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "130070938866208659": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "351564998064923907": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "1334897675047311145": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "2549324686068090770": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-5215564042546539659": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "7782534503094855116": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-3124245592735498219": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8466449882611529637": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8244955823412814389": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-3233240065584765291": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-3011746006386050043": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-192660550496189636": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-813986318382883180": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3166351987145177400": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "1771551592993392469": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1605267428818998931": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6588583676992726667": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-207552042789093548": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5383756940811624181": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4169329929790844556": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-362158023548220905": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1063879887235919790": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "4871051793478543441": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3261639575239086653": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7068811481481710304": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1448820103630994174": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-1746365392216708838": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1524871333017993590": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1294214122871866817": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "672888354985173273": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
        },
        "796848742090808461": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1139931116622919206": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8725183627901798026": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8946677687100513274": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
        },
        "8325351919213819730": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4266856569582273996": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3477082318582129768": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2069096881579107133": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1847602822380391885": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6357926466846599894": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "350156865622774978": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7317198190898775391": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
        },
        "5583366682649539324": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8243525948876928916": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7781126370652706187": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8002620429851421435": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2238594354631138402": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-7858585732481854532": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2994615462395625944": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5660826044478687669": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
        },
        "6035194977484201599": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7461232888268342294": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2779981896214217543": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7611628897600674918": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-4980579591195418808": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-360728149012335432": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1079587588992109036": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2561325843993536697": {
            "samples": [0.12311557788944723] * 59 + [0.0],
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
                "-2472880067068468831": "-2472880067068468831",
                "8218063173194464550": "8218063173194464550",
                "-5103138878160555687": "-5103138878160555687",
                "-8075458350360783120": "-8075458350360783120",
                "130070938866208659": "130070938866208659",
                "351564998064923907": "351564998064923907",
                "1334897675047311145": "1334897675047311145",
                "2549324686068090770": "2549324686068090770",
                "-5215564042546539659": "-5215564042546539659",
                "7782534503094855116": "7782534503094855116",
                "-3124245592735498219": "-3124245592735498219",
                "-8466449882611529637": "-8466449882611529637",
                "-8244955823412814389": "-8244955823412814389",
                "-3233240065584765291": "-3233240065584765291",
                "-3011746006386050043": "-3011746006386050043",
                "-192660550496189636": "-192660550496189636",
                "-813986318382883180": "-813986318382883180",
                "-3166351987145177400": "-3166351987145177400",
                "1771551592993392469": "1771551592993392469",
                "1605267428818998931": "1605267428818998931",
                "-6588583676992726667": "-6588583676992726667",
                "-207552042789093548": "-207552042789093548",
                "-5383756940811624181": "-5383756940811624181",
                "-4169329929790844556": "-4169329929790844556",
                "-362158023548220905": "-362158023548220905",
                "1063879887235919790": "1063879887235919790",
                "4871051793478543441": "4871051793478543441",
                "3261639575239086653": "3261639575239086653",
                "7068811481481710304": "7068811481481710304",
                "1448820103630994174": "1448820103630994174",
                "-1746365392216708838": "-1746365392216708838",
                "-1524871333017993590": "-1524871333017993590",
                "1294214122871866817": "1294214122871866817",
                "672888354985173273": "672888354985173273",
                "796848742090808461": "796848742090808461",
                "-1139931116622919206": "-1139931116622919206",
                "8725183627901798026": "8725183627901798026",
                "8946677687100513274": "8946677687100513274",
                "8325351919213819730": "8325351919213819730",
                "-4266856569582273996": "-4266856569582273996",
                "3477082318582129768": "3477082318582129768",
                "-2069096881579107133": "-2069096881579107133",
                "-1847602822380391885": "-1847602822380391885",
                "6357926466846599894": "6357926466846599894",
                "350156865622774978": "350156865622774978",
                "-7317198190898775391": "-7317198190898775391",
                "5583366682649539324": "5583366682649539324",
                "-8243525948876928916": "-8243525948876928916",
                "7781126370652706187": "7781126370652706187",
                "8002620429851421435": "8002620429851421435",
                "-2238594354631138402": "-2238594354631138402",
                "-7858585732481854532": "-7858585732481854532",
                "2994615462395625944": "2994615462395625944",
                "-5660826044478687669": "-5660826044478687669",
                "6035194977484201599": "6035194977484201599",
                "7461232888268342294": "7461232888268342294",
                "-2779981896214217543": "-2779981896214217543",
                "7611628897600674918": "7611628897600674918",
                "-4980579591195418808": "-4980579591195418808",
                "-360728149012335432": "-360728149012335432",
                "-1079587588992109036": "-1079587588992109036",
                "-2561325843993536697": "-2561325843993536697",
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
                "-7705019459538383592": "-7705019459538383592",
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
                "mixer": "B4/drive_mixer_ce0",
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
                "9211743483824299527": "9211743483824299527_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_a83",
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
                "-6369944410664545010": "-6369944410664545010",
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
                "mixer": "B2/drive_mixer_cec",
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
                "8290881506853866473": "8290881506853866473_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_1f4",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "-6369944410664545010": {
            "length": 40,
            "waveforms": {
                "I": "-6369944410664545010_i",
                "Q": "-6369944410664545010_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7705019459538383592": {
            "length": 40,
            "waveforms": {
                "I": "-7705019459538383592_i",
                "Q": "-7705019459538383592_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2472880067068468831": {
            "length": 60,
            "waveforms": {
                "single": "-2472880067068468831",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8290881506853866473_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6908545465314868207_i",
                "Q": "6908545465314868207_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "9211743483824299527_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4697415401926261253_i",
                "Q": "4697415401926261253_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8218063173194464550": {
            "length": 60,
            "waveforms": {
                "single": "8218063173194464550",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5103138878160555687": {
            "length": 16,
            "waveforms": {
                "single": "-5103138878160555687",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8075458350360783120": {
            "length": 16,
            "waveforms": {
                "single": "-8075458350360783120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "130070938866208659": {
            "length": 16,
            "waveforms": {
                "single": "130070938866208659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "351564998064923907": {
            "length": 16,
            "waveforms": {
                "single": "351564998064923907",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1334897675047311145": {
            "length": 16,
            "waveforms": {
                "single": "1334897675047311145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2549324686068090770": {
            "length": 16,
            "waveforms": {
                "single": "2549324686068090770",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5215564042546539659": {
            "length": 16,
            "waveforms": {
                "single": "-5215564042546539659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7782534503094855116": {
            "length": 16,
            "waveforms": {
                "single": "7782534503094855116",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3124245592735498219": {
            "length": 16,
            "waveforms": {
                "single": "-3124245592735498219",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8466449882611529637": {
            "length": 16,
            "waveforms": {
                "single": "-8466449882611529637",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8244955823412814389": {
            "length": 16,
            "waveforms": {
                "single": "-8244955823412814389",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3233240065584765291": {
            "length": 16,
            "waveforms": {
                "single": "-3233240065584765291",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3011746006386050043": {
            "length": 16,
            "waveforms": {
                "single": "-3011746006386050043",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-192660550496189636": {
            "length": 16,
            "waveforms": {
                "single": "-192660550496189636",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-813986318382883180": {
            "length": 16,
            "waveforms": {
                "single": "-813986318382883180",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3166351987145177400": {
            "length": 16,
            "waveforms": {
                "single": "-3166351987145177400",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1771551592993392469": {
            "length": 16,
            "waveforms": {
                "single": "1771551592993392469",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1605267428818998931": {
            "length": 20,
            "waveforms": {
                "single": "1605267428818998931",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6588583676992726667": {
            "length": 20,
            "waveforms": {
                "single": "-6588583676992726667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-207552042789093548": {
            "length": 20,
            "waveforms": {
                "single": "-207552042789093548",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5383756940811624181": {
            "length": 20,
            "waveforms": {
                "single": "-5383756940811624181",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4169329929790844556": {
            "length": 24,
            "waveforms": {
                "single": "-4169329929790844556",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-362158023548220905": {
            "length": 24,
            "waveforms": {
                "single": "-362158023548220905",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1063879887235919790": {
            "length": 24,
            "waveforms": {
                "single": "1063879887235919790",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4871051793478543441": {
            "length": 24,
            "waveforms": {
                "single": "4871051793478543441",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3261639575239086653": {
            "length": 28,
            "waveforms": {
                "single": "3261639575239086653",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7068811481481710304": {
            "length": 28,
            "waveforms": {
                "single": "7068811481481710304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1448820103630994174": {
            "length": 28,
            "waveforms": {
                "single": "1448820103630994174",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1746365392216708838": {
            "length": 28,
            "waveforms": {
                "single": "-1746365392216708838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1524871333017993590": {
            "length": 32,
            "waveforms": {
                "single": "-1524871333017993590",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1294214122871866817": {
            "length": 32,
            "waveforms": {
                "single": "1294214122871866817",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "672888354985173273": {
            "length": 32,
            "waveforms": {
                "single": "672888354985173273",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "796848742090808461": {
            "length": 32,
            "waveforms": {
                "single": "796848742090808461",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1139931116622919206": {
            "length": 36,
            "waveforms": {
                "single": "-1139931116622919206",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8725183627901798026": {
            "length": 36,
            "waveforms": {
                "single": "8725183627901798026",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8946677687100513274": {
            "length": 36,
            "waveforms": {
                "single": "8946677687100513274",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8325351919213819730": {
            "length": 36,
            "waveforms": {
                "single": "8325351919213819730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4266856569582273996": {
            "length": 40,
            "waveforms": {
                "single": "-4266856569582273996",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3477082318582129768": {
            "length": 40,
            "waveforms": {
                "single": "3477082318582129768",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2069096881579107133": {
            "length": 40,
            "waveforms": {
                "single": "-2069096881579107133",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1847602822380391885": {
            "length": 40,
            "waveforms": {
                "single": "-1847602822380391885",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6357926466846599894": {
            "length": 44,
            "waveforms": {
                "single": "6357926466846599894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "350156865622774978": {
            "length": 44,
            "waveforms": {
                "single": "350156865622774978",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7317198190898775391": {
            "length": 44,
            "waveforms": {
                "single": "-7317198190898775391",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5583366682649539324": {
            "length": 44,
            "waveforms": {
                "single": "5583366682649539324",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8243525948876928916": {
            "length": 48,
            "waveforms": {
                "single": "-8243525948876928916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7781126370652706187": {
            "length": 48,
            "waveforms": {
                "single": "7781126370652706187",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8002620429851421435": {
            "length": 48,
            "waveforms": {
                "single": "8002620429851421435",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2238594354631138402": {
            "length": 48,
            "waveforms": {
                "single": "-2238594354631138402",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7858585732481854532": {
            "length": 52,
            "waveforms": {
                "single": "-7858585732481854532",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2994615462395625944": {
            "length": 52,
            "waveforms": {
                "single": "2994615462395625944",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5660826044478687669": {
            "length": 52,
            "waveforms": {
                "single": "-5660826044478687669",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6035194977484201599": {
            "length": 52,
            "waveforms": {
                "single": "6035194977484201599",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7461232888268342294": {
            "length": 56,
            "waveforms": {
                "single": "7461232888268342294",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2779981896214217543": {
            "length": 56,
            "waveforms": {
                "single": "-2779981896214217543",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7611628897600674918": {
            "length": 56,
            "waveforms": {
                "single": "7611628897600674918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4980579591195418808": {
            "length": 56,
            "waveforms": {
                "single": "-4980579591195418808",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-360728149012335432": {
            "length": 60,
            "waveforms": {
                "single": "-360728149012335432",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1079587588992109036": {
            "length": 60,
            "waveforms": {
                "single": "-1079587588992109036",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2561325843993536697": {
            "length": 60,
            "waveforms": {
                "single": "-2561325843993536697",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6369944410664545010_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6369944410664545010_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7705019459538383592_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7705019459538383592_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2472880067068468831": {
            "type": "constant",
            "sample": -0.2388,
        },
        "6908545465314868207_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "6908545465314868207_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "4697415401926261253_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "4697415401926261253_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8218063173194464550": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-5103138878160555687": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8075458350360783120": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "130070938866208659": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "351564998064923907": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1334897675047311145": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2549324686068090770": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5215564042546539659": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7782534503094855116": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3124245592735498219": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8466449882611529637": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8244955823412814389": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3233240065584765291": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3011746006386050043": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-192660550496189636": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-813986318382883180": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3166351987145177400": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1771551592993392469": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "1605267428818998931": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6588583676992726667": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-207552042789093548": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5383756940811624181": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4169329929790844556": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-362158023548220905": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1063879887235919790": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4871051793478543441": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3261639575239086653": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7068811481481710304": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1448820103630994174": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1746365392216708838": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1524871333017993590": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1294214122871866817": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "672888354985173273": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "796848742090808461": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1139931116622919206": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8725183627901798026": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8946677687100513274": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8325351919213819730": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4266856569582273996": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3477082318582129768": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2069096881579107133": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1847602822380391885": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6357926466846599894": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "350156865622774978": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7317198190898775391": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5583366682649539324": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-8243525948876928916": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7781126370652706187": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8002620429851421435": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2238594354631138402": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-7858585732481854532": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2994615462395625944": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5660826044478687669": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6035194977484201599": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "7461232888268342294": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2779981896214217543": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7611628897600674918": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4980579591195418808": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-360728149012335432": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1079587588992109036": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2561325843993536697": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 59 + [0.0],
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
        "B4/drive_mixer_ce0": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_a83": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_cec": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_1f4": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

