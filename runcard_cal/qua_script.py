
# Single QUA script generated at 2025-02-09 08:26:50.569866
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
            with for_(v9,-1.99,(v9<-1.8731781376518215),(v9+0.008056680161943497)):
                align()
                play("1915213350897154053", "B2/drive")
                play("-4689886691959901283", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("7904921271263004858"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-6019505032356543442"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("4759883984831457805"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-786295215329779096"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("2559286289850256540"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("1411464472673387767"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("1632958531872103015"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-6034396524649447354"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("3830718219875269878"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-2504419021822825917"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("2017898748267177399"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-9161321977608802144"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("4215658436270344262"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-6963562289605635281"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-8900342148319362948"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-4378024378229359632"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-4156530319030644384"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-6578622073210560897"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-1958770631027477521"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("8894430563850002955"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("3274439185999286825"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-6022336007032927224"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("5472198874002453688"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-1278524177744208660"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-7741335382680333582"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-9223073637681761243"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-1017544348454769464"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-7895941363439460939"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-7674447304240745691"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-7951641707656747905"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-5476687616237578828"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("7350065079621256658"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-7289507087845671307"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-5585682089086845900"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-5091747399842504444"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("7906351145798890331"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("141462417184259902"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("1355889428205039527"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-580890430508688140"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("2560716164386142013"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-2887929363682014828"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("7793925981412906359"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-7736198964313704790"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("3832148094411155351"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-8233564345094763146"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("7860814059852494250"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("7583619656436492036"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-83735400085058333"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("4438582370004944983"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-3154960508827126157"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-3432154912243128371"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-3210660853044413123"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("4994868436182578656"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-6355698139475960176"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("4174981916396550554"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("1572636746335029389"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-6020906132497041751"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("1075271365553971033"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("5875376223618659061"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-6619298593084354605"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("920665384794843676"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("-5414471856903252119"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("6153875201821608022"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("-7566576191512734795"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("5431522354128659980"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("8573128949023490133"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("6636349090309762466"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("-1945280238875071918"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("85887372715911662"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("8958069165418564517"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("9179563224617279765"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("-3164998467349078316"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("5707183325353574539"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("7738350936944558119"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("2562146038922027486"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("5108790864766261685"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("6092123541748648923"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("6313617600947364171"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("-5629789300497356508"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("-5906983703913358722"*amp(v9), "B4/flux")
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
                play("-4689886691959901283", "B4/drive")
                measure("-7892271018515113085", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.06078547221045674)-(v3*0.9981508535127102))>0.0025565952953590303)))
                r1 = declare_stream()
                save(v4, r1)
                measure("8284456123398081785", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.6665903597333165)-(v6*0.7454242364657911))>-0.0004342766968863211)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(15).buffer(80).average().save("-7892271018515113085_B2|acquisition_shots")
        r2.buffer(15).buffer(80).average().save("8284456123398081785_B4|acquisition_shots")


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
                "5376860812236258989": "5376860812236258989",
                "2298545585313633057": "2298545585313633057",
                "7904921271263004858": "7904921271263004858",
                "-6019505032356543442": "-6019505032356543442",
                "4759883984831457805": "4759883984831457805",
                "-786295215329779096": "-786295215329779096",
                "2559286289850256540": "2559286289850256540",
                "1411464472673387767": "1411464472673387767",
                "1632958531872103015": "1632958531872103015",
                "-6034396524649447354": "-6034396524649447354",
                "3830718219875269878": "3830718219875269878",
                "-2504419021822825917": "-2504419021822825917",
                "2017898748267177399": "2017898748267177399",
                "-9161321977608802144": "-9161321977608802144",
                "4215658436270344262": "4215658436270344262",
                "-6963562289605635281": "-6963562289605635281",
                "-8900342148319362948": "-8900342148319362948",
                "-4378024378229359632": "-4378024378229359632",
                "-4156530319030644384": "-4156530319030644384",
                "-6578622073210560897": "-6578622073210560897",
                "-1958770631027477521": "-1958770631027477521",
                "8894430563850002955": "8894430563850002955",
                "3274439185999286825": "3274439185999286825",
                "-6022336007032927224": "-6022336007032927224",
                "5472198874002453688": "5472198874002453688",
                "-1278524177744208660": "-1278524177744208660",
                "-7741335382680333582": "-7741335382680333582",
                "-9223073637681761243": "-9223073637681761243",
                "-1017544348454769464": "-1017544348454769464",
                "-7895941363439460939": "-7895941363439460939",
                "-7674447304240745691": "-7674447304240745691",
                "-7951641707656747905": "-7951641707656747905",
                "-5476687616237578828": "-5476687616237578828",
                "7350065079621256658": "7350065079621256658",
                "-7289507087845671307": "-7289507087845671307",
                "-5585682089086845900": "-5585682089086845900",
                "-5091747399842504444": "-5091747399842504444",
                "7906351145798890331": "7906351145798890331",
                "141462417184259902": "141462417184259902",
                "1355889428205039527": "1355889428205039527",
                "-580890430508688140": "-580890430508688140",
                "2560716164386142013": "2560716164386142013",
                "-2887929363682014828": "-2887929363682014828",
                "7793925981412906359": "7793925981412906359",
                "-7736198964313704790": "-7736198964313704790",
                "3832148094411155351": "3832148094411155351",
                "-8233564345094763146": "-8233564345094763146",
                "7860814059852494250": "7860814059852494250",
                "7583619656436492036": "7583619656436492036",
                "-83735400085058333": "-83735400085058333",
                "4438582370004944983": "4438582370004944983",
                "-3154960508827126157": "-3154960508827126157",
                "-3432154912243128371": "-3432154912243128371",
                "-3210660853044413123": "-3210660853044413123",
                "4994868436182578656": "4994868436182578656",
                "-6355698139475960176": "-6355698139475960176",
                "4174981916396550554": "4174981916396550554",
                "1572636746335029389": "1572636746335029389",
                "-6020906132497041751": "-6020906132497041751",
                "1075271365553971033": "1075271365553971033",
                "5875376223618659061": "5875376223618659061",
                "-6619298593084354605": "-6619298593084354605",
                "920665384794843676": "920665384794843676",
                "-5414471856903252119": "-5414471856903252119",
                "6153875201821608022": "6153875201821608022",
                "-7566576191512734795": "-7566576191512734795",
                "5431522354128659980": "5431522354128659980",
                "8573128949023490133": "8573128949023490133",
                "6636349090309762466": "6636349090309762466",
                "-1945280238875071918": "-1945280238875071918",
                "85887372715911662": "85887372715911662",
                "8958069165418564517": "8958069165418564517",
                "9179563224617279765": "9179563224617279765",
                "-3164998467349078316": "-3164998467349078316",
                "5707183325353574539": "5707183325353574539",
                "7738350936944558119": "7738350936944558119",
                "2562146038922027486": "2562146038922027486",
                "5108790864766261685": "5108790864766261685",
                "6092123541748648923": "6092123541748648923",
                "6313617600947364171": "6313617600947364171",
                "-5629789300497356508": "-5629789300497356508",
                "-5906983703913358722": "-5906983703913358722",
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
                "-7892271018515113085": "-7892271018515113085_B2/acquisition",
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
                "1915213350897154053": "1915213350897154053",
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
                "-4689886691959901283": "-4689886691959901283",
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
                "8284456123398081785": "8284456123398081785_B4/acquisition",
            },
        },
    },
    "pulses": {
        "1915213350897154053": {
            "length": 40,
            "waveforms": {
                "I": "1915213350897154053_i",
                "Q": "1915213350897154053_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4689886691959901283": {
            "length": 40,
            "waveforms": {
                "I": "-4689886691959901283_i",
                "Q": "-4689886691959901283_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5376860812236258989": {
            "length": 80,
            "waveforms": {
                "single": "5376860812236258989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7892271018515113085_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4740057481262341669_i",
                "Q": "-4740057481262341669_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "8284456123398081785_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2601323522038299084_i",
                "Q": "-2601323522038299084_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "2298545585313633057": {
            "length": 80,
            "waveforms": {
                "single": "2298545585313633057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7904921271263004858": {
            "length": 16,
            "waveforms": {
                "single": "7904921271263004858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6019505032356543442": {
            "length": 16,
            "waveforms": {
                "single": "-6019505032356543442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4759883984831457805": {
            "length": 16,
            "waveforms": {
                "single": "4759883984831457805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-786295215329779096": {
            "length": 16,
            "waveforms": {
                "single": "-786295215329779096",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2559286289850256540": {
            "length": 16,
            "waveforms": {
                "single": "2559286289850256540",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1411464472673387767": {
            "length": 16,
            "waveforms": {
                "single": "1411464472673387767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1632958531872103015": {
            "length": 16,
            "waveforms": {
                "single": "1632958531872103015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6034396524649447354": {
            "length": 16,
            "waveforms": {
                "single": "-6034396524649447354",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3830718219875269878": {
            "length": 16,
            "waveforms": {
                "single": "3830718219875269878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2504419021822825917": {
            "length": 16,
            "waveforms": {
                "single": "-2504419021822825917",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2017898748267177399": {
            "length": 16,
            "waveforms": {
                "single": "2017898748267177399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9161321977608802144": {
            "length": 16,
            "waveforms": {
                "single": "-9161321977608802144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4215658436270344262": {
            "length": 16,
            "waveforms": {
                "single": "4215658436270344262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6963562289605635281": {
            "length": 16,
            "waveforms": {
                "single": "-6963562289605635281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8900342148319362948": {
            "length": 16,
            "waveforms": {
                "single": "-8900342148319362948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4378024378229359632": {
            "length": 16,
            "waveforms": {
                "single": "-4378024378229359632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4156530319030644384": {
            "length": 16,
            "waveforms": {
                "single": "-4156530319030644384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6578622073210560897": {
            "length": 20,
            "waveforms": {
                "single": "-6578622073210560897",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1958770631027477521": {
            "length": 20,
            "waveforms": {
                "single": "-1958770631027477521",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8894430563850002955": {
            "length": 20,
            "waveforms": {
                "single": "8894430563850002955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3274439185999286825": {
            "length": 20,
            "waveforms": {
                "single": "3274439185999286825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6022336007032927224": {
            "length": 24,
            "waveforms": {
                "single": "-6022336007032927224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5472198874002453688": {
            "length": 24,
            "waveforms": {
                "single": "5472198874002453688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1278524177744208660": {
            "length": 24,
            "waveforms": {
                "single": "-1278524177744208660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7741335382680333582": {
            "length": 24,
            "waveforms": {
                "single": "-7741335382680333582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9223073637681761243": {
            "length": 28,
            "waveforms": {
                "single": "-9223073637681761243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1017544348454769464": {
            "length": 28,
            "waveforms": {
                "single": "-1017544348454769464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7895941363439460939": {
            "length": 28,
            "waveforms": {
                "single": "-7895941363439460939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7674447304240745691": {
            "length": 28,
            "waveforms": {
                "single": "-7674447304240745691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7951641707656747905": {
            "length": 32,
            "waveforms": {
                "single": "-7951641707656747905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5476687616237578828": {
            "length": 32,
            "waveforms": {
                "single": "-5476687616237578828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7350065079621256658": {
            "length": 32,
            "waveforms": {
                "single": "7350065079621256658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7289507087845671307": {
            "length": 32,
            "waveforms": {
                "single": "-7289507087845671307",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5585682089086845900": {
            "length": 36,
            "waveforms": {
                "single": "-5585682089086845900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5091747399842504444": {
            "length": 36,
            "waveforms": {
                "single": "-5091747399842504444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7906351145798890331": {
            "length": 36,
            "waveforms": {
                "single": "7906351145798890331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "141462417184259902": {
            "length": 36,
            "waveforms": {
                "single": "141462417184259902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1355889428205039527": {
            "length": 40,
            "waveforms": {
                "single": "1355889428205039527",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-580890430508688140": {
            "length": 40,
            "waveforms": {
                "single": "-580890430508688140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2560716164386142013": {
            "length": 40,
            "waveforms": {
                "single": "2560716164386142013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2887929363682014828": {
            "length": 40,
            "waveforms": {
                "single": "-2887929363682014828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7793925981412906359": {
            "length": 44,
            "waveforms": {
                "single": "7793925981412906359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7736198964313704790": {
            "length": 44,
            "waveforms": {
                "single": "-7736198964313704790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3832148094411155351": {
            "length": 44,
            "waveforms": {
                "single": "3832148094411155351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8233564345094763146": {
            "length": 44,
            "waveforms": {
                "single": "-8233564345094763146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7860814059852494250": {
            "length": 48,
            "waveforms": {
                "single": "7860814059852494250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7583619656436492036": {
            "length": 48,
            "waveforms": {
                "single": "7583619656436492036",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-83735400085058333": {
            "length": 48,
            "waveforms": {
                "single": "-83735400085058333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4438582370004944983": {
            "length": 48,
            "waveforms": {
                "single": "4438582370004944983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3154960508827126157": {
            "length": 52,
            "waveforms": {
                "single": "-3154960508827126157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3432154912243128371": {
            "length": 52,
            "waveforms": {
                "single": "-3432154912243128371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3210660853044413123": {
            "length": 52,
            "waveforms": {
                "single": "-3210660853044413123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4994868436182578656": {
            "length": 52,
            "waveforms": {
                "single": "4994868436182578656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6355698139475960176": {
            "length": 56,
            "waveforms": {
                "single": "-6355698139475960176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4174981916396550554": {
            "length": 56,
            "waveforms": {
                "single": "4174981916396550554",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1572636746335029389": {
            "length": 56,
            "waveforms": {
                "single": "1572636746335029389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6020906132497041751": {
            "length": 56,
            "waveforms": {
                "single": "-6020906132497041751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1075271365553971033": {
            "length": 60,
            "waveforms": {
                "single": "1075271365553971033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5875376223618659061": {
            "length": 60,
            "waveforms": {
                "single": "5875376223618659061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6619298593084354605": {
            "length": 60,
            "waveforms": {
                "single": "-6619298593084354605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "920665384794843676": {
            "length": 60,
            "waveforms": {
                "single": "920665384794843676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5414471856903252119": {
            "length": 64,
            "waveforms": {
                "single": "-5414471856903252119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6153875201821608022": {
            "length": 64,
            "waveforms": {
                "single": "6153875201821608022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7566576191512734795": {
            "length": 64,
            "waveforms": {
                "single": "-7566576191512734795",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5431522354128659980": {
            "length": 64,
            "waveforms": {
                "single": "5431522354128659980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8573128949023490133": {
            "length": 68,
            "waveforms": {
                "single": "8573128949023490133",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6636349090309762466": {
            "length": 68,
            "waveforms": {
                "single": "6636349090309762466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1945280238875071918": {
            "length": 68,
            "waveforms": {
                "single": "-1945280238875071918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "85887372715911662": {
            "length": 68,
            "waveforms": {
                "single": "85887372715911662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8958069165418564517": {
            "length": 72,
            "waveforms": {
                "single": "8958069165418564517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9179563224617279765": {
            "length": 72,
            "waveforms": {
                "single": "9179563224617279765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3164998467349078316": {
            "length": 72,
            "waveforms": {
                "single": "-3164998467349078316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5707183325353574539": {
            "length": 72,
            "waveforms": {
                "single": "5707183325353574539",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7738350936944558119": {
            "length": 76,
            "waveforms": {
                "single": "7738350936944558119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2562146038922027486": {
            "length": 76,
            "waveforms": {
                "single": "2562146038922027486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5108790864766261685": {
            "length": 76,
            "waveforms": {
                "single": "5108790864766261685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6092123541748648923": {
            "length": 76,
            "waveforms": {
                "single": "6092123541748648923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6313617600947364171": {
            "length": 80,
            "waveforms": {
                "single": "6313617600947364171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5629789300497356508": {
            "length": 80,
            "waveforms": {
                "single": "-5629789300497356508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5906983703913358722": {
            "length": 80,
            "waveforms": {
                "single": "-5906983703913358722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1915213350897154053_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "1915213350897154053_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-4689886691959901283_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-4689886691959901283_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "5376860812236258989": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-4740057481262341669_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4740057481262341669_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2601323522038299084_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-2601323522038299084_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2298545585313633057": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7904921271263004858": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6019505032356543442": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
        },
        "4759883984831457805": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-786295215329779096": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2559286289850256540": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1411464472673387767": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "1632958531872103015": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-6034396524649447354": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "3830718219875269878": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-2504419021822825917": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "2017898748267177399": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-9161321977608802144": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "4215658436270344262": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-6963562289605635281": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8900342148319362948": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4378024378229359632": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-4156530319030644384": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6578622073210560897": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1958770631027477521": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8894430563850002955": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
        },
        "3274439185999286825": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6022336007032927224": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5472198874002453688": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1278524177744208660": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-7741335382680333582": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-9223073637681761243": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1017544348454769464": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7895941363439460939": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-7674447304240745691": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-7951641707656747905": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5476687616237578828": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7350065079621256658": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-7289507087845671307": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5585682089086845900": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5091747399842504444": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7906351145798890331": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
        },
        "141462417184259902": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1355889428205039527": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-580890430508688140": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2560716164386142013": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-2887929363682014828": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7793925981412906359": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7736198964313704790": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3832148094411155351": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8233564345094763146": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7860814059852494250": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7583619656436492036": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-83735400085058333": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
        },
        "4438582370004944983": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3154960508827126157": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3432154912243128371": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3210660853044413123": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
        },
        "4994868436182578656": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6355698139475960176": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4174981916396550554": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1572636746335029389": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-6020906132497041751": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1075271365553971033": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5875376223618659061": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6619298593084354605": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
        },
        "920665384794843676": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5414471856903252119": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6153875201821608022": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7566576191512734795": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
        },
        "5431522354128659980": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8573128949023490133": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6636349090309762466": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1945280238875071918": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
        },
        "85887372715911662": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8958069165418564517": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9179563224617279765": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3164998467349078316": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
        },
        "5707183325353574539": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7738350936944558119": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2562146038922027486": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5108790864766261685": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6092123541748648923": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6313617600947364171": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5629789300497356508": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5906983703913358722": {
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
                "5376860812236258989": "5376860812236258989",
                "2298545585313633057": "2298545585313633057",
                "7904921271263004858": "7904921271263004858",
                "-6019505032356543442": "-6019505032356543442",
                "4759883984831457805": "4759883984831457805",
                "-786295215329779096": "-786295215329779096",
                "2559286289850256540": "2559286289850256540",
                "1411464472673387767": "1411464472673387767",
                "1632958531872103015": "1632958531872103015",
                "-6034396524649447354": "-6034396524649447354",
                "3830718219875269878": "3830718219875269878",
                "-2504419021822825917": "-2504419021822825917",
                "2017898748267177399": "2017898748267177399",
                "-9161321977608802144": "-9161321977608802144",
                "4215658436270344262": "4215658436270344262",
                "-6963562289605635281": "-6963562289605635281",
                "-8900342148319362948": "-8900342148319362948",
                "-4378024378229359632": "-4378024378229359632",
                "-4156530319030644384": "-4156530319030644384",
                "-6578622073210560897": "-6578622073210560897",
                "-1958770631027477521": "-1958770631027477521",
                "8894430563850002955": "8894430563850002955",
                "3274439185999286825": "3274439185999286825",
                "-6022336007032927224": "-6022336007032927224",
                "5472198874002453688": "5472198874002453688",
                "-1278524177744208660": "-1278524177744208660",
                "-7741335382680333582": "-7741335382680333582",
                "-9223073637681761243": "-9223073637681761243",
                "-1017544348454769464": "-1017544348454769464",
                "-7895941363439460939": "-7895941363439460939",
                "-7674447304240745691": "-7674447304240745691",
                "-7951641707656747905": "-7951641707656747905",
                "-5476687616237578828": "-5476687616237578828",
                "7350065079621256658": "7350065079621256658",
                "-7289507087845671307": "-7289507087845671307",
                "-5585682089086845900": "-5585682089086845900",
                "-5091747399842504444": "-5091747399842504444",
                "7906351145798890331": "7906351145798890331",
                "141462417184259902": "141462417184259902",
                "1355889428205039527": "1355889428205039527",
                "-580890430508688140": "-580890430508688140",
                "2560716164386142013": "2560716164386142013",
                "-2887929363682014828": "-2887929363682014828",
                "7793925981412906359": "7793925981412906359",
                "-7736198964313704790": "-7736198964313704790",
                "3832148094411155351": "3832148094411155351",
                "-8233564345094763146": "-8233564345094763146",
                "7860814059852494250": "7860814059852494250",
                "7583619656436492036": "7583619656436492036",
                "-83735400085058333": "-83735400085058333",
                "4438582370004944983": "4438582370004944983",
                "-3154960508827126157": "-3154960508827126157",
                "-3432154912243128371": "-3432154912243128371",
                "-3210660853044413123": "-3210660853044413123",
                "4994868436182578656": "4994868436182578656",
                "-6355698139475960176": "-6355698139475960176",
                "4174981916396550554": "4174981916396550554",
                "1572636746335029389": "1572636746335029389",
                "-6020906132497041751": "-6020906132497041751",
                "1075271365553971033": "1075271365553971033",
                "5875376223618659061": "5875376223618659061",
                "-6619298593084354605": "-6619298593084354605",
                "920665384794843676": "920665384794843676",
                "-5414471856903252119": "-5414471856903252119",
                "6153875201821608022": "6153875201821608022",
                "-7566576191512734795": "-7566576191512734795",
                "5431522354128659980": "5431522354128659980",
                "8573128949023490133": "8573128949023490133",
                "6636349090309762466": "6636349090309762466",
                "-1945280238875071918": "-1945280238875071918",
                "85887372715911662": "85887372715911662",
                "8958069165418564517": "8958069165418564517",
                "9179563224617279765": "9179563224617279765",
                "-3164998467349078316": "-3164998467349078316",
                "5707183325353574539": "5707183325353574539",
                "7738350936944558119": "7738350936944558119",
                "2562146038922027486": "2562146038922027486",
                "5108790864766261685": "5108790864766261685",
                "6092123541748648923": "6092123541748648923",
                "6313617600947364171": "6313617600947364171",
                "-5629789300497356508": "-5629789300497356508",
                "-5906983703913358722": "-5906983703913358722",
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
                "-7892271018515113085": "-7892271018515113085_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_15b",
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
                "1915213350897154053": "1915213350897154053",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_d64",
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
                "-4689886691959901283": "-4689886691959901283",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_909",
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
                "8284456123398081785": "8284456123398081785_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_8f1",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "1915213350897154053": {
            "length": 40,
            "waveforms": {
                "I": "1915213350897154053_i",
                "Q": "1915213350897154053_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4689886691959901283": {
            "length": 40,
            "waveforms": {
                "I": "-4689886691959901283_i",
                "Q": "-4689886691959901283_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5376860812236258989": {
            "length": 80,
            "waveforms": {
                "single": "5376860812236258989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7892271018515113085_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4740057481262341669_i",
                "Q": "-4740057481262341669_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "8284456123398081785_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2601323522038299084_i",
                "Q": "-2601323522038299084_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "2298545585313633057": {
            "length": 80,
            "waveforms": {
                "single": "2298545585313633057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7904921271263004858": {
            "length": 16,
            "waveforms": {
                "single": "7904921271263004858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6019505032356543442": {
            "length": 16,
            "waveforms": {
                "single": "-6019505032356543442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4759883984831457805": {
            "length": 16,
            "waveforms": {
                "single": "4759883984831457805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-786295215329779096": {
            "length": 16,
            "waveforms": {
                "single": "-786295215329779096",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2559286289850256540": {
            "length": 16,
            "waveforms": {
                "single": "2559286289850256540",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1411464472673387767": {
            "length": 16,
            "waveforms": {
                "single": "1411464472673387767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1632958531872103015": {
            "length": 16,
            "waveforms": {
                "single": "1632958531872103015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6034396524649447354": {
            "length": 16,
            "waveforms": {
                "single": "-6034396524649447354",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3830718219875269878": {
            "length": 16,
            "waveforms": {
                "single": "3830718219875269878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2504419021822825917": {
            "length": 16,
            "waveforms": {
                "single": "-2504419021822825917",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2017898748267177399": {
            "length": 16,
            "waveforms": {
                "single": "2017898748267177399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9161321977608802144": {
            "length": 16,
            "waveforms": {
                "single": "-9161321977608802144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4215658436270344262": {
            "length": 16,
            "waveforms": {
                "single": "4215658436270344262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6963562289605635281": {
            "length": 16,
            "waveforms": {
                "single": "-6963562289605635281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8900342148319362948": {
            "length": 16,
            "waveforms": {
                "single": "-8900342148319362948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4378024378229359632": {
            "length": 16,
            "waveforms": {
                "single": "-4378024378229359632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4156530319030644384": {
            "length": 16,
            "waveforms": {
                "single": "-4156530319030644384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6578622073210560897": {
            "length": 20,
            "waveforms": {
                "single": "-6578622073210560897",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1958770631027477521": {
            "length": 20,
            "waveforms": {
                "single": "-1958770631027477521",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8894430563850002955": {
            "length": 20,
            "waveforms": {
                "single": "8894430563850002955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3274439185999286825": {
            "length": 20,
            "waveforms": {
                "single": "3274439185999286825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6022336007032927224": {
            "length": 24,
            "waveforms": {
                "single": "-6022336007032927224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5472198874002453688": {
            "length": 24,
            "waveforms": {
                "single": "5472198874002453688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1278524177744208660": {
            "length": 24,
            "waveforms": {
                "single": "-1278524177744208660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7741335382680333582": {
            "length": 24,
            "waveforms": {
                "single": "-7741335382680333582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9223073637681761243": {
            "length": 28,
            "waveforms": {
                "single": "-9223073637681761243",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1017544348454769464": {
            "length": 28,
            "waveforms": {
                "single": "-1017544348454769464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7895941363439460939": {
            "length": 28,
            "waveforms": {
                "single": "-7895941363439460939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7674447304240745691": {
            "length": 28,
            "waveforms": {
                "single": "-7674447304240745691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7951641707656747905": {
            "length": 32,
            "waveforms": {
                "single": "-7951641707656747905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5476687616237578828": {
            "length": 32,
            "waveforms": {
                "single": "-5476687616237578828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7350065079621256658": {
            "length": 32,
            "waveforms": {
                "single": "7350065079621256658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7289507087845671307": {
            "length": 32,
            "waveforms": {
                "single": "-7289507087845671307",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5585682089086845900": {
            "length": 36,
            "waveforms": {
                "single": "-5585682089086845900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5091747399842504444": {
            "length": 36,
            "waveforms": {
                "single": "-5091747399842504444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7906351145798890331": {
            "length": 36,
            "waveforms": {
                "single": "7906351145798890331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "141462417184259902": {
            "length": 36,
            "waveforms": {
                "single": "141462417184259902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1355889428205039527": {
            "length": 40,
            "waveforms": {
                "single": "1355889428205039527",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-580890430508688140": {
            "length": 40,
            "waveforms": {
                "single": "-580890430508688140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2560716164386142013": {
            "length": 40,
            "waveforms": {
                "single": "2560716164386142013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2887929363682014828": {
            "length": 40,
            "waveforms": {
                "single": "-2887929363682014828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7793925981412906359": {
            "length": 44,
            "waveforms": {
                "single": "7793925981412906359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7736198964313704790": {
            "length": 44,
            "waveforms": {
                "single": "-7736198964313704790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3832148094411155351": {
            "length": 44,
            "waveforms": {
                "single": "3832148094411155351",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8233564345094763146": {
            "length": 44,
            "waveforms": {
                "single": "-8233564345094763146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7860814059852494250": {
            "length": 48,
            "waveforms": {
                "single": "7860814059852494250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7583619656436492036": {
            "length": 48,
            "waveforms": {
                "single": "7583619656436492036",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-83735400085058333": {
            "length": 48,
            "waveforms": {
                "single": "-83735400085058333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4438582370004944983": {
            "length": 48,
            "waveforms": {
                "single": "4438582370004944983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3154960508827126157": {
            "length": 52,
            "waveforms": {
                "single": "-3154960508827126157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3432154912243128371": {
            "length": 52,
            "waveforms": {
                "single": "-3432154912243128371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3210660853044413123": {
            "length": 52,
            "waveforms": {
                "single": "-3210660853044413123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4994868436182578656": {
            "length": 52,
            "waveforms": {
                "single": "4994868436182578656",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6355698139475960176": {
            "length": 56,
            "waveforms": {
                "single": "-6355698139475960176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4174981916396550554": {
            "length": 56,
            "waveforms": {
                "single": "4174981916396550554",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1572636746335029389": {
            "length": 56,
            "waveforms": {
                "single": "1572636746335029389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6020906132497041751": {
            "length": 56,
            "waveforms": {
                "single": "-6020906132497041751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1075271365553971033": {
            "length": 60,
            "waveforms": {
                "single": "1075271365553971033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5875376223618659061": {
            "length": 60,
            "waveforms": {
                "single": "5875376223618659061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6619298593084354605": {
            "length": 60,
            "waveforms": {
                "single": "-6619298593084354605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "920665384794843676": {
            "length": 60,
            "waveforms": {
                "single": "920665384794843676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5414471856903252119": {
            "length": 64,
            "waveforms": {
                "single": "-5414471856903252119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6153875201821608022": {
            "length": 64,
            "waveforms": {
                "single": "6153875201821608022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7566576191512734795": {
            "length": 64,
            "waveforms": {
                "single": "-7566576191512734795",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5431522354128659980": {
            "length": 64,
            "waveforms": {
                "single": "5431522354128659980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8573128949023490133": {
            "length": 68,
            "waveforms": {
                "single": "8573128949023490133",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6636349090309762466": {
            "length": 68,
            "waveforms": {
                "single": "6636349090309762466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1945280238875071918": {
            "length": 68,
            "waveforms": {
                "single": "-1945280238875071918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "85887372715911662": {
            "length": 68,
            "waveforms": {
                "single": "85887372715911662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8958069165418564517": {
            "length": 72,
            "waveforms": {
                "single": "8958069165418564517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9179563224617279765": {
            "length": 72,
            "waveforms": {
                "single": "9179563224617279765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3164998467349078316": {
            "length": 72,
            "waveforms": {
                "single": "-3164998467349078316",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5707183325353574539": {
            "length": 72,
            "waveforms": {
                "single": "5707183325353574539",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7738350936944558119": {
            "length": 76,
            "waveforms": {
                "single": "7738350936944558119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2562146038922027486": {
            "length": 76,
            "waveforms": {
                "single": "2562146038922027486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5108790864766261685": {
            "length": 76,
            "waveforms": {
                "single": "5108790864766261685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6092123541748648923": {
            "length": 76,
            "waveforms": {
                "single": "6092123541748648923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6313617600947364171": {
            "length": 80,
            "waveforms": {
                "single": "6313617600947364171",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5629789300497356508": {
            "length": 80,
            "waveforms": {
                "single": "-5629789300497356508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5906983703913358722": {
            "length": 80,
            "waveforms": {
                "single": "-5906983703913358722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1915213350897154053_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1915213350897154053_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4689886691959901283_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4689886691959901283_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5376860812236258989": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-4740057481262341669_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4740057481262341669_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2601323522038299084_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-2601323522038299084_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2298545585313633057": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7904921271263004858": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6019505032356543442": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4759883984831457805": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-786295215329779096": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2559286289850256540": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1411464472673387767": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1632958531872103015": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6034396524649447354": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3830718219875269878": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2504419021822825917": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2017898748267177399": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9161321977608802144": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4215658436270344262": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6963562289605635281": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8900342148319362948": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4378024378229359632": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4156530319030644384": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6578622073210560897": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1958770631027477521": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8894430563850002955": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3274439185999286825": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6022336007032927224": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5472198874002453688": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1278524177744208660": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7741335382680333582": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-9223073637681761243": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1017544348454769464": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7895941363439460939": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7674447304240745691": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-7951641707656747905": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5476687616237578828": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7350065079621256658": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7289507087845671307": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5585682089086845900": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5091747399842504444": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7906351145798890331": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "141462417184259902": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1355889428205039527": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-580890430508688140": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2560716164386142013": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2887929363682014828": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7793925981412906359": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7736198964313704790": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3832148094411155351": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8233564345094763146": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7860814059852494250": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7583619656436492036": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-83735400085058333": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4438582370004944983": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3154960508827126157": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3432154912243128371": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3210660853044413123": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4994868436182578656": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-6355698139475960176": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4174981916396550554": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1572636746335029389": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6020906132497041751": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "1075271365553971033": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5875376223618659061": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6619298593084354605": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "920665384794843676": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5414471856903252119": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6153875201821608022": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7566576191512734795": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5431522354128659980": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8573128949023490133": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6636349090309762466": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1945280238875071918": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "85887372715911662": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "8958069165418564517": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9179563224617279765": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3164998467349078316": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5707183325353574539": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "7738350936944558119": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2562146038922027486": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5108790864766261685": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6092123541748648923": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6313617600947364171": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5629789300497356508": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5906983703913358722": {
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
        "B2/acquisition_mixer_15b": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_d64": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_909": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_8f1": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

