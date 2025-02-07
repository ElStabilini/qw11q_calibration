
# Single QUA script generated at 2025-02-07 13:57:46.176511
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
            with for_(v9,-1.99,(v9<-1.8295816326530612),(v9+0.004061224489795734)):
                align()
                play("-8161414599441454486", "B2/drive")
                play("-6951477704267723434", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("6360682666362597223"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-1306672390158953146"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("8558442354365764086"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-3936232462337249580"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("2567104709927581357"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-35240460133939808"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-5377444750009971226"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("3494737042692681629"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("3716231101891396877"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("7395729044895991401"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-8504370202969326016"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("5371298673524537852"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-7299543466788223530"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-4824589375369054453"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("8002163320489781033"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-5644475895155082555"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-8246821065216603720"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("7847557339730653676"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("2827874188859592004"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-4373043965130069217"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("6406345052057932030"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-3168217228948966731"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-2946723169750251483"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-8288927459626282901"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-3766609689536279585"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-4387935457422973129"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("4484246335279679726"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-7017495529601269563"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("6682006023282846589"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("3885853874692366872"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("3264528106805673328"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-6632555313206195179"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6411061254007479931"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("1618300711609764132"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-2510069251804170159"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("7355045492720547073"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("1019908251022451278"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("3494862342441620355"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-9175979797871141027"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("2568534584463466830"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("7118659941228927913"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("367936889482265565"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-7299418167039284804"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("1572763625663368051"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("8517765834491970378"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("7725094216822717545"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("5372728548060423325"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-4201833732946475436"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-2498008734187650029"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-2276514674988934781"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-5643046020619197082"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-5421551961420481834"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-2113068517792575645"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-1891574458593860397"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-7067779356616391030"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("2009417543609449375"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("527679288608021714"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-8508991644289112676"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-8287497585090397428"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("584684207612255427"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("-6089737897087230565"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("-5965777509981595377"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("-856528080060466219"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("-8939468946630583141"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("8237147771840901884"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("1562725667141415892"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("6085043437231419208"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("6795935484168180238"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("-8333034671036793509"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("-8610229074452795723"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("6641329503409052881"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("-4709237072249485951"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("-902065166006862300"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-1179259569422864514"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("7026269719804127265"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("7247763779002842513"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("369366764018151038"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-9001220606703542240"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("3899344266844772475"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("-3768010789676777894"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("754306980413225422"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("6318598014046654586"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("-1348757042474895783"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("-2496578859651764556"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("3884452774551868563"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("8406770544641871879"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("-77325112449882445"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("6303706521753750674"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("-1890144584057974924"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("-2511470351944668468"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("307615103945191939"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("529109163143907187"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("-189750276835866417"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("5762318980170671533"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("-4866674027684997090"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("7960078668173838396"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("-6679493499293089569"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("-6585673403332403448"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("-8067411658333831109"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("2185481309563994909"*amp(v9), "B4/flux")
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
                play("-6951477704267723434", "B4/drive")
                measure("5311635281710159683", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.075204305408579)-(v3*0.9971681465269602))>0.0024489983009435058)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-5736929023074161844", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.6829904452382262)-(v6*0.7304273076174587))>-0.0004957863375908795)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(40).buffer(100).average().save("5311635281710159683_B2|acquisition_shots")
        r2.buffer(40).buffer(100).average().save("-5736929023074161844_B4|acquisition_shots")


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
                "-2124430296495305353": "-2124430296495305353",
                "-5408061569268076231": "-5408061569268076231",
                "6360682666362597223": "6360682666362597223",
                "-1306672390158953146": "-1306672390158953146",
                "8558442354365764086": "8558442354365764086",
                "-3936232462337249580": "-3936232462337249580",
                "2567104709927581357": "2567104709927581357",
                "-35240460133939808": "-35240460133939808",
                "-5377444750009971226": "-5377444750009971226",
                "3494737042692681629": "3494737042692681629",
                "3716231101891396877": "3716231101891396877",
                "7395729044895991401": "7395729044895991401",
                "-8504370202969326016": "-8504370202969326016",
                "5371298673524537852": "5371298673524537852",
                "-7299543466788223530": "-7299543466788223530",
                "-4824589375369054453": "-4824589375369054453",
                "8002163320489781033": "8002163320489781033",
                "-5644475895155082555": "-5644475895155082555",
                "-8246821065216603720": "-8246821065216603720",
                "7847557339730653676": "7847557339730653676",
                "2827874188859592004": "2827874188859592004",
                "-4373043965130069217": "-4373043965130069217",
                "6406345052057932030": "6406345052057932030",
                "-3168217228948966731": "-3168217228948966731",
                "-2946723169750251483": "-2946723169750251483",
                "-8288927459626282901": "-8288927459626282901",
                "-3766609689536279585": "-3766609689536279585",
                "-4387935457422973129": "-4387935457422973129",
                "4484246335279679726": "4484246335279679726",
                "-7017495529601269563": "-7017495529601269563",
                "6682006023282846589": "6682006023282846589",
                "3885853874692366872": "3885853874692366872",
                "3264528106805673328": "3264528106805673328",
                "-6632555313206195179": "-6632555313206195179",
                "-6411061254007479931": "-6411061254007479931",
                "1618300711609764132": "1618300711609764132",
                "-2510069251804170159": "-2510069251804170159",
                "7355045492720547073": "7355045492720547073",
                "1019908251022451278": "1019908251022451278",
                "3494862342441620355": "3494862342441620355",
                "-9175979797871141027": "-9175979797871141027",
                "2568534584463466830": "2568534584463466830",
                "7118659941228927913": "7118659941228927913",
                "367936889482265565": "367936889482265565",
                "-7299418167039284804": "-7299418167039284804",
                "1572763625663368051": "1572763625663368051",
                "8517765834491970378": "8517765834491970378",
                "7725094216822717545": "7725094216822717545",
                "5372728548060423325": "5372728548060423325",
                "-4201833732946475436": "-4201833732946475436",
                "-2498008734187650029": "-2498008734187650029",
                "-2276514674988934781": "-2276514674988934781",
                "-5643046020619197082": "-5643046020619197082",
                "-5421551961420481834": "-5421551961420481834",
                "-2113068517792575645": "-2113068517792575645",
                "-1891574458593860397": "-1891574458593860397",
                "-7067779356616391030": "-7067779356616391030",
                "2009417543609449375": "2009417543609449375",
                "527679288608021714": "527679288608021714",
                "-8508991644289112676": "-8508991644289112676",
                "-8287497585090397428": "-8287497585090397428",
                "584684207612255427": "584684207612255427",
                "-6089737897087230565": "-6089737897087230565",
                "-5965777509981595377": "-5965777509981595377",
                "-856528080060466219": "-856528080060466219",
                "-8939468946630583141": "-8939468946630583141",
                "8237147771840901884": "8237147771840901884",
                "1562725667141415892": "1562725667141415892",
                "6085043437231419208": "6085043437231419208",
                "6795935484168180238": "6795935484168180238",
                "-8333034671036793509": "-8333034671036793509",
                "-8610229074452795723": "-8610229074452795723",
                "6641329503409052881": "6641329503409052881",
                "-4709237072249485951": "-4709237072249485951",
                "-902065166006862300": "-902065166006862300",
                "-1179259569422864514": "-1179259569422864514",
                "7026269719804127265": "7026269719804127265",
                "7247763779002842513": "7247763779002842513",
                "369366764018151038": "369366764018151038",
                "-9001220606703542240": "-9001220606703542240",
                "3899344266844772475": "3899344266844772475",
                "-3768010789676777894": "-3768010789676777894",
                "754306980413225422": "754306980413225422",
                "6318598014046654586": "6318598014046654586",
                "-1348757042474895783": "-1348757042474895783",
                "-2496578859651764556": "-2496578859651764556",
                "3884452774551868563": "3884452774551868563",
                "8406770544641871879": "8406770544641871879",
                "-77325112449882445": "-77325112449882445",
                "6303706521753750674": "6303706521753750674",
                "-1890144584057974924": "-1890144584057974924",
                "-2511470351944668468": "-2511470351944668468",
                "307615103945191939": "307615103945191939",
                "529109163143907187": "529109163143907187",
                "-189750276835866417": "-189750276835866417",
                "5762318980170671533": "5762318980170671533",
                "-4866674027684997090": "-4866674027684997090",
                "7960078668173838396": "7960078668173838396",
                "-6679493499293089569": "-6679493499293089569",
                "-6585673403332403448": "-6585673403332403448",
                "-8067411658333831109": "-8067411658333831109",
                "2185481309563994909": "2185481309563994909",
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
                "5311635281710159683": "5311635281710159683_B2/acquisition",
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
                "-5736929023074161844": "-5736929023074161844_B4/acquisition",
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
                "-8161414599441454486": "-8161414599441454486",
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
                "-6951477704267723434": "-6951477704267723434",
            },
        },
    },
    "pulses": {
        "-8161414599441454486": {
            "length": 40,
            "waveforms": {
                "I": "-8161414599441454486_i",
                "Q": "-8161414599441454486_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6951477704267723434": {
            "length": 40,
            "waveforms": {
                "I": "-6951477704267723434_i",
                "Q": "-6951477704267723434_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2124430296495305353": {
            "length": 100,
            "waveforms": {
                "single": "-2124430296495305353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5311635281710159683_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "251903384474872802_i",
                "Q": "251903384474872802_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-5736929023074161844_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8167257614290370612_i",
                "Q": "-8167257614290370612_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-5408061569268076231": {
            "length": 100,
            "waveforms": {
                "single": "-5408061569268076231",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6360682666362597223": {
            "length": 16,
            "waveforms": {
                "single": "6360682666362597223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1306672390158953146": {
            "length": 16,
            "waveforms": {
                "single": "-1306672390158953146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8558442354365764086": {
            "length": 16,
            "waveforms": {
                "single": "8558442354365764086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3936232462337249580": {
            "length": 16,
            "waveforms": {
                "single": "-3936232462337249580",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2567104709927581357": {
            "length": 16,
            "waveforms": {
                "single": "2567104709927581357",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-35240460133939808": {
            "length": 16,
            "waveforms": {
                "single": "-35240460133939808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5377444750009971226": {
            "length": 16,
            "waveforms": {
                "single": "-5377444750009971226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3494737042692681629": {
            "length": 16,
            "waveforms": {
                "single": "3494737042692681629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3716231101891396877": {
            "length": 16,
            "waveforms": {
                "single": "3716231101891396877",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7395729044895991401": {
            "length": 16,
            "waveforms": {
                "single": "7395729044895991401",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8504370202969326016": {
            "length": 16,
            "waveforms": {
                "single": "-8504370202969326016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5371298673524537852": {
            "length": 16,
            "waveforms": {
                "single": "5371298673524537852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7299543466788223530": {
            "length": 16,
            "waveforms": {
                "single": "-7299543466788223530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4824589375369054453": {
            "length": 16,
            "waveforms": {
                "single": "-4824589375369054453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8002163320489781033": {
            "length": 16,
            "waveforms": {
                "single": "8002163320489781033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5644475895155082555": {
            "length": 16,
            "waveforms": {
                "single": "-5644475895155082555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8246821065216603720": {
            "length": 16,
            "waveforms": {
                "single": "-8246821065216603720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7847557339730653676": {
            "length": 20,
            "waveforms": {
                "single": "7847557339730653676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2827874188859592004": {
            "length": 20,
            "waveforms": {
                "single": "2827874188859592004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4373043965130069217": {
            "length": 20,
            "waveforms": {
                "single": "-4373043965130069217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6406345052057932030": {
            "length": 20,
            "waveforms": {
                "single": "6406345052057932030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3168217228948966731": {
            "length": 24,
            "waveforms": {
                "single": "-3168217228948966731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2946723169750251483": {
            "length": 24,
            "waveforms": {
                "single": "-2946723169750251483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8288927459626282901": {
            "length": 24,
            "waveforms": {
                "single": "-8288927459626282901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3766609689536279585": {
            "length": 24,
            "waveforms": {
                "single": "-3766609689536279585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4387935457422973129": {
            "length": 28,
            "waveforms": {
                "single": "-4387935457422973129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4484246335279679726": {
            "length": 28,
            "waveforms": {
                "single": "4484246335279679726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7017495529601269563": {
            "length": 28,
            "waveforms": {
                "single": "-7017495529601269563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6682006023282846589": {
            "length": 28,
            "waveforms": {
                "single": "6682006023282846589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3885853874692366872": {
            "length": 32,
            "waveforms": {
                "single": "3885853874692366872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3264528106805673328": {
            "length": 32,
            "waveforms": {
                "single": "3264528106805673328",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6632555313206195179": {
            "length": 32,
            "waveforms": {
                "single": "-6632555313206195179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6411061254007479931": {
            "length": 32,
            "waveforms": {
                "single": "-6411061254007479931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1618300711609764132": {
            "length": 36,
            "waveforms": {
                "single": "1618300711609764132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2510069251804170159": {
            "length": 36,
            "waveforms": {
                "single": "-2510069251804170159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7355045492720547073": {
            "length": 36,
            "waveforms": {
                "single": "7355045492720547073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1019908251022451278": {
            "length": 36,
            "waveforms": {
                "single": "1019908251022451278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3494862342441620355": {
            "length": 40,
            "waveforms": {
                "single": "3494862342441620355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9175979797871141027": {
            "length": 40,
            "waveforms": {
                "single": "-9175979797871141027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2568534584463466830": {
            "length": 40,
            "waveforms": {
                "single": "2568534584463466830",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7118659941228927913": {
            "length": 40,
            "waveforms": {
                "single": "7118659941228927913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "367936889482265565": {
            "length": 44,
            "waveforms": {
                "single": "367936889482265565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7299418167039284804": {
            "length": 44,
            "waveforms": {
                "single": "-7299418167039284804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1572763625663368051": {
            "length": 44,
            "waveforms": {
                "single": "1572763625663368051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8517765834491970378": {
            "length": 44,
            "waveforms": {
                "single": "8517765834491970378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7725094216822717545": {
            "length": 48,
            "waveforms": {
                "single": "7725094216822717545",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5372728548060423325": {
            "length": 48,
            "waveforms": {
                "single": "5372728548060423325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4201833732946475436": {
            "length": 48,
            "waveforms": {
                "single": "-4201833732946475436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2498008734187650029": {
            "length": 48,
            "waveforms": {
                "single": "-2498008734187650029",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2276514674988934781": {
            "length": 52,
            "waveforms": {
                "single": "-2276514674988934781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5643046020619197082": {
            "length": 52,
            "waveforms": {
                "single": "-5643046020619197082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5421551961420481834": {
            "length": 52,
            "waveforms": {
                "single": "-5421551961420481834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2113068517792575645": {
            "length": 52,
            "waveforms": {
                "single": "-2113068517792575645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1891574458593860397": {
            "length": 56,
            "waveforms": {
                "single": "-1891574458593860397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7067779356616391030": {
            "length": 56,
            "waveforms": {
                "single": "-7067779356616391030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2009417543609449375": {
            "length": 56,
            "waveforms": {
                "single": "2009417543609449375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "527679288608021714": {
            "length": 56,
            "waveforms": {
                "single": "527679288608021714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8508991644289112676": {
            "length": 60,
            "waveforms": {
                "single": "-8508991644289112676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8287497585090397428": {
            "length": 60,
            "waveforms": {
                "single": "-8287497585090397428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "584684207612255427": {
            "length": 60,
            "waveforms": {
                "single": "584684207612255427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6089737897087230565": {
            "length": 60,
            "waveforms": {
                "single": "-6089737897087230565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5965777509981595377": {
            "length": 64,
            "waveforms": {
                "single": "-5965777509981595377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-856528080060466219": {
            "length": 64,
            "waveforms": {
                "single": "-856528080060466219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8939468946630583141": {
            "length": 64,
            "waveforms": {
                "single": "-8939468946630583141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8237147771840901884": {
            "length": 64,
            "waveforms": {
                "single": "8237147771840901884",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1562725667141415892": {
            "length": 68,
            "waveforms": {
                "single": "1562725667141415892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6085043437231419208": {
            "length": 68,
            "waveforms": {
                "single": "6085043437231419208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6795935484168180238": {
            "length": 68,
            "waveforms": {
                "single": "6795935484168180238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8333034671036793509": {
            "length": 68,
            "waveforms": {
                "single": "-8333034671036793509",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8610229074452795723": {
            "length": 72,
            "waveforms": {
                "single": "-8610229074452795723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6641329503409052881": {
            "length": 72,
            "waveforms": {
                "single": "6641329503409052881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4709237072249485951": {
            "length": 72,
            "waveforms": {
                "single": "-4709237072249485951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-902065166006862300": {
            "length": 72,
            "waveforms": {
                "single": "-902065166006862300",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1179259569422864514": {
            "length": 76,
            "waveforms": {
                "single": "-1179259569422864514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7026269719804127265": {
            "length": 76,
            "waveforms": {
                "single": "7026269719804127265",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7247763779002842513": {
            "length": 76,
            "waveforms": {
                "single": "7247763779002842513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "369366764018151038": {
            "length": 76,
            "waveforms": {
                "single": "369366764018151038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9001220606703542240": {
            "length": 80,
            "waveforms": {
                "single": "-9001220606703542240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3899344266844772475": {
            "length": 80,
            "waveforms": {
                "single": "3899344266844772475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3768010789676777894": {
            "length": 80,
            "waveforms": {
                "single": "-3768010789676777894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "754306980413225422": {
            "length": 80,
            "waveforms": {
                "single": "754306980413225422",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6318598014046654586": {
            "length": 84,
            "waveforms": {
                "single": "6318598014046654586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1348757042474895783": {
            "length": 84,
            "waveforms": {
                "single": "-1348757042474895783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2496578859651764556": {
            "length": 84,
            "waveforms": {
                "single": "-2496578859651764556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3884452774551868563": {
            "length": 84,
            "waveforms": {
                "single": "3884452774551868563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8406770544641871879": {
            "length": 88,
            "waveforms": {
                "single": "8406770544641871879",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-77325112449882445": {
            "length": 88,
            "waveforms": {
                "single": "-77325112449882445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6303706521753750674": {
            "length": 88,
            "waveforms": {
                "single": "6303706521753750674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1890144584057974924": {
            "length": 88,
            "waveforms": {
                "single": "-1890144584057974924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2511470351944668468": {
            "length": 92,
            "waveforms": {
                "single": "-2511470351944668468",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "307615103945191939": {
            "length": 92,
            "waveforms": {
                "single": "307615103945191939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "529109163143907187": {
            "length": 92,
            "waveforms": {
                "single": "529109163143907187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-189750276835866417": {
            "length": 92,
            "waveforms": {
                "single": "-189750276835866417",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5762318980170671533": {
            "length": 96,
            "waveforms": {
                "single": "5762318980170671533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4866674027684997090": {
            "length": 96,
            "waveforms": {
                "single": "-4866674027684997090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7960078668173838396": {
            "length": 96,
            "waveforms": {
                "single": "7960078668173838396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6679493499293089569": {
            "length": 96,
            "waveforms": {
                "single": "-6679493499293089569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6585673403332403448": {
            "length": 100,
            "waveforms": {
                "single": "-6585673403332403448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8067411658333831109": {
            "length": 100,
            "waveforms": {
                "single": "-8067411658333831109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2185481309563994909": {
            "length": 100,
            "waveforms": {
                "single": "2185481309563994909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8161414599441454486_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-8161414599441454486_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-6951477704267723434_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-6951477704267723434_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-2124430296495305353": {
            "sample": -0.2388,
            "type": "constant",
        },
        "251903384474872802_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "251903384474872802_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8167257614290370612_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-8167257614290370612_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5408061569268076231": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6360682666362597223": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1306672390158953146": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "8558442354365764086": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-3936232462337249580": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2567104709927581357": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-35240460133939808": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-5377444750009971226": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3494737042692681629": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "3716231101891396877": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "7395729044895991401": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8504370202969326016": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "5371298673524537852": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-7299543466788223530": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-4824589375369054453": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8002163320489781033": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5644475895155082555": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8246821065216603720": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7847557339730653676": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2827874188859592004": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4373043965130069217": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6406345052057932030": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3168217228948966731": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2946723169750251483": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8288927459626282901": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3766609689536279585": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4387935457422973129": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4484246335279679726": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7017495529601269563": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "6682006023282846589": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3885853874692366872": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3264528106805673328": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6632555313206195179": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6411061254007479931": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1618300711609764132": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2510069251804170159": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7355045492720547073": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
        },
        "1019908251022451278": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3494862342441620355": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9175979797871141027": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2568534584463466830": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
        },
        "7118659941228927913": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "367936889482265565": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7299418167039284804": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1572763625663368051": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
        },
        "8517765834491970378": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7725094216822717545": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5372728548060423325": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4201833732946475436": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2498008734187650029": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2276514674988934781": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5643046020619197082": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5421551961420481834": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-2113068517792575645": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1891574458593860397": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7067779356616391030": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2009417543609449375": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
        },
        "527679288608021714": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8508991644289112676": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8287497585090397428": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "584684207612255427": {
            "samples": [0.12311557788944723] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-6089737897087230565": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5965777509981595377": {
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-856528080060466219": {
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8939468946630583141": {
            "samples": [0.12311557788944723] * 63 + [0.0],
            "type": "arbitrary",
        },
        "8237147771840901884": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1562725667141415892": {
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6085043437231419208": {
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6795935484168180238": {
            "samples": [0.12311557788944723] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-8333034671036793509": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8610229074452795723": {
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6641329503409052881": {
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4709237072249485951": {
            "samples": [0.12311557788944723] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-902065166006862300": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1179259569422864514": {
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7026269719804127265": {
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7247763779002842513": {
            "samples": [0.12311557788944723] * 75 + [0.0],
            "type": "arbitrary",
        },
        "369366764018151038": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-9001220606703542240": {
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3899344266844772475": {
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3768010789676777894": {
            "samples": [0.12311557788944723] * 79 + [0.0],
            "type": "arbitrary",
        },
        "754306980413225422": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6318598014046654586": {
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1348757042474895783": {
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2496578859651764556": {
            "samples": [0.12311557788944723] * 83 + [0.0],
            "type": "arbitrary",
        },
        "3884452774551868563": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "8406770544641871879": {
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-77325112449882445": {
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6303706521753750674": {
            "samples": [0.12311557788944723] * 87 + [0.0],
            "type": "arbitrary",
        },
        "-1890144584057974924": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2511470351944668468": {
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "307615103945191939": {
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "529109163143907187": {
            "samples": [0.12311557788944723] * 91 + [0.0],
            "type": "arbitrary",
        },
        "-189750276835866417": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5762318980170671533": {
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4866674027684997090": {
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7960078668173838396": {
            "samples": [0.12311557788944723] * 95 + [0.0],
            "type": "arbitrary",
        },
        "-6679493499293089569": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6585673403332403448": {
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8067411658333831109": {
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2185481309563994909": {
            "samples": [0.12311557788944723] * 99 + [0.0],
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
                "-2124430296495305353": "-2124430296495305353",
                "-5408061569268076231": "-5408061569268076231",
                "6360682666362597223": "6360682666362597223",
                "-1306672390158953146": "-1306672390158953146",
                "8558442354365764086": "8558442354365764086",
                "-3936232462337249580": "-3936232462337249580",
                "2567104709927581357": "2567104709927581357",
                "-35240460133939808": "-35240460133939808",
                "-5377444750009971226": "-5377444750009971226",
                "3494737042692681629": "3494737042692681629",
                "3716231101891396877": "3716231101891396877",
                "7395729044895991401": "7395729044895991401",
                "-8504370202969326016": "-8504370202969326016",
                "5371298673524537852": "5371298673524537852",
                "-7299543466788223530": "-7299543466788223530",
                "-4824589375369054453": "-4824589375369054453",
                "8002163320489781033": "8002163320489781033",
                "-5644475895155082555": "-5644475895155082555",
                "-8246821065216603720": "-8246821065216603720",
                "7847557339730653676": "7847557339730653676",
                "2827874188859592004": "2827874188859592004",
                "-4373043965130069217": "-4373043965130069217",
                "6406345052057932030": "6406345052057932030",
                "-3168217228948966731": "-3168217228948966731",
                "-2946723169750251483": "-2946723169750251483",
                "-8288927459626282901": "-8288927459626282901",
                "-3766609689536279585": "-3766609689536279585",
                "-4387935457422973129": "-4387935457422973129",
                "4484246335279679726": "4484246335279679726",
                "-7017495529601269563": "-7017495529601269563",
                "6682006023282846589": "6682006023282846589",
                "3885853874692366872": "3885853874692366872",
                "3264528106805673328": "3264528106805673328",
                "-6632555313206195179": "-6632555313206195179",
                "-6411061254007479931": "-6411061254007479931",
                "1618300711609764132": "1618300711609764132",
                "-2510069251804170159": "-2510069251804170159",
                "7355045492720547073": "7355045492720547073",
                "1019908251022451278": "1019908251022451278",
                "3494862342441620355": "3494862342441620355",
                "-9175979797871141027": "-9175979797871141027",
                "2568534584463466830": "2568534584463466830",
                "7118659941228927913": "7118659941228927913",
                "367936889482265565": "367936889482265565",
                "-7299418167039284804": "-7299418167039284804",
                "1572763625663368051": "1572763625663368051",
                "8517765834491970378": "8517765834491970378",
                "7725094216822717545": "7725094216822717545",
                "5372728548060423325": "5372728548060423325",
                "-4201833732946475436": "-4201833732946475436",
                "-2498008734187650029": "-2498008734187650029",
                "-2276514674988934781": "-2276514674988934781",
                "-5643046020619197082": "-5643046020619197082",
                "-5421551961420481834": "-5421551961420481834",
                "-2113068517792575645": "-2113068517792575645",
                "-1891574458593860397": "-1891574458593860397",
                "-7067779356616391030": "-7067779356616391030",
                "2009417543609449375": "2009417543609449375",
                "527679288608021714": "527679288608021714",
                "-8508991644289112676": "-8508991644289112676",
                "-8287497585090397428": "-8287497585090397428",
                "584684207612255427": "584684207612255427",
                "-6089737897087230565": "-6089737897087230565",
                "-5965777509981595377": "-5965777509981595377",
                "-856528080060466219": "-856528080060466219",
                "-8939468946630583141": "-8939468946630583141",
                "8237147771840901884": "8237147771840901884",
                "1562725667141415892": "1562725667141415892",
                "6085043437231419208": "6085043437231419208",
                "6795935484168180238": "6795935484168180238",
                "-8333034671036793509": "-8333034671036793509",
                "-8610229074452795723": "-8610229074452795723",
                "6641329503409052881": "6641329503409052881",
                "-4709237072249485951": "-4709237072249485951",
                "-902065166006862300": "-902065166006862300",
                "-1179259569422864514": "-1179259569422864514",
                "7026269719804127265": "7026269719804127265",
                "7247763779002842513": "7247763779002842513",
                "369366764018151038": "369366764018151038",
                "-9001220606703542240": "-9001220606703542240",
                "3899344266844772475": "3899344266844772475",
                "-3768010789676777894": "-3768010789676777894",
                "754306980413225422": "754306980413225422",
                "6318598014046654586": "6318598014046654586",
                "-1348757042474895783": "-1348757042474895783",
                "-2496578859651764556": "-2496578859651764556",
                "3884452774551868563": "3884452774551868563",
                "8406770544641871879": "8406770544641871879",
                "-77325112449882445": "-77325112449882445",
                "6303706521753750674": "6303706521753750674",
                "-1890144584057974924": "-1890144584057974924",
                "-2511470351944668468": "-2511470351944668468",
                "307615103945191939": "307615103945191939",
                "529109163143907187": "529109163143907187",
                "-189750276835866417": "-189750276835866417",
                "5762318980170671533": "5762318980170671533",
                "-4866674027684997090": "-4866674027684997090",
                "7960078668173838396": "7960078668173838396",
                "-6679493499293089569": "-6679493499293089569",
                "-6585673403332403448": "-6585673403332403448",
                "-8067411658333831109": "-8067411658333831109",
                "2185481309563994909": "2185481309563994909",
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
                "5311635281710159683": "5311635281710159683_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_8ba",
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
                "-5736929023074161844": "-5736929023074161844_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_c8a",
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
                "-8161414599441454486": "-8161414599441454486",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_49c",
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
                "-6951477704267723434": "-6951477704267723434",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_b6f",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "-8161414599441454486": {
            "length": 40,
            "waveforms": {
                "I": "-8161414599441454486_i",
                "Q": "-8161414599441454486_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6951477704267723434": {
            "length": 40,
            "waveforms": {
                "I": "-6951477704267723434_i",
                "Q": "-6951477704267723434_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2124430296495305353": {
            "length": 100,
            "waveforms": {
                "single": "-2124430296495305353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5311635281710159683_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "251903384474872802_i",
                "Q": "251903384474872802_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-5736929023074161844_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8167257614290370612_i",
                "Q": "-8167257614290370612_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-5408061569268076231": {
            "length": 100,
            "waveforms": {
                "single": "-5408061569268076231",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6360682666362597223": {
            "length": 16,
            "waveforms": {
                "single": "6360682666362597223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1306672390158953146": {
            "length": 16,
            "waveforms": {
                "single": "-1306672390158953146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8558442354365764086": {
            "length": 16,
            "waveforms": {
                "single": "8558442354365764086",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3936232462337249580": {
            "length": 16,
            "waveforms": {
                "single": "-3936232462337249580",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2567104709927581357": {
            "length": 16,
            "waveforms": {
                "single": "2567104709927581357",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-35240460133939808": {
            "length": 16,
            "waveforms": {
                "single": "-35240460133939808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5377444750009971226": {
            "length": 16,
            "waveforms": {
                "single": "-5377444750009971226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3494737042692681629": {
            "length": 16,
            "waveforms": {
                "single": "3494737042692681629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3716231101891396877": {
            "length": 16,
            "waveforms": {
                "single": "3716231101891396877",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7395729044895991401": {
            "length": 16,
            "waveforms": {
                "single": "7395729044895991401",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8504370202969326016": {
            "length": 16,
            "waveforms": {
                "single": "-8504370202969326016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5371298673524537852": {
            "length": 16,
            "waveforms": {
                "single": "5371298673524537852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7299543466788223530": {
            "length": 16,
            "waveforms": {
                "single": "-7299543466788223530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4824589375369054453": {
            "length": 16,
            "waveforms": {
                "single": "-4824589375369054453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8002163320489781033": {
            "length": 16,
            "waveforms": {
                "single": "8002163320489781033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5644475895155082555": {
            "length": 16,
            "waveforms": {
                "single": "-5644475895155082555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8246821065216603720": {
            "length": 16,
            "waveforms": {
                "single": "-8246821065216603720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7847557339730653676": {
            "length": 20,
            "waveforms": {
                "single": "7847557339730653676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2827874188859592004": {
            "length": 20,
            "waveforms": {
                "single": "2827874188859592004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4373043965130069217": {
            "length": 20,
            "waveforms": {
                "single": "-4373043965130069217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6406345052057932030": {
            "length": 20,
            "waveforms": {
                "single": "6406345052057932030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3168217228948966731": {
            "length": 24,
            "waveforms": {
                "single": "-3168217228948966731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2946723169750251483": {
            "length": 24,
            "waveforms": {
                "single": "-2946723169750251483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8288927459626282901": {
            "length": 24,
            "waveforms": {
                "single": "-8288927459626282901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3766609689536279585": {
            "length": 24,
            "waveforms": {
                "single": "-3766609689536279585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4387935457422973129": {
            "length": 28,
            "waveforms": {
                "single": "-4387935457422973129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4484246335279679726": {
            "length": 28,
            "waveforms": {
                "single": "4484246335279679726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7017495529601269563": {
            "length": 28,
            "waveforms": {
                "single": "-7017495529601269563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6682006023282846589": {
            "length": 28,
            "waveforms": {
                "single": "6682006023282846589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3885853874692366872": {
            "length": 32,
            "waveforms": {
                "single": "3885853874692366872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3264528106805673328": {
            "length": 32,
            "waveforms": {
                "single": "3264528106805673328",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6632555313206195179": {
            "length": 32,
            "waveforms": {
                "single": "-6632555313206195179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6411061254007479931": {
            "length": 32,
            "waveforms": {
                "single": "-6411061254007479931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1618300711609764132": {
            "length": 36,
            "waveforms": {
                "single": "1618300711609764132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2510069251804170159": {
            "length": 36,
            "waveforms": {
                "single": "-2510069251804170159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7355045492720547073": {
            "length": 36,
            "waveforms": {
                "single": "7355045492720547073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1019908251022451278": {
            "length": 36,
            "waveforms": {
                "single": "1019908251022451278",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3494862342441620355": {
            "length": 40,
            "waveforms": {
                "single": "3494862342441620355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9175979797871141027": {
            "length": 40,
            "waveforms": {
                "single": "-9175979797871141027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2568534584463466830": {
            "length": 40,
            "waveforms": {
                "single": "2568534584463466830",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7118659941228927913": {
            "length": 40,
            "waveforms": {
                "single": "7118659941228927913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "367936889482265565": {
            "length": 44,
            "waveforms": {
                "single": "367936889482265565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7299418167039284804": {
            "length": 44,
            "waveforms": {
                "single": "-7299418167039284804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1572763625663368051": {
            "length": 44,
            "waveforms": {
                "single": "1572763625663368051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8517765834491970378": {
            "length": 44,
            "waveforms": {
                "single": "8517765834491970378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7725094216822717545": {
            "length": 48,
            "waveforms": {
                "single": "7725094216822717545",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5372728548060423325": {
            "length": 48,
            "waveforms": {
                "single": "5372728548060423325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4201833732946475436": {
            "length": 48,
            "waveforms": {
                "single": "-4201833732946475436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2498008734187650029": {
            "length": 48,
            "waveforms": {
                "single": "-2498008734187650029",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2276514674988934781": {
            "length": 52,
            "waveforms": {
                "single": "-2276514674988934781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5643046020619197082": {
            "length": 52,
            "waveforms": {
                "single": "-5643046020619197082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5421551961420481834": {
            "length": 52,
            "waveforms": {
                "single": "-5421551961420481834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2113068517792575645": {
            "length": 52,
            "waveforms": {
                "single": "-2113068517792575645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1891574458593860397": {
            "length": 56,
            "waveforms": {
                "single": "-1891574458593860397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7067779356616391030": {
            "length": 56,
            "waveforms": {
                "single": "-7067779356616391030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2009417543609449375": {
            "length": 56,
            "waveforms": {
                "single": "2009417543609449375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "527679288608021714": {
            "length": 56,
            "waveforms": {
                "single": "527679288608021714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8508991644289112676": {
            "length": 60,
            "waveforms": {
                "single": "-8508991644289112676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8287497585090397428": {
            "length": 60,
            "waveforms": {
                "single": "-8287497585090397428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "584684207612255427": {
            "length": 60,
            "waveforms": {
                "single": "584684207612255427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6089737897087230565": {
            "length": 60,
            "waveforms": {
                "single": "-6089737897087230565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5965777509981595377": {
            "length": 64,
            "waveforms": {
                "single": "-5965777509981595377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-856528080060466219": {
            "length": 64,
            "waveforms": {
                "single": "-856528080060466219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8939468946630583141": {
            "length": 64,
            "waveforms": {
                "single": "-8939468946630583141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8237147771840901884": {
            "length": 64,
            "waveforms": {
                "single": "8237147771840901884",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1562725667141415892": {
            "length": 68,
            "waveforms": {
                "single": "1562725667141415892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6085043437231419208": {
            "length": 68,
            "waveforms": {
                "single": "6085043437231419208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6795935484168180238": {
            "length": 68,
            "waveforms": {
                "single": "6795935484168180238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8333034671036793509": {
            "length": 68,
            "waveforms": {
                "single": "-8333034671036793509",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8610229074452795723": {
            "length": 72,
            "waveforms": {
                "single": "-8610229074452795723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6641329503409052881": {
            "length": 72,
            "waveforms": {
                "single": "6641329503409052881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4709237072249485951": {
            "length": 72,
            "waveforms": {
                "single": "-4709237072249485951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-902065166006862300": {
            "length": 72,
            "waveforms": {
                "single": "-902065166006862300",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1179259569422864514": {
            "length": 76,
            "waveforms": {
                "single": "-1179259569422864514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7026269719804127265": {
            "length": 76,
            "waveforms": {
                "single": "7026269719804127265",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7247763779002842513": {
            "length": 76,
            "waveforms": {
                "single": "7247763779002842513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "369366764018151038": {
            "length": 76,
            "waveforms": {
                "single": "369366764018151038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9001220606703542240": {
            "length": 80,
            "waveforms": {
                "single": "-9001220606703542240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3899344266844772475": {
            "length": 80,
            "waveforms": {
                "single": "3899344266844772475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3768010789676777894": {
            "length": 80,
            "waveforms": {
                "single": "-3768010789676777894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "754306980413225422": {
            "length": 80,
            "waveforms": {
                "single": "754306980413225422",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6318598014046654586": {
            "length": 84,
            "waveforms": {
                "single": "6318598014046654586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1348757042474895783": {
            "length": 84,
            "waveforms": {
                "single": "-1348757042474895783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2496578859651764556": {
            "length": 84,
            "waveforms": {
                "single": "-2496578859651764556",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3884452774551868563": {
            "length": 84,
            "waveforms": {
                "single": "3884452774551868563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8406770544641871879": {
            "length": 88,
            "waveforms": {
                "single": "8406770544641871879",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-77325112449882445": {
            "length": 88,
            "waveforms": {
                "single": "-77325112449882445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6303706521753750674": {
            "length": 88,
            "waveforms": {
                "single": "6303706521753750674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1890144584057974924": {
            "length": 88,
            "waveforms": {
                "single": "-1890144584057974924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2511470351944668468": {
            "length": 92,
            "waveforms": {
                "single": "-2511470351944668468",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "307615103945191939": {
            "length": 92,
            "waveforms": {
                "single": "307615103945191939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "529109163143907187": {
            "length": 92,
            "waveforms": {
                "single": "529109163143907187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-189750276835866417": {
            "length": 92,
            "waveforms": {
                "single": "-189750276835866417",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5762318980170671533": {
            "length": 96,
            "waveforms": {
                "single": "5762318980170671533",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4866674027684997090": {
            "length": 96,
            "waveforms": {
                "single": "-4866674027684997090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7960078668173838396": {
            "length": 96,
            "waveforms": {
                "single": "7960078668173838396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6679493499293089569": {
            "length": 96,
            "waveforms": {
                "single": "-6679493499293089569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6585673403332403448": {
            "length": 100,
            "waveforms": {
                "single": "-6585673403332403448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8067411658333831109": {
            "length": 100,
            "waveforms": {
                "single": "-8067411658333831109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2185481309563994909": {
            "length": 100,
            "waveforms": {
                "single": "2185481309563994909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8161414599441454486_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8161414599441454486_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6951477704267723434_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6951477704267723434_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2124430296495305353": {
            "sample": -0.2388,
            "type": "constant",
        },
        "251903384474872802_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "251903384474872802_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8167257614290370612_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-8167257614290370612_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5408061569268076231": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6360682666362597223": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1306672390158953146": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8558442354365764086": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3936232462337249580": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2567104709927581357": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-35240460133939808": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5377444750009971226": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3494737042692681629": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3716231101891396877": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7395729044895991401": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8504370202969326016": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5371298673524537852": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7299543466788223530": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4824589375369054453": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8002163320489781033": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5644475895155082555": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8246821065216603720": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7847557339730653676": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2827874188859592004": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4373043965130069217": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6406345052057932030": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3168217228948966731": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2946723169750251483": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8288927459626282901": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3766609689536279585": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4387935457422973129": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4484246335279679726": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7017495529601269563": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6682006023282846589": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3885853874692366872": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3264528106805673328": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6632555313206195179": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6411061254007479931": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1618300711609764132": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2510069251804170159": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7355045492720547073": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1019908251022451278": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3494862342441620355": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9175979797871141027": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2568534584463466830": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7118659941228927913": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "367936889482265565": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7299418167039284804": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1572763625663368051": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8517765834491970378": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7725094216822717545": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5372728548060423325": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4201833732946475436": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2498008734187650029": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2276514674988934781": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5643046020619197082": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5421551961420481834": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2113068517792575645": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1891574458593860397": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7067779356616391030": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2009417543609449375": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "527679288608021714": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8508991644289112676": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8287497585090397428": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "584684207612255427": {
            "samples": [0.12311557788944723] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6089737897087230565": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5965777509981595377": {
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-856528080060466219": {
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8939468946630583141": {
            "samples": [0.12311557788944723] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8237147771840901884": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1562725667141415892": {
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6085043437231419208": {
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6795935484168180238": {
            "samples": [0.12311557788944723] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8333034671036793509": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8610229074452795723": {
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6641329503409052881": {
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4709237072249485951": {
            "samples": [0.12311557788944723] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-902065166006862300": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1179259569422864514": {
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7026269719804127265": {
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7247763779002842513": {
            "samples": [0.12311557788944723] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "369366764018151038": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-9001220606703542240": {
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3899344266844772475": {
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3768010789676777894": {
            "samples": [0.12311557788944723] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "754306980413225422": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6318598014046654586": {
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1348757042474895783": {
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2496578859651764556": {
            "samples": [0.12311557788944723] * 83 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3884452774551868563": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "8406770544641871879": {
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-77325112449882445": {
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6303706521753750674": {
            "samples": [0.12311557788944723] * 87 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1890144584057974924": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2511470351944668468": {
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "307615103945191939": {
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "529109163143907187": {
            "samples": [0.12311557788944723] * 91 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-189750276835866417": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5762318980170671533": {
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4866674027684997090": {
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7960078668173838396": {
            "samples": [0.12311557788944723] * 95 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6679493499293089569": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6585673403332403448": {
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8067411658333831109": {
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2185481309563994909": {
            "samples": [0.12311557788944723] * 99 + [0.0],
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
        "B2/acquisition_mixer_8ba": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_c8a": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_49c": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_b6f": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

