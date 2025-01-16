
# Single QUA script generated at 2025-01-16 15:53:42.168775
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("B1/flux", "single", 0.0)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", -0.2819)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.0307)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", -0.215)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", 0.074)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("7486520634526729781", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25543, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("2657594562879384896", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25543, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("8843859636062151126", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25542, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("5150599106988371531", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25542, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("1230275248095599043", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25542, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-5512545214622774154", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25542, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-7002359249854448342", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25541, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("96482100241433256", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25541, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-8225656597109838988", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25541, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-1534544876453235045", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25541, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-3937958160746610786", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-521707544249232035", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-6444273424251965355", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("492463776538445301", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-8630282338244638776", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-2103723271771334563", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("9005116971165685004", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-8156420553861526650", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("1985210475711626692", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-6160431722937319948", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("654130572277225187", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-954791899585264511", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-7320845413615993179", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("7969968384514319356", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("1322827905238535397", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-6038835662606201973", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-6783433932331211436", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("6637151298710188493", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        play("4845371154455186662", "B4/drive")
        wait(11, "B4/flux")
        play("-8895499251000749663", "B4/flux")
        wait(48, "B4/drive")
        play("5606461783678748531", "B4/drive")
        wait(68, "B4/acquisition")
        measure("-76292095156635255", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.4386401275063697)-(v3*-0.8986628058071591))>0.0021321279781268726)))
        save(v4, r1)
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(29).average().save("-76292095156635255_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": -0.2819,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                    "offset": 0.21674190528643072,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
                "7": {
                    "offset": -0.04,
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
            },
            "digital_outputs": {
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
    },
    "octaves": {
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "4": {
                    "LO_frequency": 6700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
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
                    "output_mode": "always_on",
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
                "7486520634526729781": "7486520634526729781",
                "2657594562879384896": "2657594562879384896",
                "8843859636062151126": "8843859636062151126",
                "5150599106988371531": "5150599106988371531",
                "1230275248095599043": "1230275248095599043",
                "-5512545214622774154": "-5512545214622774154",
                "-7002359249854448342": "-7002359249854448342",
                "96482100241433256": "96482100241433256",
                "-8225656597109838988": "-8225656597109838988",
                "-1534544876453235045": "-1534544876453235045",
                "-3937958160746610786": "-3937958160746610786",
                "-521707544249232035": "-521707544249232035",
                "-6444273424251965355": "-6444273424251965355",
                "492463776538445301": "492463776538445301",
                "-8630282338244638776": "-8630282338244638776",
                "-2103723271771334563": "-2103723271771334563",
                "9005116971165685004": "9005116971165685004",
                "-8156420553861526650": "-8156420553861526650",
                "1985210475711626692": "1985210475711626692",
                "-6160431722937319948": "-6160431722937319948",
                "654130572277225187": "654130572277225187",
                "-954791899585264511": "-954791899585264511",
                "-7320845413615993179": "-7320845413615993179",
                "7969968384514319356": "7969968384514319356",
                "1322827905238535397": "1322827905238535397",
                "-6038835662606201973": "-6038835662606201973",
                "-6783433932331211436": "-6783433932331211436",
                "6637151298710188493": "6637151298710188493",
                "-8895499251000749663": "-8895499251000749663",
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
            "intermediate_frequency": 109610828.0,
            "operations": {
                "4845371154455186662": "4845371154455186662",
                "5606461783678748531": "5606461783678748531",
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
            "intermediate_frequency": 331181947.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-76292095156635255": "-76292095156635255_B4/acquisition",
            },
        },
    },
    "pulses": {
        "4845371154455186662": {
            "length": 40,
            "waveforms": {
                "I": "4845371154455186662_i",
                "Q": "4845371154455186662_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3183662398059091062": {
            "length": 16,
            "waveforms": {
                "single": "3183662398059091062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-76292095156635255_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "470019394525969398_i",
                "Q": "470019394525969398_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "1060737537195055258": {
            "length": 16,
            "waveforms": {
                "single": "1060737537195055258",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2059281341141883849": {
            "length": 16,
            "waveforms": {
                "single": "2059281341141883849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8756002260869894824": {
            "length": 16,
            "waveforms": {
                "single": "-8756002260869894824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5447233159339037181": {
            "length": 16,
            "waveforms": {
                "single": "-5447233159339037181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5303390326643074996": {
            "length": 16,
            "waveforms": {
                "single": "-5303390326643074996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3576045684747295599": {
            "length": 16,
            "waveforms": {
                "single": "-3576045684747295599",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8472867356493647312": {
            "length": 16,
            "waveforms": {
                "single": "8472867356493647312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2524924983582036775": {
            "length": 16,
            "waveforms": {
                "single": "2524924983582036775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5680759364837477734": {
            "length": 16,
            "waveforms": {
                "single": "-5680759364837477734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-271136562231703027": {
            "length": 16,
            "waveforms": {
                "single": "-271136562231703027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4549424867273519088": {
            "length": 16,
            "waveforms": {
                "single": "-4549424867273519088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5720542171150090589": {
            "length": 16,
            "waveforms": {
                "single": "5720542171150090589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3941693234563711464": {
            "length": 16,
            "waveforms": {
                "single": "-3941693234563711464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7636871904771018290": {
            "length": 16,
            "waveforms": {
                "single": "-7636871904771018290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5163725021915996291": {
            "length": 16,
            "waveforms": {
                "single": "-5163725021915996291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8471694434410857331": {
            "length": 20,
            "waveforms": {
                "single": "8471694434410857331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8815426893500028453": {
            "length": 20,
            "waveforms": {
                "single": "-8815426893500028453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1462552356064619180": {
            "length": 20,
            "waveforms": {
                "single": "-1462552356064619180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "192065577273318195": {
            "length": 20,
            "waveforms": {
                "single": "192065577273318195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4827564202784850780": {
            "length": 24,
            "waveforms": {
                "single": "4827564202784850780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8909513788053215613": {
            "length": 24,
            "waveforms": {
                "single": "8909513788053215613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8215254324112054387": {
            "length": 24,
            "waveforms": {
                "single": "8215254324112054387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2635080641667123478": {
            "length": 24,
            "waveforms": {
                "single": "-2635080641667123478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4933822221188359570": {
            "length": 28,
            "waveforms": {
                "single": "4933822221188359570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4341908129969287516": {
            "length": 28,
            "waveforms": {
                "single": "4341908129969287516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8753071850622700662": {
            "length": 28,
            "waveforms": {
                "single": "-8753071850622700662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7123985727177518862": {
            "length": 28,
            "waveforms": {
                "single": "-7123985727177518862",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3419200428639479608": {
            "length": 32,
            "waveforms": {
                "single": "3419200428639479608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7260850467623596773": {
            "length": 32,
            "waveforms": {
                "single": "7260850467623596773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1250375873957854942": {
            "length": 32,
            "waveforms": {
                "single": "1250375873957854942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4810319602005962851": {
            "length": 32,
            "waveforms": {
                "single": "-4810319602005962851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5098489606566732910": {
            "length": 36,
            "waveforms": {
                "single": "5098489606566732910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8085691332162123442": {
            "length": 36,
            "waveforms": {
                "single": "-8085691332162123442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5194724601970029446": {
            "length": 36,
            "waveforms": {
                "single": "5194724601970029446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3667399088157528442": {
            "length": 36,
            "waveforms": {
                "single": "3667399088157528442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7412259691525004119": {
            "length": 40,
            "waveforms": {
                "single": "-7412259691525004119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-374265821259382674": {
            "length": 40,
            "waveforms": {
                "single": "-374265821259382674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4866459310146265138": {
            "length": 40,
            "waveforms": {
                "single": "4866459310146265138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2135668750822087713": {
            "length": 40,
            "waveforms": {
                "single": "2135668750822087713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9155740100547697436": {
            "length": 44,
            "waveforms": {
                "single": "9155740100547697436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8983903290695897574": {
            "length": 44,
            "waveforms": {
                "single": "8983903290695897574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2676427951707768256": {
            "length": 44,
            "waveforms": {
                "single": "-2676427951707768256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6799840650038139500": {
            "length": 44,
            "waveforms": {
                "single": "6799840650038139500",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "962300600609977339": {
            "length": 48,
            "waveforms": {
                "single": "962300600609977339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6468676661435153631": {
            "length": 48,
            "waveforms": {
                "single": "6468676661435153631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "468931381419504790": {
            "length": 48,
            "waveforms": {
                "single": "468931381419504790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5519445318413340332": {
            "length": 48,
            "waveforms": {
                "single": "5519445318413340332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5242790333634856348": {
            "length": 52,
            "waveforms": {
                "single": "5242790333634856348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5134488659968018802": {
            "length": 52,
            "waveforms": {
                "single": "-5134488659968018802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3317762871321317672": {
            "length": 52,
            "waveforms": {
                "single": "-3317762871321317672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8175511706546982060": {
            "length": 52,
            "waveforms": {
                "single": "-8175511706546982060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2547573945093641047": {
            "length": 56,
            "waveforms": {
                "single": "2547573945093641047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9045588634490840874": {
            "length": 56,
            "waveforms": {
                "single": "9045588634490840874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8746087400563170055": {
            "length": 56,
            "waveforms": {
                "single": "-8746087400563170055",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5647338197385438741": {
            "length": 56,
            "waveforms": {
                "single": "-5647338197385438741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7931396866004104526": {
            "length": 60,
            "waveforms": {
                "single": "-7931396866004104526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1738419052934074322": {
            "length": 60,
            "waveforms": {
                "single": "1738419052934074322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6772162550812364356": {
            "length": 60,
            "waveforms": {
                "single": "6772162550812364356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6297918820223333855": {
            "length": 60,
            "waveforms": {
                "single": "6297918820223333855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7486520634526729781": {
            "length": 64,
            "waveforms": {
                "single": "7486520634526729781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2657594562879384896": {
            "length": 64,
            "waveforms": {
                "single": "2657594562879384896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8843859636062151126": {
            "length": 64,
            "waveforms": {
                "single": "8843859636062151126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5150599106988371531": {
            "length": 64,
            "waveforms": {
                "single": "5150599106988371531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1230275248095599043": {
            "length": 68,
            "waveforms": {
                "single": "1230275248095599043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5512545214622774154": {
            "length": 68,
            "waveforms": {
                "single": "-5512545214622774154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7002359249854448342": {
            "length": 68,
            "waveforms": {
                "single": "-7002359249854448342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "96482100241433256": {
            "length": 68,
            "waveforms": {
                "single": "96482100241433256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8225656597109838988": {
            "length": 72,
            "waveforms": {
                "single": "-8225656597109838988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1534544876453235045": {
            "length": 72,
            "waveforms": {
                "single": "-1534544876453235045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3937958160746610786": {
            "length": 72,
            "waveforms": {
                "single": "-3937958160746610786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-521707544249232035": {
            "length": 72,
            "waveforms": {
                "single": "-521707544249232035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6444273424251965355": {
            "length": 76,
            "waveforms": {
                "single": "-6444273424251965355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "492463776538445301": {
            "length": 76,
            "waveforms": {
                "single": "492463776538445301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8630282338244638776": {
            "length": 76,
            "waveforms": {
                "single": "-8630282338244638776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2103723271771334563": {
            "length": 76,
            "waveforms": {
                "single": "-2103723271771334563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9005116971165685004": {
            "length": 80,
            "waveforms": {
                "single": "9005116971165685004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8156420553861526650": {
            "length": 80,
            "waveforms": {
                "single": "-8156420553861526650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1985210475711626692": {
            "length": 80,
            "waveforms": {
                "single": "1985210475711626692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6160431722937319948": {
            "length": 80,
            "waveforms": {
                "single": "-6160431722937319948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "654130572277225187": {
            "length": 84,
            "waveforms": {
                "single": "654130572277225187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-954791899585264511": {
            "length": 84,
            "waveforms": {
                "single": "-954791899585264511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7320845413615993179": {
            "length": 84,
            "waveforms": {
                "single": "-7320845413615993179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7969968384514319356": {
            "length": 84,
            "waveforms": {
                "single": "7969968384514319356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1322827905238535397": {
            "length": 88,
            "waveforms": {
                "single": "1322827905238535397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6038835662606201973": {
            "length": 88,
            "waveforms": {
                "single": "-6038835662606201973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6783433932331211436": {
            "length": 88,
            "waveforms": {
                "single": "-6783433932331211436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6637151298710188493": {
            "length": 88,
            "waveforms": {
                "single": "6637151298710188493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8895499251000749663": {
            "length": 92,
            "waveforms": {
                "single": "-8895499251000749663",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5606461783678748531": {
            "length": 40,
            "waveforms": {
                "I": "5606461783678748531_i",
                "Q": "5606461783678748531_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "4845371154455186662_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
        },
        "4845371154455186662_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "3183662398059091062": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "470019394525969398_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "470019394525969398_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1060737537195055258": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2059281341141883849": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8756002260869894824": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5447233159339037181": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5303390326643074996": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-3576045684747295599": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8472867356493647312": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2524924983582036775": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5680759364837477734": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-271136562231703027": {
            "samples": [0.0] * 10 + [0.3] + [0.0] * 5,
            "type": "arbitrary",
        },
        "-4549424867273519088": {
            "samples": [0.0] * 10 + [0.3] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "5720542171150090589": {
            "samples": [0.0] * 10 + [0.3] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3941693234563711464": {
            "samples": [0.0] * 10 + [0.3] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7636871904771018290": {
            "samples": [0.0] * 10 + [0.3] * 5 + [0.0],
            "type": "arbitrary",
        },
        "-5163725021915996291": {
            "samples": [0.0] * 10 + [0.3] * 6,
            "type": "arbitrary",
        },
        "8471694434410857331": {
            "samples": [0.0] * 10 + [0.3] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8815426893500028453": {
            "samples": [0.0] * 10 + [0.3] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1462552356064619180": {
            "samples": [0.0] * 10 + [0.3] * 9 + [0.0],
            "type": "arbitrary",
        },
        "192065577273318195": {
            "samples": [0.0] * 10 + [0.3] * 10,
            "type": "arbitrary",
        },
        "4827564202784850780": {
            "samples": [0.0] * 10 + [0.3] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8909513788053215613": {
            "samples": [0.0] * 10 + [0.3] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8215254324112054387": {
            "samples": [0.0] * 10 + [0.3] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-2635080641667123478": {
            "samples": [0.0] * 10 + [0.3] * 14,
            "type": "arbitrary",
        },
        "4933822221188359570": {
            "samples": [0.0] * 10 + [0.3] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4341908129969287516": {
            "samples": [0.0] * 10 + [0.3] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8753071850622700662": {
            "samples": [0.0] * 10 + [0.3] * 17 + [0.0],
            "type": "arbitrary",
        },
        "-7123985727177518862": {
            "samples": [0.0] * 10 + [0.3] * 18,
            "type": "arbitrary",
        },
        "3419200428639479608": {
            "samples": [0.0] * 10 + [0.3] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7260850467623596773": {
            "samples": [0.0] * 10 + [0.3] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1250375873957854942": {
            "samples": [0.0] * 10 + [0.3] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-4810319602005962851": {
            "samples": [0.0] * 10 + [0.3] * 22,
            "type": "arbitrary",
        },
        "5098489606566732910": {
            "samples": [0.0] * 10 + [0.3] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8085691332162123442": {
            "samples": [0.0] * 10 + [0.3] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5194724601970029446": {
            "samples": [0.0] * 10 + [0.3] * 25 + [0.0],
            "type": "arbitrary",
        },
        "3667399088157528442": {
            "samples": [0.0] * 10 + [0.3] * 26,
            "type": "arbitrary",
        },
        "-7412259691525004119": {
            "samples": [0.0] * 10 + [0.3] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-374265821259382674": {
            "samples": [0.0] * 10 + [0.3] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4866459310146265138": {
            "samples": [0.0] * 10 + [0.3] * 29 + [0.0],
            "type": "arbitrary",
        },
        "2135668750822087713": {
            "samples": [0.0] * 10 + [0.3] * 30,
            "type": "arbitrary",
        },
        "9155740100547697436": {
            "samples": [0.0] * 10 + [0.3] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8983903290695897574": {
            "samples": [0.0] * 10 + [0.3] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2676427951707768256": {
            "samples": [0.0] * 10 + [0.3] * 33 + [0.0],
            "type": "arbitrary",
        },
        "6799840650038139500": {
            "samples": [0.0] * 10 + [0.3] * 34,
            "type": "arbitrary",
        },
        "962300600609977339": {
            "samples": [0.0] * 10 + [0.3] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6468676661435153631": {
            "samples": [0.0] * 10 + [0.3] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "468931381419504790": {
            "samples": [0.0] * 10 + [0.3] * 37 + [0.0],
            "type": "arbitrary",
        },
        "5519445318413340332": {
            "samples": [0.0] * 10 + [0.3] * 38,
            "type": "arbitrary",
        },
        "5242790333634856348": {
            "samples": [0.0] * 10 + [0.3] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5134488659968018802": {
            "samples": [0.0] * 10 + [0.3] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3317762871321317672": {
            "samples": [0.0] * 10 + [0.3] * 41 + [0.0],
            "type": "arbitrary",
        },
        "-8175511706546982060": {
            "samples": [0.0] * 10 + [0.3] * 42,
            "type": "arbitrary",
        },
        "2547573945093641047": {
            "samples": [0.0] * 10 + [0.3] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9045588634490840874": {
            "samples": [0.0] * 10 + [0.3] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8746087400563170055": {
            "samples": [0.0] * 10 + [0.3] * 45 + [0.0],
            "type": "arbitrary",
        },
        "-5647338197385438741": {
            "samples": [0.0] * 10 + [0.3] * 46,
            "type": "arbitrary",
        },
        "-7931396866004104526": {
            "samples": [0.0] * 10 + [0.3] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1738419052934074322": {
            "samples": [0.0] * 10 + [0.3] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6772162550812364356": {
            "samples": [0.0] * 10 + [0.3] * 49 + [0.0],
            "type": "arbitrary",
        },
        "6297918820223333855": {
            "samples": [0.0] * 10 + [0.3] * 50,
            "type": "arbitrary",
        },
        "7486520634526729781": {
            "samples": [0.0] * 10 + [0.3] * 51 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2657594562879384896": {
            "samples": [0.0] * 10 + [0.3] * 52 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8843859636062151126": {
            "samples": [0.0] * 10 + [0.3] * 53 + [0.0],
            "type": "arbitrary",
        },
        "5150599106988371531": {
            "samples": [0.0] * 10 + [0.3] * 54,
            "type": "arbitrary",
        },
        "1230275248095599043": {
            "samples": [0.0] * 10 + [0.3] * 55 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5512545214622774154": {
            "samples": [0.0] * 10 + [0.3] * 56 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7002359249854448342": {
            "samples": [0.0] * 10 + [0.3] * 57 + [0.0],
            "type": "arbitrary",
        },
        "96482100241433256": {
            "samples": [0.0] * 10 + [0.3] * 58,
            "type": "arbitrary",
        },
        "-8225656597109838988": {
            "samples": [0.0] * 10 + [0.3] * 59 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1534544876453235045": {
            "samples": [0.0] * 10 + [0.3] * 60 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3937958160746610786": {
            "samples": [0.0] * 10 + [0.3] * 61 + [0.0],
            "type": "arbitrary",
        },
        "-521707544249232035": {
            "samples": [0.0] * 10 + [0.3] * 62,
            "type": "arbitrary",
        },
        "-6444273424251965355": {
            "samples": [0.0] * 10 + [0.3] * 63 + [0.0] * 3,
            "type": "arbitrary",
        },
        "492463776538445301": {
            "samples": [0.0] * 10 + [0.3] * 64 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8630282338244638776": {
            "samples": [0.0] * 10 + [0.3] * 65 + [0.0],
            "type": "arbitrary",
        },
        "-2103723271771334563": {
            "samples": [0.0] * 10 + [0.3] * 66,
            "type": "arbitrary",
        },
        "9005116971165685004": {
            "samples": [0.0] * 10 + [0.3] * 67 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8156420553861526650": {
            "samples": [0.0] * 10 + [0.3] * 68 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1985210475711626692": {
            "samples": [0.0] * 10 + [0.3] * 69 + [0.0],
            "type": "arbitrary",
        },
        "-6160431722937319948": {
            "samples": [0.0] * 10 + [0.3] * 70,
            "type": "arbitrary",
        },
        "654130572277225187": {
            "samples": [0.0] * 10 + [0.3] * 71 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-954791899585264511": {
            "samples": [0.0] * 10 + [0.3] * 72 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7320845413615993179": {
            "samples": [0.0] * 10 + [0.3] * 73 + [0.0],
            "type": "arbitrary",
        },
        "7969968384514319356": {
            "samples": [0.0] * 10 + [0.3] * 74,
            "type": "arbitrary",
        },
        "1322827905238535397": {
            "samples": [0.0] * 10 + [0.3] * 75 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6038835662606201973": {
            "samples": [0.0] * 10 + [0.3] * 76 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6783433932331211436": {
            "samples": [0.0] * 10 + [0.3] * 77 + [0.0],
            "type": "arbitrary",
        },
        "6637151298710188493": {
            "samples": [0.0] * 10 + [0.3] * 78,
            "type": "arbitrary",
        },
        "-8895499251000749663": {
            "samples": [0.0] * 10 + [0.3] * 79 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5606461783678748531_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "5606461783678748531_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
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
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": -0.2819,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                    "offset": 0.21674190528643072,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": -0.04,
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
                "7486520634526729781": "7486520634526729781",
                "2657594562879384896": "2657594562879384896",
                "8843859636062151126": "8843859636062151126",
                "5150599106988371531": "5150599106988371531",
                "1230275248095599043": "1230275248095599043",
                "-5512545214622774154": "-5512545214622774154",
                "-7002359249854448342": "-7002359249854448342",
                "96482100241433256": "96482100241433256",
                "-8225656597109838988": "-8225656597109838988",
                "-1534544876453235045": "-1534544876453235045",
                "-3937958160746610786": "-3937958160746610786",
                "-521707544249232035": "-521707544249232035",
                "-6444273424251965355": "-6444273424251965355",
                "492463776538445301": "492463776538445301",
                "-8630282338244638776": "-8630282338244638776",
                "-2103723271771334563": "-2103723271771334563",
                "9005116971165685004": "9005116971165685004",
                "-8156420553861526650": "-8156420553861526650",
                "1985210475711626692": "1985210475711626692",
                "-6160431722937319948": "-6160431722937319948",
                "654130572277225187": "654130572277225187",
                "-954791899585264511": "-954791899585264511",
                "-7320845413615993179": "-7320845413615993179",
                "7969968384514319356": "7969968384514319356",
                "1322827905238535397": "1322827905238535397",
                "-6038835662606201973": "-6038835662606201973",
                "-6783433932331211436": "-6783433932331211436",
                "6637151298710188493": "6637151298710188493",
                "-8895499251000749663": "-8895499251000749663",
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
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109610828.0,
            "operations": {
                "4845371154455186662": "4845371154455186662",
                "5606461783678748531": "5606461783678748531",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_84b",
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
            "intermediate_frequency": 331181947.0,
            "operations": {
                "-76292095156635255": "-76292095156635255_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_1f9",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "4845371154455186662": {
            "length": 40,
            "waveforms": {
                "I": "4845371154455186662_i",
                "Q": "4845371154455186662_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3183662398059091062": {
            "length": 16,
            "waveforms": {
                "single": "3183662398059091062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-76292095156635255_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "470019394525969398_i",
                "Q": "470019394525969398_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "1060737537195055258": {
            "length": 16,
            "waveforms": {
                "single": "1060737537195055258",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2059281341141883849": {
            "length": 16,
            "waveforms": {
                "single": "2059281341141883849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8756002260869894824": {
            "length": 16,
            "waveforms": {
                "single": "-8756002260869894824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5447233159339037181": {
            "length": 16,
            "waveforms": {
                "single": "-5447233159339037181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5303390326643074996": {
            "length": 16,
            "waveforms": {
                "single": "-5303390326643074996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3576045684747295599": {
            "length": 16,
            "waveforms": {
                "single": "-3576045684747295599",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8472867356493647312": {
            "length": 16,
            "waveforms": {
                "single": "8472867356493647312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2524924983582036775": {
            "length": 16,
            "waveforms": {
                "single": "2524924983582036775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5680759364837477734": {
            "length": 16,
            "waveforms": {
                "single": "-5680759364837477734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-271136562231703027": {
            "length": 16,
            "waveforms": {
                "single": "-271136562231703027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4549424867273519088": {
            "length": 16,
            "waveforms": {
                "single": "-4549424867273519088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5720542171150090589": {
            "length": 16,
            "waveforms": {
                "single": "5720542171150090589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3941693234563711464": {
            "length": 16,
            "waveforms": {
                "single": "-3941693234563711464",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7636871904771018290": {
            "length": 16,
            "waveforms": {
                "single": "-7636871904771018290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5163725021915996291": {
            "length": 16,
            "waveforms": {
                "single": "-5163725021915996291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8471694434410857331": {
            "length": 20,
            "waveforms": {
                "single": "8471694434410857331",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8815426893500028453": {
            "length": 20,
            "waveforms": {
                "single": "-8815426893500028453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1462552356064619180": {
            "length": 20,
            "waveforms": {
                "single": "-1462552356064619180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "192065577273318195": {
            "length": 20,
            "waveforms": {
                "single": "192065577273318195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4827564202784850780": {
            "length": 24,
            "waveforms": {
                "single": "4827564202784850780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8909513788053215613": {
            "length": 24,
            "waveforms": {
                "single": "8909513788053215613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8215254324112054387": {
            "length": 24,
            "waveforms": {
                "single": "8215254324112054387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2635080641667123478": {
            "length": 24,
            "waveforms": {
                "single": "-2635080641667123478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4933822221188359570": {
            "length": 28,
            "waveforms": {
                "single": "4933822221188359570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4341908129969287516": {
            "length": 28,
            "waveforms": {
                "single": "4341908129969287516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8753071850622700662": {
            "length": 28,
            "waveforms": {
                "single": "-8753071850622700662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7123985727177518862": {
            "length": 28,
            "waveforms": {
                "single": "-7123985727177518862",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3419200428639479608": {
            "length": 32,
            "waveforms": {
                "single": "3419200428639479608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7260850467623596773": {
            "length": 32,
            "waveforms": {
                "single": "7260850467623596773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1250375873957854942": {
            "length": 32,
            "waveforms": {
                "single": "1250375873957854942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4810319602005962851": {
            "length": 32,
            "waveforms": {
                "single": "-4810319602005962851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5098489606566732910": {
            "length": 36,
            "waveforms": {
                "single": "5098489606566732910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8085691332162123442": {
            "length": 36,
            "waveforms": {
                "single": "-8085691332162123442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5194724601970029446": {
            "length": 36,
            "waveforms": {
                "single": "5194724601970029446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3667399088157528442": {
            "length": 36,
            "waveforms": {
                "single": "3667399088157528442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7412259691525004119": {
            "length": 40,
            "waveforms": {
                "single": "-7412259691525004119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-374265821259382674": {
            "length": 40,
            "waveforms": {
                "single": "-374265821259382674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4866459310146265138": {
            "length": 40,
            "waveforms": {
                "single": "4866459310146265138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2135668750822087713": {
            "length": 40,
            "waveforms": {
                "single": "2135668750822087713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9155740100547697436": {
            "length": 44,
            "waveforms": {
                "single": "9155740100547697436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8983903290695897574": {
            "length": 44,
            "waveforms": {
                "single": "8983903290695897574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2676427951707768256": {
            "length": 44,
            "waveforms": {
                "single": "-2676427951707768256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6799840650038139500": {
            "length": 44,
            "waveforms": {
                "single": "6799840650038139500",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "962300600609977339": {
            "length": 48,
            "waveforms": {
                "single": "962300600609977339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6468676661435153631": {
            "length": 48,
            "waveforms": {
                "single": "6468676661435153631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "468931381419504790": {
            "length": 48,
            "waveforms": {
                "single": "468931381419504790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5519445318413340332": {
            "length": 48,
            "waveforms": {
                "single": "5519445318413340332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5242790333634856348": {
            "length": 52,
            "waveforms": {
                "single": "5242790333634856348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5134488659968018802": {
            "length": 52,
            "waveforms": {
                "single": "-5134488659968018802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3317762871321317672": {
            "length": 52,
            "waveforms": {
                "single": "-3317762871321317672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8175511706546982060": {
            "length": 52,
            "waveforms": {
                "single": "-8175511706546982060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2547573945093641047": {
            "length": 56,
            "waveforms": {
                "single": "2547573945093641047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9045588634490840874": {
            "length": 56,
            "waveforms": {
                "single": "9045588634490840874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8746087400563170055": {
            "length": 56,
            "waveforms": {
                "single": "-8746087400563170055",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5647338197385438741": {
            "length": 56,
            "waveforms": {
                "single": "-5647338197385438741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7931396866004104526": {
            "length": 60,
            "waveforms": {
                "single": "-7931396866004104526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1738419052934074322": {
            "length": 60,
            "waveforms": {
                "single": "1738419052934074322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6772162550812364356": {
            "length": 60,
            "waveforms": {
                "single": "6772162550812364356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6297918820223333855": {
            "length": 60,
            "waveforms": {
                "single": "6297918820223333855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7486520634526729781": {
            "length": 64,
            "waveforms": {
                "single": "7486520634526729781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2657594562879384896": {
            "length": 64,
            "waveforms": {
                "single": "2657594562879384896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8843859636062151126": {
            "length": 64,
            "waveforms": {
                "single": "8843859636062151126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5150599106988371531": {
            "length": 64,
            "waveforms": {
                "single": "5150599106988371531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1230275248095599043": {
            "length": 68,
            "waveforms": {
                "single": "1230275248095599043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5512545214622774154": {
            "length": 68,
            "waveforms": {
                "single": "-5512545214622774154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7002359249854448342": {
            "length": 68,
            "waveforms": {
                "single": "-7002359249854448342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "96482100241433256": {
            "length": 68,
            "waveforms": {
                "single": "96482100241433256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8225656597109838988": {
            "length": 72,
            "waveforms": {
                "single": "-8225656597109838988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1534544876453235045": {
            "length": 72,
            "waveforms": {
                "single": "-1534544876453235045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3937958160746610786": {
            "length": 72,
            "waveforms": {
                "single": "-3937958160746610786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-521707544249232035": {
            "length": 72,
            "waveforms": {
                "single": "-521707544249232035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6444273424251965355": {
            "length": 76,
            "waveforms": {
                "single": "-6444273424251965355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "492463776538445301": {
            "length": 76,
            "waveforms": {
                "single": "492463776538445301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8630282338244638776": {
            "length": 76,
            "waveforms": {
                "single": "-8630282338244638776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2103723271771334563": {
            "length": 76,
            "waveforms": {
                "single": "-2103723271771334563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9005116971165685004": {
            "length": 80,
            "waveforms": {
                "single": "9005116971165685004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8156420553861526650": {
            "length": 80,
            "waveforms": {
                "single": "-8156420553861526650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1985210475711626692": {
            "length": 80,
            "waveforms": {
                "single": "1985210475711626692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6160431722937319948": {
            "length": 80,
            "waveforms": {
                "single": "-6160431722937319948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "654130572277225187": {
            "length": 84,
            "waveforms": {
                "single": "654130572277225187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-954791899585264511": {
            "length": 84,
            "waveforms": {
                "single": "-954791899585264511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7320845413615993179": {
            "length": 84,
            "waveforms": {
                "single": "-7320845413615993179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7969968384514319356": {
            "length": 84,
            "waveforms": {
                "single": "7969968384514319356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1322827905238535397": {
            "length": 88,
            "waveforms": {
                "single": "1322827905238535397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6038835662606201973": {
            "length": 88,
            "waveforms": {
                "single": "-6038835662606201973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6783433932331211436": {
            "length": 88,
            "waveforms": {
                "single": "-6783433932331211436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6637151298710188493": {
            "length": 88,
            "waveforms": {
                "single": "6637151298710188493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8895499251000749663": {
            "length": 92,
            "waveforms": {
                "single": "-8895499251000749663",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5606461783678748531": {
            "length": 40,
            "waveforms": {
                "I": "5606461783678748531_i",
                "Q": "5606461783678748531_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "4845371154455186662_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4845371154455186662_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3183662398059091062": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "470019394525969398_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "470019394525969398_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1060737537195055258": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2059281341141883849": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8756002260869894824": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5447233159339037181": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5303390326643074996": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3576045684747295599": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8472867356493647312": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2524924983582036775": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5680759364837477734": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-271136562231703027": {
            "samples": [0.0] * 10 + [0.3] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4549424867273519088": {
            "samples": [0.0] * 10 + [0.3] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5720542171150090589": {
            "samples": [0.0] * 10 + [0.3] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3941693234563711464": {
            "samples": [0.0] * 10 + [0.3] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7636871904771018290": {
            "samples": [0.0] * 10 + [0.3] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5163725021915996291": {
            "samples": [0.0] * 10 + [0.3] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8471694434410857331": {
            "samples": [0.0] * 10 + [0.3] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8815426893500028453": {
            "samples": [0.0] * 10 + [0.3] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1462552356064619180": {
            "samples": [0.0] * 10 + [0.3] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "192065577273318195": {
            "samples": [0.0] * 10 + [0.3] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4827564202784850780": {
            "samples": [0.0] * 10 + [0.3] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8909513788053215613": {
            "samples": [0.0] * 10 + [0.3] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8215254324112054387": {
            "samples": [0.0] * 10 + [0.3] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2635080641667123478": {
            "samples": [0.0] * 10 + [0.3] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4933822221188359570": {
            "samples": [0.0] * 10 + [0.3] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4341908129969287516": {
            "samples": [0.0] * 10 + [0.3] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8753071850622700662": {
            "samples": [0.0] * 10 + [0.3] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7123985727177518862": {
            "samples": [0.0] * 10 + [0.3] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3419200428639479608": {
            "samples": [0.0] * 10 + [0.3] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7260850467623596773": {
            "samples": [0.0] * 10 + [0.3] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1250375873957854942": {
            "samples": [0.0] * 10 + [0.3] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4810319602005962851": {
            "samples": [0.0] * 10 + [0.3] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5098489606566732910": {
            "samples": [0.0] * 10 + [0.3] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8085691332162123442": {
            "samples": [0.0] * 10 + [0.3] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5194724601970029446": {
            "samples": [0.0] * 10 + [0.3] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3667399088157528442": {
            "samples": [0.0] * 10 + [0.3] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7412259691525004119": {
            "samples": [0.0] * 10 + [0.3] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-374265821259382674": {
            "samples": [0.0] * 10 + [0.3] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4866459310146265138": {
            "samples": [0.0] * 10 + [0.3] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2135668750822087713": {
            "samples": [0.0] * 10 + [0.3] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9155740100547697436": {
            "samples": [0.0] * 10 + [0.3] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8983903290695897574": {
            "samples": [0.0] * 10 + [0.3] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2676427951707768256": {
            "samples": [0.0] * 10 + [0.3] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6799840650038139500": {
            "samples": [0.0] * 10 + [0.3] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "962300600609977339": {
            "samples": [0.0] * 10 + [0.3] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6468676661435153631": {
            "samples": [0.0] * 10 + [0.3] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "468931381419504790": {
            "samples": [0.0] * 10 + [0.3] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5519445318413340332": {
            "samples": [0.0] * 10 + [0.3] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5242790333634856348": {
            "samples": [0.0] * 10 + [0.3] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5134488659968018802": {
            "samples": [0.0] * 10 + [0.3] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3317762871321317672": {
            "samples": [0.0] * 10 + [0.3] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8175511706546982060": {
            "samples": [0.0] * 10 + [0.3] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2547573945093641047": {
            "samples": [0.0] * 10 + [0.3] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9045588634490840874": {
            "samples": [0.0] * 10 + [0.3] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8746087400563170055": {
            "samples": [0.0] * 10 + [0.3] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5647338197385438741": {
            "samples": [0.0] * 10 + [0.3] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7931396866004104526": {
            "samples": [0.0] * 10 + [0.3] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1738419052934074322": {
            "samples": [0.0] * 10 + [0.3] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6772162550812364356": {
            "samples": [0.0] * 10 + [0.3] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6297918820223333855": {
            "samples": [0.0] * 10 + [0.3] * 50,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7486520634526729781": {
            "samples": [0.0] * 10 + [0.3] * 51 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2657594562879384896": {
            "samples": [0.0] * 10 + [0.3] * 52 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8843859636062151126": {
            "samples": [0.0] * 10 + [0.3] * 53 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5150599106988371531": {
            "samples": [0.0] * 10 + [0.3] * 54,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1230275248095599043": {
            "samples": [0.0] * 10 + [0.3] * 55 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5512545214622774154": {
            "samples": [0.0] * 10 + [0.3] * 56 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7002359249854448342": {
            "samples": [0.0] * 10 + [0.3] * 57 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "96482100241433256": {
            "samples": [0.0] * 10 + [0.3] * 58,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8225656597109838988": {
            "samples": [0.0] * 10 + [0.3] * 59 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1534544876453235045": {
            "samples": [0.0] * 10 + [0.3] * 60 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3937958160746610786": {
            "samples": [0.0] * 10 + [0.3] * 61 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-521707544249232035": {
            "samples": [0.0] * 10 + [0.3] * 62,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6444273424251965355": {
            "samples": [0.0] * 10 + [0.3] * 63 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "492463776538445301": {
            "samples": [0.0] * 10 + [0.3] * 64 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8630282338244638776": {
            "samples": [0.0] * 10 + [0.3] * 65 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2103723271771334563": {
            "samples": [0.0] * 10 + [0.3] * 66,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9005116971165685004": {
            "samples": [0.0] * 10 + [0.3] * 67 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8156420553861526650": {
            "samples": [0.0] * 10 + [0.3] * 68 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1985210475711626692": {
            "samples": [0.0] * 10 + [0.3] * 69 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6160431722937319948": {
            "samples": [0.0] * 10 + [0.3] * 70,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "654130572277225187": {
            "samples": [0.0] * 10 + [0.3] * 71 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-954791899585264511": {
            "samples": [0.0] * 10 + [0.3] * 72 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7320845413615993179": {
            "samples": [0.0] * 10 + [0.3] * 73 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7969968384514319356": {
            "samples": [0.0] * 10 + [0.3] * 74,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1322827905238535397": {
            "samples": [0.0] * 10 + [0.3] * 75 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6038835662606201973": {
            "samples": [0.0] * 10 + [0.3] * 76 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6783433932331211436": {
            "samples": [0.0] * 10 + [0.3] * 77 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6637151298710188493": {
            "samples": [0.0] * 10 + [0.3] * 78,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8895499251000749663": {
            "samples": [0.0] * 10 + [0.3] * 79 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5606461783678748531_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5606461783678748531_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
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
        "B4/drive_mixer_84b": [{'intermediate_frequency': 109610828.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_1f9": [{'intermediate_frequency': 331181947.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

