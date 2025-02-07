
# Single QUA script generated at 2025-02-07 14:08:05.966878
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
            with for_(v9,-1.9900000000000002,(v9<-0.797989999999999),(v9+0.003980000000000095)):
                align()
                play("4382332537801879775", "B2/drive")
                play("-2222767505055175561", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-4602261668386679696"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("8298303205161635019"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-7231821740564976130"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-5200654128973992550"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-7729187121346034486"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("3050201895841966761"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-5531427433342867623"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("420641823663670327"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("-7344246904950960102"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-7122752845752244854"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-8066599752643908144"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-4924993157749077991"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("8073105387892316784"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("4706574042262054483"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("7253218868106288682"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("2505976347280853218"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("8458045604287391168"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-7513744378002991371"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("6305941269677908492"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("857295741609751651"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-3889946779215683813"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("7806074242747205455"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("138719186225655086"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-4488339239802996667"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-681167333560373016"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("3762516785012962644"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("1410151116250668424"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("1132956712834666210"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("590264596464640322"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-7077090460056910047"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("1795091332645742808"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("8740093541474345135"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("3992851020648909671"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("8242728160693286779"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-1331834120313611982"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-2275681027205275272"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-2054186968006560024"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-1070854291024172786"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("8849162436287076411"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-7621316008618023590"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("5376782537023371185"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("5598276596222086433"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("6581609273204473671"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-1501331593365643251"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("31147555610622867"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("5983216812617160817"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-4923563283213192518"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-4212671236276431488"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("5828610831858033460"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-6364775570885914164"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("5331245451076975104"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("2728900281015453939"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-5187163736821586947"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-7789508906883108112"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-1286171734618277175"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-1064677675419561927"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-1341872078835564141"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("2465299827407059510"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-8441480268423293825"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-679737459024487543"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("-956931862440489757"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("2850240043802133894"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("-3930623299089477521"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("4941558493613175334"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("-6131220994070678786"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-1608903223980675470"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-3545683082694403137"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("-3324189023495687889"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("5547992769206964966"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("-1126429335492521026"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("-1002468948386885838"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("4106780481534243320"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("7248387076429073473"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-4253354788451875816"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("3952174500775115963"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("-7398392074883422869"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("3454809119994057607"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-3868414572056801432"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("3399108775776770641"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("32577430146508340"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("-2319788238615785880"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("-4644346320702622333"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("8182406375156213153"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("-6457165792310714812"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("7685040994375154797"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("3629443011412717668"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("3008117243526024124"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("-5185733862285701474"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("1195297771917931645"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("-7386331557266902739"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("-7164837498068187491"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("7915375230011101824"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("2466729701942944983"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("-5200625354578605386"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("4664489389946111846"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("4885983449144827094"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("-2878905279469803335"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("-8327550807537960176"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("-5508465351648099769"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("5270923665539901478"*amp(v9), "B4/flux")
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
                play("-2222767505055175561", "B4/drive")
                measure("-8575187705376057317", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.06078547221045674)-(v3*0.9981508535127102))>0.0025565952953590303)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-3799175348537557238", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.6665903597333165)-(v6*0.7454242364657911))>-0.0004342766968863211)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(300).buffer(100).average().save("-8575187705376057317_B2|acquisition_shots")
        r2.buffer(300).buffer(100).average().save("-3799175348537557238_B4|acquisition_shots")


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
                "673250404584448585": "673250404584448585",
                "-5908297060336078065": "-5908297060336078065",
                "-4602261668386679696": "-4602261668386679696",
                "8298303205161635019": "8298303205161635019",
                "-7231821740564976130": "-7231821740564976130",
                "-5200654128973992550": "-5200654128973992550",
                "-7729187121346034486": "-7729187121346034486",
                "3050201895841966761": "3050201895841966761",
                "-5531427433342867623": "-5531427433342867623",
                "420641823663670327": "420641823663670327",
                "-7344246904950960102": "-7344246904950960102",
                "-7122752845752244854": "-7122752845752244854",
                "-8066599752643908144": "-8066599752643908144",
                "-4924993157749077991": "-4924993157749077991",
                "8073105387892316784": "8073105387892316784",
                "4706574042262054483": "4706574042262054483",
                "7253218868106288682": "7253218868106288682",
                "2505976347280853218": "2505976347280853218",
                "8458045604287391168": "8458045604287391168",
                "-7513744378002991371": "-7513744378002991371",
                "6305941269677908492": "6305941269677908492",
                "857295741609751651": "857295741609751651",
                "-3889946779215683813": "-3889946779215683813",
                "7806074242747205455": "7806074242747205455",
                "138719186225655086": "138719186225655086",
                "-4488339239802996667": "-4488339239802996667",
                "-681167333560373016": "-681167333560373016",
                "3762516785012962644": "3762516785012962644",
                "1410151116250668424": "1410151116250668424",
                "1132956712834666210": "1132956712834666210",
                "590264596464640322": "590264596464640322",
                "-7077090460056910047": "-7077090460056910047",
                "1795091332645742808": "1795091332645742808",
                "8740093541474345135": "8740093541474345135",
                "3992851020648909671": "3992851020648909671",
                "8242728160693286779": "8242728160693286779",
                "-1331834120313611982": "-1331834120313611982",
                "-2275681027205275272": "-2275681027205275272",
                "-2054186968006560024": "-2054186968006560024",
                "-1070854291024172786": "-1070854291024172786",
                "8849162436287076411": "8849162436287076411",
                "-7621316008618023590": "-7621316008618023590",
                "5376782537023371185": "5376782537023371185",
                "5598276596222086433": "5598276596222086433",
                "6581609273204473671": "6581609273204473671",
                "-1501331593365643251": "-1501331593365643251",
                "31147555610622867": "31147555610622867",
                "5983216812617160817": "5983216812617160817",
                "-4923563283213192518": "-4923563283213192518",
                "-4212671236276431488": "-4212671236276431488",
                "5828610831858033460": "5828610831858033460",
                "-6364775570885914164": "-6364775570885914164",
                "5331245451076975104": "5331245451076975104",
                "2728900281015453939": "2728900281015453939",
                "-5187163736821586947": "-5187163736821586947",
                "-7789508906883108112": "-7789508906883108112",
                "-1286171734618277175": "-1286171734618277175",
                "-1064677675419561927": "-1064677675419561927",
                "-1341872078835564141": "-1341872078835564141",
                "2465299827407059510": "2465299827407059510",
                "-8441480268423293825": "-8441480268423293825",
                "-679737459024487543": "-679737459024487543",
                "-956931862440489757": "-956931862440489757",
                "2850240043802133894": "2850240043802133894",
                "-3930623299089477521": "-3930623299089477521",
                "4941558493613175334": "4941558493613175334",
                "-6131220994070678786": "-6131220994070678786",
                "-1608903223980675470": "-1608903223980675470",
                "-3545683082694403137": "-3545683082694403137",
                "-3324189023495687889": "-3324189023495687889",
                "5547992769206964966": "5547992769206964966",
                "-1126429335492521026": "-1126429335492521026",
                "-1002468948386885838": "-1002468948386885838",
                "4106780481534243320": "4106780481534243320",
                "7248387076429073473": "7248387076429073473",
                "-4253354788451875816": "-4253354788451875816",
                "3952174500775115963": "3952174500775115963",
                "-7398392074883422869": "-7398392074883422869",
                "3454809119994057607": "3454809119994057607",
                "-3868414572056801432": "-3868414572056801432",
                "3399108775776770641": "3399108775776770641",
                "32577430146508340": "32577430146508340",
                "-2319788238615785880": "-2319788238615785880",
                "-4644346320702622333": "-4644346320702622333",
                "8182406375156213153": "8182406375156213153",
                "-6457165792310714812": "-6457165792310714812",
                "7685040994375154797": "7685040994375154797",
                "3629443011412717668": "3629443011412717668",
                "3008117243526024124": "3008117243526024124",
                "-5185733862285701474": "-5185733862285701474",
                "1195297771917931645": "1195297771917931645",
                "-7386331557266902739": "-7386331557266902739",
                "-7164837498068187491": "-7164837498068187491",
                "7915375230011101824": "7915375230011101824",
                "2466729701942944983": "2466729701942944983",
                "-5200625354578605386": "-5200625354578605386",
                "4664489389946111846": "4664489389946111846",
                "4885983449144827094": "4885983449144827094",
                "-2878905279469803335": "-2878905279469803335",
                "-8327550807537960176": "-8327550807537960176",
                "-5508465351648099769": "-5508465351648099769",
                "5270923665539901478": "5270923665539901478",
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
                "4382332537801879775": "4382332537801879775",
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
                "-2222767505055175561": "-2222767505055175561",
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
                "-8575187705376057317": "-8575187705376057317_B2/acquisition",
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
                "-3799175348537557238": "-3799175348537557238_B4/acquisition",
            },
        },
    },
    "pulses": {
        "4382332537801879775": {
            "length": 40,
            "waveforms": {
                "I": "4382332537801879775_i",
                "Q": "4382332537801879775_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2222767505055175561": {
            "length": 40,
            "waveforms": {
                "I": "-2222767505055175561_i",
                "Q": "-2222767505055175561_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "673250404584448585": {
            "length": 100,
            "waveforms": {
                "single": "673250404584448585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8575187705376057317_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1985196688154687140_i",
                "Q": "1985196688154687140_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-3799175348537557238_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4123930647378729725_i",
                "Q": "4123930647378729725_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-5908297060336078065": {
            "length": 100,
            "waveforms": {
                "single": "-5908297060336078065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4602261668386679696": {
            "length": 16,
            "waveforms": {
                "single": "-4602261668386679696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8298303205161635019": {
            "length": 16,
            "waveforms": {
                "single": "8298303205161635019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7231821740564976130": {
            "length": 16,
            "waveforms": {
                "single": "-7231821740564976130",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5200654128973992550": {
            "length": 16,
            "waveforms": {
                "single": "-5200654128973992550",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7729187121346034486": {
            "length": 16,
            "waveforms": {
                "single": "-7729187121346034486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3050201895841966761": {
            "length": 16,
            "waveforms": {
                "single": "3050201895841966761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5531427433342867623": {
            "length": 16,
            "waveforms": {
                "single": "-5531427433342867623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "420641823663670327": {
            "length": 16,
            "waveforms": {
                "single": "420641823663670327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7344246904950960102": {
            "length": 16,
            "waveforms": {
                "single": "-7344246904950960102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7122752845752244854": {
            "length": 16,
            "waveforms": {
                "single": "-7122752845752244854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8066599752643908144": {
            "length": 16,
            "waveforms": {
                "single": "-8066599752643908144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4924993157749077991": {
            "length": 16,
            "waveforms": {
                "single": "-4924993157749077991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8073105387892316784": {
            "length": 16,
            "waveforms": {
                "single": "8073105387892316784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4706574042262054483": {
            "length": 16,
            "waveforms": {
                "single": "4706574042262054483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7253218868106288682": {
            "length": 16,
            "waveforms": {
                "single": "7253218868106288682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2505976347280853218": {
            "length": 16,
            "waveforms": {
                "single": "2505976347280853218",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8458045604287391168": {
            "length": 16,
            "waveforms": {
                "single": "8458045604287391168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7513744378002991371": {
            "length": 20,
            "waveforms": {
                "single": "-7513744378002991371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6305941269677908492": {
            "length": 20,
            "waveforms": {
                "single": "6305941269677908492",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "857295741609751651": {
            "length": 20,
            "waveforms": {
                "single": "857295741609751651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3889946779215683813": {
            "length": 20,
            "waveforms": {
                "single": "-3889946779215683813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7806074242747205455": {
            "length": 24,
            "waveforms": {
                "single": "7806074242747205455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "138719186225655086": {
            "length": 24,
            "waveforms": {
                "single": "138719186225655086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4488339239802996667": {
            "length": 24,
            "waveforms": {
                "single": "-4488339239802996667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-681167333560373016": {
            "length": 24,
            "waveforms": {
                "single": "-681167333560373016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3762516785012962644": {
            "length": 28,
            "waveforms": {
                "single": "3762516785012962644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1410151116250668424": {
            "length": 28,
            "waveforms": {
                "single": "1410151116250668424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1132956712834666210": {
            "length": 28,
            "waveforms": {
                "single": "1132956712834666210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "590264596464640322": {
            "length": 28,
            "waveforms": {
                "single": "590264596464640322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7077090460056910047": {
            "length": 32,
            "waveforms": {
                "single": "-7077090460056910047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1795091332645742808": {
            "length": 32,
            "waveforms": {
                "single": "1795091332645742808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8740093541474345135": {
            "length": 32,
            "waveforms": {
                "single": "8740093541474345135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3992851020648909671": {
            "length": 32,
            "waveforms": {
                "single": "3992851020648909671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8242728160693286779": {
            "length": 36,
            "waveforms": {
                "single": "8242728160693286779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1331834120313611982": {
            "length": 36,
            "waveforms": {
                "single": "-1331834120313611982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2275681027205275272": {
            "length": 36,
            "waveforms": {
                "single": "-2275681027205275272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2054186968006560024": {
            "length": 36,
            "waveforms": {
                "single": "-2054186968006560024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1070854291024172786": {
            "length": 40,
            "waveforms": {
                "single": "-1070854291024172786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8849162436287076411": {
            "length": 40,
            "waveforms": {
                "single": "8849162436287076411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7621316008618023590": {
            "length": 40,
            "waveforms": {
                "single": "-7621316008618023590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5376782537023371185": {
            "length": 40,
            "waveforms": {
                "single": "5376782537023371185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5598276596222086433": {
            "length": 44,
            "waveforms": {
                "single": "5598276596222086433",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6581609273204473671": {
            "length": 44,
            "waveforms": {
                "single": "6581609273204473671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1501331593365643251": {
            "length": 44,
            "waveforms": {
                "single": "-1501331593365643251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "31147555610622867": {
            "length": 44,
            "waveforms": {
                "single": "31147555610622867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5983216812617160817": {
            "length": 48,
            "waveforms": {
                "single": "5983216812617160817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4923563283213192518": {
            "length": 48,
            "waveforms": {
                "single": "-4923563283213192518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4212671236276431488": {
            "length": 48,
            "waveforms": {
                "single": "-4212671236276431488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5828610831858033460": {
            "length": 48,
            "waveforms": {
                "single": "5828610831858033460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6364775570885914164": {
            "length": 52,
            "waveforms": {
                "single": "-6364775570885914164",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5331245451076975104": {
            "length": 52,
            "waveforms": {
                "single": "5331245451076975104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2728900281015453939": {
            "length": 52,
            "waveforms": {
                "single": "2728900281015453939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5187163736821586947": {
            "length": 52,
            "waveforms": {
                "single": "-5187163736821586947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7789508906883108112": {
            "length": 56,
            "waveforms": {
                "single": "-7789508906883108112",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1286171734618277175": {
            "length": 56,
            "waveforms": {
                "single": "-1286171734618277175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1064677675419561927": {
            "length": 56,
            "waveforms": {
                "single": "-1064677675419561927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1341872078835564141": {
            "length": 56,
            "waveforms": {
                "single": "-1341872078835564141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2465299827407059510": {
            "length": 60,
            "waveforms": {
                "single": "2465299827407059510",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8441480268423293825": {
            "length": 60,
            "waveforms": {
                "single": "-8441480268423293825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-679737459024487543": {
            "length": 60,
            "waveforms": {
                "single": "-679737459024487543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-956931862440489757": {
            "length": 60,
            "waveforms": {
                "single": "-956931862440489757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2850240043802133894": {
            "length": 64,
            "waveforms": {
                "single": "2850240043802133894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3930623299089477521": {
            "length": 64,
            "waveforms": {
                "single": "-3930623299089477521",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4941558493613175334": {
            "length": 64,
            "waveforms": {
                "single": "4941558493613175334",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6131220994070678786": {
            "length": 64,
            "waveforms": {
                "single": "-6131220994070678786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1608903223980675470": {
            "length": 68,
            "waveforms": {
                "single": "-1608903223980675470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3545683082694403137": {
            "length": 68,
            "waveforms": {
                "single": "-3545683082694403137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3324189023495687889": {
            "length": 68,
            "waveforms": {
                "single": "-3324189023495687889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5547992769206964966": {
            "length": 68,
            "waveforms": {
                "single": "5547992769206964966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1126429335492521026": {
            "length": 72,
            "waveforms": {
                "single": "-1126429335492521026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1002468948386885838": {
            "length": 72,
            "waveforms": {
                "single": "-1002468948386885838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4106780481534243320": {
            "length": 72,
            "waveforms": {
                "single": "4106780481534243320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7248387076429073473": {
            "length": 72,
            "waveforms": {
                "single": "7248387076429073473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4253354788451875816": {
            "length": 76,
            "waveforms": {
                "single": "-4253354788451875816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3952174500775115963": {
            "length": 76,
            "waveforms": {
                "single": "3952174500775115963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7398392074883422869": {
            "length": 76,
            "waveforms": {
                "single": "-7398392074883422869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3454809119994057607": {
            "length": 76,
            "waveforms": {
                "single": "3454809119994057607",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3868414572056801432": {
            "length": 80,
            "waveforms": {
                "single": "-3868414572056801432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3399108775776770641": {
            "length": 80,
            "waveforms": {
                "single": "3399108775776770641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "32577430146508340": {
            "length": 80,
            "waveforms": {
                "single": "32577430146508340",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2319788238615785880": {
            "length": 80,
            "waveforms": {
                "single": "-2319788238615785880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4644346320702622333": {
            "length": 84,
            "waveforms": {
                "single": "-4644346320702622333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8182406375156213153": {
            "length": 84,
            "waveforms": {
                "single": "8182406375156213153",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6457165792310714812": {
            "length": 84,
            "waveforms": {
                "single": "-6457165792310714812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7685040994375154797": {
            "length": 84,
            "waveforms": {
                "single": "7685040994375154797",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3629443011412717668": {
            "length": 88,
            "waveforms": {
                "single": "3629443011412717668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3008117243526024124": {
            "length": 88,
            "waveforms": {
                "single": "3008117243526024124",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5185733862285701474": {
            "length": 88,
            "waveforms": {
                "single": "-5185733862285701474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1195297771917931645": {
            "length": 88,
            "waveforms": {
                "single": "1195297771917931645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7386331557266902739": {
            "length": 92,
            "waveforms": {
                "single": "-7386331557266902739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7164837498068187491": {
            "length": 92,
            "waveforms": {
                "single": "-7164837498068187491",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7915375230011101824": {
            "length": 92,
            "waveforms": {
                "single": "7915375230011101824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2466729701942944983": {
            "length": 92,
            "waveforms": {
                "single": "2466729701942944983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5200625354578605386": {
            "length": 96,
            "waveforms": {
                "single": "-5200625354578605386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4664489389946111846": {
            "length": 96,
            "waveforms": {
                "single": "4664489389946111846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4885983449144827094": {
            "length": 96,
            "waveforms": {
                "single": "4885983449144827094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2878905279469803335": {
            "length": 96,
            "waveforms": {
                "single": "-2878905279469803335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8327550807537960176": {
            "length": 100,
            "waveforms": {
                "single": "-8327550807537960176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5508465351648099769": {
            "length": 100,
            "waveforms": {
                "single": "-5508465351648099769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5270923665539901478": {
            "length": 100,
            "waveforms": {
                "single": "5270923665539901478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "4382332537801879775_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "4382332537801879775_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-2222767505055175561_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-2222767505055175561_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "673250404584448585": {
            "sample": -0.2388,
            "type": "constant",
        },
        "1985196688154687140_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "1985196688154687140_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4123930647378729725_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4123930647378729725_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5908297060336078065": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4602261668386679696": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8298303205161635019": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-7231821740564976130": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-5200654128973992550": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-7729187121346034486": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "3050201895841966761": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-5531427433342867623": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "420641823663670327": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-7344246904950960102": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-7122752845752244854": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8066599752643908144": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-4924993157749077991": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8073105387892316784": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "4706574042262054483": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7253218868106288682": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2505976347280853218": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "8458045604287391168": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7513744378002991371": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6305941269677908492": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "857295741609751651": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-3889946779215683813": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "7806074242747205455": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "138719186225655086": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4488339239802996667": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-681167333560373016": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3762516785012962644": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1410151116250668424": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1132956712834666210": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "590264596464640322": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7077090460056910047": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1795091332645742808": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8740093541474345135": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "3992851020648909671": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8242728160693286779": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1331834120313611982": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2275681027205275272": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-2054186968006560024": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1070854291024172786": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8849162436287076411": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7621316008618023590": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "5376782537023371185": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5598276596222086433": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6581609273204473671": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1501331593365643251": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "31147555610622867": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5983216812617160817": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4923563283213192518": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4212671236276431488": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "5828610831858033460": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6364775570885914164": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5331245451076975104": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2728900281015453939": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-5187163736821586947": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7789508906883108112": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1286171734618277175": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1064677675419561927": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-1341872078835564141": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2465299827407059510": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8441480268423293825": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-679737459024487543": {
            "samples": [0.12562814070351758] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-956931862440489757": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2850240043802133894": {
            "samples": [0.12562814070351758] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3930623299089477521": {
            "samples": [0.12562814070351758] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4941558493613175334": {
            "samples": [0.12562814070351758] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-6131220994070678786": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1608903223980675470": {
            "samples": [0.12562814070351758] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3545683082694403137": {
            "samples": [0.12562814070351758] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3324189023495687889": {
            "samples": [0.12562814070351758] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5547992769206964966": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1126429335492521026": {
            "samples": [0.12562814070351758] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1002468948386885838": {
            "samples": [0.12562814070351758] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4106780481534243320": {
            "samples": [0.12562814070351758] * 71 + [0.0],
            "type": "arbitrary",
        },
        "7248387076429073473": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4253354788451875816": {
            "samples": [0.12562814070351758] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3952174500775115963": {
            "samples": [0.12562814070351758] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7398392074883422869": {
            "samples": [0.12562814070351758] * 75 + [0.0],
            "type": "arbitrary",
        },
        "3454809119994057607": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-3868414572056801432": {
            "samples": [0.12562814070351758] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3399108775776770641": {
            "samples": [0.12562814070351758] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "32577430146508340": {
            "samples": [0.12562814070351758] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-2319788238615785880": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4644346320702622333": {
            "samples": [0.12562814070351758] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8182406375156213153": {
            "samples": [0.12562814070351758] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6457165792310714812": {
            "samples": [0.12562814070351758] * 83 + [0.0],
            "type": "arbitrary",
        },
        "7685040994375154797": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3629443011412717668": {
            "samples": [0.12562814070351758] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3008117243526024124": {
            "samples": [0.12562814070351758] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5185733862285701474": {
            "samples": [0.12562814070351758] * 87 + [0.0],
            "type": "arbitrary",
        },
        "1195297771917931645": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7386331557266902739": {
            "samples": [0.12562814070351758] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7164837498068187491": {
            "samples": [0.12562814070351758] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7915375230011101824": {
            "samples": [0.12562814070351758] * 91 + [0.0],
            "type": "arbitrary",
        },
        "2466729701942944983": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5200625354578605386": {
            "samples": [0.12562814070351758] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4664489389946111846": {
            "samples": [0.12562814070351758] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4885983449144827094": {
            "samples": [0.12562814070351758] * 95 + [0.0],
            "type": "arbitrary",
        },
        "-2878905279469803335": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8327550807537960176": {
            "samples": [0.12562814070351758] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5508465351648099769": {
            "samples": [0.12562814070351758] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5270923665539901478": {
            "samples": [0.12562814070351758] * 99 + [0.0],
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
                "673250404584448585": "673250404584448585",
                "-5908297060336078065": "-5908297060336078065",
                "-4602261668386679696": "-4602261668386679696",
                "8298303205161635019": "8298303205161635019",
                "-7231821740564976130": "-7231821740564976130",
                "-5200654128973992550": "-5200654128973992550",
                "-7729187121346034486": "-7729187121346034486",
                "3050201895841966761": "3050201895841966761",
                "-5531427433342867623": "-5531427433342867623",
                "420641823663670327": "420641823663670327",
                "-7344246904950960102": "-7344246904950960102",
                "-7122752845752244854": "-7122752845752244854",
                "-8066599752643908144": "-8066599752643908144",
                "-4924993157749077991": "-4924993157749077991",
                "8073105387892316784": "8073105387892316784",
                "4706574042262054483": "4706574042262054483",
                "7253218868106288682": "7253218868106288682",
                "2505976347280853218": "2505976347280853218",
                "8458045604287391168": "8458045604287391168",
                "-7513744378002991371": "-7513744378002991371",
                "6305941269677908492": "6305941269677908492",
                "857295741609751651": "857295741609751651",
                "-3889946779215683813": "-3889946779215683813",
                "7806074242747205455": "7806074242747205455",
                "138719186225655086": "138719186225655086",
                "-4488339239802996667": "-4488339239802996667",
                "-681167333560373016": "-681167333560373016",
                "3762516785012962644": "3762516785012962644",
                "1410151116250668424": "1410151116250668424",
                "1132956712834666210": "1132956712834666210",
                "590264596464640322": "590264596464640322",
                "-7077090460056910047": "-7077090460056910047",
                "1795091332645742808": "1795091332645742808",
                "8740093541474345135": "8740093541474345135",
                "3992851020648909671": "3992851020648909671",
                "8242728160693286779": "8242728160693286779",
                "-1331834120313611982": "-1331834120313611982",
                "-2275681027205275272": "-2275681027205275272",
                "-2054186968006560024": "-2054186968006560024",
                "-1070854291024172786": "-1070854291024172786",
                "8849162436287076411": "8849162436287076411",
                "-7621316008618023590": "-7621316008618023590",
                "5376782537023371185": "5376782537023371185",
                "5598276596222086433": "5598276596222086433",
                "6581609273204473671": "6581609273204473671",
                "-1501331593365643251": "-1501331593365643251",
                "31147555610622867": "31147555610622867",
                "5983216812617160817": "5983216812617160817",
                "-4923563283213192518": "-4923563283213192518",
                "-4212671236276431488": "-4212671236276431488",
                "5828610831858033460": "5828610831858033460",
                "-6364775570885914164": "-6364775570885914164",
                "5331245451076975104": "5331245451076975104",
                "2728900281015453939": "2728900281015453939",
                "-5187163736821586947": "-5187163736821586947",
                "-7789508906883108112": "-7789508906883108112",
                "-1286171734618277175": "-1286171734618277175",
                "-1064677675419561927": "-1064677675419561927",
                "-1341872078835564141": "-1341872078835564141",
                "2465299827407059510": "2465299827407059510",
                "-8441480268423293825": "-8441480268423293825",
                "-679737459024487543": "-679737459024487543",
                "-956931862440489757": "-956931862440489757",
                "2850240043802133894": "2850240043802133894",
                "-3930623299089477521": "-3930623299089477521",
                "4941558493613175334": "4941558493613175334",
                "-6131220994070678786": "-6131220994070678786",
                "-1608903223980675470": "-1608903223980675470",
                "-3545683082694403137": "-3545683082694403137",
                "-3324189023495687889": "-3324189023495687889",
                "5547992769206964966": "5547992769206964966",
                "-1126429335492521026": "-1126429335492521026",
                "-1002468948386885838": "-1002468948386885838",
                "4106780481534243320": "4106780481534243320",
                "7248387076429073473": "7248387076429073473",
                "-4253354788451875816": "-4253354788451875816",
                "3952174500775115963": "3952174500775115963",
                "-7398392074883422869": "-7398392074883422869",
                "3454809119994057607": "3454809119994057607",
                "-3868414572056801432": "-3868414572056801432",
                "3399108775776770641": "3399108775776770641",
                "32577430146508340": "32577430146508340",
                "-2319788238615785880": "-2319788238615785880",
                "-4644346320702622333": "-4644346320702622333",
                "8182406375156213153": "8182406375156213153",
                "-6457165792310714812": "-6457165792310714812",
                "7685040994375154797": "7685040994375154797",
                "3629443011412717668": "3629443011412717668",
                "3008117243526024124": "3008117243526024124",
                "-5185733862285701474": "-5185733862285701474",
                "1195297771917931645": "1195297771917931645",
                "-7386331557266902739": "-7386331557266902739",
                "-7164837498068187491": "-7164837498068187491",
                "7915375230011101824": "7915375230011101824",
                "2466729701942944983": "2466729701942944983",
                "-5200625354578605386": "-5200625354578605386",
                "4664489389946111846": "4664489389946111846",
                "4885983449144827094": "4885983449144827094",
                "-2878905279469803335": "-2878905279469803335",
                "-8327550807537960176": "-8327550807537960176",
                "-5508465351648099769": "-5508465351648099769",
                "5270923665539901478": "5270923665539901478",
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
                "4382332537801879775": "4382332537801879775",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_ad1",
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
                "-2222767505055175561": "-2222767505055175561",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_f78",
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
                "-8575187705376057317": "-8575187705376057317_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_37a",
                "lo_frequency": 7370000000.0,
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
                "-3799175348537557238": "-3799175348537557238_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_8d7",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "4382332537801879775": {
            "length": 40,
            "waveforms": {
                "I": "4382332537801879775_i",
                "Q": "4382332537801879775_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2222767505055175561": {
            "length": 40,
            "waveforms": {
                "I": "-2222767505055175561_i",
                "Q": "-2222767505055175561_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "673250404584448585": {
            "length": 100,
            "waveforms": {
                "single": "673250404584448585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8575187705376057317_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1985196688154687140_i",
                "Q": "1985196688154687140_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-3799175348537557238_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4123930647378729725_i",
                "Q": "4123930647378729725_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-5908297060336078065": {
            "length": 100,
            "waveforms": {
                "single": "-5908297060336078065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4602261668386679696": {
            "length": 16,
            "waveforms": {
                "single": "-4602261668386679696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8298303205161635019": {
            "length": 16,
            "waveforms": {
                "single": "8298303205161635019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7231821740564976130": {
            "length": 16,
            "waveforms": {
                "single": "-7231821740564976130",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5200654128973992550": {
            "length": 16,
            "waveforms": {
                "single": "-5200654128973992550",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7729187121346034486": {
            "length": 16,
            "waveforms": {
                "single": "-7729187121346034486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3050201895841966761": {
            "length": 16,
            "waveforms": {
                "single": "3050201895841966761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5531427433342867623": {
            "length": 16,
            "waveforms": {
                "single": "-5531427433342867623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "420641823663670327": {
            "length": 16,
            "waveforms": {
                "single": "420641823663670327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7344246904950960102": {
            "length": 16,
            "waveforms": {
                "single": "-7344246904950960102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7122752845752244854": {
            "length": 16,
            "waveforms": {
                "single": "-7122752845752244854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8066599752643908144": {
            "length": 16,
            "waveforms": {
                "single": "-8066599752643908144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4924993157749077991": {
            "length": 16,
            "waveforms": {
                "single": "-4924993157749077991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8073105387892316784": {
            "length": 16,
            "waveforms": {
                "single": "8073105387892316784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4706574042262054483": {
            "length": 16,
            "waveforms": {
                "single": "4706574042262054483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7253218868106288682": {
            "length": 16,
            "waveforms": {
                "single": "7253218868106288682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2505976347280853218": {
            "length": 16,
            "waveforms": {
                "single": "2505976347280853218",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8458045604287391168": {
            "length": 16,
            "waveforms": {
                "single": "8458045604287391168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7513744378002991371": {
            "length": 20,
            "waveforms": {
                "single": "-7513744378002991371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6305941269677908492": {
            "length": 20,
            "waveforms": {
                "single": "6305941269677908492",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "857295741609751651": {
            "length": 20,
            "waveforms": {
                "single": "857295741609751651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3889946779215683813": {
            "length": 20,
            "waveforms": {
                "single": "-3889946779215683813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7806074242747205455": {
            "length": 24,
            "waveforms": {
                "single": "7806074242747205455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "138719186225655086": {
            "length": 24,
            "waveforms": {
                "single": "138719186225655086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4488339239802996667": {
            "length": 24,
            "waveforms": {
                "single": "-4488339239802996667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-681167333560373016": {
            "length": 24,
            "waveforms": {
                "single": "-681167333560373016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3762516785012962644": {
            "length": 28,
            "waveforms": {
                "single": "3762516785012962644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1410151116250668424": {
            "length": 28,
            "waveforms": {
                "single": "1410151116250668424",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1132956712834666210": {
            "length": 28,
            "waveforms": {
                "single": "1132956712834666210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "590264596464640322": {
            "length": 28,
            "waveforms": {
                "single": "590264596464640322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7077090460056910047": {
            "length": 32,
            "waveforms": {
                "single": "-7077090460056910047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1795091332645742808": {
            "length": 32,
            "waveforms": {
                "single": "1795091332645742808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8740093541474345135": {
            "length": 32,
            "waveforms": {
                "single": "8740093541474345135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3992851020648909671": {
            "length": 32,
            "waveforms": {
                "single": "3992851020648909671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8242728160693286779": {
            "length": 36,
            "waveforms": {
                "single": "8242728160693286779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1331834120313611982": {
            "length": 36,
            "waveforms": {
                "single": "-1331834120313611982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2275681027205275272": {
            "length": 36,
            "waveforms": {
                "single": "-2275681027205275272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2054186968006560024": {
            "length": 36,
            "waveforms": {
                "single": "-2054186968006560024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1070854291024172786": {
            "length": 40,
            "waveforms": {
                "single": "-1070854291024172786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8849162436287076411": {
            "length": 40,
            "waveforms": {
                "single": "8849162436287076411",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7621316008618023590": {
            "length": 40,
            "waveforms": {
                "single": "-7621316008618023590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5376782537023371185": {
            "length": 40,
            "waveforms": {
                "single": "5376782537023371185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5598276596222086433": {
            "length": 44,
            "waveforms": {
                "single": "5598276596222086433",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6581609273204473671": {
            "length": 44,
            "waveforms": {
                "single": "6581609273204473671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1501331593365643251": {
            "length": 44,
            "waveforms": {
                "single": "-1501331593365643251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "31147555610622867": {
            "length": 44,
            "waveforms": {
                "single": "31147555610622867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5983216812617160817": {
            "length": 48,
            "waveforms": {
                "single": "5983216812617160817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4923563283213192518": {
            "length": 48,
            "waveforms": {
                "single": "-4923563283213192518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4212671236276431488": {
            "length": 48,
            "waveforms": {
                "single": "-4212671236276431488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5828610831858033460": {
            "length": 48,
            "waveforms": {
                "single": "5828610831858033460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6364775570885914164": {
            "length": 52,
            "waveforms": {
                "single": "-6364775570885914164",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5331245451076975104": {
            "length": 52,
            "waveforms": {
                "single": "5331245451076975104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2728900281015453939": {
            "length": 52,
            "waveforms": {
                "single": "2728900281015453939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5187163736821586947": {
            "length": 52,
            "waveforms": {
                "single": "-5187163736821586947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7789508906883108112": {
            "length": 56,
            "waveforms": {
                "single": "-7789508906883108112",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1286171734618277175": {
            "length": 56,
            "waveforms": {
                "single": "-1286171734618277175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1064677675419561927": {
            "length": 56,
            "waveforms": {
                "single": "-1064677675419561927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1341872078835564141": {
            "length": 56,
            "waveforms": {
                "single": "-1341872078835564141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2465299827407059510": {
            "length": 60,
            "waveforms": {
                "single": "2465299827407059510",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8441480268423293825": {
            "length": 60,
            "waveforms": {
                "single": "-8441480268423293825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-679737459024487543": {
            "length": 60,
            "waveforms": {
                "single": "-679737459024487543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-956931862440489757": {
            "length": 60,
            "waveforms": {
                "single": "-956931862440489757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2850240043802133894": {
            "length": 64,
            "waveforms": {
                "single": "2850240043802133894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3930623299089477521": {
            "length": 64,
            "waveforms": {
                "single": "-3930623299089477521",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4941558493613175334": {
            "length": 64,
            "waveforms": {
                "single": "4941558493613175334",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6131220994070678786": {
            "length": 64,
            "waveforms": {
                "single": "-6131220994070678786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1608903223980675470": {
            "length": 68,
            "waveforms": {
                "single": "-1608903223980675470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3545683082694403137": {
            "length": 68,
            "waveforms": {
                "single": "-3545683082694403137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3324189023495687889": {
            "length": 68,
            "waveforms": {
                "single": "-3324189023495687889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5547992769206964966": {
            "length": 68,
            "waveforms": {
                "single": "5547992769206964966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1126429335492521026": {
            "length": 72,
            "waveforms": {
                "single": "-1126429335492521026",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1002468948386885838": {
            "length": 72,
            "waveforms": {
                "single": "-1002468948386885838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4106780481534243320": {
            "length": 72,
            "waveforms": {
                "single": "4106780481534243320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7248387076429073473": {
            "length": 72,
            "waveforms": {
                "single": "7248387076429073473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4253354788451875816": {
            "length": 76,
            "waveforms": {
                "single": "-4253354788451875816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3952174500775115963": {
            "length": 76,
            "waveforms": {
                "single": "3952174500775115963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7398392074883422869": {
            "length": 76,
            "waveforms": {
                "single": "-7398392074883422869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3454809119994057607": {
            "length": 76,
            "waveforms": {
                "single": "3454809119994057607",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3868414572056801432": {
            "length": 80,
            "waveforms": {
                "single": "-3868414572056801432",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3399108775776770641": {
            "length": 80,
            "waveforms": {
                "single": "3399108775776770641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "32577430146508340": {
            "length": 80,
            "waveforms": {
                "single": "32577430146508340",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2319788238615785880": {
            "length": 80,
            "waveforms": {
                "single": "-2319788238615785880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4644346320702622333": {
            "length": 84,
            "waveforms": {
                "single": "-4644346320702622333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8182406375156213153": {
            "length": 84,
            "waveforms": {
                "single": "8182406375156213153",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6457165792310714812": {
            "length": 84,
            "waveforms": {
                "single": "-6457165792310714812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7685040994375154797": {
            "length": 84,
            "waveforms": {
                "single": "7685040994375154797",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3629443011412717668": {
            "length": 88,
            "waveforms": {
                "single": "3629443011412717668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3008117243526024124": {
            "length": 88,
            "waveforms": {
                "single": "3008117243526024124",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5185733862285701474": {
            "length": 88,
            "waveforms": {
                "single": "-5185733862285701474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1195297771917931645": {
            "length": 88,
            "waveforms": {
                "single": "1195297771917931645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7386331557266902739": {
            "length": 92,
            "waveforms": {
                "single": "-7386331557266902739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7164837498068187491": {
            "length": 92,
            "waveforms": {
                "single": "-7164837498068187491",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7915375230011101824": {
            "length": 92,
            "waveforms": {
                "single": "7915375230011101824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2466729701942944983": {
            "length": 92,
            "waveforms": {
                "single": "2466729701942944983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5200625354578605386": {
            "length": 96,
            "waveforms": {
                "single": "-5200625354578605386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4664489389946111846": {
            "length": 96,
            "waveforms": {
                "single": "4664489389946111846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4885983449144827094": {
            "length": 96,
            "waveforms": {
                "single": "4885983449144827094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2878905279469803335": {
            "length": 96,
            "waveforms": {
                "single": "-2878905279469803335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8327550807537960176": {
            "length": 100,
            "waveforms": {
                "single": "-8327550807537960176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5508465351648099769": {
            "length": 100,
            "waveforms": {
                "single": "-5508465351648099769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5270923665539901478": {
            "length": 100,
            "waveforms": {
                "single": "5270923665539901478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "4382332537801879775_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4382332537801879775_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2222767505055175561_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2222767505055175561_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "673250404584448585": {
            "sample": -0.2388,
            "type": "constant",
        },
        "1985196688154687140_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "1985196688154687140_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4123930647378729725_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4123930647378729725_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5908297060336078065": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4602261668386679696": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8298303205161635019": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7231821740564976130": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5200654128973992550": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7729187121346034486": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3050201895841966761": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5531427433342867623": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "420641823663670327": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7344246904950960102": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7122752845752244854": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8066599752643908144": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4924993157749077991": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8073105387892316784": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4706574042262054483": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7253218868106288682": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2505976347280853218": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8458045604287391168": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7513744378002991371": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6305941269677908492": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "857295741609751651": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3889946779215683813": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "7806074242747205455": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "138719186225655086": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4488339239802996667": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-681167333560373016": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3762516785012962644": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1410151116250668424": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1132956712834666210": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "590264596464640322": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7077090460056910047": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1795091332645742808": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8740093541474345135": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3992851020648909671": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8242728160693286779": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1331834120313611982": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2275681027205275272": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2054186968006560024": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1070854291024172786": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8849162436287076411": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7621316008618023590": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5376782537023371185": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5598276596222086433": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6581609273204473671": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1501331593365643251": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "31147555610622867": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5983216812617160817": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4923563283213192518": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4212671236276431488": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5828610831858033460": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6364775570885914164": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5331245451076975104": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2728900281015453939": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5187163736821586947": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7789508906883108112": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1286171734618277175": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1064677675419561927": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1341872078835564141": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2465299827407059510": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8441480268423293825": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-679737459024487543": {
            "samples": [0.12562814070351758] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-956931862440489757": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2850240043802133894": {
            "samples": [0.12562814070351758] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3930623299089477521": {
            "samples": [0.12562814070351758] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4941558493613175334": {
            "samples": [0.12562814070351758] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6131220994070678786": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1608903223980675470": {
            "samples": [0.12562814070351758] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3545683082694403137": {
            "samples": [0.12562814070351758] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3324189023495687889": {
            "samples": [0.12562814070351758] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5547992769206964966": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1126429335492521026": {
            "samples": [0.12562814070351758] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1002468948386885838": {
            "samples": [0.12562814070351758] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4106780481534243320": {
            "samples": [0.12562814070351758] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7248387076429073473": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4253354788451875816": {
            "samples": [0.12562814070351758] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3952174500775115963": {
            "samples": [0.12562814070351758] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7398392074883422869": {
            "samples": [0.12562814070351758] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3454809119994057607": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-3868414572056801432": {
            "samples": [0.12562814070351758] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3399108775776770641": {
            "samples": [0.12562814070351758] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "32577430146508340": {
            "samples": [0.12562814070351758] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2319788238615785880": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4644346320702622333": {
            "samples": [0.12562814070351758] * 81 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8182406375156213153": {
            "samples": [0.12562814070351758] * 82 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6457165792310714812": {
            "samples": [0.12562814070351758] * 83 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7685040994375154797": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3629443011412717668": {
            "samples": [0.12562814070351758] * 85 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3008117243526024124": {
            "samples": [0.12562814070351758] * 86 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5185733862285701474": {
            "samples": [0.12562814070351758] * 87 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1195297771917931645": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7386331557266902739": {
            "samples": [0.12562814070351758] * 89 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7164837498068187491": {
            "samples": [0.12562814070351758] * 90 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7915375230011101824": {
            "samples": [0.12562814070351758] * 91 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2466729701942944983": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5200625354578605386": {
            "samples": [0.12562814070351758] * 93 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4664489389946111846": {
            "samples": [0.12562814070351758] * 94 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4885983449144827094": {
            "samples": [0.12562814070351758] * 95 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2878905279469803335": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8327550807537960176": {
            "samples": [0.12562814070351758] * 97 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5508465351648099769": {
            "samples": [0.12562814070351758] * 98 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5270923665539901478": {
            "samples": [0.12562814070351758] * 99 + [0.0],
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
        "B2/drive_mixer_ad1": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_f78": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_37a": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_8d7": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

