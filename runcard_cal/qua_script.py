
# Single QUA script generated at 2025-04-30 15:56:27.708028
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B1/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B3/acquisition")
    with for_(v1,0,(v1<256),(v1+1)):
        with for_(v8,0,(v8<=59),(v8+1)):
            with for_(v9,-1.99,(v9<-1.780414893617021),(v9+0.004234042553191486)):
                align()
                play("-2846668101335969838", "B1/drive")
                play("1775145310108305784", "B3/drive")
                wait(11, "B3/flux")
                with if_((v8==0), unsafe=True):
                    play("8349729268160923792"*amp(v9), "B3/flux")
                with elif_((v8==1)):
                    play("-5477163363365544448"*amp(v9), "B3/flux")
                with elif_((v8==2)):
                    play("-6196022803345318052"*amp(v9), "B3/flux")
                with elif_((v8==3)):
                    play("-7677761058346745713"*amp(v9), "B3/flux")
                with elif_((v8==4)):
                    play("-3998263115342151189"*amp(v9), "B3/flux")
                with elif_((v8==5)):
                    play("1953806141664386761"*amp(v9), "B3/flux")
                with elif_((v8==6)):
                    play("6476123911754390077"*amp(v9), "B3/flux")
                with elif_((v8==7)):
                    play("-5589588527751528420"*amp(v9), "B3/flux")
                with elif_((v8==8)):
                    play("4373059888866268872"*amp(v9), "B3/flux")
                with elif_((v8==9)):
                    play("-9061968427015233646"*amp(v9), "B3/flux")
                with elif_((v8==10)):
                    play("-8840474367816518398"*amp(v9), "B3/flux")
                with elif_((v8==11)):
                    play("-4318156597726515082"*amp(v9), "B3/flux")
                with elif_((v8==12)):
                    play("-6642714679813351535"*amp(v9), "B3/flux")
                with elif_((v8==13)):
                    play("-2120396909723348219"*amp(v9), "B3/flux")
                with elif_((v8==14)):
                    play("-8455534151421444014"*amp(v9), "B3/flux")
                with elif_((v8==15)):
                    play("1908269055717990680"*amp(v9), "B3/flux")
                with elif_((v8==16)):
                    play("1631074652301988466"*amp(v9), "B3/flux")
                with elif_((v8==17)):
                    play("-8610140132180571371"*amp(v9), "B3/flux")
                with elif_((v8==18)):
                    play("5532066654505298238"*amp(v9), "B3/flux")
                with elif_((v8==19)):
                    play("-9107505512961629727"*amp(v9), "B3/flux")
                with elif_((v8==20)):
                    play("-2162503304133027400"*amp(v9), "B3/flux")
                with elif_((v8==21)):
                    play("-1179170627150640162"*amp(v9), "B3/flux")
                with elif_((v8==22)):
                    play("-957676567951924914"*amp(v9), "B3/flux")
                with elif_((v8==23)):
                    play("3564641202138078402"*amp(v9), "B3/flux")
                with elif_((v8==24)):
                    play("1240083120051241949"*amp(v9), "B3/flux")
                with elif_((v8==25)):
                    play("2666121030835382644"*amp(v9), "B3/flux")
                with elif_((v8==26)):
                    play("6473292937078006295"*amp(v9), "B3/flux")
                with elif_((v8==27)):
                    play("6694786996276721543"*amp(v9), "B3/flux")
                with elif_((v8==28)):
                    play("-1886842332908112841"*amp(v9), "B3/flux")
                with elif_((v8==29)):
                    play("8892546684279888406"*amp(v9), "B3/flux")
                with elif_((v8==30)):
                    play("-5031879619339659894"*amp(v9), "B3/flux")
                with elif_((v8==31)):
                    play("-4320987572402898864"*amp(v9), "B3/flux")
                with elif_((v8==32)):
                    play("201330197687104452"*amp(v9), "B3/flux")
                with elif_((v8==33)):
                    play("3117949325670044919"*amp(v9), "B3/flux")
                with elif_((v8==34)):
                    play("-1901733825201016753"*amp(v9), "B3/flux")
                with elif_((v8==35)):
                    play("8351159142696809265"*amp(v9), "B3/flux")
                with elif_((v8==36)):
                    play("683804086175258896"*amp(v9), "B3/flux")
                with elif_((v8==37)):
                    play("-7897825243009575488"*amp(v9), "B3/flux")
                with elif_((v8==38)):
                    play("-7676331183810860240"*amp(v9), "B3/flux")
                with elif_((v8==39)):
                    play("-3869159277568236589"*amp(v9), "B3/flux")
                with elif_((v8==40)):
                    play("-2443121366784095894"*amp(v9), "B3/flux")
                with elif_((v8==41)):
                    play("-9117543471483581886"*amp(v9), "B3/flux")
                with elif_((v8==42)):
                    play("-245361678780929031"*amp(v9), "B3/flux")
                with elif_((v8==43)):
                    play("3561810227461694620"*amp(v9), "B3/flux")
                with elif_((v8==44)):
                    play("-3390398965212476084"*amp(v9), "B3/flux")
                with elif_((v8==45)):
                    play("2173892068420953080"*amp(v9), "B3/flux")
                with elif_((v8==46)):
                    play("7361775149858749894"*amp(v9), "B3/flux")
                with elif_((v8==47)):
                    play("7407101885447717426"*amp(v9), "B3/flux")
                with elif_((v8==48)):
                    play("-2834112899034842411"*amp(v9), "B3/flux")
                with elif_((v8==49)):
                    play("-8841882500258667327"*amp(v9), "B3/flux")
                with elif_((v8==50)):
                    play("7252495904688590069"*amp(v9), "B3/flux")
                with elif_((v8==51)):
                    play("1632504526837873939"*amp(v9), "B3/flux")
                with elif_((v8==52)):
                    play("5439676433080497590"*amp(v9), "B3/flux")
                with elif_((v8==53)):
                    play("-1234745671618988402"*amp(v9), "B3/flux")
                with elif_((v8==54)):
                    play("7637436121083664453"*amp(v9), "B3/flux")
                with elif_((v8==55)):
                    play("7858930180282379701"*amp(v9), "B3/flux")
                with elif_((v8==56)):
                    play("-5576098135599122817"*amp(v9), "B3/flux")
                with elif_((v8==57)):
                    play("-956246693416039441"*amp(v9), "B3/flux")
                with elif_((v8==58)):
                    play("8908868051108677791"*amp(v9), "B3/flux")
                with elif_((v8==59)):
                    play("-3156844388397240706"*amp(v9), "B3/flux")
                wait(11, "B1/acquisition")
                wait(11, "B3/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B1/acquisition")
                with else_():
                    wait((v8/4), "B1/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B3/acquisition")
                with else_():
                    wait((v8/4), "B3/acquisition")
                wait(4, "B1/acquisition")
                wait(4, "B3/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B3/drive")
                with else_():
                    wait((v8/4), "B3/drive")
                wait(4, "B3/drive")
                wait(11, "B1/acquisition")
                wait(11, "B3/acquisition")
                play("1775145310108305784", "B3/drive")
                measure("7818002711816239661", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.9967670294372607)-(v3*0.08034605794199916))>0.0007870074932508873)))
                r1 = declare_stream()
                save(v4, r1)
                measure("7251831333071778647", "B3/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*-0.8321494180571197)-(v6*-0.5545514818546579))>0.0026636797237234713)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("7818002711816239661_B1|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("7251831333071778647_B3|acquisition_shots")


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
            "operations": {
                "-3716934543172329159": "-3716934543172329159",
                "-2935350329198525458": "-2935350329198525458",
                "8349729268160923792": "8349729268160923792",
                "-5477163363365544448": "-5477163363365544448",
                "-6196022803345318052": "-6196022803345318052",
                "-7677761058346745713": "-7677761058346745713",
                "-3998263115342151189": "-3998263115342151189",
                "1953806141664386761": "1953806141664386761",
                "6476123911754390077": "6476123911754390077",
                "-5589588527751528420": "-5589588527751528420",
                "4373059888866268872": "4373059888866268872",
                "-9061968427015233646": "-9061968427015233646",
                "-8840474367816518398": "-8840474367816518398",
                "-4318156597726515082": "-4318156597726515082",
                "-6642714679813351535": "-6642714679813351535",
                "-2120396909723348219": "-2120396909723348219",
                "-8455534151421444014": "-8455534151421444014",
                "1908269055717990680": "1908269055717990680",
                "1631074652301988466": "1631074652301988466",
                "-8610140132180571371": "-8610140132180571371",
                "5532066654505298238": "5532066654505298238",
                "-9107505512961629727": "-9107505512961629727",
                "-2162503304133027400": "-2162503304133027400",
                "-1179170627150640162": "-1179170627150640162",
                "-957676567951924914": "-957676567951924914",
                "3564641202138078402": "3564641202138078402",
                "1240083120051241949": "1240083120051241949",
                "2666121030835382644": "2666121030835382644",
                "6473292937078006295": "6473292937078006295",
                "6694786996276721543": "6694786996276721543",
                "-1886842332908112841": "-1886842332908112841",
                "8892546684279888406": "8892546684279888406",
                "-5031879619339659894": "-5031879619339659894",
                "-4320987572402898864": "-4320987572402898864",
                "201330197687104452": "201330197687104452",
                "3117949325670044919": "3117949325670044919",
                "-1901733825201016753": "-1901733825201016753",
                "8351159142696809265": "8351159142696809265",
                "683804086175258896": "683804086175258896",
                "-7897825243009575488": "-7897825243009575488",
                "-7676331183810860240": "-7676331183810860240",
                "-3869159277568236589": "-3869159277568236589",
                "-2443121366784095894": "-2443121366784095894",
                "-9117543471483581886": "-9117543471483581886",
                "-245361678780929031": "-245361678780929031",
                "3561810227461694620": "3561810227461694620",
                "-3390398965212476084": "-3390398965212476084",
                "2173892068420953080": "2173892068420953080",
                "7361775149858749894": "7361775149858749894",
                "7407101885447717426": "7407101885447717426",
                "-2834112899034842411": "-2834112899034842411",
                "-8841882500258667327": "-8841882500258667327",
                "7252495904688590069": "7252495904688590069",
                "1632504526837873939": "1632504526837873939",
                "5439676433080497590": "5439676433080497590",
                "-1234745671618988402": "-1234745671618988402",
                "7637436121083664453": "7637436121083664453",
                "7858930180282379701": "7858930180282379701",
                "-5576098135599122817": "-5576098135599122817",
                "-956246693416039441": "-956246693416039441",
                "8908868051108677791": "8908868051108677791",
                "-3156844388397240706": "-3156844388397240706",
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
            "operations": {},
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
                "7251831333071778647": "7251831333071778647_B3/acquisition",
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
                "1775145310108305784": "1775145310108305784",
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
                "-2846668101335969838": "-2846668101335969838",
            },
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
                "7818002711816239661": "7818002711816239661_B1/acquisition",
            },
        },
    },
    "pulses": {
        "-2846668101335969838": {
            "length": 40,
            "waveforms": {
                "I": "-2846668101335969838_i",
                "Q": "-2846668101335969838_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1775145310108305784": {
            "length": 40,
            "waveforms": {
                "I": "1775145310108305784_i",
                "Q": "1775145310108305784_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3716934543172329159": {
            "length": 60,
            "waveforms": {
                "single": "-3716934543172329159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7818002711816239661_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1003284692977685823_i",
                "Q": "-1003284692977685823_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "7251831333071778647_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8963906277912727440_i",
                "Q": "8963906277912727440_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-2935350329198525458": {
            "length": 60,
            "waveforms": {
                "single": "-2935350329198525458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8349729268160923792": {
            "length": 16,
            "waveforms": {
                "single": "8349729268160923792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5477163363365544448": {
            "length": 16,
            "waveforms": {
                "single": "-5477163363365544448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6196022803345318052": {
            "length": 16,
            "waveforms": {
                "single": "-6196022803345318052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7677761058346745713": {
            "length": 16,
            "waveforms": {
                "single": "-7677761058346745713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3998263115342151189": {
            "length": 16,
            "waveforms": {
                "single": "-3998263115342151189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1953806141664386761": {
            "length": 16,
            "waveforms": {
                "single": "1953806141664386761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6476123911754390077": {
            "length": 16,
            "waveforms": {
                "single": "6476123911754390077",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5589588527751528420": {
            "length": 16,
            "waveforms": {
                "single": "-5589588527751528420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4373059888866268872": {
            "length": 16,
            "waveforms": {
                "single": "4373059888866268872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9061968427015233646": {
            "length": 16,
            "waveforms": {
                "single": "-9061968427015233646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8840474367816518398": {
            "length": 16,
            "waveforms": {
                "single": "-8840474367816518398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4318156597726515082": {
            "length": 16,
            "waveforms": {
                "single": "-4318156597726515082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6642714679813351535": {
            "length": 16,
            "waveforms": {
                "single": "-6642714679813351535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2120396909723348219": {
            "length": 16,
            "waveforms": {
                "single": "-2120396909723348219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8455534151421444014": {
            "length": 16,
            "waveforms": {
                "single": "-8455534151421444014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1908269055717990680": {
            "length": 16,
            "waveforms": {
                "single": "1908269055717990680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1631074652301988466": {
            "length": 16,
            "waveforms": {
                "single": "1631074652301988466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8610140132180571371": {
            "length": 20,
            "waveforms": {
                "single": "-8610140132180571371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5532066654505298238": {
            "length": 20,
            "waveforms": {
                "single": "5532066654505298238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9107505512961629727": {
            "length": 20,
            "waveforms": {
                "single": "-9107505512961629727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2162503304133027400": {
            "length": 20,
            "waveforms": {
                "single": "-2162503304133027400",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1179170627150640162": {
            "length": 24,
            "waveforms": {
                "single": "-1179170627150640162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-957676567951924914": {
            "length": 24,
            "waveforms": {
                "single": "-957676567951924914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3564641202138078402": {
            "length": 24,
            "waveforms": {
                "single": "3564641202138078402",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1240083120051241949": {
            "length": 24,
            "waveforms": {
                "single": "1240083120051241949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2666121030835382644": {
            "length": 28,
            "waveforms": {
                "single": "2666121030835382644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6473292937078006295": {
            "length": 28,
            "waveforms": {
                "single": "6473292937078006295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6694786996276721543": {
            "length": 28,
            "waveforms": {
                "single": "6694786996276721543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1886842332908112841": {
            "length": 28,
            "waveforms": {
                "single": "-1886842332908112841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8892546684279888406": {
            "length": 32,
            "waveforms": {
                "single": "8892546684279888406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5031879619339659894": {
            "length": 32,
            "waveforms": {
                "single": "-5031879619339659894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4320987572402898864": {
            "length": 32,
            "waveforms": {
                "single": "-4320987572402898864",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "201330197687104452": {
            "length": 32,
            "waveforms": {
                "single": "201330197687104452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3117949325670044919": {
            "length": 36,
            "waveforms": {
                "single": "3117949325670044919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1901733825201016753": {
            "length": 36,
            "waveforms": {
                "single": "-1901733825201016753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8351159142696809265": {
            "length": 36,
            "waveforms": {
                "single": "8351159142696809265",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "683804086175258896": {
            "length": 36,
            "waveforms": {
                "single": "683804086175258896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7897825243009575488": {
            "length": 40,
            "waveforms": {
                "single": "-7897825243009575488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7676331183810860240": {
            "length": 40,
            "waveforms": {
                "single": "-7676331183810860240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3869159277568236589": {
            "length": 40,
            "waveforms": {
                "single": "-3869159277568236589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2443121366784095894": {
            "length": 40,
            "waveforms": {
                "single": "-2443121366784095894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9117543471483581886": {
            "length": 44,
            "waveforms": {
                "single": "-9117543471483581886",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-245361678780929031": {
            "length": 44,
            "waveforms": {
                "single": "-245361678780929031",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3561810227461694620": {
            "length": 44,
            "waveforms": {
                "single": "3561810227461694620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3390398965212476084": {
            "length": 44,
            "waveforms": {
                "single": "-3390398965212476084",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2173892068420953080": {
            "length": 48,
            "waveforms": {
                "single": "2173892068420953080",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7361775149858749894": {
            "length": 48,
            "waveforms": {
                "single": "7361775149858749894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7407101885447717426": {
            "length": 48,
            "waveforms": {
                "single": "7407101885447717426",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2834112899034842411": {
            "length": 48,
            "waveforms": {
                "single": "-2834112899034842411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8841882500258667327": {
            "length": 52,
            "waveforms": {
                "single": "-8841882500258667327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7252495904688590069": {
            "length": 52,
            "waveforms": {
                "single": "7252495904688590069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1632504526837873939": {
            "length": 52,
            "waveforms": {
                "single": "1632504526837873939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5439676433080497590": {
            "length": 52,
            "waveforms": {
                "single": "5439676433080497590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1234745671618988402": {
            "length": 56,
            "waveforms": {
                "single": "-1234745671618988402",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7637436121083664453": {
            "length": 56,
            "waveforms": {
                "single": "7637436121083664453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7858930180282379701": {
            "length": 56,
            "waveforms": {
                "single": "7858930180282379701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5576098135599122817": {
            "length": 56,
            "waveforms": {
                "single": "-5576098135599122817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-956246693416039441": {
            "length": 60,
            "waveforms": {
                "single": "-956246693416039441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8908868051108677791": {
            "length": 60,
            "waveforms": {
                "single": "8908868051108677791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3156844388397240706": {
            "length": 60,
            "waveforms": {
                "single": "-3156844388397240706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2846668101335969838_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "-2846668101335969838_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "1775145310108305784_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "1775145310108305784_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "-3716934543172329159": {
            "sample": 0.21734999999999974,
            "type": "constant",
        },
        "-1003284692977685823_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-1003284692977685823_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8963906277912727440_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "8963906277912727440_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2935350329198525458": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "8349729268160923792": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5477163363365544448": {
            "samples": [0.11809045226130653] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6196022803345318052": {
            "samples": [0.11809045226130653] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-7677761058346745713": {
            "samples": [0.11809045226130653] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-3998263115342151189": {
            "samples": [0.11809045226130653] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1953806141664386761": {
            "samples": [0.11809045226130653] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "6476123911754390077": {
            "samples": [0.11809045226130653] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-5589588527751528420": {
            "samples": [0.11809045226130653] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "4373059888866268872": {
            "samples": [0.11809045226130653] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-9061968427015233646": {
            "samples": [0.11809045226130653] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8840474367816518398": {
            "samples": [0.11809045226130653] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-4318156597726515082": {
            "samples": [0.11809045226130653] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-6642714679813351535": {
            "samples": [0.11809045226130653] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-2120396909723348219": {
            "samples": [0.11809045226130653] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8455534151421444014": {
            "samples": [0.11809045226130653] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1908269055717990680": {
            "samples": [0.11809045226130653] * 15 + [0.0],
            "type": "arbitrary",
        },
        "1631074652301988466": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-8610140132180571371": {
            "samples": [0.11809045226130653] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5532066654505298238": {
            "samples": [0.11809045226130653] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9107505512961629727": {
            "samples": [0.11809045226130653] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2162503304133027400": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-1179170627150640162": {
            "samples": [0.11809045226130653] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-957676567951924914": {
            "samples": [0.11809045226130653] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3564641202138078402": {
            "samples": [0.11809045226130653] * 23 + [0.0],
            "type": "arbitrary",
        },
        "1240083120051241949": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "2666121030835382644": {
            "samples": [0.11809045226130653] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6473292937078006295": {
            "samples": [0.11809045226130653] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6694786996276721543": {
            "samples": [0.11809045226130653] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-1886842332908112841": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "8892546684279888406": {
            "samples": [0.11809045226130653] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5031879619339659894": {
            "samples": [0.11809045226130653] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4320987572402898864": {
            "samples": [0.11809045226130653] * 31 + [0.0],
            "type": "arbitrary",
        },
        "201330197687104452": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "3117949325670044919": {
            "samples": [0.11809045226130653] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1901733825201016753": {
            "samples": [0.11809045226130653] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8351159142696809265": {
            "samples": [0.11809045226130653] * 35 + [0.0],
            "type": "arbitrary",
        },
        "683804086175258896": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-7897825243009575488": {
            "samples": [0.11809045226130653] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7676331183810860240": {
            "samples": [0.11809045226130653] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3869159277568236589": {
            "samples": [0.11809045226130653] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-2443121366784095894": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-9117543471483581886": {
            "samples": [0.11809045226130653] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-245361678780929031": {
            "samples": [0.11809045226130653] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3561810227461694620": {
            "samples": [0.11809045226130653] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-3390398965212476084": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "2173892068420953080": {
            "samples": [0.11809045226130653] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7361775149858749894": {
            "samples": [0.11809045226130653] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7407101885447717426": {
            "samples": [0.11809045226130653] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2834112899034842411": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-8841882500258667327": {
            "samples": [0.11809045226130653] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7252495904688590069": {
            "samples": [0.11809045226130653] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1632504526837873939": {
            "samples": [0.11809045226130653] * 51 + [0.0],
            "type": "arbitrary",
        },
        "5439676433080497590": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-1234745671618988402": {
            "samples": [0.11809045226130653] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7637436121083664453": {
            "samples": [0.11809045226130653] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7858930180282379701": {
            "samples": [0.11809045226130653] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-5576098135599122817": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-956246693416039441": {
            "samples": [0.11809045226130653] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8908868051108677791": {
            "samples": [0.11809045226130653] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3156844388397240706": {
            "samples": [0.11809045226130653] * 59 + [0.0],
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
            "operations": {
                "-3716934543172329159": "-3716934543172329159",
                "-2935350329198525458": "-2935350329198525458",
                "8349729268160923792": "8349729268160923792",
                "-5477163363365544448": "-5477163363365544448",
                "-6196022803345318052": "-6196022803345318052",
                "-7677761058346745713": "-7677761058346745713",
                "-3998263115342151189": "-3998263115342151189",
                "1953806141664386761": "1953806141664386761",
                "6476123911754390077": "6476123911754390077",
                "-5589588527751528420": "-5589588527751528420",
                "4373059888866268872": "4373059888866268872",
                "-9061968427015233646": "-9061968427015233646",
                "-8840474367816518398": "-8840474367816518398",
                "-4318156597726515082": "-4318156597726515082",
                "-6642714679813351535": "-6642714679813351535",
                "-2120396909723348219": "-2120396909723348219",
                "-8455534151421444014": "-8455534151421444014",
                "1908269055717990680": "1908269055717990680",
                "1631074652301988466": "1631074652301988466",
                "-8610140132180571371": "-8610140132180571371",
                "5532066654505298238": "5532066654505298238",
                "-9107505512961629727": "-9107505512961629727",
                "-2162503304133027400": "-2162503304133027400",
                "-1179170627150640162": "-1179170627150640162",
                "-957676567951924914": "-957676567951924914",
                "3564641202138078402": "3564641202138078402",
                "1240083120051241949": "1240083120051241949",
                "2666121030835382644": "2666121030835382644",
                "6473292937078006295": "6473292937078006295",
                "6694786996276721543": "6694786996276721543",
                "-1886842332908112841": "-1886842332908112841",
                "8892546684279888406": "8892546684279888406",
                "-5031879619339659894": "-5031879619339659894",
                "-4320987572402898864": "-4320987572402898864",
                "201330197687104452": "201330197687104452",
                "3117949325670044919": "3117949325670044919",
                "-1901733825201016753": "-1901733825201016753",
                "8351159142696809265": "8351159142696809265",
                "683804086175258896": "683804086175258896",
                "-7897825243009575488": "-7897825243009575488",
                "-7676331183810860240": "-7676331183810860240",
                "-3869159277568236589": "-3869159277568236589",
                "-2443121366784095894": "-2443121366784095894",
                "-9117543471483581886": "-9117543471483581886",
                "-245361678780929031": "-245361678780929031",
                "3561810227461694620": "3561810227461694620",
                "-3390398965212476084": "-3390398965212476084",
                "2173892068420953080": "2173892068420953080",
                "7361775149858749894": "7361775149858749894",
                "7407101885447717426": "7407101885447717426",
                "-2834112899034842411": "-2834112899034842411",
                "-8841882500258667327": "-8841882500258667327",
                "7252495904688590069": "7252495904688590069",
                "1632504526837873939": "1632504526837873939",
                "5439676433080497590": "5439676433080497590",
                "-1234745671618988402": "-1234745671618988402",
                "7637436121083664453": "7637436121083664453",
                "7858930180282379701": "7858930180282379701",
                "-5576098135599122817": "-5576098135599122817",
                "-956246693416039441": "-956246693416039441",
                "8908868051108677791": "8908868051108677791",
                "-3156844388397240706": "-3156844388397240706",
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
                "7251831333071778647": "7251831333071778647_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_62d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "1775145310108305784": "1775145310108305784",
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
                "mixer": "B3/drive_mixer_ac2",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-2846668101335969838": "-2846668101335969838",
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
                "mixer": "B1/drive_mixer_2e2",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "7818002711816239661": "7818002711816239661_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_5ac",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
        },
    },
    "pulses": {
        "-2846668101335969838": {
            "length": 40,
            "waveforms": {
                "I": "-2846668101335969838_i",
                "Q": "-2846668101335969838_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1775145310108305784": {
            "length": 40,
            "waveforms": {
                "I": "1775145310108305784_i",
                "Q": "1775145310108305784_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3716934543172329159": {
            "length": 60,
            "waveforms": {
                "single": "-3716934543172329159",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7818002711816239661_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1003284692977685823_i",
                "Q": "-1003284692977685823_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7251831333071778647_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8963906277912727440_i",
                "Q": "8963906277912727440_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2935350329198525458": {
            "length": 60,
            "waveforms": {
                "single": "-2935350329198525458",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8349729268160923792": {
            "length": 16,
            "waveforms": {
                "single": "8349729268160923792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5477163363365544448": {
            "length": 16,
            "waveforms": {
                "single": "-5477163363365544448",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6196022803345318052": {
            "length": 16,
            "waveforms": {
                "single": "-6196022803345318052",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7677761058346745713": {
            "length": 16,
            "waveforms": {
                "single": "-7677761058346745713",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3998263115342151189": {
            "length": 16,
            "waveforms": {
                "single": "-3998263115342151189",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1953806141664386761": {
            "length": 16,
            "waveforms": {
                "single": "1953806141664386761",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6476123911754390077": {
            "length": 16,
            "waveforms": {
                "single": "6476123911754390077",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5589588527751528420": {
            "length": 16,
            "waveforms": {
                "single": "-5589588527751528420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4373059888866268872": {
            "length": 16,
            "waveforms": {
                "single": "4373059888866268872",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9061968427015233646": {
            "length": 16,
            "waveforms": {
                "single": "-9061968427015233646",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8840474367816518398": {
            "length": 16,
            "waveforms": {
                "single": "-8840474367816518398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4318156597726515082": {
            "length": 16,
            "waveforms": {
                "single": "-4318156597726515082",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6642714679813351535": {
            "length": 16,
            "waveforms": {
                "single": "-6642714679813351535",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2120396909723348219": {
            "length": 16,
            "waveforms": {
                "single": "-2120396909723348219",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8455534151421444014": {
            "length": 16,
            "waveforms": {
                "single": "-8455534151421444014",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1908269055717990680": {
            "length": 16,
            "waveforms": {
                "single": "1908269055717990680",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1631074652301988466": {
            "length": 16,
            "waveforms": {
                "single": "1631074652301988466",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8610140132180571371": {
            "length": 20,
            "waveforms": {
                "single": "-8610140132180571371",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5532066654505298238": {
            "length": 20,
            "waveforms": {
                "single": "5532066654505298238",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9107505512961629727": {
            "length": 20,
            "waveforms": {
                "single": "-9107505512961629727",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2162503304133027400": {
            "length": 20,
            "waveforms": {
                "single": "-2162503304133027400",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1179170627150640162": {
            "length": 24,
            "waveforms": {
                "single": "-1179170627150640162",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-957676567951924914": {
            "length": 24,
            "waveforms": {
                "single": "-957676567951924914",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3564641202138078402": {
            "length": 24,
            "waveforms": {
                "single": "3564641202138078402",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1240083120051241949": {
            "length": 24,
            "waveforms": {
                "single": "1240083120051241949",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2666121030835382644": {
            "length": 28,
            "waveforms": {
                "single": "2666121030835382644",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6473292937078006295": {
            "length": 28,
            "waveforms": {
                "single": "6473292937078006295",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6694786996276721543": {
            "length": 28,
            "waveforms": {
                "single": "6694786996276721543",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1886842332908112841": {
            "length": 28,
            "waveforms": {
                "single": "-1886842332908112841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8892546684279888406": {
            "length": 32,
            "waveforms": {
                "single": "8892546684279888406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5031879619339659894": {
            "length": 32,
            "waveforms": {
                "single": "-5031879619339659894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4320987572402898864": {
            "length": 32,
            "waveforms": {
                "single": "-4320987572402898864",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "201330197687104452": {
            "length": 32,
            "waveforms": {
                "single": "201330197687104452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3117949325670044919": {
            "length": 36,
            "waveforms": {
                "single": "3117949325670044919",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1901733825201016753": {
            "length": 36,
            "waveforms": {
                "single": "-1901733825201016753",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8351159142696809265": {
            "length": 36,
            "waveforms": {
                "single": "8351159142696809265",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "683804086175258896": {
            "length": 36,
            "waveforms": {
                "single": "683804086175258896",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7897825243009575488": {
            "length": 40,
            "waveforms": {
                "single": "-7897825243009575488",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7676331183810860240": {
            "length": 40,
            "waveforms": {
                "single": "-7676331183810860240",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3869159277568236589": {
            "length": 40,
            "waveforms": {
                "single": "-3869159277568236589",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2443121366784095894": {
            "length": 40,
            "waveforms": {
                "single": "-2443121366784095894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9117543471483581886": {
            "length": 44,
            "waveforms": {
                "single": "-9117543471483581886",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-245361678780929031": {
            "length": 44,
            "waveforms": {
                "single": "-245361678780929031",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3561810227461694620": {
            "length": 44,
            "waveforms": {
                "single": "3561810227461694620",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3390398965212476084": {
            "length": 44,
            "waveforms": {
                "single": "-3390398965212476084",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2173892068420953080": {
            "length": 48,
            "waveforms": {
                "single": "2173892068420953080",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7361775149858749894": {
            "length": 48,
            "waveforms": {
                "single": "7361775149858749894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7407101885447717426": {
            "length": 48,
            "waveforms": {
                "single": "7407101885447717426",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2834112899034842411": {
            "length": 48,
            "waveforms": {
                "single": "-2834112899034842411",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8841882500258667327": {
            "length": 52,
            "waveforms": {
                "single": "-8841882500258667327",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7252495904688590069": {
            "length": 52,
            "waveforms": {
                "single": "7252495904688590069",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1632504526837873939": {
            "length": 52,
            "waveforms": {
                "single": "1632504526837873939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5439676433080497590": {
            "length": 52,
            "waveforms": {
                "single": "5439676433080497590",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1234745671618988402": {
            "length": 56,
            "waveforms": {
                "single": "-1234745671618988402",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7637436121083664453": {
            "length": 56,
            "waveforms": {
                "single": "7637436121083664453",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7858930180282379701": {
            "length": 56,
            "waveforms": {
                "single": "7858930180282379701",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5576098135599122817": {
            "length": 56,
            "waveforms": {
                "single": "-5576098135599122817",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-956246693416039441": {
            "length": 60,
            "waveforms": {
                "single": "-956246693416039441",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8908868051108677791": {
            "length": 60,
            "waveforms": {
                "single": "8908868051108677791",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3156844388397240706": {
            "length": 60,
            "waveforms": {
                "single": "-3156844388397240706",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-2846668101335969838_i": {
            "type": "arbitrary",
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2846668101335969838_q": {
            "type": "arbitrary",
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1775145310108305784_i": {
            "type": "arbitrary",
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1775145310108305784_q": {
            "type": "arbitrary",
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3716934543172329159": {
            "type": "constant",
            "sample": 0.21734999999999974,
        },
        "-1003284692977685823_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-1003284692977685823_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8963906277912727440_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "8963906277912727440_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2935350329198525458": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "8349729268160923792": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5477163363365544448": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6196022803345318052": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7677761058346745713": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3998263115342151189": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1953806141664386761": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6476123911754390077": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5589588527751528420": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4373059888866268872": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9061968427015233646": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8840474367816518398": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4318156597726515082": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6642714679813351535": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2120396909723348219": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8455534151421444014": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1908269055717990680": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1631074652301988466": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-8610140132180571371": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5532066654505298238": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9107505512961629727": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2162503304133027400": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-1179170627150640162": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-957676567951924914": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3564641202138078402": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1240083120051241949": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "2666121030835382644": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6473292937078006295": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6694786996276721543": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1886842332908112841": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "8892546684279888406": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5031879619339659894": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4320987572402898864": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "201330197687104452": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "3117949325670044919": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1901733825201016753": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8351159142696809265": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "683804086175258896": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-7897825243009575488": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7676331183810860240": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3869159277568236589": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2443121366784095894": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-9117543471483581886": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-245361678780929031": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3561810227461694620": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3390398965212476084": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "2173892068420953080": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7361775149858749894": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7407101885447717426": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2834112899034842411": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-8841882500258667327": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7252495904688590069": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1632504526837873939": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5439676433080497590": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-1234745671618988402": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7637436121083664453": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7858930180282379701": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5576098135599122817": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-956246693416039441": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8908868051108677791": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3156844388397240706": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 59 + [0.0],
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
    },
    "mixers": {
        "B3/acquisition_mixer_62d": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_ac2": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_2e2": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_5ac": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

