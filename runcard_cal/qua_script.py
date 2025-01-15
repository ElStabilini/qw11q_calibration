
# Single QUA script generated at 2025-01-15 08:55:46.892244
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("7858681079546878519", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25553, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-4746774580840790744", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25553, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("6744271159318069475", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25552, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-7118741852513345157", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25552, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("5010856614685216295", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25552, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-5262298990543073727", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25552, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("340604260460040643", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25551, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("840884002988694082", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25551, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-5301378032117417684", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25551, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-5786232896951561838", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25551, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-7891716023486218558", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25550, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-7672605444372398481", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25550, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("4242058821547332075", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25550, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-1262556984526497866", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25550, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("2670026946447944693", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25549, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-5244533177221781349", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25549, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("2418951465738029736", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25549, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-2777022628354636199", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25549, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-7551098574517923498", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25548, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-7955121817662567138", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25548, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("1253898342595046075", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25548, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("6811895382552034691", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25548, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("1240180209428988057", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25547, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-8666856535226226162", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25547, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-5264716008548170034", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25547, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("3052990884647778587", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25547, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-2796026787942695022", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25546, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("9207761079119366507", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25546, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("7887633373973399213", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25546, "B2/flux")
        play("-9034045779497894013", "B2/drive")
        wait(11, "B2/flux")
        play("-4793232518933351888", "B2/flux")
        wait(51, "B2/drive")
        play("-9034045779497894013", "B2/drive")
        wait(71, "B2/acquisition")
        measure("2666935766152275265", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25546, "B2/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(30).average().save("2666935766152275265_B2|acquisition_shots")


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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
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
            "operations": {
                "7858681079546878519": "7858681079546878519",
                "-4746774580840790744": "-4746774580840790744",
                "6744271159318069475": "6744271159318069475",
                "-7118741852513345157": "-7118741852513345157",
                "5010856614685216295": "5010856614685216295",
                "-5262298990543073727": "-5262298990543073727",
                "340604260460040643": "340604260460040643",
                "840884002988694082": "840884002988694082",
                "-5301378032117417684": "-5301378032117417684",
                "-5786232896951561838": "-5786232896951561838",
                "-7891716023486218558": "-7891716023486218558",
                "-7672605444372398481": "-7672605444372398481",
                "4242058821547332075": "4242058821547332075",
                "-1262556984526497866": "-1262556984526497866",
                "2670026946447944693": "2670026946447944693",
                "-5244533177221781349": "-5244533177221781349",
                "2418951465738029736": "2418951465738029736",
                "-2777022628354636199": "-2777022628354636199",
                "-7551098574517923498": "-7551098574517923498",
                "-7955121817662567138": "-7955121817662567138",
                "1253898342595046075": "1253898342595046075",
                "6811895382552034691": "6811895382552034691",
                "1240180209428988057": "1240180209428988057",
                "-8666856535226226162": "-8666856535226226162",
                "-5264716008548170034": "-5264716008548170034",
                "3052990884647778587": "3052990884647778587",
                "-2796026787942695022": "-2796026787942695022",
                "9207761079119366507": "9207761079119366507",
                "7887633373973399213": "7887633373973399213",
                "-4793232518933351888": "-4793232518933351888",
            },
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
            "operations": {},
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
            "intermediate_frequency": 10073341.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "2666935766152275265": "2666935766152275265_B2/acquisition",
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
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-9034045779497894013": "-9034045779497894013",
            },
        },
    },
    "pulses": {
        "-9034045779497894013": {
            "length": 40,
            "waveforms": {
                "I": "-9034045779497894013_i",
                "Q": "-9034045779497894013_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8577171853299211241": {
            "length": 16,
            "waveforms": {
                "single": "8577171853299211241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2666935766152275265_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4612579205142039746_i",
                "Q": "-4612579205142039746_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6089536855310642122": {
            "length": 16,
            "waveforms": {
                "single": "-6089536855310642122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4111978935701290215": {
            "length": 16,
            "waveforms": {
                "single": "-4111978935701290215",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8659365398186754222": {
            "length": 16,
            "waveforms": {
                "single": "8659365398186754222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1979894310243331419": {
            "length": 16,
            "waveforms": {
                "single": "-1979894310243331419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8671720926008330768": {
            "length": 16,
            "waveforms": {
                "single": "8671720926008330768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1867873405674089922": {
            "length": 16,
            "waveforms": {
                "single": "-1867873405674089922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-965285903538119899": {
            "length": 16,
            "waveforms": {
                "single": "-965285903538119899",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8713923527062660339": {
            "length": 16,
            "waveforms": {
                "single": "-8713923527062660339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5636850366397103668": {
            "length": 16,
            "waveforms": {
                "single": "5636850366397103668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8581660428335984559": {
            "length": 16,
            "waveforms": {
                "single": "8581660428335984559",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2706129270539457440": {
            "length": 16,
            "waveforms": {
                "single": "2706129270539457440",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-95072685567604036": {
            "length": 16,
            "waveforms": {
                "single": "-95072685567604036",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2678363490126246678": {
            "length": 16,
            "waveforms": {
                "single": "-2678363490126246678",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1354460266880464173": {
            "length": 16,
            "waveforms": {
                "single": "1354460266880464173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5022710970053041492": {
            "length": 16,
            "waveforms": {
                "single": "-5022710970053041492",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4653325018579982901": {
            "length": 20,
            "waveforms": {
                "single": "-4653325018579982901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4321883263905398297": {
            "length": 20,
            "waveforms": {
                "single": "4321883263905398297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-350219244688216260": {
            "length": 20,
            "waveforms": {
                "single": "-350219244688216260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5404346680353736251": {
            "length": 20,
            "waveforms": {
                "single": "-5404346680353736251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9015527820465890672": {
            "length": 24,
            "waveforms": {
                "single": "9015527820465890672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7004276800689229958": {
            "length": 24,
            "waveforms": {
                "single": "7004276800689229958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-396174718886226831": {
            "length": 24,
            "waveforms": {
                "single": "-396174718886226831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "319264785950711846": {
            "length": 24,
            "waveforms": {
                "single": "319264785950711846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3356951575861730022": {
            "length": 28,
            "waveforms": {
                "single": "-3356951575861730022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6868012403452053319": {
            "length": 28,
            "waveforms": {
                "single": "6868012403452053319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7183456176061965025": {
            "length": 28,
            "waveforms": {
                "single": "-7183456176061965025",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6300304561293907674": {
            "length": 28,
            "waveforms": {
                "single": "6300304561293907674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2032061993586912526": {
            "length": 32,
            "waveforms": {
                "single": "2032061993586912526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4130717932678538427": {
            "length": 32,
            "waveforms": {
                "single": "-4130717932678538427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7858681079546878519": {
            "length": 32,
            "waveforms": {
                "single": "7858681079546878519",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4746774580840790744": {
            "length": 32,
            "waveforms": {
                "single": "-4746774580840790744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6744271159318069475": {
            "length": 36,
            "waveforms": {
                "single": "6744271159318069475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7118741852513345157": {
            "length": 36,
            "waveforms": {
                "single": "-7118741852513345157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5010856614685216295": {
            "length": 36,
            "waveforms": {
                "single": "5010856614685216295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5262298990543073727": {
            "length": 36,
            "waveforms": {
                "single": "-5262298990543073727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "340604260460040643": {
            "length": 40,
            "waveforms": {
                "single": "340604260460040643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "840884002988694082": {
            "length": 40,
            "waveforms": {
                "single": "840884002988694082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5301378032117417684": {
            "length": 40,
            "waveforms": {
                "single": "-5301378032117417684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5786232896951561838": {
            "length": 40,
            "waveforms": {
                "single": "-5786232896951561838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7891716023486218558": {
            "length": 44,
            "waveforms": {
                "single": "-7891716023486218558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7672605444372398481": {
            "length": 44,
            "waveforms": {
                "single": "-7672605444372398481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4242058821547332075": {
            "length": 44,
            "waveforms": {
                "single": "4242058821547332075",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1262556984526497866": {
            "length": 44,
            "waveforms": {
                "single": "-1262556984526497866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2670026946447944693": {
            "length": 48,
            "waveforms": {
                "single": "2670026946447944693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5244533177221781349": {
            "length": 48,
            "waveforms": {
                "single": "-5244533177221781349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2418951465738029736": {
            "length": 48,
            "waveforms": {
                "single": "2418951465738029736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2777022628354636199": {
            "length": 48,
            "waveforms": {
                "single": "-2777022628354636199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7551098574517923498": {
            "length": 52,
            "waveforms": {
                "single": "-7551098574517923498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7955121817662567138": {
            "length": 52,
            "waveforms": {
                "single": "-7955121817662567138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1253898342595046075": {
            "length": 52,
            "waveforms": {
                "single": "1253898342595046075",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6811895382552034691": {
            "length": 52,
            "waveforms": {
                "single": "6811895382552034691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1240180209428988057": {
            "length": 56,
            "waveforms": {
                "single": "1240180209428988057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8666856535226226162": {
            "length": 56,
            "waveforms": {
                "single": "-8666856535226226162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5264716008548170034": {
            "length": 56,
            "waveforms": {
                "single": "-5264716008548170034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3052990884647778587": {
            "length": 56,
            "waveforms": {
                "single": "3052990884647778587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2796026787942695022": {
            "length": 60,
            "waveforms": {
                "single": "-2796026787942695022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9207761079119366507": {
            "length": 60,
            "waveforms": {
                "single": "9207761079119366507",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7887633373973399213": {
            "length": 60,
            "waveforms": {
                "single": "7887633373973399213",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4793232518933351888": {
            "length": 60,
            "waveforms": {
                "single": "-4793232518933351888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-9034045779497894013_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
        },
        "-9034045779497894013_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
        },
        "8577171853299211241": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4612579205142039746_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4612579205142039746_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6089536855310642122": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4111978935701290215": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8659365398186754222": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1979894310243331419": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8671720926008330768": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-1867873405674089922": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-965285903538119899": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8713923527062660339": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5636850366397103668": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8581660428335984559": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
        },
        "2706129270539457440": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-95072685567604036": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2678363490126246678": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1354460266880464173": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
        },
        "-5022710970053041492": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
        },
        "-4653325018579982901": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4321883263905398297": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-350219244688216260": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
        },
        "-5404346680353736251": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
        },
        "9015527820465890672": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7004276800689229958": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-396174718886226831": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
        },
        "319264785950711846": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
        },
        "-3356951575861730022": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6868012403452053319": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7183456176061965025": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
        },
        "6300304561293907674": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
        },
        "2032061993586912526": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4130717932678538427": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7858681079546878519": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-4746774580840790744": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
        },
        "6744271159318069475": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7118741852513345157": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5010856614685216295": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
        },
        "-5262298990543073727": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
        },
        "340604260460040643": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "840884002988694082": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5301378032117417684": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
        },
        "-5786232896951561838": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
        },
        "-7891716023486218558": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7672605444372398481": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4242058821547332075": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
        },
        "-1262556984526497866": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
        },
        "2670026946447944693": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5244533177221781349": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2418951465738029736": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
        },
        "-2777022628354636199": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
        },
        "-7551098574517923498": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7955121817662567138": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1253898342595046075": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
        },
        "6811895382552034691": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
        },
        "1240180209428988057": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8666856535226226162": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5264716008548170034": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
        },
        "3052990884647778587": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
        },
        "-2796026787942695022": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9207761079119366507": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7887633373973399213": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
        },
        "-4793232518933351888": {
            "samples": [0.0] * 10 + [0.25] * 50,
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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
            "operations": {
                "7858681079546878519": "7858681079546878519",
                "-4746774580840790744": "-4746774580840790744",
                "6744271159318069475": "6744271159318069475",
                "-7118741852513345157": "-7118741852513345157",
                "5010856614685216295": "5010856614685216295",
                "-5262298990543073727": "-5262298990543073727",
                "340604260460040643": "340604260460040643",
                "840884002988694082": "840884002988694082",
                "-5301378032117417684": "-5301378032117417684",
                "-5786232896951561838": "-5786232896951561838",
                "-7891716023486218558": "-7891716023486218558",
                "-7672605444372398481": "-7672605444372398481",
                "4242058821547332075": "4242058821547332075",
                "-1262556984526497866": "-1262556984526497866",
                "2670026946447944693": "2670026946447944693",
                "-5244533177221781349": "-5244533177221781349",
                "2418951465738029736": "2418951465738029736",
                "-2777022628354636199": "-2777022628354636199",
                "-7551098574517923498": "-7551098574517923498",
                "-7955121817662567138": "-7955121817662567138",
                "1253898342595046075": "1253898342595046075",
                "6811895382552034691": "6811895382552034691",
                "1240180209428988057": "1240180209428988057",
                "-8666856535226226162": "-8666856535226226162",
                "-5264716008548170034": "-5264716008548170034",
                "3052990884647778587": "3052990884647778587",
                "-2796026787942695022": "-2796026787942695022",
                "9207761079119366507": "9207761079119366507",
                "7887633373973399213": "7887633373973399213",
                "-4793232518933351888": "-4793232518933351888",
            },
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
            "intermediate_frequency": 10073341.0,
            "operations": {
                "2666935766152275265": "2666935766152275265_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_08e",
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
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-9034045779497894013": "-9034045779497894013",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_88c",
                "lo_frequency": 5900000000.0,
            },
        },
    },
    "pulses": {
        "-9034045779497894013": {
            "length": 40,
            "waveforms": {
                "I": "-9034045779497894013_i",
                "Q": "-9034045779497894013_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8577171853299211241": {
            "length": 16,
            "waveforms": {
                "single": "8577171853299211241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2666935766152275265_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4612579205142039746_i",
                "Q": "-4612579205142039746_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-6089536855310642122": {
            "length": 16,
            "waveforms": {
                "single": "-6089536855310642122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4111978935701290215": {
            "length": 16,
            "waveforms": {
                "single": "-4111978935701290215",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8659365398186754222": {
            "length": 16,
            "waveforms": {
                "single": "8659365398186754222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1979894310243331419": {
            "length": 16,
            "waveforms": {
                "single": "-1979894310243331419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8671720926008330768": {
            "length": 16,
            "waveforms": {
                "single": "8671720926008330768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1867873405674089922": {
            "length": 16,
            "waveforms": {
                "single": "-1867873405674089922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-965285903538119899": {
            "length": 16,
            "waveforms": {
                "single": "-965285903538119899",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8713923527062660339": {
            "length": 16,
            "waveforms": {
                "single": "-8713923527062660339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5636850366397103668": {
            "length": 16,
            "waveforms": {
                "single": "5636850366397103668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8581660428335984559": {
            "length": 16,
            "waveforms": {
                "single": "8581660428335984559",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2706129270539457440": {
            "length": 16,
            "waveforms": {
                "single": "2706129270539457440",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-95072685567604036": {
            "length": 16,
            "waveforms": {
                "single": "-95072685567604036",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2678363490126246678": {
            "length": 16,
            "waveforms": {
                "single": "-2678363490126246678",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1354460266880464173": {
            "length": 16,
            "waveforms": {
                "single": "1354460266880464173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5022710970053041492": {
            "length": 16,
            "waveforms": {
                "single": "-5022710970053041492",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4653325018579982901": {
            "length": 20,
            "waveforms": {
                "single": "-4653325018579982901",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4321883263905398297": {
            "length": 20,
            "waveforms": {
                "single": "4321883263905398297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-350219244688216260": {
            "length": 20,
            "waveforms": {
                "single": "-350219244688216260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5404346680353736251": {
            "length": 20,
            "waveforms": {
                "single": "-5404346680353736251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9015527820465890672": {
            "length": 24,
            "waveforms": {
                "single": "9015527820465890672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7004276800689229958": {
            "length": 24,
            "waveforms": {
                "single": "7004276800689229958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-396174718886226831": {
            "length": 24,
            "waveforms": {
                "single": "-396174718886226831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "319264785950711846": {
            "length": 24,
            "waveforms": {
                "single": "319264785950711846",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3356951575861730022": {
            "length": 28,
            "waveforms": {
                "single": "-3356951575861730022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6868012403452053319": {
            "length": 28,
            "waveforms": {
                "single": "6868012403452053319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7183456176061965025": {
            "length": 28,
            "waveforms": {
                "single": "-7183456176061965025",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6300304561293907674": {
            "length": 28,
            "waveforms": {
                "single": "6300304561293907674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2032061993586912526": {
            "length": 32,
            "waveforms": {
                "single": "2032061993586912526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4130717932678538427": {
            "length": 32,
            "waveforms": {
                "single": "-4130717932678538427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7858681079546878519": {
            "length": 32,
            "waveforms": {
                "single": "7858681079546878519",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4746774580840790744": {
            "length": 32,
            "waveforms": {
                "single": "-4746774580840790744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6744271159318069475": {
            "length": 36,
            "waveforms": {
                "single": "6744271159318069475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7118741852513345157": {
            "length": 36,
            "waveforms": {
                "single": "-7118741852513345157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5010856614685216295": {
            "length": 36,
            "waveforms": {
                "single": "5010856614685216295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5262298990543073727": {
            "length": 36,
            "waveforms": {
                "single": "-5262298990543073727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "340604260460040643": {
            "length": 40,
            "waveforms": {
                "single": "340604260460040643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "840884002988694082": {
            "length": 40,
            "waveforms": {
                "single": "840884002988694082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5301378032117417684": {
            "length": 40,
            "waveforms": {
                "single": "-5301378032117417684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5786232896951561838": {
            "length": 40,
            "waveforms": {
                "single": "-5786232896951561838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7891716023486218558": {
            "length": 44,
            "waveforms": {
                "single": "-7891716023486218558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7672605444372398481": {
            "length": 44,
            "waveforms": {
                "single": "-7672605444372398481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4242058821547332075": {
            "length": 44,
            "waveforms": {
                "single": "4242058821547332075",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1262556984526497866": {
            "length": 44,
            "waveforms": {
                "single": "-1262556984526497866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2670026946447944693": {
            "length": 48,
            "waveforms": {
                "single": "2670026946447944693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5244533177221781349": {
            "length": 48,
            "waveforms": {
                "single": "-5244533177221781349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2418951465738029736": {
            "length": 48,
            "waveforms": {
                "single": "2418951465738029736",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2777022628354636199": {
            "length": 48,
            "waveforms": {
                "single": "-2777022628354636199",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7551098574517923498": {
            "length": 52,
            "waveforms": {
                "single": "-7551098574517923498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7955121817662567138": {
            "length": 52,
            "waveforms": {
                "single": "-7955121817662567138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1253898342595046075": {
            "length": 52,
            "waveforms": {
                "single": "1253898342595046075",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6811895382552034691": {
            "length": 52,
            "waveforms": {
                "single": "6811895382552034691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1240180209428988057": {
            "length": 56,
            "waveforms": {
                "single": "1240180209428988057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8666856535226226162": {
            "length": 56,
            "waveforms": {
                "single": "-8666856535226226162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5264716008548170034": {
            "length": 56,
            "waveforms": {
                "single": "-5264716008548170034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3052990884647778587": {
            "length": 56,
            "waveforms": {
                "single": "3052990884647778587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2796026787942695022": {
            "length": 60,
            "waveforms": {
                "single": "-2796026787942695022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9207761079119366507": {
            "length": 60,
            "waveforms": {
                "single": "9207761079119366507",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7887633373973399213": {
            "length": 60,
            "waveforms": {
                "single": "7887633373973399213",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4793232518933351888": {
            "length": 60,
            "waveforms": {
                "single": "-4793232518933351888",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-9034045779497894013_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9034045779497894013_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8577171853299211241": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4612579205142039746_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4612579205142039746_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6089536855310642122": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4111978935701290215": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8659365398186754222": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1979894310243331419": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8671720926008330768": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1867873405674089922": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-965285903538119899": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8713923527062660339": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5636850366397103668": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8581660428335984559": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2706129270539457440": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-95072685567604036": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2678363490126246678": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1354460266880464173": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5022710970053041492": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4653325018579982901": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4321883263905398297": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-350219244688216260": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5404346680353736251": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9015527820465890672": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7004276800689229958": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-396174718886226831": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "319264785950711846": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3356951575861730022": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6868012403452053319": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7183456176061965025": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6300304561293907674": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2032061993586912526": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4130717932678538427": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7858681079546878519": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4746774580840790744": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6744271159318069475": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7118741852513345157": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5010856614685216295": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5262298990543073727": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "340604260460040643": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "840884002988694082": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5301378032117417684": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5786232896951561838": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7891716023486218558": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7672605444372398481": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4242058821547332075": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1262556984526497866": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2670026946447944693": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5244533177221781349": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2418951465738029736": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2777022628354636199": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7551098574517923498": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7955121817662567138": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1253898342595046075": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6811895382552034691": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1240180209428988057": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8666856535226226162": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5264716008548170034": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3052990884647778587": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2796026787942695022": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9207761079119366507": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7887633373973399213": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4793232518933351888": {
            "samples": [0.0] * 10 + [0.25] * 50,
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
    },
    "mixers": {
        "B2/acquisition_mixer_08e": [{'intermediate_frequency': 10073341.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_88c": [{'intermediate_frequency': 63692382.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

