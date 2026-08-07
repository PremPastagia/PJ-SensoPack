
import math

import math
def softmax(x):
    m = max(x)
    exps = [math.exp(i - m) for i in x]
    s = sum(exps)
    for idx, _ in enumerate(exps):
        exps[idx] /= s
    return exps
def score(input):
    if input[3] < 37.566174:
        var0 = 0.14769432
    else:
        if input[3] < 37.808918:
            var0 = -0.021134749
        else:
            var0 = -0.07516441
    if input[3] < 37.566174:
        var1 = 0.1282134
    else:
        if input[3] < 37.808918:
            var1 = -0.019250188
        else:
            var1 = -0.072316185
    if input[3] < 37.566174:
        var2 = 0.11400963
    else:
        if input[3] < 37.808918:
            var2 = -0.017384144
        else:
            var2 = -0.0698173
    if input[3] < 37.566174:
        var3 = 0.10325191
    else:
        if input[3] < 37.808918:
            var3 = -0.015540386
        else:
            var3 = -0.06761911
    if input[3] < 37.566174:
        var4 = 0.09486719
    else:
        if input[3] < 37.808918:
            var4 = -0.013722303
        else:
            var4 = -0.06568102
    if input[3] < 37.566174:
        var5 = 0.088183865
    else:
        if input[3] < 37.808918:
            var5 = -0.013007759
        else:
            var5 = -0.063966386
    if input[3] < 37.566174:
        var6 = 0.08275982
    else:
        if input[3] < 37.808918:
            var6 = -0.011266346
        else:
            var6 = -0.06245011
    if input[3] < 37.566174:
        var7 = 0.07829218
    else:
        if input[3] < 37.808918:
            var7 = -0.01058287
        else:
            var7 = -0.061102867
    if input[3] < 37.566174:
        var8 = 0.0745665
    else:
        if input[3] < 37.808918:
            var8 = -0.009906964
        else:
            var8 = -0.059904855
    if input[3] < 37.566174:
        var9 = 0.07142674
    else:
        if input[3] < 37.808918:
            var9 = -0.009243462
        else:
            var9 = -0.058837205
    if input[3] < 37.566174:
        var10 = 0.06875675
    else:
        if input[3] < 37.808918:
            var10 = -0.008596162
        else:
            var10 = -0.05788359
    if input[3] < 37.566174:
        var11 = 0.06646829
    else:
        if input[3] < 37.808918:
            var11 = -0.007968045
        else:
            var11 = -0.057029862
    if input[3] < 37.566174:
        var12 = 0.06449312
    else:
        if input[3] < 37.808918:
            var12 = -0.007361375
        else:
            var12 = -0.056263704
    if input[3] < 37.566174:
        var13 = 0.06277772
    else:
        if input[3] < 37.808918:
            var13 = -0.006777855
        else:
            var13 = -0.055574387
    if input[3] < 37.566174:
        var14 = 0.061279446
    else:
        if input[3] < 37.808918:
            var14 = -0.0062186923
        else:
            var14 = -0.05495251
    if input[3] < 37.566174:
        var15 = 0.059963953
    else:
        if input[3] < 37.808918:
            var15 = -0.005684701
        else:
            var15 = -0.054389812
    if input[3] < 37.566174:
        var16 = 0.05880324
    else:
        if input[3] < 37.808918:
            var16 = -0.0051763575
        else:
            var16 = -0.05387903
    if input[3] < 37.566174:
        var17 = 0.057774253
    else:
        if input[3] < 37.808918:
            var17 = -0.004693856
        else:
            var17 = -0.053413708
    if input[3] < 37.566174:
        var18 = 0.056857806
    else:
        if input[3] < 37.808918:
            var18 = -0.0042371578
        else:
            var18 = -0.052988112
    if input[3] < 37.566174:
        var19 = 0.056037825
    else:
        if input[3] < 37.808918:
            var19 = -0.0038060278
        else:
            var19 = -0.052597135
    if input[3] < 37.566174:
        var20 = 0.05530069
    else:
        if input[3] < 37.808918:
            var20 = -0.0034000713
        else:
            var20 = -0.052236166
    if input[3] < 37.566174:
        var21 = 0.05463477
    else:
        if input[3] < 37.808918:
            var21 = -0.003018753
        else:
            var21 = -0.05190106
    if input[3] < 37.566174:
        var22 = 0.054030087
    else:
        if input[3] < 37.808918:
            var22 = -0.0026614384
        else:
            var22 = -0.051588047
    if input[3] < 37.566174:
        var23 = 0.05347796
    else:
        if input[3] < 37.808918:
            var23 = -0.0023274056
        else:
            var23 = -0.051293697
    if input[3] < 37.566174:
        var24 = 0.052970856
    else:
        if input[3] < 37.808918:
            var24 = -0.0020158521
        else:
            var24 = -0.051014848
    if input[3] < 37.566174:
        var25 = 0.05250212
    else:
        if input[3] < 37.808918:
            var25 = -0.0009440115
        else:
            var25 = -0.050750207
    if input[3] < 37.566174:
        var26 = 0.05206583
    else:
        if input[3] < 37.808918:
            var26 = 0.00008881988
        else:
            var26 = -0.050495546
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var27 = 0.05165676
        else:
            var27 = 0.001084776
    else:
        var27 = -0.05024838
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var28 = 0.051270165
        else:
            var28 = 0.002039801
    else:
        var28 = -0.050006308
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var29 = 0.05090177
        else:
            var29 = 0.0029563103
    else:
        var29 = -0.049767133
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var30 = 0.05054767
        else:
            var30 = 0.0038304788
    else:
        var30 = -0.049528696
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var31 = 0.050204284
        else:
            var31 = 0.0046650087
    else:
        var31 = -0.049288996
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var32 = 0.049868323
        else:
            var32 = 0.005456344
    else:
        var32 = -0.04904605
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var33 = 0.049536716
        else:
            var33 = 0.0062074885
    else:
        var33 = -0.048798025
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var34 = 0.049206603
        else:
            var34 = 0.005965473
    else:
        var34 = -0.048538905
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var35 = 0.048875343
        else:
            var35 = 0.005731839
    else:
        var35 = -0.04827063
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var36 = 0.048540425
        else:
            var36 = 0.005506394
    else:
        var36 = -0.047991406
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var37 = 0.04819953
        else:
            var37 = 0.0052889637
    else:
        var37 = -0.047699507
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var38 = 0.04785047
        else:
            var38 = 0.005079371
    else:
        var38 = -0.04739326
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var39 = 0.047491215
        else:
            var39 = 0.004877423
    else:
        var39 = -0.047071062
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var40 = 0.047119897
        else:
            var40 = 0.0046829386
    else:
        var40 = -0.04673139
    var41 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var42 = 0.04673479
        else:
            var42 = 0.004495716
    else:
        var42 = -0.046372823
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var43 = 0.046334345
        else:
            var43 = 0.0043155653
    else:
        var43 = -0.04599404
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var44 = 0.04591723
        else:
            var44 = 0.004142313
    else:
        var44 = -0.045593858
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var45 = 0.04548214
        else:
            var45 = 0.003975745
    else:
        var45 = -0.045171235
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var46 = 0.04502826
        else:
            var46 = 0.00381568
    else:
        var46 = -0.044725306
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var47 = 0.044554677
        else:
            var47 = 0.0036619238
    else:
        var47 = -0.044255387
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var48 = 0.04406085
        else:
            var48 = 0.0035142943
    else:
        var48 = -0.04376101
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var49 = 0.04354654
        else:
            var49 = 0.0033725896
    else:
        var49 = -0.04324194
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var50 = 0.04301171
        else:
            var50 = 0.0032366295
    else:
        var50 = -0.042698182
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var51 = 0.042453486
        else:
            var51 = 0.0034482689
    else:
        var51 = -0.04213001
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var52 = 0.041878175
        else:
            var52 = 0.0033021662
    else:
        var52 = -0.041537944
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var53 = 0.04130769
        else:
            var53 = 0.002997468
    else:
        var53 = -0.04092279
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var54 = 0.040722232
        else:
            var54 = 0.0026994473
    else:
        var54 = -0.040285613
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var55 = 0.040093686
        else:
            var55 = 0.0033828092
    else:
        var55 = -0.039653316
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var56 = 0.03944911
        else:
            var56 = 0.0040270467
    else:
        var56 = -0.039006494
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var57 = 0.038789865
        else:
            var57 = 0.0046279
    else:
        var57 = -0.038346056
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var58 = 0.038117927
        else:
            var58 = 0.0051888055
    else:
        var58 = -0.037674513
    if input[3] < 37.808918:
        if input[1] < 86.58795:
            if input[3] < 36.84778:
                var59 = 0.034822162
            else:
                var59 = -0.025777532
        else:
            var59 = 0.04838702
    else:
        var59 = -0.03699454
    if input[3] < 37.808918:
        if input[1] < 86.58795:
            if input[3] < 36.03289:
                var60 = 0.033817105
            else:
                var60 = -0.022973267
        else:
            var60 = 0.04734542
    else:
        var60 = -0.03630728
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var61 = 0.009658926
        else:
            var61 = 0.039282203
    else:
        var61 = -0.03561492
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var62 = 0.035565127
        else:
            var62 = 0.0057683745
    else:
        var62 = -0.03486747
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var63 = 0.008332754
        else:
            var63 = 0.037366595
    else:
        var63 = -0.03416903
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var64 = 0.034360796
        else:
            var64 = 0.004955416
    else:
        var64 = -0.033414256
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var65 = 0.0071522184
        else:
            var65 = 0.035472717
    else:
        var65 = -0.032719772
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var66 = 0.006899214
        else:
            var66 = 0.034591816
    else:
        var66 = -0.032031097
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var67 = 0.03253795
        else:
            var67 = 0.0050826557
    else:
        var67 = -0.03135474
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var68 = 0.03192234
        else:
            var68 = 0.004480454
    else:
        var68 = -0.030624626
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var69 = 0.031316176
        else:
            var69 = 0.003915981
    else:
        var69 = -0.029914161
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var70 = 0.030719852
        else:
            var70 = 0.0033869357
    else:
        var70 = -0.029225409
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var71 = 0.030259848
        else:
            var71 = 0.0033116245
    else:
        var71 = -0.02870874
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var72 = 0.029807394
        else:
            var72 = 0.0032322227
    else:
        var72 = -0.028204272
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var73 = 0.0031953137
        else:
            var73 = 0.029664276
    else:
        var73 = -0.027713021
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var74 = 0.029100869
        else:
            var74 = 0.002617408
    else:
        var74 = -0.027234128
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var75 = 0.028668223
        else:
            var75 = 0.0025368836
    else:
        var75 = -0.026767222
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var76 = 0.02824219
        else:
            var76 = 0.002450332
    else:
        var76 = -0.026312703
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var77 = 0.0020742253
        else:
            var77 = 0.027616639
    else:
        var77 = -0.025864873
    if input[3] < 37.808918:
        if input[3] < 37.566174:
            var78 = 0.027613422
        else:
            var78 = 0.0018591948
    else:
        var78 = -0.025428688
    if input[3] < 37.566174:
        var79 = 0.027169783
    else:
        if input[1] < 86.25803:
            var79 = -0.028808052
        else:
            var79 = 0.008533975
    if input[3] < 37.566174:
        var80 = 0.026736185
    else:
        if input[1] < 86.25803:
            var80 = -0.028294472
        else:
            var80 = 0.0081276735
    if input[3] < 37.566174:
        var81 = 0.026347611
    else:
        if input[1] < 86.25803:
            var81 = -0.027866377
        else:
            var81 = 0.0075467536
    if input[3] < 37.566174:
        var82 = 0.026035253
    else:
        if input[1] < 86.25803:
            var82 = -0.027444322
        else:
            var82 = 0.0071239197
    if input[3] < 37.566174:
        var83 = 0.025607435
    else:
        if input[1] < 86.25803:
            var83 = -0.027136493
        else:
            var83 = 0.006762583
    if input[3] < 37.566174:
        var84 = 0.02534075
    else:
        if input[1] < 86.25803:
            var84 = -0.026715053
        else:
            var84 = 0.006361832
    if input[1] < 71.20408:
        var85 = -0.006146168
    else:
        var85 = 0.008897032
    if input[1] < 71.20408:
        var86 = -0.005792672
    else:
        var86 = 0.008470806
    if input[1] < 71.20408:
        var87 = -0.005799671
    else:
        var87 = 0.008058032
    if input[1] < 71.20408:
        var88 = -0.0054567694
    else:
        var88 = 0.007671001
    if input[1] < 71.20408:
        var89 = -0.005467305
    else:
        var89 = 0.0072922306
    if input[1] < 71.20408:
        var90 = -0.00547058
    else:
        var90 = 0.0069323303
    if input[1] < 71.20408:
        var91 = -0.005134336
    else:
        var91 = 0.006596935
    if input[1] < 71.20408:
        var92 = -0.0051415204
    else:
        var92 = 0.006266574
    if input[1] < 71.20408:
        var93 = -0.005142234
    else:
        var93 = 0.005951893
    if input[1] < 71.20408:
        var94 = -0.0048115016
    else:
        var94 = 0.00566332
    if input[1] < 70.20504:
        var95 = -0.0048659686
    else:
        var95 = 0.005332932
    if input[1] < 70.20504:
        var96 = -0.004865428
    else:
        var96 = 0.005059225
    var97 = var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96
    if input[1] < 71.20408:
        var98 = -0.0044962
    else:
        var98 = 0.004855051
    if input[1] < 70.20504:
        var99 = -0.004545898
    else:
        var99 = 0.0045651747
    if input[1] < 70.20504:
        var100 = -0.004545849
    else:
        var100 = 0.0043251007
    if input[1] < 71.20408:
        var101 = -0.0041904612
    else:
        var101 = 0.0041484535
    if input[1] < 70.20504:
        var102 = -0.0042365715
    else:
        var102 = 0.0038942609
    if input[1] < 70.20504:
        var103 = -0.003929024
    else:
        var103 = 0.003704941
    if input[1] < 70.20504:
        var104 = -0.0039414
    else:
        var104 = 0.0034991005
    if input[1] < 70.20504:
        var105 = -0.0039480748
    else:
        var105 = 0.0033039458
    if input[1] < 71.20408:
        var106 = -0.0036186152
    else:
        var106 = 0.003168119
    if input[1] < 70.20504:
        var107 = -0.0036644153
    else:
        var107 = 0.0029606544
    if input[1] < 70.20504:
        var108 = -0.003672293
    else:
        var108 = 0.0027884517
    if input[1] < 70.20504:
        var109 = -0.0033821848
    else:
        var109 = 0.0026484428
    if input[1] < 70.20504:
        var110 = -0.0033971795
    else:
        var110 = 0.0024890793
    if input[1] < 71.20408:
        var111 = -0.003381516
    else:
        var111 = 0.002361201
    if input[1] < 70.20504:
        var112 = -0.0031254266
    else:
        var112 = 0.00222012
    if input[1] < 70.20504:
        var113 = -0.0031426128
    else:
        var113 = 0.002078366
    if input[1] < 70.20504:
        var114 = -0.0031554804
    else:
        var114 = 0.0019441266
    if input[1] < 70.20504:
        var115 = -0.0028795796
    else:
        var115 = 0.0018439721
    if input[1] < 70.20504:
        var116 = -0.0028995152
    else:
        var116 = 0.0017181042
    if input[1] < 70.20504:
        var117 = -0.0029145197
    else:
        var117 = 0.0015988462
    if input[1] < 70.20504:
        var118 = -0.002646454
    else:
        var118 = 0.0015147927
    if input[1] < 70.20504:
        var119 = -0.0026692112
    else:
        var119 = 0.0014027073
    if input[1] < 70.20504:
        var120 = -0.002687449
    else:
        var120 = 0.001297263
    if input[1] < 70.20504:
        var121 = -0.0024257237
    else:
        var121 = 0.0012273341
    if input[1] < 70.20504:
        var122 = -0.0024514047
    else:
        var122 = 0.0011272853
    if input[1] < 70.20504:
        var123 = -0.0024724978
    else:
        var123 = 0.0010332443
    if input[1] < 68.66822:
        var124 = 0.0013865065
    else:
        var124 = -0.002009033
    if input[1] < 70.20504:
        var125 = -0.0023390818
    else:
        var125 = 0.0009798951
    if input[1] < 68.66822:
        var126 = 0.0012643578
    else:
        var126 = -0.0021131465
    if input[1] < 68.66822:
        var127 = 0.001391275
    else:
        var127 = -0.0020417336
    if input[1] < 68.66822:
        var128 = 0.0012807201
    else:
        var128 = -0.0020487402
    if input[1] < 68.66822:
        var129 = 0.0013785305
    else:
        var129 = -0.0019661
    if input[1] < 70.20504:
        var130 = -0.0023153273
    else:
        var130 = 0.0010085505
    if input[1] < 68.66822:
        var131 = 0.0013018815
    else:
        var131 = -0.001973104
    if input[1] < 70.20504:
        var132 = -0.002356176
    else:
        var132 = 0.0009823799
    if input[1] < 68.66822:
        var133 = 0.00139166
    else:
        var133 = -0.001985356
    if input[1] < 68.66822:
        var134 = 0.0012829842
    else:
        var134 = -0.0019915523
    if input[1] < 68.66822:
        var135 = 0.0013741356
    else:
        var135 = -0.0019116463
    if input[1] < 70.20504:
        var136 = -0.002254068
    else:
        var136 = 0.001017934
    if input[1] < 68.66822:
        var137 = 0.0012980207
    else:
        var137 = -0.0019187949
    if input[1] < 70.20504:
        var138 = -0.0022944272
    else:
        var138 = 0.0009915394
    if input[1] < 68.66822:
        var139 = 0.0013833024
    else:
        var139 = -0.0019318461
    if input[1] < 68.66822:
        var140 = 0.0012759017
    else:
        var140 = -0.0019378398
    if input[1] < 68.66822:
        var141 = 0.001366773
    else:
        var141 = -0.0018600317
    if input[1] < 70.20504:
        var142 = -0.0021976533
    else:
        var142 = 0.0010247786
    if input[1] < 68.66822:
        var143 = 0.0014434898
    else:
        var143 = -0.0018771209
    if input[1] < 68.66822:
        var144 = 0.0013345699
    else:
        var144 = -0.0018850589
    if input[1] < 70.20504:
        var145 = -0.0021342495
    else:
        var145 = 0.0010520581
    if input[1] < 68.66822:
        var146 = 0.0014481001
    else:
        var146 = -0.001809714
    if input[1] < 68.66822:
        var147 = 0.0013386366
    else:
        var147 = -0.0018201331
    if input[1] < 68.66822:
        var148 = 0.0014223028
    else:
        var148 = -0.0017474632
    if input[1] < 70.20504:
        var149 = -0.0020603458
    else:
        var149 = 0.0010696132
    if input[1] < 68.66822:
        var150 = 0.001488538
    else:
        var150 = -0.0017712059
    if input[1] < 68.66822:
        var151 = 0.0013777112
    else:
        var151 = -0.0017827306
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var152 = -0.07338404
        else:
            var152 = 0.15354338
    else:
        var152 = -0.07339012
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var153 = -0.07079632
        else:
            var153 = 0.13229607
    else:
        var153 = -0.07079
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var154 = -0.068502665
        else:
            var154 = 0.11697584
    else:
        var154 = -0.06848891
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var155 = -0.066467546
        else:
            var155 = 0.105463564
    else:
        var155 = -0.06644967
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var156 = -0.06465974
        else:
            if input[3] < 37.808918:
                var156 = 0.044998437
            else:
                var156 = 0.096977055
    else:
        var156 = -0.064639956
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var157 = -0.063051574
        else:
            var157 = 0.08947413
    else:
        var157 = -0.06303135
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var158 = -0.061618663
        else:
            if input[3] < 37.808918:
                var158 = 0.0377547
            else:
                var158 = 0.084152885
    else:
        var158 = -0.061598938
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var159 = -0.060339462
        else:
            if input[3] < 37.808918:
                var159 = 0.035409532
            else:
                var159 = 0.079442576
    else:
        var159 = -0.06032086
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var160 = -0.05919505
        else:
            if input[3] < 37.808918:
                var160 = 0.03324553
            else:
                var160 = 0.07552671
    else:
        var160 = -0.059177946
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var161 = -0.058168795
        else:
            if input[3] < 37.808918:
                var161 = 0.031240124
            else:
                var161 = 0.072235316
    else:
        var161 = -0.058153428
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var162 = -0.0572461
        else:
            if input[3] < 37.808918:
                var162 = 0.029374802
            else:
                var162 = 0.06944261
    else:
        var162 = -0.0572326
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var163 = -0.056414135
        else:
            if input[3] < 37.808918:
                var163 = 0.027634213
            else:
                var163 = 0.06705355
    else:
        var163 = -0.05640256
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var164 = -0.055661585
        else:
            if input[3] < 37.808918:
                var164 = 0.026005615
            else:
                var164 = 0.064994976
    else:
        var164 = -0.055651963
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var165 = -0.05497846
        else:
            if input[3] < 37.808918:
                var165 = 0.024478305
            else:
                var165 = 0.06320971
    else:
        var165 = -0.0549708
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var166 = -0.05435593
        else:
            if input[3] < 37.808918:
                var166 = 0.023043273
            else:
                var166 = 0.0616524
    else:
        var166 = -0.054350223
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var167 = -0.053786155
        else:
            if input[3] < 37.808918:
                var167 = 0.02169284
            else:
                var167 = 0.060286608
    else:
        var167 = -0.05378237
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var168 = -0.053262103
        else:
            if input[3] < 37.808918:
                var168 = 0.020420427
            else:
                var168 = 0.059082717
    else:
        var168 = -0.05326022
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var169 = -0.0527775
        else:
            if input[3] < 37.808918:
                var169 = 0.019220375
            else:
                var169 = 0.058016397
    else:
        var169 = -0.05277751
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var170 = -0.05232668
        else:
            if input[3] < 37.808918:
                var170 = 0.018087713
            else:
                var170 = 0.057067465
    else:
        var170 = -0.052328587
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var171 = -0.051904507
        else:
            if input[3] < 37.808918:
                var171 = 0.017018104
            else:
                var171 = 0.056219023
    else:
        var171 = -0.051908314
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var172 = -0.051506322
        else:
            if input[3] < 37.808918:
                var172 = 0.016007667
            else:
                var172 = 0.055456784
    else:
        var172 = -0.05151204
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var173 = -0.051127832
        else:
            if input[3] < 37.808918:
                var173 = 0.015052966
            else:
                var173 = 0.05476859
    else:
        var173 = -0.051135488
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var174 = -0.050765105
        else:
            if input[3] < 37.808918:
                var174 = 0.014150864
            else:
                var174 = 0.054143984
    else:
        var174 = -0.050774723
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var175 = -0.050414454
        else:
            if input[3] < 37.808918:
                var175 = 0.013298501
            else:
                var175 = 0.053573947
    else:
        var175 = -0.050426096
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var176 = -0.050072487
        else:
            if input[1] < 96.68594:
                var176 = 0.053478565
            else:
                if input[1] < 97.58033:
                    var176 = -0.012359844
                else:
                    var176 = 0.034760937
    else:
        var176 = -0.050086208
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var177 = -0.049735982
        else:
            if input[1] < 96.68594:
                var177 = 0.052992698
            else:
                if input[3] < 44.185143:
                    var177 = -0.013759588
                else:
                    var177 = 0.033778086
    else:
        var177 = -0.049751844
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var178 = -0.049401913
        else:
            if input[1] < 96.68594:
                var178 = 0.052541513
            else:
                if input[1] < 97.58033:
                    var178 = -0.014566774
                else:
                    var178 = 0.032666106
    else:
        var178 = -0.049420003
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var179 = -0.04906742
        else:
            if input[1] < 96.68594:
                var179 = 0.05211952
            else:
                if input[3] < 44.185143:
                    var179 = -0.015812403
                else:
                    var179 = 0.03172059
    else:
        var179 = -0.049087826
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var180 = -0.048729774
        else:
            if input[1] < 96.68594:
                var180 = 0.051721808
            else:
                if input[1] < 97.58033:
                    var180 = -0.016496683
                else:
                    var180 = 0.030641941
    else:
        var180 = -0.04875259
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var181 = -0.048386373
        else:
            if input[1] < 96.68594:
                var181 = 0.05134393
            else:
                if input[3] < 44.185143:
                    var181 = -0.017592032
                else:
                    var181 = 0.029733343
    else:
        var181 = -0.04841171
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var182 = -0.04803474
        else:
            if input[1] < 96.68594:
                var182 = 0.05098189
            else:
                if input[1] < 97.58033:
                    var182 = -0.018158492
                else:
                    var182 = 0.02868908
    else:
        var182 = -0.048062705
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var183 = -0.047672506
        else:
            if input[1] < 96.68594:
                var183 = 0.050632007
            else:
                if input[3] < 44.185143:
                    var183 = -0.019109031
                else:
                    var183 = 0.027818663
    else:
        var183 = -0.047703214
    if input[3] < 54.91084:
        if input[3] < 37.566174:
            var184 = -0.047297426
        else:
            if input[1] < 96.68594:
                var184 = 0.05029092
            else:
                if input[1] < 97.58033:
                    var184 = -0.019563686
                else:
                    var184 = 0.026811276
    else:
        var184 = -0.047330994
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var185 = -0.046907358
            else:
                var185 = 0.0005043008
        else:
            var185 = 0.04957449
    else:
        var185 = -0.046943907
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var186 = -0.046500307
            else:
                var186 = 0.00041564112
        else:
            var186 = 0.04923194
    else:
        var186 = -0.046539947
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var187 = -0.046074413
            else:
                var187 = 0.0003364661
        else:
            var187 = 0.048888393
    else:
        var187 = -0.046117257
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var188 = -0.045627967
            else:
                var188 = 0.00026600025
        else:
            var188 = 0.04854117
    else:
        var188 = -0.045674115
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var189 = -0.045159437
            else:
                var189 = 0.00020353301
        else:
            var189 = 0.048187748
    else:
        var189 = -0.045208987
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var190 = -0.044667497
            else:
                var190 = 0.00014835877
        else:
            var190 = 0.047825795
    else:
        var190 = -0.04472052
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var191 = -0.044151045
            else:
                var191 = 0.00009989081
        else:
            var191 = 0.047453072
    else:
        var191 = -0.044207595
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var192 = -0.043609194
            else:
                var192 = 0.00005754101
        else:
            var192 = 0.04706751
    else:
        var192 = -0.043669313
    var193 = var152 + var153 + var154 + var155 + var156 + var157 + var158 + var159 + var160 + var161 + var162 + var163 + var164 + var165 + var166 + var167 + var168 + var169 + var170 + var171 + var172 + var173 + var174 + var175 + var176 + var177 + var178 + var179 + var180 + var181 + var182 + var183 + var184 + var185 + var186 + var187 + var188 + var189 + var190 + var191 + var192
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var194 = -0.043041367
            else:
                var194 = 0.000020799145
        else:
            var194 = 0.046667214
    else:
        var194 = -0.04310506
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var195 = -0.042447235
            else:
                var195 = -0.000010842208
        else:
            var195 = 0.0462504
    else:
        var195 = -0.042514477
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var196 = -0.0418268
            else:
                var196 = -0.0000377992
        else:
            var196 = 0.04581557
    else:
        var196 = -0.041897554
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var197 = -0.04118038
            else:
                var197 = -0.000060520753
        else:
            var197 = 0.045361314
    else:
        var197 = -0.04125457
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var198 = -0.04050862
            else:
                var198 = -0.00007938176
        else:
            var198 = 0.04488642
    else:
        var198 = -0.040586125
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var199 = -0.039812494
            else:
                var199 = -0.000094710325
        else:
            var199 = 0.044390008
    else:
        var199 = -0.03989316
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var200 = -0.039093312
            else:
                var200 = -0.000106868356
        else:
            var200 = 0.04387135
    else:
        var200 = -0.03917696
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var201 = -0.038352665
            else:
                var201 = -0.000116137926
        else:
            var201 = 0.04333003
    else:
        var201 = -0.038439095
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[1] < 86.58795:
                if input[3] < 37.566174:
                    var202 = -0.035229415
                else:
                    var202 = 0.032786313
            else:
                var202 = -0.050575938
        else:
            var202 = 0.04276596
    else:
        var202 = -0.03768143
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[3] < 37.566174:
                var203 = -0.03680649
            else:
                var203 = -0.00046523527
        else:
            var203 = 0.04217913
    else:
        var203 = -0.036906116
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[1] < 68.93957:
                if input[3] < 33.04824:
                    var204 = -0.026088012
                else:
                    var204 = 0.021807775
            else:
                var204 = -0.039405167
        else:
            var204 = 0.04156999
    else:
        var204 = -0.036115505
    if input[3] < 54.91084:
        if input[3] < 37.808918:
            if input[1] < 68.93957:
                if input[3] < 33.04824:
                    var205 = -0.025239287
                else:
                    var205 = 0.021590125
            else:
                var205 = -0.03835742
        else:
            var205 = 0.040939238
    else:
        var205 = -0.035312146
    if input[3] < 37.566174:
        var206 = -0.03453075
    else:
        if input[3] < 54.91084:
            if input[1] < 93.76548:
                var206 = 0.043335013
            else:
                var206 = -0.019919574
        else:
            var206 = -0.034498736
    if input[3] < 37.566174:
        var207 = -0.033710506
    else:
        if input[3] < 54.91084:
            if input[1] < 93.63151:
                var207 = 0.042739138
            else:
                var207 = -0.019415354
        else:
            var207 = -0.033678044
    if input[3] < 37.566174:
        var208 = -0.03288573
    else:
        if input[3] < 54.91084:
            if input[1] < 93.63151:
                var208 = 0.04216021
            else:
                var208 = -0.019571176
        else:
            var208 = -0.032852888
    if input[3] < 37.566174:
        var209 = -0.03205925
    else:
        if input[3] < 54.91084:
            if input[1] < 93.48088:
                var209 = 0.041559044
            else:
                var209 = -0.019410182
        else:
            var209 = -0.032026093
    if input[3] < 37.566174:
        var210 = -0.031233808
    else:
        if input[3] < 54.91084:
            if input[1] < 93.415825:
                var210 = 0.04093518
            else:
                var210 = -0.018994048
        else:
            var210 = -0.031200394
    if input[3] < 37.566174:
        var211 = -0.030412063
    else:
        if input[3] < 54.91084:
            if input[1] < 93.415825:
                var211 = 0.040336937
            else:
                var211 = -0.019087136
        else:
            var211 = -0.030378452
    if input[3] < 37.566174:
        var212 = -0.029610766
    else:
        if input[3] < 54.91084:
            if input[1] < 93.415825:
                var212 = 0.039586402
            else:
                var212 = -0.018638462
        else:
            var212 = -0.029562777
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var213 = 0.0015468587
        else:
            var213 = -0.03511661
    else:
        if input[3] < 54.91084:
            var213 = 0.035831925
        else:
            var213 = -0.028755724
    if input[3] < 37.566174:
        var214 = -0.028338362
    else:
        if input[3] < 54.91084:
            if input[1] < 92.115944:
                var214 = 0.038469613
            else:
                var214 = -0.017606467
        else:
            var214 = -0.027959451
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var215 = 0.0022094832
        else:
            var215 = -0.033159032
    else:
        if input[3] < 54.91084:
            var215 = 0.034437045
        else:
            var215 = -0.027175898
    if input[3] < 37.566174:
        var216 = -0.027095655
    else:
        if input[3] < 54.91084:
            if input[1] < 91.13089:
                var216 = 0.03745553
            else:
                var216 = -0.016648198
        else:
            var216 = -0.02640678
    if input[3] < 37.566174:
        var217 = -0.026330728
    else:
        if input[3] < 54.91084:
            if input[1] < 90.158806:
                var217 = 0.03682892
            else:
                var217 = -0.016536737
        else:
            var217 = -0.025653575
    if input[3] < 37.566174:
        var218 = -0.025749266
    else:
        if input[3] < 54.71582:
            if input[1] < 89.58745:
                var218 = 0.03614191
            else:
                var218 = -0.015769158
        else:
            var218 = -0.02414449
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var219 = 0.0028350425
        else:
            var219 = -0.029649293
    else:
        if input[3] < 54.395264:
            var219 = 0.031365667
        else:
            var219 = -0.021794708
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var220 = 0.0032447123
        else:
            var220 = -0.028707927
    else:
        if input[3] < 53.186474:
            var220 = 0.03021641
        else:
            var220 = -0.019262366
    if input[3] < 37.808918:
        if input[1] < 68.93957:
            var221 = 0.0036229703
        else:
            var221 = -0.027799532
    else:
        if input[3] < 52.65984:
            var221 = 0.029003635
        else:
            var221 = -0.016766522
    if input[1] < 89.78451:
        if input[3] < 48.591053:
            var222 = 0.013482413
        else:
            var222 = -0.007660705
    else:
        var222 = -0.020956986
    if input[1] < 89.78451:
        if input[3] < 48.041187:
            var223 = 0.0130552575
        else:
            var223 = -0.0067397724
    else:
        var223 = -0.020628678
    if input[1] < 89.78451:
        if input[3] < 47.597607:
            var224 = 0.012476658
        else:
            var224 = -0.0054722866
    else:
        var224 = -0.020308306
    if input[1] < 89.78451:
        if input[3] < 47.501717:
            var225 = 0.012034224
        else:
            var225 = -0.004550223
    else:
        var225 = -0.01999591
    if input[1] < 89.78451:
        if input[3] < 47.150513:
            var226 = 0.0114224395
        else:
            var226 = -0.0036288307
    else:
        var226 = -0.01938326
    if input[1] < 89.78451:
        if input[3] < 46.53431:
            var227 = 0.010861937
        else:
            var227 = -0.0025059637
    else:
        var227 = -0.019099234
    if input[1] < 92.115944:
        if input[3] < 46.949734:
            var228 = 0.010917663
        else:
            var228 = -0.003122854
    else:
        var228 = -0.019406116
    if input[1] < 92.115944:
        if input[3] < 46.426273:
            var229 = 0.010557403
        else:
            var229 = -0.00241881
    else:
        var229 = -0.019134754
    if input[1] < 89.78451:
        if input[1] < 61.035255:
            var230 = -0.0016701721
        else:
            var230 = 0.0108622005
    else:
        var230 = -0.018056681
    if input[1] < 89.78451:
        if input[1] < 61.035255:
            var231 = -0.0014553763
        else:
            var231 = 0.010732307
    else:
        var231 = -0.017808758
    if input[3] < 37.808918:
        if input[1] < 71.12743:
            var232 = 0.0037858223
        else:
            var232 = -0.022836387
    else:
        var232 = 0.010448459
    if input[1] < 89.929855:
        if input[1] < 61.035255:
            var233 = -0.0016079936
        else:
            var233 = 0.01046679
    else:
        var233 = -0.01699032
    if input[3] < 37.808918:
        var234 = -0.012426584
    else:
        var234 = 0.009913985
    if input[1] < 89.78451:
        if input[3] < 43.847084:
            var235 = 0.009070525
        else:
            var235 = 0.0000912657
    else:
        var235 = -0.01615747
    if input[3] < 37.808918:
        var236 = -0.012002138
    else:
        var236 = 0.009511941
    if input[1] < 89.929855:
        if input[3] < 43.847084:
            var237 = 0.009330901
        else:
            var237 = -0.0004325658
    else:
        var237 = -0.015453695
    if input[3] < 37.808918:
        var238 = -0.0115957465
    else:
        var238 = 0.009268554
    if input[1] < 89.929855:
        if input[3] < 43.847084:
            var239 = 0.009283716
        else:
            var239 = -0.00065564277
    else:
        var239 = -0.014690545
    if input[3] < 37.808918:
        var240 = -0.011204993
    else:
        var240 = 0.009157944
    if input[3] < 37.808918:
        var241 = -0.010798715
    else:
        var241 = 0.00891246
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var242 = 0.009315176
        else:
            var242 = -0.00083794066
    else:
        var242 = -0.013809352
    if input[3] < 37.808918:
        var243 = -0.010473829
    else:
        var243 = 0.0088177845
    if input[3] < 37.808918:
        var244 = -0.0101047205
    else:
        var244 = 0.008583832
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var245 = 0.009446316
        else:
            var245 = -0.001231304
    else:
        var245 = -0.013055453
    if input[3] < 37.808918:
        var246 = -0.009838401
    else:
        var246 = 0.008504682
    if input[3] < 37.808918:
        var247 = -0.009500927
    else:
        var247 = 0.008281025
    if input[1] < 89.929855:
        if input[3] < 43.847084:
            var248 = 0.009678982
        else:
            var248 = -0.0018297803
    else:
        var248 = -0.012413758
    var249 = var193 + var194 + var195 + var196 + var197 + var198 + var199 + var200 + var201 + var202 + var203 + var204 + var205 + var206 + var207 + var208 + var209 + var210 + var211 + var212 + var213 + var214 + var215 + var216 + var217 + var218 + var219 + var220 + var221 + var222 + var223 + var224 + var225 + var226 + var227 + var228 + var229 + var230 + var231 + var232 + var233 + var234 + var235 + var236 + var237 + var238 + var239 + var240 + var241 + var242 + var243 + var244 + var245 + var246 + var247 + var248
    if input[3] < 37.808918:
        var250 = -0.009287967
    else:
        var250 = 0.008217535
    if input[3] < 37.808918:
        var251 = -0.008977303
    else:
        var251 = 0.008002823
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var252 = 0.009592611
        else:
            var252 = -0.0019065542
    else:
        var252 = -0.0117837675
    if input[3] < 37.808918:
        var253 = -0.00880212
    else:
        var253 = 0.00794941
    if input[1] < 89.929855:
        if input[3] < 43.847084:
            var254 = 0.009592754
        else:
            var254 = -0.002262904
    else:
        var254 = -0.011337726
    if input[3] < 37.808918:
        var255 = -0.008643331
    else:
        var255 = 0.007896053
    if input[3] < 37.808918:
        var256 = -0.00836397
    else:
        var256 = 0.0076903873
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var257 = 0.009483936
        else:
            var257 = -0.0023086693
    else:
        var257 = -0.010812164
    if input[3] < 37.808918:
        var258 = -0.008234514
    else:
        var258 = 0.007646384
    if input[3] < 37.808918:
        var259 = -0.007973487
    else:
        var259 = 0.0074479342
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var260 = 0.009498189
        else:
            var260 = -0.0025702026
    else:
        var260 = -0.010360908
    if input[3] < 37.808918:
        var261 = -0.007871582
    else:
        var261 = 0.007412754
    if input[3] < 37.808918:
        var262 = -0.007626804
    else:
        var262 = 0.007221561
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var263 = 0.009496853
        else:
            var263 = -0.002809067
    else:
        var263 = -0.009952198
    if input[3] < 37.808918:
        var264 = -0.0075480095
    else:
        var264 = 0.0071943826
    if input[3] < 37.808918:
        var265 = -0.0073170364
    else:
        var265 = 0.007009357
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var266 = 0.0094822645
        else:
            var266 = -0.0030273902
    else:
        var266 = -0.009579921
    if input[3] < 37.808918:
        var267 = -0.0072581694
    else:
        var267 = 0.0069896677
    if input[3] < 37.808918:
        var268 = -0.007039158
    else:
        var268 = 0.006809813
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var269 = 0.009458105
        else:
            var269 = -0.0032278032
    else:
        var269 = -0.009240703
    if input[3] < 37.808918:
        var270 = -0.0069970316
    else:
        var270 = 0.0067967414
    if input[3] < 37.808918:
        var271 = -0.0067884424
    else:
        var271 = 0.0066224723
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var272 = 0.009426115
        else:
            var272 = -0.0034112025
    else:
        var272 = -0.008929964
    if input[3] < 37.808918:
        var273 = -0.006760531
    else:
        var273 = 0.0066153514
    if input[3] < 37.808918:
        var274 = -0.0065610404
    else:
        var274 = 0.0064453334
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var275 = 0.009388032
        else:
            var275 = -0.003580105
    else:
        var275 = -0.008644435
    if input[3] < 37.808918:
        var276 = -0.0065452033
    else:
        var276 = 0.0064436607
    if input[3] < 37.808918:
        var277 = -0.0063568377
    else:
        var277 = 0.0062677944
    if input[1] < 89.78451:
        if input[3] < 43.63282:
            var278 = 0.009372469
        else:
            var278 = -0.0037334212
    else:
        var278 = -0.008432689
    if input[3] < 37.808918:
        var279 = -0.0063539906
    else:
        var279 = 0.0062611834
    if input[3] < 49.704082:
        if input[1] < 71.20408:
            var280 = 0.0071979314
        else:
            var280 = 0.00021041487
    else:
        var280 = -0.008422087
    if input[3] < 37.808918:
        var281 = -0.006310848
    else:
        var281 = 0.0062505626
    if input[1] < 86.58795:
        if input[1] < 68.66822:
            var282 = -0.0021108247
        else:
            var282 = 0.01020848
    else:
        var282 = -0.007924876
    if input[3] < 37.808918:
        var283 = -0.0061681983
    else:
        var283 = 0.006141912
    if input[3] < 49.704082:
        if input[1] < 71.20408:
            var284 = 0.0072486894
        else:
            var284 = 0.00025037566
    else:
        var284 = -0.00840735
    if input[3] < 37.808918:
        var285 = -0.0061292634
    else:
        var285 = 0.006142746
    if input[3] < 49.355618:
        if input[1] < 71.20408:
            var286 = 0.006991294
        else:
            var286 = 0.00024620496
    else:
        var286 = -0.008032046
    if input[3] < 37.808918:
        var287 = -0.0060883793
    else:
        var287 = 0.0061258962
    if input[1] < 86.58795:
        if input[1] < 68.66822:
            var288 = -0.0020472088
        else:
            var288 = 0.010038801
    else:
        var288 = -0.007729899
    if input[3] < 37.808918:
        var289 = -0.0059514716
    else:
        var289 = 0.006014828
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var290 = 0.007067776
        else:
            var290 = 0.0002991587
    else:
        var290 = -0.00803109
    if input[3] < 37.808918:
        var291 = -0.005914729
    else:
        var291 = 0.006011236
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var292 = 0.0069662035
        else:
            var292 = 0.0003397726
    else:
        var292 = -0.007944128
    if input[3] < 37.808918:
        var293 = -0.005879177
    else:
        var293 = 0.0059936554
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var294 = 0.0069363983
        else:
            var294 = 0.00030957093
    else:
        var294 = -0.007866878
    if input[3] < 37.808918:
        var295 = -0.0058389516
    else:
        var295 = 0.0059841336
    if input[1] < 86.58795:
        if input[1] < 68.66822:
            var296 = -0.0020332919
        else:
            var296 = 0.00991321
    else:
        var296 = -0.0075230496
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var297 = 0.0068714577
        else:
            var297 = 0.0003140288
    else:
        var297 = -0.0077500455
    if input[3] < 37.808918:
        var298 = -0.005837082
    else:
        var298 = 0.0060128537
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var299 = 0.0067785266
        else:
            var299 = 0.000355626
    else:
        var299 = -0.0076773823
    if input[3] < 37.808918:
        var300 = -0.005795237
    else:
        var300 = 0.0059840097
    if input[3] < 49.355618:
        if input[1] < 70.20504:
            var301 = 0.0067549064
        else:
            var301 = 0.00032795887
    else:
        var301 = -0.007612997
    if input[3] < 37.808918:
        var302 = -0.0057496913
    else:
        var302 = 0.0059640436
    if input[1] < 86.58795:
        if input[1] < 68.40831:
            var303 = -0.0018638255
        else:
            var303 = 0.00952651
    else:
        var303 = -0.0073285657
    if input[3] < 54.91084:
        var304 = -0.07564052
    else:
        var304 = 0.14590536
    if input[3] < 54.91084:
        var305 = -0.07271077
    else:
        var305 = 0.12693621
    if input[3] < 54.91084:
        var306 = -0.070147865
    else:
        var306 = 0.113057315
    if input[3] < 54.91084:
        var307 = -0.067898616
    else:
        var307 = 0.10251863
    if input[3] < 54.91084:
        var308 = -0.065919265
    else:
        var308 = 0.09428846
    if input[3] < 54.91084:
        var309 = -0.06417355
    else:
        var309 = 0.08771806
    if input[3] < 54.91084:
        var310 = -0.0626292
    else:
        var310 = 0.082379006
    if input[3] < 54.91084:
        var311 = -0.061260622
    else:
        var311 = 0.077976786
    if input[3] < 54.91084:
        var312 = -0.060044706
    else:
        var312 = 0.07430249
    if input[3] < 54.91084:
        var313 = -0.058961928
    else:
        var313 = 0.07120377
    if input[3] < 54.91084:
        var314 = -0.057995487
    else:
        var314 = 0.06856704
    if input[3] < 54.91084:
        var315 = -0.057130825
    else:
        var315 = 0.06630587
    if input[3] < 54.91084:
        var316 = -0.05635534
    else:
        var316 = 0.06435334
    if input[3] < 54.91084:
        var317 = -0.055658042
    else:
        var317 = 0.062656894
    if input[3] < 54.91084:
        var318 = -0.055029344
    else:
        var318 = 0.06117465
    if input[3] < 54.91084:
        var319 = -0.05446082
    else:
        var319 = 0.059872806
    if input[3] < 54.91084:
        var320 = -0.05394506
    else:
        var320 = 0.058723815
    if input[3] < 54.91084:
        var321 = -0.053475518
    else:
        var321 = 0.057704944
    if input[3] < 54.91084:
        var322 = -0.05304637
    else:
        var322 = 0.056797314
    if input[3] < 54.91084:
        var323 = -0.05265243
    else:
        var323 = 0.05598504
    if input[3] < 54.91084:
        var324 = -0.052289035
    else:
        var324 = 0.05525468
    if input[3] < 54.91084:
        var325 = -0.051952
    else:
        var325 = 0.054594763
    if input[3] < 54.91084:
        var326 = -0.05163751
    else:
        var326 = 0.05399543
    if input[3] < 54.91084:
        var327 = -0.05134211
    else:
        var327 = 0.053448107
    if input[3] < 54.91084:
        var328 = -0.05106262
    else:
        var328 = 0.052945334
    if input[3] < 54.91084:
        var329 = -0.050796535
    else:
        var329 = 0.05248052
    if input[3] < 54.91084:
        var330 = -0.05054083
    else:
        var330 = 0.052047826
    if input[3] < 54.91084:
        var331 = -0.050293017
    else:
        var331 = 0.051642057
    if input[3] < 54.91084:
        var332 = -0.050050687
    else:
        var332 = 0.05125853
    if input[3] < 54.91084:
        var333 = -0.049811643
    else:
        var333 = 0.050892986
    if input[3] < 54.91084:
        var334 = -0.049573716
    else:
        var334 = 0.050541587
    if input[3] < 54.91084:
        var335 = -0.04933492
    else:
        var335 = 0.05020077
    if input[3] < 54.91084:
        var336 = -0.04909326
    else:
        var336 = 0.049867257
    if input[3] < 54.91084:
        var337 = -0.048846923
    else:
        var337 = 0.049538035
    if input[3] < 54.91084:
        var338 = -0.04859114
    else:
        var338 = 0.049210228
    if input[3] < 54.91084:
        var339 = -0.048326727
    else:
        var339 = 0.048881233
    if input[3] < 54.91084:
        var340 = -0.048051935
    else:
        var340 = 0.048548575
    if input[3] < 54.91084:
        var341 = -0.047765072
    else:
        var341 = 0.048209917
    if input[3] < 54.91084:
        var342 = -0.047464516
    else:
        var342 = 0.047863096
    if input[3] < 54.91084:
        var343 = -0.047148712
    else:
        var343 = 0.047506105
    if input[3] < 54.91084:
        var344 = -0.04681619
    else:
        var344 = 0.047137078
    var345 = var304 + var305 + var306 + var307 + var308 + var309 + var310 + var311 + var312 + var313 + var314 + var315 + var316 + var317 + var318 + var319 + var320 + var321 + var322 + var323 + var324 + var325 + var326 + var327 + var328 + var329 + var330 + var331 + var332 + var333 + var334 + var335 + var336 + var337 + var338 + var339 + var340 + var341 + var342 + var343 + var344
    if input[3] < 54.91084:
        var346 = -0.04646558
    else:
        var346 = 0.046754267
    if input[3] < 54.91084:
        var347 = -0.046095606
    else:
        var347 = 0.046356212
    if input[3] < 54.91084:
        var348 = -0.045705132
    else:
        var348 = 0.045941442
    if input[3] < 54.91084:
        var349 = -0.045293164
    else:
        var349 = 0.045508858
    if input[3] < 54.91084:
        var350 = -0.04485886
    else:
        var350 = 0.045057382
    if input[3] < 54.91084:
        var351 = -0.044401586
    else:
        var351 = 0.044586316
    if input[3] < 54.91084:
        var352 = -0.043920886
    else:
        var352 = 0.0440951
    if input[3] < 54.91084:
        var353 = -0.043416526
    else:
        var353 = 0.04358348
    if input[3] < 54.91084:
        var354 = -0.042888515
    else:
        var354 = 0.043051276
    if input[3] < 54.91084:
        var355 = -0.04233553
    else:
        var355 = 0.042498793
    if input[3] < 54.91084:
        var356 = -0.04176112
    else:
        var356 = 0.04192648
    if input[3] < 54.91084:
        var357 = -0.041165676
    else:
        var357 = 0.041334864
    if input[3] < 54.91084:
        var358 = -0.040549193
    else:
        var358 = 0.04072498
    if input[3] < 54.91084:
        var359 = -0.039930344
    else:
        var359 = 0.04009793
    if input[3] < 54.91084:
        var360 = -0.039296847
    else:
        var360 = 0.039454907
    if input[3] < 54.91084:
        var361 = -0.03864958
    else:
        var361 = 0.03879761
    if input[3] < 54.91084:
        var362 = -0.03799094
    else:
        var362 = 0.038127344
    if input[3] < 54.91084:
        var363 = -0.03732344
    else:
        var363 = 0.037446167
    if input[3] < 54.91084:
        var364 = -0.036651935
    else:
        var364 = 0.03675577
    if input[3] < 54.91084:
        var365 = -0.035981197
    else:
        var365 = 0.03605799
    if input[3] < 54.91084:
        var366 = -0.035312057
    else:
        var366 = 0.035354752
    if input[3] < 54.91084:
        var367 = -0.034623213
    else:
        var367 = 0.034648582
    if input[3] < 54.91084:
        var368 = -0.033951353
    else:
        var368 = 0.033941206
    if input[3] < 54.91084:
        var369 = -0.03326359
    else:
        var369 = 0.03323453
    if input[3] < 54.91084:
        var370 = -0.03264509
    else:
        var370 = 0.032530546
    if input[3] < 54.91084:
        var371 = -0.03203841
    else:
        var371 = 0.031834405
    if input[3] < 54.91084:
        var372 = -0.031324085
    else:
        var372 = 0.0311546
    if input[3] < 54.91084:
        var373 = -0.030627077
    else:
        var373 = 0.030494222
    if input[3] < 54.91084:
        var374 = -0.029949455
    else:
        var374 = 0.029854273
    if input[3] < 54.91084:
        var375 = -0.029425938
    else:
        var375 = 0.029265353
    if input[3] < 54.91084:
        var376 = -0.028913114
    else:
        var376 = 0.028688828
    if input[3] < 54.91084:
        var377 = -0.028412137
    else:
        var377 = 0.028127184
    if input[3] < 54.91084:
        var378 = -0.027991721
    else:
        var378 = 0.027579477
    if input[3] < 54.91084:
        var379 = -0.027510062
    else:
        var379 = 0.027045831
    if input[3] < 54.91084:
        var380 = -0.02703995
    else:
        var380 = 0.026528442
    if input[3] < 54.91084:
        var381 = -0.026576122
    else:
        var381 = 0.026021753
    if input[3] < 54.91084:
        var382 = -0.026189784
    else:
        var382 = 0.025528297
    if input[3] < 54.91084:
        var383 = -0.025737232
    else:
        var383 = 0.02508877
    var384 = var345 + var346 + var347 + var348 + var349 + var350 + var351 + var352 + var353 + var354 + var355 + var356 + var357 + var358 + var359 + var360 + var361 + var362 + var363 + var364 + var365 + var366 + var367 + var368 + var369 + var370 + var371 + var372 + var373 + var374 + var375 + var376 + var377 + var378 + var379 + var380 + var381 + var382 + var383 + -0.00081466226 + -0.00054106885 + -0.0004771653 + -0.00022593283 + -0.00023416965 + 0.0000012228654 + -0.000048702277 + 0.0001453844 + 0.00008811637 + 0.0002729492 + 0.00044382372 + 0.00037260883 + 0.0005370369 + 0.00068938057 + 0.0006041379 + 0.0007517844 + 0.0008892337
    return softmax([0.5 + (var97 + var98 + var99 + var100 + var101 + var102 + var103 + var104 + var105 + var106 + var107 + var108 + var109 + var110 + var111 + var112 + var113 + var114 + var115 + var116 + var117 + var118 + var119 + var120 + var121 + var122 + var123 + var124 + var125 + var126 + var127 + var128 + var129 + var130 + var131 + var132 + var133 + var134 + var135 + var136 + var137 + var138 + var139 + var140 + var141 + var142 + var143 + var144 + var145 + var146 + var147 + var148 + var149 + var150 + var151), 0.5 + (var249 + var250 + var251 + var252 + var253 + var254 + var255 + var256 + var257 + var258 + var259 + var260 + var261 + var262 + var263 + var264 + var265 + var266 + var267 + var268 + var269 + var270 + var271 + var272 + var273 + var274 + var275 + var276 + var277 + var278 + var279 + var280 + var281 + var282 + var283 + var284 + var285 + var286 + var287 + var288 + var289 + var290 + var291 + var292 + var293 + var294 + var295 + var296 + var297 + var298 + var299 + var300 + var301 + var302 + var303), 0.5 + (var384 + 0.0007927948 + 0.00092540117 + 0.0010491578 + 0.0009453351 + 0.0010654097 + 0.00095831056 + 0.0010776458 + 0.001187601 + 0.0010751552 + 0.0011826169 + 0.001282276 + 0.0011633435 + 0.0012634395 + 0.0013545456 + 0.0012305032 + 0.0013222275 + 0.0014059409 + 0.0012786312 + 0.001364472 + 0.0014424826 + 0.0013119446 + 0.0013918229 + 0.001464468 + 0.0013318289 + 0.0014067304 + 0.0014762657 + 0.0013406754 + 0.0014156586 + 0.001479957 + 0.0013473497 + 0.0014181117 + 0.0012672116 + 0.0013400441 + 0.0012771229 + 0.0013481908 + 0.0011959433 + 0.0012701687 + 0.0011277976 + 0.0012033322 + 0.0011467743 + 0.0012188981 + 0.0010744048 + 0.001149847 + 0.0010125859 + 0.0010887467 + 0.0009520993 + 0.001030953 + 0.0009840195 + 0.00085270184 + 0.00093550386 + 0.0008098231 + 0.0008932735 + 0.000766849 + 0.0008514868)])


def predict_proba(input_features):
    # m2cgen score function returns raw margins for each class
    scores = score(input_features)
    
    # Softmax conversion
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    
    probs = [e / sum_exp for e in exp_scores]
    return probs
