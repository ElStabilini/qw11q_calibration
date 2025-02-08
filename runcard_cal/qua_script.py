
# Single QUA script generated at 2025-02-08 17:06:31.598926
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
            with for_(v9,-1.99,(v9<-1.546672222222222),(v9+0.0022111111111111637)):
                align()
                play("-7158952584179743687", "B2/drive")
                play("5560492648399597716", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-1558129014401389839"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("8805674192738044855"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-8930177834034745731"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-6111092378144885324"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-6732418146031578868"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-2210100375941575552"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-1988606316742860304"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("8292094237830423481"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("5939728569068129261"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("920045418197067589"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("5442363188287070905"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("8358982316270011372"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-5076045999611491146"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-4854551940412775898"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("5827303404682145289"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-2656792252409609035"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-2435298193210893787"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("2576417564617155311"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("2797911623815870559"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-568619721814391742"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("4995671311819037422"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("8802843218061661073"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("3182851840210944943"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-12333655636758069"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("5380611528214111806"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("3028245859451817586"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("4454283770235958281"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("6929237861655127358"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("5447499606653699697"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-5413668981266793353"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-7766034650029087573"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-4086536707024493049"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-5568274962025920710"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-4142237051241780015"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-335065144999156364"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-113571085800441116"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("1862694543004010499"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("2084188602202725747"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-6109662503608999851"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-6730988271495693395"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-3911902815605832988"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("-8931585966476894660"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-4311734524293811284"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("1542801060619646606"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-6124553995901903763"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("3740560748622813469"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-3926794307898736900"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("7769226714064152368"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("9195264624848293063"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("6870706542761456610"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-7053719760858091690"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("3725669256329909557"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("2577847439153040784"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-4634466013656209579"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("3571063275570782200"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("598743803370554767"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("8804273092597546546"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("2796503491373721630"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-7444711293108838207"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("5382041402749997279"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("-1368681648996665069"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("-8043103753696151061"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("829078039006501794"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("207752271119808250"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("-7986098834691917348"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-7764604775493202100"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-390640189467504604"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("-5566845087490035237"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("814186546713597882"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("-333635270463270891"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("7040329315562426605"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("1864124417539895972"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("2085618476738611220"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-5581736579782939149"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("4283378164741778083"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("-6401623099568967251"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-8930156091941009187"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-8708662032742293939"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("-5889576576852433532"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("-6510902344739127076"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("-1323019263301330262"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("-8323721816347219555"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("-7109294805326439930"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("1762886987376212925"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("-8478327797106346912"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("-7052289886322206217"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("321674699703491279"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("8527203988930483058"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("-4633036139120324106"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("-825864232877700455"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("4185851524950348643"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("-1645750752663728557"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("-2267076520550422101"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("6605105272152230754"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("6826599331350946002"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("5785218752366202652"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("-8041673879160265588"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("830507913542387267"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("-4189175237328674405"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("-4290202317134928903"*amp(v9), "B4/flux")
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
                play("5560492648399597716", "B4/drive")
                measure("-5633416670789954898", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.06078547221045674)-(v3*0.9981508535127102))>0.0025565952953590303)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-5841315490334268105", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.6665903597333165)-(v6*0.7454242364657911))>-0.0004342766968863211)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(201).buffer(100).average().save("-5633416670789954898_B2|acquisition_shots")
        r2.buffer(201).buffer(100).average().save("-5841315490334268105_B4|acquisition_shots")


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
                "7841448908339740536": "7841448908339740536",
                "3249761660744269378": "3249761660744269378",
                "-1558129014401389839": "-1558129014401389839",
                "8805674192738044855": "8805674192738044855",
                "-8930177834034745731": "-8930177834034745731",
                "-6111092378144885324": "-6111092378144885324",
                "-6732418146031578868": "-6732418146031578868",
                "-2210100375941575552": "-2210100375941575552",
                "-1988606316742860304": "-1988606316742860304",
                "8292094237830423481": "8292094237830423481",
                "5939728569068129261": "5939728569068129261",
                "920045418197067589": "920045418197067589",
                "5442363188287070905": "5442363188287070905",
                "8358982316270011372": "8358982316270011372",
                "-5076045999611491146": "-5076045999611491146",
                "-4854551940412775898": "-4854551940412775898",
                "5827303404682145289": "5827303404682145289",
                "-2656792252409609035": "-2656792252409609035",
                "-2435298193210893787": "-2435298193210893787",
                "2576417564617155311": "2576417564617155311",
                "2797911623815870559": "2797911623815870559",
                "-568619721814391742": "-568619721814391742",
                "4995671311819037422": "4995671311819037422",
                "8802843218061661073": "8802843218061661073",
                "3182851840210944943": "3182851840210944943",
                "-12333655636758069": "-12333655636758069",
                "5380611528214111806": "5380611528214111806",
                "3028245859451817586": "3028245859451817586",
                "4454283770235958281": "4454283770235958281",
                "6929237861655127358": "6929237861655127358",
                "5447499606653699697": "5447499606653699697",
                "-5413668981266793353": "-5413668981266793353",
                "-7766034650029087573": "-7766034650029087573",
                "-4086536707024493049": "-4086536707024493049",
                "-5568274962025920710": "-5568274962025920710",
                "-4142237051241780015": "-4142237051241780015",
                "-335065144999156364": "-335065144999156364",
                "-113571085800441116": "-113571085800441116",
                "1862694543004010499": "1862694543004010499",
                "2084188602202725747": "2084188602202725747",
                "-6109662503608999851": "-6109662503608999851",
                "-6730988271495693395": "-6730988271495693395",
                "-3911902815605832988": "-3911902815605832988",
                "-8931585966476894660": "-8931585966476894660",
                "-4311734524293811284": "-4311734524293811284",
                "1542801060619646606": "1542801060619646606",
                "-6124553995901903763": "-6124553995901903763",
                "3740560748622813469": "3740560748622813469",
                "-3926794307898736900": "-3926794307898736900",
                "7769226714064152368": "7769226714064152368",
                "9195264624848293063": "9195264624848293063",
                "6870706542761456610": "6870706542761456610",
                "-7053719760858091690": "-7053719760858091690",
                "3725669256329909557": "3725669256329909557",
                "2577847439153040784": "2577847439153040784",
                "-4634466013656209579": "-4634466013656209579",
                "3571063275570782200": "3571063275570782200",
                "598743803370554767": "598743803370554767",
                "8804273092597546546": "8804273092597546546",
                "2796503491373721630": "2796503491373721630",
                "-7444711293108838207": "-7444711293108838207",
                "5382041402749997279": "5382041402749997279",
                "-1368681648996665069": "-1368681648996665069",
                "-8043103753696151061": "-8043103753696151061",
                "829078039006501794": "829078039006501794",
                "207752271119808250": "207752271119808250",
                "-7986098834691917348": "-7986098834691917348",
                "-7764604775493202100": "-7764604775493202100",
                "-390640189467504604": "-390640189467504604",
                "-5566845087490035237": "-5566845087490035237",
                "814186546713597882": "814186546713597882",
                "-333635270463270891": "-333635270463270891",
                "7040329315562426605": "7040329315562426605",
                "1864124417539895972": "1864124417539895972",
                "2085618476738611220": "2085618476738611220",
                "-5581736579782939149": "-5581736579782939149",
                "4283378164741778083": "4283378164741778083",
                "-6401623099568967251": "-6401623099568967251",
                "-8930156091941009187": "-8930156091941009187",
                "-8708662032742293939": "-8708662032742293939",
                "-5889576576852433532": "-5889576576852433532",
                "-6510902344739127076": "-6510902344739127076",
                "-1323019263301330262": "-1323019263301330262",
                "-8323721816347219555": "-8323721816347219555",
                "-7109294805326439930": "-7109294805326439930",
                "1762886987376212925": "1762886987376212925",
                "-8478327797106346912": "-8478327797106346912",
                "-7052289886322206217": "-7052289886322206217",
                "321674699703491279": "321674699703491279",
                "8527203988930483058": "8527203988930483058",
                "-4633036139120324106": "-4633036139120324106",
                "-825864232877700455": "-825864232877700455",
                "4185851524950348643": "4185851524950348643",
                "-1645750752663728557": "-1645750752663728557",
                "-2267076520550422101": "-2267076520550422101",
                "6605105272152230754": "6605105272152230754",
                "6826599331350946002": "6826599331350946002",
                "5785218752366202652": "5785218752366202652",
                "-8041673879160265588": "-8041673879160265588",
                "830507913542387267": "830507913542387267",
                "-4189175237328674405": "-4189175237328674405",
                "-4290202317134928903": "-4290202317134928903",
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
                "-5633416670789954898": "-5633416670789954898_B2/acquisition",
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
                "5560492648399597716": "5560492648399597716",
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
                "-7158952584179743687": "-7158952584179743687",
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
                "-5841315490334268105": "-5841315490334268105_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-7158952584179743687": {
            "length": 40,
            "waveforms": {
                "I": "-7158952584179743687_i",
                "Q": "-7158952584179743687_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5560492648399597716": {
            "length": 40,
            "waveforms": {
                "I": "5560492648399597716_i",
                "Q": "5560492648399597716_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7841448908339740536": {
            "length": 100,
            "waveforms": {
                "single": "7841448908339740536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5633416670789954898_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8228961484399632925_i",
                "Q": "-8228961484399632925_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-5841315490334268105_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5247407698090181548_i",
                "Q": "-5247407698090181548_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3249761660744269378": {
            "length": 100,
            "waveforms": {
                "single": "3249761660744269378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1558129014401389839": {
            "length": 16,
            "waveforms": {
                "single": "-1558129014401389839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8805674192738044855": {
            "length": 16,
            "waveforms": {
                "single": "8805674192738044855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8930177834034745731": {
            "length": 16,
            "waveforms": {
                "single": "-8930177834034745731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6111092378144885324": {
            "length": 16,
            "waveforms": {
                "single": "-6111092378144885324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6732418146031578868": {
            "length": 16,
            "waveforms": {
                "single": "-6732418146031578868",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2210100375941575552": {
            "length": 16,
            "waveforms": {
                "single": "-2210100375941575552",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1988606316742860304": {
            "length": 16,
            "waveforms": {
                "single": "-1988606316742860304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8292094237830423481": {
            "length": 16,
            "waveforms": {
                "single": "8292094237830423481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5939728569068129261": {
            "length": 16,
            "waveforms": {
                "single": "5939728569068129261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "920045418197067589": {
            "length": 16,
            "waveforms": {
                "single": "920045418197067589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5442363188287070905": {
            "length": 16,
            "waveforms": {
                "single": "5442363188287070905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8358982316270011372": {
            "length": 16,
            "waveforms": {
                "single": "8358982316270011372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5076045999611491146": {
            "length": 16,
            "waveforms": {
                "single": "-5076045999611491146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4854551940412775898": {
            "length": 16,
            "waveforms": {
                "single": "-4854551940412775898",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5827303404682145289": {
            "length": 16,
            "waveforms": {
                "single": "5827303404682145289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2656792252409609035": {
            "length": 16,
            "waveforms": {
                "single": "-2656792252409609035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2435298193210893787": {
            "length": 16,
            "waveforms": {
                "single": "-2435298193210893787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2576417564617155311": {
            "length": 20,
            "waveforms": {
                "single": "2576417564617155311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2797911623815870559": {
            "length": 20,
            "waveforms": {
                "single": "2797911623815870559",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-568619721814391742": {
            "length": 20,
            "waveforms": {
                "single": "-568619721814391742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4995671311819037422": {
            "length": 20,
            "waveforms": {
                "single": "4995671311819037422",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8802843218061661073": {
            "length": 24,
            "waveforms": {
                "single": "8802843218061661073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3182851840210944943": {
            "length": 24,
            "waveforms": {
                "single": "3182851840210944943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-12333655636758069": {
            "length": 24,
            "waveforms": {
                "single": "-12333655636758069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5380611528214111806": {
            "length": 24,
            "waveforms": {
                "single": "5380611528214111806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3028245859451817586": {
            "length": 28,
            "waveforms": {
                "single": "3028245859451817586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4454283770235958281": {
            "length": 28,
            "waveforms": {
                "single": "4454283770235958281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6929237861655127358": {
            "length": 28,
            "waveforms": {
                "single": "6929237861655127358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5447499606653699697": {
            "length": 28,
            "waveforms": {
                "single": "5447499606653699697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5413668981266793353": {
            "length": 32,
            "waveforms": {
                "single": "-5413668981266793353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7766034650029087573": {
            "length": 32,
            "waveforms": {
                "single": "-7766034650029087573",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4086536707024493049": {
            "length": 32,
            "waveforms": {
                "single": "-4086536707024493049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5568274962025920710": {
            "length": 32,
            "waveforms": {
                "single": "-5568274962025920710",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4142237051241780015": {
            "length": 36,
            "waveforms": {
                "single": "-4142237051241780015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-335065144999156364": {
            "length": 36,
            "waveforms": {
                "single": "-335065144999156364",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-113571085800441116": {
            "length": 36,
            "waveforms": {
                "single": "-113571085800441116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1862694543004010499": {
            "length": 36,
            "waveforms": {
                "single": "1862694543004010499",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2084188602202725747": {
            "length": 40,
            "waveforms": {
                "single": "2084188602202725747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6109662503608999851": {
            "length": 40,
            "waveforms": {
                "single": "-6109662503608999851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6730988271495693395": {
            "length": 40,
            "waveforms": {
                "single": "-6730988271495693395",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3911902815605832988": {
            "length": 40,
            "waveforms": {
                "single": "-3911902815605832988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8931585966476894660": {
            "length": 44,
            "waveforms": {
                "single": "-8931585966476894660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4311734524293811284": {
            "length": 44,
            "waveforms": {
                "single": "-4311734524293811284",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1542801060619646606": {
            "length": 44,
            "waveforms": {
                "single": "1542801060619646606",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6124553995901903763": {
            "length": 44,
            "waveforms": {
                "single": "-6124553995901903763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3740560748622813469": {
            "length": 48,
            "waveforms": {
                "single": "3740560748622813469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3926794307898736900": {
            "length": 48,
            "waveforms": {
                "single": "-3926794307898736900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7769226714064152368": {
            "length": 48,
            "waveforms": {
                "single": "7769226714064152368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9195264624848293063": {
            "length": 48,
            "waveforms": {
                "single": "9195264624848293063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6870706542761456610": {
            "length": 52,
            "waveforms": {
                "single": "6870706542761456610",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7053719760858091690": {
            "length": 52,
            "waveforms": {
                "single": "-7053719760858091690",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3725669256329909557": {
            "length": 52,
            "waveforms": {
                "single": "3725669256329909557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2577847439153040784": {
            "length": 52,
            "waveforms": {
                "single": "2577847439153040784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4634466013656209579": {
            "length": 56,
            "waveforms": {
                "single": "-4634466013656209579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3571063275570782200": {
            "length": 56,
            "waveforms": {
                "single": "3571063275570782200",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "598743803370554767": {
            "length": 56,
            "waveforms": {
                "single": "598743803370554767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8804273092597546546": {
            "length": 56,
            "waveforms": {
                "single": "8804273092597546546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2796503491373721630": {
            "length": 60,
            "waveforms": {
                "single": "2796503491373721630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7444711293108838207": {
            "length": 60,
            "waveforms": {
                "single": "-7444711293108838207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5382041402749997279": {
            "length": 60,
            "waveforms": {
                "single": "5382041402749997279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1368681648996665069": {
            "length": 60,
            "waveforms": {
                "single": "-1368681648996665069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8043103753696151061": {
            "length": 64,
            "waveforms": {
                "single": "-8043103753696151061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "829078039006501794": {
            "length": 64,
            "waveforms": {
                "single": "829078039006501794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "207752271119808250": {
            "length": 64,
            "waveforms": {
                "single": "207752271119808250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7986098834691917348": {
            "length": 64,
            "waveforms": {
                "single": "-7986098834691917348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7764604775493202100": {
            "length": 68,
            "waveforms": {
                "single": "-7764604775493202100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-390640189467504604": {
            "length": 68,
            "waveforms": {
                "single": "-390640189467504604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5566845087490035237": {
            "length": 68,
            "waveforms": {
                "single": "-5566845087490035237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "814186546713597882": {
            "length": 68,
            "waveforms": {
                "single": "814186546713597882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-333635270463270891": {
            "length": 72,
            "waveforms": {
                "single": "-333635270463270891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7040329315562426605": {
            "length": 72,
            "waveforms": {
                "single": "7040329315562426605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1864124417539895972": {
            "length": 72,
            "waveforms": {
                "single": "1864124417539895972",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2085618476738611220": {
            "length": 72,
            "waveforms": {
                "single": "2085618476738611220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5581736579782939149": {
            "length": 76,
            "waveforms": {
                "single": "-5581736579782939149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4283378164741778083": {
            "length": 76,
            "waveforms": {
                "single": "4283378164741778083",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6401623099568967251": {
            "length": 76,
            "waveforms": {
                "single": "-6401623099568967251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8930156091941009187": {
            "length": 76,
            "waveforms": {
                "single": "-8930156091941009187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8708662032742293939": {
            "length": 80,
            "waveforms": {
                "single": "-8708662032742293939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5889576576852433532": {
            "length": 80,
            "waveforms": {
                "single": "-5889576576852433532",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6510902344739127076": {
            "length": 80,
            "waveforms": {
                "single": "-6510902344739127076",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1323019263301330262": {
            "length": 80,
            "waveforms": {
                "single": "-1323019263301330262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8323721816347219555": {
            "length": 84,
            "waveforms": {
                "single": "-8323721816347219555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7109294805326439930": {
            "length": 84,
            "waveforms": {
                "single": "-7109294805326439930",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1762886987376212925": {
            "length": 84,
            "waveforms": {
                "single": "1762886987376212925",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8478327797106346912": {
            "length": 84,
            "waveforms": {
                "single": "-8478327797106346912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7052289886322206217": {
            "length": 88,
            "waveforms": {
                "single": "-7052289886322206217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "321674699703491279": {
            "length": 88,
            "waveforms": {
                "single": "321674699703491279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8527203988930483058": {
            "length": 88,
            "waveforms": {
                "single": "8527203988930483058",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4633036139120324106": {
            "length": 88,
            "waveforms": {
                "single": "-4633036139120324106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-825864232877700455": {
            "length": 92,
            "waveforms": {
                "single": "-825864232877700455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4185851524950348643": {
            "length": 92,
            "waveforms": {
                "single": "4185851524950348643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1645750752663728557": {
            "length": 92,
            "waveforms": {
                "single": "-1645750752663728557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2267076520550422101": {
            "length": 92,
            "waveforms": {
                "single": "-2267076520550422101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6605105272152230754": {
            "length": 96,
            "waveforms": {
                "single": "6605105272152230754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6826599331350946002": {
            "length": 96,
            "waveforms": {
                "single": "6826599331350946002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5785218752366202652": {
            "length": 96,
            "waveforms": {
                "single": "5785218752366202652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8041673879160265588": {
            "length": 96,
            "waveforms": {
                "single": "-8041673879160265588",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "830507913542387267": {
            "length": 100,
            "waveforms": {
                "single": "830507913542387267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4189175237328674405": {
            "length": 100,
            "waveforms": {
                "single": "-4189175237328674405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4290202317134928903": {
            "length": 100,
            "waveforms": {
                "single": "-4290202317134928903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7158952584179743687_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-7158952584179743687_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "5560492648399597716_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "5560492648399597716_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "7841448908339740536": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-8228961484399632925_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-8228961484399632925_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5247407698090181548_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5247407698090181548_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3249761660744269378": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-1558129014401389839": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8805674192738044855": {
            "samples": [0.22613065326633167] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-8930177834034745731": {
            "samples": [0.22613065326633167] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-6111092378144885324": {
            "samples": [0.22613065326633167] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-6732418146031578868": {
            "samples": [0.22613065326633167] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-2210100375941575552": {
            "samples": [0.22613065326633167] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-1988606316742860304": {
            "samples": [0.22613065326633167] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "8292094237830423481": {
            "samples": [0.22613065326633167] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "5939728569068129261": {
            "samples": [0.22613065326633167] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "920045418197067589": {
            "samples": [0.22613065326633167] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "5442363188287070905": {
            "samples": [0.22613065326633167] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8358982316270011372": {
            "samples": [0.22613065326633167] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-5076045999611491146": {
            "samples": [0.22613065326633167] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-4854551940412775898": {
            "samples": [0.22613065326633167] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5827303404682145289": {
            "samples": [0.22613065326633167] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2656792252409609035": {
            "samples": [0.22613065326633167] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-2435298193210893787": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2576417564617155311": {
            "samples": [0.22613065326633167] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2797911623815870559": {
            "samples": [0.22613065326633167] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-568619721814391742": {
            "samples": [0.22613065326633167] * 19 + [0.0],
            "type": "arbitrary",
        },
        "4995671311819037422": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "8802843218061661073": {
            "samples": [0.22613065326633167] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3182851840210944943": {
            "samples": [0.22613065326633167] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-12333655636758069": {
            "samples": [0.22613065326633167] * 23 + [0.0],
            "type": "arbitrary",
        },
        "5380611528214111806": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "3028245859451817586": {
            "samples": [0.22613065326633167] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4454283770235958281": {
            "samples": [0.22613065326633167] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6929237861655127358": {
            "samples": [0.22613065326633167] * 27 + [0.0],
            "type": "arbitrary",
        },
        "5447499606653699697": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-5413668981266793353": {
            "samples": [0.22613065326633167] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7766034650029087573": {
            "samples": [0.22613065326633167] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4086536707024493049": {
            "samples": [0.22613065326633167] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5568274962025920710": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-4142237051241780015": {
            "samples": [0.22613065326633167] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-335065144999156364": {
            "samples": [0.22613065326633167] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-113571085800441116": {
            "samples": [0.22613065326633167] * 35 + [0.0],
            "type": "arbitrary",
        },
        "1862694543004010499": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2084188602202725747": {
            "samples": [0.22613065326633167] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6109662503608999851": {
            "samples": [0.22613065326633167] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6730988271495693395": {
            "samples": [0.22613065326633167] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-3911902815605832988": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8931585966476894660": {
            "samples": [0.22613065326633167] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4311734524293811284": {
            "samples": [0.22613065326633167] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1542801060619646606": {
            "samples": [0.22613065326633167] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-6124553995901903763": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "3740560748622813469": {
            "samples": [0.22613065326633167] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3926794307898736900": {
            "samples": [0.22613065326633167] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7769226714064152368": {
            "samples": [0.22613065326633167] * 47 + [0.0],
            "type": "arbitrary",
        },
        "9195264624848293063": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "6870706542761456610": {
            "samples": [0.22613065326633167] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7053719760858091690": {
            "samples": [0.22613065326633167] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3725669256329909557": {
            "samples": [0.22613065326633167] * 51 + [0.0],
            "type": "arbitrary",
        },
        "2577847439153040784": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-4634466013656209579": {
            "samples": [0.22613065326633167] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3571063275570782200": {
            "samples": [0.22613065326633167] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "598743803370554767": {
            "samples": [0.22613065326633167] * 55 + [0.0],
            "type": "arbitrary",
        },
        "8804273092597546546": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2796503491373721630": {
            "samples": [0.22613065326633167] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7444711293108838207": {
            "samples": [0.22613065326633167] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5382041402749997279": {
            "samples": [0.22613065326633167] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-1368681648996665069": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8043103753696151061": {
            "samples": [0.22613065326633167] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "829078039006501794": {
            "samples": [0.22613065326633167] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "207752271119808250": {
            "samples": [0.22613065326633167] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-7986098834691917348": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-7764604775493202100": {
            "samples": [0.22613065326633167] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-390640189467504604": {
            "samples": [0.22613065326633167] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5566845087490035237": {
            "samples": [0.22613065326633167] * 67 + [0.0],
            "type": "arbitrary",
        },
        "814186546713597882": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-333635270463270891": {
            "samples": [0.22613065326633167] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7040329315562426605": {
            "samples": [0.22613065326633167] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1864124417539895972": {
            "samples": [0.22613065326633167] * 71 + [0.0],
            "type": "arbitrary",
        },
        "2085618476738611220": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-5581736579782939149": {
            "samples": [0.22613065326633167] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4283378164741778083": {
            "samples": [0.22613065326633167] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6401623099568967251": {
            "samples": [0.22613065326633167] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-8930156091941009187": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8708662032742293939": {
            "samples": [0.22613065326633167] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5889576576852433532": {
            "samples": [0.22613065326633167] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6510902344739127076": {
            "samples": [0.22613065326633167] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-1323019263301330262": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8323721816347219555": {
            "samples": [0.22613065326633167] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7109294805326439930": {
            "samples": [0.22613065326633167] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1762886987376212925": {
            "samples": [0.22613065326633167] * 83 + [0.0],
            "type": "arbitrary",
        },
        "-8478327797106346912": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-7052289886322206217": {
            "samples": [0.22613065326633167] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "321674699703491279": {
            "samples": [0.22613065326633167] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8527203988930483058": {
            "samples": [0.22613065326633167] * 87 + [0.0],
            "type": "arbitrary",
        },
        "-4633036139120324106": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-825864232877700455": {
            "samples": [0.22613065326633167] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4185851524950348643": {
            "samples": [0.22613065326633167] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1645750752663728557": {
            "samples": [0.22613065326633167] * 91 + [0.0],
            "type": "arbitrary",
        },
        "-2267076520550422101": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "6605105272152230754": {
            "samples": [0.22613065326633167] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6826599331350946002": {
            "samples": [0.22613065326633167] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5785218752366202652": {
            "samples": [0.22613065326633167] * 95 + [0.0],
            "type": "arbitrary",
        },
        "-8041673879160265588": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "830507913542387267": {
            "samples": [0.22613065326633167] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4189175237328674405": {
            "samples": [0.22613065326633167] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4290202317134928903": {
            "samples": [0.22613065326633167] * 99 + [0.0],
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
                "7841448908339740536": "7841448908339740536",
                "3249761660744269378": "3249761660744269378",
                "-1558129014401389839": "-1558129014401389839",
                "8805674192738044855": "8805674192738044855",
                "-8930177834034745731": "-8930177834034745731",
                "-6111092378144885324": "-6111092378144885324",
                "-6732418146031578868": "-6732418146031578868",
                "-2210100375941575552": "-2210100375941575552",
                "-1988606316742860304": "-1988606316742860304",
                "8292094237830423481": "8292094237830423481",
                "5939728569068129261": "5939728569068129261",
                "920045418197067589": "920045418197067589",
                "5442363188287070905": "5442363188287070905",
                "8358982316270011372": "8358982316270011372",
                "-5076045999611491146": "-5076045999611491146",
                "-4854551940412775898": "-4854551940412775898",
                "5827303404682145289": "5827303404682145289",
                "-2656792252409609035": "-2656792252409609035",
                "-2435298193210893787": "-2435298193210893787",
                "2576417564617155311": "2576417564617155311",
                "2797911623815870559": "2797911623815870559",
                "-568619721814391742": "-568619721814391742",
                "4995671311819037422": "4995671311819037422",
                "8802843218061661073": "8802843218061661073",
                "3182851840210944943": "3182851840210944943",
                "-12333655636758069": "-12333655636758069",
                "5380611528214111806": "5380611528214111806",
                "3028245859451817586": "3028245859451817586",
                "4454283770235958281": "4454283770235958281",
                "6929237861655127358": "6929237861655127358",
                "5447499606653699697": "5447499606653699697",
                "-5413668981266793353": "-5413668981266793353",
                "-7766034650029087573": "-7766034650029087573",
                "-4086536707024493049": "-4086536707024493049",
                "-5568274962025920710": "-5568274962025920710",
                "-4142237051241780015": "-4142237051241780015",
                "-335065144999156364": "-335065144999156364",
                "-113571085800441116": "-113571085800441116",
                "1862694543004010499": "1862694543004010499",
                "2084188602202725747": "2084188602202725747",
                "-6109662503608999851": "-6109662503608999851",
                "-6730988271495693395": "-6730988271495693395",
                "-3911902815605832988": "-3911902815605832988",
                "-8931585966476894660": "-8931585966476894660",
                "-4311734524293811284": "-4311734524293811284",
                "1542801060619646606": "1542801060619646606",
                "-6124553995901903763": "-6124553995901903763",
                "3740560748622813469": "3740560748622813469",
                "-3926794307898736900": "-3926794307898736900",
                "7769226714064152368": "7769226714064152368",
                "9195264624848293063": "9195264624848293063",
                "6870706542761456610": "6870706542761456610",
                "-7053719760858091690": "-7053719760858091690",
                "3725669256329909557": "3725669256329909557",
                "2577847439153040784": "2577847439153040784",
                "-4634466013656209579": "-4634466013656209579",
                "3571063275570782200": "3571063275570782200",
                "598743803370554767": "598743803370554767",
                "8804273092597546546": "8804273092597546546",
                "2796503491373721630": "2796503491373721630",
                "-7444711293108838207": "-7444711293108838207",
                "5382041402749997279": "5382041402749997279",
                "-1368681648996665069": "-1368681648996665069",
                "-8043103753696151061": "-8043103753696151061",
                "829078039006501794": "829078039006501794",
                "207752271119808250": "207752271119808250",
                "-7986098834691917348": "-7986098834691917348",
                "-7764604775493202100": "-7764604775493202100",
                "-390640189467504604": "-390640189467504604",
                "-5566845087490035237": "-5566845087490035237",
                "814186546713597882": "814186546713597882",
                "-333635270463270891": "-333635270463270891",
                "7040329315562426605": "7040329315562426605",
                "1864124417539895972": "1864124417539895972",
                "2085618476738611220": "2085618476738611220",
                "-5581736579782939149": "-5581736579782939149",
                "4283378164741778083": "4283378164741778083",
                "-6401623099568967251": "-6401623099568967251",
                "-8930156091941009187": "-8930156091941009187",
                "-8708662032742293939": "-8708662032742293939",
                "-5889576576852433532": "-5889576576852433532",
                "-6510902344739127076": "-6510902344739127076",
                "-1323019263301330262": "-1323019263301330262",
                "-8323721816347219555": "-8323721816347219555",
                "-7109294805326439930": "-7109294805326439930",
                "1762886987376212925": "1762886987376212925",
                "-8478327797106346912": "-8478327797106346912",
                "-7052289886322206217": "-7052289886322206217",
                "321674699703491279": "321674699703491279",
                "8527203988930483058": "8527203988930483058",
                "-4633036139120324106": "-4633036139120324106",
                "-825864232877700455": "-825864232877700455",
                "4185851524950348643": "4185851524950348643",
                "-1645750752663728557": "-1645750752663728557",
                "-2267076520550422101": "-2267076520550422101",
                "6605105272152230754": "6605105272152230754",
                "6826599331350946002": "6826599331350946002",
                "5785218752366202652": "5785218752366202652",
                "-8041673879160265588": "-8041673879160265588",
                "830507913542387267": "830507913542387267",
                "-4189175237328674405": "-4189175237328674405",
                "-4290202317134928903": "-4290202317134928903",
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
                "-5633416670789954898": "-5633416670789954898_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_868",
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
                "5560492648399597716": "5560492648399597716",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_5ea",
                "lo_frequency": 6700000000.0,
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
                "-7158952584179743687": "-7158952584179743687",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_19e",
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
                "-5841315490334268105": "-5841315490334268105_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_fbd",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-7158952584179743687": {
            "length": 40,
            "waveforms": {
                "I": "-7158952584179743687_i",
                "Q": "-7158952584179743687_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5560492648399597716": {
            "length": 40,
            "waveforms": {
                "I": "5560492648399597716_i",
                "Q": "5560492648399597716_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7841448908339740536": {
            "length": 100,
            "waveforms": {
                "single": "7841448908339740536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5633416670789954898_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8228961484399632925_i",
                "Q": "-8228961484399632925_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-5841315490334268105_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5247407698090181548_i",
                "Q": "-5247407698090181548_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "3249761660744269378": {
            "length": 100,
            "waveforms": {
                "single": "3249761660744269378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1558129014401389839": {
            "length": 16,
            "waveforms": {
                "single": "-1558129014401389839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8805674192738044855": {
            "length": 16,
            "waveforms": {
                "single": "8805674192738044855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8930177834034745731": {
            "length": 16,
            "waveforms": {
                "single": "-8930177834034745731",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6111092378144885324": {
            "length": 16,
            "waveforms": {
                "single": "-6111092378144885324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6732418146031578868": {
            "length": 16,
            "waveforms": {
                "single": "-6732418146031578868",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2210100375941575552": {
            "length": 16,
            "waveforms": {
                "single": "-2210100375941575552",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1988606316742860304": {
            "length": 16,
            "waveforms": {
                "single": "-1988606316742860304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8292094237830423481": {
            "length": 16,
            "waveforms": {
                "single": "8292094237830423481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5939728569068129261": {
            "length": 16,
            "waveforms": {
                "single": "5939728569068129261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "920045418197067589": {
            "length": 16,
            "waveforms": {
                "single": "920045418197067589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5442363188287070905": {
            "length": 16,
            "waveforms": {
                "single": "5442363188287070905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8358982316270011372": {
            "length": 16,
            "waveforms": {
                "single": "8358982316270011372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5076045999611491146": {
            "length": 16,
            "waveforms": {
                "single": "-5076045999611491146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4854551940412775898": {
            "length": 16,
            "waveforms": {
                "single": "-4854551940412775898",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5827303404682145289": {
            "length": 16,
            "waveforms": {
                "single": "5827303404682145289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2656792252409609035": {
            "length": 16,
            "waveforms": {
                "single": "-2656792252409609035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2435298193210893787": {
            "length": 16,
            "waveforms": {
                "single": "-2435298193210893787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2576417564617155311": {
            "length": 20,
            "waveforms": {
                "single": "2576417564617155311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2797911623815870559": {
            "length": 20,
            "waveforms": {
                "single": "2797911623815870559",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-568619721814391742": {
            "length": 20,
            "waveforms": {
                "single": "-568619721814391742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4995671311819037422": {
            "length": 20,
            "waveforms": {
                "single": "4995671311819037422",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8802843218061661073": {
            "length": 24,
            "waveforms": {
                "single": "8802843218061661073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3182851840210944943": {
            "length": 24,
            "waveforms": {
                "single": "3182851840210944943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-12333655636758069": {
            "length": 24,
            "waveforms": {
                "single": "-12333655636758069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5380611528214111806": {
            "length": 24,
            "waveforms": {
                "single": "5380611528214111806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3028245859451817586": {
            "length": 28,
            "waveforms": {
                "single": "3028245859451817586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4454283770235958281": {
            "length": 28,
            "waveforms": {
                "single": "4454283770235958281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6929237861655127358": {
            "length": 28,
            "waveforms": {
                "single": "6929237861655127358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5447499606653699697": {
            "length": 28,
            "waveforms": {
                "single": "5447499606653699697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5413668981266793353": {
            "length": 32,
            "waveforms": {
                "single": "-5413668981266793353",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7766034650029087573": {
            "length": 32,
            "waveforms": {
                "single": "-7766034650029087573",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4086536707024493049": {
            "length": 32,
            "waveforms": {
                "single": "-4086536707024493049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5568274962025920710": {
            "length": 32,
            "waveforms": {
                "single": "-5568274962025920710",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4142237051241780015": {
            "length": 36,
            "waveforms": {
                "single": "-4142237051241780015",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-335065144999156364": {
            "length": 36,
            "waveforms": {
                "single": "-335065144999156364",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-113571085800441116": {
            "length": 36,
            "waveforms": {
                "single": "-113571085800441116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1862694543004010499": {
            "length": 36,
            "waveforms": {
                "single": "1862694543004010499",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2084188602202725747": {
            "length": 40,
            "waveforms": {
                "single": "2084188602202725747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6109662503608999851": {
            "length": 40,
            "waveforms": {
                "single": "-6109662503608999851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6730988271495693395": {
            "length": 40,
            "waveforms": {
                "single": "-6730988271495693395",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3911902815605832988": {
            "length": 40,
            "waveforms": {
                "single": "-3911902815605832988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8931585966476894660": {
            "length": 44,
            "waveforms": {
                "single": "-8931585966476894660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4311734524293811284": {
            "length": 44,
            "waveforms": {
                "single": "-4311734524293811284",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1542801060619646606": {
            "length": 44,
            "waveforms": {
                "single": "1542801060619646606",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6124553995901903763": {
            "length": 44,
            "waveforms": {
                "single": "-6124553995901903763",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3740560748622813469": {
            "length": 48,
            "waveforms": {
                "single": "3740560748622813469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3926794307898736900": {
            "length": 48,
            "waveforms": {
                "single": "-3926794307898736900",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7769226714064152368": {
            "length": 48,
            "waveforms": {
                "single": "7769226714064152368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9195264624848293063": {
            "length": 48,
            "waveforms": {
                "single": "9195264624848293063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6870706542761456610": {
            "length": 52,
            "waveforms": {
                "single": "6870706542761456610",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7053719760858091690": {
            "length": 52,
            "waveforms": {
                "single": "-7053719760858091690",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3725669256329909557": {
            "length": 52,
            "waveforms": {
                "single": "3725669256329909557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2577847439153040784": {
            "length": 52,
            "waveforms": {
                "single": "2577847439153040784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4634466013656209579": {
            "length": 56,
            "waveforms": {
                "single": "-4634466013656209579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3571063275570782200": {
            "length": 56,
            "waveforms": {
                "single": "3571063275570782200",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "598743803370554767": {
            "length": 56,
            "waveforms": {
                "single": "598743803370554767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8804273092597546546": {
            "length": 56,
            "waveforms": {
                "single": "8804273092597546546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2796503491373721630": {
            "length": 60,
            "waveforms": {
                "single": "2796503491373721630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7444711293108838207": {
            "length": 60,
            "waveforms": {
                "single": "-7444711293108838207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5382041402749997279": {
            "length": 60,
            "waveforms": {
                "single": "5382041402749997279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1368681648996665069": {
            "length": 60,
            "waveforms": {
                "single": "-1368681648996665069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8043103753696151061": {
            "length": 64,
            "waveforms": {
                "single": "-8043103753696151061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "829078039006501794": {
            "length": 64,
            "waveforms": {
                "single": "829078039006501794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "207752271119808250": {
            "length": 64,
            "waveforms": {
                "single": "207752271119808250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7986098834691917348": {
            "length": 64,
            "waveforms": {
                "single": "-7986098834691917348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7764604775493202100": {
            "length": 68,
            "waveforms": {
                "single": "-7764604775493202100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-390640189467504604": {
            "length": 68,
            "waveforms": {
                "single": "-390640189467504604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5566845087490035237": {
            "length": 68,
            "waveforms": {
                "single": "-5566845087490035237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "814186546713597882": {
            "length": 68,
            "waveforms": {
                "single": "814186546713597882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-333635270463270891": {
            "length": 72,
            "waveforms": {
                "single": "-333635270463270891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7040329315562426605": {
            "length": 72,
            "waveforms": {
                "single": "7040329315562426605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1864124417539895972": {
            "length": 72,
            "waveforms": {
                "single": "1864124417539895972",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2085618476738611220": {
            "length": 72,
            "waveforms": {
                "single": "2085618476738611220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5581736579782939149": {
            "length": 76,
            "waveforms": {
                "single": "-5581736579782939149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4283378164741778083": {
            "length": 76,
            "waveforms": {
                "single": "4283378164741778083",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6401623099568967251": {
            "length": 76,
            "waveforms": {
                "single": "-6401623099568967251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8930156091941009187": {
            "length": 76,
            "waveforms": {
                "single": "-8930156091941009187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8708662032742293939": {
            "length": 80,
            "waveforms": {
                "single": "-8708662032742293939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5889576576852433532": {
            "length": 80,
            "waveforms": {
                "single": "-5889576576852433532",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6510902344739127076": {
            "length": 80,
            "waveforms": {
                "single": "-6510902344739127076",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1323019263301330262": {
            "length": 80,
            "waveforms": {
                "single": "-1323019263301330262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8323721816347219555": {
            "length": 84,
            "waveforms": {
                "single": "-8323721816347219555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7109294805326439930": {
            "length": 84,
            "waveforms": {
                "single": "-7109294805326439930",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1762886987376212925": {
            "length": 84,
            "waveforms": {
                "single": "1762886987376212925",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8478327797106346912": {
            "length": 84,
            "waveforms": {
                "single": "-8478327797106346912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7052289886322206217": {
            "length": 88,
            "waveforms": {
                "single": "-7052289886322206217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "321674699703491279": {
            "length": 88,
            "waveforms": {
                "single": "321674699703491279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8527203988930483058": {
            "length": 88,
            "waveforms": {
                "single": "8527203988930483058",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4633036139120324106": {
            "length": 88,
            "waveforms": {
                "single": "-4633036139120324106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-825864232877700455": {
            "length": 92,
            "waveforms": {
                "single": "-825864232877700455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4185851524950348643": {
            "length": 92,
            "waveforms": {
                "single": "4185851524950348643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1645750752663728557": {
            "length": 92,
            "waveforms": {
                "single": "-1645750752663728557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2267076520550422101": {
            "length": 92,
            "waveforms": {
                "single": "-2267076520550422101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6605105272152230754": {
            "length": 96,
            "waveforms": {
                "single": "6605105272152230754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6826599331350946002": {
            "length": 96,
            "waveforms": {
                "single": "6826599331350946002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5785218752366202652": {
            "length": 96,
            "waveforms": {
                "single": "5785218752366202652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8041673879160265588": {
            "length": 96,
            "waveforms": {
                "single": "-8041673879160265588",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "830507913542387267": {
            "length": 100,
            "waveforms": {
                "single": "830507913542387267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4189175237328674405": {
            "length": 100,
            "waveforms": {
                "single": "-4189175237328674405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4290202317134928903": {
            "length": 100,
            "waveforms": {
                "single": "-4290202317134928903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7158952584179743687_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7158952584179743687_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5560492648399597716_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5560492648399597716_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7841448908339740536": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-8228961484399632925_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-8228961484399632925_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5247407698090181548_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-5247407698090181548_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3249761660744269378": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-1558129014401389839": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8805674192738044855": {
            "samples": [0.22613065326633167] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8930177834034745731": {
            "samples": [0.22613065326633167] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6111092378144885324": {
            "samples": [0.22613065326633167] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6732418146031578868": {
            "samples": [0.22613065326633167] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2210100375941575552": {
            "samples": [0.22613065326633167] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1988606316742860304": {
            "samples": [0.22613065326633167] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8292094237830423481": {
            "samples": [0.22613065326633167] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5939728569068129261": {
            "samples": [0.22613065326633167] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "920045418197067589": {
            "samples": [0.22613065326633167] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5442363188287070905": {
            "samples": [0.22613065326633167] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8358982316270011372": {
            "samples": [0.22613065326633167] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5076045999611491146": {
            "samples": [0.22613065326633167] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4854551940412775898": {
            "samples": [0.22613065326633167] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5827303404682145289": {
            "samples": [0.22613065326633167] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2656792252409609035": {
            "samples": [0.22613065326633167] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2435298193210893787": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2576417564617155311": {
            "samples": [0.22613065326633167] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2797911623815870559": {
            "samples": [0.22613065326633167] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-568619721814391742": {
            "samples": [0.22613065326633167] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4995671311819037422": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "8802843218061661073": {
            "samples": [0.22613065326633167] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3182851840210944943": {
            "samples": [0.22613065326633167] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-12333655636758069": {
            "samples": [0.22613065326633167] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5380611528214111806": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "3028245859451817586": {
            "samples": [0.22613065326633167] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4454283770235958281": {
            "samples": [0.22613065326633167] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6929237861655127358": {
            "samples": [0.22613065326633167] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5447499606653699697": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-5413668981266793353": {
            "samples": [0.22613065326633167] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7766034650029087573": {
            "samples": [0.22613065326633167] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4086536707024493049": {
            "samples": [0.22613065326633167] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5568274962025920710": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-4142237051241780015": {
            "samples": [0.22613065326633167] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-335065144999156364": {
            "samples": [0.22613065326633167] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-113571085800441116": {
            "samples": [0.22613065326633167] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1862694543004010499": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2084188602202725747": {
            "samples": [0.22613065326633167] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6109662503608999851": {
            "samples": [0.22613065326633167] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6730988271495693395": {
            "samples": [0.22613065326633167] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3911902815605832988": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8931585966476894660": {
            "samples": [0.22613065326633167] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4311734524293811284": {
            "samples": [0.22613065326633167] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1542801060619646606": {
            "samples": [0.22613065326633167] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6124553995901903763": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "3740560748622813469": {
            "samples": [0.22613065326633167] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3926794307898736900": {
            "samples": [0.22613065326633167] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7769226714064152368": {
            "samples": [0.22613065326633167] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9195264624848293063": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "6870706542761456610": {
            "samples": [0.22613065326633167] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7053719760858091690": {
            "samples": [0.22613065326633167] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3725669256329909557": {
            "samples": [0.22613065326633167] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2577847439153040784": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-4634466013656209579": {
            "samples": [0.22613065326633167] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3571063275570782200": {
            "samples": [0.22613065326633167] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "598743803370554767": {
            "samples": [0.22613065326633167] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8804273092597546546": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "2796503491373721630": {
            "samples": [0.22613065326633167] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7444711293108838207": {
            "samples": [0.22613065326633167] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5382041402749997279": {
            "samples": [0.22613065326633167] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1368681648996665069": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8043103753696151061": {
            "samples": [0.22613065326633167] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "829078039006501794": {
            "samples": [0.22613065326633167] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "207752271119808250": {
            "samples": [0.22613065326633167] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7986098834691917348": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-7764604775493202100": {
            "samples": [0.22613065326633167] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-390640189467504604": {
            "samples": [0.22613065326633167] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5566845087490035237": {
            "samples": [0.22613065326633167] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "814186546713597882": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-333635270463270891": {
            "samples": [0.22613065326633167] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7040329315562426605": {
            "samples": [0.22613065326633167] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1864124417539895972": {
            "samples": [0.22613065326633167] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2085618476738611220": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-5581736579782939149": {
            "samples": [0.22613065326633167] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4283378164741778083": {
            "samples": [0.22613065326633167] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6401623099568967251": {
            "samples": [0.22613065326633167] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8930156091941009187": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8708662032742293939": {
            "samples": [0.22613065326633167] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5889576576852433532": {
            "samples": [0.22613065326633167] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6510902344739127076": {
            "samples": [0.22613065326633167] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1323019263301330262": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-8323721816347219555": {
            "samples": [0.22613065326633167] * 81 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7109294805326439930": {
            "samples": [0.22613065326633167] * 82 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1762886987376212925": {
            "samples": [0.22613065326633167] * 83 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8478327797106346912": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-7052289886322206217": {
            "samples": [0.22613065326633167] * 85 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "321674699703491279": {
            "samples": [0.22613065326633167] * 86 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8527203988930483058": {
            "samples": [0.22613065326633167] * 87 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4633036139120324106": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "-825864232877700455": {
            "samples": [0.22613065326633167] * 89 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4185851524950348643": {
            "samples": [0.22613065326633167] * 90 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1645750752663728557": {
            "samples": [0.22613065326633167] * 91 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2267076520550422101": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "6605105272152230754": {
            "samples": [0.22613065326633167] * 93 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6826599331350946002": {
            "samples": [0.22613065326633167] * 94 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5785218752366202652": {
            "samples": [0.22613065326633167] * 95 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8041673879160265588": {
            "sample": 0.22613065326633167,
            "type": "constant",
        },
        "830507913542387267": {
            "samples": [0.22613065326633167] * 97 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4189175237328674405": {
            "samples": [0.22613065326633167] * 98 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4290202317134928903": {
            "samples": [0.22613065326633167] * 99 + [0.0],
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
        "B2/acquisition_mixer_868": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_5ea": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_19e": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_fbd": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

