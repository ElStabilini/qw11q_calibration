
# Single QUA script generated at 2025-02-11 15:47:41.745091
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
    a1 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79])
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
        with for_each_((v8),(a1)):
            with for_(v9,1.1963927855711418,(v9<1.9933139073746846),(v9*1.0033333333333334)):
                align()
                play("-5965799674146238547", "B2/drive")
                play("145269158898435031", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("242480935742633465"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("5351730365663762623"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("5475690752769397811"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("6690117763790177436"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-8628396282173072643"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("7894944499971279922"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-5442550143817142536"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("72700578094925157"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("6453732212298558276"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-3120830068708340485"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("1499021373474742891"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-5750390140886636919"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("679134853688714789"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("1390026900625475819"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("8929990878504674100"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-6970108369360643317"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("6300430806326377666"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("8331598417917361246"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-1909616366565198591"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-1864289630976231059"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-1965316710782485557"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("6906865081920167298"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-5036541819524553381"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-7638886989586074546"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("5465652794247445652"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-9173919373219482313"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-3887415427560737861"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("4318113861666253918"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("2338727341288090862"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("4813681432707259939"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("3543554077469193348"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("6018508168888362425"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-5483233695992586864"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("5198621649102334323"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("5420115708301049571"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("243910810278518938"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-5098293479597512480"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-7626826471969554416"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-1197301477394202708"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("356410396627967114"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-8225218932556867270"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("2554170084631133977"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-7020392196375764784"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("6455162086834443749"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("4102796418072149529"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("3825602014656147315"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-8240110424849771182"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("5030428750837249801"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-4339118422646461410"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("4210542231051221699"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-6968678494824757844"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-3161506588582134193"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-5763851758643655358"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-963746900578967330"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-6583738278429683460"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-4108784187010514383"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("1667117746386275851"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-4164484531227801349"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-357312624985177698"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-7235709639969869173"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("3543679377218132074"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("3266484973802129860"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("914119305039835640"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("-6753235751481714729"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("-2230917981391711413"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-8953833446462915994"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("8345088810069766849"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("8566582869268482097"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("5200051523638219796"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("5421545582836935044"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("3096987500750098591"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("8951523085663556481"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("-4875369545862911759"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-5594228985842685363"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("-7075967240844113024"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("2334105899968304202"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("2555599959167019450"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("6362771865409643101"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("355002264185818185"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("4974853706368901561"*amp(v9), "B4/flux")
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
                play("145269158898435031", "B4/drive")
                measure("1572982625673988131", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.08488717563068002)-(v3*0.9963905697132255))>0.0026186590055777594)))
                r1 = declare_stream()
                save(v4, r1)
                measure("8971162394599218220", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.6672183692080369)-(v6*0.7448621669754532))>-0.0003217018907382291)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(200).buffer(80).average().save("1572982625673988131_B2|acquisition_shots")
        r2.buffer(200).buffer(80).average().save("8971162394599218220_B4|acquisition_shots")


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
                "-6246355887883027268": "-6246355887883027268",
                "-8460174609512600957": "-8460174609512600957",
                "242480935742633465": "242480935742633465",
                "5351730365663762623": "5351730365663762623",
                "5475690752769397811": "5475690752769397811",
                "6690117763790177436": "6690117763790177436",
                "-8628396282173072643": "-8628396282173072643",
                "7894944499971279922": "7894944499971279922",
                "-5442550143817142536": "-5442550143817142536",
                "72700578094925157": "72700578094925157",
                "6453732212298558276": "6453732212298558276",
                "-3120830068708340485": "-3120830068708340485",
                "1499021373474742891": "1499021373474742891",
                "-5750390140886636919": "-5750390140886636919",
                "679134853688714789": "679134853688714789",
                "1390026900625475819": "1390026900625475819",
                "8929990878504674100": "8929990878504674100",
                "-6970108369360643317": "-6970108369360643317",
                "6300430806326377666": "6300430806326377666",
                "8331598417917361246": "8331598417917361246",
                "-1909616366565198591": "-1909616366565198591",
                "-1864289630976231059": "-1864289630976231059",
                "-1965316710782485557": "-1965316710782485557",
                "6906865081920167298": "6906865081920167298",
                "-5036541819524553381": "-5036541819524553381",
                "-7638886989586074546": "-7638886989586074546",
                "5465652794247445652": "5465652794247445652",
                "-9173919373219482313": "-9173919373219482313",
                "-3887415427560737861": "-3887415427560737861",
                "4318113861666253918": "4318113861666253918",
                "2338727341288090862": "2338727341288090862",
                "4813681432707259939": "4813681432707259939",
                "3543554077469193348": "3543554077469193348",
                "6018508168888362425": "6018508168888362425",
                "-5483233695992586864": "-5483233695992586864",
                "5198621649102334323": "5198621649102334323",
                "5420115708301049571": "5420115708301049571",
                "243910810278518938": "243910810278518938",
                "-5098293479597512480": "-5098293479597512480",
                "-7626826471969554416": "-7626826471969554416",
                "-1197301477394202708": "-1197301477394202708",
                "356410396627967114": "356410396627967114",
                "-8225218932556867270": "-8225218932556867270",
                "2554170084631133977": "2554170084631133977",
                "-7020392196375764784": "-7020392196375764784",
                "6455162086834443749": "6455162086834443749",
                "4102796418072149529": "4102796418072149529",
                "3825602014656147315": "3825602014656147315",
                "-8240110424849771182": "-8240110424849771182",
                "5030428750837249801": "5030428750837249801",
                "-4339118422646461410": "-4339118422646461410",
                "4210542231051221699": "4210542231051221699",
                "-6968678494824757844": "-6968678494824757844",
                "-3161506588582134193": "-3161506588582134193",
                "-5763851758643655358": "-5763851758643655358",
                "-963746900578967330": "-963746900578967330",
                "-6583738278429683460": "-6583738278429683460",
                "-4108784187010514383": "-4108784187010514383",
                "1667117746386275851": "1667117746386275851",
                "-4164484531227801349": "-4164484531227801349",
                "-357312624985177698": "-357312624985177698",
                "-7235709639969869173": "-7235709639969869173",
                "3543679377218132074": "3543679377218132074",
                "3266484973802129860": "3266484973802129860",
                "914119305039835640": "914119305039835640",
                "-6753235751481714729": "-6753235751481714729",
                "-2230917981391711413": "-2230917981391711413",
                "-8953833446462915994": "-8953833446462915994",
                "8345088810069766849": "8345088810069766849",
                "8566582869268482097": "8566582869268482097",
                "5200051523638219796": "5200051523638219796",
                "5421545582836935044": "5421545582836935044",
                "3096987500750098591": "3096987500750098591",
                "8951523085663556481": "8951523085663556481",
                "-4875369545862911759": "-4875369545862911759",
                "-5594228985842685363": "-5594228985842685363",
                "-7075967240844113024": "-7075967240844113024",
                "2334105899968304202": "2334105899968304202",
                "2555599959167019450": "2555599959167019450",
                "6362771865409643101": "6362771865409643101",
                "355002264185818185": "355002264185818185",
                "4974853706368901561": "4974853706368901561",
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
                "145269158898435031": "145269158898435031",
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
                "8971162394599218220": "8971162394599218220_B4/acquisition",
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
                "1572982625673988131": "1572982625673988131_B2/acquisition",
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
                "-5965799674146238547": "-5965799674146238547",
            },
        },
    },
    "pulses": {
        "-5965799674146238547": {
            "length": 40,
            "waveforms": {
                "I": "-5965799674146238547_i",
                "Q": "-5965799674146238547_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "145269158898435031": {
            "length": 40,
            "waveforms": {
                "I": "145269158898435031_i",
                "Q": "145269158898435031_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6246355887883027268": {
            "length": 80,
            "waveforms": {
                "single": "-6246355887883027268",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1572982625673988131_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1368324028480544025_i",
                "Q": "1368324028480544025_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "8971162394599218220_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7050836970284699389_i",
                "Q": "-7050836970284699389_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-8460174609512600957": {
            "length": 80,
            "waveforms": {
                "single": "-8460174609512600957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "242480935742633465": {
            "length": 16,
            "waveforms": {
                "single": "242480935742633465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5351730365663762623": {
            "length": 16,
            "waveforms": {
                "single": "5351730365663762623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5475690752769397811": {
            "length": 16,
            "waveforms": {
                "single": "5475690752769397811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6690117763790177436": {
            "length": 16,
            "waveforms": {
                "single": "6690117763790177436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8628396282173072643": {
            "length": 16,
            "waveforms": {
                "single": "-8628396282173072643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7894944499971279922": {
            "length": 16,
            "waveforms": {
                "single": "7894944499971279922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5442550143817142536": {
            "length": 16,
            "waveforms": {
                "single": "-5442550143817142536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "72700578094925157": {
            "length": 16,
            "waveforms": {
                "single": "72700578094925157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6453732212298558276": {
            "length": 16,
            "waveforms": {
                "single": "6453732212298558276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3120830068708340485": {
            "length": 16,
            "waveforms": {
                "single": "-3120830068708340485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1499021373474742891": {
            "length": 16,
            "waveforms": {
                "single": "1499021373474742891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5750390140886636919": {
            "length": 16,
            "waveforms": {
                "single": "-5750390140886636919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "679134853688714789": {
            "length": 16,
            "waveforms": {
                "single": "679134853688714789",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1390026900625475819": {
            "length": 16,
            "waveforms": {
                "single": "1390026900625475819",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8929990878504674100": {
            "length": 16,
            "waveforms": {
                "single": "8929990878504674100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6970108369360643317": {
            "length": 16,
            "waveforms": {
                "single": "-6970108369360643317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6300430806326377666": {
            "length": 16,
            "waveforms": {
                "single": "6300430806326377666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8331598417917361246": {
            "length": 20,
            "waveforms": {
                "single": "8331598417917361246",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1909616366565198591": {
            "length": 20,
            "waveforms": {
                "single": "-1909616366565198591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1864289630976231059": {
            "length": 20,
            "waveforms": {
                "single": "-1864289630976231059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1965316710782485557": {
            "length": 20,
            "waveforms": {
                "single": "-1965316710782485557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6906865081920167298": {
            "length": 24,
            "waveforms": {
                "single": "6906865081920167298",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5036541819524553381": {
            "length": 24,
            "waveforms": {
                "single": "-5036541819524553381",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7638886989586074546": {
            "length": 24,
            "waveforms": {
                "single": "-7638886989586074546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5465652794247445652": {
            "length": 24,
            "waveforms": {
                "single": "5465652794247445652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9173919373219482313": {
            "length": 28,
            "waveforms": {
                "single": "-9173919373219482313",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3887415427560737861": {
            "length": 28,
            "waveforms": {
                "single": "-3887415427560737861",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4318113861666253918": {
            "length": 28,
            "waveforms": {
                "single": "4318113861666253918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2338727341288090862": {
            "length": 28,
            "waveforms": {
                "single": "2338727341288090862",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4813681432707259939": {
            "length": 32,
            "waveforms": {
                "single": "4813681432707259939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3543554077469193348": {
            "length": 32,
            "waveforms": {
                "single": "3543554077469193348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6018508168888362425": {
            "length": 32,
            "waveforms": {
                "single": "6018508168888362425",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5483233695992586864": {
            "length": 32,
            "waveforms": {
                "single": "-5483233695992586864",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5198621649102334323": {
            "length": 36,
            "waveforms": {
                "single": "5198621649102334323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5420115708301049571": {
            "length": 36,
            "waveforms": {
                "single": "5420115708301049571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "243910810278518938": {
            "length": 36,
            "waveforms": {
                "single": "243910810278518938",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5098293479597512480": {
            "length": 36,
            "waveforms": {
                "single": "-5098293479597512480",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7626826471969554416": {
            "length": 40,
            "waveforms": {
                "single": "-7626826471969554416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1197301477394202708": {
            "length": 40,
            "waveforms": {
                "single": "-1197301477394202708",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "356410396627967114": {
            "length": 40,
            "waveforms": {
                "single": "356410396627967114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8225218932556867270": {
            "length": 40,
            "waveforms": {
                "single": "-8225218932556867270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2554170084631133977": {
            "length": 44,
            "waveforms": {
                "single": "2554170084631133977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7020392196375764784": {
            "length": 44,
            "waveforms": {
                "single": "-7020392196375764784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6455162086834443749": {
            "length": 44,
            "waveforms": {
                "single": "6455162086834443749",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4102796418072149529": {
            "length": 44,
            "waveforms": {
                "single": "4102796418072149529",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3825602014656147315": {
            "length": 48,
            "waveforms": {
                "single": "3825602014656147315",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8240110424849771182": {
            "length": 48,
            "waveforms": {
                "single": "-8240110424849771182",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5030428750837249801": {
            "length": 48,
            "waveforms": {
                "single": "5030428750837249801",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4339118422646461410": {
            "length": 48,
            "waveforms": {
                "single": "-4339118422646461410",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4210542231051221699": {
            "length": 52,
            "waveforms": {
                "single": "4210542231051221699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6968678494824757844": {
            "length": 52,
            "waveforms": {
                "single": "-6968678494824757844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3161506588582134193": {
            "length": 52,
            "waveforms": {
                "single": "-3161506588582134193",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5763851758643655358": {
            "length": 52,
            "waveforms": {
                "single": "-5763851758643655358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-963746900578967330": {
            "length": 56,
            "waveforms": {
                "single": "-963746900578967330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6583738278429683460": {
            "length": 56,
            "waveforms": {
                "single": "-6583738278429683460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4108784187010514383": {
            "length": 56,
            "waveforms": {
                "single": "-4108784187010514383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1667117746386275851": {
            "length": 56,
            "waveforms": {
                "single": "1667117746386275851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4164484531227801349": {
            "length": 60,
            "waveforms": {
                "single": "-4164484531227801349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-357312624985177698": {
            "length": 60,
            "waveforms": {
                "single": "-357312624985177698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7235709639969869173": {
            "length": 60,
            "waveforms": {
                "single": "-7235709639969869173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3543679377218132074": {
            "length": 60,
            "waveforms": {
                "single": "3543679377218132074",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3266484973802129860": {
            "length": 64,
            "waveforms": {
                "single": "3266484973802129860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "914119305039835640": {
            "length": 64,
            "waveforms": {
                "single": "914119305039835640",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6753235751481714729": {
            "length": 64,
            "waveforms": {
                "single": "-6753235751481714729",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2230917981391711413": {
            "length": 64,
            "waveforms": {
                "single": "-2230917981391711413",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8953833446462915994": {
            "length": 68,
            "waveforms": {
                "single": "-8953833446462915994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8345088810069766849": {
            "length": 68,
            "waveforms": {
                "single": "8345088810069766849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8566582869268482097": {
            "length": 68,
            "waveforms": {
                "single": "8566582869268482097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5200051523638219796": {
            "length": 68,
            "waveforms": {
                "single": "5200051523638219796",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5421545582836935044": {
            "length": 72,
            "waveforms": {
                "single": "5421545582836935044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3096987500750098591": {
            "length": 72,
            "waveforms": {
                "single": "3096987500750098591",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8951523085663556481": {
            "length": 72,
            "waveforms": {
                "single": "8951523085663556481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4875369545862911759": {
            "length": 72,
            "waveforms": {
                "single": "-4875369545862911759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5594228985842685363": {
            "length": 76,
            "waveforms": {
                "single": "-5594228985842685363",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7075967240844113024": {
            "length": 76,
            "waveforms": {
                "single": "-7075967240844113024",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2334105899968304202": {
            "length": 76,
            "waveforms": {
                "single": "2334105899968304202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2555599959167019450": {
            "length": 76,
            "waveforms": {
                "single": "2555599959167019450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6362771865409643101": {
            "length": 80,
            "waveforms": {
                "single": "6362771865409643101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "355002264185818185": {
            "length": 80,
            "waveforms": {
                "single": "355002264185818185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4974853706368901561": {
            "length": 80,
            "waveforms": {
                "single": "4974853706368901561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-5965799674146238547_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-5965799674146238547_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "145269158898435031_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "145269158898435031_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-6246355887883027268": {
            "sample": -0.2388,
            "type": "constant",
        },
        "1368324028480544025_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "1368324028480544025_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7050836970284699389_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-7050836970284699389_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8460174609512600957": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "242480935742633465": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5351730365663762623": {
            "samples": [0.1253768844221106] + [0.0] * 15,
            "type": "arbitrary",
        },
        "5475690752769397811": {
            "samples": [0.1253768844221106] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "6690117763790177436": {
            "samples": [0.1253768844221106] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-8628396282173072643": {
            "samples": [0.1253768844221106] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "7894944499971279922": {
            "samples": [0.1253768844221106] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-5442550143817142536": {
            "samples": [0.1253768844221106] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "72700578094925157": {
            "samples": [0.1253768844221106] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "6453732212298558276": {
            "samples": [0.1253768844221106] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-3120830068708340485": {
            "samples": [0.1253768844221106] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "1499021373474742891": {
            "samples": [0.1253768844221106] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-5750390140886636919": {
            "samples": [0.1253768844221106] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "679134853688714789": {
            "samples": [0.1253768844221106] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "1390026900625475819": {
            "samples": [0.1253768844221106] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8929990878504674100": {
            "samples": [0.1253768844221106] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6970108369360643317": {
            "samples": [0.1253768844221106] * 15 + [0.0],
            "type": "arbitrary",
        },
        "6300430806326377666": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "8331598417917361246": {
            "samples": [0.1253768844221106] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1909616366565198591": {
            "samples": [0.1253768844221106] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1864289630976231059": {
            "samples": [0.1253768844221106] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-1965316710782485557": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "6906865081920167298": {
            "samples": [0.1253768844221106] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5036541819524553381": {
            "samples": [0.1253768844221106] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7638886989586074546": {
            "samples": [0.1253768844221106] * 23 + [0.0],
            "type": "arbitrary",
        },
        "5465652794247445652": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-9173919373219482313": {
            "samples": [0.1253768844221106] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3887415427560737861": {
            "samples": [0.1253768844221106] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4318113861666253918": {
            "samples": [0.1253768844221106] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2338727341288090862": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "4813681432707259939": {
            "samples": [0.1253768844221106] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3543554077469193348": {
            "samples": [0.1253768844221106] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6018508168888362425": {
            "samples": [0.1253768844221106] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5483233695992586864": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "5198621649102334323": {
            "samples": [0.1253768844221106] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5420115708301049571": {
            "samples": [0.1253768844221106] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "243910810278518938": {
            "samples": [0.1253768844221106] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-5098293479597512480": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-7626826471969554416": {
            "samples": [0.1253768844221106] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1197301477394202708": {
            "samples": [0.1253768844221106] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "356410396627967114": {
            "samples": [0.1253768844221106] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-8225218932556867270": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "2554170084631133977": {
            "samples": [0.1253768844221106] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7020392196375764784": {
            "samples": [0.1253768844221106] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6455162086834443749": {
            "samples": [0.1253768844221106] * 43 + [0.0],
            "type": "arbitrary",
        },
        "4102796418072149529": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "3825602014656147315": {
            "samples": [0.1253768844221106] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8240110424849771182": {
            "samples": [0.1253768844221106] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5030428750837249801": {
            "samples": [0.1253768844221106] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-4339118422646461410": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "4210542231051221699": {
            "samples": [0.1253768844221106] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6968678494824757844": {
            "samples": [0.1253768844221106] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3161506588582134193": {
            "samples": [0.1253768844221106] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-5763851758643655358": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-963746900578967330": {
            "samples": [0.1253768844221106] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6583738278429683460": {
            "samples": [0.1253768844221106] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4108784187010514383": {
            "samples": [0.1253768844221106] * 55 + [0.0],
            "type": "arbitrary",
        },
        "1667117746386275851": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-4164484531227801349": {
            "samples": [0.1253768844221106] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-357312624985177698": {
            "samples": [0.1253768844221106] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7235709639969869173": {
            "samples": [0.1253768844221106] * 59 + [0.0],
            "type": "arbitrary",
        },
        "3543679377218132074": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "3266484973802129860": {
            "samples": [0.1253768844221106] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "914119305039835640": {
            "samples": [0.1253768844221106] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6753235751481714729": {
            "samples": [0.1253768844221106] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-2230917981391711413": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-8953833446462915994": {
            "samples": [0.1253768844221106] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8345088810069766849": {
            "samples": [0.1253768844221106] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8566582869268482097": {
            "samples": [0.1253768844221106] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5200051523638219796": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "5421545582836935044": {
            "samples": [0.1253768844221106] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3096987500750098591": {
            "samples": [0.1253768844221106] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8951523085663556481": {
            "samples": [0.1253768844221106] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-4875369545862911759": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "-5594228985842685363": {
            "samples": [0.1253768844221106] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7075967240844113024": {
            "samples": [0.1253768844221106] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2334105899968304202": {
            "samples": [0.1253768844221106] * 75 + [0.0],
            "type": "arbitrary",
        },
        "2555599959167019450": {
            "sample": 0.1253768844221106,
            "type": "constant",
        },
        "6362771865409643101": {
            "samples": [0.1253768844221106] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "355002264185818185": {
            "samples": [0.1253768844221106] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4974853706368901561": {
            "samples": [0.1253768844221106] * 79 + [0.0],
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
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.082216163036566, -1.013483744074572, -0.0005934150341553434, -0.0005835327755912938, 0.007717830054774853, 0.003632375897519549, -0.00044011698253741335, 0.001605758501608272, -0.012449189070277502, -0.007236945254569601, 0.00976822190693331, 0.005697927299491748, 0.004773147069343227, -0.002901494501723682, -0.0017290035617877402, -0.001732703182405211, -0.004127059088728484, 0.006652439702682195, -0.0018491032089883812, -0.005021633883561784, 0.003839210780199868],
                        "feedback": [0.9999990463256836, -0.9262251003261055],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0864486524147088, -1.0114796931248773, -0.00016385035736341804, -0.0001631375856683214, 0.0007132004480542389, -0.005469433104324626, -0.0031203713793950478, 0.0020985293007232484, -0.005440448977252687, 0.0029103915350147547, 0.006805519982961323, 0.007363572786123743, -0.0038086062520665135, -0.003181071276233404, 0.0005943072751533468, -0.003554727873357823, 0.0023584825716348456, -0.005872694192023741, 0.0012065363048726322, 0.0017448644372721935, 0.001253029817072768],
                        "feedback": [0.9999990463256836, -0.9287365023806654],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1030496953566256, -1.0381134620821453, -0.0004260403462593258, -0.000420572662019365, 0.005570686385595049, -0.0020512683945509416, -0.0006392178405930675, -0.001996407788676792, 0.0004683735253229373, -0.003829742786740141, 0.0057195392567130805, 0.006959373393239386, -0.0034838926793923962, 0.0011703722958150697, -0.0027201873232208813, -0.004669494937616429, -0.0016907470696459624, -9.041142346012665e-05, 0.0001460934840622299, 0.002830673562819465, 0.0005694981868720677],
                        "feedback": [0.9999990463256836, -0.9336222939492675],
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
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
                "-6246355887883027268": "-6246355887883027268",
                "-8460174609512600957": "-8460174609512600957",
                "242480935742633465": "242480935742633465",
                "5351730365663762623": "5351730365663762623",
                "5475690752769397811": "5475690752769397811",
                "6690117763790177436": "6690117763790177436",
                "-8628396282173072643": "-8628396282173072643",
                "7894944499971279922": "7894944499971279922",
                "-5442550143817142536": "-5442550143817142536",
                "72700578094925157": "72700578094925157",
                "6453732212298558276": "6453732212298558276",
                "-3120830068708340485": "-3120830068708340485",
                "1499021373474742891": "1499021373474742891",
                "-5750390140886636919": "-5750390140886636919",
                "679134853688714789": "679134853688714789",
                "1390026900625475819": "1390026900625475819",
                "8929990878504674100": "8929990878504674100",
                "-6970108369360643317": "-6970108369360643317",
                "6300430806326377666": "6300430806326377666",
                "8331598417917361246": "8331598417917361246",
                "-1909616366565198591": "-1909616366565198591",
                "-1864289630976231059": "-1864289630976231059",
                "-1965316710782485557": "-1965316710782485557",
                "6906865081920167298": "6906865081920167298",
                "-5036541819524553381": "-5036541819524553381",
                "-7638886989586074546": "-7638886989586074546",
                "5465652794247445652": "5465652794247445652",
                "-9173919373219482313": "-9173919373219482313",
                "-3887415427560737861": "-3887415427560737861",
                "4318113861666253918": "4318113861666253918",
                "2338727341288090862": "2338727341288090862",
                "4813681432707259939": "4813681432707259939",
                "3543554077469193348": "3543554077469193348",
                "6018508168888362425": "6018508168888362425",
                "-5483233695992586864": "-5483233695992586864",
                "5198621649102334323": "5198621649102334323",
                "5420115708301049571": "5420115708301049571",
                "243910810278518938": "243910810278518938",
                "-5098293479597512480": "-5098293479597512480",
                "-7626826471969554416": "-7626826471969554416",
                "-1197301477394202708": "-1197301477394202708",
                "356410396627967114": "356410396627967114",
                "-8225218932556867270": "-8225218932556867270",
                "2554170084631133977": "2554170084631133977",
                "-7020392196375764784": "-7020392196375764784",
                "6455162086834443749": "6455162086834443749",
                "4102796418072149529": "4102796418072149529",
                "3825602014656147315": "3825602014656147315",
                "-8240110424849771182": "-8240110424849771182",
                "5030428750837249801": "5030428750837249801",
                "-4339118422646461410": "-4339118422646461410",
                "4210542231051221699": "4210542231051221699",
                "-6968678494824757844": "-6968678494824757844",
                "-3161506588582134193": "-3161506588582134193",
                "-5763851758643655358": "-5763851758643655358",
                "-963746900578967330": "-963746900578967330",
                "-6583738278429683460": "-6583738278429683460",
                "-4108784187010514383": "-4108784187010514383",
                "1667117746386275851": "1667117746386275851",
                "-4164484531227801349": "-4164484531227801349",
                "-357312624985177698": "-357312624985177698",
                "-7235709639969869173": "-7235709639969869173",
                "3543679377218132074": "3543679377218132074",
                "3266484973802129860": "3266484973802129860",
                "914119305039835640": "914119305039835640",
                "-6753235751481714729": "-6753235751481714729",
                "-2230917981391711413": "-2230917981391711413",
                "-8953833446462915994": "-8953833446462915994",
                "8345088810069766849": "8345088810069766849",
                "8566582869268482097": "8566582869268482097",
                "5200051523638219796": "5200051523638219796",
                "5421545582836935044": "5421545582836935044",
                "3096987500750098591": "3096987500750098591",
                "8951523085663556481": "8951523085663556481",
                "-4875369545862911759": "-4875369545862911759",
                "-5594228985842685363": "-5594228985842685363",
                "-7075967240844113024": "-7075967240844113024",
                "2334105899968304202": "2334105899968304202",
                "2555599959167019450": "2555599959167019450",
                "6362771865409643101": "6362771865409643101",
                "355002264185818185": "355002264185818185",
                "4974853706368901561": "4974853706368901561",
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
                "145269158898435031": "145269158898435031",
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
                "mixer": "B4/drive_mixer_748",
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
                "8971162394599218220": "8971162394599218220_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_234",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "1572982625673988131": "1572982625673988131_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_763",
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
                "-5965799674146238547": "-5965799674146238547",
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
                "mixer": "B2/drive_mixer_921",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
    },
    "pulses": {
        "-5965799674146238547": {
            "length": 40,
            "waveforms": {
                "I": "-5965799674146238547_i",
                "Q": "-5965799674146238547_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "145269158898435031": {
            "length": 40,
            "waveforms": {
                "I": "145269158898435031_i",
                "Q": "145269158898435031_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6246355887883027268": {
            "length": 80,
            "waveforms": {
                "single": "-6246355887883027268",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1572982625673988131_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1368324028480544025_i",
                "Q": "1368324028480544025_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8971162394599218220_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7050836970284699389_i",
                "Q": "-7050836970284699389_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8460174609512600957": {
            "length": 80,
            "waveforms": {
                "single": "-8460174609512600957",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "242480935742633465": {
            "length": 16,
            "waveforms": {
                "single": "242480935742633465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5351730365663762623": {
            "length": 16,
            "waveforms": {
                "single": "5351730365663762623",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5475690752769397811": {
            "length": 16,
            "waveforms": {
                "single": "5475690752769397811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6690117763790177436": {
            "length": 16,
            "waveforms": {
                "single": "6690117763790177436",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8628396282173072643": {
            "length": 16,
            "waveforms": {
                "single": "-8628396282173072643",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7894944499971279922": {
            "length": 16,
            "waveforms": {
                "single": "7894944499971279922",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5442550143817142536": {
            "length": 16,
            "waveforms": {
                "single": "-5442550143817142536",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "72700578094925157": {
            "length": 16,
            "waveforms": {
                "single": "72700578094925157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6453732212298558276": {
            "length": 16,
            "waveforms": {
                "single": "6453732212298558276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3120830068708340485": {
            "length": 16,
            "waveforms": {
                "single": "-3120830068708340485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1499021373474742891": {
            "length": 16,
            "waveforms": {
                "single": "1499021373474742891",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5750390140886636919": {
            "length": 16,
            "waveforms": {
                "single": "-5750390140886636919",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "679134853688714789": {
            "length": 16,
            "waveforms": {
                "single": "679134853688714789",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1390026900625475819": {
            "length": 16,
            "waveforms": {
                "single": "1390026900625475819",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8929990878504674100": {
            "length": 16,
            "waveforms": {
                "single": "8929990878504674100",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6970108369360643317": {
            "length": 16,
            "waveforms": {
                "single": "-6970108369360643317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6300430806326377666": {
            "length": 16,
            "waveforms": {
                "single": "6300430806326377666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8331598417917361246": {
            "length": 20,
            "waveforms": {
                "single": "8331598417917361246",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1909616366565198591": {
            "length": 20,
            "waveforms": {
                "single": "-1909616366565198591",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1864289630976231059": {
            "length": 20,
            "waveforms": {
                "single": "-1864289630976231059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1965316710782485557": {
            "length": 20,
            "waveforms": {
                "single": "-1965316710782485557",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6906865081920167298": {
            "length": 24,
            "waveforms": {
                "single": "6906865081920167298",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5036541819524553381": {
            "length": 24,
            "waveforms": {
                "single": "-5036541819524553381",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7638886989586074546": {
            "length": 24,
            "waveforms": {
                "single": "-7638886989586074546",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5465652794247445652": {
            "length": 24,
            "waveforms": {
                "single": "5465652794247445652",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9173919373219482313": {
            "length": 28,
            "waveforms": {
                "single": "-9173919373219482313",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3887415427560737861": {
            "length": 28,
            "waveforms": {
                "single": "-3887415427560737861",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4318113861666253918": {
            "length": 28,
            "waveforms": {
                "single": "4318113861666253918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2338727341288090862": {
            "length": 28,
            "waveforms": {
                "single": "2338727341288090862",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4813681432707259939": {
            "length": 32,
            "waveforms": {
                "single": "4813681432707259939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3543554077469193348": {
            "length": 32,
            "waveforms": {
                "single": "3543554077469193348",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6018508168888362425": {
            "length": 32,
            "waveforms": {
                "single": "6018508168888362425",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5483233695992586864": {
            "length": 32,
            "waveforms": {
                "single": "-5483233695992586864",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5198621649102334323": {
            "length": 36,
            "waveforms": {
                "single": "5198621649102334323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5420115708301049571": {
            "length": 36,
            "waveforms": {
                "single": "5420115708301049571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "243910810278518938": {
            "length": 36,
            "waveforms": {
                "single": "243910810278518938",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5098293479597512480": {
            "length": 36,
            "waveforms": {
                "single": "-5098293479597512480",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7626826471969554416": {
            "length": 40,
            "waveforms": {
                "single": "-7626826471969554416",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1197301477394202708": {
            "length": 40,
            "waveforms": {
                "single": "-1197301477394202708",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "356410396627967114": {
            "length": 40,
            "waveforms": {
                "single": "356410396627967114",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8225218932556867270": {
            "length": 40,
            "waveforms": {
                "single": "-8225218932556867270",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2554170084631133977": {
            "length": 44,
            "waveforms": {
                "single": "2554170084631133977",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7020392196375764784": {
            "length": 44,
            "waveforms": {
                "single": "-7020392196375764784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6455162086834443749": {
            "length": 44,
            "waveforms": {
                "single": "6455162086834443749",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4102796418072149529": {
            "length": 44,
            "waveforms": {
                "single": "4102796418072149529",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3825602014656147315": {
            "length": 48,
            "waveforms": {
                "single": "3825602014656147315",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8240110424849771182": {
            "length": 48,
            "waveforms": {
                "single": "-8240110424849771182",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5030428750837249801": {
            "length": 48,
            "waveforms": {
                "single": "5030428750837249801",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4339118422646461410": {
            "length": 48,
            "waveforms": {
                "single": "-4339118422646461410",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4210542231051221699": {
            "length": 52,
            "waveforms": {
                "single": "4210542231051221699",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6968678494824757844": {
            "length": 52,
            "waveforms": {
                "single": "-6968678494824757844",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3161506588582134193": {
            "length": 52,
            "waveforms": {
                "single": "-3161506588582134193",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5763851758643655358": {
            "length": 52,
            "waveforms": {
                "single": "-5763851758643655358",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-963746900578967330": {
            "length": 56,
            "waveforms": {
                "single": "-963746900578967330",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6583738278429683460": {
            "length": 56,
            "waveforms": {
                "single": "-6583738278429683460",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4108784187010514383": {
            "length": 56,
            "waveforms": {
                "single": "-4108784187010514383",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1667117746386275851": {
            "length": 56,
            "waveforms": {
                "single": "1667117746386275851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4164484531227801349": {
            "length": 60,
            "waveforms": {
                "single": "-4164484531227801349",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-357312624985177698": {
            "length": 60,
            "waveforms": {
                "single": "-357312624985177698",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7235709639969869173": {
            "length": 60,
            "waveforms": {
                "single": "-7235709639969869173",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3543679377218132074": {
            "length": 60,
            "waveforms": {
                "single": "3543679377218132074",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3266484973802129860": {
            "length": 64,
            "waveforms": {
                "single": "3266484973802129860",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "914119305039835640": {
            "length": 64,
            "waveforms": {
                "single": "914119305039835640",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6753235751481714729": {
            "length": 64,
            "waveforms": {
                "single": "-6753235751481714729",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2230917981391711413": {
            "length": 64,
            "waveforms": {
                "single": "-2230917981391711413",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8953833446462915994": {
            "length": 68,
            "waveforms": {
                "single": "-8953833446462915994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8345088810069766849": {
            "length": 68,
            "waveforms": {
                "single": "8345088810069766849",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8566582869268482097": {
            "length": 68,
            "waveforms": {
                "single": "8566582869268482097",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5200051523638219796": {
            "length": 68,
            "waveforms": {
                "single": "5200051523638219796",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5421545582836935044": {
            "length": 72,
            "waveforms": {
                "single": "5421545582836935044",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3096987500750098591": {
            "length": 72,
            "waveforms": {
                "single": "3096987500750098591",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8951523085663556481": {
            "length": 72,
            "waveforms": {
                "single": "8951523085663556481",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4875369545862911759": {
            "length": 72,
            "waveforms": {
                "single": "-4875369545862911759",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5594228985842685363": {
            "length": 76,
            "waveforms": {
                "single": "-5594228985842685363",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7075967240844113024": {
            "length": 76,
            "waveforms": {
                "single": "-7075967240844113024",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2334105899968304202": {
            "length": 76,
            "waveforms": {
                "single": "2334105899968304202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2555599959167019450": {
            "length": 76,
            "waveforms": {
                "single": "2555599959167019450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6362771865409643101": {
            "length": 80,
            "waveforms": {
                "single": "6362771865409643101",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "355002264185818185": {
            "length": 80,
            "waveforms": {
                "single": "355002264185818185",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4974853706368901561": {
            "length": 80,
            "waveforms": {
                "single": "4974853706368901561",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-5965799674146238547_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5965799674146238547_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "145269158898435031_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "145269158898435031_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6246355887883027268": {
            "type": "constant",
            "sample": -0.2388,
        },
        "1368324028480544025_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "1368324028480544025_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7050836970284699389_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-7050836970284699389_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8460174609512600957": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "242480935742633465": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5351730365663762623": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5475690752769397811": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6690117763790177436": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8628396282173072643": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7894944499971279922": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5442550143817142536": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "72700578094925157": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6453732212298558276": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3120830068708340485": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1499021373474742891": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5750390140886636919": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "679134853688714789": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1390026900625475819": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8929990878504674100": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6970108369360643317": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6300430806326377666": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "8331598417917361246": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1909616366565198591": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1864289630976231059": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1965316710782485557": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "6906865081920167298": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5036541819524553381": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7638886989586074546": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5465652794247445652": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-9173919373219482313": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3887415427560737861": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4318113861666253918": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2338727341288090862": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "4813681432707259939": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3543554077469193348": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6018508168888362425": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5483233695992586864": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "5198621649102334323": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5420115708301049571": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "243910810278518938": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5098293479597512480": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-7626826471969554416": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1197301477394202708": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "356410396627967114": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8225218932556867270": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "2554170084631133977": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7020392196375764784": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6455162086834443749": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4102796418072149529": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "3825602014656147315": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8240110424849771182": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5030428750837249801": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4339118422646461410": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "4210542231051221699": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6968678494824757844": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3161506588582134193": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5763851758643655358": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-963746900578967330": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6583738278429683460": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4108784187010514383": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1667117746386275851": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-4164484531227801349": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-357312624985177698": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7235709639969869173": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3543679377218132074": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "3266484973802129860": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "914119305039835640": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6753235751481714729": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2230917981391711413": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-8953833446462915994": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8345088810069766849": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8566582869268482097": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5200051523638219796": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "5421545582836935044": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3096987500750098591": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8951523085663556481": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4875369545862911759": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "-5594228985842685363": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7075967240844113024": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2334105899968304202": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2555599959167019450": {
            "type": "constant",
            "sample": 0.1253768844221106,
        },
        "6362771865409643101": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "355002264185818185": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4974853706368901561": {
            "type": "arbitrary",
            "samples": [0.1253768844221106] * 79 + [0.0],
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
        "B4/drive_mixer_748": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_234": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_763": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_921": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

