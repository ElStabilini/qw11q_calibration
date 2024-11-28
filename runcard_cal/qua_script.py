
# Single QUA script generated at 2024-11-28 08:52:25.856513
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(int, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "D1/acquisition")
    with for_(v1,0,(v1<3000),(v1+1)):
        with for_(v5,0,(v5<=79),(v5+1)):
            align()
            with if_((v5==0), unsafe=True):
                play("-5399356442740566797", "D1/drive")
            with elif_((v5==1)):
                play("-6020682210627260341", "D1/drive")
            with elif_((v5==2)):
                play("5176650348720911465", "D1/drive")
            with elif_((v5==3)):
                play("-2490704707800638904", "D1/drive")
            with elif_((v5==4)):
                play("2031613062289364412", "D1/drive")
            with elif_((v5==5)):
                play("2253107121488079660", "D1/drive")
            with elif_((v5==6)):
                play("-71450960598756793", "D1/drive")
            with elif_((v5==7)):
                play("-8265302066410482391", "D1/drive")
            with elif_((v5==8)):
                play("5161758856428007553", "D1/drive")
            with elif_((v5==9)):
                play("-8762667447191540747", "D1/drive")
            with elif_((v5==10)):
                play("-5846048319208600280", "D1/drive")
            with elif_((v5==11)):
                play("-6564907759188373884", "D1/drive")
            with elif_((v5==12)):
                play("-612838502181835934", "D1/drive")
            with elif_((v5==13)):
                play("1862115589237333143", "D1/drive")
            with elif_((v5==14)):
                play("1584921185821330929", "D1/drive")
            with elif_((v5==15)):
                play("5392093092063954580", "D1/drive")
            with elif_((v5==16)):
                play("1087555805040272573", "D1/drive")
            with elif_((v5==17)):
                play("-1264809863722021647", "D1/drive")
            with elif_((v5==18)):
                play("-3201589722435749314", "D1/drive")
            with elif_((v5==19)):
                play("-9209359323659574230", "D1/drive")
            with elif_((v5==20)):
                play("-5402187417416950579", "D1/drive")
            with elif_((v5==21)):
                play("-879869647326947263", "D1/drive")
            with elif_((v5==22)):
                play("-658375588128232015", "D1/drive")
            with elif_((v5==23)):
                play("-1778389818629643021", "D1/drive")
            with elif_((v5==24)):
                play("-4130755487391937241", "D1/drive")
            with elif_((v5==25)):
                play("6648633529796064006", "D1/drive")
            with elif_((v5==26)):
                play("-7275792773823484294", "D1/drive")
            with elif_((v5==27)):
                play("-1711501740190055130", "D1/drive")
            with elif_((v5==28)):
                play("-3745815270996862857", "D1/drive")
            with elif_((v5==29)):
                play("-3524321211798147609", "D1/drive")
            with elif_((v5==30)):
                play("155176731206446915", "D1/drive")
            with elif_((v5==31)):
                play("-1326561523794980746", "D1/drive")
            with elif_((v5==32)):
                play("-1105067464596265498", "D1/drive")
            with elif_((v5==33)):
                play("3906648293231783600", "D1/drive")
            with elif_((v5==34)):
                play("8526499735414866976", "D1/drive")
            with elif_((v5==35)):
                play("6104407981234950463", "D1/drive")
            with elif_((v5==36)):
                play("6325902040433665711", "D1/drive")
            with elif_((v5==37)):
                play("-7598524263185882589", "D1/drive")
            with elif_((v5==38)):
                play("-2489274833264753431", "D1/drive")
            with elif_((v5==39)):
                play("-4412678124829952482", "D1/drive")
            with elif_((v5==40)):
                play("-4689872528245954696", "D1/drive")
            with elif_((v5==41)):
                play("-70021086062871320", "D1/drive")
            with elif_((v5==42)):
                play("53939301042763868", "D1/drive")
            with elif_((v5==43)):
                play("8259468590269755647", "D1/drive")
            with elif_((v5==44)):
                play("-4622984449806366805", "D1/drive")
            with elif_((v5==45)):
                play("314919130332203064", "D1/drive")
            with elif_((v5==46)):
                play("-2037446538430091156", "D1/drive")
            with elif_((v5==47)):
                play("-5009766010630318589", "D1/drive")
            with elif_((v5==48)):
                play("-4238044233411292421", "D1/drive")
            with elif_((v5==49)):
                play("-2812006322627151726", "D1/drive")
            with elif_((v5==50)):
                play("5393522966599840053", "D1/drive")
            with elif_((v5==51)):
                play("5615017025798555301", "D1/drive")
            with elif_((v5==52)):
                play("3192925271618638788", "D1/drive")
            with elif_((v5==53)):
                play("7812776713801722164", "D1/drive")
            with elif_((v5==54)):
                play("2266597513640485263", "D1/drive")
            with elif_((v5==55)):
                play("-5400757542881065106", "D1/drive")
            with elif_((v5==56)):
                play("7038216929604661594", "D1/drive")
            with elif_((v5==57)):
                play("-3202997854877898243", "D1/drive")
            with elif_((v5==58)):
                play("-2981503795679182995", "D1/drive")
            with elif_((v5==59)):
                play("2873031789234274895", "D1/drive")
            with elif_((v5==60)):
                play("-783744107676016132", "D1/drive")
            with elif_((v5==61)):
                play("5070791477237441758", "D1/drive")
            with elif_((v5==62)):
                play("4449465709350748214", "D1/drive")
            with elif_((v5==63)):
                play("4670959768549463462", "D1/drive")
            with elif_((v5==64)):
                play("-3522891337262262136", "D1/drive")
            with elif_((v5==65)):
                play("6868719456552630325", "D1/drive")
            with elif_((v5==66)):
                play("-1325131649259095273", "D1/drive")
            with elif_((v5==67)):
                play("5055899984944537846", "D1/drive")
            with elif_((v5==68)):
                play("-1822497030040153629", "D1/drive")
            with elif_((v5==69)):
                play("-3304235285041581290", "D1/drive")
            with elif_((v5==70)):
                play("4901294004185410489", "D1/drive")
            with elif_((v5==71)):
                play("6327331914969551184", "D1/drive")
            with elif_((v5==72)):
                play("-8312240252497376781", "D1/drive")
            with elif_((v5==73)):
                play("8525091602972718047", "D1/drive")
            with elif_((v5==74)):
                play("-6114480564494209918", "D1/drive")
            with elif_((v5==75)):
                play("-4688442653710069223", "D1/drive")
            with elif_((v5==76)):
                play("-7040808322472363443", "D1/drive")
            with elif_((v5==77)):
                play("2035348380515494895", "D1/drive")
            with elif_((v5==78)):
                play("-2269188906508187112", "D1/drive")
            with elif_((v5==79)):
                play("1537982999734436539", "D1/drive")
            with if_(((v5/4)<4)):
                wait(4, "D1/acquisition")
            with else_():
                wait((v5/4), "D1/acquisition")
            measure("-8235708793481200348", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            assign(v4, Cast.to_int((((v2*0.9832190513468051)-(v3*-0.1824288822217816))>0.0011543927554382514)))
            r1 = declare_stream()
            save(v4, r1)
            wait(12500, )
    with stream_processing():
        r1.buffer(80).buffer(3000).save("-8235708793481200348_D1|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
                "7": {
                    "offset": -0.04,
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
        "con6": {
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
    },
    "octaves": {
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
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
        "D5/flux": {
            "singleInput": {
                "port": ('con9', 7),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D1/acquisition": {
            "RF_inputs": {
                "port": ('octave5', 1),
            },
            "RF_outputs": {
                "port": ('octave5', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -312360584.50398064,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-8235708793481200348": "-8235708793481200348_D1/acquisition",
            },
        },
        "D1/drive": {
            "RF_inputs": {
                "port": ('octave5', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-4689872528245954696": "-4689872528245954696",
                "-5399356442740566797": "-5399356442740566797",
                "-6020682210627260341": "-6020682210627260341",
                "5176650348720911465": "5176650348720911465",
                "-2490704707800638904": "-2490704707800638904",
                "2031613062289364412": "2031613062289364412",
                "2253107121488079660": "2253107121488079660",
                "-71450960598756793": "-71450960598756793",
                "-8265302066410482391": "-8265302066410482391",
                "5161758856428007553": "5161758856428007553",
                "-8762667447191540747": "-8762667447191540747",
                "-5846048319208600280": "-5846048319208600280",
                "-6564907759188373884": "-6564907759188373884",
                "-612838502181835934": "-612838502181835934",
                "1862115589237333143": "1862115589237333143",
                "1584921185821330929": "1584921185821330929",
                "5392093092063954580": "5392093092063954580",
                "1087555805040272573": "1087555805040272573",
                "-1264809863722021647": "-1264809863722021647",
                "-3201589722435749314": "-3201589722435749314",
                "-9209359323659574230": "-9209359323659574230",
                "-5402187417416950579": "-5402187417416950579",
                "-879869647326947263": "-879869647326947263",
                "-658375588128232015": "-658375588128232015",
                "-1778389818629643021": "-1778389818629643021",
                "-4130755487391937241": "-4130755487391937241",
                "6648633529796064006": "6648633529796064006",
                "-7275792773823484294": "-7275792773823484294",
                "-1711501740190055130": "-1711501740190055130",
                "-3745815270996862857": "-3745815270996862857",
                "-3524321211798147609": "-3524321211798147609",
                "155176731206446915": "155176731206446915",
                "-1326561523794980746": "-1326561523794980746",
                "-1105067464596265498": "-1105067464596265498",
                "3906648293231783600": "3906648293231783600",
                "8526499735414866976": "8526499735414866976",
                "6104407981234950463": "6104407981234950463",
                "6325902040433665711": "6325902040433665711",
                "-7598524263185882589": "-7598524263185882589",
                "-2489274833264753431": "-2489274833264753431",
                "-4412678124829952482": "-4412678124829952482",
                "-70021086062871320": "-70021086062871320",
                "53939301042763868": "53939301042763868",
                "8259468590269755647": "8259468590269755647",
                "-4622984449806366805": "-4622984449806366805",
                "314919130332203064": "314919130332203064",
                "-2037446538430091156": "-2037446538430091156",
                "-5009766010630318589": "-5009766010630318589",
                "-4238044233411292421": "-4238044233411292421",
                "-2812006322627151726": "-2812006322627151726",
                "5393522966599840053": "5393522966599840053",
                "5615017025798555301": "5615017025798555301",
                "3192925271618638788": "3192925271618638788",
                "7812776713801722164": "7812776713801722164",
                "2266597513640485263": "2266597513640485263",
                "-5400757542881065106": "-5400757542881065106",
                "7038216929604661594": "7038216929604661594",
                "-3202997854877898243": "-3202997854877898243",
                "-2981503795679182995": "-2981503795679182995",
                "2873031789234274895": "2873031789234274895",
                "-783744107676016132": "-783744107676016132",
                "5070791477237441758": "5070791477237441758",
                "4449465709350748214": "4449465709350748214",
                "4670959768549463462": "4670959768549463462",
                "-3522891337262262136": "-3522891337262262136",
                "6868719456552630325": "6868719456552630325",
                "-1325131649259095273": "-1325131649259095273",
                "5055899984944537846": "5055899984944537846",
                "-1822497030040153629": "-1822497030040153629",
                "-3304235285041581290": "-3304235285041581290",
                "4901294004185410489": "4901294004185410489",
                "6327331914969551184": "6327331914969551184",
                "-8312240252497376781": "-8312240252497376781",
                "8525091602972718047": "8525091602972718047",
                "-6114480564494209918": "-6114480564494209918",
                "-4688442653710069223": "-4688442653710069223",
                "-7040808322472363443": "-7040808322472363443",
                "2035348380515494895": "2035348380515494895",
                "-2269188906508187112": "-2269188906508187112",
                "1537982999734436539": "1537982999734436539",
            },
        },
    },
    "pulses": {
        "-4689872528245954696": {
            "length": 40,
            "waveforms": {
                "I": "-4689872528245954696_i",
                "Q": "-4689872528245954696_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8235708793481200348_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5725775278552983433_i",
                "Q": "-5725775278552983433_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "-5399356442740566797": {
            "length": 16,
            "waveforms": {
                "I": "-5399356442740566797_i",
                "Q": "-5399356442740566797_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6020682210627260341": {
            "length": 16,
            "waveforms": {
                "I": "-6020682210627260341_i",
                "Q": "-6020682210627260341_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5176650348720911465": {
            "length": 16,
            "waveforms": {
                "I": "5176650348720911465_i",
                "Q": "5176650348720911465_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2490704707800638904": {
            "length": 16,
            "waveforms": {
                "I": "-2490704707800638904_i",
                "Q": "-2490704707800638904_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2031613062289364412": {
            "length": 16,
            "waveforms": {
                "I": "2031613062289364412_i",
                "Q": "2031613062289364412_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2253107121488079660": {
            "length": 16,
            "waveforms": {
                "I": "2253107121488079660_i",
                "Q": "2253107121488079660_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-71450960598756793": {
            "length": 16,
            "waveforms": {
                "I": "-71450960598756793_i",
                "Q": "-71450960598756793_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8265302066410482391": {
            "length": 16,
            "waveforms": {
                "I": "-8265302066410482391_i",
                "Q": "-8265302066410482391_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5161758856428007553": {
            "length": 16,
            "waveforms": {
                "I": "5161758856428007553_i",
                "Q": "5161758856428007553_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8762667447191540747": {
            "length": 16,
            "waveforms": {
                "I": "-8762667447191540747_i",
                "Q": "-8762667447191540747_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5846048319208600280": {
            "length": 16,
            "waveforms": {
                "I": "-5846048319208600280_i",
                "Q": "-5846048319208600280_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6564907759188373884": {
            "length": 16,
            "waveforms": {
                "I": "-6564907759188373884_i",
                "Q": "-6564907759188373884_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-612838502181835934": {
            "length": 16,
            "waveforms": {
                "I": "-612838502181835934_i",
                "Q": "-612838502181835934_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1862115589237333143": {
            "length": 16,
            "waveforms": {
                "I": "1862115589237333143_i",
                "Q": "1862115589237333143_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1584921185821330929": {
            "length": 16,
            "waveforms": {
                "I": "1584921185821330929_i",
                "Q": "1584921185821330929_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5392093092063954580": {
            "length": 16,
            "waveforms": {
                "I": "5392093092063954580_i",
                "Q": "5392093092063954580_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1087555805040272573": {
            "length": 16,
            "waveforms": {
                "I": "1087555805040272573_i",
                "Q": "1087555805040272573_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1264809863722021647": {
            "length": 20,
            "waveforms": {
                "I": "-1264809863722021647_i",
                "Q": "-1264809863722021647_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3201589722435749314": {
            "length": 20,
            "waveforms": {
                "I": "-3201589722435749314_i",
                "Q": "-3201589722435749314_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9209359323659574230": {
            "length": 20,
            "waveforms": {
                "I": "-9209359323659574230_i",
                "Q": "-9209359323659574230_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5402187417416950579": {
            "length": 20,
            "waveforms": {
                "I": "-5402187417416950579_i",
                "Q": "-5402187417416950579_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-879869647326947263": {
            "length": 24,
            "waveforms": {
                "I": "-879869647326947263_i",
                "Q": "-879869647326947263_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-658375588128232015": {
            "length": 24,
            "waveforms": {
                "I": "-658375588128232015_i",
                "Q": "-658375588128232015_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1778389818629643021": {
            "length": 24,
            "waveforms": {
                "I": "-1778389818629643021_i",
                "Q": "-1778389818629643021_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4130755487391937241": {
            "length": 24,
            "waveforms": {
                "I": "-4130755487391937241_i",
                "Q": "-4130755487391937241_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6648633529796064006": {
            "length": 28,
            "waveforms": {
                "I": "6648633529796064006_i",
                "Q": "6648633529796064006_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7275792773823484294": {
            "length": 28,
            "waveforms": {
                "I": "-7275792773823484294_i",
                "Q": "-7275792773823484294_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1711501740190055130": {
            "length": 28,
            "waveforms": {
                "I": "-1711501740190055130_i",
                "Q": "-1711501740190055130_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3745815270996862857": {
            "length": 28,
            "waveforms": {
                "I": "-3745815270996862857_i",
                "Q": "-3745815270996862857_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3524321211798147609": {
            "length": 32,
            "waveforms": {
                "I": "-3524321211798147609_i",
                "Q": "-3524321211798147609_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "155176731206446915": {
            "length": 32,
            "waveforms": {
                "I": "155176731206446915_i",
                "Q": "155176731206446915_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1326561523794980746": {
            "length": 32,
            "waveforms": {
                "I": "-1326561523794980746_i",
                "Q": "-1326561523794980746_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1105067464596265498": {
            "length": 32,
            "waveforms": {
                "I": "-1105067464596265498_i",
                "Q": "-1105067464596265498_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3906648293231783600": {
            "length": 36,
            "waveforms": {
                "I": "3906648293231783600_i",
                "Q": "3906648293231783600_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8526499735414866976": {
            "length": 36,
            "waveforms": {
                "I": "8526499735414866976_i",
                "Q": "8526499735414866976_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6104407981234950463": {
            "length": 36,
            "waveforms": {
                "I": "6104407981234950463_i",
                "Q": "6104407981234950463_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6325902040433665711": {
            "length": 36,
            "waveforms": {
                "I": "6325902040433665711_i",
                "Q": "6325902040433665711_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7598524263185882589": {
            "length": 40,
            "waveforms": {
                "I": "-7598524263185882589_i",
                "Q": "-7598524263185882589_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2489274833264753431": {
            "length": 40,
            "waveforms": {
                "I": "-2489274833264753431_i",
                "Q": "-2489274833264753431_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4412678124829952482": {
            "length": 40,
            "waveforms": {
                "I": "-4412678124829952482_i",
                "Q": "-4412678124829952482_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-70021086062871320": {
            "length": 44,
            "waveforms": {
                "I": "-70021086062871320_i",
                "Q": "-70021086062871320_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "53939301042763868": {
            "length": 44,
            "waveforms": {
                "I": "53939301042763868_i",
                "Q": "53939301042763868_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8259468590269755647": {
            "length": 44,
            "waveforms": {
                "I": "8259468590269755647_i",
                "Q": "8259468590269755647_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4622984449806366805": {
            "length": 44,
            "waveforms": {
                "I": "-4622984449806366805_i",
                "Q": "-4622984449806366805_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "314919130332203064": {
            "length": 48,
            "waveforms": {
                "I": "314919130332203064_i",
                "Q": "314919130332203064_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2037446538430091156": {
            "length": 48,
            "waveforms": {
                "I": "-2037446538430091156_i",
                "Q": "-2037446538430091156_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5009766010630318589": {
            "length": 48,
            "waveforms": {
                "I": "-5009766010630318589_i",
                "Q": "-5009766010630318589_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4238044233411292421": {
            "length": 48,
            "waveforms": {
                "I": "-4238044233411292421_i",
                "Q": "-4238044233411292421_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2812006322627151726": {
            "length": 52,
            "waveforms": {
                "I": "-2812006322627151726_i",
                "Q": "-2812006322627151726_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5393522966599840053": {
            "length": 52,
            "waveforms": {
                "I": "5393522966599840053_i",
                "Q": "5393522966599840053_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5615017025798555301": {
            "length": 52,
            "waveforms": {
                "I": "5615017025798555301_i",
                "Q": "5615017025798555301_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3192925271618638788": {
            "length": 52,
            "waveforms": {
                "I": "3192925271618638788_i",
                "Q": "3192925271618638788_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7812776713801722164": {
            "length": 56,
            "waveforms": {
                "I": "7812776713801722164_i",
                "Q": "7812776713801722164_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2266597513640485263": {
            "length": 56,
            "waveforms": {
                "I": "2266597513640485263_i",
                "Q": "2266597513640485263_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5400757542881065106": {
            "length": 56,
            "waveforms": {
                "I": "-5400757542881065106_i",
                "Q": "-5400757542881065106_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7038216929604661594": {
            "length": 56,
            "waveforms": {
                "I": "7038216929604661594_i",
                "Q": "7038216929604661594_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3202997854877898243": {
            "length": 60,
            "waveforms": {
                "I": "-3202997854877898243_i",
                "Q": "-3202997854877898243_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2981503795679182995": {
            "length": 60,
            "waveforms": {
                "I": "-2981503795679182995_i",
                "Q": "-2981503795679182995_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2873031789234274895": {
            "length": 60,
            "waveforms": {
                "I": "2873031789234274895_i",
                "Q": "2873031789234274895_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-783744107676016132": {
            "length": 60,
            "waveforms": {
                "I": "-783744107676016132_i",
                "Q": "-783744107676016132_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5070791477237441758": {
            "length": 64,
            "waveforms": {
                "I": "5070791477237441758_i",
                "Q": "5070791477237441758_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4449465709350748214": {
            "length": 64,
            "waveforms": {
                "I": "4449465709350748214_i",
                "Q": "4449465709350748214_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4670959768549463462": {
            "length": 64,
            "waveforms": {
                "I": "4670959768549463462_i",
                "Q": "4670959768549463462_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3522891337262262136": {
            "length": 64,
            "waveforms": {
                "I": "-3522891337262262136_i",
                "Q": "-3522891337262262136_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6868719456552630325": {
            "length": 68,
            "waveforms": {
                "I": "6868719456552630325_i",
                "Q": "6868719456552630325_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1325131649259095273": {
            "length": 68,
            "waveforms": {
                "I": "-1325131649259095273_i",
                "Q": "-1325131649259095273_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5055899984944537846": {
            "length": 68,
            "waveforms": {
                "I": "5055899984944537846_i",
                "Q": "5055899984944537846_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1822497030040153629": {
            "length": 68,
            "waveforms": {
                "I": "-1822497030040153629_i",
                "Q": "-1822497030040153629_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3304235285041581290": {
            "length": 72,
            "waveforms": {
                "I": "-3304235285041581290_i",
                "Q": "-3304235285041581290_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4901294004185410489": {
            "length": 72,
            "waveforms": {
                "I": "4901294004185410489_i",
                "Q": "4901294004185410489_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6327331914969551184": {
            "length": 72,
            "waveforms": {
                "I": "6327331914969551184_i",
                "Q": "6327331914969551184_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8312240252497376781": {
            "length": 72,
            "waveforms": {
                "I": "-8312240252497376781_i",
                "Q": "-8312240252497376781_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8525091602972718047": {
            "length": 76,
            "waveforms": {
                "I": "8525091602972718047_i",
                "Q": "8525091602972718047_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6114480564494209918": {
            "length": 76,
            "waveforms": {
                "I": "-6114480564494209918_i",
                "Q": "-6114480564494209918_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4688442653710069223": {
            "length": 76,
            "waveforms": {
                "I": "-4688442653710069223_i",
                "Q": "-4688442653710069223_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7040808322472363443": {
            "length": 76,
            "waveforms": {
                "I": "-7040808322472363443_i",
                "Q": "-7040808322472363443_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2035348380515494895": {
            "length": 80,
            "waveforms": {
                "I": "2035348380515494895_i",
                "Q": "2035348380515494895_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2269188906508187112": {
            "length": 80,
            "waveforms": {
                "I": "-2269188906508187112_i",
                "Q": "-2269188906508187112_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1537982999734436539": {
            "length": 80,
            "waveforms": {
                "I": "1537982999734436539_i",
                "Q": "1537982999734436539_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-4689872528245954696_i": {
            "samples": [0.0023070262666795988, 0.0031044431662757732, 0.004112718991022126, 0.005363996778119129, 0.006887508198136117, 0.008706626172317102, 0.010835571342251184, 0.013276019527849927, 0.01601393634639623, 0.019017019945043494, 0.022233148808923724, 0.025590197417340237, 0.028997492617133785, 0.03234904063691291, 0.03552847063473545, 0.03841543626053164, 0.04089301903624815, 0.042855515995282936, 0.044215896103105515] + [0.044912195149836395] * 2 + [0.044215896103105515, 0.042855515995282936, 0.04089301903624815, 0.03841543626053164, 0.03552847063473545, 0.03234904063691291, 0.028997492617133785, 0.025590197417340237, 0.022233148808923724, 0.019017019945043494, 0.01601393634639623, 0.013276019527849927, 0.010835571342251184, 0.008706626172317102, 0.006887508198136117, 0.005363996778119129, 0.004112718991022126, 0.0031044431662757732, 0.0023070262666795988],
            "type": "arbitrary",
        },
        "-4689872528245954696_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-5725775278552983433_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-5725775278552983433_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5399356442740566797_i": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5399356442740566797_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6020682210627260341_i": {
            "samples": [0.045] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6020682210627260341_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5176650348720911465_i": {
            "samples": [0.020602501279722643] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "5176650348720911465_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-2490704707800638904_i": {
            "samples": [0.011220849394978333, 0.045, 0.011220849394978333] + [0.0] * 13,
            "type": "arbitrary",
        },
        "-2490704707800638904_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2031613062289364412_i": {
            "samples": [0.007758973075218879] + [0.03701599030793991] * 2 + [0.007758973075218879] + [0.0] * 12,
            "type": "arbitrary",
        },
        "2031613062289364412_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2253107121488079660_i": {
            "samples": [0.006090087745647572, 0.027293879687068503, 0.045, 0.027293879687068503, 0.006090087745647572] + [0.0] * 11,
            "type": "arbitrary",
        },
        "2253107121488079660_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-71450960598756793_i": {
            "samples": [0.005137279200435915, 0.020602501279722647] + [0.0412584910079413] * 2 + [0.020602501279722647, 0.005137279200435915] + [0.0] * 10,
            "type": "arbitrary",
        },
        "-71450960598756793_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8265302066410482391_i": {
            "samples": [0.004530100489780403, 0.01622015048690195, 0.03486768429974622, 0.045, 0.03486768429974622, 0.01622015048690195, 0.004530100489780403] + [0.0] * 9,
            "type": "arbitrary",
        },
        "-8265302066410482391_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5161758856428007553_i": {
            "samples": [0.004112718991022128, 0.01327601952784993, 0.02899749261713379] + [0.042855515995282936] * 2 + [0.02899749261713379, 0.01327601952784993, 0.004112718991022128] + [0.0] * 8,
            "type": "arbitrary",
        },
        "5161758856428007553_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8762667447191540747_i": {
            "samples": [0.0038096094880138488, 0.01122084939497833, 0.024273337825693197, 0.03856486011458755, 0.045, 0.03856486011458755, 0.024273337825693197, 0.01122084939497833, 0.0038096094880138488] + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8762667447191540747_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5846048319208600280_i": {
            "samples": [0.003580177892320246, 0.009731932507344929, 0.02060250127972264, 0.03396778208950533] + [0.043615495551435485] * 2 + [0.03396778208950533, 0.02060250127972264, 0.009731932507344929, 0.003580177892320246] + [0.0] * 6,
            "type": "arbitrary",
        },
        "-5846048319208600280_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6564907759188373884_i": {
            "samples": [0.003400824362087738, 0.008617283775659838, 0.01775931955800422, 0.029768159504221858, 0.04058330213903772, 0.045, 0.04058330213903772, 0.029768159504221858, 0.01775931955800422, 0.008617283775659838, 0.003400824362087738] + [0.0] * 5,
            "type": "arbitrary",
        },
        "-6564907759188373884_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-612838502181835934_i": {
            "samples": [0.0032569606163357326, 0.007758973075218879, 0.015538090084714526, 0.026157285804303654, 0.03701599030793991] + [0.04403395764329525] * 2 + [0.03701599030793991, 0.026157285804303654, 0.015538090084714526, 0.007758973075218879, 0.0032569606163357326] + [0.0] * 4,
            "type": "arbitrary",
        },
        "-612838502181835934_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "1862115589237333143_i": {
            "samples": [0.00313911400558867, 0.0070819554546795276, 0.013780169102611909, 0.02312656637865019, 0.033475187796194086, 0.041791709925866324, 0.045, 0.041791709925866324, 0.033475187796194086, 0.02312656637865019, 0.013780169102611909, 0.0070819554546795276, 0.00313911400558867] + [0.0] * 3,
            "type": "arbitrary",
        },
        "1862115589237333143_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "1584921185821330929_i": {
            "samples": [0.0030408807189704077, 0.006536836325154028, 0.012369186349601106, 0.020602501279722643, 0.03020675427893248, 0.038984634909117126] + [0.044288214895822076] * 2 + [0.038984634909117126, 0.03020675427893248, 0.020602501279722643, 0.012369186349601106, 0.006536836325154028, 0.0030408807189704077] + [0.0] * 2,
            "type": "arbitrary",
        },
        "1584921185821330929_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5392093092063954580_i": {
            "samples": [0.0029577837877438713, 0.006090087745647572, 0.01122084939497833, 0.018500053072823434, 0.027293879687068503, 0.03603318313125636, 0.04256817610080444, 0.045, 0.04256817610080444, 0.03603318313125636, 0.027293879687068503, 0.018500053072823434, 0.01122084939497833, 0.006090087745647572, 0.0029577837877438713, 0.0],
            "type": "arbitrary",
        },
        "5392093092063954580_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "1087555805040272573_i": {
            "samples": [0.002886603231749668, 0.005718315154083024, 0.01027395147062127, 0.016741538367185362, 0.024742389790509828, 0.03316472159899549, 0.04031804794466557] + [0.04445402275413001] * 2 + [0.04031804794466557, 0.03316472159899549, 0.024742389790509828, 0.016741538367185362, 0.01027395147062127, 0.005718315154083024, 0.002886603231749668],
            "type": "arbitrary",
        },
        "1087555805040272573_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1264809863722021647_i": {
            "samples": [0.0028249661996606213, 0.005404788539183576, 0.009483648111828325, 0.015261718144141496, 0.02252489106451083, 0.030489706454936944, 0.03785079975109237, 0.04309512555812251, 0.045, 0.04309512555812251, 0.03785079975109237, 0.030489706454936944, 0.02252489106451083, 0.015261718144141496, 0.009483648111828325, 0.005404788539183576, 0.0028249661996606213] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1264809863722021647_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
        },
        "-3201589722435749314_i": {
            "samples": [0.002771086967490843, 0.0051372792004359125, 0.008816694774556523, 0.014007739812935151, 0.02060250127972264, 0.028051846679528352, 0.0353583985391161, 0.0412584910079413] + [0.0445680586213723] * 2 + [0.0412584910079413, 0.0353583985391161, 0.028051846679528352, 0.02060250127972264, 0.014007739812935151, 0.008816694774556523, 0.0051372792004359125, 0.002771086967490843] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3201589722435749314_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
        },
        "-9209359323659574230_i": {
            "samples": [0.0027235967694566334, 0.004906672471959597, 0.00824813067227343, 0.01293743560534336, 0.018934989754037124, 0.025858668138996333, 0.032951215211532645, 0.03917968351030313, 0.043468496224329134, 0.045, 0.043468496224329134, 0.03917968351030313, 0.032951215211532645, 0.025858668138996333, 0.018934989754037124, 0.01293743560534336, 0.00824813067227343, 0.004906672471959597, 0.0027235967694566334, 0.0],
            "type": "arbitrary",
        },
        "-9209359323659574230_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
        },
        "-5402187417416950579_i": {
            "samples": [0.002681429344289374, 0.004706055058005065, 0.007758973075218877, 0.01201733258518545, 0.017485115738056386, 0.023899319596590533, 0.030687333803565666, 0.03701599030793991, 0.04194461215617874] + [0.044649807221710955] * 2 + [0.04194461215617874, 0.03701599030793991, 0.030687333803565666, 0.023899319596590533, 0.017485115738056386, 0.01201733258518545, 0.007758973075218877, 0.004706055058005065, 0.002681429344289374],
            "type": "arbitrary",
        },
        "-5402187417416950579_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
        },
        "-879869647326947263_i": {
            "samples": [0.0026437420840333746, 0.004530100489780402, 0.0073346048100830456, 0.01122084939497833, 0.016220150486901945, 0.022154612403294235, 0.02859259449459615, 0.03486768429974622, 0.040176562570300486, 0.043742397162897365, 0.045, 0.043742397162897365, 0.040176562570300486, 0.03486768429974622, 0.02859259449459615, 0.022154612403294235, 0.016220150486901945, 0.01122084939497833, 0.0073346048100830456, 0.004530100489780402, 0.0026437420840333746] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-879869647326947263_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "-658375588128232015_i": {
            "samples": [0.002609860540872115, 0.00437464648410137, 0.006963635959888166, 0.01052680526488461, 0.015112090735730868, 0.020602501279722643, 0.02667367042822907, 0.03279540856535964, 0.03829223754247891, 0.04245959787865623] + [0.044710388440118876] * 2 + [0.04245959787865623, 0.03829223754247891, 0.03279540856535964, 0.02667367042822907, 0.020602501279722643, 0.015112090735730868, 0.01052680526488461, 0.006963635959888166, 0.00437464648410137, 0.002609860540872115] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-658375588128232015_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "-1778389818629643021_i": {
            "samples": [0.002579238622452966, 0.0042363986336785495, 0.0066370914436332945, 0.009918236716819908, 0.014137311375621348, 0.019220950654690473, 0.02492634433738389, 0.030833157592210256, 0.03637919638388446, 0.04094151280701048, 0.04394913753524951, 0.045, 0.04394913753524951, 0.04094151280701048, 0.03637919638388446, 0.030833157592210256, 0.02492634433738389, 0.019220950654690473, 0.014137311375621348, 0.009918236716819908, 0.0066370914436332945, 0.0042363986336785495, 0.002579238622452966, 0.0],
            "type": "arbitrary",
        },
        "-1778389818629643021_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "-4130755487391937241_i": {
            "samples": [0.002551429548171046, 0.004112718991022128, 0.00634782441601157, 0.009381476336160566, 0.01327601952784993, 0.017989330087402715, 0.02334062666460994, 0.02899749261713379, 0.03449521007116611, 0.03929230936293479, 0.042855515995282936] + [0.04475652045276505] * 2 + [0.042855515995282936, 0.03929230936293479, 0.03449521007116611, 0.02899749261713379, 0.02334062666460994, 0.017989330087402715, 0.01327601952784993, 0.009381476336160566, 0.00634782441601157, 0.004112718991022128, 0.002551429548171046],
            "type": "arbitrary",
        },
        "-4130755487391937241_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "6648633529796064006_i": {
            "samples": [0.0025260643275360176, 0.0040014727856723855, 0.006090087745647572, 0.00890544145876266, 0.012511678520393735, 0.01688899944831298, 0.021903851518198725, 0.027293879687068503, 0.03267670666831609, 0.03758715951350724, 0.04154023558739861, 0.04410894029880399, 0.045, 0.04410894029880399, 0.04154023558739861, 0.03758715951350724, 0.03267670666831609, 0.027293879687068503, 0.021903851518198725, 0.01688899944831298, 0.012511678520393735, 0.00890544145876266, 0.006090087745647572, 0.0040014727856723855, 0.0025260643275360176] + [0.0] * 3,
            "type": "arbitrary",
        },
        "6648633529796064006_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "-7275792773823484294_i": {
            "samples": [0.0025028355874354992, 0.0039009156449618773, 0.005859217370023295, 0.00848108614953415, 0.011830474202861593, 0.01590346086689613, 0.020602501279722643, 0.02572095375451038, 0.030945179119672497, 0.03587878657292559, 0.040088638425953435, 0.04316618612562091] + [0.044792454939364075] * 2 + [0.04316618612562091, 0.040088638425953435, 0.03587878657292559, 0.030945179119672497, 0.02572095375451038, 0.020602501279722643, 0.01590346086689613, 0.011830474202861593, 0.00848108614953415, 0.005859217370023295, 0.0039009156449618773, 0.0025028355874354992] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7275792773823484294_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "-1711501740190055130_i": {
            "samples": [0.0024814852626756563, 0.0038096094880138488, 0.005651395719435244, 0.008100978437746048, 0.011220849394978333, 0.015018290122123386, 0.019423243080843425, 0.024273337825693197, 0.029311885423359323, 0.03420302420732057, 0.03856486011458755, 0.04201704562427031, 0.04423497268175237, 0.045, 0.04423497268175237, 0.04201704562427031, 0.03856486011458755, 0.03420302420732057, 0.029311885423359323, 0.024273337825693197, 0.019423243080843425, 0.015018290122123386, 0.011220849394978333, 0.008100978437746048, 0.005651395719435244, 0.0038096094880138488, 0.0024814852626756563, 0.0],
            "type": "arbitrary",
        },
        "-1711501740190055130_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "-3745815270996862857_i": {
            "samples": [0.0024617951167852383, 0.003726359018304561, 0.0054634730847848405, 0.007758973075218879, 0.010673110496635019, 0.014220965746182155, 0.018353483216057877, 0.022943476855747564, 0.027781218361001815, 0.032583270094514144, 0.03701599030793991, 0.040731968667614436, 0.04341429502287785] + [0.044820988381976366] * 2 + [0.04341429502287785, 0.040731968667614436, 0.03701599030793991, 0.032583270094514144, 0.027781218361001815, 0.022943476855747564, 0.018353483216057877, 0.014220965746182155, 0.010673110496635019, 0.007758973075218879, 0.0054634730847848405, 0.003726359018304561, 0.0024617951167852383],
            "type": "arbitrary",
        },
        "-3745815270996862857_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "-3524321211798147609_i": {
            "samples": [0.0024435793635176613, 0.0036501632161548623, 0.005292831373674129, 0.007449957059914865, 0.01017910090171241, 0.013500660222938617, 0.017381631298331857, 0.021722809694617814, 0.02635308117604699, 0.031033927425680702, 0.03547578536508673, 0.03936563263600119, 0.04240259052527128, 0.044336099473404764, 0.045, 0.044336099473404764, 0.04240259052527128, 0.03936563263600119, 0.03547578536508673, 0.031033927425680702, 0.02635308117604699, 0.021722809694617814, 0.017381631298331857, 0.013500660222938617, 0.01017910090171241, 0.007449957059914865, 0.005292831373674129, 0.0036501632161548623, 0.0024435793635176613] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3524321211798147609_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "155176731206446915_i": {
            "samples": [0.002426678866378028, 0.003580177892320246, 0.0051372792004359125, 0.007169650683264689, 0.009731932507344929, 0.012848027113724358, 0.01649719336831532, 0.02060250127972264, 0.02502453976979439, 0.02956300063421708, 0.03396778208950533, 0.03795964420789055, 0.0412584910079413, 0.043615495551435485] + [0.04484402095366661] * 2 + [0.043615495551435485, 0.0412584910079413, 0.03795964420789055, 0.03396778208950533, 0.02956300063421708, 0.02502453976979439, 0.02060250127972264, 0.01649719336831532, 0.012848027113724358, 0.009731932507344929, 0.007169650683264689, 0.0051372792004359125, 0.003580177892320246, 0.002426678866378028] + [0.0] * 2,
            "type": "arbitrary",
        },
        "155176731206446915_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "-1326561523794980746_i": {
            "samples": [0.0024109565367578835, 0.0035156864938290025, 0.004994970371269144, 0.006914451090177933, 0.009325766086476159, 0.012255000795126673, 0.015690767457769792, 0.019573885564962007, 0.023790957461622565, 0.028174019611510417, 0.03250781063827401, 0.036545057250441104, 0.040028709455768426, 0.04271855432848505, 0.04441846252714071, 0.045, 0.04441846252714071, 0.04271855432848505, 0.040028709455768426, 0.036545057250441104, 0.03250781063827401, 0.028174019611510417, 0.023790957461622565, 0.019573885564962007, 0.015690767457769792, 0.012255000795126673, 0.009325766086476159, 0.006914451090177933, 0.004994970371269144, 0.0035156864938290025, 0.0024109565367578835, 0.0],
            "type": "arbitrary",
        },
        "-1326561523794980746_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "-1105067464596265498_i": {
            "samples": [0.0023962936518776646, 0.003456077133652085, 0.004864340004480777, 0.006681308535800779, 0.008955631989591218, 0.011714616017857806, 0.014953986494751055, 0.01862872011349104, 0.022646764226304746, 0.02686744738608851, 0.031105971004103065, 0.035144569347404675, 0.038749829545265374, 0.04169447159923057, 0.04378085710534654] + [0.0448628802330165] * 2 + [0.04378085710534654, 0.04169447159923057, 0.038749829545265374, 0.035144569347404675, 0.031105971004103065, 0.02686744738608851, 0.022646764226304746, 0.01862872011349104, 0.014953986494751055, 0.011714616017857806, 0.008955631989591218, 0.006681308535800779, 0.004864340004480777, 0.003456077133652085, 0.0023962936518776646],
            "type": "arbitrary",
        },
        "-1105067464596265498_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "3906648293231783600_i": {
            "samples": [0.0023825868853451075, 0.0034008243620877393, 0.004744054065238999, 0.0064676279185557, 0.00861728377565984, 0.011220849394978333, 0.014279435607375697, 0.01775931955800422, 0.021585970145073075, 0.025641698701671392, 0.02976815950422186, 0.033774361377894954, 0.03745003934865391, 0.04058330213903772, 0.042980598125817636, 0.044486424232505616, 0.045, 0.044486424232505616, 0.042980598125817636, 0.04058330213903772, 0.03745003934865391, 0.033774361377894954, 0.02976815950422186, 0.025641698701671392, 0.021585970145073075, 0.01775931955800422, 0.014279435607375697, 0.011220849394978333, 0.00861728377565984, 0.0064676279185557, 0.004744054065238999, 0.0034008243620877393, 0.0023825868853451075] + [0.0] * 3,
            "type": "arbitrary",
        },
        "3906648293231783600_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "8526499735414866976_i": {
            "samples": [0.002369745894728846, 0.0033494745849758367, 0.0046329691928013806, 0.006271189960418482, 0.008307078573323065, 0.010768482304484909, 0.013660559820788764, 0.016958612410017813, 0.020602501279722643, 0.02449386971171626, 0.02849723182010489, 0.03244559669603551, 0.036150696913277686, 0.03941716641018121, 0.0420592908560809, 0.0439183797241986] + [0.0448785163526999] * 2 + [0.0439183797241986, 0.0420592908560809, 0.03941716641018121, 0.036150696913277686, 0.03244559669603551, 0.02849723182010489, 0.02449386971171626, 0.020602501279722643, 0.016958612410017813, 0.013660559820788764, 0.010768482304484909, 0.008307078573323065, 0.006271189960418482, 0.0046329691928013806, 0.0033494745849758367, 0.002369745894728846] + [0.0] * 2,
            "type": "arbitrary",
        },
        "8526499735414866976_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "6104407981234950463_i": {
            "samples": [0.002357691348142151, 0.0033016343115772305, 0.004530100489780399, 0.006090087745647572, 0.008021879081327156, 0.010352983454721408, 0.013091571317076667, 0.016220150486901945, 0.019690413196512112, 0.023420255445931595, 0.027293879687068503, 0.031165619589233893, 0.03486768429974622, 0.03822146174557406, 0.041051433457284535, 0.043200244857846494, 0.04454315115204302, 0.045, 0.04454315115204302, 0.043200244857846494, 0.041051433457284535, 0.03822146174557406, 0.03486768429974622, 0.031165619589233893, 0.027293879687068503, 0.023420255445931595, 0.019690413196512112, 0.016220150486901945, 0.013091571317076667, 0.010352983454721408, 0.008021879081327156, 0.006090087745647572, 0.004530100489780399, 0.0033016343115772305, 0.002357691348142151, 0.0],
            "type": "arbitrary",
        },
        "6104407981234950463_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "6325902040433665711_i": {
            "samples": [0.002346353299521717, 0.0032569606163357313, 0.0044345955187797504, 0.005922675334206895, 0.007758973075218878, 0.00997040888541069, 0.012567361250607789, 0.015538090084714525, 0.01884402087812471, 0.022416712622672377, 0.02615728580430365, 0.029938899807673777, 0.03361254540686738, 0.03701599030793991, 0.03998524390179175, 0.04236747013441668, 0.04403395764329525] + [0.044891623769994185] * 2 + [0.04403395764329525, 0.04236747013441668, 0.03998524390179175, 0.03701599030793991, 0.03361254540686738, 0.029938899807673777, 0.02615728580430365, 0.022416712622672377, 0.01884402087812471, 0.015538090084714525, 0.012567361250607789, 0.00997040888541069, 0.007758973075218878, 0.005922675334206895, 0.0044345955187797504, 0.0032569606163357313, 0.002346353299521717],
            "type": "arbitrary",
        },
        "6325902040433665711_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "-7598524263185882589_i": {
            "samples": [0.002335669842884592, 0.003215153346284126, 0.004345713174304989, 0.005767525922407299, 0.007516007086959697, 0.009617317104979359, 0.01208341858496279, 0.014907157287993888, 0.01805797205500425, 0.02147891051554825, 0.025085609068644998, 0.02876776885451699, 0.03239342286852773, 0.03581596273281828, 0.03888351771803405, 0.04144991033641262, 0.0433861159211894, 0.044590986286279576, 0.045, 0.044590986286279576, 0.0433861159211894, 0.04144991033641262, 0.03888351771803405, 0.03581596273281828, 0.03239342286852773, 0.02876776885451699, 0.025085609068644998, 0.02147891051554825, 0.01805797205500425, 0.014907157287993888, 0.01208341858496279, 0.009617317104979359, 0.007516007086959697, 0.005767525922407299, 0.004345713174304989, 0.003215153346284126, 0.002335669842884592] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7598524263185882589_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-2489274833264753431_i": {
            "samples": [0.0023255859913126685, 0.003175948715009545, 0.004262806410670822, 0.005623397594830979, 0.007290931578012656, 0.009290697194004017, 0.011635756917750779, 0.014322605346206307, 0.017327282732784, 0.020602501279722643, 0.024076341173783655, 0.027652988889901368, 0.031215818050692484, 0.03463286447219627, 0.037764449415815096, 0.04047239942068012, 0.04263004575896565, 0.04413200882895417] + [0.044902719567521156] * 2 + [0.04413200882895417, 0.04263004575896565, 0.04047239942068012, 0.037764449415815096, 0.03463286447219627, 0.031215818050692484, 0.027652988889901368, 0.024076341173783655, 0.020602501279722643, 0.017327282732784, 0.014322605346206307, 0.011635756917750779, 0.009290697194004017, 0.007290931578012656, 0.005623397594830979, 0.004262806410670822, 0.003175948715009545, 0.0023255859913126685] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2489274833264753431_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-4412678124829952482_i": {
            "samples": [0.0023160527381292616, 0.003139114005588671, 0.004185308040118834, 0.005489205145584141, 0.0070819554546795276, 0.008987907922313233, 0.011220849394978333, 0.013780169102611909, 0.016647347899696227, 0.019783232685447464, 0.023126566378650192, 0.026594188993507337, 0.030083200552476104, 0.033475187796194086, 0.0366423821808049, 0.039455365694803866, 0.041791709925866324, 0.04354476023446263, 0.044631693012253504, 0.045, 0.044631693012253504, 0.04354476023446263, 0.041791709925866324, 0.039455365694803866, 0.0366423821808049, 0.033475187796194086, 0.030083200552476104, 0.026594188993507337, 0.023126566378650192, 0.019783232685447464, 0.016647347899696227, 0.013780169102611909, 0.011220849394978333, 0.008987907922313233, 0.0070819554546795276, 0.005489205145584141, 0.004185308040118834, 0.003139114005588671, 0.0023160527381292616, 0.0],
            "type": "arbitrary",
        },
        "-4412678124829952482_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-70021086062871320_i": {
            "samples": [0.002298467282013625, 0.003071753129323663, 0.004044598549210856, 0.005246934746939324, 0.006706208220111929, 0.008444803201727434, 0.010477150002685766, 0.012806720149016473, 0.015423175704628934, 0.018299988718455947, 0.021392865802783618, 0.024639292928737164, 0.027959451271045772, 0.031258646978771204, 0.034431253739310434, 0.03736600151243667, 0.039952277935397115, 0.042086963621413266, 0.04368122124228356, 0.04466661880713002, 0.045, 0.04466661880713002, 0.04368122124228356, 0.042086963621413266, 0.039952277935397115, 0.03736600151243667, 0.034431253739310434, 0.031258646978771204, 0.027959451271045772, 0.024639292928737164, 0.021392865802783618, 0.018299988718455947, 0.015423175704628934, 0.012806720149016473, 0.010477150002685766, 0.008444803201727434, 0.006706208220111929, 0.005246934746939324, 0.004044598549210856, 0.003071753129323663, 0.002298467282013625] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-70021086062871320_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "53939301042763868_i": {
            "samples": [0.002290340443109101, 0.003040880718970406, 0.003980556207121157, 0.0051372792004359125, 0.006536836325154025, 0.008200627499825764, 0.010143120675347301, 0.012369186349601104, 0.014871531844695524, 0.017628498018846427, 0.02060250127972264, 0.023739393607378083, 0.026968967851849397, 0.03020675427893248, 0.033357141928063716, 0.03631772498912383, 0.038984634909117126, 0.0412584910079413, 0.04305050412463992, 0.044288214895822076] + [0.04492035118368515] * 2 + [0.044288214895822076, 0.04305050412463992, 0.0412584910079413, 0.038984634909117126, 0.03631772498912383, 0.033357141928063716, 0.03020675427893248, 0.026968967851849397, 0.023739393607378083, 0.02060250127972264, 0.017628498018846427, 0.014871531844695524, 0.012369186349601104, 0.010143120675347301, 0.008200627499825764, 0.006536836325154025, 0.0051372792004359125, 0.003980556207121157, 0.003040880718970406, 0.002290340443109101] + [0.0] * 2,
            "type": "arbitrary",
        },
        "53939301042763868_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "8259468590269755647_i": {
            "samples": [0.002282613878441956, 0.0030116800421040894, 0.00392024482363332, 0.005034374636005118, 0.006378313375728078, 0.007972493186884571, 0.009831288533885395, 0.01196064799578202, 0.014355785406816845, 0.01699914928966451, 0.01985890963969827, 0.022888197540850325, 0.026025301412808174, 0.029194962686577716, 0.03231082615520607, 0.03527899317411319, 0.038002510143230084, 0.04038651383377471, 0.0423436636171159, 0.04379943184129589, 0.04469680751117565, 0.045, 0.04469680751117565, 0.04379943184129589, 0.0423436636171159, 0.04038651383377471, 0.038002510143230084, 0.03527899317411319, 0.03231082615520607, 0.029194962686577716, 0.026025301412808174, 0.022888197540850325, 0.01985890963969827, 0.01699914928966451, 0.014355785406816845, 0.01196064799578202, 0.009831288533885395, 0.007972493186884571, 0.006378313375728078, 0.005034374636005118, 0.00392024482363332, 0.0030116800421040894, 0.002282613878441956, 0.0],
            "type": "arbitrary",
        },
        "8259468590269755647_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "-4622984449806366805_i": {
            "samples": [0.0022752587709870802, 0.0029840202764447096, 0.0038633548579549335, 0.0049376384969694, 0.00622968142826453, 0.007758973075218878, 0.009539695436145574, 0.011578615519847506, 0.01387300729711731, 0.016408786144965208, 0.019159058061268403, 0.0220832866923284, 0.025127259572151332, 0.028223989387651714, 0.031295618037513455, 0.034256305533367615, 0.03701599030793991, 0.03948481254632568, 0.04157790922741945, 0.043220229774447644, 0.044350993672068774] + [0.04492742171182011] * 2 + [0.044350993672068774, 0.043220229774447644, 0.04157790922741945, 0.03948481254632568, 0.03701599030793991, 0.034256305533367615, 0.031295618037513455, 0.028223989387651714, 0.025127259572151332, 0.0220832866923284, 0.019159058061268403, 0.016408786144965208, 0.01387300729711731, 0.011578615519847506, 0.009539695436145574, 0.007758973075218878, 0.00622968142826453, 0.0049376384969694, 0.0038633548579549335, 0.0029840202764447096, 0.0022752587709870802],
            "type": "arbitrary",
        },
        "-4622984449806366805_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "314919130332203064_i": {
            "samples": [0.002268249001323914, 0.0029577837877438713, 0.0038096094880138488, 0.0048465515335514445, 0.006090087745647572, 0.007558795654089012, 0.009266591089538943, 0.01122084939497833, 0.01342053432816397, 0.01585448797479736, 0.018500053072823434, 0.02132220268779138, 0.024273337825693197, 0.027293879687068503, 0.030313730490512704, 0.03325460833261389, 0.03603318313125636, 0.03856486011458755, 0.040767983599927934, 0.04256817610080444, 0.04390249410291806, 0.044723077799689856, 0.045, 0.044723077799689856, 0.04390249410291806, 0.04256817610080444, 0.040767983599927934, 0.03856486011458755, 0.03603318313125636, 0.03325460833261389, 0.030313730490512704, 0.027293879687068503, 0.024273337825693197, 0.02132220268779138, 0.018500053072823434, 0.01585448797479736, 0.01342053432816397, 0.01122084939497833, 0.009266591089538943, 0.007558795654089012, 0.006090087745647572, 0.0048465515335514445, 0.0038096094880138488, 0.0029577837877438713, 0.002268249001323914] + [0.0] * 3,
            "type": "arbitrary",
        },
        "314919130332203064_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-2037446538430091156_i": {
            "samples": [0.0022615608395822576, 0.002932864520601318, 0.003758760460735895, 0.004760649623148641, 0.005958771201714929, 0.007370825381837093, 0.00901040800045584, 0.01088533282269449, 0.012995945737972792, 0.015333559684314104, 0.01787915576936509, 0.020602501279722643, 0.023461826182497255, 0.026404174709919723, 0.029366507779970033, 0.03227757743901369, 0.03506053033367666, 0.03763612929881027, 0.03992641754448022, 0.04185859607443986, 0.04336884873340308, 0.04440583598342185] + [0.04493359111031693] * 2 + [0.04440583598342185, 0.04336884873340308, 0.04185859607443986, 0.03992641754448022, 0.03763612929881027, 0.03506053033367666, 0.03227757743901369, 0.029366507779970033, 0.026404174709919723, 0.023461826182497255, 0.020602501279722643, 0.01787915576936509, 0.015333559684314104, 0.012995945737972792, 0.01088533282269449, 0.00901040800045584, 0.007370825381837093, 0.005958771201714929, 0.004760649623148641, 0.003758760460735895, 0.002932864520601318, 0.0022615608395822576] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2037446538430091156_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-5009766010630318589_i": {
            "samples": [0.0022551726786126905, 0.0029091666178561433, 0.003710584550668933, 0.004679516802908711, 0.005835050681741723, 0.007194045770117959, 0.008769739701211816, 0.010570247395266656, 0.012597041018014099, 0.014843519161489465, 0.017293788920022278, 0.019921790688190392, 0.022690890195482847, 0.0255540439911971, 0.028454613075855284, 0.03132785596158564, 0.03410308006849492, 0.036706373427339595, 0.039063782647928855, 0.04110475402306036, 0.042765618258428395, 0.04399288047528688, 0.04474607899637652, 0.045, 0.04474607899637652, 0.04399288047528688, 0.042765618258428395, 0.04110475402306036, 0.039063782647928855, 0.036706373427339595, 0.03410308006849492, 0.03132785596158564, 0.028454613075855284, 0.0255540439911971, 0.022690890195482847, 0.019921790688190392, 0.017293788920022278, 0.014843519161489465, 0.012597041018014099, 0.010570247395266656, 0.008769739701211816, 0.007194045770117959, 0.005835050681741723, 0.004679516802908711, 0.003710584550668933, 0.0029091666178561433, 0.0022551726786126905, 0.0],
            "type": "arbitrary",
        },
        "-5009766010630318589_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-4238044233411292421_i": {
            "samples": [0.0022490648020923256, 0.002886603231749669, 0.0036648805264638787, 0.004602779313517965, 0.005718315154083024, 0.0070275448297335615, 0.008543321810579173, 0.010273951470621273, 0.012221819276561888, 0.014382083582930012, 0.016741538367185362, 0.019277757810779724, 0.02195863200027421, 0.024742389790509828, 0.027578180623949435, 0.030407252619400714, 0.03316472159899549, 0.035781878196983995, 0.03818893203389997, 0.04031804794466557, 0.04210649424101218, 0.04349970122287654, 0.04445402275413001] + [0.044939006217156886] * 2 + [0.04445402275413001, 0.04349970122287654, 0.04210649424101218, 0.04031804794466557, 0.03818893203389997, 0.035781878196983995, 0.03316472159899549, 0.030407252619400714, 0.027578180623949435, 0.024742389790509828, 0.02195863200027421, 0.019277757810779724, 0.016741538367185362, 0.014382083582930012, 0.012221819276561888, 0.010273951470621273, 0.008543321810579173, 0.0070275448297335615, 0.005718315154083024, 0.004602779313517965, 0.0036648805264638787, 0.002886603231749669, 0.0022490648020923256],
            "type": "arbitrary",
        },
        "-4238044233411292421_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-2812006322627151726_i": {
            "samples": [0.002243219182348703, 0.00286509549664543, 0.0036214665430845685, 0.004530100489780403, 0.005608015145664268, 0.006870502518018646, 0.008330015541669001, 0.009994960993703648, 0.011868460228350485, 0.013947155318533784, 0.01622015048690195, 0.018668185356823963, 0.021263135798531962, 0.023967928732267805, 0.02673693866631924, 0.029516906409324264, 0.032248385742071686, 0.03486768429974622, 0.03730922377347726, 0.03950820561072078, 0.04140343565391694, 0.04294013828570386, 0.04407258057339122, 0.044766331401892075, 0.045, 0.044766331401892075, 0.04407258057339122, 0.04294013828570386, 0.04140343565391694, 0.03950820561072078, 0.03730922377347726, 0.03486768429974622, 0.032248385742071686, 0.029516906409324264, 0.02673693866631924, 0.023967928732267805, 0.021263135798531962, 0.018668185356823963, 0.01622015048690195, 0.013947155318533784, 0.011868460228350485, 0.009994960993703648, 0.008330015541669001, 0.006870502518018646, 0.005608015145664268, 0.004530100489780403, 0.0036214665430845685, 0.00286509549664543, 0.002243219182348703] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2812006322627151726_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "5393522966599840053_i": {
            "samples": [0.002237619303555732, 0.0028445716383879984, 0.003580177892320246, 0.004461176362983632, 0.005503655400610527, 0.00672217988626881, 0.00812879332285023, 0.009731932507344929, 0.011535306813678311, 0.013536807946077398, 0.01572752700898904, 0.01809096223925947, 0.02060250127972264, 0.023229255327547334, 0.025930308315230993, 0.028657422646728443, 0.031356214897321565, 0.03396778208950533, 0.03643072419005491, 0.0386834743621144, 0.04066681850429382, 0.042326462851395394, 0.043615495551435485, 0.044496587007505486] + [0.044943785141606137] * 2 + [0.044496587007505486, 0.043615495551435485, 0.042326462851395394, 0.04066681850429382, 0.0386834743621144, 0.03643072419005491, 0.03396778208950533, 0.031356214897321565, 0.028657422646728443, 0.025930308315230993, 0.023229255327547334, 0.02060250127972264, 0.01809096223925947, 0.01572752700898904, 0.013536807946077398, 0.011535306813678311, 0.009731932507344929, 0.00812879332285023, 0.00672217988626881, 0.005503655400610527, 0.004461176362983632, 0.003580177892320246, 0.0028445716383879984, 0.002237619303555732] + [0.0] * 2,
            "type": "arbitrary",
        },
        "5393522966599840053_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "5615017025798555301_i": {
            "samples": [0.0022322500066664524, 0.0028249661996606213, 0.0035408650560035527, 0.004395731863752645, 0.005404788539183576, 0.0065819096743409905, 0.007938726243331798, 0.009483648111828325, 0.011220849394978333, 0.013149272708892313, 0.015261718144141496, 0.017544089001665954, 0.019974867725426344, 0.02252489106451083, 0.02515748274940722, 0.027828984880678528, 0.030489706454936944, 0.03308528030756846, 0.03555839015421074, 0.03785079975109237, 0.039905589113387624, 0.0416694808715781, 0.04309512555812251, 0.04414320968250296, 0.04478425585579964, 0.045, 0.04478425585579964, 0.04414320968250296, 0.04309512555812251, 0.0416694808715781, 0.039905589113387624, 0.03785079975109237, 0.03555839015421074, 0.03308528030756846, 0.030489706454936944, 0.027828984880678528, 0.02515748274940722, 0.02252489106451083, 0.019974867725426344, 0.017544089001665954, 0.015261718144141496, 0.013149272708892313, 0.011220849394978333, 0.009483648111828325, 0.007938726243331798, 0.0065819096743409905, 0.005404788539183576, 0.004395731863752645, 0.0035408650560035527, 0.0028249661996606213, 0.0022322500066664524, 0.0],
            "type": "arbitrary",
        },
        "5615017025798555301_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "3192925271618638788_i": {
            "samples": [0.0022270973530301706, 0.002806219364174241, 0.003503392015899386, 0.0043335175332762516, 0.005311009565081267, 0.006449088139978684, 0.007758973075218878, 0.009249002151979598, 0.010923711446082687, 0.012782925623788405, 0.014820914704026435, 0.017025679631132086, 0.01937843094622511, 0.021853322038281, 0.024417490369076637, 0.027031446604730405, 0.029649833165918307, 0.032222551282821706, 0.0346962306710861, 0.03701599030793991, 0.03912741462266989, 0.04097864892771672, 0.04252250315163484, 0.043718445554516816, 0.044534369188016384] + [0.044948023753154064] * 2 + [0.044534369188016384, 0.043718445554516816, 0.04252250315163484, 0.04097864892771672, 0.03912741462266989, 0.03701599030793991, 0.0346962306710861, 0.032222551282821706, 0.029649833165918307, 0.027031446604730405, 0.024417490369076637, 0.021853322038281, 0.01937843094622511, 0.017025679631132086, 0.014820914704026435, 0.012782925623788405, 0.010923711446082687, 0.009249002151979598, 0.007758973075218878, 0.006449088139978684, 0.005311009565081267, 0.0043335175332762516, 0.003503392015899386, 0.002806219364174241, 0.0022270973530301706],
            "type": "arbitrary",
        },
        "3192925271618638788_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "7812776713801722164_i": {
            "samples": [0.0022221485041214635, 0.0027882763653518834, 0.003467634781995055, 0.0042743066663799584, 0.005221951094417901, 0.006323167944034364, 0.007588770658725412, 0.009026989431452753, 0.01064263663170876, 0.012436275357891683, 0.014403439706323315, 0.01653396078013889, 0.018811454732179145, 0.021213027506237683, 0.023709244916873748, 0.0262644061328905, 0.02883714375131922, 0.03138135515132871, 0.03384744880835653, 0.03618386719741171, 0.038338826543671004, 0.04026219481588473, 0.04190741476215459, 0.043233369965617566, 0.04420608993687952, 0.044800195693516454, 0.045, 0.044800195693516454, 0.04420608993687952, 0.043233369965617566, 0.04190741476215459, 0.04026219481588473, 0.038338826543671004, 0.03618386719741171, 0.03384744880835653, 0.03138135515132871, 0.02883714375131922, 0.0262644061328905, 0.023709244916873748, 0.021213027506237683, 0.018811454732179145, 0.01653396078013889, 0.014403439706323315, 0.012436275357891683, 0.01064263663170876, 0.009026989431452753, 0.007588770658725412, 0.006323167944034364, 0.005221951094417901, 0.0042743066663799584, 0.003467634781995055, 0.0027882763653518834, 0.0022221485041214635] + [0.0] * 3,
            "type": "arbitrary",
        },
        "7812776713801722164_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "2266597513640485263_i": {
            "samples": [0.002217391615205061, 0.0027710869674908442, 0.0034334801072547667, 0.004217892822637325, 0.005137279200435915, 0.00620365194075587, 0.00742742546731715, 0.008816694774556525, 0.010376477167048592, 0.012107951931622883, 0.014007739812935151, 0.016067269169839395, 0.018272278128532837, 0.020602501279722643, 0.02303158503848993, 0.025527267506754027, 0.028051846679528352, 0.030562945600649025, 0.03301456543598165, 0.0353583985391161, 0.037545354818060456, 0.03952723757770026, 0.0412584910079413, 0.04269793195211086, 0.04381037456878093, 0.0445680586213723] + [0.04495180052302276] * 2 + [0.0445680586213723, 0.04381037456878093, 0.04269793195211086, 0.0412584910079413, 0.03952723757770026, 0.037545354818060456, 0.0353583985391161, 0.03301456543598165, 0.030562945600649025, 0.028051846679528352, 0.025527267506754027, 0.02303158503848993, 0.020602501279722643, 0.018272278128532837, 0.016067269169839395, 0.014007739812935151, 0.012107951931622883, 0.010376477167048592, 0.008816694774556525, 0.00742742546731715, 0.00620365194075587, 0.005137279200435915, 0.004217892822637325, 0.0034334801072547667, 0.0027710869674908442, 0.002217391615205061] + [0.0] * 2,
            "type": "arbitrary",
        },
        "2266597513640485263_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "-5400757542881065106_i": {
            "samples": [0.002212815741090006, 0.0027546050092919216, 0.003400824362087736, 0.00416408765212899, 0.005056689785065528, 0.006090087745647572, 0.007274306195427147, 0.008617283775659837, 0.010124183346261053, 0.011796696263059339, 0.013632376843449557, 0.015624047755243337, 0.017759319558004215, 0.020020267479223943, 0.022383305310115148, 0.024819289852372393, 0.027293879687068503, 0.029768159504221858, 0.032199526451551545, 0.034542818825439844, 0.03675165104070378, 0.038779903413772035, 0.04058330213903772, 0.04212101510529366, 0.04335718385920805, 0.04426231173926075, 0.04481443325319743, 0.045, 0.04481443325319743, 0.04426231173926075, 0.04335718385920805, 0.04212101510529366, 0.04058330213903772, 0.038779903413772035, 0.03675165104070378, 0.034542818825439844, 0.032199526451551545, 0.029768159504221858, 0.027293879687068503, 0.024819289852372393, 0.022383305310115148, 0.020020267479223943, 0.017759319558004215, 0.015624047755243337, 0.013632376843449557, 0.011796696263059339, 0.010124183346261053, 0.008617283775659837, 0.007274306195427147, 0.006090087745647572, 0.005056689785065528, 0.00416408765212899, 0.003400824362087736, 0.0027546050092919216, 0.002212815741090006, 0.0],
            "type": "arbitrary",
        },
        "-5400757542881065106_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "7038216929604661594_i": {
            "samples": [0.0022084107524006375, 0.0027387880012189475, 0.0033695725460432756, 0.004112718991022128, 0.004979905402541571, 0.005982062972914511, 0.007128837233564075, 0.008427994594487299, 0.009884794131735198, 0.011501350540878646, 0.01327601952784993, 0.015202841086232495, 0.017271078583235244, 0.01946489187090932, 0.021763180388161444, 0.024139627215236197, 0.026562967279791676, 0.02899749261713379, 0.03140379522113198, 0.033739734277870206, 0.03596160033132889, 0.038025435198323014, 0.03988845428739891, 0.04151050840112763, 0.042855515995282936, 0.043892794889926215, 0.044598224938458914] + [0.04495518017940069] * 2 + [0.044598224938458914, 0.043892794889926215, 0.042855515995282936, 0.04151050840112763, 0.03988845428739891, 0.038025435198323014, 0.03596160033132889, 0.033739734277870206, 0.03140379522113198, 0.02899749261713379, 0.026562967279791676, 0.024139627215236197, 0.021763180388161444, 0.01946489187090932, 0.017271078583235244, 0.015202841086232495, 0.01327601952784993, 0.011501350540878646, 0.009884794131735198, 0.008427994594487299, 0.007128837233564075, 0.005982062972914511, 0.004979905402541571, 0.004112718991022128, 0.0033695725460432756, 0.0027387880012189475, 0.0022084107524006375],
            "type": "arbitrary",
        },
        "7038216929604661594_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "-3202997854877898243_i": {
            "samples": [0.0022041672610212623, 0.0027235967694566334, 0.003339637417765964, 0.004063629189209328, 0.004906672471959597, 0.005879201050812177, 0.0069904929146177245, 0.00824813067227343, 0.00965742870156196, 0.01122084939497833, 0.01293743560534336, 0.014802290186514024, 0.016806135924491428, 0.018934989754037124, 0.021169983629724904, 0.023487360566243804, 0.025858668138996333, 0.028251163287007264, 0.030628431927808918, 0.032951215211532645, 0.035178421908103295, 0.03726829425836711, 0.03917968351030313, 0.04087338217883925, 0.04231345359995032, 0.043468496224329134, 0.04431278071652505, 0.04482720242454831, 0.045, 0.04482720242454831, 0.04431278071652505, 0.043468496224329134, 0.04231345359995032, 0.04087338217883925, 0.03917968351030313, 0.03726829425836711, 0.035178421908103295, 0.032951215211532645, 0.030628431927808918, 0.028251163287007264, 0.025858668138996333, 0.023487360566243804, 0.021169983629724904, 0.018934989754037124, 0.016806135924491428, 0.014802290186514024, 0.01293743560534336, 0.01122084939497833, 0.00965742870156196, 0.00824813067227343, 0.0069904929146177245, 0.005879201050812177, 0.004906672471959597, 0.004063629189209328, 0.003339637417765964, 0.0027235967694566334, 0.0022041672610212623] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3202997854877898243_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "-2981503795679182995_i": {
            "samples": [0.0022000765535638445, 0.0027089951403200833, 0.003310938727159947, 0.004016673638096744, 0.004836758825351658, 0.005781157536901707, 0.006858792431400477, 0.00807705425873921, 0.009441278859598588, 0.010954211822799577, 0.012615484334646553, 0.014421127187472583, 0.01636315220799365, 0.018429231169743602, 0.020602501279722647, 0.022861523385990394, 0.025180414076097682, 0.027529165912161934, 0.029874161425676646, 0.03217887658333588, 0.03440475878802271, 0.03651225376285231, 0.03846194561401491, 0.04021576572467536, 0.0417382195917189, 0.04299757686225765, 0.04396696907260694, 0.04462534214256114] + [0.0449582164972744] * 2 + [0.04462534214256114, 0.04396696907260694, 0.04299757686225765, 0.0417382195917189, 0.04021576572467536, 0.03846194561401491, 0.03651225376285231, 0.03440475878802271, 0.03217887658333588, 0.029874161425676646, 0.027529165912161934, 0.025180414076097682, 0.022861523385990394, 0.020602501279722647, 0.018429231169743602, 0.01636315220799365, 0.014421127187472583, 0.012615484334646553, 0.010954211822799577, 0.009441278859598588, 0.00807705425873921, 0.006858792431400477, 0.005781157536901707, 0.004836758825351658, 0.004016673638096744, 0.003310938727159947, 0.0027089951403200833, 0.0022000765535638445] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2981503795679182995_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "2873031789234274895_i": {
            "samples": [0.002196130531869861, 0.00269494965987533, 0.0032834025361357256, 0.003971719471492274, 0.00476995154594304, 0.005687616866699139, 0.006733295339340903, 0.007914180653231268, 0.009235602220084849, 0.010700533823254657, 0.012309109451161164, 0.014058169889185347, 0.01594086581103374, 0.017946344042468355, 0.020059543113723828, 0.022261121993637233, 0.024527541931425485, 0.026831315665573872, 0.029141431071326555, 0.03142394792159734, 0.03364275726798451, 0.035760483547890354, 0.03773950049698226, 0.039543023924107475, 0.04113623799411029, 0.04248740739295065, 0.04356892602588164, 0.04435825396678133, 0.04483869828757789, 0.045, 0.04483869828757789, 0.04435825396678133, 0.04356892602588164, 0.04248740739295065, 0.04113623799411029, 0.039543023924107475, 0.03773950049698226, 0.035760483547890354, 0.03364275726798451, 0.03142394792159734, 0.029141431071326555, 0.026831315665573872, 0.024527541931425485, 0.022261121993637233, 0.020059543113723828, 0.017946344042468355, 0.01594086581103374, 0.014058169889185347, 0.012309109451161164, 0.010700533823254657, 0.009235602220084849, 0.007914180653231268, 0.006733295339340903, 0.005687616866699139, 0.00476995154594304, 0.003971719471492274, 0.0032834025361357256, 0.00269494965987533, 0.002196130531869861, 0.0],
            "type": "arbitrary",
        },
        "2873031789234274895_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "-783744107676016132_i": {
            "samples": [0.0021923216596943657, 0.002681429344289374, 0.0032569606163357313, 0.003928644416596959, 0.004706055058005065, 0.005598289478878552, 0.006613597570109367, 0.007758973075218877, 0.009039716086480309, 0.010458981687450198, 0.01201733258518545, 0.013712316371840982, 0.015538090084714525, 0.017485115738056386, 0.019539950256436477, 0.02168515158433456, 0.023899319596590533, 0.02615728580430365, 0.028430459865181792, 0.030687333803565666, 0.03289413696746988, 0.035015626532756805, 0.03701599030793991, 0.03885983122874933, 0.04051319678373799, 0.04194461215617874, 0.04312607348933794, 0.04403395764329525, 0.044649807221710955] + [0.0449609544493054] * 2 + [0.044649807221710955, 0.04403395764329525, 0.04312607348933794, 0.04194461215617874, 0.04051319678373799, 0.03885983122874933, 0.03701599030793991, 0.035015626532756805, 0.03289413696746988, 0.030687333803565666, 0.028430459865181792, 0.02615728580430365, 0.023899319596590533, 0.02168515158433456, 0.019539950256436477, 0.017485115738056386, 0.015538090084714525, 0.013712316371840982, 0.01201733258518545, 0.010458981687450198, 0.009039716086480309, 0.007758973075218877, 0.006613597570109367, 0.005598289478878552, 0.004706055058005065, 0.003928644416596959, 0.0032569606163357313, 0.002681429344289374, 0.0021923216596943657],
            "type": "arbitrary",
        },
        "-783744107676016132_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "5070791477237441758_i": {
            "samples": [0.0021886429148360656, 0.0026684054570661002, 0.003231549913927979, 0.003887335775491176, 0.004644889435378892, 0.0055129092683462695, 0.006499327892100825, 0.007610938089798383, 0.00885299195172299, 0.010228785895018255, 0.011739247140411496, 0.01338253974378367, 0.015153710168604475, 0.01704439342104495, 0.01904260075800304, 0.021132608770249143, 0.023294967153449017, 0.025506638703374357, 0.027741280092557885, 0.029969665982641225, 0.03216025226948306, 0.03427986709655573, 0.03629451111718945, 0.038170241784092104, 0.0398741106459297, 0.041375118156849744, 0.042645147713701946, 0.043659839791339576, 0.04439936829374993, 0.04484908458732194, 0.045, 0.04484908458732194, 0.04439936829374993, 0.043659839791339576, 0.042645147713701946, 0.041375118156849744, 0.0398741106459297, 0.038170241784092104, 0.03629451111718945, 0.03427986709655573, 0.03216025226948306, 0.029969665982641225, 0.027741280092557885, 0.025506638703374357, 0.023294967153449017, 0.021132608770249143, 0.01904260075800304, 0.01704439342104495, 0.015153710168604475, 0.01338253974378367, 0.011739247140411496, 0.010228785895018255, 0.00885299195172299, 0.007610938089798383, 0.006499327892100825, 0.0055129092683462695, 0.004644889435378892, 0.003887335775491176, 0.003231549913927979, 0.0026684054570661002, 0.0021886429148360656] + [0.0] * 3,
            "type": "arbitrary",
        },
        "5070791477237441758_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "4449465709350748214_i": {
            "samples": [0.002185087746075712, 0.002655851309862345, 0.003207112072979275, 0.0038476895203500205, 0.00458628890050234, 0.005431231325399248, 0.006390144762382165, 0.007469621523042266, 0.008674850554271462, 0.01000923556603093, 0.011474012621772363, 0.013067883084571026, 0.014786679559752713, 0.016623083512700733, 0.01856641339812717, 0.020602501279722643, 0.022713673963176244, 0.024878851591730918, 0.027073772516205467, 0.02927134818388462, 0.031442146003505825, 0.033554991917466456, 0.035577678084197664, 0.0374777550166612, 0.039223382122376235, 0.04078420621619092, 0.04213223455563385, 0.04324266753656638, 0.04409465654787863, 0.04467195467294955] + [0.044963431879664346] * 2 + [0.04467195467294955, 0.04409465654787863, 0.04324266753656638, 0.04213223455563385, 0.04078420621619092, 0.039223382122376235, 0.0374777550166612, 0.035577678084197664, 0.033554991917466456, 0.031442146003505825, 0.02927134818388462, 0.027073772516205467, 0.024878851591730918, 0.022713673963176244, 0.020602501279722643, 0.01856641339812717, 0.016623083512700733, 0.014786679559752713, 0.013067883084571026, 0.011474012621772363, 0.01000923556603093, 0.008674850554271462, 0.007469621523042266, 0.006390144762382165, 0.005431231325399248, 0.00458628890050234, 0.0038476895203500205, 0.003207112072979275, 0.002655851309862345, 0.002185087746075712] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4449465709350748214_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "4670959768549463462_i": {
            "samples": [0.002181650034369001, 0.002643742084033377, 0.003183593010117178, 0.0038096094880138505, 0.004530100489780403, 0.0053530299250222225, 0.006285733522147417, 0.007334604810083049, 0.008504757430977157, 0.009799673420622566, 0.011220849394978335, 0.012767454620626752, 0.01443601655818671, 0.01622015048690195, 0.018110350096950997, 0.0200938553525385, 0.02215461240329424, 0.024273337825693204, 0.026427696042506662, 0.028592594494596158, 0.030740596189361813, 0.03284244384848766, 0.03486768429974622, 0.036785376314758506, 0.03856486011458755, 0.040176562570300486, 0.04159280900995399, 0.0427886107493784, 0.043742397162897365, 0.04443666238597582, 0.044858499582217694, 0.045, 0.044858499582217694, 0.04443666238597582, 0.043742397162897365, 0.0427886107493784, 0.04159280900995399, 0.040176562570300486, 0.03856486011458755, 0.036785376314758506, 0.03486768429974622, 0.03284244384848766, 0.030740596189361813, 0.028592594494596158, 0.026427696042506662, 0.024273337825693204, 0.02215461240329424, 0.0200938553525385, 0.018110350096950997, 0.01622015048690195, 0.01443601655818671, 0.012767454620626752, 0.011220849394978335, 0.009799673420622566, 0.008504757430977157, 0.007334604810083049, 0.006285733522147417, 0.0053530299250222225, 0.004530100489780403, 0.0038096094880138505, 0.003183593010117178, 0.002643742084033377, 0.002181650034369001, 0.0],
            "type": "arbitrary",
        },
        "4670959768549463462_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "-3522891337262262136_i": {
            "samples": [0.0021783240578117802, 0.0026320546704428397, 0.0031609425342021065, 0.0037730066615581682, 0.0044761828645273165, 0.005278096735337163, 0.006185803894099255, 0.007205501725868167, 0.00834221891399041, 0.009599491201180295, 0.010979033855880314, 0.012480423155625142, 0.014100800679714075, 0.015834615189656717, 0.01767341723767234, 0.01960572127284428, 0.02161694883567558, 0.023689464411198798, 0.02580271266467483, 0.027933462183037508, 0.030056156616078404, 0.03214336943314592, 0.03416635360856382, 0.03609567268084811, 0.03790189507499922, 0.03955632961299501, 0.04103177702677753, 0.042303270255439764, 0.04334877552461066, 0.0441498267730566, 0.04469206793220909] + [0.04496568081800304] * 2 + [0.04469206793220909, 0.0441498267730566, 0.04334877552461066, 0.042303270255439764, 0.04103177702677753, 0.03955632961299501, 0.03790189507499922, 0.03609567268084811, 0.03416635360856382, 0.03214336943314592, 0.030056156616078404, 0.027933462183037508, 0.02580271266467483, 0.023689464411198798, 0.02161694883567558, 0.01960572127284428, 0.01767341723767234, 0.015834615189656717, 0.014100800679714075, 0.012480423155625142, 0.010979033855880314, 0.009599491201180295, 0.00834221891399041, 0.007205501725868167, 0.006185803894099255, 0.005278096735337163, 0.0044761828645273165, 0.0037730066615581682, 0.0031609425342021065, 0.0026320546704428397, 0.0021783240578117802],
            "type": "arbitrary",
        },
        "-3522891337262262136_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "6868719456552630325_i": {
            "samples": [0.0021751044599569004, 0.002620767525400632, 0.00313911400558867, 0.0037377985282149332, 0.004424405249577707, 0.005206239218437463, 0.006090087745647572, 0.007081955454679527, 0.00818677852451955, 0.009408125515012428, 0.01074789398542346, 0.01220601376639065, 0.013780169102611905, 0.015465552827263584, 0.01725466614595881, 0.01913717740164616, 0.021099852291742723, 0.02312656637865019, 0.02519840837916, 0.027293879687068503, 0.029389191973642894, 0.03145866066493294, 0.033475187796194086, 0.03541082340652936, 0.03723739049602661, 0.03892715486391898, 0.04045351811076749, 0.041791709925866324, 0.04291945465770895, 0.04381758719122487, 0.04447059437758889, 0.044867060658126935, 0.045, 0.044867060658126935, 0.04447059437758889, 0.04381758719122487, 0.04291945465770895, 0.041791709925866324, 0.04045351811076749, 0.03892715486391898, 0.03723739049602661, 0.03541082340652936, 0.033475187796194086, 0.03145866066493294, 0.029389191973642894, 0.027293879687068503, 0.02519840837916, 0.02312656637865019, 0.021099852291742723, 0.01913717740164616, 0.01725466614595881, 0.015465552827263584, 0.013780169102611905, 0.01220601376639065, 0.01074789398542346, 0.009408125515012428, 0.00818677852451955, 0.007081955454679527, 0.006090087745647572, 0.005206239218437463, 0.004424405249577707, 0.0037377985282149332, 0.00313911400558867, 0.002620767525400632, 0.0021751044599569004] + [0.0] * 3,
            "type": "arbitrary",
        },
        "6868719456552630325_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-1325131649259095273_i": {
            "samples": [0.002171986221114665, 0.002609860540872116, 0.003118064030284104, 0.00370390850444649, 0.004374646484101372, 0.005137279200435915, 0.005998337086518649, 0.006963635959888166, 0.008038013721346155, 0.009225054058572166, 0.01052680526488461, 0.011943503766852505, 0.013473313196074164, 0.015112090735730868, 0.01685319292267304, 0.018687333005137006, 0.020602501279722647, 0.022583958521671287, 0.024614310676048176, 0.02667367042822907, 0.028739908193952862, 0.030788991575058402, 0.03279540856535964, 0.034732665939567205, 0.036573850514480734, 0.03829223754247891, 0.039861927585410406, 0.0412584910079413, 0.04245959787865623, 0.043445610688308, 0.044200117949938736, 0.044710388440118876] + [0.0449677285193337] * 2 + [0.044710388440118876, 0.044200117949938736, 0.043445610688308, 0.04245959787865623, 0.0412584910079413, 0.039861927585410406, 0.03829223754247891, 0.036573850514480734, 0.034732665939567205, 0.03279540856535964, 0.030788991575058402, 0.028739908193952862, 0.02667367042822907, 0.024614310676048176, 0.022583958521671287, 0.020602501279722647, 0.018687333005137006, 0.01685319292267304, 0.015112090735730868, 0.013473313196074164, 0.011943503766852505, 0.01052680526488461, 0.009225054058572166, 0.008038013721346155, 0.006963635959888166, 0.005998337086518649, 0.005137279200435915, 0.004374646484101372, 0.00370390850444649, 0.003118064030284104, 0.002609860540872116, 0.002171986221114665] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1325131649259095273_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "5055899984944537846_i": {
            "samples": [0.0021689646323143747, 0.00259931492734166, 0.0030977521849327484, 0.0036712654202062777, 0.004326794171231298, 0.005071051590628177, 0.005910322273415651, 0.00685023762010808, 0.007895532966577221, 0.00904979218747297, 0.01031518692593761, 0.0116922189367116, 0.013179475163895156, 0.014773406018382276, 0.016468137787138275, 0.0182553301210571, 0.02012408905060979, 0.022060944931844295, 0.02404990312009857, 0.026072573027081374, 0.02810837859433496, 0.030134850201614855, 0.03212799474266039, 0.03406273718987366, 0.03591342359971117, 0.03765437235880761, 0.03926045771391213, 0.04070770743270076, 0.041973894951609594, 0.04303910569305359, 0.04388625744905485, 0.044501555855697046, 0.04487486799687647, 0.045, 0.04487486799687647, 0.044501555855697046, 0.04388625744905485, 0.04303910569305359, 0.041973894951609594, 0.04070770743270076, 0.03926045771391213, 0.03765437235880761, 0.03591342359971117, 0.03406273718987366, 0.03212799474266039, 0.030134850201614855, 0.02810837859433496, 0.026072573027081374, 0.02404990312009857, 0.022060944931844295, 0.02012408905060979, 0.0182553301210571, 0.016468137787138275, 0.014773406018382276, 0.013179475163895156, 0.0116922189367116, 0.01031518692593761, 0.00904979218747297, 0.007895532966577221, 0.00685023762010808, 0.005910322273415651, 0.005071051590628177, 0.004326794171231298, 0.0036712654202062777, 0.0030977521849327484, 0.00259931492734166, 0.0021689646323143747, 0.0],
            "type": "arbitrary",
        },
        "5055899984944537846_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-1822497030040153629_i": {
            "samples": [0.002166035271643658, 0.0025891131079189447, 0.003078140769086128, 0.0036398030554722935, 0.004280743914885552, 0.0050074032323041, 0.005825830397858919, 0.006741477102010137, 0.007758973075218879, 0.008881889799595737, 0.01011249851057478, 0.011451530007377753, 0.012897944825849661, 0.014448723118231133, 0.016098684056405882, 0.01784034466081627, 0.019663827602424643, 0.02155682669389912, 0.023504637465419673, 0.025490258423118042, 0.027494566355442732, 0.02949656645461664, 0.03147371515396398, 0.03340231056809872, 0.035257942401047876, 0.03701599030793991, 0.03865215711254247, 0.040143021143175674, 0.04146659038536539, 0.04260284026867511, 0.04353421678295046, 0.044246087293011806, 0.04472712288590957] + [0.04496959829325634] * 2 + [0.04472712288590957, 0.044246087293011806, 0.04353421678295046, 0.04260284026867511, 0.04146659038536539, 0.040143021143175674, 0.03865215711254247, 0.03701599030793991, 0.035257942401047876, 0.03340231056809872, 0.03147371515396398, 0.02949656645461664, 0.027494566355442732, 0.025490258423118042, 0.023504637465419673, 0.02155682669389912, 0.019663827602424643, 0.01784034466081627, 0.016098684056405882, 0.014448723118231133, 0.012897944825849661, 0.011451530007377753, 0.01011249851057478, 0.008881889799595737, 0.007758973075218879, 0.006741477102010137, 0.005825830397858919, 0.0050074032323041, 0.004280743914885552, 0.0036398030554722935, 0.003078140769086128, 0.0025891131079189447, 0.002166035271643658],
            "type": "arbitrary",
        },
        "-1822497030040153629_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-3304235285041581290_i": {
            "samples": [0.002163193982716146, 0.002579238622452966, 0.0030591945816725377, 0.003609459723038464, 0.0042363986336785495, 0.00494619186999557, 0.005744663836344411, 0.0066370914436332945, 0.007627996818823539, 0.008720928501502967, 0.009918236716819908, 0.011220849394978333, 0.012628056550846435, 0.014137311375621348, 0.015744056860317837, 0.017441586908559705, 0.019220950654690473, 0.021070908048339047, 0.0229779436827221, 0.02492634433738389, 0.02689834380683798, 0.028874336349259823, 0.030833157592210256, 0.03275242907474077, 0.034608959903622755, 0.03637919638388446, 0.038039708083193915, 0.03956769673606484, 0.04094151280701048, 0.04214116351304094, 0.043148795731562835, 0.04394913753524951, 0.04452988311146775, 0.04488200751433152, 0.045, 0.04488200751433152, 0.04452988311146775, 0.04394913753524951, 0.043148795731562835, 0.04214116351304094, 0.04094151280701048, 0.03956769673606484, 0.038039708083193915, 0.03637919638388446, 0.034608959903622755, 0.03275242907474077, 0.030833157592210256, 0.028874336349259823, 0.02689834380683798, 0.02492634433738389, 0.0229779436827221, 0.021070908048339047, 0.019220950654690473, 0.017441586908559705, 0.015744056860317837, 0.014137311375621348, 0.012628056550846435, 0.011220849394978333, 0.009918236716819908, 0.008720928501502967, 0.007627996818823539, 0.0066370914436332945, 0.005744663836344411, 0.00494619186999557, 0.0042363986336785495, 0.003609459723038464, 0.0030591945816725377, 0.002579238622452966, 0.002163193982716146] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3304235285041581290_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "4901294004185410489_i": {
            "samples": [0.0021604368550476164, 0.002569676040571002, 0.0030408807189704046, 0.003580177892320246, 0.004193667943116493, 0.00488728521988948, 0.005666638944560216, 0.006536836325154024, 0.007502290756732057, 0.008566519031111391, 0.009731932507344929, 0.010999628168486271, 0.012369186349601104, 0.013838482608945404, 0.01540352167143638, 0.017058301548348594, 0.0187947157852923, 0.02060250127972264, 0.022469238222628894, 0.024380407457957384, 0.026319508939098797, 0.028268243036700006, 0.03020675427893248, 0.03211393476571738, 0.03396778208950533, 0.035745804225606435, 0.037425461639280226, 0.038984634909117126, 0.04040210459417239, 0.04165802896999096, 0.04273440470076863, 0.043615495551435485, 0.044288214895822076, 0.04474244903575] + [0.04497131016992334] * 2 + [0.04474244903575, 0.044288214895822076, 0.043615495551435485, 0.04273440470076863, 0.04165802896999096, 0.04040210459417239, 0.038984634909117126, 0.037425461639280226, 0.035745804225606435, 0.03396778208950533, 0.03211393476571738, 0.03020675427893248, 0.028268243036700006, 0.026319508939098797, 0.024380407457957384, 0.022469238222628894, 0.02060250127972264, 0.0187947157852923, 0.017058301548348594, 0.01540352167143638, 0.013838482608945404, 0.012369186349601104, 0.010999628168486271, 0.009731932507344929, 0.008566519031111391, 0.007502290756732057, 0.006536836325154024, 0.005666638944560216, 0.00488728521988948, 0.004193667943116493, 0.003580177892320246, 0.0030408807189704046, 0.002569676040571002, 0.0021604368550476164] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4901294004185410489_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "6327331914969551184_i": {
            "samples": [0.0021577602061462007, 0.00256041088269117, 0.0030231683917254235, 0.003551903849593068, 0.0041524675983879485, 0.004830560131804775, 0.005591584879652752, 0.006440484506803888, 0.007381563271341646, 0.008418298912115105, 0.009553148459435458, 0.010787353240006802, 0.012120749129840432, 0.013551588746267273, 0.015076382712201393, 0.016689767326000245, 0.018384405888755034, 0.020150930547545298, 0.021977930790704685, 0.02385199367719188, 0.025757799511374038, 0.027678275019371663, 0.029594804193792443, 0.03148749491696293, 0.03333549732966061, 0.035117367774724025, 0.036811470111183776, 0.03839640436462706, 0.03985145114932052, 0.04115701915355455, 0.042295082293231645, 0.0432495929617966, 0.044006858165732, 0.044555866236682166, 0.044888553229553804, 0.045, 0.044888553229553804, 0.044555866236682166, 0.044006858165732, 0.0432495929617966, 0.042295082293231645, 0.04115701915355455, 0.03985145114932052, 0.03839640436462706, 0.036811470111183776, 0.035117367774724025, 0.03333549732966061, 0.03148749491696293, 0.029594804193792443, 0.027678275019371663, 0.025757799511374038, 0.02385199367719188, 0.021977930790704685, 0.020150930547545298, 0.018384405888755034, 0.016689767326000245, 0.015076382712201393, 0.013551588746267273, 0.012120749129840432, 0.010787353240006802, 0.009553148459435458, 0.008418298912115105, 0.007381563271341646, 0.006440484506803888, 0.005591584879652752, 0.004830560131804775, 0.0041524675983879485, 0.003551903849593068, 0.0030231683917254235, 0.00256041088269117, 0.0021577602061462007, 0.0],
            "type": "arbitrary",
        },
        "6327331914969551184_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "-8312240252497376781_i": {
            "samples": [0.0021551605651445723, 0.0025514295481710446, 0.003006028759341267, 0.003524587390652799, 0.004112718991022126, 0.004775901832574295, 0.005519342536486394, 0.006347824416011567, 0.007265542786415831, 0.00827593031799268, 0.009381476336160563, 0.010583544763801127, 0.011882196113555836, 0.013276019527849927, 0.01476198128821445, 0.016335296431938186, 0.01798933008740271, 0.019715534841786272, 0.021503429868766095, 0.023340626664609936, 0.025212905078076605, 0.02710434189748496, 0.02899749261713379, 0.030873625199486478, 0.032713002746540806, 0.03449521007116611, 0.03619951730125708, 0.037805271943342475, 0.03929230936293479, 0.04064137048494054, 0.04183451474617286, 0.042855515995282936, 0.043690229166174925, 0.04432691616061069, 0.04475652045276505] + [0.04497288143846635] * 2 + [0.04475652045276505, 0.04432691616061069, 0.043690229166174925, 0.042855515995282936, 0.04183451474617286, 0.04064137048494054, 0.03929230936293479, 0.037805271943342475, 0.03619951730125708, 0.03449521007116611, 0.032713002746540806, 0.030873625199486478, 0.02899749261713379, 0.02710434189748496, 0.025212905078076605, 0.023340626664609936, 0.021503429868766095, 0.019715534841786272, 0.01798933008740271, 0.016335296431938186, 0.01476198128821445, 0.013276019527849927, 0.011882196113555836, 0.010583544763801127, 0.009381476336160563, 0.00827593031799268, 0.007265542786415831, 0.006347824416011567, 0.005519342536486394, 0.004775901832574295, 0.004112718991022126, 0.003524587390652799, 0.003006028759341267, 0.0025514295481710446, 0.0021551605651445723],
            "type": "arbitrary",
        },
        "-8312240252497376781_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "8525091602972718047_i": {
            "samples": [0.0021526346578215473, 0.0025427192498536683, 0.0029894347793242714, 0.0034981815423799265, 0.004074348693517276, 0.004723203241918649, 0.005449763585535232, 0.006258658867933907, 0.0071539761497483294, 0.00813909812557603, 0.009216534860031633, 0.01038775373056061, 0.0116530124132898, 0.0130112002934734, 0.014459694085719213, 0.01599423367485511, 0.017608824203925306, 0.019295670215758183, 0.021045147181805075, 0.022845815020008063, 0.024684477217809496, 0.026546287955502738, 0.028414908200599404, 0.030272710160164185, 0.03210102779105792, 0.03388044934312591, 0.03559114621970404, 0.03721323085893177, 0.03872713494344725, 0.04011399810594215, 0.0413560564763048, 0.04243701996316964, 0.04334242711385802, 0.04405996676942095, 0.04457975652392329, 0.04489456918749988, 0.045, 0.04489456918749988, 0.04457975652392329, 0.04405996676942095, 0.04334242711385802, 0.04243701996316964, 0.0413560564763048, 0.04011399810594215, 0.03872713494344725, 0.03721323085893177, 0.03559114621970404, 0.03388044934312591, 0.03210102779105792, 0.030272710160164185, 0.028414908200599404, 0.026546287955502738, 0.024684477217809496, 0.022845815020008063, 0.021045147181805075, 0.019295670215758183, 0.017608824203925306, 0.01599423367485511, 0.014459694085719213, 0.0130112002934734, 0.0116530124132898, 0.01038775373056061, 0.009216534860031633, 0.00813909812557603, 0.0071539761497483294, 0.006258658867933907, 0.005449763585535232, 0.004723203241918649, 0.004074348693517276, 0.0034981815423799265, 0.0029894347793242714, 0.0025427192498536683, 0.0021526346578215473] + [0.0] * 3,
            "type": "arbitrary",
        },
        "8525091602972718047_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "-6114480564494209918_i": {
            "samples": [0.0021501793928774163, 0.0025342679543580195, 0.0029733610703794443, 0.0034726423101149877, 0.004037288046759245, 0.004672364352978906, 0.00538270960151913, 0.006172803905368992, 0.00704662716352945, 0.00800750814011312, 0.00905796767184457, 0.010199559743662337, 0.011432714762644666, 0.01275658986367743, 0.014168931462649895, 0.01566595550244146, 0.017242250884816592, 0.01889071142409377, 0.020602501279722643, 0.02236705821708559, 0.024172138211441818, 0.026003903862479198, 0.02784705785134705, 0.02968502128437544, 0.03150015527426285, 0.03327402256535433, 0.034987684476295855, 0.0366220269762337, 0.03815810839596251, 0.03957752016653072, 0.04086275113228451, 0.04199754545138831, 0.04296724391052138, 0.0437590986631742, 0.044362551957982076, 0.044769470343010764] + [0.04497432708505203] * 2 + [0.044769470343010764, 0.044362551957982076, 0.0437590986631742, 0.04296724391052138, 0.04199754545138831, 0.04086275113228451, 0.03957752016653072, 0.03815810839596251, 0.0366220269762337, 0.034987684476295855, 0.03327402256535433, 0.03150015527426285, 0.02968502128437544, 0.02784705785134705, 0.026003903862479198, 0.024172138211441818, 0.02236705821708559, 0.020602501279722643, 0.01889071142409377, 0.017242250884816592, 0.01566595550244146, 0.014168931462649895, 0.01275658986367743, 0.011432714762644666, 0.010199559743662337, 0.00905796767184457, 0.00800750814011312, 0.00704662716352945, 0.006172803905368992, 0.00538270960151913, 0.004672364352978906, 0.004037288046759245, 0.0034726423101149877, 0.0029733610703794443, 0.0025342679543580195, 0.0021501793928774163] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6114480564494209918_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "-4688442653710069223_i": {
            "samples": [0.002147791849342387, 0.0025260643275360176, 0.0029577837877438713, 0.0034479284481222067, 0.0040014727856723855, 0.004623291670612245, 0.005318051273180125, 0.006090087745647572, 0.006943275247570575, 0.007880885475531793, 0.00890544145876266, 0.010018568964550093, 0.01122084939497833, 0.012511678520393735, 0.013889135755647852, 0.01534986891434664, 0.01688899944831298, 0.018500053072823434, 0.020174920377342438, 0.021903851518198725, 0.02367548838420554, 0.025476936728273888, 0.027293879687068503, 0.029110732895895854, 0.030910840085582453, 0.03267670666831609, 0.034390267432717066, 0.03603318313125636, 0.03758715951350724, 0.03903428129325348, 0.04035735268860909, 0.04154023558739861, 0.04256817610080444, 0.043428110300535616, 0.04410894029880399, 0.04460177252197282, 0.04490011102885229, 0.045, 0.04490011102885229, 0.04460177252197282, 0.04410894029880399, 0.043428110300535616, 0.04256817610080444, 0.04154023558739861, 0.04035735268860909, 0.03903428129325348, 0.03758715951350724, 0.03603318313125636, 0.034390267432717066, 0.03267670666831609, 0.030910840085582453, 0.029110732895895854, 0.027293879687068503, 0.025476936728273888, 0.02367548838420554, 0.021903851518198725, 0.020174920377342438, 0.018500053072823434, 0.01688899944831298, 0.01534986891434664, 0.013889135755647852, 0.012511678520393735, 0.01122084939497833, 0.010018568964550093, 0.00890544145876266, 0.007880885475531793, 0.006943275247570575, 0.006090087745647572, 0.005318051273180125, 0.004623291670612245, 0.0040014727856723855, 0.0034479284481222067, 0.0029577837877438713, 0.0025260643275360176, 0.002147791849342387, 0.0],
            "type": "arbitrary",
        },
        "-4688442653710069223_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "-7040808322472363443_i": {
            "samples": [0.002145469265010479, 0.0025180976845833327, 0.0029426805095074922, 0.0034240012507389377, 0.003966842699084948, 0.0045758977013691336, 0.005255667685714234, 0.006010349823505539, 0.0068437142221444685, 0.007758973075218878, 0.008758644236996193, 0.009844412214928072, 0.011016990063460089, 0.012275986089621082, 0.013619779619870707, 0.015045410303477688, 0.016548485517319054, 0.01812311037093041, 0.019761844574239264, 0.02145569001512742, 0.023194112298432084, 0.024965098728831677, 0.026755254292330614, 0.028549936128284808, 0.030333425817680976, 0.03208913758244995, 0.03379985923954389, 0.035448021531003945, 0.03701599030793991, 0.03848637503253217, 0.03984234622532486, 0.04106795386740071, 0.04214843840311731, 0.04307052590392806, 0.04382269916117862, 0.04439543697712503, 0.04478141470745432] + [0.04497566015139245] * 2 + [0.04478141470745432, 0.04439543697712503, 0.04382269916117862, 0.04307052590392806, 0.04214843840311731, 0.04106795386740071, 0.03984234622532486, 0.03848637503253217, 0.03701599030793991, 0.035448021531003945, 0.03379985923954389, 0.03208913758244995, 0.030333425817680976, 0.028549936128284808, 0.026755254292330614, 0.024965098728831677, 0.023194112298432084, 0.02145569001512742, 0.019761844574239264, 0.01812311037093041, 0.016548485517319054, 0.015045410303477688, 0.013619779619870707, 0.012275986089621082, 0.011016990063460089, 0.009844412214928072, 0.008758644236996193, 0.007758973075218878, 0.0068437142221444685, 0.006010349823505539, 0.005255667685714234, 0.0045758977013691336, 0.003966842699084948, 0.0034240012507389377, 0.0029426805095074922, 0.0025180976845833327, 0.002145469265010479],
            "type": "arbitrary",
        },
        "-7040808322472363443_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "2035348380515494895_i": {
            "samples": [0.0021432090258028083, 0.0025103579443485785, 0.0029280301328143657, 0.003400824362087738, 0.003933341320261181, 0.004530100489780402, 0.005195445668351942, 0.005933439920175686, 0.006747751198620647, 0.007641530360080955, 0.008617283775659838, 0.00967674322407993, 0.010820736195198617, 0.012049060126664212, 0.013360364413972401, 0.014752044254341146, 0.01622015048690195, 0.01775931955800422, 0.019362727557242443, 0.02102207192854205, 0.022727583958740687, 0.024468074487837863, 0.026231014481970672, 0.02800265118108745, 0.029768159504221858, 0.03151182729865732, 0.03321727189296453, 0.03486768429974622, 0.036446096356076804, 0.03793566513256709, 0.039319968128458664, 0.04058330213903772, 0.04171097826593652, 0.04268960536581334, 0.04350735431447342, 0.044154195807363496, 0.044622105018217416, 0.0449052272790755, 0.045, 0.0449052272790755, 0.044622105018217416, 0.044154195807363496, 0.04350735431447342, 0.04268960536581334, 0.04171097826593652, 0.04058330213903772, 0.039319968128458664, 0.03793566513256709, 0.036446096356076804, 0.03486768429974622, 0.03321727189296453, 0.03151182729865732, 0.029768159504221858, 0.02800265118108745, 0.026231014481970672, 0.024468074487837863, 0.022727583958740687, 0.02102207192854205, 0.019362727557242443, 0.01775931955800422, 0.01622015048690195, 0.014752044254341146, 0.013360364413972401, 0.012049060126664212, 0.010820736195198617, 0.00967674322407993, 0.008617283775659838, 0.007641530360080955, 0.006747751198620647, 0.005933439920175686, 0.005195445668351942, 0.004530100489780402, 0.003933341320261181, 0.003400824362087738, 0.0029280301328143657, 0.0025103579443485785, 0.0021432090258028083] + [0.0] * 3,
            "type": "arbitrary",
        },
        "2035348380515494895_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "-2269188906508187112_i": {
            "samples": [0.002141008655974335, 0.0025028355874354992, 0.0029138127789625334, 0.0033783636024714127, 0.0039009156449618795, 0.004485823196201629, 0.005137279200435915, 0.0058592173700232975, 0.006655205567335754, 0.007528331991962452, 0.008481086149534151, 0.00951523701029627, 0.010631711171939819, 0.011830474202861594, 0.013110418639099576, 0.014469262321099336, 0.015903460866896136, 0.01740813807020783, 0.018977037872588722, 0.020602501279722643, 0.022275471169779036, 0.023985527378951276, 0.025720953754510386, 0.027468838054007422, 0.029215204661970466, 0.030945179119672497, 0.03264318245137526, 0.03429315225781028, 0.03587878657292559, 0.03738380558232485, 0.038792225519649066, 0.040088638425953435, 0.0412584910079413, 0.042288355588599384, 0.04316618612562091, 0.043881552487627755, 0.04442584662486435, 0.044792454939364075] + [0.04497689202979855] * 2 + [0.044792454939364075, 0.04442584662486435, 0.043881552487627755, 0.04316618612562091, 0.042288355588599384, 0.0412584910079413, 0.040088638425953435, 0.038792225519649066, 0.03738380558232485, 0.03587878657292559, 0.03429315225781028, 0.03264318245137526, 0.030945179119672497, 0.029215204661970466, 0.027468838054007422, 0.025720953754510386, 0.023985527378951276, 0.022275471169779036, 0.020602501279722643, 0.018977037872588722, 0.01740813807020783, 0.015903460866896136, 0.014469262321099336, 0.013110418639099576, 0.011830474202861594, 0.010631711171939819, 0.00951523701029627, 0.008481086149534151, 0.007528331991962452, 0.006655205567335754, 0.0058592173700232975, 0.005137279200435915, 0.004485823196201629, 0.0039009156449618795, 0.0033783636024714127, 0.0029138127789625334, 0.0025028355874354992, 0.002141008655974335] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2269188906508187112_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "1537982999734436539_i": {
            "samples": [0.002138865809087063, 0.0024955216177367967, 0.0029000097065299086, 0.003356586809784028, 0.0038695158742528477, 0.004442993712003372, 0.005081068870094062, 0.005787550337006248, 0.006565908073257962, 0.007419166741676062, 0.008349794409521471, 0.009359588386083407, 0.01044956072980217, 0.011619826291553531, 0.012869496437953957, 0.014196581803098438, 0.015597907532670414, 0.017069044496358852, 0.018604259841200503, 0.020196490031619566, 0.021837339167665844, 0.023517104892288677, 0.02522483359781917, 0.026948405933114875, 0.028674652813496203, 0.03038950126827824, 0.03207814855252314, 0.03372526203140174, 0.03531520145056301, 0.03683225936864509, 0.0382609147826893, 0.03958609435604398, 0.04079343519026052, 0.0418695427915073, 0.04280223778600969, 0.04358078504860368, 0.04419609922635268, 0.04464092115967802, 0.044909960412638034, 0.045, 0.044909960412638034, 0.04464092115967802, 0.04419609922635268, 0.04358078504860368, 0.04280223778600969, 0.0418695427915073, 0.04079343519026052, 0.03958609435604398, 0.0382609147826893, 0.03683225936864509, 0.03531520145056301, 0.03372526203140174, 0.03207814855252314, 0.03038950126827824, 0.028674652813496203, 0.026948405933114875, 0.02522483359781917, 0.023517104892288677, 0.021837339167665844, 0.020196490031619566, 0.018604259841200503, 0.017069044496358852, 0.015597907532670414, 0.014196581803098438, 0.012869496437953957, 0.011619826291553531, 0.01044956072980217, 0.009359588386083407, 0.008349794409521471, 0.007419166741676062, 0.006565908073257962, 0.005787550337006248, 0.005081068870094062, 0.004442993712003372, 0.0038695158742528477, 0.003356586809784028, 0.0029000097065299086, 0.0024955216177367967, 0.002138865809087063, 0.0],
            "type": "arbitrary",
        },
        "1537982999734436539_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": -0.04,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con6": {
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
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 4),
            },
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
            },
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 6),
            },
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "D1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con6', 1),
                "out2": ('con6', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": -312360584.50398064,
            "operations": {
                "-8235708793481200348": "-8235708793481200348_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_4b8",
                "lo_frequency": 7450000000.0,
            },
        },
        "D1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-4689872528245954696": "-4689872528245954696",
                "-5399356442740566797": "-5399356442740566797",
                "-6020682210627260341": "-6020682210627260341",
                "5176650348720911465": "5176650348720911465",
                "-2490704707800638904": "-2490704707800638904",
                "2031613062289364412": "2031613062289364412",
                "2253107121488079660": "2253107121488079660",
                "-71450960598756793": "-71450960598756793",
                "-8265302066410482391": "-8265302066410482391",
                "5161758856428007553": "5161758856428007553",
                "-8762667447191540747": "-8762667447191540747",
                "-5846048319208600280": "-5846048319208600280",
                "-6564907759188373884": "-6564907759188373884",
                "-612838502181835934": "-612838502181835934",
                "1862115589237333143": "1862115589237333143",
                "1584921185821330929": "1584921185821330929",
                "5392093092063954580": "5392093092063954580",
                "1087555805040272573": "1087555805040272573",
                "-1264809863722021647": "-1264809863722021647",
                "-3201589722435749314": "-3201589722435749314",
                "-9209359323659574230": "-9209359323659574230",
                "-5402187417416950579": "-5402187417416950579",
                "-879869647326947263": "-879869647326947263",
                "-658375588128232015": "-658375588128232015",
                "-1778389818629643021": "-1778389818629643021",
                "-4130755487391937241": "-4130755487391937241",
                "6648633529796064006": "6648633529796064006",
                "-7275792773823484294": "-7275792773823484294",
                "-1711501740190055130": "-1711501740190055130",
                "-3745815270996862857": "-3745815270996862857",
                "-3524321211798147609": "-3524321211798147609",
                "155176731206446915": "155176731206446915",
                "-1326561523794980746": "-1326561523794980746",
                "-1105067464596265498": "-1105067464596265498",
                "3906648293231783600": "3906648293231783600",
                "8526499735414866976": "8526499735414866976",
                "6104407981234950463": "6104407981234950463",
                "6325902040433665711": "6325902040433665711",
                "-7598524263185882589": "-7598524263185882589",
                "-2489274833264753431": "-2489274833264753431",
                "-4412678124829952482": "-4412678124829952482",
                "-70021086062871320": "-70021086062871320",
                "53939301042763868": "53939301042763868",
                "8259468590269755647": "8259468590269755647",
                "-4622984449806366805": "-4622984449806366805",
                "314919130332203064": "314919130332203064",
                "-2037446538430091156": "-2037446538430091156",
                "-5009766010630318589": "-5009766010630318589",
                "-4238044233411292421": "-4238044233411292421",
                "-2812006322627151726": "-2812006322627151726",
                "5393522966599840053": "5393522966599840053",
                "5615017025798555301": "5615017025798555301",
                "3192925271618638788": "3192925271618638788",
                "7812776713801722164": "7812776713801722164",
                "2266597513640485263": "2266597513640485263",
                "-5400757542881065106": "-5400757542881065106",
                "7038216929604661594": "7038216929604661594",
                "-3202997854877898243": "-3202997854877898243",
                "-2981503795679182995": "-2981503795679182995",
                "2873031789234274895": "2873031789234274895",
                "-783744107676016132": "-783744107676016132",
                "5070791477237441758": "5070791477237441758",
                "4449465709350748214": "4449465709350748214",
                "4670959768549463462": "4670959768549463462",
                "-3522891337262262136": "-3522891337262262136",
                "6868719456552630325": "6868719456552630325",
                "-1325131649259095273": "-1325131649259095273",
                "5055899984944537846": "5055899984944537846",
                "-1822497030040153629": "-1822497030040153629",
                "-3304235285041581290": "-3304235285041581290",
                "4901294004185410489": "4901294004185410489",
                "6327331914969551184": "6327331914969551184",
                "-8312240252497376781": "-8312240252497376781",
                "8525091602972718047": "8525091602972718047",
                "-6114480564494209918": "-6114480564494209918",
                "-4688442653710069223": "-4688442653710069223",
                "-7040808322472363443": "-7040808322472363443",
                "2035348380515494895": "2035348380515494895",
                "-2269188906508187112": "-2269188906508187112",
                "1537982999734436539": "1537982999734436539",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_cb2",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "-4689872528245954696": {
            "length": 40,
            "waveforms": {
                "I": "-4689872528245954696_i",
                "Q": "-4689872528245954696_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8235708793481200348_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5725775278552983433_i",
                "Q": "-5725775278552983433_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "-5399356442740566797": {
            "length": 16,
            "waveforms": {
                "I": "-5399356442740566797_i",
                "Q": "-5399356442740566797_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6020682210627260341": {
            "length": 16,
            "waveforms": {
                "I": "-6020682210627260341_i",
                "Q": "-6020682210627260341_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5176650348720911465": {
            "length": 16,
            "waveforms": {
                "I": "5176650348720911465_i",
                "Q": "5176650348720911465_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2490704707800638904": {
            "length": 16,
            "waveforms": {
                "I": "-2490704707800638904_i",
                "Q": "-2490704707800638904_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2031613062289364412": {
            "length": 16,
            "waveforms": {
                "I": "2031613062289364412_i",
                "Q": "2031613062289364412_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2253107121488079660": {
            "length": 16,
            "waveforms": {
                "I": "2253107121488079660_i",
                "Q": "2253107121488079660_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-71450960598756793": {
            "length": 16,
            "waveforms": {
                "I": "-71450960598756793_i",
                "Q": "-71450960598756793_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8265302066410482391": {
            "length": 16,
            "waveforms": {
                "I": "-8265302066410482391_i",
                "Q": "-8265302066410482391_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5161758856428007553": {
            "length": 16,
            "waveforms": {
                "I": "5161758856428007553_i",
                "Q": "5161758856428007553_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8762667447191540747": {
            "length": 16,
            "waveforms": {
                "I": "-8762667447191540747_i",
                "Q": "-8762667447191540747_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5846048319208600280": {
            "length": 16,
            "waveforms": {
                "I": "-5846048319208600280_i",
                "Q": "-5846048319208600280_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6564907759188373884": {
            "length": 16,
            "waveforms": {
                "I": "-6564907759188373884_i",
                "Q": "-6564907759188373884_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-612838502181835934": {
            "length": 16,
            "waveforms": {
                "I": "-612838502181835934_i",
                "Q": "-612838502181835934_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1862115589237333143": {
            "length": 16,
            "waveforms": {
                "I": "1862115589237333143_i",
                "Q": "1862115589237333143_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1584921185821330929": {
            "length": 16,
            "waveforms": {
                "I": "1584921185821330929_i",
                "Q": "1584921185821330929_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5392093092063954580": {
            "length": 16,
            "waveforms": {
                "I": "5392093092063954580_i",
                "Q": "5392093092063954580_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1087555805040272573": {
            "length": 16,
            "waveforms": {
                "I": "1087555805040272573_i",
                "Q": "1087555805040272573_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1264809863722021647": {
            "length": 20,
            "waveforms": {
                "I": "-1264809863722021647_i",
                "Q": "-1264809863722021647_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3201589722435749314": {
            "length": 20,
            "waveforms": {
                "I": "-3201589722435749314_i",
                "Q": "-3201589722435749314_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9209359323659574230": {
            "length": 20,
            "waveforms": {
                "I": "-9209359323659574230_i",
                "Q": "-9209359323659574230_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5402187417416950579": {
            "length": 20,
            "waveforms": {
                "I": "-5402187417416950579_i",
                "Q": "-5402187417416950579_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-879869647326947263": {
            "length": 24,
            "waveforms": {
                "I": "-879869647326947263_i",
                "Q": "-879869647326947263_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-658375588128232015": {
            "length": 24,
            "waveforms": {
                "I": "-658375588128232015_i",
                "Q": "-658375588128232015_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1778389818629643021": {
            "length": 24,
            "waveforms": {
                "I": "-1778389818629643021_i",
                "Q": "-1778389818629643021_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4130755487391937241": {
            "length": 24,
            "waveforms": {
                "I": "-4130755487391937241_i",
                "Q": "-4130755487391937241_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6648633529796064006": {
            "length": 28,
            "waveforms": {
                "I": "6648633529796064006_i",
                "Q": "6648633529796064006_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7275792773823484294": {
            "length": 28,
            "waveforms": {
                "I": "-7275792773823484294_i",
                "Q": "-7275792773823484294_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1711501740190055130": {
            "length": 28,
            "waveforms": {
                "I": "-1711501740190055130_i",
                "Q": "-1711501740190055130_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3745815270996862857": {
            "length": 28,
            "waveforms": {
                "I": "-3745815270996862857_i",
                "Q": "-3745815270996862857_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3524321211798147609": {
            "length": 32,
            "waveforms": {
                "I": "-3524321211798147609_i",
                "Q": "-3524321211798147609_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "155176731206446915": {
            "length": 32,
            "waveforms": {
                "I": "155176731206446915_i",
                "Q": "155176731206446915_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1326561523794980746": {
            "length": 32,
            "waveforms": {
                "I": "-1326561523794980746_i",
                "Q": "-1326561523794980746_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1105067464596265498": {
            "length": 32,
            "waveforms": {
                "I": "-1105067464596265498_i",
                "Q": "-1105067464596265498_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3906648293231783600": {
            "length": 36,
            "waveforms": {
                "I": "3906648293231783600_i",
                "Q": "3906648293231783600_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8526499735414866976": {
            "length": 36,
            "waveforms": {
                "I": "8526499735414866976_i",
                "Q": "8526499735414866976_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6104407981234950463": {
            "length": 36,
            "waveforms": {
                "I": "6104407981234950463_i",
                "Q": "6104407981234950463_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6325902040433665711": {
            "length": 36,
            "waveforms": {
                "I": "6325902040433665711_i",
                "Q": "6325902040433665711_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7598524263185882589": {
            "length": 40,
            "waveforms": {
                "I": "-7598524263185882589_i",
                "Q": "-7598524263185882589_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2489274833264753431": {
            "length": 40,
            "waveforms": {
                "I": "-2489274833264753431_i",
                "Q": "-2489274833264753431_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4412678124829952482": {
            "length": 40,
            "waveforms": {
                "I": "-4412678124829952482_i",
                "Q": "-4412678124829952482_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-70021086062871320": {
            "length": 44,
            "waveforms": {
                "I": "-70021086062871320_i",
                "Q": "-70021086062871320_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "53939301042763868": {
            "length": 44,
            "waveforms": {
                "I": "53939301042763868_i",
                "Q": "53939301042763868_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8259468590269755647": {
            "length": 44,
            "waveforms": {
                "I": "8259468590269755647_i",
                "Q": "8259468590269755647_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4622984449806366805": {
            "length": 44,
            "waveforms": {
                "I": "-4622984449806366805_i",
                "Q": "-4622984449806366805_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "314919130332203064": {
            "length": 48,
            "waveforms": {
                "I": "314919130332203064_i",
                "Q": "314919130332203064_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2037446538430091156": {
            "length": 48,
            "waveforms": {
                "I": "-2037446538430091156_i",
                "Q": "-2037446538430091156_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5009766010630318589": {
            "length": 48,
            "waveforms": {
                "I": "-5009766010630318589_i",
                "Q": "-5009766010630318589_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4238044233411292421": {
            "length": 48,
            "waveforms": {
                "I": "-4238044233411292421_i",
                "Q": "-4238044233411292421_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2812006322627151726": {
            "length": 52,
            "waveforms": {
                "I": "-2812006322627151726_i",
                "Q": "-2812006322627151726_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5393522966599840053": {
            "length": 52,
            "waveforms": {
                "I": "5393522966599840053_i",
                "Q": "5393522966599840053_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5615017025798555301": {
            "length": 52,
            "waveforms": {
                "I": "5615017025798555301_i",
                "Q": "5615017025798555301_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3192925271618638788": {
            "length": 52,
            "waveforms": {
                "I": "3192925271618638788_i",
                "Q": "3192925271618638788_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7812776713801722164": {
            "length": 56,
            "waveforms": {
                "I": "7812776713801722164_i",
                "Q": "7812776713801722164_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2266597513640485263": {
            "length": 56,
            "waveforms": {
                "I": "2266597513640485263_i",
                "Q": "2266597513640485263_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5400757542881065106": {
            "length": 56,
            "waveforms": {
                "I": "-5400757542881065106_i",
                "Q": "-5400757542881065106_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7038216929604661594": {
            "length": 56,
            "waveforms": {
                "I": "7038216929604661594_i",
                "Q": "7038216929604661594_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3202997854877898243": {
            "length": 60,
            "waveforms": {
                "I": "-3202997854877898243_i",
                "Q": "-3202997854877898243_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2981503795679182995": {
            "length": 60,
            "waveforms": {
                "I": "-2981503795679182995_i",
                "Q": "-2981503795679182995_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2873031789234274895": {
            "length": 60,
            "waveforms": {
                "I": "2873031789234274895_i",
                "Q": "2873031789234274895_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-783744107676016132": {
            "length": 60,
            "waveforms": {
                "I": "-783744107676016132_i",
                "Q": "-783744107676016132_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5070791477237441758": {
            "length": 64,
            "waveforms": {
                "I": "5070791477237441758_i",
                "Q": "5070791477237441758_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4449465709350748214": {
            "length": 64,
            "waveforms": {
                "I": "4449465709350748214_i",
                "Q": "4449465709350748214_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4670959768549463462": {
            "length": 64,
            "waveforms": {
                "I": "4670959768549463462_i",
                "Q": "4670959768549463462_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3522891337262262136": {
            "length": 64,
            "waveforms": {
                "I": "-3522891337262262136_i",
                "Q": "-3522891337262262136_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6868719456552630325": {
            "length": 68,
            "waveforms": {
                "I": "6868719456552630325_i",
                "Q": "6868719456552630325_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1325131649259095273": {
            "length": 68,
            "waveforms": {
                "I": "-1325131649259095273_i",
                "Q": "-1325131649259095273_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5055899984944537846": {
            "length": 68,
            "waveforms": {
                "I": "5055899984944537846_i",
                "Q": "5055899984944537846_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1822497030040153629": {
            "length": 68,
            "waveforms": {
                "I": "-1822497030040153629_i",
                "Q": "-1822497030040153629_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3304235285041581290": {
            "length": 72,
            "waveforms": {
                "I": "-3304235285041581290_i",
                "Q": "-3304235285041581290_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4901294004185410489": {
            "length": 72,
            "waveforms": {
                "I": "4901294004185410489_i",
                "Q": "4901294004185410489_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6327331914969551184": {
            "length": 72,
            "waveforms": {
                "I": "6327331914969551184_i",
                "Q": "6327331914969551184_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8312240252497376781": {
            "length": 72,
            "waveforms": {
                "I": "-8312240252497376781_i",
                "Q": "-8312240252497376781_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8525091602972718047": {
            "length": 76,
            "waveforms": {
                "I": "8525091602972718047_i",
                "Q": "8525091602972718047_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6114480564494209918": {
            "length": 76,
            "waveforms": {
                "I": "-6114480564494209918_i",
                "Q": "-6114480564494209918_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4688442653710069223": {
            "length": 76,
            "waveforms": {
                "I": "-4688442653710069223_i",
                "Q": "-4688442653710069223_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7040808322472363443": {
            "length": 76,
            "waveforms": {
                "I": "-7040808322472363443_i",
                "Q": "-7040808322472363443_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2035348380515494895": {
            "length": 80,
            "waveforms": {
                "I": "2035348380515494895_i",
                "Q": "2035348380515494895_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2269188906508187112": {
            "length": 80,
            "waveforms": {
                "I": "-2269188906508187112_i",
                "Q": "-2269188906508187112_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1537982999734436539": {
            "length": 80,
            "waveforms": {
                "I": "1537982999734436539_i",
                "Q": "1537982999734436539_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-4689872528245954696_i": {
            "samples": [0.0023070262666795988, 0.0031044431662757732, 0.004112718991022126, 0.005363996778119129, 0.006887508198136117, 0.008706626172317102, 0.010835571342251184, 0.013276019527849927, 0.01601393634639623, 0.019017019945043494, 0.022233148808923724, 0.025590197417340237, 0.028997492617133785, 0.03234904063691291, 0.03552847063473545, 0.03841543626053164, 0.04089301903624815, 0.042855515995282936, 0.044215896103105515] + [0.044912195149836395] * 2 + [0.044215896103105515, 0.042855515995282936, 0.04089301903624815, 0.03841543626053164, 0.03552847063473545, 0.03234904063691291, 0.028997492617133785, 0.025590197417340237, 0.022233148808923724, 0.019017019945043494, 0.01601393634639623, 0.013276019527849927, 0.010835571342251184, 0.008706626172317102, 0.006887508198136117, 0.005363996778119129, 0.004112718991022126, 0.0031044431662757732, 0.0023070262666795988],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4689872528245954696_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5725775278552983433_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-5725775278552983433_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5399356442740566797_i": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5399356442740566797_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6020682210627260341_i": {
            "samples": [0.045] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6020682210627260341_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5176650348720911465_i": {
            "samples": [0.020602501279722643] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5176650348720911465_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2490704707800638904_i": {
            "samples": [0.011220849394978333, 0.045, 0.011220849394978333] + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2490704707800638904_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2031613062289364412_i": {
            "samples": [0.007758973075218879] + [0.03701599030793991] * 2 + [0.007758973075218879] + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2031613062289364412_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2253107121488079660_i": {
            "samples": [0.006090087745647572, 0.027293879687068503, 0.045, 0.027293879687068503, 0.006090087745647572] + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2253107121488079660_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-71450960598756793_i": {
            "samples": [0.005137279200435915, 0.020602501279722647] + [0.0412584910079413] * 2 + [0.020602501279722647, 0.005137279200435915] + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-71450960598756793_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8265302066410482391_i": {
            "samples": [0.004530100489780403, 0.01622015048690195, 0.03486768429974622, 0.045, 0.03486768429974622, 0.01622015048690195, 0.004530100489780403] + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8265302066410482391_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5161758856428007553_i": {
            "samples": [0.004112718991022128, 0.01327601952784993, 0.02899749261713379] + [0.042855515995282936] * 2 + [0.02899749261713379, 0.01327601952784993, 0.004112718991022128] + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5161758856428007553_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8762667447191540747_i": {
            "samples": [0.0038096094880138488, 0.01122084939497833, 0.024273337825693197, 0.03856486011458755, 0.045, 0.03856486011458755, 0.024273337825693197, 0.01122084939497833, 0.0038096094880138488] + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8762667447191540747_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5846048319208600280_i": {
            "samples": [0.003580177892320246, 0.009731932507344929, 0.02060250127972264, 0.03396778208950533] + [0.043615495551435485] * 2 + [0.03396778208950533, 0.02060250127972264, 0.009731932507344929, 0.003580177892320246] + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5846048319208600280_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6564907759188373884_i": {
            "samples": [0.003400824362087738, 0.008617283775659838, 0.01775931955800422, 0.029768159504221858, 0.04058330213903772, 0.045, 0.04058330213903772, 0.029768159504221858, 0.01775931955800422, 0.008617283775659838, 0.003400824362087738] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6564907759188373884_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-612838502181835934_i": {
            "samples": [0.0032569606163357326, 0.007758973075218879, 0.015538090084714526, 0.026157285804303654, 0.03701599030793991] + [0.04403395764329525] * 2 + [0.03701599030793991, 0.026157285804303654, 0.015538090084714526, 0.007758973075218879, 0.0032569606163357326] + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-612838502181835934_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1862115589237333143_i": {
            "samples": [0.00313911400558867, 0.0070819554546795276, 0.013780169102611909, 0.02312656637865019, 0.033475187796194086, 0.041791709925866324, 0.045, 0.041791709925866324, 0.033475187796194086, 0.02312656637865019, 0.013780169102611909, 0.0070819554546795276, 0.00313911400558867] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1862115589237333143_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1584921185821330929_i": {
            "samples": [0.0030408807189704077, 0.006536836325154028, 0.012369186349601106, 0.020602501279722643, 0.03020675427893248, 0.038984634909117126] + [0.044288214895822076] * 2 + [0.038984634909117126, 0.03020675427893248, 0.020602501279722643, 0.012369186349601106, 0.006536836325154028, 0.0030408807189704077] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1584921185821330929_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5392093092063954580_i": {
            "samples": [0.0029577837877438713, 0.006090087745647572, 0.01122084939497833, 0.018500053072823434, 0.027293879687068503, 0.03603318313125636, 0.04256817610080444, 0.045, 0.04256817610080444, 0.03603318313125636, 0.027293879687068503, 0.018500053072823434, 0.01122084939497833, 0.006090087745647572, 0.0029577837877438713, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5392093092063954580_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1087555805040272573_i": {
            "samples": [0.002886603231749668, 0.005718315154083024, 0.01027395147062127, 0.016741538367185362, 0.024742389790509828, 0.03316472159899549, 0.04031804794466557] + [0.04445402275413001] * 2 + [0.04031804794466557, 0.03316472159899549, 0.024742389790509828, 0.016741538367185362, 0.01027395147062127, 0.005718315154083024, 0.002886603231749668],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1087555805040272573_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1264809863722021647_i": {
            "samples": [0.0028249661996606213, 0.005404788539183576, 0.009483648111828325, 0.015261718144141496, 0.02252489106451083, 0.030489706454936944, 0.03785079975109237, 0.04309512555812251, 0.045, 0.04309512555812251, 0.03785079975109237, 0.030489706454936944, 0.02252489106451083, 0.015261718144141496, 0.009483648111828325, 0.005404788539183576, 0.0028249661996606213] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1264809863722021647_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3201589722435749314_i": {
            "samples": [0.002771086967490843, 0.0051372792004359125, 0.008816694774556523, 0.014007739812935151, 0.02060250127972264, 0.028051846679528352, 0.0353583985391161, 0.0412584910079413] + [0.0445680586213723] * 2 + [0.0412584910079413, 0.0353583985391161, 0.028051846679528352, 0.02060250127972264, 0.014007739812935151, 0.008816694774556523, 0.0051372792004359125, 0.002771086967490843] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3201589722435749314_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9209359323659574230_i": {
            "samples": [0.0027235967694566334, 0.004906672471959597, 0.00824813067227343, 0.01293743560534336, 0.018934989754037124, 0.025858668138996333, 0.032951215211532645, 0.03917968351030313, 0.043468496224329134, 0.045, 0.043468496224329134, 0.03917968351030313, 0.032951215211532645, 0.025858668138996333, 0.018934989754037124, 0.01293743560534336, 0.00824813067227343, 0.004906672471959597, 0.0027235967694566334, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9209359323659574230_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5402187417416950579_i": {
            "samples": [0.002681429344289374, 0.004706055058005065, 0.007758973075218877, 0.01201733258518545, 0.017485115738056386, 0.023899319596590533, 0.030687333803565666, 0.03701599030793991, 0.04194461215617874] + [0.044649807221710955] * 2 + [0.04194461215617874, 0.03701599030793991, 0.030687333803565666, 0.023899319596590533, 0.017485115738056386, 0.01201733258518545, 0.007758973075218877, 0.004706055058005065, 0.002681429344289374],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5402187417416950579_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-879869647326947263_i": {
            "samples": [0.0026437420840333746, 0.004530100489780402, 0.0073346048100830456, 0.01122084939497833, 0.016220150486901945, 0.022154612403294235, 0.02859259449459615, 0.03486768429974622, 0.040176562570300486, 0.043742397162897365, 0.045, 0.043742397162897365, 0.040176562570300486, 0.03486768429974622, 0.02859259449459615, 0.022154612403294235, 0.016220150486901945, 0.01122084939497833, 0.0073346048100830456, 0.004530100489780402, 0.0026437420840333746] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-879869647326947263_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-658375588128232015_i": {
            "samples": [0.002609860540872115, 0.00437464648410137, 0.006963635959888166, 0.01052680526488461, 0.015112090735730868, 0.020602501279722643, 0.02667367042822907, 0.03279540856535964, 0.03829223754247891, 0.04245959787865623] + [0.044710388440118876] * 2 + [0.04245959787865623, 0.03829223754247891, 0.03279540856535964, 0.02667367042822907, 0.020602501279722643, 0.015112090735730868, 0.01052680526488461, 0.006963635959888166, 0.00437464648410137, 0.002609860540872115] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-658375588128232015_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1778389818629643021_i": {
            "samples": [0.002579238622452966, 0.0042363986336785495, 0.0066370914436332945, 0.009918236716819908, 0.014137311375621348, 0.019220950654690473, 0.02492634433738389, 0.030833157592210256, 0.03637919638388446, 0.04094151280701048, 0.04394913753524951, 0.045, 0.04394913753524951, 0.04094151280701048, 0.03637919638388446, 0.030833157592210256, 0.02492634433738389, 0.019220950654690473, 0.014137311375621348, 0.009918236716819908, 0.0066370914436332945, 0.0042363986336785495, 0.002579238622452966, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1778389818629643021_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4130755487391937241_i": {
            "samples": [0.002551429548171046, 0.004112718991022128, 0.00634782441601157, 0.009381476336160566, 0.01327601952784993, 0.017989330087402715, 0.02334062666460994, 0.02899749261713379, 0.03449521007116611, 0.03929230936293479, 0.042855515995282936] + [0.04475652045276505] * 2 + [0.042855515995282936, 0.03929230936293479, 0.03449521007116611, 0.02899749261713379, 0.02334062666460994, 0.017989330087402715, 0.01327601952784993, 0.009381476336160566, 0.00634782441601157, 0.004112718991022128, 0.002551429548171046],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4130755487391937241_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6648633529796064006_i": {
            "samples": [0.0025260643275360176, 0.0040014727856723855, 0.006090087745647572, 0.00890544145876266, 0.012511678520393735, 0.01688899944831298, 0.021903851518198725, 0.027293879687068503, 0.03267670666831609, 0.03758715951350724, 0.04154023558739861, 0.04410894029880399, 0.045, 0.04410894029880399, 0.04154023558739861, 0.03758715951350724, 0.03267670666831609, 0.027293879687068503, 0.021903851518198725, 0.01688899944831298, 0.012511678520393735, 0.00890544145876266, 0.006090087745647572, 0.0040014727856723855, 0.0025260643275360176] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6648633529796064006_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7275792773823484294_i": {
            "samples": [0.0025028355874354992, 0.0039009156449618773, 0.005859217370023295, 0.00848108614953415, 0.011830474202861593, 0.01590346086689613, 0.020602501279722643, 0.02572095375451038, 0.030945179119672497, 0.03587878657292559, 0.040088638425953435, 0.04316618612562091] + [0.044792454939364075] * 2 + [0.04316618612562091, 0.040088638425953435, 0.03587878657292559, 0.030945179119672497, 0.02572095375451038, 0.020602501279722643, 0.01590346086689613, 0.011830474202861593, 0.00848108614953415, 0.005859217370023295, 0.0039009156449618773, 0.0025028355874354992] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7275792773823484294_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1711501740190055130_i": {
            "samples": [0.0024814852626756563, 0.0038096094880138488, 0.005651395719435244, 0.008100978437746048, 0.011220849394978333, 0.015018290122123386, 0.019423243080843425, 0.024273337825693197, 0.029311885423359323, 0.03420302420732057, 0.03856486011458755, 0.04201704562427031, 0.04423497268175237, 0.045, 0.04423497268175237, 0.04201704562427031, 0.03856486011458755, 0.03420302420732057, 0.029311885423359323, 0.024273337825693197, 0.019423243080843425, 0.015018290122123386, 0.011220849394978333, 0.008100978437746048, 0.005651395719435244, 0.0038096094880138488, 0.0024814852626756563, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1711501740190055130_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3745815270996862857_i": {
            "samples": [0.0024617951167852383, 0.003726359018304561, 0.0054634730847848405, 0.007758973075218879, 0.010673110496635019, 0.014220965746182155, 0.018353483216057877, 0.022943476855747564, 0.027781218361001815, 0.032583270094514144, 0.03701599030793991, 0.040731968667614436, 0.04341429502287785] + [0.044820988381976366] * 2 + [0.04341429502287785, 0.040731968667614436, 0.03701599030793991, 0.032583270094514144, 0.027781218361001815, 0.022943476855747564, 0.018353483216057877, 0.014220965746182155, 0.010673110496635019, 0.007758973075218879, 0.0054634730847848405, 0.003726359018304561, 0.0024617951167852383],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3745815270996862857_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3524321211798147609_i": {
            "samples": [0.0024435793635176613, 0.0036501632161548623, 0.005292831373674129, 0.007449957059914865, 0.01017910090171241, 0.013500660222938617, 0.017381631298331857, 0.021722809694617814, 0.02635308117604699, 0.031033927425680702, 0.03547578536508673, 0.03936563263600119, 0.04240259052527128, 0.044336099473404764, 0.045, 0.044336099473404764, 0.04240259052527128, 0.03936563263600119, 0.03547578536508673, 0.031033927425680702, 0.02635308117604699, 0.021722809694617814, 0.017381631298331857, 0.013500660222938617, 0.01017910090171241, 0.007449957059914865, 0.005292831373674129, 0.0036501632161548623, 0.0024435793635176613] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3524321211798147609_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "155176731206446915_i": {
            "samples": [0.002426678866378028, 0.003580177892320246, 0.0051372792004359125, 0.007169650683264689, 0.009731932507344929, 0.012848027113724358, 0.01649719336831532, 0.02060250127972264, 0.02502453976979439, 0.02956300063421708, 0.03396778208950533, 0.03795964420789055, 0.0412584910079413, 0.043615495551435485] + [0.04484402095366661] * 2 + [0.043615495551435485, 0.0412584910079413, 0.03795964420789055, 0.03396778208950533, 0.02956300063421708, 0.02502453976979439, 0.02060250127972264, 0.01649719336831532, 0.012848027113724358, 0.009731932507344929, 0.007169650683264689, 0.0051372792004359125, 0.003580177892320246, 0.002426678866378028] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "155176731206446915_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1326561523794980746_i": {
            "samples": [0.0024109565367578835, 0.0035156864938290025, 0.004994970371269144, 0.006914451090177933, 0.009325766086476159, 0.012255000795126673, 0.015690767457769792, 0.019573885564962007, 0.023790957461622565, 0.028174019611510417, 0.03250781063827401, 0.036545057250441104, 0.040028709455768426, 0.04271855432848505, 0.04441846252714071, 0.045, 0.04441846252714071, 0.04271855432848505, 0.040028709455768426, 0.036545057250441104, 0.03250781063827401, 0.028174019611510417, 0.023790957461622565, 0.019573885564962007, 0.015690767457769792, 0.012255000795126673, 0.009325766086476159, 0.006914451090177933, 0.004994970371269144, 0.0035156864938290025, 0.0024109565367578835, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1326561523794980746_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1105067464596265498_i": {
            "samples": [0.0023962936518776646, 0.003456077133652085, 0.004864340004480777, 0.006681308535800779, 0.008955631989591218, 0.011714616017857806, 0.014953986494751055, 0.01862872011349104, 0.022646764226304746, 0.02686744738608851, 0.031105971004103065, 0.035144569347404675, 0.038749829545265374, 0.04169447159923057, 0.04378085710534654] + [0.0448628802330165] * 2 + [0.04378085710534654, 0.04169447159923057, 0.038749829545265374, 0.035144569347404675, 0.031105971004103065, 0.02686744738608851, 0.022646764226304746, 0.01862872011349104, 0.014953986494751055, 0.011714616017857806, 0.008955631989591218, 0.006681308535800779, 0.004864340004480777, 0.003456077133652085, 0.0023962936518776646],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1105067464596265498_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3906648293231783600_i": {
            "samples": [0.0023825868853451075, 0.0034008243620877393, 0.004744054065238999, 0.0064676279185557, 0.00861728377565984, 0.011220849394978333, 0.014279435607375697, 0.01775931955800422, 0.021585970145073075, 0.025641698701671392, 0.02976815950422186, 0.033774361377894954, 0.03745003934865391, 0.04058330213903772, 0.042980598125817636, 0.044486424232505616, 0.045, 0.044486424232505616, 0.042980598125817636, 0.04058330213903772, 0.03745003934865391, 0.033774361377894954, 0.02976815950422186, 0.025641698701671392, 0.021585970145073075, 0.01775931955800422, 0.014279435607375697, 0.011220849394978333, 0.00861728377565984, 0.0064676279185557, 0.004744054065238999, 0.0034008243620877393, 0.0023825868853451075] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3906648293231783600_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8526499735414866976_i": {
            "samples": [0.002369745894728846, 0.0033494745849758367, 0.0046329691928013806, 0.006271189960418482, 0.008307078573323065, 0.010768482304484909, 0.013660559820788764, 0.016958612410017813, 0.020602501279722643, 0.02449386971171626, 0.02849723182010489, 0.03244559669603551, 0.036150696913277686, 0.03941716641018121, 0.0420592908560809, 0.0439183797241986] + [0.0448785163526999] * 2 + [0.0439183797241986, 0.0420592908560809, 0.03941716641018121, 0.036150696913277686, 0.03244559669603551, 0.02849723182010489, 0.02449386971171626, 0.020602501279722643, 0.016958612410017813, 0.013660559820788764, 0.010768482304484909, 0.008307078573323065, 0.006271189960418482, 0.0046329691928013806, 0.0033494745849758367, 0.002369745894728846] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8526499735414866976_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6104407981234950463_i": {
            "samples": [0.002357691348142151, 0.0033016343115772305, 0.004530100489780399, 0.006090087745647572, 0.008021879081327156, 0.010352983454721408, 0.013091571317076667, 0.016220150486901945, 0.019690413196512112, 0.023420255445931595, 0.027293879687068503, 0.031165619589233893, 0.03486768429974622, 0.03822146174557406, 0.041051433457284535, 0.043200244857846494, 0.04454315115204302, 0.045, 0.04454315115204302, 0.043200244857846494, 0.041051433457284535, 0.03822146174557406, 0.03486768429974622, 0.031165619589233893, 0.027293879687068503, 0.023420255445931595, 0.019690413196512112, 0.016220150486901945, 0.013091571317076667, 0.010352983454721408, 0.008021879081327156, 0.006090087745647572, 0.004530100489780399, 0.0033016343115772305, 0.002357691348142151, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6104407981234950463_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6325902040433665711_i": {
            "samples": [0.002346353299521717, 0.0032569606163357313, 0.0044345955187797504, 0.005922675334206895, 0.007758973075218878, 0.00997040888541069, 0.012567361250607789, 0.015538090084714525, 0.01884402087812471, 0.022416712622672377, 0.02615728580430365, 0.029938899807673777, 0.03361254540686738, 0.03701599030793991, 0.03998524390179175, 0.04236747013441668, 0.04403395764329525] + [0.044891623769994185] * 2 + [0.04403395764329525, 0.04236747013441668, 0.03998524390179175, 0.03701599030793991, 0.03361254540686738, 0.029938899807673777, 0.02615728580430365, 0.022416712622672377, 0.01884402087812471, 0.015538090084714525, 0.012567361250607789, 0.00997040888541069, 0.007758973075218878, 0.005922675334206895, 0.0044345955187797504, 0.0032569606163357313, 0.002346353299521717],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6325902040433665711_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7598524263185882589_i": {
            "samples": [0.002335669842884592, 0.003215153346284126, 0.004345713174304989, 0.005767525922407299, 0.007516007086959697, 0.009617317104979359, 0.01208341858496279, 0.014907157287993888, 0.01805797205500425, 0.02147891051554825, 0.025085609068644998, 0.02876776885451699, 0.03239342286852773, 0.03581596273281828, 0.03888351771803405, 0.04144991033641262, 0.0433861159211894, 0.044590986286279576, 0.045, 0.044590986286279576, 0.0433861159211894, 0.04144991033641262, 0.03888351771803405, 0.03581596273281828, 0.03239342286852773, 0.02876776885451699, 0.025085609068644998, 0.02147891051554825, 0.01805797205500425, 0.014907157287993888, 0.01208341858496279, 0.009617317104979359, 0.007516007086959697, 0.005767525922407299, 0.004345713174304989, 0.003215153346284126, 0.002335669842884592] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7598524263185882589_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2489274833264753431_i": {
            "samples": [0.0023255859913126685, 0.003175948715009545, 0.004262806410670822, 0.005623397594830979, 0.007290931578012656, 0.009290697194004017, 0.011635756917750779, 0.014322605346206307, 0.017327282732784, 0.020602501279722643, 0.024076341173783655, 0.027652988889901368, 0.031215818050692484, 0.03463286447219627, 0.037764449415815096, 0.04047239942068012, 0.04263004575896565, 0.04413200882895417] + [0.044902719567521156] * 2 + [0.04413200882895417, 0.04263004575896565, 0.04047239942068012, 0.037764449415815096, 0.03463286447219627, 0.031215818050692484, 0.027652988889901368, 0.024076341173783655, 0.020602501279722643, 0.017327282732784, 0.014322605346206307, 0.011635756917750779, 0.009290697194004017, 0.007290931578012656, 0.005623397594830979, 0.004262806410670822, 0.003175948715009545, 0.0023255859913126685] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2489274833264753431_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4412678124829952482_i": {
            "samples": [0.0023160527381292616, 0.003139114005588671, 0.004185308040118834, 0.005489205145584141, 0.0070819554546795276, 0.008987907922313233, 0.011220849394978333, 0.013780169102611909, 0.016647347899696227, 0.019783232685447464, 0.023126566378650192, 0.026594188993507337, 0.030083200552476104, 0.033475187796194086, 0.0366423821808049, 0.039455365694803866, 0.041791709925866324, 0.04354476023446263, 0.044631693012253504, 0.045, 0.044631693012253504, 0.04354476023446263, 0.041791709925866324, 0.039455365694803866, 0.0366423821808049, 0.033475187796194086, 0.030083200552476104, 0.026594188993507337, 0.023126566378650192, 0.019783232685447464, 0.016647347899696227, 0.013780169102611909, 0.011220849394978333, 0.008987907922313233, 0.0070819554546795276, 0.005489205145584141, 0.004185308040118834, 0.003139114005588671, 0.0023160527381292616, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4412678124829952482_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-70021086062871320_i": {
            "samples": [0.002298467282013625, 0.003071753129323663, 0.004044598549210856, 0.005246934746939324, 0.006706208220111929, 0.008444803201727434, 0.010477150002685766, 0.012806720149016473, 0.015423175704628934, 0.018299988718455947, 0.021392865802783618, 0.024639292928737164, 0.027959451271045772, 0.031258646978771204, 0.034431253739310434, 0.03736600151243667, 0.039952277935397115, 0.042086963621413266, 0.04368122124228356, 0.04466661880713002, 0.045, 0.04466661880713002, 0.04368122124228356, 0.042086963621413266, 0.039952277935397115, 0.03736600151243667, 0.034431253739310434, 0.031258646978771204, 0.027959451271045772, 0.024639292928737164, 0.021392865802783618, 0.018299988718455947, 0.015423175704628934, 0.012806720149016473, 0.010477150002685766, 0.008444803201727434, 0.006706208220111929, 0.005246934746939324, 0.004044598549210856, 0.003071753129323663, 0.002298467282013625] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-70021086062871320_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "53939301042763868_i": {
            "samples": [0.002290340443109101, 0.003040880718970406, 0.003980556207121157, 0.0051372792004359125, 0.006536836325154025, 0.008200627499825764, 0.010143120675347301, 0.012369186349601104, 0.014871531844695524, 0.017628498018846427, 0.02060250127972264, 0.023739393607378083, 0.026968967851849397, 0.03020675427893248, 0.033357141928063716, 0.03631772498912383, 0.038984634909117126, 0.0412584910079413, 0.04305050412463992, 0.044288214895822076] + [0.04492035118368515] * 2 + [0.044288214895822076, 0.04305050412463992, 0.0412584910079413, 0.038984634909117126, 0.03631772498912383, 0.033357141928063716, 0.03020675427893248, 0.026968967851849397, 0.023739393607378083, 0.02060250127972264, 0.017628498018846427, 0.014871531844695524, 0.012369186349601104, 0.010143120675347301, 0.008200627499825764, 0.006536836325154025, 0.0051372792004359125, 0.003980556207121157, 0.003040880718970406, 0.002290340443109101] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "53939301042763868_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8259468590269755647_i": {
            "samples": [0.002282613878441956, 0.0030116800421040894, 0.00392024482363332, 0.005034374636005118, 0.006378313375728078, 0.007972493186884571, 0.009831288533885395, 0.01196064799578202, 0.014355785406816845, 0.01699914928966451, 0.01985890963969827, 0.022888197540850325, 0.026025301412808174, 0.029194962686577716, 0.03231082615520607, 0.03527899317411319, 0.038002510143230084, 0.04038651383377471, 0.0423436636171159, 0.04379943184129589, 0.04469680751117565, 0.045, 0.04469680751117565, 0.04379943184129589, 0.0423436636171159, 0.04038651383377471, 0.038002510143230084, 0.03527899317411319, 0.03231082615520607, 0.029194962686577716, 0.026025301412808174, 0.022888197540850325, 0.01985890963969827, 0.01699914928966451, 0.014355785406816845, 0.01196064799578202, 0.009831288533885395, 0.007972493186884571, 0.006378313375728078, 0.005034374636005118, 0.00392024482363332, 0.0030116800421040894, 0.002282613878441956, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8259468590269755647_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4622984449806366805_i": {
            "samples": [0.0022752587709870802, 0.0029840202764447096, 0.0038633548579549335, 0.0049376384969694, 0.00622968142826453, 0.007758973075218878, 0.009539695436145574, 0.011578615519847506, 0.01387300729711731, 0.016408786144965208, 0.019159058061268403, 0.0220832866923284, 0.025127259572151332, 0.028223989387651714, 0.031295618037513455, 0.034256305533367615, 0.03701599030793991, 0.03948481254632568, 0.04157790922741945, 0.043220229774447644, 0.044350993672068774] + [0.04492742171182011] * 2 + [0.044350993672068774, 0.043220229774447644, 0.04157790922741945, 0.03948481254632568, 0.03701599030793991, 0.034256305533367615, 0.031295618037513455, 0.028223989387651714, 0.025127259572151332, 0.0220832866923284, 0.019159058061268403, 0.016408786144965208, 0.01387300729711731, 0.011578615519847506, 0.009539695436145574, 0.007758973075218878, 0.00622968142826453, 0.0049376384969694, 0.0038633548579549335, 0.0029840202764447096, 0.0022752587709870802],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4622984449806366805_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "314919130332203064_i": {
            "samples": [0.002268249001323914, 0.0029577837877438713, 0.0038096094880138488, 0.0048465515335514445, 0.006090087745647572, 0.007558795654089012, 0.009266591089538943, 0.01122084939497833, 0.01342053432816397, 0.01585448797479736, 0.018500053072823434, 0.02132220268779138, 0.024273337825693197, 0.027293879687068503, 0.030313730490512704, 0.03325460833261389, 0.03603318313125636, 0.03856486011458755, 0.040767983599927934, 0.04256817610080444, 0.04390249410291806, 0.044723077799689856, 0.045, 0.044723077799689856, 0.04390249410291806, 0.04256817610080444, 0.040767983599927934, 0.03856486011458755, 0.03603318313125636, 0.03325460833261389, 0.030313730490512704, 0.027293879687068503, 0.024273337825693197, 0.02132220268779138, 0.018500053072823434, 0.01585448797479736, 0.01342053432816397, 0.01122084939497833, 0.009266591089538943, 0.007558795654089012, 0.006090087745647572, 0.0048465515335514445, 0.0038096094880138488, 0.0029577837877438713, 0.002268249001323914] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "314919130332203064_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2037446538430091156_i": {
            "samples": [0.0022615608395822576, 0.002932864520601318, 0.003758760460735895, 0.004760649623148641, 0.005958771201714929, 0.007370825381837093, 0.00901040800045584, 0.01088533282269449, 0.012995945737972792, 0.015333559684314104, 0.01787915576936509, 0.020602501279722643, 0.023461826182497255, 0.026404174709919723, 0.029366507779970033, 0.03227757743901369, 0.03506053033367666, 0.03763612929881027, 0.03992641754448022, 0.04185859607443986, 0.04336884873340308, 0.04440583598342185] + [0.04493359111031693] * 2 + [0.04440583598342185, 0.04336884873340308, 0.04185859607443986, 0.03992641754448022, 0.03763612929881027, 0.03506053033367666, 0.03227757743901369, 0.029366507779970033, 0.026404174709919723, 0.023461826182497255, 0.020602501279722643, 0.01787915576936509, 0.015333559684314104, 0.012995945737972792, 0.01088533282269449, 0.00901040800045584, 0.007370825381837093, 0.005958771201714929, 0.004760649623148641, 0.003758760460735895, 0.002932864520601318, 0.0022615608395822576] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2037446538430091156_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5009766010630318589_i": {
            "samples": [0.0022551726786126905, 0.0029091666178561433, 0.003710584550668933, 0.004679516802908711, 0.005835050681741723, 0.007194045770117959, 0.008769739701211816, 0.010570247395266656, 0.012597041018014099, 0.014843519161489465, 0.017293788920022278, 0.019921790688190392, 0.022690890195482847, 0.0255540439911971, 0.028454613075855284, 0.03132785596158564, 0.03410308006849492, 0.036706373427339595, 0.039063782647928855, 0.04110475402306036, 0.042765618258428395, 0.04399288047528688, 0.04474607899637652, 0.045, 0.04474607899637652, 0.04399288047528688, 0.042765618258428395, 0.04110475402306036, 0.039063782647928855, 0.036706373427339595, 0.03410308006849492, 0.03132785596158564, 0.028454613075855284, 0.0255540439911971, 0.022690890195482847, 0.019921790688190392, 0.017293788920022278, 0.014843519161489465, 0.012597041018014099, 0.010570247395266656, 0.008769739701211816, 0.007194045770117959, 0.005835050681741723, 0.004679516802908711, 0.003710584550668933, 0.0029091666178561433, 0.0022551726786126905, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5009766010630318589_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4238044233411292421_i": {
            "samples": [0.0022490648020923256, 0.002886603231749669, 0.0036648805264638787, 0.004602779313517965, 0.005718315154083024, 0.0070275448297335615, 0.008543321810579173, 0.010273951470621273, 0.012221819276561888, 0.014382083582930012, 0.016741538367185362, 0.019277757810779724, 0.02195863200027421, 0.024742389790509828, 0.027578180623949435, 0.030407252619400714, 0.03316472159899549, 0.035781878196983995, 0.03818893203389997, 0.04031804794466557, 0.04210649424101218, 0.04349970122287654, 0.04445402275413001] + [0.044939006217156886] * 2 + [0.04445402275413001, 0.04349970122287654, 0.04210649424101218, 0.04031804794466557, 0.03818893203389997, 0.035781878196983995, 0.03316472159899549, 0.030407252619400714, 0.027578180623949435, 0.024742389790509828, 0.02195863200027421, 0.019277757810779724, 0.016741538367185362, 0.014382083582930012, 0.012221819276561888, 0.010273951470621273, 0.008543321810579173, 0.0070275448297335615, 0.005718315154083024, 0.004602779313517965, 0.0036648805264638787, 0.002886603231749669, 0.0022490648020923256],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4238044233411292421_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2812006322627151726_i": {
            "samples": [0.002243219182348703, 0.00286509549664543, 0.0036214665430845685, 0.004530100489780403, 0.005608015145664268, 0.006870502518018646, 0.008330015541669001, 0.009994960993703648, 0.011868460228350485, 0.013947155318533784, 0.01622015048690195, 0.018668185356823963, 0.021263135798531962, 0.023967928732267805, 0.02673693866631924, 0.029516906409324264, 0.032248385742071686, 0.03486768429974622, 0.03730922377347726, 0.03950820561072078, 0.04140343565391694, 0.04294013828570386, 0.04407258057339122, 0.044766331401892075, 0.045, 0.044766331401892075, 0.04407258057339122, 0.04294013828570386, 0.04140343565391694, 0.03950820561072078, 0.03730922377347726, 0.03486768429974622, 0.032248385742071686, 0.029516906409324264, 0.02673693866631924, 0.023967928732267805, 0.021263135798531962, 0.018668185356823963, 0.01622015048690195, 0.013947155318533784, 0.011868460228350485, 0.009994960993703648, 0.008330015541669001, 0.006870502518018646, 0.005608015145664268, 0.004530100489780403, 0.0036214665430845685, 0.00286509549664543, 0.002243219182348703] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2812006322627151726_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5393522966599840053_i": {
            "samples": [0.002237619303555732, 0.0028445716383879984, 0.003580177892320246, 0.004461176362983632, 0.005503655400610527, 0.00672217988626881, 0.00812879332285023, 0.009731932507344929, 0.011535306813678311, 0.013536807946077398, 0.01572752700898904, 0.01809096223925947, 0.02060250127972264, 0.023229255327547334, 0.025930308315230993, 0.028657422646728443, 0.031356214897321565, 0.03396778208950533, 0.03643072419005491, 0.0386834743621144, 0.04066681850429382, 0.042326462851395394, 0.043615495551435485, 0.044496587007505486] + [0.044943785141606137] * 2 + [0.044496587007505486, 0.043615495551435485, 0.042326462851395394, 0.04066681850429382, 0.0386834743621144, 0.03643072419005491, 0.03396778208950533, 0.031356214897321565, 0.028657422646728443, 0.025930308315230993, 0.023229255327547334, 0.02060250127972264, 0.01809096223925947, 0.01572752700898904, 0.013536807946077398, 0.011535306813678311, 0.009731932507344929, 0.00812879332285023, 0.00672217988626881, 0.005503655400610527, 0.004461176362983632, 0.003580177892320246, 0.0028445716383879984, 0.002237619303555732] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5393522966599840053_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5615017025798555301_i": {
            "samples": [0.0022322500066664524, 0.0028249661996606213, 0.0035408650560035527, 0.004395731863752645, 0.005404788539183576, 0.0065819096743409905, 0.007938726243331798, 0.009483648111828325, 0.011220849394978333, 0.013149272708892313, 0.015261718144141496, 0.017544089001665954, 0.019974867725426344, 0.02252489106451083, 0.02515748274940722, 0.027828984880678528, 0.030489706454936944, 0.03308528030756846, 0.03555839015421074, 0.03785079975109237, 0.039905589113387624, 0.0416694808715781, 0.04309512555812251, 0.04414320968250296, 0.04478425585579964, 0.045, 0.04478425585579964, 0.04414320968250296, 0.04309512555812251, 0.0416694808715781, 0.039905589113387624, 0.03785079975109237, 0.03555839015421074, 0.03308528030756846, 0.030489706454936944, 0.027828984880678528, 0.02515748274940722, 0.02252489106451083, 0.019974867725426344, 0.017544089001665954, 0.015261718144141496, 0.013149272708892313, 0.011220849394978333, 0.009483648111828325, 0.007938726243331798, 0.0065819096743409905, 0.005404788539183576, 0.004395731863752645, 0.0035408650560035527, 0.0028249661996606213, 0.0022322500066664524, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5615017025798555301_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3192925271618638788_i": {
            "samples": [0.0022270973530301706, 0.002806219364174241, 0.003503392015899386, 0.0043335175332762516, 0.005311009565081267, 0.006449088139978684, 0.007758973075218878, 0.009249002151979598, 0.010923711446082687, 0.012782925623788405, 0.014820914704026435, 0.017025679631132086, 0.01937843094622511, 0.021853322038281, 0.024417490369076637, 0.027031446604730405, 0.029649833165918307, 0.032222551282821706, 0.0346962306710861, 0.03701599030793991, 0.03912741462266989, 0.04097864892771672, 0.04252250315163484, 0.043718445554516816, 0.044534369188016384] + [0.044948023753154064] * 2 + [0.044534369188016384, 0.043718445554516816, 0.04252250315163484, 0.04097864892771672, 0.03912741462266989, 0.03701599030793991, 0.0346962306710861, 0.032222551282821706, 0.029649833165918307, 0.027031446604730405, 0.024417490369076637, 0.021853322038281, 0.01937843094622511, 0.017025679631132086, 0.014820914704026435, 0.012782925623788405, 0.010923711446082687, 0.009249002151979598, 0.007758973075218878, 0.006449088139978684, 0.005311009565081267, 0.0043335175332762516, 0.003503392015899386, 0.002806219364174241, 0.0022270973530301706],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3192925271618638788_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7812776713801722164_i": {
            "samples": [0.0022221485041214635, 0.0027882763653518834, 0.003467634781995055, 0.0042743066663799584, 0.005221951094417901, 0.006323167944034364, 0.007588770658725412, 0.009026989431452753, 0.01064263663170876, 0.012436275357891683, 0.014403439706323315, 0.01653396078013889, 0.018811454732179145, 0.021213027506237683, 0.023709244916873748, 0.0262644061328905, 0.02883714375131922, 0.03138135515132871, 0.03384744880835653, 0.03618386719741171, 0.038338826543671004, 0.04026219481588473, 0.04190741476215459, 0.043233369965617566, 0.04420608993687952, 0.044800195693516454, 0.045, 0.044800195693516454, 0.04420608993687952, 0.043233369965617566, 0.04190741476215459, 0.04026219481588473, 0.038338826543671004, 0.03618386719741171, 0.03384744880835653, 0.03138135515132871, 0.02883714375131922, 0.0262644061328905, 0.023709244916873748, 0.021213027506237683, 0.018811454732179145, 0.01653396078013889, 0.014403439706323315, 0.012436275357891683, 0.01064263663170876, 0.009026989431452753, 0.007588770658725412, 0.006323167944034364, 0.005221951094417901, 0.0042743066663799584, 0.003467634781995055, 0.0027882763653518834, 0.0022221485041214635] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7812776713801722164_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2266597513640485263_i": {
            "samples": [0.002217391615205061, 0.0027710869674908442, 0.0034334801072547667, 0.004217892822637325, 0.005137279200435915, 0.00620365194075587, 0.00742742546731715, 0.008816694774556525, 0.010376477167048592, 0.012107951931622883, 0.014007739812935151, 0.016067269169839395, 0.018272278128532837, 0.020602501279722643, 0.02303158503848993, 0.025527267506754027, 0.028051846679528352, 0.030562945600649025, 0.03301456543598165, 0.0353583985391161, 0.037545354818060456, 0.03952723757770026, 0.0412584910079413, 0.04269793195211086, 0.04381037456878093, 0.0445680586213723] + [0.04495180052302276] * 2 + [0.0445680586213723, 0.04381037456878093, 0.04269793195211086, 0.0412584910079413, 0.03952723757770026, 0.037545354818060456, 0.0353583985391161, 0.03301456543598165, 0.030562945600649025, 0.028051846679528352, 0.025527267506754027, 0.02303158503848993, 0.020602501279722643, 0.018272278128532837, 0.016067269169839395, 0.014007739812935151, 0.012107951931622883, 0.010376477167048592, 0.008816694774556525, 0.00742742546731715, 0.00620365194075587, 0.005137279200435915, 0.004217892822637325, 0.0034334801072547667, 0.0027710869674908442, 0.002217391615205061] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2266597513640485263_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5400757542881065106_i": {
            "samples": [0.002212815741090006, 0.0027546050092919216, 0.003400824362087736, 0.00416408765212899, 0.005056689785065528, 0.006090087745647572, 0.007274306195427147, 0.008617283775659837, 0.010124183346261053, 0.011796696263059339, 0.013632376843449557, 0.015624047755243337, 0.017759319558004215, 0.020020267479223943, 0.022383305310115148, 0.024819289852372393, 0.027293879687068503, 0.029768159504221858, 0.032199526451551545, 0.034542818825439844, 0.03675165104070378, 0.038779903413772035, 0.04058330213903772, 0.04212101510529366, 0.04335718385920805, 0.04426231173926075, 0.04481443325319743, 0.045, 0.04481443325319743, 0.04426231173926075, 0.04335718385920805, 0.04212101510529366, 0.04058330213903772, 0.038779903413772035, 0.03675165104070378, 0.034542818825439844, 0.032199526451551545, 0.029768159504221858, 0.027293879687068503, 0.024819289852372393, 0.022383305310115148, 0.020020267479223943, 0.017759319558004215, 0.015624047755243337, 0.013632376843449557, 0.011796696263059339, 0.010124183346261053, 0.008617283775659837, 0.007274306195427147, 0.006090087745647572, 0.005056689785065528, 0.00416408765212899, 0.003400824362087736, 0.0027546050092919216, 0.002212815741090006, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5400757542881065106_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7038216929604661594_i": {
            "samples": [0.0022084107524006375, 0.0027387880012189475, 0.0033695725460432756, 0.004112718991022128, 0.004979905402541571, 0.005982062972914511, 0.007128837233564075, 0.008427994594487299, 0.009884794131735198, 0.011501350540878646, 0.01327601952784993, 0.015202841086232495, 0.017271078583235244, 0.01946489187090932, 0.021763180388161444, 0.024139627215236197, 0.026562967279791676, 0.02899749261713379, 0.03140379522113198, 0.033739734277870206, 0.03596160033132889, 0.038025435198323014, 0.03988845428739891, 0.04151050840112763, 0.042855515995282936, 0.043892794889926215, 0.044598224938458914] + [0.04495518017940069] * 2 + [0.044598224938458914, 0.043892794889926215, 0.042855515995282936, 0.04151050840112763, 0.03988845428739891, 0.038025435198323014, 0.03596160033132889, 0.033739734277870206, 0.03140379522113198, 0.02899749261713379, 0.026562967279791676, 0.024139627215236197, 0.021763180388161444, 0.01946489187090932, 0.017271078583235244, 0.015202841086232495, 0.01327601952784993, 0.011501350540878646, 0.009884794131735198, 0.008427994594487299, 0.007128837233564075, 0.005982062972914511, 0.004979905402541571, 0.004112718991022128, 0.0033695725460432756, 0.0027387880012189475, 0.0022084107524006375],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7038216929604661594_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3202997854877898243_i": {
            "samples": [0.0022041672610212623, 0.0027235967694566334, 0.003339637417765964, 0.004063629189209328, 0.004906672471959597, 0.005879201050812177, 0.0069904929146177245, 0.00824813067227343, 0.00965742870156196, 0.01122084939497833, 0.01293743560534336, 0.014802290186514024, 0.016806135924491428, 0.018934989754037124, 0.021169983629724904, 0.023487360566243804, 0.025858668138996333, 0.028251163287007264, 0.030628431927808918, 0.032951215211532645, 0.035178421908103295, 0.03726829425836711, 0.03917968351030313, 0.04087338217883925, 0.04231345359995032, 0.043468496224329134, 0.04431278071652505, 0.04482720242454831, 0.045, 0.04482720242454831, 0.04431278071652505, 0.043468496224329134, 0.04231345359995032, 0.04087338217883925, 0.03917968351030313, 0.03726829425836711, 0.035178421908103295, 0.032951215211532645, 0.030628431927808918, 0.028251163287007264, 0.025858668138996333, 0.023487360566243804, 0.021169983629724904, 0.018934989754037124, 0.016806135924491428, 0.014802290186514024, 0.01293743560534336, 0.01122084939497833, 0.00965742870156196, 0.00824813067227343, 0.0069904929146177245, 0.005879201050812177, 0.004906672471959597, 0.004063629189209328, 0.003339637417765964, 0.0027235967694566334, 0.0022041672610212623] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3202997854877898243_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2981503795679182995_i": {
            "samples": [0.0022000765535638445, 0.0027089951403200833, 0.003310938727159947, 0.004016673638096744, 0.004836758825351658, 0.005781157536901707, 0.006858792431400477, 0.00807705425873921, 0.009441278859598588, 0.010954211822799577, 0.012615484334646553, 0.014421127187472583, 0.01636315220799365, 0.018429231169743602, 0.020602501279722647, 0.022861523385990394, 0.025180414076097682, 0.027529165912161934, 0.029874161425676646, 0.03217887658333588, 0.03440475878802271, 0.03651225376285231, 0.03846194561401491, 0.04021576572467536, 0.0417382195917189, 0.04299757686225765, 0.04396696907260694, 0.04462534214256114] + [0.0449582164972744] * 2 + [0.04462534214256114, 0.04396696907260694, 0.04299757686225765, 0.0417382195917189, 0.04021576572467536, 0.03846194561401491, 0.03651225376285231, 0.03440475878802271, 0.03217887658333588, 0.029874161425676646, 0.027529165912161934, 0.025180414076097682, 0.022861523385990394, 0.020602501279722647, 0.018429231169743602, 0.01636315220799365, 0.014421127187472583, 0.012615484334646553, 0.010954211822799577, 0.009441278859598588, 0.00807705425873921, 0.006858792431400477, 0.005781157536901707, 0.004836758825351658, 0.004016673638096744, 0.003310938727159947, 0.0027089951403200833, 0.0022000765535638445] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2981503795679182995_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2873031789234274895_i": {
            "samples": [0.002196130531869861, 0.00269494965987533, 0.0032834025361357256, 0.003971719471492274, 0.00476995154594304, 0.005687616866699139, 0.006733295339340903, 0.007914180653231268, 0.009235602220084849, 0.010700533823254657, 0.012309109451161164, 0.014058169889185347, 0.01594086581103374, 0.017946344042468355, 0.020059543113723828, 0.022261121993637233, 0.024527541931425485, 0.026831315665573872, 0.029141431071326555, 0.03142394792159734, 0.03364275726798451, 0.035760483547890354, 0.03773950049698226, 0.039543023924107475, 0.04113623799411029, 0.04248740739295065, 0.04356892602588164, 0.04435825396678133, 0.04483869828757789, 0.045, 0.04483869828757789, 0.04435825396678133, 0.04356892602588164, 0.04248740739295065, 0.04113623799411029, 0.039543023924107475, 0.03773950049698226, 0.035760483547890354, 0.03364275726798451, 0.03142394792159734, 0.029141431071326555, 0.026831315665573872, 0.024527541931425485, 0.022261121993637233, 0.020059543113723828, 0.017946344042468355, 0.01594086581103374, 0.014058169889185347, 0.012309109451161164, 0.010700533823254657, 0.009235602220084849, 0.007914180653231268, 0.006733295339340903, 0.005687616866699139, 0.00476995154594304, 0.003971719471492274, 0.0032834025361357256, 0.00269494965987533, 0.002196130531869861, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2873031789234274895_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-783744107676016132_i": {
            "samples": [0.0021923216596943657, 0.002681429344289374, 0.0032569606163357313, 0.003928644416596959, 0.004706055058005065, 0.005598289478878552, 0.006613597570109367, 0.007758973075218877, 0.009039716086480309, 0.010458981687450198, 0.01201733258518545, 0.013712316371840982, 0.015538090084714525, 0.017485115738056386, 0.019539950256436477, 0.02168515158433456, 0.023899319596590533, 0.02615728580430365, 0.028430459865181792, 0.030687333803565666, 0.03289413696746988, 0.035015626532756805, 0.03701599030793991, 0.03885983122874933, 0.04051319678373799, 0.04194461215617874, 0.04312607348933794, 0.04403395764329525, 0.044649807221710955] + [0.0449609544493054] * 2 + [0.044649807221710955, 0.04403395764329525, 0.04312607348933794, 0.04194461215617874, 0.04051319678373799, 0.03885983122874933, 0.03701599030793991, 0.035015626532756805, 0.03289413696746988, 0.030687333803565666, 0.028430459865181792, 0.02615728580430365, 0.023899319596590533, 0.02168515158433456, 0.019539950256436477, 0.017485115738056386, 0.015538090084714525, 0.013712316371840982, 0.01201733258518545, 0.010458981687450198, 0.009039716086480309, 0.007758973075218877, 0.006613597570109367, 0.005598289478878552, 0.004706055058005065, 0.003928644416596959, 0.0032569606163357313, 0.002681429344289374, 0.0021923216596943657],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-783744107676016132_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5070791477237441758_i": {
            "samples": [0.0021886429148360656, 0.0026684054570661002, 0.003231549913927979, 0.003887335775491176, 0.004644889435378892, 0.0055129092683462695, 0.006499327892100825, 0.007610938089798383, 0.00885299195172299, 0.010228785895018255, 0.011739247140411496, 0.01338253974378367, 0.015153710168604475, 0.01704439342104495, 0.01904260075800304, 0.021132608770249143, 0.023294967153449017, 0.025506638703374357, 0.027741280092557885, 0.029969665982641225, 0.03216025226948306, 0.03427986709655573, 0.03629451111718945, 0.038170241784092104, 0.0398741106459297, 0.041375118156849744, 0.042645147713701946, 0.043659839791339576, 0.04439936829374993, 0.04484908458732194, 0.045, 0.04484908458732194, 0.04439936829374993, 0.043659839791339576, 0.042645147713701946, 0.041375118156849744, 0.0398741106459297, 0.038170241784092104, 0.03629451111718945, 0.03427986709655573, 0.03216025226948306, 0.029969665982641225, 0.027741280092557885, 0.025506638703374357, 0.023294967153449017, 0.021132608770249143, 0.01904260075800304, 0.01704439342104495, 0.015153710168604475, 0.01338253974378367, 0.011739247140411496, 0.010228785895018255, 0.00885299195172299, 0.007610938089798383, 0.006499327892100825, 0.0055129092683462695, 0.004644889435378892, 0.003887335775491176, 0.003231549913927979, 0.0026684054570661002, 0.0021886429148360656] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5070791477237441758_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4449465709350748214_i": {
            "samples": [0.002185087746075712, 0.002655851309862345, 0.003207112072979275, 0.0038476895203500205, 0.00458628890050234, 0.005431231325399248, 0.006390144762382165, 0.007469621523042266, 0.008674850554271462, 0.01000923556603093, 0.011474012621772363, 0.013067883084571026, 0.014786679559752713, 0.016623083512700733, 0.01856641339812717, 0.020602501279722643, 0.022713673963176244, 0.024878851591730918, 0.027073772516205467, 0.02927134818388462, 0.031442146003505825, 0.033554991917466456, 0.035577678084197664, 0.0374777550166612, 0.039223382122376235, 0.04078420621619092, 0.04213223455563385, 0.04324266753656638, 0.04409465654787863, 0.04467195467294955] + [0.044963431879664346] * 2 + [0.04467195467294955, 0.04409465654787863, 0.04324266753656638, 0.04213223455563385, 0.04078420621619092, 0.039223382122376235, 0.0374777550166612, 0.035577678084197664, 0.033554991917466456, 0.031442146003505825, 0.02927134818388462, 0.027073772516205467, 0.024878851591730918, 0.022713673963176244, 0.020602501279722643, 0.01856641339812717, 0.016623083512700733, 0.014786679559752713, 0.013067883084571026, 0.011474012621772363, 0.01000923556603093, 0.008674850554271462, 0.007469621523042266, 0.006390144762382165, 0.005431231325399248, 0.00458628890050234, 0.0038476895203500205, 0.003207112072979275, 0.002655851309862345, 0.002185087746075712] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4449465709350748214_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4670959768549463462_i": {
            "samples": [0.002181650034369001, 0.002643742084033377, 0.003183593010117178, 0.0038096094880138505, 0.004530100489780403, 0.0053530299250222225, 0.006285733522147417, 0.007334604810083049, 0.008504757430977157, 0.009799673420622566, 0.011220849394978335, 0.012767454620626752, 0.01443601655818671, 0.01622015048690195, 0.018110350096950997, 0.0200938553525385, 0.02215461240329424, 0.024273337825693204, 0.026427696042506662, 0.028592594494596158, 0.030740596189361813, 0.03284244384848766, 0.03486768429974622, 0.036785376314758506, 0.03856486011458755, 0.040176562570300486, 0.04159280900995399, 0.0427886107493784, 0.043742397162897365, 0.04443666238597582, 0.044858499582217694, 0.045, 0.044858499582217694, 0.04443666238597582, 0.043742397162897365, 0.0427886107493784, 0.04159280900995399, 0.040176562570300486, 0.03856486011458755, 0.036785376314758506, 0.03486768429974622, 0.03284244384848766, 0.030740596189361813, 0.028592594494596158, 0.026427696042506662, 0.024273337825693204, 0.02215461240329424, 0.0200938553525385, 0.018110350096950997, 0.01622015048690195, 0.01443601655818671, 0.012767454620626752, 0.011220849394978335, 0.009799673420622566, 0.008504757430977157, 0.007334604810083049, 0.006285733522147417, 0.0053530299250222225, 0.004530100489780403, 0.0038096094880138505, 0.003183593010117178, 0.002643742084033377, 0.002181650034369001, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4670959768549463462_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3522891337262262136_i": {
            "samples": [0.0021783240578117802, 0.0026320546704428397, 0.0031609425342021065, 0.0037730066615581682, 0.0044761828645273165, 0.005278096735337163, 0.006185803894099255, 0.007205501725868167, 0.00834221891399041, 0.009599491201180295, 0.010979033855880314, 0.012480423155625142, 0.014100800679714075, 0.015834615189656717, 0.01767341723767234, 0.01960572127284428, 0.02161694883567558, 0.023689464411198798, 0.02580271266467483, 0.027933462183037508, 0.030056156616078404, 0.03214336943314592, 0.03416635360856382, 0.03609567268084811, 0.03790189507499922, 0.03955632961299501, 0.04103177702677753, 0.042303270255439764, 0.04334877552461066, 0.0441498267730566, 0.04469206793220909] + [0.04496568081800304] * 2 + [0.04469206793220909, 0.0441498267730566, 0.04334877552461066, 0.042303270255439764, 0.04103177702677753, 0.03955632961299501, 0.03790189507499922, 0.03609567268084811, 0.03416635360856382, 0.03214336943314592, 0.030056156616078404, 0.027933462183037508, 0.02580271266467483, 0.023689464411198798, 0.02161694883567558, 0.01960572127284428, 0.01767341723767234, 0.015834615189656717, 0.014100800679714075, 0.012480423155625142, 0.010979033855880314, 0.009599491201180295, 0.00834221891399041, 0.007205501725868167, 0.006185803894099255, 0.005278096735337163, 0.0044761828645273165, 0.0037730066615581682, 0.0031609425342021065, 0.0026320546704428397, 0.0021783240578117802],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3522891337262262136_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6868719456552630325_i": {
            "samples": [0.0021751044599569004, 0.002620767525400632, 0.00313911400558867, 0.0037377985282149332, 0.004424405249577707, 0.005206239218437463, 0.006090087745647572, 0.007081955454679527, 0.00818677852451955, 0.009408125515012428, 0.01074789398542346, 0.01220601376639065, 0.013780169102611905, 0.015465552827263584, 0.01725466614595881, 0.01913717740164616, 0.021099852291742723, 0.02312656637865019, 0.02519840837916, 0.027293879687068503, 0.029389191973642894, 0.03145866066493294, 0.033475187796194086, 0.03541082340652936, 0.03723739049602661, 0.03892715486391898, 0.04045351811076749, 0.041791709925866324, 0.04291945465770895, 0.04381758719122487, 0.04447059437758889, 0.044867060658126935, 0.045, 0.044867060658126935, 0.04447059437758889, 0.04381758719122487, 0.04291945465770895, 0.041791709925866324, 0.04045351811076749, 0.03892715486391898, 0.03723739049602661, 0.03541082340652936, 0.033475187796194086, 0.03145866066493294, 0.029389191973642894, 0.027293879687068503, 0.02519840837916, 0.02312656637865019, 0.021099852291742723, 0.01913717740164616, 0.01725466614595881, 0.015465552827263584, 0.013780169102611905, 0.01220601376639065, 0.01074789398542346, 0.009408125515012428, 0.00818677852451955, 0.007081955454679527, 0.006090087745647572, 0.005206239218437463, 0.004424405249577707, 0.0037377985282149332, 0.00313911400558867, 0.002620767525400632, 0.0021751044599569004] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6868719456552630325_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1325131649259095273_i": {
            "samples": [0.002171986221114665, 0.002609860540872116, 0.003118064030284104, 0.00370390850444649, 0.004374646484101372, 0.005137279200435915, 0.005998337086518649, 0.006963635959888166, 0.008038013721346155, 0.009225054058572166, 0.01052680526488461, 0.011943503766852505, 0.013473313196074164, 0.015112090735730868, 0.01685319292267304, 0.018687333005137006, 0.020602501279722647, 0.022583958521671287, 0.024614310676048176, 0.02667367042822907, 0.028739908193952862, 0.030788991575058402, 0.03279540856535964, 0.034732665939567205, 0.036573850514480734, 0.03829223754247891, 0.039861927585410406, 0.0412584910079413, 0.04245959787865623, 0.043445610688308, 0.044200117949938736, 0.044710388440118876] + [0.0449677285193337] * 2 + [0.044710388440118876, 0.044200117949938736, 0.043445610688308, 0.04245959787865623, 0.0412584910079413, 0.039861927585410406, 0.03829223754247891, 0.036573850514480734, 0.034732665939567205, 0.03279540856535964, 0.030788991575058402, 0.028739908193952862, 0.02667367042822907, 0.024614310676048176, 0.022583958521671287, 0.020602501279722647, 0.018687333005137006, 0.01685319292267304, 0.015112090735730868, 0.013473313196074164, 0.011943503766852505, 0.01052680526488461, 0.009225054058572166, 0.008038013721346155, 0.006963635959888166, 0.005998337086518649, 0.005137279200435915, 0.004374646484101372, 0.00370390850444649, 0.003118064030284104, 0.002609860540872116, 0.002171986221114665] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1325131649259095273_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5055899984944537846_i": {
            "samples": [0.0021689646323143747, 0.00259931492734166, 0.0030977521849327484, 0.0036712654202062777, 0.004326794171231298, 0.005071051590628177, 0.005910322273415651, 0.00685023762010808, 0.007895532966577221, 0.00904979218747297, 0.01031518692593761, 0.0116922189367116, 0.013179475163895156, 0.014773406018382276, 0.016468137787138275, 0.0182553301210571, 0.02012408905060979, 0.022060944931844295, 0.02404990312009857, 0.026072573027081374, 0.02810837859433496, 0.030134850201614855, 0.03212799474266039, 0.03406273718987366, 0.03591342359971117, 0.03765437235880761, 0.03926045771391213, 0.04070770743270076, 0.041973894951609594, 0.04303910569305359, 0.04388625744905485, 0.044501555855697046, 0.04487486799687647, 0.045, 0.04487486799687647, 0.044501555855697046, 0.04388625744905485, 0.04303910569305359, 0.041973894951609594, 0.04070770743270076, 0.03926045771391213, 0.03765437235880761, 0.03591342359971117, 0.03406273718987366, 0.03212799474266039, 0.030134850201614855, 0.02810837859433496, 0.026072573027081374, 0.02404990312009857, 0.022060944931844295, 0.02012408905060979, 0.0182553301210571, 0.016468137787138275, 0.014773406018382276, 0.013179475163895156, 0.0116922189367116, 0.01031518692593761, 0.00904979218747297, 0.007895532966577221, 0.00685023762010808, 0.005910322273415651, 0.005071051590628177, 0.004326794171231298, 0.0036712654202062777, 0.0030977521849327484, 0.00259931492734166, 0.0021689646323143747, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5055899984944537846_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1822497030040153629_i": {
            "samples": [0.002166035271643658, 0.0025891131079189447, 0.003078140769086128, 0.0036398030554722935, 0.004280743914885552, 0.0050074032323041, 0.005825830397858919, 0.006741477102010137, 0.007758973075218879, 0.008881889799595737, 0.01011249851057478, 0.011451530007377753, 0.012897944825849661, 0.014448723118231133, 0.016098684056405882, 0.01784034466081627, 0.019663827602424643, 0.02155682669389912, 0.023504637465419673, 0.025490258423118042, 0.027494566355442732, 0.02949656645461664, 0.03147371515396398, 0.03340231056809872, 0.035257942401047876, 0.03701599030793991, 0.03865215711254247, 0.040143021143175674, 0.04146659038536539, 0.04260284026867511, 0.04353421678295046, 0.044246087293011806, 0.04472712288590957] + [0.04496959829325634] * 2 + [0.04472712288590957, 0.044246087293011806, 0.04353421678295046, 0.04260284026867511, 0.04146659038536539, 0.040143021143175674, 0.03865215711254247, 0.03701599030793991, 0.035257942401047876, 0.03340231056809872, 0.03147371515396398, 0.02949656645461664, 0.027494566355442732, 0.025490258423118042, 0.023504637465419673, 0.02155682669389912, 0.019663827602424643, 0.01784034466081627, 0.016098684056405882, 0.014448723118231133, 0.012897944825849661, 0.011451530007377753, 0.01011249851057478, 0.008881889799595737, 0.007758973075218879, 0.006741477102010137, 0.005825830397858919, 0.0050074032323041, 0.004280743914885552, 0.0036398030554722935, 0.003078140769086128, 0.0025891131079189447, 0.002166035271643658],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1822497030040153629_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3304235285041581290_i": {
            "samples": [0.002163193982716146, 0.002579238622452966, 0.0030591945816725377, 0.003609459723038464, 0.0042363986336785495, 0.00494619186999557, 0.005744663836344411, 0.0066370914436332945, 0.007627996818823539, 0.008720928501502967, 0.009918236716819908, 0.011220849394978333, 0.012628056550846435, 0.014137311375621348, 0.015744056860317837, 0.017441586908559705, 0.019220950654690473, 0.021070908048339047, 0.0229779436827221, 0.02492634433738389, 0.02689834380683798, 0.028874336349259823, 0.030833157592210256, 0.03275242907474077, 0.034608959903622755, 0.03637919638388446, 0.038039708083193915, 0.03956769673606484, 0.04094151280701048, 0.04214116351304094, 0.043148795731562835, 0.04394913753524951, 0.04452988311146775, 0.04488200751433152, 0.045, 0.04488200751433152, 0.04452988311146775, 0.04394913753524951, 0.043148795731562835, 0.04214116351304094, 0.04094151280701048, 0.03956769673606484, 0.038039708083193915, 0.03637919638388446, 0.034608959903622755, 0.03275242907474077, 0.030833157592210256, 0.028874336349259823, 0.02689834380683798, 0.02492634433738389, 0.0229779436827221, 0.021070908048339047, 0.019220950654690473, 0.017441586908559705, 0.015744056860317837, 0.014137311375621348, 0.012628056550846435, 0.011220849394978333, 0.009918236716819908, 0.008720928501502967, 0.007627996818823539, 0.0066370914436332945, 0.005744663836344411, 0.00494619186999557, 0.0042363986336785495, 0.003609459723038464, 0.0030591945816725377, 0.002579238622452966, 0.002163193982716146] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3304235285041581290_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4901294004185410489_i": {
            "samples": [0.0021604368550476164, 0.002569676040571002, 0.0030408807189704046, 0.003580177892320246, 0.004193667943116493, 0.00488728521988948, 0.005666638944560216, 0.006536836325154024, 0.007502290756732057, 0.008566519031111391, 0.009731932507344929, 0.010999628168486271, 0.012369186349601104, 0.013838482608945404, 0.01540352167143638, 0.017058301548348594, 0.0187947157852923, 0.02060250127972264, 0.022469238222628894, 0.024380407457957384, 0.026319508939098797, 0.028268243036700006, 0.03020675427893248, 0.03211393476571738, 0.03396778208950533, 0.035745804225606435, 0.037425461639280226, 0.038984634909117126, 0.04040210459417239, 0.04165802896999096, 0.04273440470076863, 0.043615495551435485, 0.044288214895822076, 0.04474244903575] + [0.04497131016992334] * 2 + [0.04474244903575, 0.044288214895822076, 0.043615495551435485, 0.04273440470076863, 0.04165802896999096, 0.04040210459417239, 0.038984634909117126, 0.037425461639280226, 0.035745804225606435, 0.03396778208950533, 0.03211393476571738, 0.03020675427893248, 0.028268243036700006, 0.026319508939098797, 0.024380407457957384, 0.022469238222628894, 0.02060250127972264, 0.0187947157852923, 0.017058301548348594, 0.01540352167143638, 0.013838482608945404, 0.012369186349601104, 0.010999628168486271, 0.009731932507344929, 0.008566519031111391, 0.007502290756732057, 0.006536836325154024, 0.005666638944560216, 0.00488728521988948, 0.004193667943116493, 0.003580177892320246, 0.0030408807189704046, 0.002569676040571002, 0.0021604368550476164] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4901294004185410489_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6327331914969551184_i": {
            "samples": [0.0021577602061462007, 0.00256041088269117, 0.0030231683917254235, 0.003551903849593068, 0.0041524675983879485, 0.004830560131804775, 0.005591584879652752, 0.006440484506803888, 0.007381563271341646, 0.008418298912115105, 0.009553148459435458, 0.010787353240006802, 0.012120749129840432, 0.013551588746267273, 0.015076382712201393, 0.016689767326000245, 0.018384405888755034, 0.020150930547545298, 0.021977930790704685, 0.02385199367719188, 0.025757799511374038, 0.027678275019371663, 0.029594804193792443, 0.03148749491696293, 0.03333549732966061, 0.035117367774724025, 0.036811470111183776, 0.03839640436462706, 0.03985145114932052, 0.04115701915355455, 0.042295082293231645, 0.0432495929617966, 0.044006858165732, 0.044555866236682166, 0.044888553229553804, 0.045, 0.044888553229553804, 0.044555866236682166, 0.044006858165732, 0.0432495929617966, 0.042295082293231645, 0.04115701915355455, 0.03985145114932052, 0.03839640436462706, 0.036811470111183776, 0.035117367774724025, 0.03333549732966061, 0.03148749491696293, 0.029594804193792443, 0.027678275019371663, 0.025757799511374038, 0.02385199367719188, 0.021977930790704685, 0.020150930547545298, 0.018384405888755034, 0.016689767326000245, 0.015076382712201393, 0.013551588746267273, 0.012120749129840432, 0.010787353240006802, 0.009553148459435458, 0.008418298912115105, 0.007381563271341646, 0.006440484506803888, 0.005591584879652752, 0.004830560131804775, 0.0041524675983879485, 0.003551903849593068, 0.0030231683917254235, 0.00256041088269117, 0.0021577602061462007, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6327331914969551184_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8312240252497376781_i": {
            "samples": [0.0021551605651445723, 0.0025514295481710446, 0.003006028759341267, 0.003524587390652799, 0.004112718991022126, 0.004775901832574295, 0.005519342536486394, 0.006347824416011567, 0.007265542786415831, 0.00827593031799268, 0.009381476336160563, 0.010583544763801127, 0.011882196113555836, 0.013276019527849927, 0.01476198128821445, 0.016335296431938186, 0.01798933008740271, 0.019715534841786272, 0.021503429868766095, 0.023340626664609936, 0.025212905078076605, 0.02710434189748496, 0.02899749261713379, 0.030873625199486478, 0.032713002746540806, 0.03449521007116611, 0.03619951730125708, 0.037805271943342475, 0.03929230936293479, 0.04064137048494054, 0.04183451474617286, 0.042855515995282936, 0.043690229166174925, 0.04432691616061069, 0.04475652045276505] + [0.04497288143846635] * 2 + [0.04475652045276505, 0.04432691616061069, 0.043690229166174925, 0.042855515995282936, 0.04183451474617286, 0.04064137048494054, 0.03929230936293479, 0.037805271943342475, 0.03619951730125708, 0.03449521007116611, 0.032713002746540806, 0.030873625199486478, 0.02899749261713379, 0.02710434189748496, 0.025212905078076605, 0.023340626664609936, 0.021503429868766095, 0.019715534841786272, 0.01798933008740271, 0.016335296431938186, 0.01476198128821445, 0.013276019527849927, 0.011882196113555836, 0.010583544763801127, 0.009381476336160563, 0.00827593031799268, 0.007265542786415831, 0.006347824416011567, 0.005519342536486394, 0.004775901832574295, 0.004112718991022126, 0.003524587390652799, 0.003006028759341267, 0.0025514295481710446, 0.0021551605651445723],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8312240252497376781_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8525091602972718047_i": {
            "samples": [0.0021526346578215473, 0.0025427192498536683, 0.0029894347793242714, 0.0034981815423799265, 0.004074348693517276, 0.004723203241918649, 0.005449763585535232, 0.006258658867933907, 0.0071539761497483294, 0.00813909812557603, 0.009216534860031633, 0.01038775373056061, 0.0116530124132898, 0.0130112002934734, 0.014459694085719213, 0.01599423367485511, 0.017608824203925306, 0.019295670215758183, 0.021045147181805075, 0.022845815020008063, 0.024684477217809496, 0.026546287955502738, 0.028414908200599404, 0.030272710160164185, 0.03210102779105792, 0.03388044934312591, 0.03559114621970404, 0.03721323085893177, 0.03872713494344725, 0.04011399810594215, 0.0413560564763048, 0.04243701996316964, 0.04334242711385802, 0.04405996676942095, 0.04457975652392329, 0.04489456918749988, 0.045, 0.04489456918749988, 0.04457975652392329, 0.04405996676942095, 0.04334242711385802, 0.04243701996316964, 0.0413560564763048, 0.04011399810594215, 0.03872713494344725, 0.03721323085893177, 0.03559114621970404, 0.03388044934312591, 0.03210102779105792, 0.030272710160164185, 0.028414908200599404, 0.026546287955502738, 0.024684477217809496, 0.022845815020008063, 0.021045147181805075, 0.019295670215758183, 0.017608824203925306, 0.01599423367485511, 0.014459694085719213, 0.0130112002934734, 0.0116530124132898, 0.01038775373056061, 0.009216534860031633, 0.00813909812557603, 0.0071539761497483294, 0.006258658867933907, 0.005449763585535232, 0.004723203241918649, 0.004074348693517276, 0.0034981815423799265, 0.0029894347793242714, 0.0025427192498536683, 0.0021526346578215473] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8525091602972718047_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6114480564494209918_i": {
            "samples": [0.0021501793928774163, 0.0025342679543580195, 0.0029733610703794443, 0.0034726423101149877, 0.004037288046759245, 0.004672364352978906, 0.00538270960151913, 0.006172803905368992, 0.00704662716352945, 0.00800750814011312, 0.00905796767184457, 0.010199559743662337, 0.011432714762644666, 0.01275658986367743, 0.014168931462649895, 0.01566595550244146, 0.017242250884816592, 0.01889071142409377, 0.020602501279722643, 0.02236705821708559, 0.024172138211441818, 0.026003903862479198, 0.02784705785134705, 0.02968502128437544, 0.03150015527426285, 0.03327402256535433, 0.034987684476295855, 0.0366220269762337, 0.03815810839596251, 0.03957752016653072, 0.04086275113228451, 0.04199754545138831, 0.04296724391052138, 0.0437590986631742, 0.044362551957982076, 0.044769470343010764] + [0.04497432708505203] * 2 + [0.044769470343010764, 0.044362551957982076, 0.0437590986631742, 0.04296724391052138, 0.04199754545138831, 0.04086275113228451, 0.03957752016653072, 0.03815810839596251, 0.0366220269762337, 0.034987684476295855, 0.03327402256535433, 0.03150015527426285, 0.02968502128437544, 0.02784705785134705, 0.026003903862479198, 0.024172138211441818, 0.02236705821708559, 0.020602501279722643, 0.01889071142409377, 0.017242250884816592, 0.01566595550244146, 0.014168931462649895, 0.01275658986367743, 0.011432714762644666, 0.010199559743662337, 0.00905796767184457, 0.00800750814011312, 0.00704662716352945, 0.006172803905368992, 0.00538270960151913, 0.004672364352978906, 0.004037288046759245, 0.0034726423101149877, 0.0029733610703794443, 0.0025342679543580195, 0.0021501793928774163] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6114480564494209918_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4688442653710069223_i": {
            "samples": [0.002147791849342387, 0.0025260643275360176, 0.0029577837877438713, 0.0034479284481222067, 0.0040014727856723855, 0.004623291670612245, 0.005318051273180125, 0.006090087745647572, 0.006943275247570575, 0.007880885475531793, 0.00890544145876266, 0.010018568964550093, 0.01122084939497833, 0.012511678520393735, 0.013889135755647852, 0.01534986891434664, 0.01688899944831298, 0.018500053072823434, 0.020174920377342438, 0.021903851518198725, 0.02367548838420554, 0.025476936728273888, 0.027293879687068503, 0.029110732895895854, 0.030910840085582453, 0.03267670666831609, 0.034390267432717066, 0.03603318313125636, 0.03758715951350724, 0.03903428129325348, 0.04035735268860909, 0.04154023558739861, 0.04256817610080444, 0.043428110300535616, 0.04410894029880399, 0.04460177252197282, 0.04490011102885229, 0.045, 0.04490011102885229, 0.04460177252197282, 0.04410894029880399, 0.043428110300535616, 0.04256817610080444, 0.04154023558739861, 0.04035735268860909, 0.03903428129325348, 0.03758715951350724, 0.03603318313125636, 0.034390267432717066, 0.03267670666831609, 0.030910840085582453, 0.029110732895895854, 0.027293879687068503, 0.025476936728273888, 0.02367548838420554, 0.021903851518198725, 0.020174920377342438, 0.018500053072823434, 0.01688899944831298, 0.01534986891434664, 0.013889135755647852, 0.012511678520393735, 0.01122084939497833, 0.010018568964550093, 0.00890544145876266, 0.007880885475531793, 0.006943275247570575, 0.006090087745647572, 0.005318051273180125, 0.004623291670612245, 0.0040014727856723855, 0.0034479284481222067, 0.0029577837877438713, 0.0025260643275360176, 0.002147791849342387, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4688442653710069223_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7040808322472363443_i": {
            "samples": [0.002145469265010479, 0.0025180976845833327, 0.0029426805095074922, 0.0034240012507389377, 0.003966842699084948, 0.0045758977013691336, 0.005255667685714234, 0.006010349823505539, 0.0068437142221444685, 0.007758973075218878, 0.008758644236996193, 0.009844412214928072, 0.011016990063460089, 0.012275986089621082, 0.013619779619870707, 0.015045410303477688, 0.016548485517319054, 0.01812311037093041, 0.019761844574239264, 0.02145569001512742, 0.023194112298432084, 0.024965098728831677, 0.026755254292330614, 0.028549936128284808, 0.030333425817680976, 0.03208913758244995, 0.03379985923954389, 0.035448021531003945, 0.03701599030793991, 0.03848637503253217, 0.03984234622532486, 0.04106795386740071, 0.04214843840311731, 0.04307052590392806, 0.04382269916117862, 0.04439543697712503, 0.04478141470745432] + [0.04497566015139245] * 2 + [0.04478141470745432, 0.04439543697712503, 0.04382269916117862, 0.04307052590392806, 0.04214843840311731, 0.04106795386740071, 0.03984234622532486, 0.03848637503253217, 0.03701599030793991, 0.035448021531003945, 0.03379985923954389, 0.03208913758244995, 0.030333425817680976, 0.028549936128284808, 0.026755254292330614, 0.024965098728831677, 0.023194112298432084, 0.02145569001512742, 0.019761844574239264, 0.01812311037093041, 0.016548485517319054, 0.015045410303477688, 0.013619779619870707, 0.012275986089621082, 0.011016990063460089, 0.009844412214928072, 0.008758644236996193, 0.007758973075218878, 0.0068437142221444685, 0.006010349823505539, 0.005255667685714234, 0.0045758977013691336, 0.003966842699084948, 0.0034240012507389377, 0.0029426805095074922, 0.0025180976845833327, 0.002145469265010479],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7040808322472363443_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2035348380515494895_i": {
            "samples": [0.0021432090258028083, 0.0025103579443485785, 0.0029280301328143657, 0.003400824362087738, 0.003933341320261181, 0.004530100489780402, 0.005195445668351942, 0.005933439920175686, 0.006747751198620647, 0.007641530360080955, 0.008617283775659838, 0.00967674322407993, 0.010820736195198617, 0.012049060126664212, 0.013360364413972401, 0.014752044254341146, 0.01622015048690195, 0.01775931955800422, 0.019362727557242443, 0.02102207192854205, 0.022727583958740687, 0.024468074487837863, 0.026231014481970672, 0.02800265118108745, 0.029768159504221858, 0.03151182729865732, 0.03321727189296453, 0.03486768429974622, 0.036446096356076804, 0.03793566513256709, 0.039319968128458664, 0.04058330213903772, 0.04171097826593652, 0.04268960536581334, 0.04350735431447342, 0.044154195807363496, 0.044622105018217416, 0.0449052272790755, 0.045, 0.0449052272790755, 0.044622105018217416, 0.044154195807363496, 0.04350735431447342, 0.04268960536581334, 0.04171097826593652, 0.04058330213903772, 0.039319968128458664, 0.03793566513256709, 0.036446096356076804, 0.03486768429974622, 0.03321727189296453, 0.03151182729865732, 0.029768159504221858, 0.02800265118108745, 0.026231014481970672, 0.024468074487837863, 0.022727583958740687, 0.02102207192854205, 0.019362727557242443, 0.01775931955800422, 0.01622015048690195, 0.014752044254341146, 0.013360364413972401, 0.012049060126664212, 0.010820736195198617, 0.00967674322407993, 0.008617283775659838, 0.007641530360080955, 0.006747751198620647, 0.005933439920175686, 0.005195445668351942, 0.004530100489780402, 0.003933341320261181, 0.003400824362087738, 0.0029280301328143657, 0.0025103579443485785, 0.0021432090258028083] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2035348380515494895_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2269188906508187112_i": {
            "samples": [0.002141008655974335, 0.0025028355874354992, 0.0029138127789625334, 0.0033783636024714127, 0.0039009156449618795, 0.004485823196201629, 0.005137279200435915, 0.0058592173700232975, 0.006655205567335754, 0.007528331991962452, 0.008481086149534151, 0.00951523701029627, 0.010631711171939819, 0.011830474202861594, 0.013110418639099576, 0.014469262321099336, 0.015903460866896136, 0.01740813807020783, 0.018977037872588722, 0.020602501279722643, 0.022275471169779036, 0.023985527378951276, 0.025720953754510386, 0.027468838054007422, 0.029215204661970466, 0.030945179119672497, 0.03264318245137526, 0.03429315225781028, 0.03587878657292559, 0.03738380558232485, 0.038792225519649066, 0.040088638425953435, 0.0412584910079413, 0.042288355588599384, 0.04316618612562091, 0.043881552487627755, 0.04442584662486435, 0.044792454939364075] + [0.04497689202979855] * 2 + [0.044792454939364075, 0.04442584662486435, 0.043881552487627755, 0.04316618612562091, 0.042288355588599384, 0.0412584910079413, 0.040088638425953435, 0.038792225519649066, 0.03738380558232485, 0.03587878657292559, 0.03429315225781028, 0.03264318245137526, 0.030945179119672497, 0.029215204661970466, 0.027468838054007422, 0.025720953754510386, 0.023985527378951276, 0.022275471169779036, 0.020602501279722643, 0.018977037872588722, 0.01740813807020783, 0.015903460866896136, 0.014469262321099336, 0.013110418639099576, 0.011830474202861594, 0.010631711171939819, 0.00951523701029627, 0.008481086149534151, 0.007528331991962452, 0.006655205567335754, 0.0058592173700232975, 0.005137279200435915, 0.004485823196201629, 0.0039009156449618795, 0.0033783636024714127, 0.0029138127789625334, 0.0025028355874354992, 0.002141008655974335] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2269188906508187112_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1537982999734436539_i": {
            "samples": [0.002138865809087063, 0.0024955216177367967, 0.0029000097065299086, 0.003356586809784028, 0.0038695158742528477, 0.004442993712003372, 0.005081068870094062, 0.005787550337006248, 0.006565908073257962, 0.007419166741676062, 0.008349794409521471, 0.009359588386083407, 0.01044956072980217, 0.011619826291553531, 0.012869496437953957, 0.014196581803098438, 0.015597907532670414, 0.017069044496358852, 0.018604259841200503, 0.020196490031619566, 0.021837339167665844, 0.023517104892288677, 0.02522483359781917, 0.026948405933114875, 0.028674652813496203, 0.03038950126827824, 0.03207814855252314, 0.03372526203140174, 0.03531520145056301, 0.03683225936864509, 0.0382609147826893, 0.03958609435604398, 0.04079343519026052, 0.0418695427915073, 0.04280223778600969, 0.04358078504860368, 0.04419609922635268, 0.04464092115967802, 0.044909960412638034, 0.045, 0.044909960412638034, 0.04464092115967802, 0.04419609922635268, 0.04358078504860368, 0.04280223778600969, 0.0418695427915073, 0.04079343519026052, 0.03958609435604398, 0.0382609147826893, 0.03683225936864509, 0.03531520145056301, 0.03372526203140174, 0.03207814855252314, 0.03038950126827824, 0.028674652813496203, 0.026948405933114875, 0.02522483359781917, 0.023517104892288677, 0.021837339167665844, 0.020196490031619566, 0.018604259841200503, 0.017069044496358852, 0.015597907532670414, 0.014196581803098438, 0.012869496437953957, 0.011619826291553531, 0.01044956072980217, 0.009359588386083407, 0.008349794409521471, 0.007419166741676062, 0.006565908073257962, 0.005787550337006248, 0.005081068870094062, 0.004442993712003372, 0.0038695158742528477, 0.003356586809784028, 0.0029000097065299086, 0.0024955216177367967, 0.002138865809087063, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1537982999734436539_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "D1/acquisition_mixer_4b8": [{'intermediate_frequency': -312360584.50398064, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_cb2": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

