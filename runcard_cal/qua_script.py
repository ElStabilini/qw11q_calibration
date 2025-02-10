
# Single QUA script generated at 2025-02-10 06:58:13.917175
# QUA library version: 1.1.6

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
        with for_(v8,0,(v8<=79),(v8+1)):
            with for_(v9,-1.99,(v9<-1.8711639676113359),(v9+0.0040283400809717484)):
                align()
                play("-7214017706243396228", "B2/drive")
                play("4627626324609100052", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-6903055487712810610"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-6681561428514095362"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-1669845670686046264"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("1647928247818531605"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("1370733844402529391"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("749408076515835847"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("8954937365742827626"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("3334945987892111496"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("594802095756708490"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-5025189282094007640"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-1218017375851383989"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-5522554662875065996"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("979742312151782874"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("1201236371350498122"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("6212952129178547220"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("6434446188377262468"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("4825033970137805680"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("8632205876380429331"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("8853699935579144579"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-182970997317989811"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-7395284450127240174"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("2857608517770585844"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-2162074633100475828"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("8090818334797350190"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("7469492566910656646"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("5987754311909228985"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-7936671991710319315"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-8557997759597012859"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-2703462174683554969"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-6360238071593845996"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-505702486680388106"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-284208427481672858"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("7921320861745318921"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("1913551260521494005"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("5720723166764117656"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("7146761077548258351"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-3094453706934301486"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-4576191961935729147"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-8880729248959411154"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-675199959732419375"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("5179335625181038515"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("1522559728270747488"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-8495789032564336770"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("7598589372382920626"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("6977263604496227082"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-1216587501315498516"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-3541145583402334969"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-3417185196296699781"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("7362203820891301466"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("6214382003714432693"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-997931449094817670"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("4111317980826311488"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("8633635750916314804"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-3432076688589603693"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-7615348634790069949"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-7393854575591354701"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-2382138817763305603"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-2160644758564590355"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-3642383013566018016"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("37114929438576508"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("258608988637291756"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("-1775704542169515971"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("3788586491463913193"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("-6452628293018646644"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("643549205032366140"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-6949993673799705000"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-2828830694231339086"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("488943224273238783"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("1914981135057379478"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("5722153041300003129"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("-1945202015221547240"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("7919912729303169992"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("-4574762087399843674"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-5293621527379617278"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("-5072127468180902030"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("-5349321871596904244"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-2874367780177735167"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("3077701476828802783"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("2358842036849029179"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("5275461164831969646"*amp(v9), "B4/flux")
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
                play("4627626324609100052", "B4/drive")
                measure("5154831460063705726", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-5600454482625450093", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(30).buffer(80).average().save("5154831460063705726_B2|acquisition_shots")
        r2.buffer(30).buffer(80).average().save("-5600454482625450093_B4|acquisition_shots")


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
                "9015628126969995137": "9015628126969995137",
                "-8648965138787578654": "-8648965138787578654",
                "-6903055487712810610": "-6903055487712810610",
                "-6681561428514095362": "-6681561428514095362",
                "-1669845670686046264": "-1669845670686046264",
                "1647928247818531605": "1647928247818531605",
                "1370733844402529391": "1370733844402529391",
                "749408076515835847": "749408076515835847",
                "8954937365742827626": "8954937365742827626",
                "3334945987892111496": "3334945987892111496",
                "594802095756708490": "594802095756708490",
                "-5025189282094007640": "-5025189282094007640",
                "-1218017375851383989": "-1218017375851383989",
                "-5522554662875065996": "-5522554662875065996",
                "979742312151782874": "979742312151782874",
                "1201236371350498122": "1201236371350498122",
                "6212952129178547220": "6212952129178547220",
                "6434446188377262468": "6434446188377262468",
                "4825033970137805680": "4825033970137805680",
                "8632205876380429331": "8632205876380429331",
                "8853699935579144579": "8853699935579144579",
                "-182970997317989811": "-182970997317989811",
                "-7395284450127240174": "-7395284450127240174",
                "2857608517770585844": "2857608517770585844",
                "-2162074633100475828": "-2162074633100475828",
                "8090818334797350190": "8090818334797350190",
                "7469492566910656646": "7469492566910656646",
                "5987754311909228985": "5987754311909228985",
                "-7936671991710319315": "-7936671991710319315",
                "-8557997759597012859": "-8557997759597012859",
                "-2703462174683554969": "-2703462174683554969",
                "-6360238071593845996": "-6360238071593845996",
                "-505702486680388106": "-505702486680388106",
                "-284208427481672858": "-284208427481672858",
                "7921320861745318921": "7921320861745318921",
                "1913551260521494005": "1913551260521494005",
                "5720723166764117656": "5720723166764117656",
                "7146761077548258351": "7146761077548258351",
                "-3094453706934301486": "-3094453706934301486",
                "-4576191961935729147": "-4576191961935729147",
                "-8880729248959411154": "-8880729248959411154",
                "-675199959732419375": "-675199959732419375",
                "5179335625181038515": "5179335625181038515",
                "1522559728270747488": "1522559728270747488",
                "-8495789032564336770": "-8495789032564336770",
                "7598589372382920626": "7598589372382920626",
                "6977263604496227082": "6977263604496227082",
                "-1216587501315498516": "-1216587501315498516",
                "-3541145583402334969": "-3541145583402334969",
                "-3417185196296699781": "-3417185196296699781",
                "7362203820891301466": "7362203820891301466",
                "6214382003714432693": "6214382003714432693",
                "-997931449094817670": "-997931449094817670",
                "4111317980826311488": "4111317980826311488",
                "8633635750916314804": "8633635750916314804",
                "-3432076688589603693": "-3432076688589603693",
                "-7615348634790069949": "-7615348634790069949",
                "-7393854575591354701": "-7393854575591354701",
                "-2382138817763305603": "-2382138817763305603",
                "-2160644758564590355": "-2160644758564590355",
                "-3642383013566018016": "-3642383013566018016",
                "37114929438576508": "37114929438576508",
                "258608988637291756": "258608988637291756",
                "-1775704542169515971": "-1775704542169515971",
                "3788586491463913193": "3788586491463913193",
                "-6452628293018646644": "-6452628293018646644",
                "643549205032366140": "643549205032366140",
                "-6949993673799705000": "-6949993673799705000",
                "-2828830694231339086": "-2828830694231339086",
                "488943224273238783": "488943224273238783",
                "1914981135057379478": "1914981135057379478",
                "5722153041300003129": "5722153041300003129",
                "-1945202015221547240": "-1945202015221547240",
                "7919912729303169992": "7919912729303169992",
                "-4574762087399843674": "-4574762087399843674",
                "-5293621527379617278": "-5293621527379617278",
                "-5072127468180902030": "-5072127468180902030",
                "-5349321871596904244": "-5349321871596904244",
                "-2874367780177735167": "-2874367780177735167",
                "3077701476828802783": "3077701476828802783",
                "2358842036849029179": "2358842036849029179",
                "5275461164831969646": "5275461164831969646",
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
                "-7214017706243396228": "-7214017706243396228",
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
                "-5600454482625450093": "-5600454482625450093_B4/acquisition",
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
                "4627626324609100052": "4627626324609100052",
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
                "5154831460063705726": "5154831460063705726_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-7214017706243396228": {
            "length": 40,
            "waveforms": {
                "I": "-7214017706243396228_i",
                "Q": "-7214017706243396228_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4627626324609100052": {
            "length": 40,
            "waveforms": {
                "I": "4627626324609100052_i",
                "Q": "4627626324609100052_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9015628126969995137": {
            "length": 80,
            "waveforms": {
                "single": "9015628126969995137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5154831460063705726_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1052249854807244050_i",
                "Q": "-1052249854807244050_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-5600454482625450093_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1165117755933466191_i",
                "Q": "1165117755933466191_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-8648965138787578654": {
            "length": 80,
            "waveforms": {
                "single": "-8648965138787578654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6903055487712810610": {
            "length": 16,
            "waveforms": {
                "single": "-6903055487712810610",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6681561428514095362": {
            "length": 16,
            "waveforms": {
                "single": "-6681561428514095362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1669845670686046264": {
            "length": 16,
            "waveforms": {
                "single": "-1669845670686046264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1647928247818531605": {
            "length": 16,
            "waveforms": {
                "single": "1647928247818531605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1370733844402529391": {
            "length": 16,
            "waveforms": {
                "single": "1370733844402529391",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "749408076515835847": {
            "length": 16,
            "waveforms": {
                "single": "749408076515835847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8954937365742827626": {
            "length": 16,
            "waveforms": {
                "single": "8954937365742827626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3334945987892111496": {
            "length": 16,
            "waveforms": {
                "single": "3334945987892111496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "594802095756708490": {
            "length": 16,
            "waveforms": {
                "single": "594802095756708490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5025189282094007640": {
            "length": 16,
            "waveforms": {
                "single": "-5025189282094007640",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1218017375851383989": {
            "length": 16,
            "waveforms": {
                "single": "-1218017375851383989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5522554662875065996": {
            "length": 16,
            "waveforms": {
                "single": "-5522554662875065996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "979742312151782874": {
            "length": 16,
            "waveforms": {
                "single": "979742312151782874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1201236371350498122": {
            "length": 16,
            "waveforms": {
                "single": "1201236371350498122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6212952129178547220": {
            "length": 16,
            "waveforms": {
                "single": "6212952129178547220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6434446188377262468": {
            "length": 16,
            "waveforms": {
                "single": "6434446188377262468",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4825033970137805680": {
            "length": 16,
            "waveforms": {
                "single": "4825033970137805680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8632205876380429331": {
            "length": 20,
            "waveforms": {
                "single": "8632205876380429331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8853699935579144579": {
            "length": 20,
            "waveforms": {
                "single": "8853699935579144579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-182970997317989811": {
            "length": 20,
            "waveforms": {
                "single": "-182970997317989811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7395284450127240174": {
            "length": 20,
            "waveforms": {
                "single": "-7395284450127240174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2857608517770585844": {
            "length": 24,
            "waveforms": {
                "single": "2857608517770585844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2162074633100475828": {
            "length": 24,
            "waveforms": {
                "single": "-2162074633100475828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8090818334797350190": {
            "length": 24,
            "waveforms": {
                "single": "8090818334797350190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7469492566910656646": {
            "length": 24,
            "waveforms": {
                "single": "7469492566910656646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5987754311909228985": {
            "length": 28,
            "waveforms": {
                "single": "5987754311909228985",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7936671991710319315": {
            "length": 28,
            "waveforms": {
                "single": "-7936671991710319315",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8557997759597012859": {
            "length": 28,
            "waveforms": {
                "single": "-8557997759597012859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2703462174683554969": {
            "length": 28,
            "waveforms": {
                "single": "-2703462174683554969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6360238071593845996": {
            "length": 32,
            "waveforms": {
                "single": "-6360238071593845996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-505702486680388106": {
            "length": 32,
            "waveforms": {
                "single": "-505702486680388106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-284208427481672858": {
            "length": 32,
            "waveforms": {
                "single": "-284208427481672858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7921320861745318921": {
            "length": 32,
            "waveforms": {
                "single": "7921320861745318921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1913551260521494005": {
            "length": 36,
            "waveforms": {
                "single": "1913551260521494005",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5720723166764117656": {
            "length": 36,
            "waveforms": {
                "single": "5720723166764117656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7146761077548258351": {
            "length": 36,
            "waveforms": {
                "single": "7146761077548258351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3094453706934301486": {
            "length": 36,
            "waveforms": {
                "single": "-3094453706934301486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4576191961935729147": {
            "length": 40,
            "waveforms": {
                "single": "-4576191961935729147",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8880729248959411154": {
            "length": 40,
            "waveforms": {
                "single": "-8880729248959411154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-675199959732419375": {
            "length": 40,
            "waveforms": {
                "single": "-675199959732419375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5179335625181038515": {
            "length": 40,
            "waveforms": {
                "single": "5179335625181038515",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1522559728270747488": {
            "length": 44,
            "waveforms": {
                "single": "1522559728270747488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8495789032564336770": {
            "length": 44,
            "waveforms": {
                "single": "-8495789032564336770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7598589372382920626": {
            "length": 44,
            "waveforms": {
                "single": "7598589372382920626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6977263604496227082": {
            "length": 44,
            "waveforms": {
                "single": "6977263604496227082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216587501315498516": {
            "length": 48,
            "waveforms": {
                "single": "-1216587501315498516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3541145583402334969": {
            "length": 48,
            "waveforms": {
                "single": "-3541145583402334969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3417185196296699781": {
            "length": 48,
            "waveforms": {
                "single": "-3417185196296699781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7362203820891301466": {
            "length": 48,
            "waveforms": {
                "single": "7362203820891301466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6214382003714432693": {
            "length": 52,
            "waveforms": {
                "single": "6214382003714432693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-997931449094817670": {
            "length": 52,
            "waveforms": {
                "single": "-997931449094817670",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4111317980826311488": {
            "length": 52,
            "waveforms": {
                "single": "4111317980826311488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8633635750916314804": {
            "length": 52,
            "waveforms": {
                "single": "8633635750916314804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3432076688589603693": {
            "length": 56,
            "waveforms": {
                "single": "-3432076688589603693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7615348634790069949": {
            "length": 56,
            "waveforms": {
                "single": "-7615348634790069949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7393854575591354701": {
            "length": 56,
            "waveforms": {
                "single": "-7393854575591354701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2382138817763305603": {
            "length": 56,
            "waveforms": {
                "single": "-2382138817763305603",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2160644758564590355": {
            "length": 60,
            "waveforms": {
                "single": "-2160644758564590355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3642383013566018016": {
            "length": 60,
            "waveforms": {
                "single": "-3642383013566018016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "37114929438576508": {
            "length": 60,
            "waveforms": {
                "single": "37114929438576508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "258608988637291756": {
            "length": 60,
            "waveforms": {
                "single": "258608988637291756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1775704542169515971": {
            "length": 64,
            "waveforms": {
                "single": "-1775704542169515971",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3788586491463913193": {
            "length": 64,
            "waveforms": {
                "single": "3788586491463913193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6452628293018646644": {
            "length": 64,
            "waveforms": {
                "single": "-6452628293018646644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "643549205032366140": {
            "length": 64,
            "waveforms": {
                "single": "643549205032366140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6949993673799705000": {
            "length": 68,
            "waveforms": {
                "single": "-6949993673799705000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2828830694231339086": {
            "length": 68,
            "waveforms": {
                "single": "-2828830694231339086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "488943224273238783": {
            "length": 68,
            "waveforms": {
                "single": "488943224273238783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1914981135057379478": {
            "length": 68,
            "waveforms": {
                "single": "1914981135057379478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5722153041300003129": {
            "length": 72,
            "waveforms": {
                "single": "5722153041300003129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1945202015221547240": {
            "length": 72,
            "waveforms": {
                "single": "-1945202015221547240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7919912729303169992": {
            "length": 72,
            "waveforms": {
                "single": "7919912729303169992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4574762087399843674": {
            "length": 72,
            "waveforms": {
                "single": "-4574762087399843674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5293621527379617278": {
            "length": 76,
            "waveforms": {
                "single": "-5293621527379617278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5072127468180902030": {
            "length": 76,
            "waveforms": {
                "single": "-5072127468180902030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5349321871596904244": {
            "length": 76,
            "waveforms": {
                "single": "-5349321871596904244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2874367780177735167": {
            "length": 76,
            "waveforms": {
                "single": "-2874367780177735167",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3077701476828802783": {
            "length": 80,
            "waveforms": {
                "single": "3077701476828802783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2358842036849029179": {
            "length": 80,
            "waveforms": {
                "single": "2358842036849029179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5275461164831969646": {
            "length": 80,
            "waveforms": {
                "single": "5275461164831969646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7214017706243396228_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-7214017706243396228_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "4627626324609100052_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "4627626324609100052_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "9015628126969995137": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-1052249854807244050_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1052249854807244050_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1165117755933466191_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1165117755933466191_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8648965138787578654": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6903055487712810610": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6681561428514095362": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-1669845670686046264": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "1647928247818531605": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "1370733844402529391": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "749408076515835847": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "8954937365742827626": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3334945987892111496": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "594802095756708490": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-5025189282094007640": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-1218017375851383989": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-5522554662875065996": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "979742312151782874": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "1201236371350498122": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6212952129178547220": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6434446188377262468": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
        },
        "4825033970137805680": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8632205876380429331": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8853699935579144579": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-182970997317989811": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-7395284450127240174": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2857608517770585844": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2162074633100475828": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8090818334797350190": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
        },
        "7469492566910656646": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "5987754311909228985": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7936671991710319315": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8557997759597012859": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-2703462174683554969": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6360238071593845996": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-505702486680388106": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-284208427481672858": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
        },
        "7921320861745318921": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1913551260521494005": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5720723166764117656": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7146761077548258351": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-3094453706934301486": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-4576191961935729147": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8880729248959411154": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-675199959732419375": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
        },
        "5179335625181038515": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1522559728270747488": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8495789032564336770": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7598589372382920626": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
        },
        "6977263604496227082": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-1216587501315498516": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3541145583402334969": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3417185196296699781": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
        },
        "7362203820891301466": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6214382003714432693": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-997931449094817670": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4111317980826311488": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
        },
        "8633635750916314804": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3432076688589603693": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7615348634790069949": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7393854575591354701": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-2382138817763305603": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-2160644758564590355": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3642383013566018016": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "37114929438576508": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
        },
        "258608988637291756": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-1775704542169515971": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3788586491463913193": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6452628293018646644": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
        },
        "643549205032366140": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6949993673799705000": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2828830694231339086": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "488943224273238783": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
        },
        "1914981135057379478": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "5722153041300003129": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1945202015221547240": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7919912729303169992": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-4574762087399843674": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5293621527379617278": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5072127468180902030": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5349321871596904244": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-2874367780177735167": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "3077701476828802783": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2358842036849029179": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5275461164831969646": {
            "samples": [0.06206030150753769] * 79 + [0.0],
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
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
                    },
                },
                "5": {
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
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": 0.05418914676504196,
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
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
            },
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
                },
                "8": {
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
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 1),
            },
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 2),
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
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 3),
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
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "operations": {
                "9015628126969995137": "9015628126969995137",
                "-8648965138787578654": "-8648965138787578654",
                "-6903055487712810610": "-6903055487712810610",
                "-6681561428514095362": "-6681561428514095362",
                "-1669845670686046264": "-1669845670686046264",
                "1647928247818531605": "1647928247818531605",
                "1370733844402529391": "1370733844402529391",
                "749408076515835847": "749408076515835847",
                "8954937365742827626": "8954937365742827626",
                "3334945987892111496": "3334945987892111496",
                "594802095756708490": "594802095756708490",
                "-5025189282094007640": "-5025189282094007640",
                "-1218017375851383989": "-1218017375851383989",
                "-5522554662875065996": "-5522554662875065996",
                "979742312151782874": "979742312151782874",
                "1201236371350498122": "1201236371350498122",
                "6212952129178547220": "6212952129178547220",
                "6434446188377262468": "6434446188377262468",
                "4825033970137805680": "4825033970137805680",
                "8632205876380429331": "8632205876380429331",
                "8853699935579144579": "8853699935579144579",
                "-182970997317989811": "-182970997317989811",
                "-7395284450127240174": "-7395284450127240174",
                "2857608517770585844": "2857608517770585844",
                "-2162074633100475828": "-2162074633100475828",
                "8090818334797350190": "8090818334797350190",
                "7469492566910656646": "7469492566910656646",
                "5987754311909228985": "5987754311909228985",
                "-7936671991710319315": "-7936671991710319315",
                "-8557997759597012859": "-8557997759597012859",
                "-2703462174683554969": "-2703462174683554969",
                "-6360238071593845996": "-6360238071593845996",
                "-505702486680388106": "-505702486680388106",
                "-284208427481672858": "-284208427481672858",
                "7921320861745318921": "7921320861745318921",
                "1913551260521494005": "1913551260521494005",
                "5720723166764117656": "5720723166764117656",
                "7146761077548258351": "7146761077548258351",
                "-3094453706934301486": "-3094453706934301486",
                "-4576191961935729147": "-4576191961935729147",
                "-8880729248959411154": "-8880729248959411154",
                "-675199959732419375": "-675199959732419375",
                "5179335625181038515": "5179335625181038515",
                "1522559728270747488": "1522559728270747488",
                "-8495789032564336770": "-8495789032564336770",
                "7598589372382920626": "7598589372382920626",
                "6977263604496227082": "6977263604496227082",
                "-1216587501315498516": "-1216587501315498516",
                "-3541145583402334969": "-3541145583402334969",
                "-3417185196296699781": "-3417185196296699781",
                "7362203820891301466": "7362203820891301466",
                "6214382003714432693": "6214382003714432693",
                "-997931449094817670": "-997931449094817670",
                "4111317980826311488": "4111317980826311488",
                "8633635750916314804": "8633635750916314804",
                "-3432076688589603693": "-3432076688589603693",
                "-7615348634790069949": "-7615348634790069949",
                "-7393854575591354701": "-7393854575591354701",
                "-2382138817763305603": "-2382138817763305603",
                "-2160644758564590355": "-2160644758564590355",
                "-3642383013566018016": "-3642383013566018016",
                "37114929438576508": "37114929438576508",
                "258608988637291756": "258608988637291756",
                "-1775704542169515971": "-1775704542169515971",
                "3788586491463913193": "3788586491463913193",
                "-6452628293018646644": "-6452628293018646644",
                "643549205032366140": "643549205032366140",
                "-6949993673799705000": "-6949993673799705000",
                "-2828830694231339086": "-2828830694231339086",
                "488943224273238783": "488943224273238783",
                "1914981135057379478": "1914981135057379478",
                "5722153041300003129": "5722153041300003129",
                "-1945202015221547240": "-1945202015221547240",
                "7919912729303169992": "7919912729303169992",
                "-4574762087399843674": "-4574762087399843674",
                "-5293621527379617278": "-5293621527379617278",
                "-5072127468180902030": "-5072127468180902030",
                "-5349321871596904244": "-5349321871596904244",
                "-2874367780177735167": "-2874367780177735167",
                "3077701476828802783": "3077701476828802783",
                "2358842036849029179": "2358842036849029179",
                "5275461164831969646": "5275461164831969646",
            },
            "singleInput": {
                "port": ('con4', 4),
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
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 5),
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
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 63761228.0,
            "operations": {
                "-7214017706243396228": "-7214017706243396228",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_9ff",
                "lo_frequency": 5900000000.0,
            },
        },
        "B4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1),
                "out2": ('con2', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": 330300527.0,
            "operations": {
                "-5600454482625450093": "-5600454482625450093_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_fc3",
                "lo_frequency": 7370000000.0,
            },
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109615374.0,
            "operations": {
                "4627626324609100052": "4627626324609100052",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_20d",
                "lo_frequency": 6700000000.0,
            },
        },
        "B2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1),
                "out2": ('con2', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": 10040944.0,
            "operations": {
                "5154831460063705726": "5154831460063705726_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_1bb",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-7214017706243396228": {
            "length": 40,
            "waveforms": {
                "I": "-7214017706243396228_i",
                "Q": "-7214017706243396228_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4627626324609100052": {
            "length": 40,
            "waveforms": {
                "I": "4627626324609100052_i",
                "Q": "4627626324609100052_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9015628126969995137": {
            "length": 80,
            "waveforms": {
                "single": "9015628126969995137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5154831460063705726_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1052249854807244050_i",
                "Q": "-1052249854807244050_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-5600454482625450093_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1165117755933466191_i",
                "Q": "1165117755933466191_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-8648965138787578654": {
            "length": 80,
            "waveforms": {
                "single": "-8648965138787578654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6903055487712810610": {
            "length": 16,
            "waveforms": {
                "single": "-6903055487712810610",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6681561428514095362": {
            "length": 16,
            "waveforms": {
                "single": "-6681561428514095362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1669845670686046264": {
            "length": 16,
            "waveforms": {
                "single": "-1669845670686046264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1647928247818531605": {
            "length": 16,
            "waveforms": {
                "single": "1647928247818531605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1370733844402529391": {
            "length": 16,
            "waveforms": {
                "single": "1370733844402529391",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "749408076515835847": {
            "length": 16,
            "waveforms": {
                "single": "749408076515835847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8954937365742827626": {
            "length": 16,
            "waveforms": {
                "single": "8954937365742827626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3334945987892111496": {
            "length": 16,
            "waveforms": {
                "single": "3334945987892111496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "594802095756708490": {
            "length": 16,
            "waveforms": {
                "single": "594802095756708490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5025189282094007640": {
            "length": 16,
            "waveforms": {
                "single": "-5025189282094007640",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1218017375851383989": {
            "length": 16,
            "waveforms": {
                "single": "-1218017375851383989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5522554662875065996": {
            "length": 16,
            "waveforms": {
                "single": "-5522554662875065996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "979742312151782874": {
            "length": 16,
            "waveforms": {
                "single": "979742312151782874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1201236371350498122": {
            "length": 16,
            "waveforms": {
                "single": "1201236371350498122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6212952129178547220": {
            "length": 16,
            "waveforms": {
                "single": "6212952129178547220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6434446188377262468": {
            "length": 16,
            "waveforms": {
                "single": "6434446188377262468",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4825033970137805680": {
            "length": 16,
            "waveforms": {
                "single": "4825033970137805680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8632205876380429331": {
            "length": 20,
            "waveforms": {
                "single": "8632205876380429331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8853699935579144579": {
            "length": 20,
            "waveforms": {
                "single": "8853699935579144579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-182970997317989811": {
            "length": 20,
            "waveforms": {
                "single": "-182970997317989811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7395284450127240174": {
            "length": 20,
            "waveforms": {
                "single": "-7395284450127240174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2857608517770585844": {
            "length": 24,
            "waveforms": {
                "single": "2857608517770585844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2162074633100475828": {
            "length": 24,
            "waveforms": {
                "single": "-2162074633100475828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8090818334797350190": {
            "length": 24,
            "waveforms": {
                "single": "8090818334797350190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7469492566910656646": {
            "length": 24,
            "waveforms": {
                "single": "7469492566910656646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5987754311909228985": {
            "length": 28,
            "waveforms": {
                "single": "5987754311909228985",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7936671991710319315": {
            "length": 28,
            "waveforms": {
                "single": "-7936671991710319315",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8557997759597012859": {
            "length": 28,
            "waveforms": {
                "single": "-8557997759597012859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2703462174683554969": {
            "length": 28,
            "waveforms": {
                "single": "-2703462174683554969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6360238071593845996": {
            "length": 32,
            "waveforms": {
                "single": "-6360238071593845996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-505702486680388106": {
            "length": 32,
            "waveforms": {
                "single": "-505702486680388106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-284208427481672858": {
            "length": 32,
            "waveforms": {
                "single": "-284208427481672858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7921320861745318921": {
            "length": 32,
            "waveforms": {
                "single": "7921320861745318921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1913551260521494005": {
            "length": 36,
            "waveforms": {
                "single": "1913551260521494005",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5720723166764117656": {
            "length": 36,
            "waveforms": {
                "single": "5720723166764117656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7146761077548258351": {
            "length": 36,
            "waveforms": {
                "single": "7146761077548258351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3094453706934301486": {
            "length": 36,
            "waveforms": {
                "single": "-3094453706934301486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4576191961935729147": {
            "length": 40,
            "waveforms": {
                "single": "-4576191961935729147",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8880729248959411154": {
            "length": 40,
            "waveforms": {
                "single": "-8880729248959411154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-675199959732419375": {
            "length": 40,
            "waveforms": {
                "single": "-675199959732419375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5179335625181038515": {
            "length": 40,
            "waveforms": {
                "single": "5179335625181038515",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1522559728270747488": {
            "length": 44,
            "waveforms": {
                "single": "1522559728270747488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8495789032564336770": {
            "length": 44,
            "waveforms": {
                "single": "-8495789032564336770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7598589372382920626": {
            "length": 44,
            "waveforms": {
                "single": "7598589372382920626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6977263604496227082": {
            "length": 44,
            "waveforms": {
                "single": "6977263604496227082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1216587501315498516": {
            "length": 48,
            "waveforms": {
                "single": "-1216587501315498516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3541145583402334969": {
            "length": 48,
            "waveforms": {
                "single": "-3541145583402334969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3417185196296699781": {
            "length": 48,
            "waveforms": {
                "single": "-3417185196296699781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7362203820891301466": {
            "length": 48,
            "waveforms": {
                "single": "7362203820891301466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6214382003714432693": {
            "length": 52,
            "waveforms": {
                "single": "6214382003714432693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-997931449094817670": {
            "length": 52,
            "waveforms": {
                "single": "-997931449094817670",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4111317980826311488": {
            "length": 52,
            "waveforms": {
                "single": "4111317980826311488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8633635750916314804": {
            "length": 52,
            "waveforms": {
                "single": "8633635750916314804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3432076688589603693": {
            "length": 56,
            "waveforms": {
                "single": "-3432076688589603693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7615348634790069949": {
            "length": 56,
            "waveforms": {
                "single": "-7615348634790069949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7393854575591354701": {
            "length": 56,
            "waveforms": {
                "single": "-7393854575591354701",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2382138817763305603": {
            "length": 56,
            "waveforms": {
                "single": "-2382138817763305603",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2160644758564590355": {
            "length": 60,
            "waveforms": {
                "single": "-2160644758564590355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3642383013566018016": {
            "length": 60,
            "waveforms": {
                "single": "-3642383013566018016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "37114929438576508": {
            "length": 60,
            "waveforms": {
                "single": "37114929438576508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "258608988637291756": {
            "length": 60,
            "waveforms": {
                "single": "258608988637291756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1775704542169515971": {
            "length": 64,
            "waveforms": {
                "single": "-1775704542169515971",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3788586491463913193": {
            "length": 64,
            "waveforms": {
                "single": "3788586491463913193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6452628293018646644": {
            "length": 64,
            "waveforms": {
                "single": "-6452628293018646644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "643549205032366140": {
            "length": 64,
            "waveforms": {
                "single": "643549205032366140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6949993673799705000": {
            "length": 68,
            "waveforms": {
                "single": "-6949993673799705000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2828830694231339086": {
            "length": 68,
            "waveforms": {
                "single": "-2828830694231339086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "488943224273238783": {
            "length": 68,
            "waveforms": {
                "single": "488943224273238783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1914981135057379478": {
            "length": 68,
            "waveforms": {
                "single": "1914981135057379478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5722153041300003129": {
            "length": 72,
            "waveforms": {
                "single": "5722153041300003129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1945202015221547240": {
            "length": 72,
            "waveforms": {
                "single": "-1945202015221547240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7919912729303169992": {
            "length": 72,
            "waveforms": {
                "single": "7919912729303169992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4574762087399843674": {
            "length": 72,
            "waveforms": {
                "single": "-4574762087399843674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5293621527379617278": {
            "length": 76,
            "waveforms": {
                "single": "-5293621527379617278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5072127468180902030": {
            "length": 76,
            "waveforms": {
                "single": "-5072127468180902030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5349321871596904244": {
            "length": 76,
            "waveforms": {
                "single": "-5349321871596904244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2874367780177735167": {
            "length": 76,
            "waveforms": {
                "single": "-2874367780177735167",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3077701476828802783": {
            "length": 80,
            "waveforms": {
                "single": "3077701476828802783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2358842036849029179": {
            "length": 80,
            "waveforms": {
                "single": "2358842036849029179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5275461164831969646": {
            "length": 80,
            "waveforms": {
                "single": "5275461164831969646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7214017706243396228_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7214017706243396228_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4627626324609100052_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4627626324609100052_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9015628126969995137": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-1052249854807244050_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-1052249854807244050_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1165117755933466191_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1165117755933466191_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8648965138787578654": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6903055487712810610": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6681561428514095362": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1669845670686046264": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1647928247818531605": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1370733844402529391": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "749408076515835847": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8954937365742827626": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3334945987892111496": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "594802095756708490": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5025189282094007640": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1218017375851383989": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5522554662875065996": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "979742312151782874": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1201236371350498122": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6212952129178547220": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6434446188377262468": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4825033970137805680": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8632205876380429331": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8853699935579144579": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-182970997317989811": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7395284450127240174": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2857608517770585844": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2162074633100475828": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8090818334797350190": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7469492566910656646": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "5987754311909228985": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7936671991710319315": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8557997759597012859": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2703462174683554969": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6360238071593845996": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-505702486680388106": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-284208427481672858": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7921320861745318921": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1913551260521494005": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5720723166764117656": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7146761077548258351": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3094453706934301486": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-4576191961935729147": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8880729248959411154": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-675199959732419375": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5179335625181038515": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1522559728270747488": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8495789032564336770": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7598589372382920626": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6977263604496227082": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-1216587501315498516": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3541145583402334969": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3417185196296699781": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7362203820891301466": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6214382003714432693": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-997931449094817670": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4111317980826311488": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8633635750916314804": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3432076688589603693": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7615348634790069949": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7393854575591354701": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2382138817763305603": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-2160644758564590355": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3642383013566018016": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "37114929438576508": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "258608988637291756": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-1775704542169515971": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3788586491463913193": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6452628293018646644": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "643549205032366140": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6949993673799705000": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2828830694231339086": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "488943224273238783": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1914981135057379478": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "5722153041300003129": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1945202015221547240": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7919912729303169992": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4574762087399843674": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5293621527379617278": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5072127468180902030": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5349321871596904244": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2874367780177735167": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "3077701476828802783": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2358842036849029179": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5275461164831969646": {
            "samples": [0.06206030150753769] * 79 + [0.0],
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B2/drive_mixer_9ff": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_fc3": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_20d": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_1bb": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

