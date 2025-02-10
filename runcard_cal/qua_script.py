
# Single QUA script generated at 2025-02-10 06:54:43.689514
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
                play("-1754574909145824285", "B2/drive")
                play("3716457573997316228", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-5192774133393814404"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-1385602227151190753"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("3058081891422144907"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("6865253797664768558"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("5255841579425311770"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("6045367277878740456"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-7781525353647727784"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("1090656439054925071"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("8464621025080622567"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("3288416127058091934"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("-350555848617796575"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-129061789419081327"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-8710691118603915711"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("2068697898584085536"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-7505864382422813225"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("7301907715610849882"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-8325750902208841327"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-8947076670095534871"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-8725582610896819623"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("146599181805833232"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("7908341991204639514"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-673287337980194870"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-8340642394501745239"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("7577568686835764441"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("7799062746034479689"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-8495248375260872596"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-7069210464476731901"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-3262038558234108250"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-5864383728295629415"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-9048314100259217918"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("361759040553199308"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-1990606628209094912"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("4390425005994538207"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("2781012787755081419"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("6588184693997705070"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("968193316146988940"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-1384172352615305280"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-3708730434702141733"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("813587335387861583"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("-4206095815483200089"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("6046797152414625929"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("6268291211613341177"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("8244556840417792792"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("8466050899616508040"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("798695843094957671"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-8775866437911941090"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-6229221612067706891"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-2549723669063112367"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-2328229609864397119"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("6543952182838255736"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-130469921861230256"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("5821599335145307694"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("5102739895165534090"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("2750374226403239870"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("8143319410254109745"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("7521993642367416201"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("-2719221142115143636"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-8339212519965859766"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("8699605476431743418"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("1747396283757572714"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("5554568190000196365"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("6980606100784337060"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("7752327878003363228"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("2303682349935206387"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("-5461206378679424042"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-5239712319480708794"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("5013180648417117224"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("2688622566330280771"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("7210940336420284087"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("6589614568533590543"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("6811108627732305791"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("-8816549990087385418"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("-8105657943150624388"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("-3583340173060621072"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("-4204665940947314616"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("-1385580485057454209"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-1164086425858738961"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-453194378921977931"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("4069123391168025385"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("1744565309081188932"*amp(v9), "B4/flux")
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
                play("3716457573997316228", "B4/drive")
                measure("-2084144712387192182", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
                assign(v4, Cast.to_int((((v2*0.7359973353402354)-(v3*0.6769844328875466))>0.0024378669440833717)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-8019123602724849505", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                assign(v7, Cast.to_int((((v5*0.45141096231273753)-(v6*0.8923161676804294))>-0.000508161646537873)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(15).buffer(80).average().save("-2084144712387192182_B2|acquisition_shots")
        r2.buffer(15).buffer(80).average().save("-8019123602724849505_B4|acquisition_shots")


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
                "1456349190373552563": "1456349190373552563",
                "6266883079171192248": "6266883079171192248",
                "-5192774133393814404": "-5192774133393814404",
                "-1385602227151190753": "-1385602227151190753",
                "3058081891422144907": "3058081891422144907",
                "6865253797664768558": "6865253797664768558",
                "5255841579425311770": "5255841579425311770",
                "6045367277878740456": "6045367277878740456",
                "-7781525353647727784": "-7781525353647727784",
                "1090656439054925071": "1090656439054925071",
                "8464621025080622567": "8464621025080622567",
                "3288416127058091934": "3288416127058091934",
                "-350555848617796575": "-350555848617796575",
                "-129061789419081327": "-129061789419081327",
                "-8710691118603915711": "-8710691118603915711",
                "2068697898584085536": "2068697898584085536",
                "-7505864382422813225": "-7505864382422813225",
                "7301907715610849882": "7301907715610849882",
                "-8325750902208841327": "-8325750902208841327",
                "-8947076670095534871": "-8947076670095534871",
                "-8725582610896819623": "-8725582610896819623",
                "146599181805833232": "146599181805833232",
                "7908341991204639514": "7908341991204639514",
                "-673287337980194870": "-673287337980194870",
                "-8340642394501745239": "-8340642394501745239",
                "7577568686835764441": "7577568686835764441",
                "7799062746034479689": "7799062746034479689",
                "-8495248375260872596": "-8495248375260872596",
                "-7069210464476731901": "-7069210464476731901",
                "-3262038558234108250": "-3262038558234108250",
                "-5864383728295629415": "-5864383728295629415",
                "-9048314100259217918": "-9048314100259217918",
                "361759040553199308": "361759040553199308",
                "-1990606628209094912": "-1990606628209094912",
                "4390425005994538207": "4390425005994538207",
                "2781012787755081419": "2781012787755081419",
                "6588184693997705070": "6588184693997705070",
                "968193316146988940": "968193316146988940",
                "-1384172352615305280": "-1384172352615305280",
                "-3708730434702141733": "-3708730434702141733",
                "813587335387861583": "813587335387861583",
                "-4206095815483200089": "-4206095815483200089",
                "6046797152414625929": "6046797152414625929",
                "6268291211613341177": "6268291211613341177",
                "8244556840417792792": "8244556840417792792",
                "8466050899616508040": "8466050899616508040",
                "798695843094957671": "798695843094957671",
                "-8775866437911941090": "-8775866437911941090",
                "-6229221612067706891": "-6229221612067706891",
                "-2549723669063112367": "-2549723669063112367",
                "-2328229609864397119": "-2328229609864397119",
                "6543952182838255736": "6543952182838255736",
                "-130469921861230256": "-130469921861230256",
                "5821599335145307694": "5821599335145307694",
                "5102739895165534090": "5102739895165534090",
                "2750374226403239870": "2750374226403239870",
                "8143319410254109745": "8143319410254109745",
                "7521993642367416201": "7521993642367416201",
                "-2719221142115143636": "-2719221142115143636",
                "-8339212519965859766": "-8339212519965859766",
                "8699605476431743418": "8699605476431743418",
                "1747396283757572714": "1747396283757572714",
                "5554568190000196365": "5554568190000196365",
                "6980606100784337060": "6980606100784337060",
                "7752327878003363228": "7752327878003363228",
                "2303682349935206387": "2303682349935206387",
                "-5461206378679424042": "-5461206378679424042",
                "-5239712319480708794": "-5239712319480708794",
                "5013180648417117224": "5013180648417117224",
                "2688622566330280771": "2688622566330280771",
                "7210940336420284087": "7210940336420284087",
                "6589614568533590543": "6589614568533590543",
                "6811108627732305791": "6811108627732305791",
                "-8816549990087385418": "-8816549990087385418",
                "-8105657943150624388": "-8105657943150624388",
                "-3583340173060621072": "-3583340173060621072",
                "-4204665940947314616": "-4204665940947314616",
                "-1385580485057454209": "-1385580485057454209",
                "-1164086425858738961": "-1164086425858738961",
                "-453194378921977931": "-453194378921977931",
                "4069123391168025385": "4069123391168025385",
                "1744565309081188932": "1744565309081188932",
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
                "-8019123602724849505": "-8019123602724849505_B4/acquisition",
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
                "-1754574909145824285": "-1754574909145824285",
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
                "-2084144712387192182": "-2084144712387192182_B2/acquisition",
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
                "3716457573997316228": "3716457573997316228",
            },
        },
    },
    "pulses": {
        "-1754574909145824285": {
            "length": 40,
            "waveforms": {
                "I": "-1754574909145824285_i",
                "Q": "-1754574909145824285_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3716457573997316228": {
            "length": 40,
            "waveforms": {
                "I": "3716457573997316228_i",
                "Q": "3716457573997316228_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1456349190373552563": {
            "length": 80,
            "waveforms": {
                "single": "1456349190373552563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2084144712387192182_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2911491531732205985_i",
                "Q": "2911491531732205985_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-8019123602724849505_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "651868107971880442_i",
                "Q": "651868107971880442_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6266883079171192248": {
            "length": 80,
            "waveforms": {
                "single": "6266883079171192248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5192774133393814404": {
            "length": 16,
            "waveforms": {
                "single": "-5192774133393814404",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1385602227151190753": {
            "length": 16,
            "waveforms": {
                "single": "-1385602227151190753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3058081891422144907": {
            "length": 16,
            "waveforms": {
                "single": "3058081891422144907",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6865253797664768558": {
            "length": 16,
            "waveforms": {
                "single": "6865253797664768558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5255841579425311770": {
            "length": 16,
            "waveforms": {
                "single": "5255841579425311770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6045367277878740456": {
            "length": 16,
            "waveforms": {
                "single": "6045367277878740456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7781525353647727784": {
            "length": 16,
            "waveforms": {
                "single": "-7781525353647727784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1090656439054925071": {
            "length": 16,
            "waveforms": {
                "single": "1090656439054925071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8464621025080622567": {
            "length": 16,
            "waveforms": {
                "single": "8464621025080622567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3288416127058091934": {
            "length": 16,
            "waveforms": {
                "single": "3288416127058091934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-350555848617796575": {
            "length": 16,
            "waveforms": {
                "single": "-350555848617796575",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-129061789419081327": {
            "length": 16,
            "waveforms": {
                "single": "-129061789419081327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8710691118603915711": {
            "length": 16,
            "waveforms": {
                "single": "-8710691118603915711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2068697898584085536": {
            "length": 16,
            "waveforms": {
                "single": "2068697898584085536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7505864382422813225": {
            "length": 16,
            "waveforms": {
                "single": "-7505864382422813225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7301907715610849882": {
            "length": 16,
            "waveforms": {
                "single": "7301907715610849882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8325750902208841327": {
            "length": 16,
            "waveforms": {
                "single": "-8325750902208841327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8947076670095534871": {
            "length": 20,
            "waveforms": {
                "single": "-8947076670095534871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8725582610896819623": {
            "length": 20,
            "waveforms": {
                "single": "-8725582610896819623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "146599181805833232": {
            "length": 20,
            "waveforms": {
                "single": "146599181805833232",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7908341991204639514": {
            "length": 20,
            "waveforms": {
                "single": "7908341991204639514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-673287337980194870": {
            "length": 24,
            "waveforms": {
                "single": "-673287337980194870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8340642394501745239": {
            "length": 24,
            "waveforms": {
                "single": "-8340642394501745239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7577568686835764441": {
            "length": 24,
            "waveforms": {
                "single": "7577568686835764441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7799062746034479689": {
            "length": 24,
            "waveforms": {
                "single": "7799062746034479689",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8495248375260872596": {
            "length": 28,
            "waveforms": {
                "single": "-8495248375260872596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7069210464476731901": {
            "length": 28,
            "waveforms": {
                "single": "-7069210464476731901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3262038558234108250": {
            "length": 28,
            "waveforms": {
                "single": "-3262038558234108250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5864383728295629415": {
            "length": 28,
            "waveforms": {
                "single": "-5864383728295629415",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9048314100259217918": {
            "length": 32,
            "waveforms": {
                "single": "-9048314100259217918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "361759040553199308": {
            "length": 32,
            "waveforms": {
                "single": "361759040553199308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1990606628209094912": {
            "length": 32,
            "waveforms": {
                "single": "-1990606628209094912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4390425005994538207": {
            "length": 32,
            "waveforms": {
                "single": "4390425005994538207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2781012787755081419": {
            "length": 36,
            "waveforms": {
                "single": "2781012787755081419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6588184693997705070": {
            "length": 36,
            "waveforms": {
                "single": "6588184693997705070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "968193316146988940": {
            "length": 36,
            "waveforms": {
                "single": "968193316146988940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1384172352615305280": {
            "length": 36,
            "waveforms": {
                "single": "-1384172352615305280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3708730434702141733": {
            "length": 40,
            "waveforms": {
                "single": "-3708730434702141733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "813587335387861583": {
            "length": 40,
            "waveforms": {
                "single": "813587335387861583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4206095815483200089": {
            "length": 40,
            "waveforms": {
                "single": "-4206095815483200089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6046797152414625929": {
            "length": 40,
            "waveforms": {
                "single": "6046797152414625929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6268291211613341177": {
            "length": 44,
            "waveforms": {
                "single": "6268291211613341177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8244556840417792792": {
            "length": 44,
            "waveforms": {
                "single": "8244556840417792792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8466050899616508040": {
            "length": 44,
            "waveforms": {
                "single": "8466050899616508040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "798695843094957671": {
            "length": 44,
            "waveforms": {
                "single": "798695843094957671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8775866437911941090": {
            "length": 48,
            "waveforms": {
                "single": "-8775866437911941090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6229221612067706891": {
            "length": 48,
            "waveforms": {
                "single": "-6229221612067706891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2549723669063112367": {
            "length": 48,
            "waveforms": {
                "single": "-2549723669063112367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2328229609864397119": {
            "length": 48,
            "waveforms": {
                "single": "-2328229609864397119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6543952182838255736": {
            "length": 52,
            "waveforms": {
                "single": "6543952182838255736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-130469921861230256": {
            "length": 52,
            "waveforms": {
                "single": "-130469921861230256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5821599335145307694": {
            "length": 52,
            "waveforms": {
                "single": "5821599335145307694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5102739895165534090": {
            "length": 52,
            "waveforms": {
                "single": "5102739895165534090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2750374226403239870": {
            "length": 56,
            "waveforms": {
                "single": "2750374226403239870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8143319410254109745": {
            "length": 56,
            "waveforms": {
                "single": "8143319410254109745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7521993642367416201": {
            "length": 56,
            "waveforms": {
                "single": "7521993642367416201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2719221142115143636": {
            "length": 56,
            "waveforms": {
                "single": "-2719221142115143636",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8339212519965859766": {
            "length": 60,
            "waveforms": {
                "single": "-8339212519965859766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8699605476431743418": {
            "length": 60,
            "waveforms": {
                "single": "8699605476431743418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1747396283757572714": {
            "length": 60,
            "waveforms": {
                "single": "1747396283757572714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5554568190000196365": {
            "length": 60,
            "waveforms": {
                "single": "5554568190000196365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6980606100784337060": {
            "length": 64,
            "waveforms": {
                "single": "6980606100784337060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7752327878003363228": {
            "length": 64,
            "waveforms": {
                "single": "7752327878003363228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2303682349935206387": {
            "length": 64,
            "waveforms": {
                "single": "2303682349935206387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5461206378679424042": {
            "length": 64,
            "waveforms": {
                "single": "-5461206378679424042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5239712319480708794": {
            "length": 68,
            "waveforms": {
                "single": "-5239712319480708794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5013180648417117224": {
            "length": 68,
            "waveforms": {
                "single": "5013180648417117224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2688622566330280771": {
            "length": 68,
            "waveforms": {
                "single": "2688622566330280771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7210940336420284087": {
            "length": 68,
            "waveforms": {
                "single": "7210940336420284087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6589614568533590543": {
            "length": 72,
            "waveforms": {
                "single": "6589614568533590543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6811108627732305791": {
            "length": 72,
            "waveforms": {
                "single": "6811108627732305791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8816549990087385418": {
            "length": 72,
            "waveforms": {
                "single": "-8816549990087385418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8105657943150624388": {
            "length": 72,
            "waveforms": {
                "single": "-8105657943150624388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3583340173060621072": {
            "length": 76,
            "waveforms": {
                "single": "-3583340173060621072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4204665940947314616": {
            "length": 76,
            "waveforms": {
                "single": "-4204665940947314616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1385580485057454209": {
            "length": 76,
            "waveforms": {
                "single": "-1385580485057454209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1164086425858738961": {
            "length": 76,
            "waveforms": {
                "single": "-1164086425858738961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-453194378921977931": {
            "length": 80,
            "waveforms": {
                "single": "-453194378921977931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4069123391168025385": {
            "length": 80,
            "waveforms": {
                "single": "4069123391168025385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1744565309081188932": {
            "length": 80,
            "waveforms": {
                "single": "1744565309081188932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1754574909145824285_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-1754574909145824285_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "3716457573997316228_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "3716457573997316228_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "1456349190373552563": {
            "sample": -0.2388,
            "type": "constant",
        },
        "2911491531732205985_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "2911491531732205985_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "651868107971880442_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "651868107971880442_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6266883079171192248": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5192774133393814404": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1385602227151190753": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
        },
        "3058081891422144907": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "6865253797664768558": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "5255841579425311770": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "6045367277878740456": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-7781525353647727784": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "1090656439054925071": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "8464621025080622567": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3288416127058091934": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-350555848617796575": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-129061789419081327": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-8710691118603915711": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "2068697898584085536": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7505864382422813225": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7301907715610849882": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8325750902208841327": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8947076670095534871": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8725582610896819623": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "146599181805833232": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7908341991204639514": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-673287337980194870": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8340642394501745239": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7577568686835764441": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
        },
        "7799062746034479689": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8495248375260872596": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7069210464476731901": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3262038558234108250": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5864383728295629415": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-9048314100259217918": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "361759040553199308": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1990606628209094912": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
        },
        "4390425005994538207": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2781012787755081419": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6588184693997705070": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "968193316146988940": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-1384172352615305280": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3708730434702141733": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "813587335387861583": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4206095815483200089": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6046797152414625929": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6268291211613341177": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8244556840417792792": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8466050899616508040": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
        },
        "798695843094957671": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8775866437911941090": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6229221612067706891": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2549723669063112367": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2328229609864397119": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6543952182838255736": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-130469921861230256": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5821599335145307694": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
        },
        "5102739895165534090": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2750374226403239870": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8143319410254109745": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7521993642367416201": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-2719221142115143636": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8339212519965859766": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8699605476431743418": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1747396283757572714": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
        },
        "5554568190000196365": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6980606100784337060": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7752327878003363228": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2303682349935206387": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-5461206378679424042": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5239712319480708794": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5013180648417117224": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2688622566330280771": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
        },
        "7210940336420284087": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6589614568533590543": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6811108627732305791": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8816549990087385418": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-8105657943150624388": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3583340173060621072": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4204665940947314616": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1385580485057454209": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-1164086425858738961": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-453194378921977931": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4069123391168025385": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1744565309081188932": {
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
                "1456349190373552563": "1456349190373552563",
                "6266883079171192248": "6266883079171192248",
                "-5192774133393814404": "-5192774133393814404",
                "-1385602227151190753": "-1385602227151190753",
                "3058081891422144907": "3058081891422144907",
                "6865253797664768558": "6865253797664768558",
                "5255841579425311770": "5255841579425311770",
                "6045367277878740456": "6045367277878740456",
                "-7781525353647727784": "-7781525353647727784",
                "1090656439054925071": "1090656439054925071",
                "8464621025080622567": "8464621025080622567",
                "3288416127058091934": "3288416127058091934",
                "-350555848617796575": "-350555848617796575",
                "-129061789419081327": "-129061789419081327",
                "-8710691118603915711": "-8710691118603915711",
                "2068697898584085536": "2068697898584085536",
                "-7505864382422813225": "-7505864382422813225",
                "7301907715610849882": "7301907715610849882",
                "-8325750902208841327": "-8325750902208841327",
                "-8947076670095534871": "-8947076670095534871",
                "-8725582610896819623": "-8725582610896819623",
                "146599181805833232": "146599181805833232",
                "7908341991204639514": "7908341991204639514",
                "-673287337980194870": "-673287337980194870",
                "-8340642394501745239": "-8340642394501745239",
                "7577568686835764441": "7577568686835764441",
                "7799062746034479689": "7799062746034479689",
                "-8495248375260872596": "-8495248375260872596",
                "-7069210464476731901": "-7069210464476731901",
                "-3262038558234108250": "-3262038558234108250",
                "-5864383728295629415": "-5864383728295629415",
                "-9048314100259217918": "-9048314100259217918",
                "361759040553199308": "361759040553199308",
                "-1990606628209094912": "-1990606628209094912",
                "4390425005994538207": "4390425005994538207",
                "2781012787755081419": "2781012787755081419",
                "6588184693997705070": "6588184693997705070",
                "968193316146988940": "968193316146988940",
                "-1384172352615305280": "-1384172352615305280",
                "-3708730434702141733": "-3708730434702141733",
                "813587335387861583": "813587335387861583",
                "-4206095815483200089": "-4206095815483200089",
                "6046797152414625929": "6046797152414625929",
                "6268291211613341177": "6268291211613341177",
                "8244556840417792792": "8244556840417792792",
                "8466050899616508040": "8466050899616508040",
                "798695843094957671": "798695843094957671",
                "-8775866437911941090": "-8775866437911941090",
                "-6229221612067706891": "-6229221612067706891",
                "-2549723669063112367": "-2549723669063112367",
                "-2328229609864397119": "-2328229609864397119",
                "6543952182838255736": "6543952182838255736",
                "-130469921861230256": "-130469921861230256",
                "5821599335145307694": "5821599335145307694",
                "5102739895165534090": "5102739895165534090",
                "2750374226403239870": "2750374226403239870",
                "8143319410254109745": "8143319410254109745",
                "7521993642367416201": "7521993642367416201",
                "-2719221142115143636": "-2719221142115143636",
                "-8339212519965859766": "-8339212519965859766",
                "8699605476431743418": "8699605476431743418",
                "1747396283757572714": "1747396283757572714",
                "5554568190000196365": "5554568190000196365",
                "6980606100784337060": "6980606100784337060",
                "7752327878003363228": "7752327878003363228",
                "2303682349935206387": "2303682349935206387",
                "-5461206378679424042": "-5461206378679424042",
                "-5239712319480708794": "-5239712319480708794",
                "5013180648417117224": "5013180648417117224",
                "2688622566330280771": "2688622566330280771",
                "7210940336420284087": "7210940336420284087",
                "6589614568533590543": "6589614568533590543",
                "6811108627732305791": "6811108627732305791",
                "-8816549990087385418": "-8816549990087385418",
                "-8105657943150624388": "-8105657943150624388",
                "-3583340173060621072": "-3583340173060621072",
                "-4204665940947314616": "-4204665940947314616",
                "-1385580485057454209": "-1385580485057454209",
                "-1164086425858738961": "-1164086425858738961",
                "-453194378921977931": "-453194378921977931",
                "4069123391168025385": "4069123391168025385",
                "1744565309081188932": "1744565309081188932",
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
                "-8019123602724849505": "-8019123602724849505_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_fe2",
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
                "-1754574909145824285": "-1754574909145824285",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_487",
                "lo_frequency": 5900000000.0,
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
                "-2084144712387192182": "-2084144712387192182_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_bdb",
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
                "3716457573997316228": "3716457573997316228",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_13d",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "-1754574909145824285": {
            "length": 40,
            "waveforms": {
                "I": "-1754574909145824285_i",
                "Q": "-1754574909145824285_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3716457573997316228": {
            "length": 40,
            "waveforms": {
                "I": "3716457573997316228_i",
                "Q": "3716457573997316228_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1456349190373552563": {
            "length": 80,
            "waveforms": {
                "single": "1456349190373552563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2084144712387192182_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2911491531732205985_i",
                "Q": "2911491531732205985_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-8019123602724849505_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "651868107971880442_i",
                "Q": "651868107971880442_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "6266883079171192248": {
            "length": 80,
            "waveforms": {
                "single": "6266883079171192248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5192774133393814404": {
            "length": 16,
            "waveforms": {
                "single": "-5192774133393814404",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1385602227151190753": {
            "length": 16,
            "waveforms": {
                "single": "-1385602227151190753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3058081891422144907": {
            "length": 16,
            "waveforms": {
                "single": "3058081891422144907",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6865253797664768558": {
            "length": 16,
            "waveforms": {
                "single": "6865253797664768558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5255841579425311770": {
            "length": 16,
            "waveforms": {
                "single": "5255841579425311770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6045367277878740456": {
            "length": 16,
            "waveforms": {
                "single": "6045367277878740456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7781525353647727784": {
            "length": 16,
            "waveforms": {
                "single": "-7781525353647727784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1090656439054925071": {
            "length": 16,
            "waveforms": {
                "single": "1090656439054925071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8464621025080622567": {
            "length": 16,
            "waveforms": {
                "single": "8464621025080622567",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3288416127058091934": {
            "length": 16,
            "waveforms": {
                "single": "3288416127058091934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-350555848617796575": {
            "length": 16,
            "waveforms": {
                "single": "-350555848617796575",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-129061789419081327": {
            "length": 16,
            "waveforms": {
                "single": "-129061789419081327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8710691118603915711": {
            "length": 16,
            "waveforms": {
                "single": "-8710691118603915711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2068697898584085536": {
            "length": 16,
            "waveforms": {
                "single": "2068697898584085536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7505864382422813225": {
            "length": 16,
            "waveforms": {
                "single": "-7505864382422813225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7301907715610849882": {
            "length": 16,
            "waveforms": {
                "single": "7301907715610849882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8325750902208841327": {
            "length": 16,
            "waveforms": {
                "single": "-8325750902208841327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8947076670095534871": {
            "length": 20,
            "waveforms": {
                "single": "-8947076670095534871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8725582610896819623": {
            "length": 20,
            "waveforms": {
                "single": "-8725582610896819623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "146599181805833232": {
            "length": 20,
            "waveforms": {
                "single": "146599181805833232",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7908341991204639514": {
            "length": 20,
            "waveforms": {
                "single": "7908341991204639514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-673287337980194870": {
            "length": 24,
            "waveforms": {
                "single": "-673287337980194870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8340642394501745239": {
            "length": 24,
            "waveforms": {
                "single": "-8340642394501745239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7577568686835764441": {
            "length": 24,
            "waveforms": {
                "single": "7577568686835764441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7799062746034479689": {
            "length": 24,
            "waveforms": {
                "single": "7799062746034479689",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8495248375260872596": {
            "length": 28,
            "waveforms": {
                "single": "-8495248375260872596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7069210464476731901": {
            "length": 28,
            "waveforms": {
                "single": "-7069210464476731901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3262038558234108250": {
            "length": 28,
            "waveforms": {
                "single": "-3262038558234108250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5864383728295629415": {
            "length": 28,
            "waveforms": {
                "single": "-5864383728295629415",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9048314100259217918": {
            "length": 32,
            "waveforms": {
                "single": "-9048314100259217918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "361759040553199308": {
            "length": 32,
            "waveforms": {
                "single": "361759040553199308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1990606628209094912": {
            "length": 32,
            "waveforms": {
                "single": "-1990606628209094912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4390425005994538207": {
            "length": 32,
            "waveforms": {
                "single": "4390425005994538207",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2781012787755081419": {
            "length": 36,
            "waveforms": {
                "single": "2781012787755081419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6588184693997705070": {
            "length": 36,
            "waveforms": {
                "single": "6588184693997705070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "968193316146988940": {
            "length": 36,
            "waveforms": {
                "single": "968193316146988940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1384172352615305280": {
            "length": 36,
            "waveforms": {
                "single": "-1384172352615305280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3708730434702141733": {
            "length": 40,
            "waveforms": {
                "single": "-3708730434702141733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "813587335387861583": {
            "length": 40,
            "waveforms": {
                "single": "813587335387861583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4206095815483200089": {
            "length": 40,
            "waveforms": {
                "single": "-4206095815483200089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6046797152414625929": {
            "length": 40,
            "waveforms": {
                "single": "6046797152414625929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6268291211613341177": {
            "length": 44,
            "waveforms": {
                "single": "6268291211613341177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8244556840417792792": {
            "length": 44,
            "waveforms": {
                "single": "8244556840417792792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8466050899616508040": {
            "length": 44,
            "waveforms": {
                "single": "8466050899616508040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "798695843094957671": {
            "length": 44,
            "waveforms": {
                "single": "798695843094957671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8775866437911941090": {
            "length": 48,
            "waveforms": {
                "single": "-8775866437911941090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6229221612067706891": {
            "length": 48,
            "waveforms": {
                "single": "-6229221612067706891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2549723669063112367": {
            "length": 48,
            "waveforms": {
                "single": "-2549723669063112367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2328229609864397119": {
            "length": 48,
            "waveforms": {
                "single": "-2328229609864397119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6543952182838255736": {
            "length": 52,
            "waveforms": {
                "single": "6543952182838255736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-130469921861230256": {
            "length": 52,
            "waveforms": {
                "single": "-130469921861230256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5821599335145307694": {
            "length": 52,
            "waveforms": {
                "single": "5821599335145307694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5102739895165534090": {
            "length": 52,
            "waveforms": {
                "single": "5102739895165534090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2750374226403239870": {
            "length": 56,
            "waveforms": {
                "single": "2750374226403239870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8143319410254109745": {
            "length": 56,
            "waveforms": {
                "single": "8143319410254109745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7521993642367416201": {
            "length": 56,
            "waveforms": {
                "single": "7521993642367416201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2719221142115143636": {
            "length": 56,
            "waveforms": {
                "single": "-2719221142115143636",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8339212519965859766": {
            "length": 60,
            "waveforms": {
                "single": "-8339212519965859766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8699605476431743418": {
            "length": 60,
            "waveforms": {
                "single": "8699605476431743418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1747396283757572714": {
            "length": 60,
            "waveforms": {
                "single": "1747396283757572714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5554568190000196365": {
            "length": 60,
            "waveforms": {
                "single": "5554568190000196365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6980606100784337060": {
            "length": 64,
            "waveforms": {
                "single": "6980606100784337060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7752327878003363228": {
            "length": 64,
            "waveforms": {
                "single": "7752327878003363228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2303682349935206387": {
            "length": 64,
            "waveforms": {
                "single": "2303682349935206387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5461206378679424042": {
            "length": 64,
            "waveforms": {
                "single": "-5461206378679424042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5239712319480708794": {
            "length": 68,
            "waveforms": {
                "single": "-5239712319480708794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5013180648417117224": {
            "length": 68,
            "waveforms": {
                "single": "5013180648417117224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2688622566330280771": {
            "length": 68,
            "waveforms": {
                "single": "2688622566330280771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7210940336420284087": {
            "length": 68,
            "waveforms": {
                "single": "7210940336420284087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6589614568533590543": {
            "length": 72,
            "waveforms": {
                "single": "6589614568533590543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6811108627732305791": {
            "length": 72,
            "waveforms": {
                "single": "6811108627732305791",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8816549990087385418": {
            "length": 72,
            "waveforms": {
                "single": "-8816549990087385418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8105657943150624388": {
            "length": 72,
            "waveforms": {
                "single": "-8105657943150624388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3583340173060621072": {
            "length": 76,
            "waveforms": {
                "single": "-3583340173060621072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4204665940947314616": {
            "length": 76,
            "waveforms": {
                "single": "-4204665940947314616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1385580485057454209": {
            "length": 76,
            "waveforms": {
                "single": "-1385580485057454209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1164086425858738961": {
            "length": 76,
            "waveforms": {
                "single": "-1164086425858738961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-453194378921977931": {
            "length": 80,
            "waveforms": {
                "single": "-453194378921977931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4069123391168025385": {
            "length": 80,
            "waveforms": {
                "single": "4069123391168025385",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1744565309081188932": {
            "length": 80,
            "waveforms": {
                "single": "1744565309081188932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1754574909145824285_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1754574909145824285_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3716457573997316228_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3716457573997316228_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1456349190373552563": {
            "sample": -0.2388,
            "type": "constant",
        },
        "2911491531732205985_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "2911491531732205985_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "651868107971880442_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "651868107971880442_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6266883079171192248": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5192774133393814404": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1385602227151190753": {
            "samples": [0.06206030150753769] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3058081891422144907": {
            "samples": [0.06206030150753769] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6865253797664768558": {
            "samples": [0.06206030150753769] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5255841579425311770": {
            "samples": [0.06206030150753769] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6045367277878740456": {
            "samples": [0.06206030150753769] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7781525353647727784": {
            "samples": [0.06206030150753769] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1090656439054925071": {
            "samples": [0.06206030150753769] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8464621025080622567": {
            "samples": [0.06206030150753769] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3288416127058091934": {
            "samples": [0.06206030150753769] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-350555848617796575": {
            "samples": [0.06206030150753769] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-129061789419081327": {
            "samples": [0.06206030150753769] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8710691118603915711": {
            "samples": [0.06206030150753769] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2068697898584085536": {
            "samples": [0.06206030150753769] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7505864382422813225": {
            "samples": [0.06206030150753769] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7301907715610849882": {
            "samples": [0.06206030150753769] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8325750902208841327": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8947076670095534871": {
            "samples": [0.06206030150753769] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8725582610896819623": {
            "samples": [0.06206030150753769] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "146599181805833232": {
            "samples": [0.06206030150753769] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7908341991204639514": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-673287337980194870": {
            "samples": [0.06206030150753769] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8340642394501745239": {
            "samples": [0.06206030150753769] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7577568686835764441": {
            "samples": [0.06206030150753769] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7799062746034479689": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8495248375260872596": {
            "samples": [0.06206030150753769] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7069210464476731901": {
            "samples": [0.06206030150753769] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3262038558234108250": {
            "samples": [0.06206030150753769] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5864383728295629415": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-9048314100259217918": {
            "samples": [0.06206030150753769] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "361759040553199308": {
            "samples": [0.06206030150753769] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1990606628209094912": {
            "samples": [0.06206030150753769] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4390425005994538207": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2781012787755081419": {
            "samples": [0.06206030150753769] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6588184693997705070": {
            "samples": [0.06206030150753769] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "968193316146988940": {
            "samples": [0.06206030150753769] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1384172352615305280": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3708730434702141733": {
            "samples": [0.06206030150753769] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "813587335387861583": {
            "samples": [0.06206030150753769] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4206095815483200089": {
            "samples": [0.06206030150753769] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6046797152414625929": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6268291211613341177": {
            "samples": [0.06206030150753769] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8244556840417792792": {
            "samples": [0.06206030150753769] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8466050899616508040": {
            "samples": [0.06206030150753769] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "798695843094957671": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8775866437911941090": {
            "samples": [0.06206030150753769] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6229221612067706891": {
            "samples": [0.06206030150753769] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2549723669063112367": {
            "samples": [0.06206030150753769] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2328229609864397119": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6543952182838255736": {
            "samples": [0.06206030150753769] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-130469921861230256": {
            "samples": [0.06206030150753769] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5821599335145307694": {
            "samples": [0.06206030150753769] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5102739895165534090": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "2750374226403239870": {
            "samples": [0.06206030150753769] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8143319410254109745": {
            "samples": [0.06206030150753769] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7521993642367416201": {
            "samples": [0.06206030150753769] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2719221142115143636": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-8339212519965859766": {
            "samples": [0.06206030150753769] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8699605476431743418": {
            "samples": [0.06206030150753769] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1747396283757572714": {
            "samples": [0.06206030150753769] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5554568190000196365": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6980606100784337060": {
            "samples": [0.06206030150753769] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7752327878003363228": {
            "samples": [0.06206030150753769] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2303682349935206387": {
            "samples": [0.06206030150753769] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5461206378679424042": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-5239712319480708794": {
            "samples": [0.06206030150753769] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5013180648417117224": {
            "samples": [0.06206030150753769] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2688622566330280771": {
            "samples": [0.06206030150753769] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7210940336420284087": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "6589614568533590543": {
            "samples": [0.06206030150753769] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6811108627732305791": {
            "samples": [0.06206030150753769] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8816549990087385418": {
            "samples": [0.06206030150753769] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8105657943150624388": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-3583340173060621072": {
            "samples": [0.06206030150753769] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4204665940947314616": {
            "samples": [0.06206030150753769] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1385580485057454209": {
            "samples": [0.06206030150753769] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1164086425858738961": {
            "sample": 0.06206030150753769,
            "type": "constant",
        },
        "-453194378921977931": {
            "samples": [0.06206030150753769] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4069123391168025385": {
            "samples": [0.06206030150753769] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1744565309081188932": {
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
        "B4/acquisition_mixer_fe2": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_487": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_bdb": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_13d": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

