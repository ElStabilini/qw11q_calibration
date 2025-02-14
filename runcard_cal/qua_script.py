
# Single QUA script generated at 2025-02-14 09:40:42.909928
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
        with for_(v8,0,(v8<=79),(v8+1)):
            with for_(v9,-1.99,(v9<-1.7503877551020408),(v9+0.00812244897959169)):
                align()
                play("-3619686294738309927", "B2/drive")
                play("2491382538306363651", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-1034656448431198002"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("5346375185772435117"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-8578051117847113183"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("4526488665986407015"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-2254374676905204400"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("6617807115797448455"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-1049547940724101914"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("8815566803800615318"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("-1869434460510130016"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("7002747332192522839"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("7224241391391238087"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("549819286691752095"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-9024742994315146666"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("8800675311507711406"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-3791533177288382320"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("7980788791721683304"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-1593773489285215457"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-1372279430086500209"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("6833249859140491570"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-2192165949872528311"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-5387351445720231323"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("6058690074943431000"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("3706324406181136780"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-3961030650340413589"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-8588089076369065342"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-4780917170126441691"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-7309450162498483627"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-7087956103299768379"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("2703346463535469624"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-3509485240101428353"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("2871546394102204766"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-2304658503920325867"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("5069306082105371629"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-4505256198901527132"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("4142978324127218104"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("5126311001109605342"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("6340738012130384967"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-5724974427375533530"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("7545564748311487453"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("4749412599721007736"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("6725678228525459351"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("6947172287724174599"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-646370591107896541"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-3248715761169417706"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-9080318038783494906"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-4068602280955445808"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-3847108221756730560"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("5025073570945922295"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-5216141213536637542"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("2157823372489059954"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("3583861283273200649"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("1231495614510906429"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("2214828291493293667"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("3429255302514073292"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-2190736075336642838"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("8662465119540837638"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("8883959178739552886"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-7586519266165547115"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-7365025206966831867"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("2887867760930994151"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("-4779487295590556218"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("7659487176895170482"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("-6980084990571757483"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("-6758590931373042235"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("2651482209439374991"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-4560831243369875372"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-5708653060546744145"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("5070735956641257102"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("5292230015839972350"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("-8142798300041530168"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("8822207518666593787"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("1943810503681902312"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("-5723544552839648057"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("3148637239863004798"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("4363064250883784423"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("8170236157126408074"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("2550244779275691944"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-644940716572011068"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("4748004467278858807"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("-5493210317203701030"*amp(v9), "B4/flux")
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
                play("2491382538306363651", "B4/drive")
                measure("-4567785583615994549", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7301161584051474)-(v3*0.6833230533471776))>0.002634776715916271)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-6931477253142932187", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.4852100881460357)-(v6*0.8743976042746894))>-0.0004963015755993342)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(30).buffer(80).average().save("-4567785583615994549_B2|acquisition_shots")
        r2.buffer(30).buffer(80).average().save("-6931477253142932187_B4|acquisition_shots")


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
                "3688628427027057900": "3688628427027057900",
                "-4067172406419560335": "-4067172406419560335",
                "-1034656448431198002": "-1034656448431198002",
                "5346375185772435117": "5346375185772435117",
                "-8578051117847113183": "-8578051117847113183",
                "4526488665986407015": "4526488665986407015",
                "-2254374676905204400": "-2254374676905204400",
                "6617807115797448455": "6617807115797448455",
                "-1049547940724101914": "-1049547940724101914",
                "8815566803800615318": "8815566803800615318",
                "-1869434460510130016": "-1869434460510130016",
                "7002747332192522839": "7002747332192522839",
                "7224241391391238087": "7224241391391238087",
                "549819286691752095": "549819286691752095",
                "-9024742994315146666": "-9024742994315146666",
                "8800675311507711406": "8800675311507711406",
                "-3791533177288382320": "-3791533177288382320",
                "7980788791721683304": "7980788791721683304",
                "-1593773489285215457": "-1593773489285215457",
                "-1372279430086500209": "-1372279430086500209",
                "6833249859140491570": "6833249859140491570",
                "-2192165949872528311": "-2192165949872528311",
                "-5387351445720231323": "-5387351445720231323",
                "6058690074943431000": "6058690074943431000",
                "3706324406181136780": "3706324406181136780",
                "-3961030650340413589": "-3961030650340413589",
                "-8588089076369065342": "-8588089076369065342",
                "-4780917170126441691": "-4780917170126441691",
                "-7309450162498483627": "-7309450162498483627",
                "-7087956103299768379": "-7087956103299768379",
                "2703346463535469624": "2703346463535469624",
                "-3509485240101428353": "-3509485240101428353",
                "2871546394102204766": "2871546394102204766",
                "-2304658503920325867": "-2304658503920325867",
                "5069306082105371629": "5069306082105371629",
                "-4505256198901527132": "-4505256198901527132",
                "4142978324127218104": "4142978324127218104",
                "5126311001109605342": "5126311001109605342",
                "6340738012130384967": "6340738012130384967",
                "-5724974427375533530": "-5724974427375533530",
                "7545564748311487453": "7545564748311487453",
                "4749412599721007736": "4749412599721007736",
                "6725678228525459351": "6725678228525459351",
                "6947172287724174599": "6947172287724174599",
                "-646370591107896541": "-646370591107896541",
                "-3248715761169417706": "-3248715761169417706",
                "-9080318038783494906": "-9080318038783494906",
                "-4068602280955445808": "-4068602280955445808",
                "-3847108221756730560": "-3847108221756730560",
                "5025073570945922295": "5025073570945922295",
                "-5216141213536637542": "-5216141213536637542",
                "2157823372489059954": "2157823372489059954",
                "3583861283273200649": "3583861283273200649",
                "1231495614510906429": "1231495614510906429",
                "2214828291493293667": "2214828291493293667",
                "3429255302514073292": "3429255302514073292",
                "-2190736075336642838": "-2190736075336642838",
                "8662465119540837638": "8662465119540837638",
                "8883959178739552886": "8883959178739552886",
                "-7586519266165547115": "-7586519266165547115",
                "-7365025206966831867": "-7365025206966831867",
                "2887867760930994151": "2887867760930994151",
                "-4779487295590556218": "-4779487295590556218",
                "7659487176895170482": "7659487176895170482",
                "-6980084990571757483": "-6980084990571757483",
                "-6758590931373042235": "-6758590931373042235",
                "2651482209439374991": "2651482209439374991",
                "-4560831243369875372": "-4560831243369875372",
                "-5708653060546744145": "-5708653060546744145",
                "5070735956641257102": "5070735956641257102",
                "5292230015839972350": "5292230015839972350",
                "-8142798300041530168": "-8142798300041530168",
                "8822207518666593787": "8822207518666593787",
                "1943810503681902312": "1943810503681902312",
                "-5723544552839648057": "-5723544552839648057",
                "3148637239863004798": "3148637239863004798",
                "4363064250883784423": "4363064250883784423",
                "8170236157126408074": "8170236157126408074",
                "2550244779275691944": "2550244779275691944",
                "-644940716572011068": "-644940716572011068",
                "4748004467278858807": "4748004467278858807",
                "-5493210317203701030": "-5493210317203701030",
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
                "-6931477253142932187": "-6931477253142932187_B4/acquisition",
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
                "2491382538306363651": "2491382538306363651",
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
                "-3619686294738309927": "-3619686294738309927",
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
                "-4567785583615994549": "-4567785583615994549_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-3619686294738309927": {
            "length": 40,
            "waveforms": {
                "I": "-3619686294738309927_i",
                "Q": "-3619686294738309927_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2491382538306363651": {
            "length": 40,
            "waveforms": {
                "I": "2491382538306363651_i",
                "Q": "2491382538306363651_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3688628427027057900": {
            "length": 80,
            "waveforms": {
                "single": "3688628427027057900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4567785583615994549_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4569576002357912955_i",
                "Q": "-4569576002357912955_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6931477253142932187_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4161881944009471046_i",
                "Q": "-4161881944009471046_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4067172406419560335": {
            "length": 80,
            "waveforms": {
                "single": "-4067172406419560335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1034656448431198002": {
            "length": 16,
            "waveforms": {
                "single": "-1034656448431198002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5346375185772435117": {
            "length": 16,
            "waveforms": {
                "single": "5346375185772435117",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8578051117847113183": {
            "length": 16,
            "waveforms": {
                "single": "-8578051117847113183",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4526488665986407015": {
            "length": 16,
            "waveforms": {
                "single": "4526488665986407015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2254374676905204400": {
            "length": 16,
            "waveforms": {
                "single": "-2254374676905204400",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6617807115797448455": {
            "length": 16,
            "waveforms": {
                "single": "6617807115797448455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1049547940724101914": {
            "length": 16,
            "waveforms": {
                "single": "-1049547940724101914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8815566803800615318": {
            "length": 16,
            "waveforms": {
                "single": "8815566803800615318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1869434460510130016": {
            "length": 16,
            "waveforms": {
                "single": "-1869434460510130016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7002747332192522839": {
            "length": 16,
            "waveforms": {
                "single": "7002747332192522839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7224241391391238087": {
            "length": 16,
            "waveforms": {
                "single": "7224241391391238087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "549819286691752095": {
            "length": 16,
            "waveforms": {
                "single": "549819286691752095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9024742994315146666": {
            "length": 16,
            "waveforms": {
                "single": "-9024742994315146666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8800675311507711406": {
            "length": 16,
            "waveforms": {
                "single": "8800675311507711406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3791533177288382320": {
            "length": 16,
            "waveforms": {
                "single": "-3791533177288382320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7980788791721683304": {
            "length": 16,
            "waveforms": {
                "single": "7980788791721683304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1593773489285215457": {
            "length": 16,
            "waveforms": {
                "single": "-1593773489285215457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1372279430086500209": {
            "length": 20,
            "waveforms": {
                "single": "-1372279430086500209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6833249859140491570": {
            "length": 20,
            "waveforms": {
                "single": "6833249859140491570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2192165949872528311": {
            "length": 20,
            "waveforms": {
                "single": "-2192165949872528311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5387351445720231323": {
            "length": 20,
            "waveforms": {
                "single": "-5387351445720231323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6058690074943431000": {
            "length": 24,
            "waveforms": {
                "single": "6058690074943431000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3706324406181136780": {
            "length": 24,
            "waveforms": {
                "single": "3706324406181136780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3961030650340413589": {
            "length": 24,
            "waveforms": {
                "single": "-3961030650340413589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8588089076369065342": {
            "length": 24,
            "waveforms": {
                "single": "-8588089076369065342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4780917170126441691": {
            "length": 28,
            "waveforms": {
                "single": "-4780917170126441691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7309450162498483627": {
            "length": 28,
            "waveforms": {
                "single": "-7309450162498483627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7087956103299768379": {
            "length": 28,
            "waveforms": {
                "single": "-7087956103299768379",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2703346463535469624": {
            "length": 28,
            "waveforms": {
                "single": "2703346463535469624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3509485240101428353": {
            "length": 32,
            "waveforms": {
                "single": "-3509485240101428353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2871546394102204766": {
            "length": 32,
            "waveforms": {
                "single": "2871546394102204766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2304658503920325867": {
            "length": 32,
            "waveforms": {
                "single": "-2304658503920325867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5069306082105371629": {
            "length": 32,
            "waveforms": {
                "single": "5069306082105371629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4505256198901527132": {
            "length": 36,
            "waveforms": {
                "single": "-4505256198901527132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4142978324127218104": {
            "length": 36,
            "waveforms": {
                "single": "4142978324127218104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5126311001109605342": {
            "length": 36,
            "waveforms": {
                "single": "5126311001109605342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6340738012130384967": {
            "length": 36,
            "waveforms": {
                "single": "6340738012130384967",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5724974427375533530": {
            "length": 40,
            "waveforms": {
                "single": "-5724974427375533530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7545564748311487453": {
            "length": 40,
            "waveforms": {
                "single": "7545564748311487453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4749412599721007736": {
            "length": 40,
            "waveforms": {
                "single": "4749412599721007736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6725678228525459351": {
            "length": 40,
            "waveforms": {
                "single": "6725678228525459351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6947172287724174599": {
            "length": 44,
            "waveforms": {
                "single": "6947172287724174599",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-646370591107896541": {
            "length": 44,
            "waveforms": {
                "single": "-646370591107896541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3248715761169417706": {
            "length": 44,
            "waveforms": {
                "single": "-3248715761169417706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9080318038783494906": {
            "length": 44,
            "waveforms": {
                "single": "-9080318038783494906",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4068602280955445808": {
            "length": 48,
            "waveforms": {
                "single": "-4068602280955445808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3847108221756730560": {
            "length": 48,
            "waveforms": {
                "single": "-3847108221756730560",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5025073570945922295": {
            "length": 48,
            "waveforms": {
                "single": "5025073570945922295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5216141213536637542": {
            "length": 48,
            "waveforms": {
                "single": "-5216141213536637542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2157823372489059954": {
            "length": 52,
            "waveforms": {
                "single": "2157823372489059954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3583861283273200649": {
            "length": 52,
            "waveforms": {
                "single": "3583861283273200649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1231495614510906429": {
            "length": 52,
            "waveforms": {
                "single": "1231495614510906429",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2214828291493293667": {
            "length": 52,
            "waveforms": {
                "single": "2214828291493293667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3429255302514073292": {
            "length": 56,
            "waveforms": {
                "single": "3429255302514073292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2190736075336642838": {
            "length": 56,
            "waveforms": {
                "single": "-2190736075336642838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8662465119540837638": {
            "length": 56,
            "waveforms": {
                "single": "8662465119540837638",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8883959178739552886": {
            "length": 56,
            "waveforms": {
                "single": "8883959178739552886",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7586519266165547115": {
            "length": 60,
            "waveforms": {
                "single": "-7586519266165547115",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7365025206966831867": {
            "length": 60,
            "waveforms": {
                "single": "-7365025206966831867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2887867760930994151": {
            "length": 60,
            "waveforms": {
                "single": "2887867760930994151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4779487295590556218": {
            "length": 60,
            "waveforms": {
                "single": "-4779487295590556218",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7659487176895170482": {
            "length": 64,
            "waveforms": {
                "single": "7659487176895170482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6980084990571757483": {
            "length": 64,
            "waveforms": {
                "single": "-6980084990571757483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6758590931373042235": {
            "length": 64,
            "waveforms": {
                "single": "-6758590931373042235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2651482209439374991": {
            "length": 64,
            "waveforms": {
                "single": "2651482209439374991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4560831243369875372": {
            "length": 68,
            "waveforms": {
                "single": "-4560831243369875372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5708653060546744145": {
            "length": 68,
            "waveforms": {
                "single": "-5708653060546744145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5070735956641257102": {
            "length": 68,
            "waveforms": {
                "single": "5070735956641257102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5292230015839972350": {
            "length": 68,
            "waveforms": {
                "single": "5292230015839972350",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8142798300041530168": {
            "length": 72,
            "waveforms": {
                "single": "-8142798300041530168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8822207518666593787": {
            "length": 72,
            "waveforms": {
                "single": "8822207518666593787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1943810503681902312": {
            "length": 72,
            "waveforms": {
                "single": "1943810503681902312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5723544552839648057": {
            "length": 72,
            "waveforms": {
                "single": "-5723544552839648057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3148637239863004798": {
            "length": 76,
            "waveforms": {
                "single": "3148637239863004798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4363064250883784423": {
            "length": 76,
            "waveforms": {
                "single": "4363064250883784423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8170236157126408074": {
            "length": 76,
            "waveforms": {
                "single": "8170236157126408074",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2550244779275691944": {
            "length": 76,
            "waveforms": {
                "single": "2550244779275691944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-644940716572011068": {
            "length": 80,
            "waveforms": {
                "single": "-644940716572011068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4748004467278858807": {
            "length": 80,
            "waveforms": {
                "single": "4748004467278858807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5493210317203701030": {
            "length": 80,
            "waveforms": {
                "single": "-5493210317203701030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-3619686294738309927_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-3619686294738309927_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "2491382538306363651_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "2491382538306363651_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "3688628427027057900": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-4569576002357912955_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4569576002357912955_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4161881944009471046_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-4161881944009471046_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4067172406419560335": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1034656448431198002": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5346375185772435117": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-8578051117847113183": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4526488665986407015": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-2254374676905204400": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "6617807115797448455": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-1049547940724101914": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8815566803800615318": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-1869434460510130016": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "7002747332192522839": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "7224241391391238087": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "549819286691752095": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-9024742994315146666": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "8800675311507711406": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3791533177288382320": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7980788791721683304": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-1593773489285215457": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1372279430086500209": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6833249859140491570": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2192165949872528311": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5387351445720231323": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6058690074943431000": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3706324406181136780": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3961030650340413589": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8588089076369065342": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4780917170126441691": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7309450162498483627": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7087956103299768379": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2703346463535469624": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3509485240101428353": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2871546394102204766": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2304658503920325867": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
        },
        "5069306082105371629": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4505256198901527132": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4142978324127218104": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5126311001109605342": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
        },
        "6340738012130384967": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5724974427375533530": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7545564748311487453": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4749412599721007736": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6725678228525459351": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6947172287724174599": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-646370591107896541": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3248715761169417706": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-9080318038783494906": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4068602280955445808": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3847108221756730560": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5025073570945922295": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-5216141213536637542": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2157823372489059954": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3583861283273200649": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1231495614510906429": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
        },
        "2214828291493293667": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3429255302514073292": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2190736075336642838": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8662465119540837638": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
        },
        "8883959178739552886": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-7586519266165547115": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7365025206966831867": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2887867760930994151": {
            "samples": [0.12311557788944723] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-4779487295590556218": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7659487176895170482": {
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6980084990571757483": {
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6758590931373042235": {
            "samples": [0.12311557788944723] * 63 + [0.0],
            "type": "arbitrary",
        },
        "2651482209439374991": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4560831243369875372": {
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5708653060546744145": {
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5070735956641257102": {
            "samples": [0.12311557788944723] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5292230015839972350": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8142798300041530168": {
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8822207518666593787": {
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1943810503681902312": {
            "samples": [0.12311557788944723] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-5723544552839648057": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3148637239863004798": {
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4363064250883784423": {
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8170236157126408074": {
            "samples": [0.12311557788944723] * 75 + [0.0],
            "type": "arbitrary",
        },
        "2550244779275691944": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-644940716572011068": {
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4748004467278858807": {
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5493210317203701030": {
            "samples": [0.12311557788944723] * 79 + [0.0],
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
                "3688628427027057900": "3688628427027057900",
                "-4067172406419560335": "-4067172406419560335",
                "-1034656448431198002": "-1034656448431198002",
                "5346375185772435117": "5346375185772435117",
                "-8578051117847113183": "-8578051117847113183",
                "4526488665986407015": "4526488665986407015",
                "-2254374676905204400": "-2254374676905204400",
                "6617807115797448455": "6617807115797448455",
                "-1049547940724101914": "-1049547940724101914",
                "8815566803800615318": "8815566803800615318",
                "-1869434460510130016": "-1869434460510130016",
                "7002747332192522839": "7002747332192522839",
                "7224241391391238087": "7224241391391238087",
                "549819286691752095": "549819286691752095",
                "-9024742994315146666": "-9024742994315146666",
                "8800675311507711406": "8800675311507711406",
                "-3791533177288382320": "-3791533177288382320",
                "7980788791721683304": "7980788791721683304",
                "-1593773489285215457": "-1593773489285215457",
                "-1372279430086500209": "-1372279430086500209",
                "6833249859140491570": "6833249859140491570",
                "-2192165949872528311": "-2192165949872528311",
                "-5387351445720231323": "-5387351445720231323",
                "6058690074943431000": "6058690074943431000",
                "3706324406181136780": "3706324406181136780",
                "-3961030650340413589": "-3961030650340413589",
                "-8588089076369065342": "-8588089076369065342",
                "-4780917170126441691": "-4780917170126441691",
                "-7309450162498483627": "-7309450162498483627",
                "-7087956103299768379": "-7087956103299768379",
                "2703346463535469624": "2703346463535469624",
                "-3509485240101428353": "-3509485240101428353",
                "2871546394102204766": "2871546394102204766",
                "-2304658503920325867": "-2304658503920325867",
                "5069306082105371629": "5069306082105371629",
                "-4505256198901527132": "-4505256198901527132",
                "4142978324127218104": "4142978324127218104",
                "5126311001109605342": "5126311001109605342",
                "6340738012130384967": "6340738012130384967",
                "-5724974427375533530": "-5724974427375533530",
                "7545564748311487453": "7545564748311487453",
                "4749412599721007736": "4749412599721007736",
                "6725678228525459351": "6725678228525459351",
                "6947172287724174599": "6947172287724174599",
                "-646370591107896541": "-646370591107896541",
                "-3248715761169417706": "-3248715761169417706",
                "-9080318038783494906": "-9080318038783494906",
                "-4068602280955445808": "-4068602280955445808",
                "-3847108221756730560": "-3847108221756730560",
                "5025073570945922295": "5025073570945922295",
                "-5216141213536637542": "-5216141213536637542",
                "2157823372489059954": "2157823372489059954",
                "3583861283273200649": "3583861283273200649",
                "1231495614510906429": "1231495614510906429",
                "2214828291493293667": "2214828291493293667",
                "3429255302514073292": "3429255302514073292",
                "-2190736075336642838": "-2190736075336642838",
                "8662465119540837638": "8662465119540837638",
                "8883959178739552886": "8883959178739552886",
                "-7586519266165547115": "-7586519266165547115",
                "-7365025206966831867": "-7365025206966831867",
                "2887867760930994151": "2887867760930994151",
                "-4779487295590556218": "-4779487295590556218",
                "7659487176895170482": "7659487176895170482",
                "-6980084990571757483": "-6980084990571757483",
                "-6758590931373042235": "-6758590931373042235",
                "2651482209439374991": "2651482209439374991",
                "-4560831243369875372": "-4560831243369875372",
                "-5708653060546744145": "-5708653060546744145",
                "5070735956641257102": "5070735956641257102",
                "5292230015839972350": "5292230015839972350",
                "-8142798300041530168": "-8142798300041530168",
                "8822207518666593787": "8822207518666593787",
                "1943810503681902312": "1943810503681902312",
                "-5723544552839648057": "-5723544552839648057",
                "3148637239863004798": "3148637239863004798",
                "4363064250883784423": "4363064250883784423",
                "8170236157126408074": "8170236157126408074",
                "2550244779275691944": "2550244779275691944",
                "-644940716572011068": "-644940716572011068",
                "4748004467278858807": "4748004467278858807",
                "-5493210317203701030": "-5493210317203701030",
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
                "-6931477253142932187": "-6931477253142932187_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_1f6",
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
                "2491382538306363651": "2491382538306363651",
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
                "mixer": "B4/drive_mixer_2b0",
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
                "-3619686294738309927": "-3619686294738309927",
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
                "mixer": "B2/drive_mixer_fe8",
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
                "-4567785583615994549": "-4567785583615994549_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_ac5",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "-3619686294738309927": {
            "length": 40,
            "waveforms": {
                "I": "-3619686294738309927_i",
                "Q": "-3619686294738309927_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2491382538306363651": {
            "length": 40,
            "waveforms": {
                "I": "2491382538306363651_i",
                "Q": "2491382538306363651_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3688628427027057900": {
            "length": 80,
            "waveforms": {
                "single": "3688628427027057900",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4567785583615994549_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4569576002357912955_i",
                "Q": "-4569576002357912955_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6931477253142932187_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4161881944009471046_i",
                "Q": "-4161881944009471046_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4067172406419560335": {
            "length": 80,
            "waveforms": {
                "single": "-4067172406419560335",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1034656448431198002": {
            "length": 16,
            "waveforms": {
                "single": "-1034656448431198002",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5346375185772435117": {
            "length": 16,
            "waveforms": {
                "single": "5346375185772435117",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8578051117847113183": {
            "length": 16,
            "waveforms": {
                "single": "-8578051117847113183",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4526488665986407015": {
            "length": 16,
            "waveforms": {
                "single": "4526488665986407015",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2254374676905204400": {
            "length": 16,
            "waveforms": {
                "single": "-2254374676905204400",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6617807115797448455": {
            "length": 16,
            "waveforms": {
                "single": "6617807115797448455",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1049547940724101914": {
            "length": 16,
            "waveforms": {
                "single": "-1049547940724101914",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8815566803800615318": {
            "length": 16,
            "waveforms": {
                "single": "8815566803800615318",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1869434460510130016": {
            "length": 16,
            "waveforms": {
                "single": "-1869434460510130016",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7002747332192522839": {
            "length": 16,
            "waveforms": {
                "single": "7002747332192522839",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7224241391391238087": {
            "length": 16,
            "waveforms": {
                "single": "7224241391391238087",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "549819286691752095": {
            "length": 16,
            "waveforms": {
                "single": "549819286691752095",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9024742994315146666": {
            "length": 16,
            "waveforms": {
                "single": "-9024742994315146666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8800675311507711406": {
            "length": 16,
            "waveforms": {
                "single": "8800675311507711406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3791533177288382320": {
            "length": 16,
            "waveforms": {
                "single": "-3791533177288382320",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7980788791721683304": {
            "length": 16,
            "waveforms": {
                "single": "7980788791721683304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1593773489285215457": {
            "length": 16,
            "waveforms": {
                "single": "-1593773489285215457",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1372279430086500209": {
            "length": 20,
            "waveforms": {
                "single": "-1372279430086500209",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6833249859140491570": {
            "length": 20,
            "waveforms": {
                "single": "6833249859140491570",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2192165949872528311": {
            "length": 20,
            "waveforms": {
                "single": "-2192165949872528311",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5387351445720231323": {
            "length": 20,
            "waveforms": {
                "single": "-5387351445720231323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6058690074943431000": {
            "length": 24,
            "waveforms": {
                "single": "6058690074943431000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3706324406181136780": {
            "length": 24,
            "waveforms": {
                "single": "3706324406181136780",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3961030650340413589": {
            "length": 24,
            "waveforms": {
                "single": "-3961030650340413589",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8588089076369065342": {
            "length": 24,
            "waveforms": {
                "single": "-8588089076369065342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4780917170126441691": {
            "length": 28,
            "waveforms": {
                "single": "-4780917170126441691",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7309450162498483627": {
            "length": 28,
            "waveforms": {
                "single": "-7309450162498483627",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7087956103299768379": {
            "length": 28,
            "waveforms": {
                "single": "-7087956103299768379",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2703346463535469624": {
            "length": 28,
            "waveforms": {
                "single": "2703346463535469624",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3509485240101428353": {
            "length": 32,
            "waveforms": {
                "single": "-3509485240101428353",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2871546394102204766": {
            "length": 32,
            "waveforms": {
                "single": "2871546394102204766",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2304658503920325867": {
            "length": 32,
            "waveforms": {
                "single": "-2304658503920325867",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5069306082105371629": {
            "length": 32,
            "waveforms": {
                "single": "5069306082105371629",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4505256198901527132": {
            "length": 36,
            "waveforms": {
                "single": "-4505256198901527132",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4142978324127218104": {
            "length": 36,
            "waveforms": {
                "single": "4142978324127218104",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5126311001109605342": {
            "length": 36,
            "waveforms": {
                "single": "5126311001109605342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6340738012130384967": {
            "length": 36,
            "waveforms": {
                "single": "6340738012130384967",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5724974427375533530": {
            "length": 40,
            "waveforms": {
                "single": "-5724974427375533530",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7545564748311487453": {
            "length": 40,
            "waveforms": {
                "single": "7545564748311487453",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4749412599721007736": {
            "length": 40,
            "waveforms": {
                "single": "4749412599721007736",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6725678228525459351": {
            "length": 40,
            "waveforms": {
                "single": "6725678228525459351",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6947172287724174599": {
            "length": 44,
            "waveforms": {
                "single": "6947172287724174599",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-646370591107896541": {
            "length": 44,
            "waveforms": {
                "single": "-646370591107896541",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3248715761169417706": {
            "length": 44,
            "waveforms": {
                "single": "-3248715761169417706",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9080318038783494906": {
            "length": 44,
            "waveforms": {
                "single": "-9080318038783494906",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4068602280955445808": {
            "length": 48,
            "waveforms": {
                "single": "-4068602280955445808",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3847108221756730560": {
            "length": 48,
            "waveforms": {
                "single": "-3847108221756730560",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5025073570945922295": {
            "length": 48,
            "waveforms": {
                "single": "5025073570945922295",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5216141213536637542": {
            "length": 48,
            "waveforms": {
                "single": "-5216141213536637542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2157823372489059954": {
            "length": 52,
            "waveforms": {
                "single": "2157823372489059954",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3583861283273200649": {
            "length": 52,
            "waveforms": {
                "single": "3583861283273200649",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1231495614510906429": {
            "length": 52,
            "waveforms": {
                "single": "1231495614510906429",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2214828291493293667": {
            "length": 52,
            "waveforms": {
                "single": "2214828291493293667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3429255302514073292": {
            "length": 56,
            "waveforms": {
                "single": "3429255302514073292",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2190736075336642838": {
            "length": 56,
            "waveforms": {
                "single": "-2190736075336642838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8662465119540837638": {
            "length": 56,
            "waveforms": {
                "single": "8662465119540837638",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8883959178739552886": {
            "length": 56,
            "waveforms": {
                "single": "8883959178739552886",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7586519266165547115": {
            "length": 60,
            "waveforms": {
                "single": "-7586519266165547115",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7365025206966831867": {
            "length": 60,
            "waveforms": {
                "single": "-7365025206966831867",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2887867760930994151": {
            "length": 60,
            "waveforms": {
                "single": "2887867760930994151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4779487295590556218": {
            "length": 60,
            "waveforms": {
                "single": "-4779487295590556218",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7659487176895170482": {
            "length": 64,
            "waveforms": {
                "single": "7659487176895170482",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6980084990571757483": {
            "length": 64,
            "waveforms": {
                "single": "-6980084990571757483",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6758590931373042235": {
            "length": 64,
            "waveforms": {
                "single": "-6758590931373042235",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2651482209439374991": {
            "length": 64,
            "waveforms": {
                "single": "2651482209439374991",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4560831243369875372": {
            "length": 68,
            "waveforms": {
                "single": "-4560831243369875372",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5708653060546744145": {
            "length": 68,
            "waveforms": {
                "single": "-5708653060546744145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5070735956641257102": {
            "length": 68,
            "waveforms": {
                "single": "5070735956641257102",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5292230015839972350": {
            "length": 68,
            "waveforms": {
                "single": "5292230015839972350",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8142798300041530168": {
            "length": 72,
            "waveforms": {
                "single": "-8142798300041530168",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8822207518666593787": {
            "length": 72,
            "waveforms": {
                "single": "8822207518666593787",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1943810503681902312": {
            "length": 72,
            "waveforms": {
                "single": "1943810503681902312",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5723544552839648057": {
            "length": 72,
            "waveforms": {
                "single": "-5723544552839648057",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3148637239863004798": {
            "length": 76,
            "waveforms": {
                "single": "3148637239863004798",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4363064250883784423": {
            "length": 76,
            "waveforms": {
                "single": "4363064250883784423",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8170236157126408074": {
            "length": 76,
            "waveforms": {
                "single": "8170236157126408074",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2550244779275691944": {
            "length": 76,
            "waveforms": {
                "single": "2550244779275691944",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-644940716572011068": {
            "length": 80,
            "waveforms": {
                "single": "-644940716572011068",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4748004467278858807": {
            "length": 80,
            "waveforms": {
                "single": "4748004467278858807",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5493210317203701030": {
            "length": 80,
            "waveforms": {
                "single": "-5493210317203701030",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-3619686294738309927_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3619686294738309927_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2491382538306363651_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2491382538306363651_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3688628427027057900": {
            "type": "constant",
            "sample": -0.2388,
        },
        "-4569576002357912955_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-4569576002357912955_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4161881944009471046_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-4161881944009471046_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4067172406419560335": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1034656448431198002": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5346375185772435117": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8578051117847113183": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4526488665986407015": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2254374676905204400": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6617807115797448455": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1049547940724101914": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8815566803800615318": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1869434460510130016": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7002747332192522839": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7224241391391238087": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "549819286691752095": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9024742994315146666": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8800675311507711406": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3791533177288382320": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7980788791721683304": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1593773489285215457": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1372279430086500209": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6833249859140491570": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2192165949872528311": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5387351445720231323": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6058690074943431000": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3706324406181136780": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3961030650340413589": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8588089076369065342": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4780917170126441691": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7309450162498483627": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7087956103299768379": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2703346463535469624": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-3509485240101428353": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2871546394102204766": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2304658503920325867": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5069306082105371629": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4505256198901527132": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4142978324127218104": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5126311001109605342": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6340738012130384967": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-5724974427375533530": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7545564748311487453": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4749412599721007736": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6725678228525459351": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6947172287724174599": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-646370591107896541": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3248715761169417706": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9080318038783494906": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4068602280955445808": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3847108221756730560": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5025073570945922295": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5216141213536637542": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2157823372489059954": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3583861283273200649": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1231495614510906429": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2214828291493293667": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3429255302514073292": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2190736075336642838": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8662465119540837638": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8883959178739552886": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-7586519266165547115": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7365025206966831867": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2887867760930994151": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4779487295590556218": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "7659487176895170482": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6980084990571757483": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6758590931373042235": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2651482209439374991": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4560831243369875372": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5708653060546744145": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5070735956641257102": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5292230015839972350": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-8142798300041530168": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8822207518666593787": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1943810503681902312": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5723544552839648057": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3148637239863004798": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4363064250883784423": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8170236157126408074": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2550244779275691944": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-644940716572011068": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4748004467278858807": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5493210317203701030": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 79 + [0.0],
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
        "B4/acquisition_mixer_1f6": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_2b0": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_fe8": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_ac5": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

