
# Single QUA script generated at 2025-02-17 14:05:40.282192
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
                play("6756965012916871280", "B2/drive")
                play("-5578710227748006758", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-3398477494011678342"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-3176983434812963094"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("502514508191631430"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("4309686414434255081"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-4174409242657499243"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("8652343453201336243"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("6728940161636137192"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("8154978072420277887"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("4099380089457840758"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-8094006313286106866"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("8000372091661150530"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("333017035139600161"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-6916394479221779649"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-6694900420023064401"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("8385312308056224914"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("8606806367254940162"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("6282248285168103709"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("5134426467991234936"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("5355920527189950184"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-2408968201424680245"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("3155322832208748919"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("5519366684386309320"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("5740860743585024568"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("5119534975698331024"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("7938620431588191431"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("8160114490786906679"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-5274913825094595839"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-5053419765895880591"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-531101995805877275"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-2855660077892713728"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-5208025746655007948"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("2377549739134050618"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-5705391127436066304"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-5982585530852068518"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("2222943758374923261"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-5444411298146627108"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-922093528056623792"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("4642197505576805372"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-977793872273910758"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-8571336751105981898"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-4049018981015978582"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("5027137721971879756"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-6152083003904099787"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-8186396534710907514"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-7964902475512192266"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("1900212269012524966"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-5767142787509025403"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-6914964604685894176"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("3864424412502107071"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("4085918471700822319"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-4495710857484012065"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("1885320776719621054"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-6308530329092104544"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-6929856096978798088"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-4110770641088937681"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("3156752706744634392"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("6963924612987258043"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("1343933235136541913"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-2312842661773749114"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("3541692923139708776"*amp(v9), "B4/flux")
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
                play("-5578710227748006758", "B4/drive")
                measure("-5435404080443863626", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-2815184573587987978", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("-5435404080443863626_B2|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("-2815184573587987978_B4|acquisition_shots")


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
                "-1055980337815744117": "-1055980337815744117",
                "3763186982338424024": "3763186982338424024",
                "-3398477494011678342": "-3398477494011678342",
                "-3176983434812963094": "-3176983434812963094",
                "502514508191631430": "502514508191631430",
                "4309686414434255081": "4309686414434255081",
                "-4174409242657499243": "-4174409242657499243",
                "8652343453201336243": "8652343453201336243",
                "6728940161636137192": "6728940161636137192",
                "8154978072420277887": "8154978072420277887",
                "4099380089457840758": "4099380089457840758",
                "-8094006313286106866": "-8094006313286106866",
                "8000372091661150530": "8000372091661150530",
                "333017035139600161": "333017035139600161",
                "-6916394479221779649": "-6916394479221779649",
                "-6694900420023064401": "-6694900420023064401",
                "8385312308056224914": "8385312308056224914",
                "8606806367254940162": "8606806367254940162",
                "6282248285168103709": "6282248285168103709",
                "5134426467991234936": "5134426467991234936",
                "5355920527189950184": "5355920527189950184",
                "-2408968201424680245": "-2408968201424680245",
                "3155322832208748919": "3155322832208748919",
                "5519366684386309320": "5519366684386309320",
                "5740860743585024568": "5740860743585024568",
                "5119534975698331024": "5119534975698331024",
                "7938620431588191431": "7938620431588191431",
                "8160114490786906679": "8160114490786906679",
                "-5274913825094595839": "-5274913825094595839",
                "-5053419765895880591": "-5053419765895880591",
                "-531101995805877275": "-531101995805877275",
                "-2855660077892713728": "-2855660077892713728",
                "-5208025746655007948": "-5208025746655007948",
                "2377549739134050618": "2377549739134050618",
                "-5705391127436066304": "-5705391127436066304",
                "-5982585530852068518": "-5982585530852068518",
                "2222943758374923261": "2222943758374923261",
                "-5444411298146627108": "-5444411298146627108",
                "-922093528056623792": "-922093528056623792",
                "4642197505576805372": "4642197505576805372",
                "-977793872273910758": "-977793872273910758",
                "-8571336751105981898": "-8571336751105981898",
                "-4049018981015978582": "-4049018981015978582",
                "5027137721971879756": "5027137721971879756",
                "-6152083003904099787": "-6152083003904099787",
                "-8186396534710907514": "-8186396534710907514",
                "-7964902475512192266": "-7964902475512192266",
                "1900212269012524966": "1900212269012524966",
                "-5767142787509025403": "-5767142787509025403",
                "-6914964604685894176": "-6914964604685894176",
                "3864424412502107071": "3864424412502107071",
                "4085918471700822319": "4085918471700822319",
                "-4495710857484012065": "-4495710857484012065",
                "1885320776719621054": "1885320776719621054",
                "-6308530329092104544": "-6308530329092104544",
                "-6929856096978798088": "-6929856096978798088",
                "-4110770641088937681": "-4110770641088937681",
                "3156752706744634392": "3156752706744634392",
                "6963924612987258043": "6963924612987258043",
                "1343933235136541913": "1343933235136541913",
                "-2312842661773749114": "-2312842661773749114",
                "3541692923139708776": "3541692923139708776",
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
                "-5435404080443863626": "-5435404080443863626_B2/acquisition",
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
                "6756965012916871280": "6756965012916871280",
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
                "-5578710227748006758": "-5578710227748006758",
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
                "-2815184573587987978": "-2815184573587987978_B4/acquisition",
            },
        },
    },
    "pulses": {
        "6756965012916871280": {
            "length": 40,
            "waveforms": {
                "I": "6756965012916871280_i",
                "Q": "6756965012916871280_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5578710227748006758": {
            "length": 40,
            "waveforms": {
                "I": "-5578710227748006758_i",
                "Q": "-5578710227748006758_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1055980337815744117": {
            "length": 60,
            "waveforms": {
                "single": "-1055980337815744117",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5435404080443863626_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8113834294804231851_i",
                "Q": "8113834294804231851_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-2815184573587987978_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7678708526067264968_i",
                "Q": "7678708526067264968_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3763186982338424024": {
            "length": 60,
            "waveforms": {
                "single": "3763186982338424024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3398477494011678342": {
            "length": 16,
            "waveforms": {
                "single": "-3398477494011678342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3176983434812963094": {
            "length": 16,
            "waveforms": {
                "single": "-3176983434812963094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "502514508191631430": {
            "length": 16,
            "waveforms": {
                "single": "502514508191631430",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4309686414434255081": {
            "length": 16,
            "waveforms": {
                "single": "4309686414434255081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4174409242657499243": {
            "length": 16,
            "waveforms": {
                "single": "-4174409242657499243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8652343453201336243": {
            "length": 16,
            "waveforms": {
                "single": "8652343453201336243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6728940161636137192": {
            "length": 16,
            "waveforms": {
                "single": "6728940161636137192",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8154978072420277887": {
            "length": 16,
            "waveforms": {
                "single": "8154978072420277887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4099380089457840758": {
            "length": 16,
            "waveforms": {
                "single": "4099380089457840758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8094006313286106866": {
            "length": 16,
            "waveforms": {
                "single": "-8094006313286106866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8000372091661150530": {
            "length": 16,
            "waveforms": {
                "single": "8000372091661150530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "333017035139600161": {
            "length": 16,
            "waveforms": {
                "single": "333017035139600161",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6916394479221779649": {
            "length": 16,
            "waveforms": {
                "single": "-6916394479221779649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6694900420023064401": {
            "length": 16,
            "waveforms": {
                "single": "-6694900420023064401",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8385312308056224914": {
            "length": 16,
            "waveforms": {
                "single": "8385312308056224914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8606806367254940162": {
            "length": 16,
            "waveforms": {
                "single": "8606806367254940162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6282248285168103709": {
            "length": 16,
            "waveforms": {
                "single": "6282248285168103709",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5134426467991234936": {
            "length": 20,
            "waveforms": {
                "single": "5134426467991234936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5355920527189950184": {
            "length": 20,
            "waveforms": {
                "single": "5355920527189950184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2408968201424680245": {
            "length": 20,
            "waveforms": {
                "single": "-2408968201424680245",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3155322832208748919": {
            "length": 20,
            "waveforms": {
                "single": "3155322832208748919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5519366684386309320": {
            "length": 24,
            "waveforms": {
                "single": "5519366684386309320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5740860743585024568": {
            "length": 24,
            "waveforms": {
                "single": "5740860743585024568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5119534975698331024": {
            "length": 24,
            "waveforms": {
                "single": "5119534975698331024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7938620431588191431": {
            "length": 24,
            "waveforms": {
                "single": "7938620431588191431",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8160114490786906679": {
            "length": 28,
            "waveforms": {
                "single": "8160114490786906679",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5274913825094595839": {
            "length": 28,
            "waveforms": {
                "single": "-5274913825094595839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5053419765895880591": {
            "length": 28,
            "waveforms": {
                "single": "-5053419765895880591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-531101995805877275": {
            "length": 28,
            "waveforms": {
                "single": "-531101995805877275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2855660077892713728": {
            "length": 32,
            "waveforms": {
                "single": "-2855660077892713728",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5208025746655007948": {
            "length": 32,
            "waveforms": {
                "single": "-5208025746655007948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2377549739134050618": {
            "length": 32,
            "waveforms": {
                "single": "2377549739134050618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5705391127436066304": {
            "length": 32,
            "waveforms": {
                "single": "-5705391127436066304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5982585530852068518": {
            "length": 36,
            "waveforms": {
                "single": "-5982585530852068518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2222943758374923261": {
            "length": 36,
            "waveforms": {
                "single": "2222943758374923261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5444411298146627108": {
            "length": 36,
            "waveforms": {
                "single": "-5444411298146627108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-922093528056623792": {
            "length": 36,
            "waveforms": {
                "single": "-922093528056623792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4642197505576805372": {
            "length": 40,
            "waveforms": {
                "single": "4642197505576805372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-977793872273910758": {
            "length": 40,
            "waveforms": {
                "single": "-977793872273910758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8571336751105981898": {
            "length": 40,
            "waveforms": {
                "single": "-8571336751105981898",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4049018981015978582": {
            "length": 40,
            "waveforms": {
                "single": "-4049018981015978582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5027137721971879756": {
            "length": 44,
            "waveforms": {
                "single": "5027137721971879756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6152083003904099787": {
            "length": 44,
            "waveforms": {
                "single": "-6152083003904099787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8186396534710907514": {
            "length": 44,
            "waveforms": {
                "single": "-8186396534710907514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7964902475512192266": {
            "length": 44,
            "waveforms": {
                "single": "-7964902475512192266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1900212269012524966": {
            "length": 48,
            "waveforms": {
                "single": "1900212269012524966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5767142787509025403": {
            "length": 48,
            "waveforms": {
                "single": "-5767142787509025403",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6914964604685894176": {
            "length": 48,
            "waveforms": {
                "single": "-6914964604685894176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3864424412502107071": {
            "length": 48,
            "waveforms": {
                "single": "3864424412502107071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4085918471700822319": {
            "length": 52,
            "waveforms": {
                "single": "4085918471700822319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4495710857484012065": {
            "length": 52,
            "waveforms": {
                "single": "-4495710857484012065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1885320776719621054": {
            "length": 52,
            "waveforms": {
                "single": "1885320776719621054",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6308530329092104544": {
            "length": 52,
            "waveforms": {
                "single": "-6308530329092104544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6929856096978798088": {
            "length": 56,
            "waveforms": {
                "single": "-6929856096978798088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4110770641088937681": {
            "length": 56,
            "waveforms": {
                "single": "-4110770641088937681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3156752706744634392": {
            "length": 56,
            "waveforms": {
                "single": "3156752706744634392",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6963924612987258043": {
            "length": 56,
            "waveforms": {
                "single": "6963924612987258043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1343933235136541913": {
            "length": 60,
            "waveforms": {
                "single": "1343933235136541913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2312842661773749114": {
            "length": 60,
            "waveforms": {
                "single": "-2312842661773749114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3541692923139708776": {
            "length": 60,
            "waveforms": {
                "single": "3541692923139708776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6756965012916871280_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "6756965012916871280_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-5578710227748006758_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-5578710227748006758_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-1055980337815744117": {
            "sample": -0.2388,
            "type": "constant",
        },
        "8113834294804231851_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "8113834294804231851_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7678708526067264968_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "7678708526067264968_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3763186982338424024": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-3398477494011678342": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-3176983434812963094": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "502514508191631430": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4309686414434255081": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-4174409242657499243": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "8652343453201336243": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "6728940161636137192": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8154978072420277887": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "4099380089457840758": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8094006313286106866": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "8000372091661150530": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "333017035139600161": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-6916394479221779649": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-6694900420023064401": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8385312308056224914": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8606806367254940162": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "6282248285168103709": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5134426467991234936": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5355920527189950184": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2408968201424680245": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "3155322832208748919": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5519366684386309320": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5740860743585024568": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5119534975698331024": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "7938620431588191431": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8160114490786906679": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5274913825094595839": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5053419765895880591": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-531101995805877275": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-2855660077892713728": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5208025746655007948": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2377549739134050618": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5705391127436066304": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5982585530852068518": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2222943758374923261": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5444411298146627108": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-922093528056623792": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "4642197505576805372": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-977793872273910758": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8571336751105981898": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-4049018981015978582": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5027137721971879756": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6152083003904099787": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8186396534710907514": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-7964902475512192266": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1900212269012524966": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5767142787509025403": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6914964604685894176": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "3864424412502107071": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "4085918471700822319": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4495710857484012065": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1885320776719621054": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-6308530329092104544": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6929856096978798088": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4110770641088937681": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3156752706744634392": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "6963924612987258043": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1343933235136541913": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2312842661773749114": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3541692923139708776": {
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
                "-1055980337815744117": "-1055980337815744117",
                "3763186982338424024": "3763186982338424024",
                "-3398477494011678342": "-3398477494011678342",
                "-3176983434812963094": "-3176983434812963094",
                "502514508191631430": "502514508191631430",
                "4309686414434255081": "4309686414434255081",
                "-4174409242657499243": "-4174409242657499243",
                "8652343453201336243": "8652343453201336243",
                "6728940161636137192": "6728940161636137192",
                "8154978072420277887": "8154978072420277887",
                "4099380089457840758": "4099380089457840758",
                "-8094006313286106866": "-8094006313286106866",
                "8000372091661150530": "8000372091661150530",
                "333017035139600161": "333017035139600161",
                "-6916394479221779649": "-6916394479221779649",
                "-6694900420023064401": "-6694900420023064401",
                "8385312308056224914": "8385312308056224914",
                "8606806367254940162": "8606806367254940162",
                "6282248285168103709": "6282248285168103709",
                "5134426467991234936": "5134426467991234936",
                "5355920527189950184": "5355920527189950184",
                "-2408968201424680245": "-2408968201424680245",
                "3155322832208748919": "3155322832208748919",
                "5519366684386309320": "5519366684386309320",
                "5740860743585024568": "5740860743585024568",
                "5119534975698331024": "5119534975698331024",
                "7938620431588191431": "7938620431588191431",
                "8160114490786906679": "8160114490786906679",
                "-5274913825094595839": "-5274913825094595839",
                "-5053419765895880591": "-5053419765895880591",
                "-531101995805877275": "-531101995805877275",
                "-2855660077892713728": "-2855660077892713728",
                "-5208025746655007948": "-5208025746655007948",
                "2377549739134050618": "2377549739134050618",
                "-5705391127436066304": "-5705391127436066304",
                "-5982585530852068518": "-5982585530852068518",
                "2222943758374923261": "2222943758374923261",
                "-5444411298146627108": "-5444411298146627108",
                "-922093528056623792": "-922093528056623792",
                "4642197505576805372": "4642197505576805372",
                "-977793872273910758": "-977793872273910758",
                "-8571336751105981898": "-8571336751105981898",
                "-4049018981015978582": "-4049018981015978582",
                "5027137721971879756": "5027137721971879756",
                "-6152083003904099787": "-6152083003904099787",
                "-8186396534710907514": "-8186396534710907514",
                "-7964902475512192266": "-7964902475512192266",
                "1900212269012524966": "1900212269012524966",
                "-5767142787509025403": "-5767142787509025403",
                "-6914964604685894176": "-6914964604685894176",
                "3864424412502107071": "3864424412502107071",
                "4085918471700822319": "4085918471700822319",
                "-4495710857484012065": "-4495710857484012065",
                "1885320776719621054": "1885320776719621054",
                "-6308530329092104544": "-6308530329092104544",
                "-6929856096978798088": "-6929856096978798088",
                "-4110770641088937681": "-4110770641088937681",
                "3156752706744634392": "3156752706744634392",
                "6963924612987258043": "6963924612987258043",
                "1343933235136541913": "1343933235136541913",
                "-2312842661773749114": "-2312842661773749114",
                "3541692923139708776": "3541692923139708776",
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
                "-5435404080443863626": "-5435404080443863626_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_9c4",
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
                "6756965012916871280": "6756965012916871280",
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
                "mixer": "B2/drive_mixer_7d2",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-5578710227748006758": "-5578710227748006758",
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
                "mixer": "B4/drive_mixer_bc5",
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
                "-2815184573587987978": "-2815184573587987978_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_ec8",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "6756965012916871280": {
            "length": 40,
            "waveforms": {
                "I": "6756965012916871280_i",
                "Q": "6756965012916871280_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5578710227748006758": {
            "length": 40,
            "waveforms": {
                "I": "-5578710227748006758_i",
                "Q": "-5578710227748006758_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1055980337815744117": {
            "length": 60,
            "waveforms": {
                "single": "-1055980337815744117",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5435404080443863626_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8113834294804231851_i",
                "Q": "8113834294804231851_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2815184573587987978_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7678708526067264968_i",
                "Q": "7678708526067264968_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3763186982338424024": {
            "length": 60,
            "waveforms": {
                "single": "3763186982338424024",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3398477494011678342": {
            "length": 16,
            "waveforms": {
                "single": "-3398477494011678342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3176983434812963094": {
            "length": 16,
            "waveforms": {
                "single": "-3176983434812963094",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "502514508191631430": {
            "length": 16,
            "waveforms": {
                "single": "502514508191631430",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4309686414434255081": {
            "length": 16,
            "waveforms": {
                "single": "4309686414434255081",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4174409242657499243": {
            "length": 16,
            "waveforms": {
                "single": "-4174409242657499243",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8652343453201336243": {
            "length": 16,
            "waveforms": {
                "single": "8652343453201336243",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6728940161636137192": {
            "length": 16,
            "waveforms": {
                "single": "6728940161636137192",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8154978072420277887": {
            "length": 16,
            "waveforms": {
                "single": "8154978072420277887",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4099380089457840758": {
            "length": 16,
            "waveforms": {
                "single": "4099380089457840758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8094006313286106866": {
            "length": 16,
            "waveforms": {
                "single": "-8094006313286106866",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8000372091661150530": {
            "length": 16,
            "waveforms": {
                "single": "8000372091661150530",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "333017035139600161": {
            "length": 16,
            "waveforms": {
                "single": "333017035139600161",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6916394479221779649": {
            "length": 16,
            "waveforms": {
                "single": "-6916394479221779649",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6694900420023064401": {
            "length": 16,
            "waveforms": {
                "single": "-6694900420023064401",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8385312308056224914": {
            "length": 16,
            "waveforms": {
                "single": "8385312308056224914",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8606806367254940162": {
            "length": 16,
            "waveforms": {
                "single": "8606806367254940162",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6282248285168103709": {
            "length": 16,
            "waveforms": {
                "single": "6282248285168103709",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5134426467991234936": {
            "length": 20,
            "waveforms": {
                "single": "5134426467991234936",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5355920527189950184": {
            "length": 20,
            "waveforms": {
                "single": "5355920527189950184",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2408968201424680245": {
            "length": 20,
            "waveforms": {
                "single": "-2408968201424680245",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3155322832208748919": {
            "length": 20,
            "waveforms": {
                "single": "3155322832208748919",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5519366684386309320": {
            "length": 24,
            "waveforms": {
                "single": "5519366684386309320",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5740860743585024568": {
            "length": 24,
            "waveforms": {
                "single": "5740860743585024568",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5119534975698331024": {
            "length": 24,
            "waveforms": {
                "single": "5119534975698331024",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7938620431588191431": {
            "length": 24,
            "waveforms": {
                "single": "7938620431588191431",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8160114490786906679": {
            "length": 28,
            "waveforms": {
                "single": "8160114490786906679",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5274913825094595839": {
            "length": 28,
            "waveforms": {
                "single": "-5274913825094595839",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5053419765895880591": {
            "length": 28,
            "waveforms": {
                "single": "-5053419765895880591",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-531101995805877275": {
            "length": 28,
            "waveforms": {
                "single": "-531101995805877275",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2855660077892713728": {
            "length": 32,
            "waveforms": {
                "single": "-2855660077892713728",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5208025746655007948": {
            "length": 32,
            "waveforms": {
                "single": "-5208025746655007948",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2377549739134050618": {
            "length": 32,
            "waveforms": {
                "single": "2377549739134050618",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5705391127436066304": {
            "length": 32,
            "waveforms": {
                "single": "-5705391127436066304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5982585530852068518": {
            "length": 36,
            "waveforms": {
                "single": "-5982585530852068518",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2222943758374923261": {
            "length": 36,
            "waveforms": {
                "single": "2222943758374923261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5444411298146627108": {
            "length": 36,
            "waveforms": {
                "single": "-5444411298146627108",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-922093528056623792": {
            "length": 36,
            "waveforms": {
                "single": "-922093528056623792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4642197505576805372": {
            "length": 40,
            "waveforms": {
                "single": "4642197505576805372",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-977793872273910758": {
            "length": 40,
            "waveforms": {
                "single": "-977793872273910758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8571336751105981898": {
            "length": 40,
            "waveforms": {
                "single": "-8571336751105981898",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4049018981015978582": {
            "length": 40,
            "waveforms": {
                "single": "-4049018981015978582",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5027137721971879756": {
            "length": 44,
            "waveforms": {
                "single": "5027137721971879756",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6152083003904099787": {
            "length": 44,
            "waveforms": {
                "single": "-6152083003904099787",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8186396534710907514": {
            "length": 44,
            "waveforms": {
                "single": "-8186396534710907514",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7964902475512192266": {
            "length": 44,
            "waveforms": {
                "single": "-7964902475512192266",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1900212269012524966": {
            "length": 48,
            "waveforms": {
                "single": "1900212269012524966",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5767142787509025403": {
            "length": 48,
            "waveforms": {
                "single": "-5767142787509025403",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6914964604685894176": {
            "length": 48,
            "waveforms": {
                "single": "-6914964604685894176",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3864424412502107071": {
            "length": 48,
            "waveforms": {
                "single": "3864424412502107071",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4085918471700822319": {
            "length": 52,
            "waveforms": {
                "single": "4085918471700822319",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4495710857484012065": {
            "length": 52,
            "waveforms": {
                "single": "-4495710857484012065",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1885320776719621054": {
            "length": 52,
            "waveforms": {
                "single": "1885320776719621054",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6308530329092104544": {
            "length": 52,
            "waveforms": {
                "single": "-6308530329092104544",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6929856096978798088": {
            "length": 56,
            "waveforms": {
                "single": "-6929856096978798088",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4110770641088937681": {
            "length": 56,
            "waveforms": {
                "single": "-4110770641088937681",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3156752706744634392": {
            "length": 56,
            "waveforms": {
                "single": "3156752706744634392",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6963924612987258043": {
            "length": 56,
            "waveforms": {
                "single": "6963924612987258043",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1343933235136541913": {
            "length": 60,
            "waveforms": {
                "single": "1343933235136541913",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2312842661773749114": {
            "length": 60,
            "waveforms": {
                "single": "-2312842661773749114",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3541692923139708776": {
            "length": 60,
            "waveforms": {
                "single": "3541692923139708776",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "6756965012916871280_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6756965012916871280_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5578710227748006758_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5578710227748006758_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1055980337815744117": {
            "type": "constant",
            "sample": -0.2388,
        },
        "8113834294804231851_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "8113834294804231851_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7678708526067264968_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "7678708526067264968_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3763186982338424024": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-3398477494011678342": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3176983434812963094": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "502514508191631430": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4309686414434255081": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4174409242657499243": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8652343453201336243": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6728940161636137192": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8154978072420277887": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4099380089457840758": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8094006313286106866": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8000372091661150530": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "333017035139600161": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6916394479221779649": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6694900420023064401": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8385312308056224914": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8606806367254940162": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6282248285168103709": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5134426467991234936": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5355920527189950184": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2408968201424680245": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3155322832208748919": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5519366684386309320": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5740860743585024568": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5119534975698331024": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7938620431588191431": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8160114490786906679": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5274913825094595839": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5053419765895880591": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-531101995805877275": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-2855660077892713728": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5208025746655007948": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2377549739134050618": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5705391127436066304": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-5982585530852068518": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2222943758374923261": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5444411298146627108": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-922093528056623792": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "4642197505576805372": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-977793872273910758": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8571336751105981898": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4049018981015978582": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5027137721971879756": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6152083003904099787": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8186396534710907514": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7964902475512192266": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1900212269012524966": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5767142787509025403": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6914964604685894176": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3864424412502107071": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "4085918471700822319": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4495710857484012065": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1885320776719621054": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6308530329092104544": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-6929856096978798088": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4110770641088937681": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3156752706744634392": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6963924612987258043": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1343933235136541913": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2312842661773749114": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3541692923139708776": {
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
        "B2/acquisition_mixer_9c4": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_7d2": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_bc5": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_ec8": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

