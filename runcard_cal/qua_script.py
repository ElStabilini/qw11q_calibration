
# Single QUA script generated at 2025-02-14 09:50:04.647068
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
        with for_(v8,0,(v8<=119),(v8+1)):
            with for_(v9,-1.99,(v9<-1.7503877551020408),(v9+0.00812244897959169)):
                align()
                play("8184241719077206361", "B2/drive")
                play("-196862618431489046", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("6852654029804875484"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("6575459626388873270"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-3665755158093686567"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("7902591900631173574"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-4163120538874744923"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-1246501410891804456"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-1965360850871578060"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("3986708406134959890"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("8509026176224963206"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("6184468094138126753"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-7739958209481421547"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-8361283977368115091"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-6807572103345945269"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-2285254333255941953"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-4609812415342778406"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-87494645252775090"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-7754849701774325459"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("5145715171773989256"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("8062334299756929723"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("468791420924858583"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("7564968918975871367"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-2676245865506688470"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-2953440268922690684"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-2731946209723975436"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("947551733280619088"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-5803171318466043260"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("3272985384521815078"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("4699023295305955773"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-5542191489176604064"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("1553986008874408720"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("4544417314546828416"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-7521295124959090081"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-2998977354869086765"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("2110272075052042393"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("6632589845142045709"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-6249863194934076743"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("8830349533145212572"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("9051843592343927820"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-8684008434428862766"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-5864922978539002359"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-5643428919340287111"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("-1963930976335692587"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-1742436917136977339"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-4593491048513989021"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("1787540585689644098"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("6407392027872727474"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("5688532587892953870"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("4206794332891526209"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-3987056772920199389"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-4608382540806892933"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-801210634564269282"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-6808980235788094198"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-9161345904550388418"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("3665406791308447068"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-6575807993174112769"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("5863166479311613931"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-8776405688155314034"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("2889475042662626167"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-4875413685952004262"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("1076655571054533688"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("-4931114030169291228"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("3274415259057700551"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("7796733029147703867"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("2777049878276642195"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("5693669006259582662"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("147489806098345761"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("-7519865250423204608"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("-2997547480333201292"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("-5322105562420037745"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("532430022493420145"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("-88895745393273399"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("132598313805441849"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("2951683769695302256"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("2330358001808608712"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("-5863493104003116886"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("517538530200516233"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-7966557126891238091"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-3444239356801234775"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("362932549441388876"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("1788970460225529571"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("-5423342992583720792"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("3986730148228696434"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("4208224207427411682"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("8015396113670035333"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("-5909030189949512967"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("-8233588272036349420"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("-6807550361252208725"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("-3000378455009585074"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("1521939315080418242"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("-6962156342011336082"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("-581124707807702963"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("-8774975813619428561"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("9050442492203429511"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("-6577216125616261698"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("-6355722066417546450"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("-6977047834304239994"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("-1122512249390782104"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("8840136167227015188"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("1075247438612384759"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("1296741497811100007"*amp(v9), "B4/flux")
                with elif_((v8==100)):
                    play("6308457255639149105"*amp(v9), "B4/flux")
                with elif_((v8==101)):
                    play("3494501185814266870"*amp(v9), "B4/flux")
                with elif_((v8==102)):
                    play("-9000173630888746796"*amp(v9), "B4/flux")
                with elif_((v8==103)):
                    play("8727711002841031216"*amp(v9), "B4/flux")
                with elif_((v8==104)):
                    play("-1513503781641528621"*amp(v9), "B4/flux")
                with elif_((v8==105)):
                    play("-87465870857387926"*amp(v9), "B4/flux")
                with elif_((v8==106)):
                    play("-1569204125858815587"*amp(v9), "B4/flux")
                with elif_((v8==107)):
                    play("2953113644231187729"*amp(v9), "B4/flux")
                with elif_((v8==108)):
                    play("2331787876344494185"*amp(v9), "B4/flux")
                with elif_((v8==109)):
                    play("6138959782587117836"*amp(v9), "B4/flux")
                with elif_((v8==110)):
                    play("131190181363292920"*amp(v9), "B4/flux")
                with elif_((v8==111)):
                    play("-2221175487399001300"*amp(v9), "B4/flux")
                with elif_((v8==112)):
                    play("-7841166865249717430"*amp(v9), "B4/flux")
                with elif_((v8==113)):
                    play("364362423977274349"*amp(v9), "B4/flux")
                with elif_((v8==114)):
                    play("-5643407177246550567"*amp(v9), "B4/flux")
                with elif_((v8==115)):
                    play("-1836235271003926916"*amp(v9), "B4/flux")
                with elif_((v8==116)):
                    play("-1614741211805211668"*amp(v9), "B4/flux")
                with elif_((v8==117)):
                    play("7795331929007205558"*amp(v9), "B4/flux")
                with elif_((v8==118)):
                    play("-5087121111068916894"*amp(v9), "B4/flux")
                with elif_((v8==119)):
                    play("-564803340978913578"*amp(v9), "B4/flux")
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
                play("-196862618431489046", "B4/drive")
                measure("-818727195718244064", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7301161584051474)-(v3*0.6833230533471776))>0.002634776715916271)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-7487101510498968938", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.4852100881460357)-(v6*0.8743976042746894))>-0.0004963015755993342)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(30).buffer(120).average().save("-818727195718244064_B2|acquisition_shots")
        r2.buffer(30).buffer(120).average().save("-7487101510498968938_B4|acquisition_shots")


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
                "2097502163907163756": "2097502163907163756",
                "-8232158397500463947": "-8232158397500463947",
                "6852654029804875484": "6852654029804875484",
                "6575459626388873270": "6575459626388873270",
                "-3665755158093686567": "-3665755158093686567",
                "7902591900631173574": "7902591900631173574",
                "-4163120538874744923": "-4163120538874744923",
                "-1246501410891804456": "-1246501410891804456",
                "-1965360850871578060": "-1965360850871578060",
                "3986708406134959890": "3986708406134959890",
                "8509026176224963206": "8509026176224963206",
                "6184468094138126753": "6184468094138126753",
                "-7739958209481421547": "-7739958209481421547",
                "-8361283977368115091": "-8361283977368115091",
                "-6807572103345945269": "-6807572103345945269",
                "-2285254333255941953": "-2285254333255941953",
                "-4609812415342778406": "-4609812415342778406",
                "-87494645252775090": "-87494645252775090",
                "-7754849701774325459": "-7754849701774325459",
                "5145715171773989256": "5145715171773989256",
                "8062334299756929723": "8062334299756929723",
                "468791420924858583": "468791420924858583",
                "7564968918975871367": "7564968918975871367",
                "-2676245865506688470": "-2676245865506688470",
                "-2953440268922690684": "-2953440268922690684",
                "-2731946209723975436": "-2731946209723975436",
                "947551733280619088": "947551733280619088",
                "-5803171318466043260": "-5803171318466043260",
                "3272985384521815078": "3272985384521815078",
                "4699023295305955773": "4699023295305955773",
                "-5542191489176604064": "-5542191489176604064",
                "1553986008874408720": "1553986008874408720",
                "4544417314546828416": "4544417314546828416",
                "-7521295124959090081": "-7521295124959090081",
                "-2998977354869086765": "-2998977354869086765",
                "2110272075052042393": "2110272075052042393",
                "6632589845142045709": "6632589845142045709",
                "-6249863194934076743": "-6249863194934076743",
                "8830349533145212572": "8830349533145212572",
                "9051843592343927820": "9051843592343927820",
                "-8684008434428862766": "-8684008434428862766",
                "-5864922978539002359": "-5864922978539002359",
                "-5643428919340287111": "-5643428919340287111",
                "-1963930976335692587": "-1963930976335692587",
                "-1742436917136977339": "-1742436917136977339",
                "-4593491048513989021": "-4593491048513989021",
                "1787540585689644098": "1787540585689644098",
                "6407392027872727474": "6407392027872727474",
                "5688532587892953870": "5688532587892953870",
                "4206794332891526209": "4206794332891526209",
                "-3987056772920199389": "-3987056772920199389",
                "-4608382540806892933": "-4608382540806892933",
                "-801210634564269282": "-801210634564269282",
                "-6808980235788094198": "-6808980235788094198",
                "-9161345904550388418": "-9161345904550388418",
                "3665406791308447068": "3665406791308447068",
                "-6575807993174112769": "-6575807993174112769",
                "5863166479311613931": "5863166479311613931",
                "-8776405688155314034": "-8776405688155314034",
                "2889475042662626167": "2889475042662626167",
                "-4875413685952004262": "-4875413685952004262",
                "1076655571054533688": "1076655571054533688",
                "-4931114030169291228": "-4931114030169291228",
                "3274415259057700551": "3274415259057700551",
                "7796733029147703867": "7796733029147703867",
                "2777049878276642195": "2777049878276642195",
                "5693669006259582662": "5693669006259582662",
                "147489806098345761": "147489806098345761",
                "-7519865250423204608": "-7519865250423204608",
                "-2997547480333201292": "-2997547480333201292",
                "-5322105562420037745": "-5322105562420037745",
                "532430022493420145": "532430022493420145",
                "-88895745393273399": "-88895745393273399",
                "132598313805441849": "132598313805441849",
                "2951683769695302256": "2951683769695302256",
                "2330358001808608712": "2330358001808608712",
                "-5863493104003116886": "-5863493104003116886",
                "517538530200516233": "517538530200516233",
                "-7966557126891238091": "-7966557126891238091",
                "-3444239356801234775": "-3444239356801234775",
                "362932549441388876": "362932549441388876",
                "1788970460225529571": "1788970460225529571",
                "-5423342992583720792": "-5423342992583720792",
                "3986730148228696434": "3986730148228696434",
                "4208224207427411682": "4208224207427411682",
                "8015396113670035333": "8015396113670035333",
                "-5909030189949512967": "-5909030189949512967",
                "-8233588272036349420": "-8233588272036349420",
                "-6807550361252208725": "-6807550361252208725",
                "-3000378455009585074": "-3000378455009585074",
                "1521939315080418242": "1521939315080418242",
                "-6962156342011336082": "-6962156342011336082",
                "-581124707807702963": "-581124707807702963",
                "-8774975813619428561": "-8774975813619428561",
                "9050442492203429511": "9050442492203429511",
                "-6577216125616261698": "-6577216125616261698",
                "-6355722066417546450": "-6355722066417546450",
                "-6977047834304239994": "-6977047834304239994",
                "-1122512249390782104": "-1122512249390782104",
                "8840136167227015188": "8840136167227015188",
                "1075247438612384759": "1075247438612384759",
                "1296741497811100007": "1296741497811100007",
                "6308457255639149105": "6308457255639149105",
                "3494501185814266870": "3494501185814266870",
                "-9000173630888746796": "-9000173630888746796",
                "8727711002841031216": "8727711002841031216",
                "-1513503781641528621": "-1513503781641528621",
                "-87465870857387926": "-87465870857387926",
                "-1569204125858815587": "-1569204125858815587",
                "2953113644231187729": "2953113644231187729",
                "2331787876344494185": "2331787876344494185",
                "6138959782587117836": "6138959782587117836",
                "131190181363292920": "131190181363292920",
                "-2221175487399001300": "-2221175487399001300",
                "-7841166865249717430": "-7841166865249717430",
                "364362423977274349": "364362423977274349",
                "-5643407177246550567": "-5643407177246550567",
                "-1836235271003926916": "-1836235271003926916",
                "-1614741211805211668": "-1614741211805211668",
                "7795331929007205558": "7795331929007205558",
                "-5087121111068916894": "-5087121111068916894",
                "-564803340978913578": "-564803340978913578",
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
                "-7487101510498968938": "-7487101510498968938_B4/acquisition",
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
                "-818727195718244064": "-818727195718244064_B2/acquisition",
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
                "-196862618431489046": "-196862618431489046",
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
                "8184241719077206361": "8184241719077206361",
            },
        },
    },
    "pulses": {
        "8184241719077206361": {
            "length": 40,
            "waveforms": {
                "I": "8184241719077206361_i",
                "Q": "8184241719077206361_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-196862618431489046": {
            "length": 40,
            "waveforms": {
                "I": "-196862618431489046_i",
                "Q": "-196862618431489046_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2097502163907163756": {
            "length": 120,
            "waveforms": {
                "single": "2097502163907163756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-818727195718244064_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5808884634377180267_i",
                "Q": "5808884634377180267_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-7487101510498968938_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7947618593601222852_i",
                "Q": "7947618593601222852_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-8232158397500463947": {
            "length": 120,
            "waveforms": {
                "single": "-8232158397500463947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6852654029804875484": {
            "length": 16,
            "waveforms": {
                "single": "6852654029804875484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6575459626388873270": {
            "length": 16,
            "waveforms": {
                "single": "6575459626388873270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3665755158093686567": {
            "length": 16,
            "waveforms": {
                "single": "-3665755158093686567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7902591900631173574": {
            "length": 16,
            "waveforms": {
                "single": "7902591900631173574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4163120538874744923": {
            "length": 16,
            "waveforms": {
                "single": "-4163120538874744923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1246501410891804456": {
            "length": 16,
            "waveforms": {
                "single": "-1246501410891804456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1965360850871578060": {
            "length": 16,
            "waveforms": {
                "single": "-1965360850871578060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3986708406134959890": {
            "length": 16,
            "waveforms": {
                "single": "3986708406134959890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8509026176224963206": {
            "length": 16,
            "waveforms": {
                "single": "8509026176224963206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6184468094138126753": {
            "length": 16,
            "waveforms": {
                "single": "6184468094138126753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7739958209481421547": {
            "length": 16,
            "waveforms": {
                "single": "-7739958209481421547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8361283977368115091": {
            "length": 16,
            "waveforms": {
                "single": "-8361283977368115091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6807572103345945269": {
            "length": 16,
            "waveforms": {
                "single": "-6807572103345945269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2285254333255941953": {
            "length": 16,
            "waveforms": {
                "single": "-2285254333255941953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4609812415342778406": {
            "length": 16,
            "waveforms": {
                "single": "-4609812415342778406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-87494645252775090": {
            "length": 16,
            "waveforms": {
                "single": "-87494645252775090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7754849701774325459": {
            "length": 16,
            "waveforms": {
                "single": "-7754849701774325459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5145715171773989256": {
            "length": 20,
            "waveforms": {
                "single": "5145715171773989256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8062334299756929723": {
            "length": 20,
            "waveforms": {
                "single": "8062334299756929723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "468791420924858583": {
            "length": 20,
            "waveforms": {
                "single": "468791420924858583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7564968918975871367": {
            "length": 20,
            "waveforms": {
                "single": "7564968918975871367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2676245865506688470": {
            "length": 24,
            "waveforms": {
                "single": "-2676245865506688470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2953440268922690684": {
            "length": 24,
            "waveforms": {
                "single": "-2953440268922690684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2731946209723975436": {
            "length": 24,
            "waveforms": {
                "single": "-2731946209723975436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "947551733280619088": {
            "length": 24,
            "waveforms": {
                "single": "947551733280619088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5803171318466043260": {
            "length": 28,
            "waveforms": {
                "single": "-5803171318466043260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3272985384521815078": {
            "length": 28,
            "waveforms": {
                "single": "3272985384521815078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4699023295305955773": {
            "length": 28,
            "waveforms": {
                "single": "4699023295305955773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5542191489176604064": {
            "length": 28,
            "waveforms": {
                "single": "-5542191489176604064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1553986008874408720": {
            "length": 32,
            "waveforms": {
                "single": "1553986008874408720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4544417314546828416": {
            "length": 32,
            "waveforms": {
                "single": "4544417314546828416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7521295124959090081": {
            "length": 32,
            "waveforms": {
                "single": "-7521295124959090081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2998977354869086765": {
            "length": 32,
            "waveforms": {
                "single": "-2998977354869086765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2110272075052042393": {
            "length": 36,
            "waveforms": {
                "single": "2110272075052042393",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6632589845142045709": {
            "length": 36,
            "waveforms": {
                "single": "6632589845142045709",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6249863194934076743": {
            "length": 36,
            "waveforms": {
                "single": "-6249863194934076743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8830349533145212572": {
            "length": 36,
            "waveforms": {
                "single": "8830349533145212572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9051843592343927820": {
            "length": 40,
            "waveforms": {
                "single": "9051843592343927820",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8684008434428862766": {
            "length": 40,
            "waveforms": {
                "single": "-8684008434428862766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5864922978539002359": {
            "length": 40,
            "waveforms": {
                "single": "-5864922978539002359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5643428919340287111": {
            "length": 40,
            "waveforms": {
                "single": "-5643428919340287111",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1963930976335692587": {
            "length": 44,
            "waveforms": {
                "single": "-1963930976335692587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1742436917136977339": {
            "length": 44,
            "waveforms": {
                "single": "-1742436917136977339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4593491048513989021": {
            "length": 44,
            "waveforms": {
                "single": "-4593491048513989021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1787540585689644098": {
            "length": 44,
            "waveforms": {
                "single": "1787540585689644098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6407392027872727474": {
            "length": 48,
            "waveforms": {
                "single": "6407392027872727474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5688532587892953870": {
            "length": 48,
            "waveforms": {
                "single": "5688532587892953870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4206794332891526209": {
            "length": 48,
            "waveforms": {
                "single": "4206794332891526209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3987056772920199389": {
            "length": 48,
            "waveforms": {
                "single": "-3987056772920199389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4608382540806892933": {
            "length": 52,
            "waveforms": {
                "single": "-4608382540806892933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-801210634564269282": {
            "length": 52,
            "waveforms": {
                "single": "-801210634564269282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6808980235788094198": {
            "length": 52,
            "waveforms": {
                "single": "-6808980235788094198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9161345904550388418": {
            "length": 52,
            "waveforms": {
                "single": "-9161345904550388418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3665406791308447068": {
            "length": 56,
            "waveforms": {
                "single": "3665406791308447068",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6575807993174112769": {
            "length": 56,
            "waveforms": {
                "single": "-6575807993174112769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5863166479311613931": {
            "length": 56,
            "waveforms": {
                "single": "5863166479311613931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8776405688155314034": {
            "length": 56,
            "waveforms": {
                "single": "-8776405688155314034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2889475042662626167": {
            "length": 60,
            "waveforms": {
                "single": "2889475042662626167",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4875413685952004262": {
            "length": 60,
            "waveforms": {
                "single": "-4875413685952004262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1076655571054533688": {
            "length": 60,
            "waveforms": {
                "single": "1076655571054533688",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4931114030169291228": {
            "length": 60,
            "waveforms": {
                "single": "-4931114030169291228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3274415259057700551": {
            "length": 64,
            "waveforms": {
                "single": "3274415259057700551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7796733029147703867": {
            "length": 64,
            "waveforms": {
                "single": "7796733029147703867",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2777049878276642195": {
            "length": 64,
            "waveforms": {
                "single": "2777049878276642195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5693669006259582662": {
            "length": 64,
            "waveforms": {
                "single": "5693669006259582662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "147489806098345761": {
            "length": 68,
            "waveforms": {
                "single": "147489806098345761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7519865250423204608": {
            "length": 68,
            "waveforms": {
                "single": "-7519865250423204608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2997547480333201292": {
            "length": 68,
            "waveforms": {
                "single": "-2997547480333201292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5322105562420037745": {
            "length": 68,
            "waveforms": {
                "single": "-5322105562420037745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "532430022493420145": {
            "length": 72,
            "waveforms": {
                "single": "532430022493420145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-88895745393273399": {
            "length": 72,
            "waveforms": {
                "single": "-88895745393273399",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "132598313805441849": {
            "length": 72,
            "waveforms": {
                "single": "132598313805441849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2951683769695302256": {
            "length": 72,
            "waveforms": {
                "single": "2951683769695302256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2330358001808608712": {
            "length": 76,
            "waveforms": {
                "single": "2330358001808608712",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5863493104003116886": {
            "length": 76,
            "waveforms": {
                "single": "-5863493104003116886",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "517538530200516233": {
            "length": 76,
            "waveforms": {
                "single": "517538530200516233",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7966557126891238091": {
            "length": 76,
            "waveforms": {
                "single": "-7966557126891238091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3444239356801234775": {
            "length": 80,
            "waveforms": {
                "single": "-3444239356801234775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "362932549441388876": {
            "length": 80,
            "waveforms": {
                "single": "362932549441388876",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1788970460225529571": {
            "length": 80,
            "waveforms": {
                "single": "1788970460225529571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5423342992583720792": {
            "length": 80,
            "waveforms": {
                "single": "-5423342992583720792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3986730148228696434": {
            "length": 84,
            "waveforms": {
                "single": "3986730148228696434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4208224207427411682": {
            "length": 84,
            "waveforms": {
                "single": "4208224207427411682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8015396113670035333": {
            "length": 84,
            "waveforms": {
                "single": "8015396113670035333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5909030189949512967": {
            "length": 84,
            "waveforms": {
                "single": "-5909030189949512967",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8233588272036349420": {
            "length": 88,
            "waveforms": {
                "single": "-8233588272036349420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6807550361252208725": {
            "length": 88,
            "waveforms": {
                "single": "-6807550361252208725",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3000378455009585074": {
            "length": 88,
            "waveforms": {
                "single": "-3000378455009585074",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1521939315080418242": {
            "length": 88,
            "waveforms": {
                "single": "1521939315080418242",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6962156342011336082": {
            "length": 92,
            "waveforms": {
                "single": "-6962156342011336082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-581124707807702963": {
            "length": 92,
            "waveforms": {
                "single": "-581124707807702963",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8774975813619428561": {
            "length": 92,
            "waveforms": {
                "single": "-8774975813619428561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9050442492203429511": {
            "length": 92,
            "waveforms": {
                "single": "9050442492203429511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6577216125616261698": {
            "length": 96,
            "waveforms": {
                "single": "-6577216125616261698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6355722066417546450": {
            "length": 96,
            "waveforms": {
                "single": "-6355722066417546450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6977047834304239994": {
            "length": 96,
            "waveforms": {
                "single": "-6977047834304239994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1122512249390782104": {
            "length": 96,
            "waveforms": {
                "single": "-1122512249390782104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8840136167227015188": {
            "length": 100,
            "waveforms": {
                "single": "8840136167227015188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1075247438612384759": {
            "length": 100,
            "waveforms": {
                "single": "1075247438612384759",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1296741497811100007": {
            "length": 100,
            "waveforms": {
                "single": "1296741497811100007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6308457255639149105": {
            "length": 100,
            "waveforms": {
                "single": "6308457255639149105",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3494501185814266870": {
            "length": 104,
            "waveforms": {
                "single": "3494501185814266870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9000173630888746796": {
            "length": 104,
            "waveforms": {
                "single": "-9000173630888746796",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8727711002841031216": {
            "length": 104,
            "waveforms": {
                "single": "8727711002841031216",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1513503781641528621": {
            "length": 104,
            "waveforms": {
                "single": "-1513503781641528621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-87465870857387926": {
            "length": 108,
            "waveforms": {
                "single": "-87465870857387926",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1569204125858815587": {
            "length": 108,
            "waveforms": {
                "single": "-1569204125858815587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2953113644231187729": {
            "length": 108,
            "waveforms": {
                "single": "2953113644231187729",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2331787876344494185": {
            "length": 108,
            "waveforms": {
                "single": "2331787876344494185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6138959782587117836": {
            "length": 112,
            "waveforms": {
                "single": "6138959782587117836",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "131190181363292920": {
            "length": 112,
            "waveforms": {
                "single": "131190181363292920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2221175487399001300": {
            "length": 112,
            "waveforms": {
                "single": "-2221175487399001300",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7841166865249717430": {
            "length": 112,
            "waveforms": {
                "single": "-7841166865249717430",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "364362423977274349": {
            "length": 116,
            "waveforms": {
                "single": "364362423977274349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5643407177246550567": {
            "length": 116,
            "waveforms": {
                "single": "-5643407177246550567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1836235271003926916": {
            "length": 116,
            "waveforms": {
                "single": "-1836235271003926916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1614741211805211668": {
            "length": 116,
            "waveforms": {
                "single": "-1614741211805211668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7795331929007205558": {
            "length": 120,
            "waveforms": {
                "single": "7795331929007205558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5087121111068916894": {
            "length": 120,
            "waveforms": {
                "single": "-5087121111068916894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-564803340978913578": {
            "length": 120,
            "waveforms": {
                "single": "-564803340978913578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8184241719077206361_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "8184241719077206361_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-196862618431489046_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-196862618431489046_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "2097502163907163756": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5808884634377180267_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5808884634377180267_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7947618593601222852_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "7947618593601222852_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8232158397500463947": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6852654029804875484": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "6575459626388873270": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-3665755158093686567": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "7902591900631173574": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-4163120538874744923": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-1246501410891804456": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-1965360850871578060": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3986708406134959890": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "8509026176224963206": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "6184468094138126753": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-7739958209481421547": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-8361283977368115091": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-6807572103345945269": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-2285254333255941953": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4609812415342778406": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-87494645252775090": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-7754849701774325459": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5145715171773989256": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8062334299756929723": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "468791420924858583": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7564968918975871367": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2676245865506688470": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2953440268922690684": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2731946209723975436": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "947551733280619088": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5803171318466043260": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3272985384521815078": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4699023295305955773": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5542191489176604064": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1553986008874408720": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4544417314546828416": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7521295124959090081": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-2998977354869086765": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2110272075052042393": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6632589845142045709": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6249863194934076743": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
        },
        "8830349533145212572": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "9051843592343927820": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8684008434428862766": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5864922978539002359": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-5643428919340287111": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1963930976335692587": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1742436917136977339": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4593491048513989021": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1787540585689644098": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6407392027872727474": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5688532587892953870": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4206794332891526209": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-3987056772920199389": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4608382540806892933": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-801210634564269282": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6808980235788094198": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-9161345904550388418": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3665406791308447068": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6575807993174112769": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5863166479311613931": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-8776405688155314034": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2889475042662626167": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4875413685952004262": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1076655571054533688": {
            "samples": [0.12311557788944723] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-4931114030169291228": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3274415259057700551": {
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7796733029147703867": {
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2777049878276642195": {
            "samples": [0.12311557788944723] * 63 + [0.0],
            "type": "arbitrary",
        },
        "5693669006259582662": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "147489806098345761": {
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7519865250423204608": {
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2997547480333201292": {
            "samples": [0.12311557788944723] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-5322105562420037745": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "532430022493420145": {
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-88895745393273399": {
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "132598313805441849": {
            "samples": [0.12311557788944723] * 71 + [0.0],
            "type": "arbitrary",
        },
        "2951683769695302256": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2330358001808608712": {
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5863493104003116886": {
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "517538530200516233": {
            "samples": [0.12311557788944723] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-7966557126891238091": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3444239356801234775": {
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "362932549441388876": {
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1788970460225529571": {
            "samples": [0.12311557788944723] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-5423342992583720792": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3986730148228696434": {
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4208224207427411682": {
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8015396113670035333": {
            "samples": [0.12311557788944723] * 83 + [0.0],
            "type": "arbitrary",
        },
        "-5909030189949512967": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-8233588272036349420": {
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6807550361252208725": {
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3000378455009585074": {
            "samples": [0.12311557788944723] * 87 + [0.0],
            "type": "arbitrary",
        },
        "1521939315080418242": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6962156342011336082": {
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-581124707807702963": {
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8774975813619428561": {
            "samples": [0.12311557788944723] * 91 + [0.0],
            "type": "arbitrary",
        },
        "9050442492203429511": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6577216125616261698": {
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6355722066417546450": {
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6977047834304239994": {
            "samples": [0.12311557788944723] * 95 + [0.0],
            "type": "arbitrary",
        },
        "-1122512249390782104": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "8840136167227015188": {
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1075247438612384759": {
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1296741497811100007": {
            "samples": [0.12311557788944723] * 99 + [0.0],
            "type": "arbitrary",
        },
        "6308457255639149105": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3494501185814266870": {
            "samples": [0.12311557788944723] * 101 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9000173630888746796": {
            "samples": [0.12311557788944723] * 102 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8727711002841031216": {
            "samples": [0.12311557788944723] * 103 + [0.0],
            "type": "arbitrary",
        },
        "-1513503781641528621": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-87465870857387926": {
            "samples": [0.12311557788944723] * 105 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1569204125858815587": {
            "samples": [0.12311557788944723] * 106 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2953113644231187729": {
            "samples": [0.12311557788944723] * 107 + [0.0],
            "type": "arbitrary",
        },
        "2331787876344494185": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6138959782587117836": {
            "samples": [0.12311557788944723] * 109 + [0.0] * 3,
            "type": "arbitrary",
        },
        "131190181363292920": {
            "samples": [0.12311557788944723] * 110 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2221175487399001300": {
            "samples": [0.12311557788944723] * 111 + [0.0],
            "type": "arbitrary",
        },
        "-7841166865249717430": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "364362423977274349": {
            "samples": [0.12311557788944723] * 113 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5643407177246550567": {
            "samples": [0.12311557788944723] * 114 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1836235271003926916": {
            "samples": [0.12311557788944723] * 115 + [0.0],
            "type": "arbitrary",
        },
        "-1614741211805211668": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7795331929007205558": {
            "samples": [0.12311557788944723] * 117 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5087121111068916894": {
            "samples": [0.12311557788944723] * 118 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-564803340978913578": {
            "samples": [0.12311557788944723] * 119 + [0.0],
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
                "2097502163907163756": "2097502163907163756",
                "-8232158397500463947": "-8232158397500463947",
                "6852654029804875484": "6852654029804875484",
                "6575459626388873270": "6575459626388873270",
                "-3665755158093686567": "-3665755158093686567",
                "7902591900631173574": "7902591900631173574",
                "-4163120538874744923": "-4163120538874744923",
                "-1246501410891804456": "-1246501410891804456",
                "-1965360850871578060": "-1965360850871578060",
                "3986708406134959890": "3986708406134959890",
                "8509026176224963206": "8509026176224963206",
                "6184468094138126753": "6184468094138126753",
                "-7739958209481421547": "-7739958209481421547",
                "-8361283977368115091": "-8361283977368115091",
                "-6807572103345945269": "-6807572103345945269",
                "-2285254333255941953": "-2285254333255941953",
                "-4609812415342778406": "-4609812415342778406",
                "-87494645252775090": "-87494645252775090",
                "-7754849701774325459": "-7754849701774325459",
                "5145715171773989256": "5145715171773989256",
                "8062334299756929723": "8062334299756929723",
                "468791420924858583": "468791420924858583",
                "7564968918975871367": "7564968918975871367",
                "-2676245865506688470": "-2676245865506688470",
                "-2953440268922690684": "-2953440268922690684",
                "-2731946209723975436": "-2731946209723975436",
                "947551733280619088": "947551733280619088",
                "-5803171318466043260": "-5803171318466043260",
                "3272985384521815078": "3272985384521815078",
                "4699023295305955773": "4699023295305955773",
                "-5542191489176604064": "-5542191489176604064",
                "1553986008874408720": "1553986008874408720",
                "4544417314546828416": "4544417314546828416",
                "-7521295124959090081": "-7521295124959090081",
                "-2998977354869086765": "-2998977354869086765",
                "2110272075052042393": "2110272075052042393",
                "6632589845142045709": "6632589845142045709",
                "-6249863194934076743": "-6249863194934076743",
                "8830349533145212572": "8830349533145212572",
                "9051843592343927820": "9051843592343927820",
                "-8684008434428862766": "-8684008434428862766",
                "-5864922978539002359": "-5864922978539002359",
                "-5643428919340287111": "-5643428919340287111",
                "-1963930976335692587": "-1963930976335692587",
                "-1742436917136977339": "-1742436917136977339",
                "-4593491048513989021": "-4593491048513989021",
                "1787540585689644098": "1787540585689644098",
                "6407392027872727474": "6407392027872727474",
                "5688532587892953870": "5688532587892953870",
                "4206794332891526209": "4206794332891526209",
                "-3987056772920199389": "-3987056772920199389",
                "-4608382540806892933": "-4608382540806892933",
                "-801210634564269282": "-801210634564269282",
                "-6808980235788094198": "-6808980235788094198",
                "-9161345904550388418": "-9161345904550388418",
                "3665406791308447068": "3665406791308447068",
                "-6575807993174112769": "-6575807993174112769",
                "5863166479311613931": "5863166479311613931",
                "-8776405688155314034": "-8776405688155314034",
                "2889475042662626167": "2889475042662626167",
                "-4875413685952004262": "-4875413685952004262",
                "1076655571054533688": "1076655571054533688",
                "-4931114030169291228": "-4931114030169291228",
                "3274415259057700551": "3274415259057700551",
                "7796733029147703867": "7796733029147703867",
                "2777049878276642195": "2777049878276642195",
                "5693669006259582662": "5693669006259582662",
                "147489806098345761": "147489806098345761",
                "-7519865250423204608": "-7519865250423204608",
                "-2997547480333201292": "-2997547480333201292",
                "-5322105562420037745": "-5322105562420037745",
                "532430022493420145": "532430022493420145",
                "-88895745393273399": "-88895745393273399",
                "132598313805441849": "132598313805441849",
                "2951683769695302256": "2951683769695302256",
                "2330358001808608712": "2330358001808608712",
                "-5863493104003116886": "-5863493104003116886",
                "517538530200516233": "517538530200516233",
                "-7966557126891238091": "-7966557126891238091",
                "-3444239356801234775": "-3444239356801234775",
                "362932549441388876": "362932549441388876",
                "1788970460225529571": "1788970460225529571",
                "-5423342992583720792": "-5423342992583720792",
                "3986730148228696434": "3986730148228696434",
                "4208224207427411682": "4208224207427411682",
                "8015396113670035333": "8015396113670035333",
                "-5909030189949512967": "-5909030189949512967",
                "-8233588272036349420": "-8233588272036349420",
                "-6807550361252208725": "-6807550361252208725",
                "-3000378455009585074": "-3000378455009585074",
                "1521939315080418242": "1521939315080418242",
                "-6962156342011336082": "-6962156342011336082",
                "-581124707807702963": "-581124707807702963",
                "-8774975813619428561": "-8774975813619428561",
                "9050442492203429511": "9050442492203429511",
                "-6577216125616261698": "-6577216125616261698",
                "-6355722066417546450": "-6355722066417546450",
                "-6977047834304239994": "-6977047834304239994",
                "-1122512249390782104": "-1122512249390782104",
                "8840136167227015188": "8840136167227015188",
                "1075247438612384759": "1075247438612384759",
                "1296741497811100007": "1296741497811100007",
                "6308457255639149105": "6308457255639149105",
                "3494501185814266870": "3494501185814266870",
                "-9000173630888746796": "-9000173630888746796",
                "8727711002841031216": "8727711002841031216",
                "-1513503781641528621": "-1513503781641528621",
                "-87465870857387926": "-87465870857387926",
                "-1569204125858815587": "-1569204125858815587",
                "2953113644231187729": "2953113644231187729",
                "2331787876344494185": "2331787876344494185",
                "6138959782587117836": "6138959782587117836",
                "131190181363292920": "131190181363292920",
                "-2221175487399001300": "-2221175487399001300",
                "-7841166865249717430": "-7841166865249717430",
                "364362423977274349": "364362423977274349",
                "-5643407177246550567": "-5643407177246550567",
                "-1836235271003926916": "-1836235271003926916",
                "-1614741211805211668": "-1614741211805211668",
                "7795331929007205558": "7795331929007205558",
                "-5087121111068916894": "-5087121111068916894",
                "-564803340978913578": "-564803340978913578",
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
                "-7487101510498968938": "-7487101510498968938_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_995",
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
                "-818727195718244064": "-818727195718244064_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_36d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-196862618431489046": "-196862618431489046",
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
                "mixer": "B4/drive_mixer_7da",
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
                "8184241719077206361": "8184241719077206361",
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
                "mixer": "B2/drive_mixer_6e0",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
    },
    "pulses": {
        "8184241719077206361": {
            "length": 40,
            "waveforms": {
                "I": "8184241719077206361_i",
                "Q": "8184241719077206361_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-196862618431489046": {
            "length": 40,
            "waveforms": {
                "I": "-196862618431489046_i",
                "Q": "-196862618431489046_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2097502163907163756": {
            "length": 120,
            "waveforms": {
                "single": "2097502163907163756",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-818727195718244064_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5808884634377180267_i",
                "Q": "5808884634377180267_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-7487101510498968938_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7947618593601222852_i",
                "Q": "7947618593601222852_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8232158397500463947": {
            "length": 120,
            "waveforms": {
                "single": "-8232158397500463947",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6852654029804875484": {
            "length": 16,
            "waveforms": {
                "single": "6852654029804875484",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6575459626388873270": {
            "length": 16,
            "waveforms": {
                "single": "6575459626388873270",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3665755158093686567": {
            "length": 16,
            "waveforms": {
                "single": "-3665755158093686567",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7902591900631173574": {
            "length": 16,
            "waveforms": {
                "single": "7902591900631173574",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4163120538874744923": {
            "length": 16,
            "waveforms": {
                "single": "-4163120538874744923",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1246501410891804456": {
            "length": 16,
            "waveforms": {
                "single": "-1246501410891804456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1965360850871578060": {
            "length": 16,
            "waveforms": {
                "single": "-1965360850871578060",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3986708406134959890": {
            "length": 16,
            "waveforms": {
                "single": "3986708406134959890",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8509026176224963206": {
            "length": 16,
            "waveforms": {
                "single": "8509026176224963206",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6184468094138126753": {
            "length": 16,
            "waveforms": {
                "single": "6184468094138126753",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7739958209481421547": {
            "length": 16,
            "waveforms": {
                "single": "-7739958209481421547",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8361283977368115091": {
            "length": 16,
            "waveforms": {
                "single": "-8361283977368115091",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6807572103345945269": {
            "length": 16,
            "waveforms": {
                "single": "-6807572103345945269",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2285254333255941953": {
            "length": 16,
            "waveforms": {
                "single": "-2285254333255941953",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4609812415342778406": {
            "length": 16,
            "waveforms": {
                "single": "-4609812415342778406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-87494645252775090": {
            "length": 16,
            "waveforms": {
                "single": "-87494645252775090",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7754849701774325459": {
            "length": 16,
            "waveforms": {
                "single": "-7754849701774325459",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5145715171773989256": {
            "length": 20,
            "waveforms": {
                "single": "5145715171773989256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8062334299756929723": {
            "length": 20,
            "waveforms": {
                "single": "8062334299756929723",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "468791420924858583": {
            "length": 20,
            "waveforms": {
                "single": "468791420924858583",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7564968918975871367": {
            "length": 20,
            "waveforms": {
                "single": "7564968918975871367",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2676245865506688470": {
            "length": 24,
            "waveforms": {
                "single": "-2676245865506688470",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2953440268922690684": {
            "length": 24,
            "waveforms": {
                "single": "-2953440268922690684",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2731946209723975436": {
            "length": 24,
            "waveforms": {
                "single": "-2731946209723975436",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "947551733280619088": {
            "length": 24,
            "waveforms": {
                "single": "947551733280619088",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5803171318466043260": {
            "length": 28,
            "waveforms": {
                "single": "-5803171318466043260",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3272985384521815078": {
            "length": 28,
            "waveforms": {
                "single": "3272985384521815078",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4699023295305955773": {
            "length": 28,
            "waveforms": {
                "single": "4699023295305955773",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5542191489176604064": {
            "length": 28,
            "waveforms": {
                "single": "-5542191489176604064",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1553986008874408720": {
            "length": 32,
            "waveforms": {
                "single": "1553986008874408720",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4544417314546828416": {
            "length": 32,
            "waveforms": {
                "single": "4544417314546828416",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7521295124959090081": {
            "length": 32,
            "waveforms": {
                "single": "-7521295124959090081",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2998977354869086765": {
            "length": 32,
            "waveforms": {
                "single": "-2998977354869086765",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2110272075052042393": {
            "length": 36,
            "waveforms": {
                "single": "2110272075052042393",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6632589845142045709": {
            "length": 36,
            "waveforms": {
                "single": "6632589845142045709",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6249863194934076743": {
            "length": 36,
            "waveforms": {
                "single": "-6249863194934076743",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8830349533145212572": {
            "length": 36,
            "waveforms": {
                "single": "8830349533145212572",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9051843592343927820": {
            "length": 40,
            "waveforms": {
                "single": "9051843592343927820",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8684008434428862766": {
            "length": 40,
            "waveforms": {
                "single": "-8684008434428862766",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5864922978539002359": {
            "length": 40,
            "waveforms": {
                "single": "-5864922978539002359",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5643428919340287111": {
            "length": 40,
            "waveforms": {
                "single": "-5643428919340287111",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1963930976335692587": {
            "length": 44,
            "waveforms": {
                "single": "-1963930976335692587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1742436917136977339": {
            "length": 44,
            "waveforms": {
                "single": "-1742436917136977339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4593491048513989021": {
            "length": 44,
            "waveforms": {
                "single": "-4593491048513989021",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1787540585689644098": {
            "length": 44,
            "waveforms": {
                "single": "1787540585689644098",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6407392027872727474": {
            "length": 48,
            "waveforms": {
                "single": "6407392027872727474",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5688532587892953870": {
            "length": 48,
            "waveforms": {
                "single": "5688532587892953870",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4206794332891526209": {
            "length": 48,
            "waveforms": {
                "single": "4206794332891526209",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3987056772920199389": {
            "length": 48,
            "waveforms": {
                "single": "-3987056772920199389",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4608382540806892933": {
            "length": 52,
            "waveforms": {
                "single": "-4608382540806892933",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-801210634564269282": {
            "length": 52,
            "waveforms": {
                "single": "-801210634564269282",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6808980235788094198": {
            "length": 52,
            "waveforms": {
                "single": "-6808980235788094198",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9161345904550388418": {
            "length": 52,
            "waveforms": {
                "single": "-9161345904550388418",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3665406791308447068": {
            "length": 56,
            "waveforms": {
                "single": "3665406791308447068",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6575807993174112769": {
            "length": 56,
            "waveforms": {
                "single": "-6575807993174112769",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5863166479311613931": {
            "length": 56,
            "waveforms": {
                "single": "5863166479311613931",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8776405688155314034": {
            "length": 56,
            "waveforms": {
                "single": "-8776405688155314034",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2889475042662626167": {
            "length": 60,
            "waveforms": {
                "single": "2889475042662626167",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4875413685952004262": {
            "length": 60,
            "waveforms": {
                "single": "-4875413685952004262",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1076655571054533688": {
            "length": 60,
            "waveforms": {
                "single": "1076655571054533688",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4931114030169291228": {
            "length": 60,
            "waveforms": {
                "single": "-4931114030169291228",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3274415259057700551": {
            "length": 64,
            "waveforms": {
                "single": "3274415259057700551",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7796733029147703867": {
            "length": 64,
            "waveforms": {
                "single": "7796733029147703867",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2777049878276642195": {
            "length": 64,
            "waveforms": {
                "single": "2777049878276642195",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5693669006259582662": {
            "length": 64,
            "waveforms": {
                "single": "5693669006259582662",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "147489806098345761": {
            "length": 68,
            "waveforms": {
                "single": "147489806098345761",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7519865250423204608": {
            "length": 68,
            "waveforms": {
                "single": "-7519865250423204608",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2997547480333201292": {
            "length": 68,
            "waveforms": {
                "single": "-2997547480333201292",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5322105562420037745": {
            "length": 68,
            "waveforms": {
                "single": "-5322105562420037745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "532430022493420145": {
            "length": 72,
            "waveforms": {
                "single": "532430022493420145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-88895745393273399": {
            "length": 72,
            "waveforms": {
                "single": "-88895745393273399",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "132598313805441849": {
            "length": 72,
            "waveforms": {
                "single": "132598313805441849",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2951683769695302256": {
            "length": 72,
            "waveforms": {
                "single": "2951683769695302256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2330358001808608712": {
            "length": 76,
            "waveforms": {
                "single": "2330358001808608712",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5863493104003116886": {
            "length": 76,
            "waveforms": {
                "single": "-5863493104003116886",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "517538530200516233": {
            "length": 76,
            "waveforms": {
                "single": "517538530200516233",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7966557126891238091": {
            "length": 76,
            "waveforms": {
                "single": "-7966557126891238091",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3444239356801234775": {
            "length": 80,
            "waveforms": {
                "single": "-3444239356801234775",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "362932549441388876": {
            "length": 80,
            "waveforms": {
                "single": "362932549441388876",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1788970460225529571": {
            "length": 80,
            "waveforms": {
                "single": "1788970460225529571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5423342992583720792": {
            "length": 80,
            "waveforms": {
                "single": "-5423342992583720792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3986730148228696434": {
            "length": 84,
            "waveforms": {
                "single": "3986730148228696434",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4208224207427411682": {
            "length": 84,
            "waveforms": {
                "single": "4208224207427411682",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8015396113670035333": {
            "length": 84,
            "waveforms": {
                "single": "8015396113670035333",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5909030189949512967": {
            "length": 84,
            "waveforms": {
                "single": "-5909030189949512967",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8233588272036349420": {
            "length": 88,
            "waveforms": {
                "single": "-8233588272036349420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6807550361252208725": {
            "length": 88,
            "waveforms": {
                "single": "-6807550361252208725",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3000378455009585074": {
            "length": 88,
            "waveforms": {
                "single": "-3000378455009585074",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1521939315080418242": {
            "length": 88,
            "waveforms": {
                "single": "1521939315080418242",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6962156342011336082": {
            "length": 92,
            "waveforms": {
                "single": "-6962156342011336082",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-581124707807702963": {
            "length": 92,
            "waveforms": {
                "single": "-581124707807702963",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8774975813619428561": {
            "length": 92,
            "waveforms": {
                "single": "-8774975813619428561",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9050442492203429511": {
            "length": 92,
            "waveforms": {
                "single": "9050442492203429511",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6577216125616261698": {
            "length": 96,
            "waveforms": {
                "single": "-6577216125616261698",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6355722066417546450": {
            "length": 96,
            "waveforms": {
                "single": "-6355722066417546450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6977047834304239994": {
            "length": 96,
            "waveforms": {
                "single": "-6977047834304239994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1122512249390782104": {
            "length": 96,
            "waveforms": {
                "single": "-1122512249390782104",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8840136167227015188": {
            "length": 100,
            "waveforms": {
                "single": "8840136167227015188",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1075247438612384759": {
            "length": 100,
            "waveforms": {
                "single": "1075247438612384759",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1296741497811100007": {
            "length": 100,
            "waveforms": {
                "single": "1296741497811100007",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6308457255639149105": {
            "length": 100,
            "waveforms": {
                "single": "6308457255639149105",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3494501185814266870": {
            "length": 104,
            "waveforms": {
                "single": "3494501185814266870",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9000173630888746796": {
            "length": 104,
            "waveforms": {
                "single": "-9000173630888746796",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8727711002841031216": {
            "length": 104,
            "waveforms": {
                "single": "8727711002841031216",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1513503781641528621": {
            "length": 104,
            "waveforms": {
                "single": "-1513503781641528621",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-87465870857387926": {
            "length": 108,
            "waveforms": {
                "single": "-87465870857387926",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1569204125858815587": {
            "length": 108,
            "waveforms": {
                "single": "-1569204125858815587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2953113644231187729": {
            "length": 108,
            "waveforms": {
                "single": "2953113644231187729",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2331787876344494185": {
            "length": 108,
            "waveforms": {
                "single": "2331787876344494185",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6138959782587117836": {
            "length": 112,
            "waveforms": {
                "single": "6138959782587117836",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "131190181363292920": {
            "length": 112,
            "waveforms": {
                "single": "131190181363292920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2221175487399001300": {
            "length": 112,
            "waveforms": {
                "single": "-2221175487399001300",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7841166865249717430": {
            "length": 112,
            "waveforms": {
                "single": "-7841166865249717430",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "364362423977274349": {
            "length": 116,
            "waveforms": {
                "single": "364362423977274349",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5643407177246550567": {
            "length": 116,
            "waveforms": {
                "single": "-5643407177246550567",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1836235271003926916": {
            "length": 116,
            "waveforms": {
                "single": "-1836235271003926916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1614741211805211668": {
            "length": 116,
            "waveforms": {
                "single": "-1614741211805211668",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7795331929007205558": {
            "length": 120,
            "waveforms": {
                "single": "7795331929007205558",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5087121111068916894": {
            "length": 120,
            "waveforms": {
                "single": "-5087121111068916894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-564803340978913578": {
            "length": 120,
            "waveforms": {
                "single": "-564803340978913578",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "8184241719077206361_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8184241719077206361_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-196862618431489046_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-196862618431489046_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2097502163907163756": {
            "type": "constant",
            "sample": -0.2388,
        },
        "5808884634377180267_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5808884634377180267_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7947618593601222852_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "7947618593601222852_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8232158397500463947": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6852654029804875484": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6575459626388873270": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3665755158093686567": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7902591900631173574": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4163120538874744923": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1246501410891804456": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1965360850871578060": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3986708406134959890": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8509026176224963206": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6184468094138126753": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7739958209481421547": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8361283977368115091": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6807572103345945269": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2285254333255941953": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4609812415342778406": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-87494645252775090": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7754849701774325459": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "5145715171773989256": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8062334299756929723": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "468791420924858583": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7564968918975871367": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-2676245865506688470": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2953440268922690684": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2731946209723975436": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "947551733280619088": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-5803171318466043260": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3272985384521815078": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4699023295305955773": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5542191489176604064": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "1553986008874408720": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4544417314546828416": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7521295124959090081": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2998977354869086765": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2110272075052042393": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6632589845142045709": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6249863194934076743": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8830349533145212572": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "9051843592343927820": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8684008434428862766": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5864922978539002359": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5643428919340287111": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1963930976335692587": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1742436917136977339": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4593491048513989021": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1787540585689644098": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6407392027872727474": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5688532587892953870": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4206794332891526209": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3987056772920199389": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4608382540806892933": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-801210634564269282": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6808980235788094198": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9161345904550388418": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3665406791308447068": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6575807993174112769": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5863166479311613931": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8776405688155314034": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2889475042662626167": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4875413685952004262": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1076655571054533688": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4931114030169291228": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3274415259057700551": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7796733029147703867": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2777049878276642195": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5693669006259582662": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "147489806098345761": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7519865250423204608": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2997547480333201292": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5322105562420037745": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "532430022493420145": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-88895745393273399": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "132598313805441849": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2951683769695302256": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2330358001808608712": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5863493104003116886": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "517538530200516233": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7966557126891238091": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-3444239356801234775": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "362932549441388876": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1788970460225529571": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5423342992583720792": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3986730148228696434": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4208224207427411682": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8015396113670035333": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 83 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5909030189949512967": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-8233588272036349420": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6807550361252208725": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3000378455009585074": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 87 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1521939315080418242": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-6962156342011336082": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-581124707807702963": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8774975813619428561": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 91 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9050442492203429511": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-6577216125616261698": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6355722066417546450": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6977047834304239994": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 95 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1122512249390782104": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "8840136167227015188": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1075247438612384759": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1296741497811100007": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 99 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6308457255639149105": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3494501185814266870": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 101 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9000173630888746796": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 102 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8727711002841031216": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 103 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1513503781641528621": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-87465870857387926": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 105 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1569204125858815587": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 106 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2953113644231187729": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 107 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2331787876344494185": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6138959782587117836": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 109 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "131190181363292920": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 110 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2221175487399001300": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 111 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7841166865249717430": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "364362423977274349": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 113 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5643407177246550567": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 114 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1836235271003926916": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 115 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1614741211805211668": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "7795331929007205558": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 117 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5087121111068916894": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 118 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-564803340978913578": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 119 + [0.0],
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
        "B4/acquisition_mixer_995": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_36d": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_7da": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_6e0": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

