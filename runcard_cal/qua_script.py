
# Single QUA script generated at 2025-02-17 13:35:00.101440
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
                play("-312816259730164655", "B2/drive")
                play("2780606365525313958", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("1581321951054567697"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("1802816010253282945"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-5962072718361347484"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("4000575698256449808"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("7807747604499073459"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("2187756226648357329"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-5405786652183713811"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("4385515914651524192"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("2033150245889229972"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("3459188156673370667"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("1535784865108171616"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-788773216978664837"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-8982624322790390435"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-8761130263591675187"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("8966754370138102825"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-6563370575588508324"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-5137332664804367629"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-1330160758561743978"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-1108666699363028730"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("867598929441422885"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("1089092988640138133"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-7104758117171587465"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("6322302805666902479"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-9207822140059708670"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("8520062493670069342"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("8741556552868784590"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("6707243022061976863"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-7119649609464491377"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("2745465135060225855"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("9126496769263858974"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("6774131100501564754"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("311319895565439832"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6900993557243810531"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-8048815374420679304"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-4241643468178055653"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-2815605557393914958"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-5629561627218797193"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-1822389720976173542"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-396351810192032847"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("7809177479034958932"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("1801407877811134016"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("5608579784053757667"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("5830073843252472915"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-3206597089644661475"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-4688335344646089136"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-166017574556085820"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-787343342442779364"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("5067192242470678526"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("2253236172645796291"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("2964128219582557321"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("7486445989672560637"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-180909066848989732"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-1328730884025858505"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-8541044336835108868"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-3529328579007059770"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-3307834519808344522"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("4897694769418647257"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-1110074831805177659"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-888580772606462411"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("1475463079571097990"*amp(v9), "B4/flux")
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
                play("2780606365525313958", "B4/drive")
                measure("-1352949204045139353", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-5045363561381052979", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("-1352949204045139353_B2|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("-5045363561381052979_B4|acquisition_shots")


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
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
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
                "4766638934335910714": "4766638934335910714",
                "8742986427404670063": "8742986427404670063",
                "1581321951054567697": "1581321951054567697",
                "1802816010253282945": "1802816010253282945",
                "-5962072718361347484": "-5962072718361347484",
                "4000575698256449808": "4000575698256449808",
                "7807747604499073459": "7807747604499073459",
                "2187756226648357329": "2187756226648357329",
                "-5405786652183713811": "-5405786652183713811",
                "4385515914651524192": "4385515914651524192",
                "2033150245889229972": "2033150245889229972",
                "3459188156673370667": "3459188156673370667",
                "1535784865108171616": "1535784865108171616",
                "-788773216978664837": "-788773216978664837",
                "-8982624322790390435": "-8982624322790390435",
                "-8761130263591675187": "-8761130263591675187",
                "8966754370138102825": "8966754370138102825",
                "-6563370575588508324": "-6563370575588508324",
                "-5137332664804367629": "-5137332664804367629",
                "-1330160758561743978": "-1330160758561743978",
                "-1108666699363028730": "-1108666699363028730",
                "867598929441422885": "867598929441422885",
                "1089092988640138133": "1089092988640138133",
                "-7104758117171587465": "-7104758117171587465",
                "6322302805666902479": "6322302805666902479",
                "-9207822140059708670": "-9207822140059708670",
                "8520062493670069342": "8520062493670069342",
                "8741556552868784590": "8741556552868784590",
                "6707243022061976863": "6707243022061976863",
                "-7119649609464491377": "-7119649609464491377",
                "2745465135060225855": "2745465135060225855",
                "9126496769263858974": "9126496769263858974",
                "6774131100501564754": "6774131100501564754",
                "311319895565439832": "311319895565439832",
                "-6900993557243810531": "-6900993557243810531",
                "-8048815374420679304": "-8048815374420679304",
                "-4241643468178055653": "-4241643468178055653",
                "-2815605557393914958": "-2815605557393914958",
                "-5629561627218797193": "-5629561627218797193",
                "-1822389720976173542": "-1822389720976173542",
                "-396351810192032847": "-396351810192032847",
                "7809177479034958932": "7809177479034958932",
                "1801407877811134016": "1801407877811134016",
                "5608579784053757667": "5608579784053757667",
                "5830073843252472915": "5830073843252472915",
                "-3206597089644661475": "-3206597089644661475",
                "-4688335344646089136": "-4688335344646089136",
                "-166017574556085820": "-166017574556085820",
                "-787343342442779364": "-787343342442779364",
                "5067192242470678526": "5067192242470678526",
                "2253236172645796291": "2253236172645796291",
                "2964128219582557321": "2964128219582557321",
                "7486445989672560637": "7486445989672560637",
                "-180909066848989732": "-180909066848989732",
                "-1328730884025858505": "-1328730884025858505",
                "-8541044336835108868": "-8541044336835108868",
                "-3529328579007059770": "-3529328579007059770",
                "-3307834519808344522": "-3307834519808344522",
                "4897694769418647257": "4897694769418647257",
                "-1110074831805177659": "-1110074831805177659",
                "-888580772606462411": "-888580772606462411",
                "1475463079571097990": "1475463079571097990",
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
                "-312816259730164655": "-312816259730164655",
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
                "-5045363561381052979": "-5045363561381052979_B4/acquisition",
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
                "2780606365525313958": "2780606365525313958",
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
                "-1352949204045139353": "-1352949204045139353_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-312816259730164655": {
            "length": 40,
            "waveforms": {
                "I": "-312816259730164655_i",
                "Q": "-312816259730164655_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2780606365525313958": {
            "length": 40,
            "waveforms": {
                "I": "2780606365525313958_i",
                "Q": "2780606365525313958_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4766638934335910714": {
            "length": 60,
            "waveforms": {
                "single": "4766638934335910714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1352949204045139353_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6047604451235621065_i",
                "Q": "6047604451235621065_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-5045363561381052979_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1214121299514286054_i",
                "Q": "1214121299514286054_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "8742986427404670063": {
            "length": 60,
            "waveforms": {
                "single": "8742986427404670063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1581321951054567697": {
            "length": 16,
            "waveforms": {
                "single": "1581321951054567697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1802816010253282945": {
            "length": 16,
            "waveforms": {
                "single": "1802816010253282945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5962072718361347484": {
            "length": 16,
            "waveforms": {
                "single": "-5962072718361347484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4000575698256449808": {
            "length": 16,
            "waveforms": {
                "single": "4000575698256449808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7807747604499073459": {
            "length": 16,
            "waveforms": {
                "single": "7807747604499073459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2187756226648357329": {
            "length": 16,
            "waveforms": {
                "single": "2187756226648357329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5405786652183713811": {
            "length": 16,
            "waveforms": {
                "single": "-5405786652183713811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4385515914651524192": {
            "length": 16,
            "waveforms": {
                "single": "4385515914651524192",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2033150245889229972": {
            "length": 16,
            "waveforms": {
                "single": "2033150245889229972",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3459188156673370667": {
            "length": 16,
            "waveforms": {
                "single": "3459188156673370667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1535784865108171616": {
            "length": 16,
            "waveforms": {
                "single": "1535784865108171616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-788773216978664837": {
            "length": 16,
            "waveforms": {
                "single": "-788773216978664837",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8982624322790390435": {
            "length": 16,
            "waveforms": {
                "single": "-8982624322790390435",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8761130263591675187": {
            "length": 16,
            "waveforms": {
                "single": "-8761130263591675187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8966754370138102825": {
            "length": 16,
            "waveforms": {
                "single": "8966754370138102825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6563370575588508324": {
            "length": 16,
            "waveforms": {
                "single": "-6563370575588508324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5137332664804367629": {
            "length": 16,
            "waveforms": {
                "single": "-5137332664804367629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1330160758561743978": {
            "length": 20,
            "waveforms": {
                "single": "-1330160758561743978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1108666699363028730": {
            "length": 20,
            "waveforms": {
                "single": "-1108666699363028730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "867598929441422885": {
            "length": 20,
            "waveforms": {
                "single": "867598929441422885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1089092988640138133": {
            "length": 20,
            "waveforms": {
                "single": "1089092988640138133",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7104758117171587465": {
            "length": 24,
            "waveforms": {
                "single": "-7104758117171587465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6322302805666902479": {
            "length": 24,
            "waveforms": {
                "single": "6322302805666902479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9207822140059708670": {
            "length": 24,
            "waveforms": {
                "single": "-9207822140059708670",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8520062493670069342": {
            "length": 24,
            "waveforms": {
                "single": "8520062493670069342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8741556552868784590": {
            "length": 28,
            "waveforms": {
                "single": "8741556552868784590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6707243022061976863": {
            "length": 28,
            "waveforms": {
                "single": "6707243022061976863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7119649609464491377": {
            "length": 28,
            "waveforms": {
                "single": "-7119649609464491377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2745465135060225855": {
            "length": 28,
            "waveforms": {
                "single": "2745465135060225855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9126496769263858974": {
            "length": 32,
            "waveforms": {
                "single": "9126496769263858974",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6774131100501564754": {
            "length": 32,
            "waveforms": {
                "single": "6774131100501564754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "311319895565439832": {
            "length": 32,
            "waveforms": {
                "single": "311319895565439832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6900993557243810531": {
            "length": 32,
            "waveforms": {
                "single": "-6900993557243810531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8048815374420679304": {
            "length": 36,
            "waveforms": {
                "single": "-8048815374420679304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4241643468178055653": {
            "length": 36,
            "waveforms": {
                "single": "-4241643468178055653",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2815605557393914958": {
            "length": 36,
            "waveforms": {
                "single": "-2815605557393914958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5629561627218797193": {
            "length": 36,
            "waveforms": {
                "single": "-5629561627218797193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1822389720976173542": {
            "length": 40,
            "waveforms": {
                "single": "-1822389720976173542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-396351810192032847": {
            "length": 40,
            "waveforms": {
                "single": "-396351810192032847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7809177479034958932": {
            "length": 40,
            "waveforms": {
                "single": "7809177479034958932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1801407877811134016": {
            "length": 40,
            "waveforms": {
                "single": "1801407877811134016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5608579784053757667": {
            "length": 44,
            "waveforms": {
                "single": "5608579784053757667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5830073843252472915": {
            "length": 44,
            "waveforms": {
                "single": "5830073843252472915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3206597089644661475": {
            "length": 44,
            "waveforms": {
                "single": "-3206597089644661475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4688335344646089136": {
            "length": 44,
            "waveforms": {
                "single": "-4688335344646089136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-166017574556085820": {
            "length": 48,
            "waveforms": {
                "single": "-166017574556085820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-787343342442779364": {
            "length": 48,
            "waveforms": {
                "single": "-787343342442779364",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5067192242470678526": {
            "length": 48,
            "waveforms": {
                "single": "5067192242470678526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2253236172645796291": {
            "length": 48,
            "waveforms": {
                "single": "2253236172645796291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2964128219582557321": {
            "length": 52,
            "waveforms": {
                "single": "2964128219582557321",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7486445989672560637": {
            "length": 52,
            "waveforms": {
                "single": "7486445989672560637",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-180909066848989732": {
            "length": 52,
            "waveforms": {
                "single": "-180909066848989732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1328730884025858505": {
            "length": 52,
            "waveforms": {
                "single": "-1328730884025858505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8541044336835108868": {
            "length": 56,
            "waveforms": {
                "single": "-8541044336835108868",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3529328579007059770": {
            "length": 56,
            "waveforms": {
                "single": "-3529328579007059770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3307834519808344522": {
            "length": 56,
            "waveforms": {
                "single": "-3307834519808344522",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4897694769418647257": {
            "length": 56,
            "waveforms": {
                "single": "4897694769418647257",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1110074831805177659": {
            "length": 60,
            "waveforms": {
                "single": "-1110074831805177659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-888580772606462411": {
            "length": 60,
            "waveforms": {
                "single": "-888580772606462411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1475463079571097990": {
            "length": 60,
            "waveforms": {
                "single": "1475463079571097990",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-312816259730164655_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-312816259730164655_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "2780606365525313958_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "2780606365525313958_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "4766638934335910714": {
            "sample": -0.2388,
            "type": "constant",
        },
        "6047604451235621065_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "6047604451235621065_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1214121299514286054_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1214121299514286054_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8742986427404670063": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1581321951054567697": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "1802816010253282945": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-5962072718361347484": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4000575698256449808": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "7807747604499073459": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "2187756226648357329": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-5405786652183713811": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "4385515914651524192": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "2033150245889229972": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3459188156673370667": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "1535784865108171616": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-788773216978664837": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-8982624322790390435": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8761130263591675187": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8966754370138102825": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6563370575588508324": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-5137332664804367629": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1330160758561743978": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1108666699363028730": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "867598929441422885": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "1089092988640138133": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7104758117171587465": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6322302805666902479": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9207822140059708670": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "8520062493670069342": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8741556552868784590": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6707243022061976863": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7119649609464491377": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2745465135060225855": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "9126496769263858974": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6774131100501564754": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "311319895565439832": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6900993557243810531": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8048815374420679304": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4241643468178055653": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2815605557393914958": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-5629561627218797193": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1822389720976173542": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-396351810192032847": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7809177479034958932": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "1801407877811134016": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5608579784053757667": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5830073843252472915": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3206597089644661475": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-4688335344646089136": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-166017574556085820": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-787343342442779364": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5067192242470678526": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "2253236172645796291": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2964128219582557321": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7486445989672560637": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-180909066848989732": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-1328730884025858505": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8541044336835108868": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3529328579007059770": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3307834519808344522": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "4897694769418647257": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1110074831805177659": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-888580772606462411": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1475463079571097990": {
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
                "4766638934335910714": "4766638934335910714",
                "8742986427404670063": "8742986427404670063",
                "1581321951054567697": "1581321951054567697",
                "1802816010253282945": "1802816010253282945",
                "-5962072718361347484": "-5962072718361347484",
                "4000575698256449808": "4000575698256449808",
                "7807747604499073459": "7807747604499073459",
                "2187756226648357329": "2187756226648357329",
                "-5405786652183713811": "-5405786652183713811",
                "4385515914651524192": "4385515914651524192",
                "2033150245889229972": "2033150245889229972",
                "3459188156673370667": "3459188156673370667",
                "1535784865108171616": "1535784865108171616",
                "-788773216978664837": "-788773216978664837",
                "-8982624322790390435": "-8982624322790390435",
                "-8761130263591675187": "-8761130263591675187",
                "8966754370138102825": "8966754370138102825",
                "-6563370575588508324": "-6563370575588508324",
                "-5137332664804367629": "-5137332664804367629",
                "-1330160758561743978": "-1330160758561743978",
                "-1108666699363028730": "-1108666699363028730",
                "867598929441422885": "867598929441422885",
                "1089092988640138133": "1089092988640138133",
                "-7104758117171587465": "-7104758117171587465",
                "6322302805666902479": "6322302805666902479",
                "-9207822140059708670": "-9207822140059708670",
                "8520062493670069342": "8520062493670069342",
                "8741556552868784590": "8741556552868784590",
                "6707243022061976863": "6707243022061976863",
                "-7119649609464491377": "-7119649609464491377",
                "2745465135060225855": "2745465135060225855",
                "9126496769263858974": "9126496769263858974",
                "6774131100501564754": "6774131100501564754",
                "311319895565439832": "311319895565439832",
                "-6900993557243810531": "-6900993557243810531",
                "-8048815374420679304": "-8048815374420679304",
                "-4241643468178055653": "-4241643468178055653",
                "-2815605557393914958": "-2815605557393914958",
                "-5629561627218797193": "-5629561627218797193",
                "-1822389720976173542": "-1822389720976173542",
                "-396351810192032847": "-396351810192032847",
                "7809177479034958932": "7809177479034958932",
                "1801407877811134016": "1801407877811134016",
                "5608579784053757667": "5608579784053757667",
                "5830073843252472915": "5830073843252472915",
                "-3206597089644661475": "-3206597089644661475",
                "-4688335344646089136": "-4688335344646089136",
                "-166017574556085820": "-166017574556085820",
                "-787343342442779364": "-787343342442779364",
                "5067192242470678526": "5067192242470678526",
                "2253236172645796291": "2253236172645796291",
                "2964128219582557321": "2964128219582557321",
                "7486445989672560637": "7486445989672560637",
                "-180909066848989732": "-180909066848989732",
                "-1328730884025858505": "-1328730884025858505",
                "-8541044336835108868": "-8541044336835108868",
                "-3529328579007059770": "-3529328579007059770",
                "-3307834519808344522": "-3307834519808344522",
                "4897694769418647257": "4897694769418647257",
                "-1110074831805177659": "-1110074831805177659",
                "-888580772606462411": "-888580772606462411",
                "1475463079571097990": "1475463079571097990",
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
                "-312816259730164655": "-312816259730164655",
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
                "mixer": "B2/drive_mixer_476",
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
                "-5045363561381052979": "-5045363561381052979_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_643",
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
                "2780606365525313958": "2780606365525313958",
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
                "mixer": "B4/drive_mixer_410",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-1352949204045139353": "-1352949204045139353_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_486",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "-312816259730164655": {
            "length": 40,
            "waveforms": {
                "I": "-312816259730164655_i",
                "Q": "-312816259730164655_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2780606365525313958": {
            "length": 40,
            "waveforms": {
                "I": "2780606365525313958_i",
                "Q": "2780606365525313958_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4766638934335910714": {
            "length": 60,
            "waveforms": {
                "single": "4766638934335910714",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1352949204045139353_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6047604451235621065_i",
                "Q": "6047604451235621065_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5045363561381052979_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1214121299514286054_i",
                "Q": "1214121299514286054_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8742986427404670063": {
            "length": 60,
            "waveforms": {
                "single": "8742986427404670063",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1581321951054567697": {
            "length": 16,
            "waveforms": {
                "single": "1581321951054567697",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1802816010253282945": {
            "length": 16,
            "waveforms": {
                "single": "1802816010253282945",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5962072718361347484": {
            "length": 16,
            "waveforms": {
                "single": "-5962072718361347484",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4000575698256449808": {
            "length": 16,
            "waveforms": {
                "single": "4000575698256449808",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7807747604499073459": {
            "length": 16,
            "waveforms": {
                "single": "7807747604499073459",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2187756226648357329": {
            "length": 16,
            "waveforms": {
                "single": "2187756226648357329",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5405786652183713811": {
            "length": 16,
            "waveforms": {
                "single": "-5405786652183713811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4385515914651524192": {
            "length": 16,
            "waveforms": {
                "single": "4385515914651524192",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2033150245889229972": {
            "length": 16,
            "waveforms": {
                "single": "2033150245889229972",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3459188156673370667": {
            "length": 16,
            "waveforms": {
                "single": "3459188156673370667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1535784865108171616": {
            "length": 16,
            "waveforms": {
                "single": "1535784865108171616",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-788773216978664837": {
            "length": 16,
            "waveforms": {
                "single": "-788773216978664837",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8982624322790390435": {
            "length": 16,
            "waveforms": {
                "single": "-8982624322790390435",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8761130263591675187": {
            "length": 16,
            "waveforms": {
                "single": "-8761130263591675187",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8966754370138102825": {
            "length": 16,
            "waveforms": {
                "single": "8966754370138102825",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6563370575588508324": {
            "length": 16,
            "waveforms": {
                "single": "-6563370575588508324",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5137332664804367629": {
            "length": 16,
            "waveforms": {
                "single": "-5137332664804367629",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1330160758561743978": {
            "length": 20,
            "waveforms": {
                "single": "-1330160758561743978",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1108666699363028730": {
            "length": 20,
            "waveforms": {
                "single": "-1108666699363028730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "867598929441422885": {
            "length": 20,
            "waveforms": {
                "single": "867598929441422885",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1089092988640138133": {
            "length": 20,
            "waveforms": {
                "single": "1089092988640138133",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7104758117171587465": {
            "length": 24,
            "waveforms": {
                "single": "-7104758117171587465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6322302805666902479": {
            "length": 24,
            "waveforms": {
                "single": "6322302805666902479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9207822140059708670": {
            "length": 24,
            "waveforms": {
                "single": "-9207822140059708670",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8520062493670069342": {
            "length": 24,
            "waveforms": {
                "single": "8520062493670069342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8741556552868784590": {
            "length": 28,
            "waveforms": {
                "single": "8741556552868784590",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6707243022061976863": {
            "length": 28,
            "waveforms": {
                "single": "6707243022061976863",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7119649609464491377": {
            "length": 28,
            "waveforms": {
                "single": "-7119649609464491377",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2745465135060225855": {
            "length": 28,
            "waveforms": {
                "single": "2745465135060225855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9126496769263858974": {
            "length": 32,
            "waveforms": {
                "single": "9126496769263858974",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6774131100501564754": {
            "length": 32,
            "waveforms": {
                "single": "6774131100501564754",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "311319895565439832": {
            "length": 32,
            "waveforms": {
                "single": "311319895565439832",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6900993557243810531": {
            "length": 32,
            "waveforms": {
                "single": "-6900993557243810531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8048815374420679304": {
            "length": 36,
            "waveforms": {
                "single": "-8048815374420679304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4241643468178055653": {
            "length": 36,
            "waveforms": {
                "single": "-4241643468178055653",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2815605557393914958": {
            "length": 36,
            "waveforms": {
                "single": "-2815605557393914958",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5629561627218797193": {
            "length": 36,
            "waveforms": {
                "single": "-5629561627218797193",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1822389720976173542": {
            "length": 40,
            "waveforms": {
                "single": "-1822389720976173542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-396351810192032847": {
            "length": 40,
            "waveforms": {
                "single": "-396351810192032847",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7809177479034958932": {
            "length": 40,
            "waveforms": {
                "single": "7809177479034958932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1801407877811134016": {
            "length": 40,
            "waveforms": {
                "single": "1801407877811134016",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5608579784053757667": {
            "length": 44,
            "waveforms": {
                "single": "5608579784053757667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5830073843252472915": {
            "length": 44,
            "waveforms": {
                "single": "5830073843252472915",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3206597089644661475": {
            "length": 44,
            "waveforms": {
                "single": "-3206597089644661475",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4688335344646089136": {
            "length": 44,
            "waveforms": {
                "single": "-4688335344646089136",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-166017574556085820": {
            "length": 48,
            "waveforms": {
                "single": "-166017574556085820",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-787343342442779364": {
            "length": 48,
            "waveforms": {
                "single": "-787343342442779364",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5067192242470678526": {
            "length": 48,
            "waveforms": {
                "single": "5067192242470678526",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2253236172645796291": {
            "length": 48,
            "waveforms": {
                "single": "2253236172645796291",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2964128219582557321": {
            "length": 52,
            "waveforms": {
                "single": "2964128219582557321",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7486445989672560637": {
            "length": 52,
            "waveforms": {
                "single": "7486445989672560637",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-180909066848989732": {
            "length": 52,
            "waveforms": {
                "single": "-180909066848989732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1328730884025858505": {
            "length": 52,
            "waveforms": {
                "single": "-1328730884025858505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8541044336835108868": {
            "length": 56,
            "waveforms": {
                "single": "-8541044336835108868",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3529328579007059770": {
            "length": 56,
            "waveforms": {
                "single": "-3529328579007059770",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3307834519808344522": {
            "length": 56,
            "waveforms": {
                "single": "-3307834519808344522",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4897694769418647257": {
            "length": 56,
            "waveforms": {
                "single": "4897694769418647257",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1110074831805177659": {
            "length": 60,
            "waveforms": {
                "single": "-1110074831805177659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-888580772606462411": {
            "length": 60,
            "waveforms": {
                "single": "-888580772606462411",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1475463079571097990": {
            "length": 60,
            "waveforms": {
                "single": "1475463079571097990",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-312816259730164655_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-312816259730164655_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2780606365525313958_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2780606365525313958_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4766638934335910714": {
            "type": "constant",
            "sample": -0.2388,
        },
        "6047604451235621065_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "6047604451235621065_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "1214121299514286054_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "1214121299514286054_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8742986427404670063": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1581321951054567697": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1802816010253282945": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5962072718361347484": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4000575698256449808": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7807747604499073459": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2187756226648357329": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5405786652183713811": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4385515914651524192": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2033150245889229972": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3459188156673370667": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1535784865108171616": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-788773216978664837": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8982624322790390435": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8761130263591675187": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8966754370138102825": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6563370575588508324": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5137332664804367629": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-1330160758561743978": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1108666699363028730": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "867598929441422885": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1089092988640138133": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-7104758117171587465": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6322302805666902479": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9207822140059708670": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8520062493670069342": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8741556552868784590": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6707243022061976863": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7119649609464491377": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2745465135060225855": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "9126496769263858974": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6774131100501564754": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "311319895565439832": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6900993557243810531": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-8048815374420679304": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4241643468178055653": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2815605557393914958": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5629561627218797193": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-1822389720976173542": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-396351810192032847": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7809177479034958932": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1801407877811134016": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5608579784053757667": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5830073843252472915": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3206597089644661475": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4688335344646089136": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-166017574556085820": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-787343342442779364": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5067192242470678526": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2253236172645796291": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "2964128219582557321": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7486445989672560637": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-180909066848989732": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1328730884025858505": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-8541044336835108868": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3529328579007059770": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3307834519808344522": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4897694769418647257": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-1110074831805177659": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-888580772606462411": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1475463079571097990": {
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
        "B2/drive_mixer_476": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_643": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_410": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_486": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

