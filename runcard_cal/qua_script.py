
# Single QUA script generated at 2025-02-07 14:26:17.668647
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
        with for_(v8,0,(v8<=99),(v8+1)):
            with for_(v9,-1.99,(v9<-1.4228499999999995),(v9+0.002842857142857147)):
                align()
                play("1292839950968877500", "B2/drive")
                play("8784619959208724241", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-5019204591206069852"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-4797710532007354604"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-4086818485070593574"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-3592883795826252118"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-1046238969982017919"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("2633258973022576605"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("2854753032221291853"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-6719809248785606908"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("4059579768402394339"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-3856484249434646547"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("3239693248616366237"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("887327579854072017"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("932654315443039549"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-11192591448623741"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("8860989201254029114"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("8318297084884003226"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("8539791144082718474"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("8262596740666716260"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-1978618043815843577"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-1933291308226876045"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-2475983424596901933"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-2753177828012904147"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-278223736593735070"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("5673845520412802880"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("8815452115307633033"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("7871605208415969743"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-6052821095203578557"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("7374239827634911387"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-5120434989068102279"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("4744679755456614953"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-2922675301064935416"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("1599642469025067900"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6067712587496482469"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-8596245579868524405"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-8697272659674778903"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("4729788263163711041"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-9194638040455837259"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-989108751228845480"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-1266303154644847694"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-1044809095446132446"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-1763668535425906050"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("-1542174476227190802"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("4960122498799658068"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("6386160409583798763"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-8253411757883129202"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("3241123123152251710"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("6231554428824671406"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-5834158010681247091"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-1311840240591243775"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("3797409189329885383"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-2210360411893939533"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-4562726080656233753"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("6119129264438687434"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("6340623323637402682"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("4016065241550566229"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-4177785864261159369"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-3956291805062444121"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-276793862057849597"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-55299802859134349"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("3253183640768771840"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("3474677699967487088"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("3696171759166202336"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("7375669702170796860"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("5893931447169369199"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("-7541096868712133319"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-2921245426529049943"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-2797285039423414755"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("-5121843121510251208"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("-7474208790272545428"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("4509724078500881266"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("2157358409738587046"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("7550303593589456921"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("6928977825702763377"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("178254773956101029"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("-3188276571674161272"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("2376014461959267892"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-3243976915891448238"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("4961552373335543541"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("5085512760441178729"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("4464186992554485185"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("2982448737553057524"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("-6054222195344076866"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("-5832728136145361618"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("-1310410366055358302"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("-3634968448142194755"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("2219567136771263135"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("1598241368884569591"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("1819735428083284839"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("4638820883973145246"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("4017495116086451702"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("-4176355989725273896"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("-9196039140596335568"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("-6279420012613395101"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("-6155459625507759913"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("-6776785393394453457"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("3476107574503372561"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("1151549492416536108"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("5673867262506539424"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("5895361321705254672"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("-8744210845761673293"*amp(v9), "B4/flux")
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
                play("8784619959208724241", "B4/drive")
                measure("5931209932826119817", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.06078547221045674)-(v3*0.9981508535127102))>0.0025565952953590303)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-1322718175353050215", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.6665903597333165)-(v6*0.7454242364657911))>-0.0004342766968863211)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(200).buffer(100).average().save("5931209932826119817_B2|acquisition_shots")
        r2.buffer(200).buffer(100).average().save("-1322718175353050215_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.25498290735703955,
                    "filter": {
                        "feedforward": [1.0732888182245781, -0.9737209520873108, -0.0005203790392933598, -0.0005149944373311913, -0.002105044281710212, -0.003388157787203089, -0.0027995218244958146, 0.0029055980790707184, -0.002492824987361109, 0.0018688320586038787, 0.007669994237074814, 0.006431769668045485, 0.00019505700310456196, -0.001968630346827333, 0.002342580506761632, -0.007645763391517998, 0.0019060799407871365, -0.006897677857935084, 0.0054469947281882624, -0.012373869741610479, 0.010667355535212872],
                        "feedback": [0.9999990463256836, -0.9016765067668822],
                    },
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "filter": {
                        "feedforward": [1.082216163036566, -1.013483744074572, -0.0005934150341553434, -0.0005835327755912938, 0.007717830054774853, 0.003632375897519549, -0.00044011698253741335, 0.001605758501608272, -0.012449189070277502, -0.007236945254569601, 0.00976822190693331, 0.005697927299491748, 0.004773147069343227, -0.002901494501723682, -0.0017290035617877402, -0.001732703182405211, -0.004127059088728484, 0.006652439702682195, -0.0018491032089883812, -0.005021633883561784, 0.003839210780199868],
                        "feedback": [0.9999990463256836, -0.9262251003261055],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.0864486524147088, -1.0114796931248773, -0.00016385035736341804, -0.0001631375856683214, 0.0007132004480542389, -0.005469433104324626, -0.0031203713793950478, 0.0020985293007232484, -0.005440448977252687, 0.0029103915350147547, 0.006805519982961323, 0.007363572786123743, -0.0038086062520665135, -0.003181071276233404, 0.0005943072751533468, -0.003554727873357823, 0.0023584825716348456, -0.005872694192023741, 0.0012065363048726322, 0.0017448644372721935, 0.001253029817072768],
                        "feedback": [0.9999990463256836, -0.9287365023806654],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.1030496953566256, -1.0381134620821453, -0.0004260403462593258, -0.000420572662019365, 0.005570686385595049, -0.0020512683945509416, -0.0006392178405930675, -0.001996407788676792, 0.0004683735253229373, -0.003829742786740141, 0.0057195392567130805, 0.006959373393239386, -0.0034838926793923962, 0.0011703722958150697, -0.0027201873232208813, -0.004669494937616429, -0.0016907470696459624, -9.041142346012665e-05, 0.0001460934840622299, 0.002830673562819465, 0.0005694981868720677],
                        "feedback": [0.9999990463256836, -0.9336222939492675],
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "-7951085683972061690": "-7951085683972061690",
                "3694763626724053407": "3694763626724053407",
                "-5019204591206069852": "-5019204591206069852",
                "-4797710532007354604": "-4797710532007354604",
                "-4086818485070593574": "-4086818485070593574",
                "-3592883795826252118": "-3592883795826252118",
                "-1046238969982017919": "-1046238969982017919",
                "2633258973022576605": "2633258973022576605",
                "2854753032221291853": "2854753032221291853",
                "-6719809248785606908": "-6719809248785606908",
                "4059579768402394339": "4059579768402394339",
                "-3856484249434646547": "-3856484249434646547",
                "3239693248616366237": "3239693248616366237",
                "887327579854072017": "887327579854072017",
                "932654315443039549": "932654315443039549",
                "-11192591448623741": "-11192591448623741",
                "8860989201254029114": "8860989201254029114",
                "8318297084884003226": "8318297084884003226",
                "8539791144082718474": "8539791144082718474",
                "8262596740666716260": "8262596740666716260",
                "-1978618043815843577": "-1978618043815843577",
                "-1933291308226876045": "-1933291308226876045",
                "-2475983424596901933": "-2475983424596901933",
                "-2753177828012904147": "-2753177828012904147",
                "-278223736593735070": "-278223736593735070",
                "5673845520412802880": "5673845520412802880",
                "8815452115307633033": "8815452115307633033",
                "7871605208415969743": "7871605208415969743",
                "-6052821095203578557": "-6052821095203578557",
                "7374239827634911387": "7374239827634911387",
                "-5120434989068102279": "-5120434989068102279",
                "4744679755456614953": "4744679755456614953",
                "-2922675301064935416": "-2922675301064935416",
                "1599642469025067900": "1599642469025067900",
                "-6067712587496482469": "-6067712587496482469",
                "-8596245579868524405": "-8596245579868524405",
                "-8697272659674778903": "-8697272659674778903",
                "4729788263163711041": "4729788263163711041",
                "-9194638040455837259": "-9194638040455837259",
                "-989108751228845480": "-989108751228845480",
                "-1266303154644847694": "-1266303154644847694",
                "-1044809095446132446": "-1044809095446132446",
                "-1763668535425906050": "-1763668535425906050",
                "-1542174476227190802": "-1542174476227190802",
                "4960122498799658068": "4960122498799658068",
                "6386160409583798763": "6386160409583798763",
                "-8253411757883129202": "-8253411757883129202",
                "3241123123152251710": "3241123123152251710",
                "6231554428824671406": "6231554428824671406",
                "-5834158010681247091": "-5834158010681247091",
                "-1311840240591243775": "-1311840240591243775",
                "3797409189329885383": "3797409189329885383",
                "-2210360411893939533": "-2210360411893939533",
                "-4562726080656233753": "-4562726080656233753",
                "6119129264438687434": "6119129264438687434",
                "6340623323637402682": "6340623323637402682",
                "4016065241550566229": "4016065241550566229",
                "-4177785864261159369": "-4177785864261159369",
                "-3956291805062444121": "-3956291805062444121",
                "-276793862057849597": "-276793862057849597",
                "-55299802859134349": "-55299802859134349",
                "3253183640768771840": "3253183640768771840",
                "3474677699967487088": "3474677699967487088",
                "3696171759166202336": "3696171759166202336",
                "7375669702170796860": "7375669702170796860",
                "5893931447169369199": "5893931447169369199",
                "-7541096868712133319": "-7541096868712133319",
                "-2921245426529049943": "-2921245426529049943",
                "-2797285039423414755": "-2797285039423414755",
                "-5121843121510251208": "-5121843121510251208",
                "-7474208790272545428": "-7474208790272545428",
                "4509724078500881266": "4509724078500881266",
                "2157358409738587046": "2157358409738587046",
                "7550303593589456921": "7550303593589456921",
                "6928977825702763377": "6928977825702763377",
                "178254773956101029": "178254773956101029",
                "-3188276571674161272": "-3188276571674161272",
                "2376014461959267892": "2376014461959267892",
                "-3243976915891448238": "-3243976915891448238",
                "4961552373335543541": "4961552373335543541",
                "5085512760441178729": "5085512760441178729",
                "4464186992554485185": "4464186992554485185",
                "2982448737553057524": "2982448737553057524",
                "-6054222195344076866": "-6054222195344076866",
                "-5832728136145361618": "-5832728136145361618",
                "-1310410366055358302": "-1310410366055358302",
                "-3634968448142194755": "-3634968448142194755",
                "2219567136771263135": "2219567136771263135",
                "1598241368884569591": "1598241368884569591",
                "1819735428083284839": "1819735428083284839",
                "4638820883973145246": "4638820883973145246",
                "4017495116086451702": "4017495116086451702",
                "-4176355989725273896": "-4176355989725273896",
                "-9196039140596335568": "-9196039140596335568",
                "-6279420012613395101": "-6279420012613395101",
                "-6155459625507759913": "-6155459625507759913",
                "-6776785393394453457": "-6776785393394453457",
                "3476107574503372561": "3476107574503372561",
                "1151549492416536108": "1151549492416536108",
                "5673867262506539424": "5673867262506539424",
                "5895361321705254672": "5895361321705254672",
                "-8744210845761673293": "-8744210845761673293",
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
                "5931209932826119817": "5931209932826119817_B2/acquisition",
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
                "1292839950968877500": "1292839950968877500",
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
                "8784619959208724241": "8784619959208724241",
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
                "-1322718175353050215": "-1322718175353050215_B4/acquisition",
            },
        },
    },
    "pulses": {
        "1292839950968877500": {
            "length": 40,
            "waveforms": {
                "I": "1292839950968877500_i",
                "Q": "1292839950968877500_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8784619959208724241": {
            "length": 40,
            "waveforms": {
                "I": "8784619959208724241_i",
                "Q": "8784619959208724241_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7951085683972061690": {
            "length": 100,
            "waveforms": {
                "single": "-7951085683972061690",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5931209932826119817_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5719521543880685833_i",
                "Q": "5719521543880685833_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-1322718175353050215_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8701075330190137210_i",
                "Q": "8701075330190137210_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3694763626724053407": {
            "length": 100,
            "waveforms": {
                "single": "3694763626724053407",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5019204591206069852": {
            "length": 16,
            "waveforms": {
                "single": "-5019204591206069852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4797710532007354604": {
            "length": 16,
            "waveforms": {
                "single": "-4797710532007354604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4086818485070593574": {
            "length": 16,
            "waveforms": {
                "single": "-4086818485070593574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3592883795826252118": {
            "length": 16,
            "waveforms": {
                "single": "-3592883795826252118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1046238969982017919": {
            "length": 16,
            "waveforms": {
                "single": "-1046238969982017919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2633258973022576605": {
            "length": 16,
            "waveforms": {
                "single": "2633258973022576605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2854753032221291853": {
            "length": 16,
            "waveforms": {
                "single": "2854753032221291853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6719809248785606908": {
            "length": 16,
            "waveforms": {
                "single": "-6719809248785606908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4059579768402394339": {
            "length": 16,
            "waveforms": {
                "single": "4059579768402394339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3856484249434646547": {
            "length": 16,
            "waveforms": {
                "single": "-3856484249434646547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3239693248616366237": {
            "length": 16,
            "waveforms": {
                "single": "3239693248616366237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "887327579854072017": {
            "length": 16,
            "waveforms": {
                "single": "887327579854072017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "932654315443039549": {
            "length": 16,
            "waveforms": {
                "single": "932654315443039549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-11192591448623741": {
            "length": 16,
            "waveforms": {
                "single": "-11192591448623741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8860989201254029114": {
            "length": 16,
            "waveforms": {
                "single": "8860989201254029114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8318297084884003226": {
            "length": 16,
            "waveforms": {
                "single": "8318297084884003226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8539791144082718474": {
            "length": 16,
            "waveforms": {
                "single": "8539791144082718474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8262596740666716260": {
            "length": 20,
            "waveforms": {
                "single": "8262596740666716260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1978618043815843577": {
            "length": 20,
            "waveforms": {
                "single": "-1978618043815843577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1933291308226876045": {
            "length": 20,
            "waveforms": {
                "single": "-1933291308226876045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2475983424596901933": {
            "length": 20,
            "waveforms": {
                "single": "-2475983424596901933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2753177828012904147": {
            "length": 24,
            "waveforms": {
                "single": "-2753177828012904147",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-278223736593735070": {
            "length": 24,
            "waveforms": {
                "single": "-278223736593735070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5673845520412802880": {
            "length": 24,
            "waveforms": {
                "single": "5673845520412802880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8815452115307633033": {
            "length": 24,
            "waveforms": {
                "single": "8815452115307633033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7871605208415969743": {
            "length": 28,
            "waveforms": {
                "single": "7871605208415969743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6052821095203578557": {
            "length": 28,
            "waveforms": {
                "single": "-6052821095203578557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7374239827634911387": {
            "length": 28,
            "waveforms": {
                "single": "7374239827634911387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5120434989068102279": {
            "length": 28,
            "waveforms": {
                "single": "-5120434989068102279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4744679755456614953": {
            "length": 32,
            "waveforms": {
                "single": "4744679755456614953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2922675301064935416": {
            "length": 32,
            "waveforms": {
                "single": "-2922675301064935416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1599642469025067900": {
            "length": 32,
            "waveforms": {
                "single": "1599642469025067900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6067712587496482469": {
            "length": 32,
            "waveforms": {
                "single": "-6067712587496482469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8596245579868524405": {
            "length": 36,
            "waveforms": {
                "single": "-8596245579868524405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8697272659674778903": {
            "length": 36,
            "waveforms": {
                "single": "-8697272659674778903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4729788263163711041": {
            "length": 36,
            "waveforms": {
                "single": "4729788263163711041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9194638040455837259": {
            "length": 36,
            "waveforms": {
                "single": "-9194638040455837259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-989108751228845480": {
            "length": 40,
            "waveforms": {
                "single": "-989108751228845480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1266303154644847694": {
            "length": 40,
            "waveforms": {
                "single": "-1266303154644847694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1044809095446132446": {
            "length": 40,
            "waveforms": {
                "single": "-1044809095446132446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1763668535425906050": {
            "length": 40,
            "waveforms": {
                "single": "-1763668535425906050",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1542174476227190802": {
            "length": 44,
            "waveforms": {
                "single": "-1542174476227190802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4960122498799658068": {
            "length": 44,
            "waveforms": {
                "single": "4960122498799658068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6386160409583798763": {
            "length": 44,
            "waveforms": {
                "single": "6386160409583798763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8253411757883129202": {
            "length": 44,
            "waveforms": {
                "single": "-8253411757883129202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3241123123152251710": {
            "length": 48,
            "waveforms": {
                "single": "3241123123152251710",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6231554428824671406": {
            "length": 48,
            "waveforms": {
                "single": "6231554428824671406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5834158010681247091": {
            "length": 48,
            "waveforms": {
                "single": "-5834158010681247091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1311840240591243775": {
            "length": 48,
            "waveforms": {
                "single": "-1311840240591243775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3797409189329885383": {
            "length": 52,
            "waveforms": {
                "single": "3797409189329885383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2210360411893939533": {
            "length": 52,
            "waveforms": {
                "single": "-2210360411893939533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4562726080656233753": {
            "length": 52,
            "waveforms": {
                "single": "-4562726080656233753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6119129264438687434": {
            "length": 52,
            "waveforms": {
                "single": "6119129264438687434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6340623323637402682": {
            "length": 56,
            "waveforms": {
                "single": "6340623323637402682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4016065241550566229": {
            "length": 56,
            "waveforms": {
                "single": "4016065241550566229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4177785864261159369": {
            "length": 56,
            "waveforms": {
                "single": "-4177785864261159369",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3956291805062444121": {
            "length": 56,
            "waveforms": {
                "single": "-3956291805062444121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-276793862057849597": {
            "length": 60,
            "waveforms": {
                "single": "-276793862057849597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-55299802859134349": {
            "length": 60,
            "waveforms": {
                "single": "-55299802859134349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3253183640768771840": {
            "length": 60,
            "waveforms": {
                "single": "3253183640768771840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3474677699967487088": {
            "length": 60,
            "waveforms": {
                "single": "3474677699967487088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3696171759166202336": {
            "length": 64,
            "waveforms": {
                "single": "3696171759166202336",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7375669702170796860": {
            "length": 64,
            "waveforms": {
                "single": "7375669702170796860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5893931447169369199": {
            "length": 64,
            "waveforms": {
                "single": "5893931447169369199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7541096868712133319": {
            "length": 64,
            "waveforms": {
                "single": "-7541096868712133319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2921245426529049943": {
            "length": 68,
            "waveforms": {
                "single": "-2921245426529049943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2797285039423414755": {
            "length": 68,
            "waveforms": {
                "single": "-2797285039423414755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5121843121510251208": {
            "length": 68,
            "waveforms": {
                "single": "-5121843121510251208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7474208790272545428": {
            "length": 68,
            "waveforms": {
                "single": "-7474208790272545428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4509724078500881266": {
            "length": 72,
            "waveforms": {
                "single": "4509724078500881266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2157358409738587046": {
            "length": 72,
            "waveforms": {
                "single": "2157358409738587046",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7550303593589456921": {
            "length": 72,
            "waveforms": {
                "single": "7550303593589456921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6928977825702763377": {
            "length": 72,
            "waveforms": {
                "single": "6928977825702763377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "178254773956101029": {
            "length": 76,
            "waveforms": {
                "single": "178254773956101029",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3188276571674161272": {
            "length": 76,
            "waveforms": {
                "single": "-3188276571674161272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2376014461959267892": {
            "length": 76,
            "waveforms": {
                "single": "2376014461959267892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3243976915891448238": {
            "length": 76,
            "waveforms": {
                "single": "-3243976915891448238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4961552373335543541": {
            "length": 80,
            "waveforms": {
                "single": "4961552373335543541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5085512760441178729": {
            "length": 80,
            "waveforms": {
                "single": "5085512760441178729",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4464186992554485185": {
            "length": 80,
            "waveforms": {
                "single": "4464186992554485185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2982448737553057524": {
            "length": 80,
            "waveforms": {
                "single": "2982448737553057524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6054222195344076866": {
            "length": 84,
            "waveforms": {
                "single": "-6054222195344076866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5832728136145361618": {
            "length": 84,
            "waveforms": {
                "single": "-5832728136145361618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1310410366055358302": {
            "length": 84,
            "waveforms": {
                "single": "-1310410366055358302",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3634968448142194755": {
            "length": 84,
            "waveforms": {
                "single": "-3634968448142194755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2219567136771263135": {
            "length": 88,
            "waveforms": {
                "single": "2219567136771263135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1598241368884569591": {
            "length": 88,
            "waveforms": {
                "single": "1598241368884569591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1819735428083284839": {
            "length": 88,
            "waveforms": {
                "single": "1819735428083284839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4638820883973145246": {
            "length": 88,
            "waveforms": {
                "single": "4638820883973145246",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4017495116086451702": {
            "length": 92,
            "waveforms": {
                "single": "4017495116086451702",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4176355989725273896": {
            "length": 92,
            "waveforms": {
                "single": "-4176355989725273896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9196039140596335568": {
            "length": 92,
            "waveforms": {
                "single": "-9196039140596335568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6279420012613395101": {
            "length": 92,
            "waveforms": {
                "single": "-6279420012613395101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6155459625507759913": {
            "length": 96,
            "waveforms": {
                "single": "-6155459625507759913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6776785393394453457": {
            "length": 96,
            "waveforms": {
                "single": "-6776785393394453457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3476107574503372561": {
            "length": 96,
            "waveforms": {
                "single": "3476107574503372561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1151549492416536108": {
            "length": 96,
            "waveforms": {
                "single": "1151549492416536108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5673867262506539424": {
            "length": 100,
            "waveforms": {
                "single": "5673867262506539424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5895361321705254672": {
            "length": 100,
            "waveforms": {
                "single": "5895361321705254672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8744210845761673293": {
            "length": 100,
            "waveforms": {
                "single": "-8744210845761673293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1292839950968877500_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "1292839950968877500_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "8784619959208724241_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "8784619959208724241_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-7951085683972061690": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5719521543880685833_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5719521543880685833_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8701075330190137210_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "8701075330190137210_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3694763626724053407": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-5019204591206069852": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4797710532007354604": {
            "samples": [0.1758793969849246] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-4086818485070593574": {
            "samples": [0.1758793969849246] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-3592883795826252118": {
            "samples": [0.1758793969849246] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-1046238969982017919": {
            "samples": [0.1758793969849246] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "2633258973022576605": {
            "samples": [0.1758793969849246] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "2854753032221291853": {
            "samples": [0.1758793969849246] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-6719809248785606908": {
            "samples": [0.1758793969849246] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "4059579768402394339": {
            "samples": [0.1758793969849246] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-3856484249434646547": {
            "samples": [0.1758793969849246] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3239693248616366237": {
            "samples": [0.1758793969849246] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "887327579854072017": {
            "samples": [0.1758793969849246] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "932654315443039549": {
            "samples": [0.1758793969849246] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-11192591448623741": {
            "samples": [0.1758793969849246] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8860989201254029114": {
            "samples": [0.1758793969849246] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8318297084884003226": {
            "samples": [0.1758793969849246] * 15 + [0.0],
            "type": "arbitrary",
        },
        "8539791144082718474": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "8262596740666716260": {
            "samples": [0.1758793969849246] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1978618043815843577": {
            "samples": [0.1758793969849246] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1933291308226876045": {
            "samples": [0.1758793969849246] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2475983424596901933": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-2753177828012904147": {
            "samples": [0.1758793969849246] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-278223736593735070": {
            "samples": [0.1758793969849246] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5673845520412802880": {
            "samples": [0.1758793969849246] * 23 + [0.0],
            "type": "arbitrary",
        },
        "8815452115307633033": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "7871605208415969743": {
            "samples": [0.1758793969849246] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6052821095203578557": {
            "samples": [0.1758793969849246] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7374239827634911387": {
            "samples": [0.1758793969849246] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5120434989068102279": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4744679755456614953": {
            "samples": [0.1758793969849246] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2922675301064935416": {
            "samples": [0.1758793969849246] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1599642469025067900": {
            "samples": [0.1758793969849246] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6067712587496482469": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-8596245579868524405": {
            "samples": [0.1758793969849246] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8697272659674778903": {
            "samples": [0.1758793969849246] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4729788263163711041": {
            "samples": [0.1758793969849246] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-9194638040455837259": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-989108751228845480": {
            "samples": [0.1758793969849246] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1266303154644847694": {
            "samples": [0.1758793969849246] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1044809095446132446": {
            "samples": [0.1758793969849246] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1763668535425906050": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-1542174476227190802": {
            "samples": [0.1758793969849246] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4960122498799658068": {
            "samples": [0.1758793969849246] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6386160409583798763": {
            "samples": [0.1758793969849246] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8253411757883129202": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3241123123152251710": {
            "samples": [0.1758793969849246] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6231554428824671406": {
            "samples": [0.1758793969849246] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5834158010681247091": {
            "samples": [0.1758793969849246] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-1311840240591243775": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3797409189329885383": {
            "samples": [0.1758793969849246] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2210360411893939533": {
            "samples": [0.1758793969849246] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4562726080656233753": {
            "samples": [0.1758793969849246] * 51 + [0.0],
            "type": "arbitrary",
        },
        "6119129264438687434": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "6340623323637402682": {
            "samples": [0.1758793969849246] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4016065241550566229": {
            "samples": [0.1758793969849246] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4177785864261159369": {
            "samples": [0.1758793969849246] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-3956291805062444121": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-276793862057849597": {
            "samples": [0.1758793969849246] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-55299802859134349": {
            "samples": [0.1758793969849246] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3253183640768771840": {
            "samples": [0.1758793969849246] * 59 + [0.0],
            "type": "arbitrary",
        },
        "3474677699967487088": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3696171759166202336": {
            "samples": [0.1758793969849246] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7375669702170796860": {
            "samples": [0.1758793969849246] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5893931447169369199": {
            "samples": [0.1758793969849246] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-7541096868712133319": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-2921245426529049943": {
            "samples": [0.1758793969849246] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2797285039423414755": {
            "samples": [0.1758793969849246] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5121843121510251208": {
            "samples": [0.1758793969849246] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-7474208790272545428": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4509724078500881266": {
            "samples": [0.1758793969849246] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2157358409738587046": {
            "samples": [0.1758793969849246] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7550303593589456921": {
            "samples": [0.1758793969849246] * 71 + [0.0],
            "type": "arbitrary",
        },
        "6928977825702763377": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "178254773956101029": {
            "samples": [0.1758793969849246] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3188276571674161272": {
            "samples": [0.1758793969849246] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2376014461959267892": {
            "samples": [0.1758793969849246] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-3243976915891448238": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4961552373335543541": {
            "samples": [0.1758793969849246] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5085512760441178729": {
            "samples": [0.1758793969849246] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4464186992554485185": {
            "samples": [0.1758793969849246] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2982448737553057524": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-6054222195344076866": {
            "samples": [0.1758793969849246] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5832728136145361618": {
            "samples": [0.1758793969849246] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1310410366055358302": {
            "samples": [0.1758793969849246] * 83 + [0.0],
            "type": "arbitrary",
        },
        "-3634968448142194755": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "2219567136771263135": {
            "samples": [0.1758793969849246] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1598241368884569591": {
            "samples": [0.1758793969849246] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1819735428083284839": {
            "samples": [0.1758793969849246] * 87 + [0.0],
            "type": "arbitrary",
        },
        "4638820883973145246": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4017495116086451702": {
            "samples": [0.1758793969849246] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4176355989725273896": {
            "samples": [0.1758793969849246] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9196039140596335568": {
            "samples": [0.1758793969849246] * 91 + [0.0],
            "type": "arbitrary",
        },
        "-6279420012613395101": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-6155459625507759913": {
            "samples": [0.1758793969849246] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6776785393394453457": {
            "samples": [0.1758793969849246] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3476107574503372561": {
            "samples": [0.1758793969849246] * 95 + [0.0],
            "type": "arbitrary",
        },
        "1151549492416536108": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "5673867262506539424": {
            "samples": [0.1758793969849246] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5895361321705254672": {
            "samples": [0.1758793969849246] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8744210845761673293": {
            "samples": [0.1758793969849246] * 99 + [0.0],
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
                        "feedforward": [1.0732888182245781, -0.9737209520873108, -0.0005203790392933598, -0.0005149944373311913, -0.002105044281710212, -0.003388157787203089, -0.0027995218244958146, 0.0029055980790707184, -0.002492824987361109, 0.0018688320586038787, 0.007669994237074814, 0.006431769668045485, 0.00019505700310456196, -0.001968630346827333, 0.002342580506761632, -0.007645763391517998, 0.0019060799407871365, -0.006897677857935084, 0.0054469947281882624, -0.012373869741610479, 0.010667355535212872],
                        "feedback": [0.9999990463256836, -0.9016765067668822],
                    },
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.082216163036566, -1.013483744074572, -0.0005934150341553434, -0.0005835327755912938, 0.007717830054774853, 0.003632375897519549, -0.00044011698253741335, 0.001605758501608272, -0.012449189070277502, -0.007236945254569601, 0.00976822190693331, 0.005697927299491748, 0.004773147069343227, -0.002901494501723682, -0.0017290035617877402, -0.001732703182405211, -0.004127059088728484, 0.006652439702682195, -0.0018491032089883812, -0.005021633883561784, 0.003839210780199868],
                        "feedback": [0.9999990463256836, -0.9262251003261055],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0864486524147088, -1.0114796931248773, -0.00016385035736341804, -0.0001631375856683214, 0.0007132004480542389, -0.005469433104324626, -0.0031203713793950478, 0.0020985293007232484, -0.005440448977252687, 0.0029103915350147547, 0.006805519982961323, 0.007363572786123743, -0.0038086062520665135, -0.003181071276233404, 0.0005943072751533468, -0.003554727873357823, 0.0023584825716348456, -0.005872694192023741, 0.0012065363048726322, 0.0017448644372721935, 0.001253029817072768],
                        "feedback": [0.9999990463256836, -0.9287365023806654],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1030496953566256, -1.0381134620821453, -0.0004260403462593258, -0.000420572662019365, 0.005570686385595049, -0.0020512683945509416, -0.0006392178405930675, -0.001996407788676792, 0.0004683735253229373, -0.003829742786740141, 0.0057195392567130805, 0.006959373393239386, -0.0034838926793923962, 0.0011703722958150697, -0.0027201873232208813, -0.004669494937616429, -0.0016907470696459624, -9.041142346012665e-05, 0.0001460934840622299, 0.002830673562819465, 0.0005694981868720677],
                        "feedback": [0.9999990463256836, -0.9336222939492675],
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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "7": {
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
                "-7951085683972061690": "-7951085683972061690",
                "3694763626724053407": "3694763626724053407",
                "-5019204591206069852": "-5019204591206069852",
                "-4797710532007354604": "-4797710532007354604",
                "-4086818485070593574": "-4086818485070593574",
                "-3592883795826252118": "-3592883795826252118",
                "-1046238969982017919": "-1046238969982017919",
                "2633258973022576605": "2633258973022576605",
                "2854753032221291853": "2854753032221291853",
                "-6719809248785606908": "-6719809248785606908",
                "4059579768402394339": "4059579768402394339",
                "-3856484249434646547": "-3856484249434646547",
                "3239693248616366237": "3239693248616366237",
                "887327579854072017": "887327579854072017",
                "932654315443039549": "932654315443039549",
                "-11192591448623741": "-11192591448623741",
                "8860989201254029114": "8860989201254029114",
                "8318297084884003226": "8318297084884003226",
                "8539791144082718474": "8539791144082718474",
                "8262596740666716260": "8262596740666716260",
                "-1978618043815843577": "-1978618043815843577",
                "-1933291308226876045": "-1933291308226876045",
                "-2475983424596901933": "-2475983424596901933",
                "-2753177828012904147": "-2753177828012904147",
                "-278223736593735070": "-278223736593735070",
                "5673845520412802880": "5673845520412802880",
                "8815452115307633033": "8815452115307633033",
                "7871605208415969743": "7871605208415969743",
                "-6052821095203578557": "-6052821095203578557",
                "7374239827634911387": "7374239827634911387",
                "-5120434989068102279": "-5120434989068102279",
                "4744679755456614953": "4744679755456614953",
                "-2922675301064935416": "-2922675301064935416",
                "1599642469025067900": "1599642469025067900",
                "-6067712587496482469": "-6067712587496482469",
                "-8596245579868524405": "-8596245579868524405",
                "-8697272659674778903": "-8697272659674778903",
                "4729788263163711041": "4729788263163711041",
                "-9194638040455837259": "-9194638040455837259",
                "-989108751228845480": "-989108751228845480",
                "-1266303154644847694": "-1266303154644847694",
                "-1044809095446132446": "-1044809095446132446",
                "-1763668535425906050": "-1763668535425906050",
                "-1542174476227190802": "-1542174476227190802",
                "4960122498799658068": "4960122498799658068",
                "6386160409583798763": "6386160409583798763",
                "-8253411757883129202": "-8253411757883129202",
                "3241123123152251710": "3241123123152251710",
                "6231554428824671406": "6231554428824671406",
                "-5834158010681247091": "-5834158010681247091",
                "-1311840240591243775": "-1311840240591243775",
                "3797409189329885383": "3797409189329885383",
                "-2210360411893939533": "-2210360411893939533",
                "-4562726080656233753": "-4562726080656233753",
                "6119129264438687434": "6119129264438687434",
                "6340623323637402682": "6340623323637402682",
                "4016065241550566229": "4016065241550566229",
                "-4177785864261159369": "-4177785864261159369",
                "-3956291805062444121": "-3956291805062444121",
                "-276793862057849597": "-276793862057849597",
                "-55299802859134349": "-55299802859134349",
                "3253183640768771840": "3253183640768771840",
                "3474677699967487088": "3474677699967487088",
                "3696171759166202336": "3696171759166202336",
                "7375669702170796860": "7375669702170796860",
                "5893931447169369199": "5893931447169369199",
                "-7541096868712133319": "-7541096868712133319",
                "-2921245426529049943": "-2921245426529049943",
                "-2797285039423414755": "-2797285039423414755",
                "-5121843121510251208": "-5121843121510251208",
                "-7474208790272545428": "-7474208790272545428",
                "4509724078500881266": "4509724078500881266",
                "2157358409738587046": "2157358409738587046",
                "7550303593589456921": "7550303593589456921",
                "6928977825702763377": "6928977825702763377",
                "178254773956101029": "178254773956101029",
                "-3188276571674161272": "-3188276571674161272",
                "2376014461959267892": "2376014461959267892",
                "-3243976915891448238": "-3243976915891448238",
                "4961552373335543541": "4961552373335543541",
                "5085512760441178729": "5085512760441178729",
                "4464186992554485185": "4464186992554485185",
                "2982448737553057524": "2982448737553057524",
                "-6054222195344076866": "-6054222195344076866",
                "-5832728136145361618": "-5832728136145361618",
                "-1310410366055358302": "-1310410366055358302",
                "-3634968448142194755": "-3634968448142194755",
                "2219567136771263135": "2219567136771263135",
                "1598241368884569591": "1598241368884569591",
                "1819735428083284839": "1819735428083284839",
                "4638820883973145246": "4638820883973145246",
                "4017495116086451702": "4017495116086451702",
                "-4176355989725273896": "-4176355989725273896",
                "-9196039140596335568": "-9196039140596335568",
                "-6279420012613395101": "-6279420012613395101",
                "-6155459625507759913": "-6155459625507759913",
                "-6776785393394453457": "-6776785393394453457",
                "3476107574503372561": "3476107574503372561",
                "1151549492416536108": "1151549492416536108",
                "5673867262506539424": "5673867262506539424",
                "5895361321705254672": "5895361321705254672",
                "-8744210845761673293": "-8744210845761673293",
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
                "5931209932826119817": "5931209932826119817_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_867",
                "lo_frequency": 7370000000.0,
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
                "1292839950968877500": "1292839950968877500",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_a92",
                "lo_frequency": 5900000000.0,
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
                "8784619959208724241": "8784619959208724241",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_035",
                "lo_frequency": 6700000000.0,
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
                "-1322718175353050215": "-1322718175353050215_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_e29",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "1292839950968877500": {
            "length": 40,
            "waveforms": {
                "I": "1292839950968877500_i",
                "Q": "1292839950968877500_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8784619959208724241": {
            "length": 40,
            "waveforms": {
                "I": "8784619959208724241_i",
                "Q": "8784619959208724241_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7951085683972061690": {
            "length": 100,
            "waveforms": {
                "single": "-7951085683972061690",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5931209932826119817_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5719521543880685833_i",
                "Q": "5719521543880685833_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-1322718175353050215_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8701075330190137210_i",
                "Q": "8701075330190137210_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "3694763626724053407": {
            "length": 100,
            "waveforms": {
                "single": "3694763626724053407",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5019204591206069852": {
            "length": 16,
            "waveforms": {
                "single": "-5019204591206069852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4797710532007354604": {
            "length": 16,
            "waveforms": {
                "single": "-4797710532007354604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4086818485070593574": {
            "length": 16,
            "waveforms": {
                "single": "-4086818485070593574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3592883795826252118": {
            "length": 16,
            "waveforms": {
                "single": "-3592883795826252118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1046238969982017919": {
            "length": 16,
            "waveforms": {
                "single": "-1046238969982017919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2633258973022576605": {
            "length": 16,
            "waveforms": {
                "single": "2633258973022576605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2854753032221291853": {
            "length": 16,
            "waveforms": {
                "single": "2854753032221291853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6719809248785606908": {
            "length": 16,
            "waveforms": {
                "single": "-6719809248785606908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4059579768402394339": {
            "length": 16,
            "waveforms": {
                "single": "4059579768402394339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3856484249434646547": {
            "length": 16,
            "waveforms": {
                "single": "-3856484249434646547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3239693248616366237": {
            "length": 16,
            "waveforms": {
                "single": "3239693248616366237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "887327579854072017": {
            "length": 16,
            "waveforms": {
                "single": "887327579854072017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "932654315443039549": {
            "length": 16,
            "waveforms": {
                "single": "932654315443039549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-11192591448623741": {
            "length": 16,
            "waveforms": {
                "single": "-11192591448623741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8860989201254029114": {
            "length": 16,
            "waveforms": {
                "single": "8860989201254029114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8318297084884003226": {
            "length": 16,
            "waveforms": {
                "single": "8318297084884003226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8539791144082718474": {
            "length": 16,
            "waveforms": {
                "single": "8539791144082718474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8262596740666716260": {
            "length": 20,
            "waveforms": {
                "single": "8262596740666716260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1978618043815843577": {
            "length": 20,
            "waveforms": {
                "single": "-1978618043815843577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1933291308226876045": {
            "length": 20,
            "waveforms": {
                "single": "-1933291308226876045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2475983424596901933": {
            "length": 20,
            "waveforms": {
                "single": "-2475983424596901933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2753177828012904147": {
            "length": 24,
            "waveforms": {
                "single": "-2753177828012904147",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-278223736593735070": {
            "length": 24,
            "waveforms": {
                "single": "-278223736593735070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5673845520412802880": {
            "length": 24,
            "waveforms": {
                "single": "5673845520412802880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8815452115307633033": {
            "length": 24,
            "waveforms": {
                "single": "8815452115307633033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7871605208415969743": {
            "length": 28,
            "waveforms": {
                "single": "7871605208415969743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6052821095203578557": {
            "length": 28,
            "waveforms": {
                "single": "-6052821095203578557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7374239827634911387": {
            "length": 28,
            "waveforms": {
                "single": "7374239827634911387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5120434989068102279": {
            "length": 28,
            "waveforms": {
                "single": "-5120434989068102279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4744679755456614953": {
            "length": 32,
            "waveforms": {
                "single": "4744679755456614953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2922675301064935416": {
            "length": 32,
            "waveforms": {
                "single": "-2922675301064935416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1599642469025067900": {
            "length": 32,
            "waveforms": {
                "single": "1599642469025067900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6067712587496482469": {
            "length": 32,
            "waveforms": {
                "single": "-6067712587496482469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8596245579868524405": {
            "length": 36,
            "waveforms": {
                "single": "-8596245579868524405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8697272659674778903": {
            "length": 36,
            "waveforms": {
                "single": "-8697272659674778903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4729788263163711041": {
            "length": 36,
            "waveforms": {
                "single": "4729788263163711041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9194638040455837259": {
            "length": 36,
            "waveforms": {
                "single": "-9194638040455837259",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-989108751228845480": {
            "length": 40,
            "waveforms": {
                "single": "-989108751228845480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1266303154644847694": {
            "length": 40,
            "waveforms": {
                "single": "-1266303154644847694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1044809095446132446": {
            "length": 40,
            "waveforms": {
                "single": "-1044809095446132446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1763668535425906050": {
            "length": 40,
            "waveforms": {
                "single": "-1763668535425906050",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1542174476227190802": {
            "length": 44,
            "waveforms": {
                "single": "-1542174476227190802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4960122498799658068": {
            "length": 44,
            "waveforms": {
                "single": "4960122498799658068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6386160409583798763": {
            "length": 44,
            "waveforms": {
                "single": "6386160409583798763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8253411757883129202": {
            "length": 44,
            "waveforms": {
                "single": "-8253411757883129202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3241123123152251710": {
            "length": 48,
            "waveforms": {
                "single": "3241123123152251710",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6231554428824671406": {
            "length": 48,
            "waveforms": {
                "single": "6231554428824671406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5834158010681247091": {
            "length": 48,
            "waveforms": {
                "single": "-5834158010681247091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1311840240591243775": {
            "length": 48,
            "waveforms": {
                "single": "-1311840240591243775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3797409189329885383": {
            "length": 52,
            "waveforms": {
                "single": "3797409189329885383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2210360411893939533": {
            "length": 52,
            "waveforms": {
                "single": "-2210360411893939533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4562726080656233753": {
            "length": 52,
            "waveforms": {
                "single": "-4562726080656233753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6119129264438687434": {
            "length": 52,
            "waveforms": {
                "single": "6119129264438687434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6340623323637402682": {
            "length": 56,
            "waveforms": {
                "single": "6340623323637402682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4016065241550566229": {
            "length": 56,
            "waveforms": {
                "single": "4016065241550566229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4177785864261159369": {
            "length": 56,
            "waveforms": {
                "single": "-4177785864261159369",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3956291805062444121": {
            "length": 56,
            "waveforms": {
                "single": "-3956291805062444121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-276793862057849597": {
            "length": 60,
            "waveforms": {
                "single": "-276793862057849597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-55299802859134349": {
            "length": 60,
            "waveforms": {
                "single": "-55299802859134349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3253183640768771840": {
            "length": 60,
            "waveforms": {
                "single": "3253183640768771840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3474677699967487088": {
            "length": 60,
            "waveforms": {
                "single": "3474677699967487088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3696171759166202336": {
            "length": 64,
            "waveforms": {
                "single": "3696171759166202336",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7375669702170796860": {
            "length": 64,
            "waveforms": {
                "single": "7375669702170796860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5893931447169369199": {
            "length": 64,
            "waveforms": {
                "single": "5893931447169369199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7541096868712133319": {
            "length": 64,
            "waveforms": {
                "single": "-7541096868712133319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2921245426529049943": {
            "length": 68,
            "waveforms": {
                "single": "-2921245426529049943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2797285039423414755": {
            "length": 68,
            "waveforms": {
                "single": "-2797285039423414755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5121843121510251208": {
            "length": 68,
            "waveforms": {
                "single": "-5121843121510251208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7474208790272545428": {
            "length": 68,
            "waveforms": {
                "single": "-7474208790272545428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4509724078500881266": {
            "length": 72,
            "waveforms": {
                "single": "4509724078500881266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2157358409738587046": {
            "length": 72,
            "waveforms": {
                "single": "2157358409738587046",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7550303593589456921": {
            "length": 72,
            "waveforms": {
                "single": "7550303593589456921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6928977825702763377": {
            "length": 72,
            "waveforms": {
                "single": "6928977825702763377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "178254773956101029": {
            "length": 76,
            "waveforms": {
                "single": "178254773956101029",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3188276571674161272": {
            "length": 76,
            "waveforms": {
                "single": "-3188276571674161272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2376014461959267892": {
            "length": 76,
            "waveforms": {
                "single": "2376014461959267892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3243976915891448238": {
            "length": 76,
            "waveforms": {
                "single": "-3243976915891448238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4961552373335543541": {
            "length": 80,
            "waveforms": {
                "single": "4961552373335543541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5085512760441178729": {
            "length": 80,
            "waveforms": {
                "single": "5085512760441178729",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4464186992554485185": {
            "length": 80,
            "waveforms": {
                "single": "4464186992554485185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2982448737553057524": {
            "length": 80,
            "waveforms": {
                "single": "2982448737553057524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6054222195344076866": {
            "length": 84,
            "waveforms": {
                "single": "-6054222195344076866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5832728136145361618": {
            "length": 84,
            "waveforms": {
                "single": "-5832728136145361618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1310410366055358302": {
            "length": 84,
            "waveforms": {
                "single": "-1310410366055358302",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3634968448142194755": {
            "length": 84,
            "waveforms": {
                "single": "-3634968448142194755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2219567136771263135": {
            "length": 88,
            "waveforms": {
                "single": "2219567136771263135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1598241368884569591": {
            "length": 88,
            "waveforms": {
                "single": "1598241368884569591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1819735428083284839": {
            "length": 88,
            "waveforms": {
                "single": "1819735428083284839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4638820883973145246": {
            "length": 88,
            "waveforms": {
                "single": "4638820883973145246",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4017495116086451702": {
            "length": 92,
            "waveforms": {
                "single": "4017495116086451702",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4176355989725273896": {
            "length": 92,
            "waveforms": {
                "single": "-4176355989725273896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9196039140596335568": {
            "length": 92,
            "waveforms": {
                "single": "-9196039140596335568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6279420012613395101": {
            "length": 92,
            "waveforms": {
                "single": "-6279420012613395101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6155459625507759913": {
            "length": 96,
            "waveforms": {
                "single": "-6155459625507759913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6776785393394453457": {
            "length": 96,
            "waveforms": {
                "single": "-6776785393394453457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3476107574503372561": {
            "length": 96,
            "waveforms": {
                "single": "3476107574503372561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1151549492416536108": {
            "length": 96,
            "waveforms": {
                "single": "1151549492416536108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5673867262506539424": {
            "length": 100,
            "waveforms": {
                "single": "5673867262506539424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5895361321705254672": {
            "length": 100,
            "waveforms": {
                "single": "5895361321705254672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8744210845761673293": {
            "length": 100,
            "waveforms": {
                "single": "-8744210845761673293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1292839950968877500_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1292839950968877500_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8784619959208724241_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8784619959208724241_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7951085683972061690": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5719521543880685833_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5719521543880685833_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8701075330190137210_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "8701075330190137210_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3694763626724053407": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-5019204591206069852": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4797710532007354604": {
            "samples": [0.1758793969849246] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4086818485070593574": {
            "samples": [0.1758793969849246] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3592883795826252118": {
            "samples": [0.1758793969849246] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1046238969982017919": {
            "samples": [0.1758793969849246] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2633258973022576605": {
            "samples": [0.1758793969849246] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2854753032221291853": {
            "samples": [0.1758793969849246] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6719809248785606908": {
            "samples": [0.1758793969849246] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4059579768402394339": {
            "samples": [0.1758793969849246] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3856484249434646547": {
            "samples": [0.1758793969849246] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3239693248616366237": {
            "samples": [0.1758793969849246] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "887327579854072017": {
            "samples": [0.1758793969849246] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "932654315443039549": {
            "samples": [0.1758793969849246] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-11192591448623741": {
            "samples": [0.1758793969849246] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8860989201254029114": {
            "samples": [0.1758793969849246] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8318297084884003226": {
            "samples": [0.1758793969849246] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8539791144082718474": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "8262596740666716260": {
            "samples": [0.1758793969849246] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1978618043815843577": {
            "samples": [0.1758793969849246] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1933291308226876045": {
            "samples": [0.1758793969849246] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2475983424596901933": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-2753177828012904147": {
            "samples": [0.1758793969849246] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-278223736593735070": {
            "samples": [0.1758793969849246] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5673845520412802880": {
            "samples": [0.1758793969849246] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8815452115307633033": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "7871605208415969743": {
            "samples": [0.1758793969849246] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6052821095203578557": {
            "samples": [0.1758793969849246] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7374239827634911387": {
            "samples": [0.1758793969849246] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5120434989068102279": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4744679755456614953": {
            "samples": [0.1758793969849246] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2922675301064935416": {
            "samples": [0.1758793969849246] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1599642469025067900": {
            "samples": [0.1758793969849246] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6067712587496482469": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-8596245579868524405": {
            "samples": [0.1758793969849246] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8697272659674778903": {
            "samples": [0.1758793969849246] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4729788263163711041": {
            "samples": [0.1758793969849246] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9194638040455837259": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-989108751228845480": {
            "samples": [0.1758793969849246] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1266303154644847694": {
            "samples": [0.1758793969849246] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1044809095446132446": {
            "samples": [0.1758793969849246] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1763668535425906050": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-1542174476227190802": {
            "samples": [0.1758793969849246] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4960122498799658068": {
            "samples": [0.1758793969849246] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6386160409583798763": {
            "samples": [0.1758793969849246] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8253411757883129202": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3241123123152251710": {
            "samples": [0.1758793969849246] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6231554428824671406": {
            "samples": [0.1758793969849246] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5834158010681247091": {
            "samples": [0.1758793969849246] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1311840240591243775": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3797409189329885383": {
            "samples": [0.1758793969849246] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2210360411893939533": {
            "samples": [0.1758793969849246] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4562726080656233753": {
            "samples": [0.1758793969849246] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6119129264438687434": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "6340623323637402682": {
            "samples": [0.1758793969849246] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4016065241550566229": {
            "samples": [0.1758793969849246] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4177785864261159369": {
            "samples": [0.1758793969849246] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3956291805062444121": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-276793862057849597": {
            "samples": [0.1758793969849246] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-55299802859134349": {
            "samples": [0.1758793969849246] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3253183640768771840": {
            "samples": [0.1758793969849246] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3474677699967487088": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "3696171759166202336": {
            "samples": [0.1758793969849246] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7375669702170796860": {
            "samples": [0.1758793969849246] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5893931447169369199": {
            "samples": [0.1758793969849246] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7541096868712133319": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-2921245426529049943": {
            "samples": [0.1758793969849246] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2797285039423414755": {
            "samples": [0.1758793969849246] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5121843121510251208": {
            "samples": [0.1758793969849246] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7474208790272545428": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4509724078500881266": {
            "samples": [0.1758793969849246] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2157358409738587046": {
            "samples": [0.1758793969849246] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7550303593589456921": {
            "samples": [0.1758793969849246] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6928977825702763377": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "178254773956101029": {
            "samples": [0.1758793969849246] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3188276571674161272": {
            "samples": [0.1758793969849246] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2376014461959267892": {
            "samples": [0.1758793969849246] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3243976915891448238": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4961552373335543541": {
            "samples": [0.1758793969849246] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5085512760441178729": {
            "samples": [0.1758793969849246] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4464186992554485185": {
            "samples": [0.1758793969849246] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2982448737553057524": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-6054222195344076866": {
            "samples": [0.1758793969849246] * 81 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5832728136145361618": {
            "samples": [0.1758793969849246] * 82 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1310410366055358302": {
            "samples": [0.1758793969849246] * 83 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3634968448142194755": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "2219567136771263135": {
            "samples": [0.1758793969849246] * 85 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1598241368884569591": {
            "samples": [0.1758793969849246] * 86 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1819735428083284839": {
            "samples": [0.1758793969849246] * 87 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4638820883973145246": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "4017495116086451702": {
            "samples": [0.1758793969849246] * 89 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4176355989725273896": {
            "samples": [0.1758793969849246] * 90 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9196039140596335568": {
            "samples": [0.1758793969849246] * 91 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6279420012613395101": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "-6155459625507759913": {
            "samples": [0.1758793969849246] * 93 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6776785393394453457": {
            "samples": [0.1758793969849246] * 94 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3476107574503372561": {
            "samples": [0.1758793969849246] * 95 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1151549492416536108": {
            "sample": 0.1758793969849246,
            "type": "constant",
        },
        "5673867262506539424": {
            "samples": [0.1758793969849246] * 97 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5895361321705254672": {
            "samples": [0.1758793969849246] * 98 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8744210845761673293": {
            "samples": [0.1758793969849246] * 99 + [0.0],
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
        "B2/acquisition_mixer_867": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_a92": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_035": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_e29": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

