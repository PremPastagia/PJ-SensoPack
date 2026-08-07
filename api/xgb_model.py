
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
    if input[2] < 417.8072:
        if input[4] < 7.310009:
            if input[5] < 4452.413:
                var0 = 0.14949562
            else:
                var0 = 0.0000000025544848
        else:
            if input[0] < 26.110664:
                var0 = 0.10344829
            else:
                if input[0] < 29.257029:
                    var0 = -0.048
                else:
                    var0 = 0.0000000025544848
    else:
        if input[2] < 433.85468:
            if input[5] < 4693.2686:
                if input[1] < 83.43807:
                    if input[5] < 537.6977:
                        var0 = 0.027272731
                    else:
                        var0 = 0.11294118
                else:
                    if input[4] < 7.243017:
                        var0 = 0.060000002
                    else:
                        var0 = -0.04
            else:
                var0 = -0.067058824
        else:
            if input[4] < 7.293997:
                if input[2] < 462.86743:
                    if input[5] < 888.78937:
                        var0 = 0.064864874
                    else:
                        var0 = -0.027522935
                else:
                    var0 = -0.06
            else:
                if input[4] < 7.322918:
                    if input[0] < 32.755127:
                        var0 = -0.0652174
                    else:
                        var0 = -0.008108105
                else:
                    var0 = -0.07494571
    if input[2] < 429.77728:
        if input[5] < 4554.5503:
            if input[4] < 7.256852:
                var1 = 0.12953372
            else:
                if input[1] < 66.80687:
                    var1 = 0.097303145
                else:
                    if input[0] < 32.23246:
                        var1 = 0.0007565972
                    else:
                        var1 = 0.08288061
        else:
            if input[4] < 7.3523836:
                var1 = -0.06043693
            else:
                var1 = 0.0005945946
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var1 = -0.0026498754
                    else:
                        var1 = 0.09016998
                else:
                    var1 = -0.05294174
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var1 = -0.00051483925
                    else:
                        var1 = -0.06521382
                else:
                    if input[5] < 4693.2686:
                        var1 = 0.10377884
                    else:
                        var1 = -0.059588023
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var1 = 0.04297202
                else:
                    if input[0] < 35.580082:
                        var1 = -0.06812402
                    else:
                        var1 = 0.0020826072
            else:
                var1 = -0.07216959
    if input[2] < 429.77728:
        if input[5] < 4554.5503:
            if input[4] < 7.256852:
                var2 = 0.11500207
            else:
                if input[1] < 97.78946:
                    if input[4] < 7.3376346:
                        var2 = 0.08209633
                    else:
                        var2 = 0.0029815438
                else:
                    var2 = -0.02305522
        else:
            if input[0] < 27.043375:
                var2 = 0.0012032486
            else:
                var2 = -0.059005387
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var2 = -0.002310672
                    else:
                        var2 = 0.085474856
                else:
                    var2 = -0.0515497
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var2 = -0.0002263271
                    else:
                        var2 = -0.063449614
                else:
                    if input[5] < 4693.2686:
                        var2 = 0.09850777
                    else:
                        var2 = -0.057985168
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var2 = 0.04290509
                else:
                    if input[0] < 35.580082:
                        var2 = -0.06570483
                    else:
                        var2 = 0.00328341
            else:
                var2 = -0.06973567
    if input[2] < 429.77728:
        if input[5] < 4554.5503:
            if input[4] < 7.256852:
                var3 = 0.104028046
            else:
                if input[0] < 25.986551:
                    if input[0] < 21.101826:
                        var3 = 0.013369891
                    else:
                        var3 = 0.0873844
                else:
                    if input[0] < 30.878813:
                        var3 = -0.046845477
                    else:
                        var3 = 0.07283332
        else:
            if input[4] < 7.3523836:
                var3 = -0.057590097
            else:
                var3 = 0.0016894011
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[4] < 7.1964808:
                        var3 = -0.0026011749
                    else:
                        var3 = 0.08186121
                else:
                    var3 = -0.050200652
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var3 = 0.00010555298
                    else:
                        var3 = -0.0617869
                else:
                    if input[5] < 4693.2686:
                        var3 = 0.093922205
                    else:
                        var3 = -0.05645559
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var3 = 0.042893738
                else:
                    if input[0] < 35.580082:
                        var3 = -0.06352517
                    else:
                        var3 = 0.0044862223
            else:
                var3 = -0.067598686
    if input[2] < 429.77728:
        if input[5] < 4554.5503:
            if input[4] < 7.256852:
                var4 = 0.09548984
            else:
                if input[1] < 66.80687:
                    if input[0] < 25.986551:
                        var4 = 0.0860981
                    else:
                        var4 = 0.025305614
                else:
                    if input[0] < 30.878813:
                        var4 = -0.0076152976
                    else:
                        var4 = 0.06150036
        else:
            if input[0] < 27.043375:
                var4 = 0.0026644939
            else:
                var4 = -0.055877473
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var4 = -0.00284091
                    else:
                        var4 = 0.07780805
                else:
                    var4 = -0.048855826
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var4 = 0.000025441428
                    else:
                        var4 = -0.06017977
                else:
                    if input[5] < 4693.2686:
                        var4 = 0.089785755
                    else:
                        var4 = -0.054740738
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var4 = 0.042007226
                else:
                    if input[0] < 35.580082:
                        var4 = -0.061717656
                    else:
                        var4 = 0.0056863464
            else:
                var4 = -0.06571694
    if input[2] < 429.77728:
        if input[5] < 4554.5503:
            if input[4] < 7.256852:
                var5 = 0.08869563
            else:
                if input[1] < 97.78946:
                    if input[4] < 7.322918:
                        var5 = 0.07323198
                    else:
                        var5 = 0.009703799
                else:
                    var5 = -0.024959406
        else:
            if input[4] < 7.3523836:
                var5 = -0.054268237
            else:
                var5 = 0.0036018768
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var5 = -0.0028751255
                    else:
                        var5 = 0.07413762
                else:
                    var5 = -0.047565218
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var5 = -0.000021426873
                    else:
                        var5 = -0.05867361
                else:
                    if input[5] < 4693.2686:
                        var5 = 0.08612527
                    else:
                        var5 = -0.053125598
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var5 = 0.041207805
                else:
                    if input[0] < 35.580082:
                        var5 = -0.060078826
                    else:
                        var5 = 0.0068766163
            else:
                var5 = -0.06405609
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var6 = 0.08335906
                else:
                    var6 = 0.026327902
            else:
                var6 = 0.030030167
        else:
            if input[5] < 4315.5137:
                if input[1] < 97.78946:
                    if input[5] < 537.6977:
                        var6 = -0.0066711954
                    else:
                        var6 = 0.073366314
                else:
                    var6 = -0.047451515
            else:
                var6 = -0.053231914
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var6 = -0.0029604153
                    else:
                        var6 = 0.07116135
                else:
                    var6 = -0.046252105
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var6 = 0.00016574033
                    else:
                        var6 = -0.057187654
                else:
                    if input[5] < 4693.2686:
                        var6 = 0.08290488
                    else:
                        var6 = -0.05156211
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var6 = 0.04040601
                else:
                    if input[0] < 35.580082:
                        var6 = -0.058600802
                    else:
                        var6 = 0.0076633194
            else:
                var6 = -0.06258646
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var7 = 0.07882177
                else:
                    var7 = 0.02479378
            else:
                var7 = 0.02803053
        else:
            if input[5] < 4315.5137:
                if input[1] < 97.78946:
                    if input[5] < 537.6977:
                        var7 = -0.007164176
                    else:
                        var7 = 0.06911738
                else:
                    var7 = -0.046865106
            else:
                var7 = -0.05161506
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[4] < 7.1964808:
                        var7 = -0.0033018345
                    else:
                        var7 = 0.06862848
                else:
                    var7 = -0.04499717
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var7 = 0.00035428672
                    else:
                        var7 = -0.055796307
                else:
                    if input[5] < 4693.2686:
                        var7 = 0.08035803
                    else:
                        var7 = -0.050113317
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var7 = 0.039649263
                else:
                    if input[0] < 35.580082:
                        var7 = -0.057222296
                    else:
                        var7 = 0.00842677
            else:
                var7 = -0.061283227
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var8 = 0.075045444
                else:
                    var8 = 0.023363618
            else:
                var8 = 0.026191363
        else:
            if input[0] < 25.986551:
                if input[4] < 7.3376346:
                    if input[0] < 20.804243:
                        var8 = 0.019987782
                    else:
                        var8 = 0.078558765
                else:
                    var8 = -0.013410091
            else:
                if input[0] < 35.9314:
                    if input[4] < 7.243017:
                        var8 = 0.007444415
                    else:
                        var8 = -0.041749757
                else:
                    if input[4] < 7.2781405:
                        var8 = 0.065955155
                    else:
                        var8 = -0.007716106
    else:
        if input[4] < 7.293997:
            if input[5] < 888.78937:
                if input[2] < 462.86743:
                    if input[3] < 21.621714:
                        var8 = -0.0038451576
                    else:
                        var8 = 0.06568163
                else:
                    var8 = -0.044240475
            else:
                if input[5] < 3097.8657:
                    if input[1] < 47.170612:
                        var8 = 0.00019596203
                    else:
                        var8 = -0.05490297
                else:
                    if input[5] < 4693.2686:
                        var8 = 0.07694731
                    else:
                        var8 = -0.048554193
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var8 = 0.039749283
                else:
                    if input[0] < 35.580082:
                        var8 = -0.055817008
                    else:
                        var8 = 0.0095552495
            else:
                var8 = -0.060126074
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var9 = 0.07186939
                else:
                    var9 = 0.02202733
            else:
                var9 = 0.024494587
        else:
            if input[5] < 4315.5137:
                if input[1] < 97.78946:
                    if input[5] < 537.6977:
                        var9 = -0.0074274302
                    else:
                        var9 = 0.064370655
                else:
                    var9 = -0.045383807
            else:
                var9 = -0.049515944
    else:
        if input[4] < 7.293997:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[4] < 7.1964808:
                        var9 = -0.004005276
                    else:
                        var9 = 0.06280806
                else:
                    if input[5] < 3097.8657:
                        var9 = -0.041847773
                    else:
                        var9 = 0.009609732
            else:
                var9 = -0.049397483
        else:
            if input[2] < 452.94366:
                if input[1] < 44.30488:
                    var9 = 0.03986412
                else:
                    if input[0] < 35.580082:
                        var9 = -0.054511826
                    else:
                        var9 = 0.01065724
            else:
                var9 = -0.059099484
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var10 = 0.06917419
                else:
                    var10 = 0.020776259
            else:
                var10 = 0.022924956
        else:
            if input[0] < 25.986551:
                if input[4] < 7.3376346:
                    if input[0] < 20.804243:
                        var10 = 0.017606786
                    else:
                        var10 = 0.07352197
                else:
                    var10 = -0.0152431745
            else:
                if input[0] < 35.9314:
                    if input[4] < 7.243017:
                        var10 = 0.005826916
                    else:
                        var10 = -0.03976616
                else:
                    if input[4] < 7.2781405:
                        var10 = 0.061809044
                    else:
                        var10 = -0.0076238364
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var10 = 0.070961684
                    else:
                        var10 = -0.0010581259
                else:
                    if input[1] < 46.92819:
                        var10 = 0.042650763
                    else:
                        var10 = -0.029099587
            else:
                var10 = -0.052590974
        else:
            if input[2] < 433.85468:
                var10 = 0.0016459288
            else:
                var10 = -0.058196165
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var11 = 0.066869445
                else:
                    var11 = 0.019602975
            else:
                var11 = 0.021469578
        else:
            if input[0] < 25.986551:
                if input[4] < 7.3376346:
                    if input[0] < 20.804243:
                        var11 = 0.016563183
                    else:
                        var11 = 0.070777886
                else:
                    var11 = -0.013918096
            else:
                if input[0] < 37.875954:
                    if input[4] < 7.243017:
                        var11 = 0.01833049
                    else:
                        var11 = -0.0416166
                else:
                    var11 = 0.056556184
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var11 = 0.06880363
                    else:
                        var11 = -0.000181207
                else:
                    if input[1] < 46.92819:
                        var11 = 0.041915983
                    else:
                        var11 = -0.02732852
            else:
                var11 = -0.051480632
        else:
            if input[2] < 433.85468:
                var11 = 0.002710829
            else:
                var11 = -0.05737859
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var12 = 0.06488543
                else:
                    var12 = 0.018501032
            else:
                var12 = 0.020117437
        else:
            if input[5] < 4315.5137:
                if input[1] < 97.78946:
                    if input[5] < 537.6977:
                        var12 = -0.008962645
                    else:
                        var12 = 0.05855572
                else:
                    var12 = -0.043788146
            else:
                var12 = -0.04709178
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var12 = 0.06679057
                    else:
                        var12 = 0.0006503343
                else:
                    if input[1] < 46.92819:
                        var12 = 0.041200362
                    else:
                        var12 = -0.025613187
            else:
                var12 = -0.050429363
        else:
            if input[2] < 433.85468:
                var12 = 0.0033931003
            else:
                var12 = -0.05665005
    if input[2] < 429.77728:
        if input[4] < 7.256852:
            if input[5] < 4554.5503:
                var13 = 0.06305875
            else:
                var13 = -0.03901408
        else:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var13 = -0.0016421321
                else:
                    if input[1] < 79.73578:
                        var13 = 0.06681534
                    else:
                        var13 = 0.025207058
            else:
                if input[0] < 30.878813:
                    if input[0] < 26.50474:
                        var13 = -0.0075257765
                    else:
                        var13 = -0.060345113
                else:
                    if input[3] < 122.0666:
                        var13 = 0.049658302
                    else:
                        var13 = -0.030419165
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var13 = 0.064184345
                    else:
                        var13 = 0.00079056807
                else:
                    if input[1] < 46.92819:
                        var13 = 0.0398644
                    else:
                        var13 = -0.024575913
            else:
                var13 = -0.049163714
        else:
            if input[2] < 433.85468:
                var13 = 0.0043179216
            else:
                var13 = -0.055998612
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var14 = 0.061675925
                else:
                    var14 = 0.016253946
            else:
                var14 = 0.01823767
        else:
            if input[0] < 25.986551:
                if input[4] < 7.3376346:
                    if input[0] < 20.804243:
                        var14 = 0.014381629
                    else:
                        var14 = 0.065493375
                else:
                    var14 = -0.013207199
            else:
                if input[0] < 35.9314:
                    if input[1] < 80.43887:
                        var14 = -0.036601577
                    else:
                        var14 = 0.0018651979
                else:
                    if input[4] < 7.2781405:
                        var14 = 0.055474658
                    else:
                        var14 = -0.0063219927
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var14 = 0.06176884
                    else:
                        var14 = 0.000918726
                else:
                    if input[5] < 3138.0425:
                        var14 = -0.03437255
                    else:
                        var14 = 0.012998995
            else:
                var14 = -0.047950935
        else:
            if input[2] < 433.85468:
                var14 = 0.0052167033
            else:
                var14 = -0.055414807
    if input[2] < 429.77728:
        if input[4] < 7.256852:
            if input[5] < 4554.5503:
                var15 = 0.060240965
            else:
                var15 = -0.038502675
        else:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var15 = -0.0019287696
                else:
                    if input[1] < 79.73578:
                        var15 = 0.06356939
                    else:
                        var15 = 0.023427783
            else:
                if input[0] < 30.878813:
                    if input[0] < 26.50474:
                        var15 = -0.008963874
                    else:
                        var15 = -0.05877163
                else:
                    if input[1] < 75.8811:
                        var15 = -0.005852353
                    else:
                        var15 = 0.05628232
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var15 = 0.059949912
                    else:
                        var15 = 0.0014693288
                else:
                    if input[5] < 3138.0425:
                        var15 = -0.032909814
                    else:
                        var15 = 0.012960257
            else:
                var15 = -0.046965852
        else:
            if input[2] < 433.85468:
                var15 = 0.0056114756
            else:
                var15 = -0.054889858
    if input[2] < 429.77728:
        if input[4] < 7.256852:
            if input[5] < 4554.5503:
                var16 = 0.05907464
            else:
                var16 = -0.03773723
        else:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var16 = -0.0022194674
                else:
                    if input[1] < 79.73578:
                        var16 = 0.061658558
                    else:
                        var16 = 0.02264486
            else:
                if input[0] < 30.878813:
                    if input[0] < 26.50474:
                        var16 = -0.008991377
                    else:
                        var16 = -0.057363313
                else:
                    if input[1] < 75.8811:
                        var16 = -0.005491408
                    else:
                        var16 = 0.054918032
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 4693.2686:
                    if input[5] < 3138.0425:
                        var16 = 0.00093096326
                    else:
                        var16 = 0.08028745
                else:
                    var16 = -0.045316968
            else:
                var16 = -0.046243113
        else:
            if input[2] < 433.85468:
                var16 = 0.006109816
            else:
                var16 = -0.054418843
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var17 = 0.05821633
                else:
                    var17 = 0.013249583
            else:
                var17 = 0.015970442
        else:
            if input[5] < 4315.5137:
                if input[5] < 537.6977:
                    if input[2] < 417.8072:
                        var17 = -0.042893954
                    else:
                        var17 = 0.019079281
                else:
                    if input[1] < 97.78946:
                        var17 = 0.05253851
                    else:
                        var17 = -0.04032197
            else:
                var17 = -0.043363888
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var17 = 0.05833537
                    else:
                        var17 = 0.0015902243
                else:
                    if input[1] < 46.92819:
                        var17 = 0.04188156
                    else:
                        var17 = -0.022037221
            else:
                var17 = -0.045123283
        else:
            if input[2] < 433.85468:
                var17 = 0.0065758936
            else:
                var17 = -0.0539948
    if input[2] < 429.77728:
        if input[4] < 7.256852:
            if input[5] < 4554.5503:
                var18 = 0.05713386
            else:
                var18 = -0.036785524
        else:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var18 = -0.0037037488
                else:
                    if input[1] < 79.73578:
                        var18 = 0.05899783
                    else:
                        var18 = 0.020763652
            else:
                if input[0] < 30.878813:
                    if input[0] < 26.50474:
                        var18 = -0.009515843
                    else:
                        var18 = -0.0560575
                else:
                    if input[1] < 75.8811:
                        var18 = -0.005505111
                    else:
                        var18 = 0.05256738
    else:
        if input[4] < 7.322918:
            if input[2] < 462.86743:
                if input[5] < 888.78937:
                    if input[1] < 78.1442:
                        var18 = 0.05635571
                    else:
                        var18 = 0.001703673
                else:
                    if input[5] < 3138.0425:
                        var18 = -0.031395506
                    else:
                        var18 = 0.015642846
            else:
                var18 = -0.044472855
        else:
            if input[2] < 433.85468:
                var18 = 0.0072601335
            else:
                var18 = -0.05361236
    if input[2] < 429.77728:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var19 = 0.056529313
                else:
                    var19 = 0.011593121
            else:
                var19 = 0.014532076
        else:
            if input[5] < 4315.5137:
                if input[5] < 537.6977:
                    if input[2] < 417.8072:
                        var19 = -0.04253473
                    else:
                        var19 = 0.01760329
                else:
                    if input[1] < 97.78946:
                        var19 = 0.050089765
                    else:
                        var19 = -0.038848814
            else:
                var19 = -0.041603636
    else:
        if input[4] < 7.322918:
            if input[0] < 32.755127:
                if input[0] < 25.087263:
                    if input[0] < 22.883705:
                        var19 = -0.021758117
                    else:
                        var19 = 0.04972856
                else:
                    if input[1] < 90.31466:
                        var19 = -0.047332656
                    else:
                        var19 = 0.0072319726
            else:
                if input[0] < 38.797752:
                    if input[1] < 71.36714:
                        var19 = 0.08168768
                    else:
                        var19 = 0.006395889
                else:
                    var19 = -0.03163865
        else:
            if input[2] < 433.85468:
                var19 = 0.0076666633
            else:
                var19 = -0.053264447
    if input[2] < 429.77728:
        if input[4] < 7.256852:
            if input[5] < 4554.5503:
                var20 = 0.05558324
            else:
                var20 = -0.035846874
        else:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var20 = -0.0051206113
                else:
                    if input[1] < 79.73578:
                        var20 = 0.056655884
                    else:
                        var20 = 0.01835295
            else:
                if input[0] < 30.878813:
                    if input[3] < 117.19176:
                        var20 = -0.055783737
                    else:
                        var20 = -0.015746003
                else:
                    if input[1] < 75.8811:
                        var20 = -0.00551989
                    else:
                        var20 = 0.049943104
    else:
        if input[4] < 7.322918:
            if input[0] < 32.755127:
                if input[0] < 25.087263:
                    if input[0] < 22.883705:
                        var20 = -0.020611566
                    else:
                        var20 = 0.04742465
                else:
                    if input[1] < 90.31466:
                        var20 = -0.0460611
                    else:
                        var20 = 0.0072448477
            else:
                if input[0] < 38.797752:
                    if input[1] < 71.36714:
                        var20 = 0.07857092
                    else:
                        var20 = 0.0062781083
                else:
                    var20 = -0.030787725
        else:
            if input[2] < 433.85468:
                var20 = 0.008027165
            else:
                var20 = -0.05295151
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var21 = 0.055197295
                else:
                    var21 = 0.009630613
            else:
                var21 = 0.013043177
        else:
            if input[5] < 4693.2686:
                if input[4] < 7.3523836:
                    if input[3] < 13.104021:
                        var21 = -0.035116356
                    else:
                        var21 = 0.035454717
                else:
                    if input[3] < 13.104021:
                        var21 = 0.01377801
                    else:
                        var21 = -0.04750517
            else:
                var21 = -0.045691665
    else:
        if input[4] < 7.322918:
            if input[1] < 46.92819:
                var21 = 0.06333515
            else:
                if input[5] < 3138.0425:
                    if input[5] < 888.78937:
                        var21 = -0.00007223963
                    else:
                        var21 = -0.04923042
                else:
                    if input[5] < 4672.0903:
                        var21 = 0.064950146
                    else:
                        var21 = -0.028694177
        else:
            var21 = -0.052662868
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var22 = 0.05463294
                else:
                    var22 = 0.008849173
            else:
                var22 = 0.0121386
        else:
            if input[5] < 4693.2686:
                if input[4] < 7.3523836:
                    if input[3] < 13.104021:
                        var22 = -0.033968553
                    else:
                        var22 = 0.0338621
                else:
                    if input[3] < 13.104021:
                        var22 = 0.013429855
                    else:
                        var22 = -0.046647783
            else:
                var22 = -0.04460859
    else:
        if input[4] < 7.322918:
            if input[0] < 30.359:
                if input[1] < 48.330498:
                    var22 = 0.031194523
                else:
                    if input[2] < 457.59:
                        var22 = -0.05221283
                    else:
                        var22 = -0.0057069673
            else:
                if input[0] < 38.797752:
                    if input[1] < 71.36714:
                        var22 = 0.06715633
                    else:
                        var22 = 0.008937982
                else:
                    var22 = -0.029134646
        else:
            var22 = -0.052405603
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var23 = 0.05412632
                else:
                    var23 = 0.008103053
            else:
                var23 = 0.011285036
        else:
            if input[0] < 25.986551:
                if input[1] < 66.80687:
                    if input[4] < 7.243017:
                        var23 = 0.009120918
                    else:
                        var23 = 0.062128723
                else:
                    if input[1] < 85.865974:
                        var23 = -0.02172797
                    else:
                        var23 = 0.04810826
            else:
                if input[0] < 36.260155:
                    if input[4] < 7.256852:
                        var23 = -0.0054051
                    else:
                        var23 = -0.03662967
                else:
                    if input[4] < 7.2781405:
                        var23 = 0.053037167
                    else:
                        var23 = -0.006916622
    else:
        if input[4] < 7.322918:
            if input[0] < 30.359:
                if input[1] < 48.330498:
                    var23 = 0.030611483
                else:
                    if input[2] < 457.59:
                        var23 = -0.051410735
                    else:
                        var23 = -0.0043390472
            else:
                if input[0] < 38.797752:
                    if input[1] < 71.36714:
                        var23 = 0.064623415
                    else:
                        var23 = 0.0089054005
                else:
                    var23 = -0.028362993
        else:
            var23 = -0.052170455
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var24 = 0.05367015
                else:
                    var24 = 0.0073904633
            else:
                var24 = 0.01047946
        else:
            if input[5] < 4693.2686:
                if input[4] < 7.3523836:
                    if input[3] < 13.104021:
                        var24 = -0.03307706
                    else:
                        var24 = 0.03172083
                else:
                    if input[3] < 13.104021:
                        var24 = 0.014190539
                    else:
                        var24 = -0.045409996
            else:
                var24 = -0.04267965
    else:
        if input[4] < 7.322918:
            if input[1] < 46.92819:
                var24 = 0.05881359
            else:
                if input[5] < 3138.0425:
                    if input[5] < 888.78937:
                        var24 = 0.002155088
                    else:
                        var24 = -0.047712762
                else:
                    if input[4] < 7.243017:
                        var24 = 0.04102444
                    else:
                        var24 = 0.007686723
        else:
            var24 = -0.051955443
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[4] < 7.322918:
                if input[5] < 4394.467:
                    var25 = 0.053258117
                else:
                    var25 = 0.006706754
            else:
                var25 = 0.009715758
        else:
            if input[0] < 25.986551:
                if input[1] < 66.80687:
                    if input[4] < 7.243017:
                        var25 = 0.0076296027
                    else:
                        var25 = 0.059187528
                else:
                    if input[1] < 85.865974:
                        var25 = -0.021758627
                    else:
                        var25 = 0.046454072
            else:
                if input[0] < 36.260155:
                    if input[1] < 81.10271:
                        var25 = -0.034232207
                    else:
                        var25 = -0.0032185104
                else:
                    var25 = 0.037189547
    else:
        if input[4] < 7.322918:
            if input[0] < 30.359:
                if input[0] < 24.703085:
                    if input[0] < 22.422846:
                        var25 = -0.025997777
                    else:
                        var25 = 0.045693956
                else:
                    var25 = -0.048783034
            else:
                if input[0] < 36.583706:
                    var25 = 0.055507958
                else:
                    var25 = -0.0072615966
        else:
            var25 = -0.051758777
    if input[2] < 439.61963:
        if input[2] < 407.72763:
            if input[1] < 40.452465:
                var26 = 0.00018676497
            else:
                if input[2] < 399.29376:
                    var26 = 0.052957904
                else:
                    if input[1] < 85.19493:
                        var26 = 0.04653021
                    else:
                        var26 = -0.010449262
        else:
            if input[5] < 4693.2686:
                if input[4] < 7.3523836:
                    if input[1] < 97.78946:
                        var26 = 0.029121673
                    else:
                        var26 = -0.03836684
                else:
                    if input[3] < 13.104021:
                        var26 = 0.014201984
                    else:
                        var26 = -0.043750133
            else:
                var26 = -0.040817764
    else:
        if input[4] < 7.322918:
            if input[1] < 48.330498:
                var26 = 0.045017835
            else:
                if input[5] < 3138.0425:
                    if input[0] < 32.755127:
                        var26 = -0.040559217
                    else:
                        var26 = 0.010300195
                else:
                    if input[4] < 7.243017:
                        var26 = 0.038669135
                    else:
                        var26 = 0.008385299
        else:
            var26 = -0.051576585
    if input[4] < 7.322918:
        if input[2] < 407.72763:
            if input[5] < 4394.467:
                var27 = 0.05254602
            else:
                var27 = 0.0049925284
        else:
            if input[5] < 4693.2686:
                if input[5] < 3138.0425:
                    if input[1] < 56.845116:
                        var27 = 0.037090477
                    else:
                        var27 = -0.014835671
                else:
                    var27 = 0.059546728
            else:
                var27 = -0.03989382
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var27 = 0.05310418
                else:
                    if input[5] < 395.23544:
                        var27 = 0.013800842
                    else:
                        var27 = -0.008449673
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var27 = -0.019638188
                    else:
                        var27 = 0.017087532
                else:
                    var27 = -0.04869558
        else:
            var27 = -0.05142024
    if input[4] < 7.322918:
        if input[2] < 407.72763:
            if input[5] < 4394.467:
                var28 = 0.0522358
            else:
                var28 = 0.004404056
        else:
            if input[0] < 35.580082:
                if input[0] < 25.986551:
                    if input[0] < 22.883705:
                        var28 = -0.00908157
                    else:
                        var28 = 0.042800423
                else:
                    if input[4] < 7.256852:
                        var28 = 0.00035245065
                    else:
                        var28 = -0.051473904
            else:
                if input[5] < 1007.39386:
                    var28 = 0.0626713
                else:
                    if input[1] < 85.703255:
                        var28 = 0.0055956454
                    else:
                        var28 = -0.007429485
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var28 = 0.05158337
                else:
                    if input[5] < 395.23544:
                        var28 = 0.013408561
                    else:
                        var28 = -0.008252385
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var28 = -0.01882886
                    else:
                        var28 = 0.016799694
                else:
                    var28 = -0.04765787
        else:
            var28 = -0.051265545
    if input[4] < 7.322918:
        if input[2] < 399.29376:
            var29 = 0.051961847
        else:
            if input[5] < 4693.2686:
                if input[3] < 133.33838:
                    if input[0] < 36.119766:
                        var29 = -0.0071559697
                    else:
                        var29 = 0.04433019
                else:
                    var29 = 0.059862103
            else:
                var29 = -0.038389813
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var29 = 0.049828697
                else:
                    if input[5] < 395.23544:
                        var29 = 0.013257478
                    else:
                        var29 = -0.007848428
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var29 = -0.018191962
                    else:
                        var29 = 0.016494486
                else:
                    var29 = -0.046500035
        else:
            var29 = -0.051120486
    if input[4] < 7.322918:
        if input[2] < 399.29376:
            var30 = 0.051696766
        else:
            if input[5] < 4693.2686:
                if input[3] < 133.33838:
                    if input[0] < 36.119766:
                        var30 = -0.006739219
                    else:
                        var30 = 0.04273442
                else:
                    var30 = 0.05869266
            else:
                var30 = -0.037400845
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var30 = 0.048495527
                else:
                    if input[5] < 395.23544:
                        var30 = 0.012863854
                    else:
                        var30 = -0.007680165
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var30 = -0.017482588
                    else:
                        var30 = 0.016207362
                else:
                    var30 = -0.045564637
        else:
            var30 = -0.05098468
    if input[2] < 462.86743:
        if input[2] < 407.72763:
            if input[1] < 40.452465:
                var31 = -0.0034679302
            else:
                if input[5] < 4452.413:
                    if input[4] < 7.322918:
                        var31 = 0.05148088
                    else:
                        var31 = 0.012466519
                else:
                    var31 = 0.00816975
        else:
            if input[1] < 56.845116:
                if input[5] < 1040.2141:
                    var31 = 0.06312711
                else:
                    if input[2] < 429.77728:
                        var31 = 0.028236454
                    else:
                        var31 = -0.021027165
            else:
                if input[4] < 7.3376346:
                    if input[1] < 62.443443:
                        var31 = -0.040881075
                    else:
                        var31 = 0.010741344
                else:
                    if input[5] < 395.23544:
                        var31 = 0.012705581
                    else:
                        var31 = -0.048435148
    else:
        var31 = -0.0508638
    if input[2] < 462.86743:
        if input[2] < 399.29376:
            if input[1] < 40.452465:
                var32 = -0.0035483397
            else:
                var32 = 0.051263887
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var32 = 0.038200084
                    else:
                        var32 = -0.008254748
                else:
                    if input[0] < 22.79356:
                        var32 = -0.0084541
                    else:
                        var32 = 0.058762874
            else:
                var32 = -0.039892416
    else:
        var32 = -0.05073849
    if input[2] < 462.86743:
        if input[2] < 399.29376:
            if input[1] < 40.452465:
                var33 = -0.004141106
            else:
                var33 = 0.05104967
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var33 = 0.036509704
                    else:
                        var33 = -0.00772785
                else:
                    if input[0] < 22.79356:
                        var33 = -0.008694435
                    else:
                        var33 = 0.057522874
            else:
                var33 = -0.0392756
    else:
        var33 = -0.05061857
    if input[4] < 7.322918:
        if input[2] < 399.29376:
            var34 = 0.050811257
        else:
            if input[0] < 36.119766:
                if input[0] < 25.986551:
                    if input[0] < 22.883705:
                        var34 = -0.006976064
                    else:
                        var34 = 0.03886309
                else:
                    if input[4] < 7.256852:
                        var34 = 0.0023563064
                    else:
                        var34 = -0.049630944
            else:
                if input[5] < 1007.39386:
                    var34 = 0.059512377
                else:
                    if input[2] < 423.73544:
                        var34 = 0.031442314
                    else:
                        var34 = -0.030270612
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var34 = 0.044185665
                else:
                    if input[5] < 395.23544:
                        var34 = 0.013875454
                    else:
                        var34 = -0.0058004013
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var34 = -0.016588202
                    else:
                        var34 = 0.016615406
                else:
                    var34 = -0.04367314
        else:
            var34 = -0.05051599
    if input[2] < 462.86743:
        if input[2] < 399.29376:
            if input[1] < 40.452465:
                var35 = -0.0059301797
            else:
                var35 = 0.050655205
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var35 = 0.034347523
                    else:
                        var35 = -0.0072686295
                else:
                    if input[0] < 22.79356:
                        var35 = -0.008544347
                    else:
                        var35 = 0.05586341
            else:
                var35 = -0.03820755
    else:
        var35 = -0.050394155
    if input[2] < 462.86743:
        if input[2] < 399.29376:
            if input[1] < 40.452465:
                var36 = -0.0065561645
            else:
                var36 = 0.050470114
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var36 = 0.032869734
                    else:
                        var36 = -0.0070683076
                else:
                    if input[0] < 22.79356:
                        var36 = -0.008452213
                    else:
                        var36 = 0.054794975
            else:
                var36 = -0.037308212
    else:
        var36 = -0.050283838
    if input[4] < 7.322918:
        if input[2] < 399.29376:
            var37 = 0.05025663
        else:
            if input[0] < 36.119766:
                if input[0] < 25.986551:
                    if input[0] < 22.883705:
                        var37 = -0.0076442505
                    else:
                        var37 = 0.035438083
                else:
                    if input[4] < 7.256852:
                        var37 = 0.002485247
                    else:
                        var37 = -0.048363302
            else:
                if input[5] < 1007.39386:
                    var37 = 0.05899484
                else:
                    if input[1] < 85.703255:
                        var37 = 0.008096794
                    else:
                        var37 = -0.0070911213
    else:
        if input[2] < 433.85468:
            if input[5] < 1040.2141:
                if input[0] < 23.014591:
                    var37 = 0.041671757
                else:
                    if input[5] < 395.23544:
                        var37 = 0.014578884
                    else:
                        var37 = -0.004700122
            else:
                if input[1] < 83.43807:
                    if input[1] < 75.8811:
                        var37 = -0.01523559
                    else:
                        var37 = 0.01635926
                else:
                    var37 = -0.042799003
        else:
            var37 = -0.050210405
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var38 = 0.050026216
        else:
            if input[5] < 4737.7285:
                if input[5] < 3138.0425:
                    if input[5] < 1040.2141:
                        var38 = 0.015291556
                    else:
                        var38 = -0.015902413
                else:
                    if input[1] < 81.73901:
                        var38 = 0.05491211
                    else:
                        var38 = 0.00654846
            else:
                var38 = -0.036409102
    else:
        var38 = -0.050072785
    if input[4] < 7.3822474:
        if input[2] < 407.72763:
            if input[1] < 40.763638:
                var39 = -0.0040202676
            else:
                if input[5] < 4452.413:
                    var39 = 0.05003779
                else:
                    var39 = 0.002247823
        else:
            if input[5] < 4693.2686:
                if input[5] < 3138.0425:
                    if input[1] < 56.845116:
                        var39 = 0.027312681
                    else:
                        var39 = -0.010492133
                else:
                    if input[0] < 23.645546:
                        var39 = -0.0021666207
                    else:
                        var39 = 0.04951779
            else:
                var39 = -0.03463205
    else:
        if input[3] < 12.350893:
            var39 = 0.00078291737
        else:
            var39 = -0.0501104
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var40 = 0.04967488
        else:
            if input[5] < 4737.7285:
                if input[5] < 3138.0425:
                    if input[5] < 1040.2141:
                        var40 = 0.0145268245
                    else:
                        var40 = -0.015890026
                else:
                    if input[1] < 81.73901:
                        var40 = 0.053341486
                    else:
                        var40 = 0.005060579
            else:
                var40 = -0.03496255
    else:
        var40 = -0.049861185
    var41 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40
    if input[4] < 7.3822474:
        if input[2] < 380.03854:
            var42 = 0.049495105
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[0] < 36.260155:
                        var42 = -0.003732544
                    else:
                        var42 = 0.0307217
                else:
                    if input[0] < 22.79356:
                        var42 = -0.0021724897
                    else:
                        var42 = 0.051739227
            else:
                var42 = -0.03318732
    else:
        if input[3] < 12.350893:
            var42 = 0.00052016426
        else:
            var42 = -0.04991087
    if input[4] < 7.3822474:
        if input[2] < 380.03854:
            var43 = 0.04931421
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[0] < 36.260155:
                        var43 = -0.0035776638
                    else:
                        var43 = 0.029863516
                else:
                    if input[0] < 22.79356:
                        var43 = -0.0025571692
                    else:
                        var43 = 0.05089283
            else:
                var43 = -0.03259758
    else:
        if input[3] < 12.350893:
            var43 = 0.0007851943
        else:
            var43 = -0.049803313
    if input[4] < 7.3822474:
        if input[2] < 380.03854:
            var44 = 0.04912908
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[0] < 36.260155:
                        var44 = -0.0034320825
                    else:
                        var44 = 0.029028663
                else:
                    if input[0] < 22.79356:
                        var44 = -0.0029170539
                    else:
                        var44 = 0.050074156
            else:
                var44 = -0.03201881
    else:
        if input[3] < 12.350893:
            var44 = 0.0010320402
        else:
            var44 = -0.049692318
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var45 = 0.0489379
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var45 = 0.025457272
                    else:
                        var45 = -0.005662947
                else:
                    if input[4] < 7.3376346:
                        var45 = 0.049260404
                    else:
                        var45 = -0.011468678
            else:
                var45 = -0.032891806
    else:
        var45 = -0.049422756
    if input[4] < 7.3822474:
        if input[2] < 380.03854:
            var46 = 0.048739698
        else:
            if input[1] < 97.78946:
                if input[1] < 90.31466:
                    if input[1] < 83.43807:
                        var46 = 0.010787323
                    else:
                        var46 = -0.029858192
                else:
                    if input[4] < 7.293997:
                        var46 = 0.051878463
                    else:
                        var46 = 0.001714151
            else:
                var46 = -0.03399596
    else:
        if input[3] < 12.350893:
            var46 = 0.0017684933
        else:
            var46 = -0.049472447
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var47 = 0.048532948
        else:
            if input[5] < 4737.7285:
                if input[5] < 3138.0425:
                    if input[5] < 1040.2141:
                        var47 = 0.013356375
                    else:
                        var47 = -0.015881058
                else:
                    if input[1] < 81.73901:
                        var47 = 0.050597053
                    else:
                        var47 = 0.0018698795
            else:
                var47 = -0.032206777
    else:
        var47 = -0.049186613
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var48 = 0.04831625
        else:
            if input[0] < 36.260155:
                if input[0] < 25.986551:
                    if input[2] < 423.73544:
                        var48 = 0.041096322
                    else:
                        var48 = 0.0012252546
                else:
                    if input[0] < 29.948753:
                        var48 = -0.031613357
                    else:
                        var48 = 0.0016606248
            else:
                if input[1] < 78.1442:
                    var48 = 0.04691269
                else:
                    if input[1] < 89.23889:
                        var48 = -0.031384688
                    else:
                        var48 = 0.021913117
    else:
        var48 = -0.049058568
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var49 = 0.048084795
        else:
            if input[5] < 4737.7285:
                if input[5] < 3138.0425:
                    if input[1] < 56.845116:
                        var49 = 0.023184774
                    else:
                        var49 = -0.0077816397
                else:
                    if input[1] < 81.73901:
                        var49 = 0.049707856
                    else:
                        var49 = 0.0015526478
            else:
                var49 = -0.031218678
    else:
        var49 = -0.048925962
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var50 = 0.047843557
        else:
            if input[1] < 97.78946:
                if input[4] < 7.293997:
                    if input[1] < 90.07144:
                        var50 = 0.008212714
                    else:
                        var50 = 0.050525945
                else:
                    if input[0] < 30.878813:
                        var50 = -0.02062119
                    else:
                        var50 = 0.017921267
            else:
                var50 = -0.032690387
    else:
        var50 = -0.048787247
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var51 = 0.04758848
        else:
            if input[5] < 4737.7285:
                if input[3] < 133.33838:
                    if input[1] < 56.845116:
                        var51 = 0.022855703
                    else:
                        var51 = -0.0059172404
                else:
                    if input[4] < 7.3376346:
                        var51 = 0.0469941
                    else:
                        var51 = -0.011535205
            else:
                var51 = -0.030347202
    else:
        var51 = -0.04865053
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var52 = 0.047317933
        else:
            if input[0] < 36.260155:
                if input[0] < 25.986551:
                    if input[2] < 423.73544:
                        var52 = 0.040152203
                    else:
                        var52 = 0.000459236
                else:
                    if input[0] < 29.948753:
                        var52 = -0.030833354
                    else:
                        var52 = 0.0013702924
            else:
                if input[1] < 78.1442:
                    var52 = 0.045186084
                else:
                    if input[1] < 89.23889:
                        var52 = -0.03109845
                    else:
                        var52 = 0.020113695
    else:
        var52 = -0.04850085
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var53 = 0.047031473
        else:
            if input[0] < 36.260155:
                if input[0] < 34.86882:
                    if input[4] < 7.256852:
                        var53 = 0.021546029
                    else:
                        var53 = -0.0047696135
                else:
                    if input[3] < 75.37392:
                        var53 = -0.047816906
                    else:
                        var53 = -0.012038886
            else:
                if input[1] < 78.1442:
                    var53 = 0.04411769
                else:
                    if input[1] < 90.07144:
                        var53 = -0.02769868
                    else:
                        var53 = 0.01835939
    else:
        var53 = -0.048360016
    if input[4] < 7.3822474:
        if input[2] < 380.03854:
            var54 = 0.046721946
        else:
            if input[1] < 97.78946:
                if input[1] < 90.31466:
                    if input[1] < 83.43807:
                        var54 = 0.009938501
                    else:
                        var54 = -0.029318241
                else:
                    if input[4] < 7.293997:
                        var54 = 0.04897383
                    else:
                        var54 = 0.0016432574
            else:
                var54 = -0.030962456
    else:
        if input[3] < 12.350893:
            var54 = 0.004137861
        else:
            var54 = -0.04848082
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var55 = 0.046406202
        else:
            if input[0] < 36.260155:
                if input[0] < 34.86882:
                    if input[2] < 429.77728:
                        var55 = 0.016846806
                    else:
                        var55 = -0.007126854
                else:
                    if input[3] < 75.37392:
                        var55 = -0.046925966
                    else:
                        var55 = -0.01135183
            else:
                if input[1] < 78.1442:
                    var55 = 0.043129098
                else:
                    if input[1] < 90.07144:
                        var55 = -0.026882727
                    else:
                        var55 = 0.016958158
    else:
        var55 = -0.048045304
    if input[2] < 462.86743:
        if input[4] < 7.1246004:
            var56 = 0.04571093
        else:
            if input[0] < 25.986551:
                if input[2] < 423.73544:
                    if input[1] < 83.43807:
                        var56 = 0.043932904
                    else:
                        var56 = 0.013561758
                else:
                    if input[1] < 66.80687:
                        var56 = 0.01569497
                    else:
                        var56 = -0.023933498
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var56 = 0.011801284
                    else:
                        var56 = -0.048537657
                else:
                    if input[5] < 4496.4277:
                        var56 = 0.01953249
                    else:
                        var56 = -0.034970343
    else:
        var56 = -0.04789071
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var57 = 0.04574988
        else:
            if input[1] < 97.78946:
                if input[4] < 7.293997:
                    if input[1] < 90.07144:
                        var57 = 0.006511045
                    else:
                        var57 = 0.048009474
                else:
                    if input[0] < 30.878813:
                        var57 = -0.019144816
                    else:
                        var57 = 0.018066444
            else:
                var57 = -0.029964793
    else:
        var57 = -0.04772523
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var58 = 0.04539729
        else:
            if input[1] < 97.78946:
                if input[1] < 94.96665:
                    if input[1] < 83.43807:
                        var58 = 0.009256792
                    else:
                        var58 = -0.014365005
                else:
                    var58 = 0.039235063
            else:
                var58 = -0.02919716
    else:
        var58 = -0.0475591
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var59 = 0.04499511
        else:
            if input[1] < 97.78946:
                if input[1] < 94.96665:
                    if input[1] < 83.43807:
                        var59 = 0.009009878
                    else:
                        var59 = -0.013720162
                else:
                    var59 = 0.038545303
            else:
                var59 = -0.028740069
    else:
        var59 = -0.04738384
    if input[2] < 462.86743:
        if input[4] < 7.1246004:
            var60 = 0.04415958
        else:
            if input[0] < 25.986551:
                if input[2] < 423.73544:
                    if input[1] < 83.43807:
                        var60 = 0.04329848
                    else:
                        var60 = 0.013271776
                else:
                    if input[1] < 66.80687:
                        var60 = 0.014186538
                    else:
                        var60 = -0.022411972
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var60 = 0.011040045
                    else:
                        var60 = -0.047438674
                else:
                    if input[5] < 4496.4277:
                        var60 = 0.01804264
                    else:
                        var60 = -0.03361231
    else:
        var60 = -0.047202203
    if input[2] < 462.86743:
        if input[4] < 7.1246004:
            var61 = 0.043686192
        else:
            if input[5] < 3138.0425:
                if input[5] < 1040.2141:
                    if input[1] < 56.845116:
                        var61 = 0.049571615
                    else:
                        var61 = -0.0010109751
                else:
                    if input[2] < 429.77728:
                        var61 = 0.008688956
                    else:
                        var61 = -0.038997646
            else:
                if input[5] < 4737.7285:
                    if input[1] < 82.106895:
                        var61 = 0.04741743
                    else:
                        var61 = 0.0007355817
                else:
                    var61 = -0.025613284
    else:
        var61 = -0.046999358
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var62 = 0.043751925
        else:
            if input[0] < 36.260155:
                if input[0] < 34.86882:
                    if input[0] < 34.571377:
                        var62 = 0.0014096709
                    else:
                        var62 = 0.041470654
                else:
                    if input[3] < 75.37392:
                        var62 = -0.04637465
                    else:
                        var62 = -0.010429332
            else:
                if input[1] < 78.1442:
                    var62 = 0.04097488
                else:
                    if input[1] < 90.07144:
                        var62 = -0.026907293
                    else:
                        var62 = 0.015162589
    else:
        var62 = -0.04680501
    if input[2] < 462.86743:
        if input[4] < 7.1246004:
            var63 = 0.042767696
        else:
            if input[5] < 431.76425:
                if input[1] < 76.9051:
                    var63 = -0.0072541707
                else:
                    var63 = 0.05451363
            else:
                if input[5] < 523.5276:
                    if input[4] < 7.1964808:
                        var63 = -0.04989833
                    else:
                        var63 = -0.0054744794
                else:
                    if input[4] < 7.3523836:
                        var63 = 0.01116311
                    else:
                        var63 = -0.03020647
    else:
        var63 = -0.046605915
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var64 = 0.04283623
        else:
            if input[5] < 938.6545:
                if input[5] < 652.72906:
                    if input[1] < 76.9051:
                        var64 = -0.022131661
                    else:
                        var64 = 0.021014873
                else:
                    var64 = 0.043031044
            else:
                if input[5] < 1294.5337:
                    if input[1] < 41.056152:
                        var64 = 0.010802794
                    else:
                        var64 = -0.038824525
                else:
                    if input[4] < 7.3376346:
                        var64 = 0.017189693
                    else:
                        var64 = -0.0307953
    else:
        var64 = -0.04636812
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var65 = 0.042393226
        else:
            if input[0] < 25.636688:
                if input[1] < 85.865974:
                    if input[1] < 83.43807:
                        var65 = 0.013933069
                    else:
                        var65 = -0.042469565
                else:
                    var65 = 0.04745261
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var65 = 0.015721193
                    else:
                        var65 = -0.042988796
                else:
                    if input[5] < 4496.4277:
                        var65 = 0.017822145
                    else:
                        var65 = -0.033502072
    else:
        var65 = -0.046132166
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var66 = 0.04181556
        else:
            if input[5] < 3138.0425:
                if input[5] < 1040.2141:
                    if input[1] < 56.845116:
                        var66 = 0.04703851
                    else:
                        var66 = -0.0010283953
                else:
                    if input[2] < 429.77728:
                        var66 = 0.008524877
                    else:
                        var66 = -0.038331773
            else:
                if input[5] < 4554.5503:
                    if input[4] < 7.293997:
                        var66 = 0.046197504
                    else:
                        var66 = -0.0050553265
                else:
                    if input[0] < 27.043375:
                        var66 = 0.02595885
                    else:
                        var66 = -0.035657283
    else:
        var66 = -0.045882758
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var67 = 0.041365568
        else:
            if input[5] < 3138.0425:
                if input[5] < 1040.2141:
                    if input[1] < 56.845116:
                        var67 = 0.046231613
                    else:
                        var67 = -0.0012803914
                else:
                    if input[2] < 429.77728:
                        var67 = 0.008150709
                    else:
                        var67 = -0.037459552
            else:
                if input[5] < 4554.5503:
                    if input[4] < 7.293997:
                        var67 = 0.045592662
                    else:
                        var67 = -0.0039751157
                else:
                    if input[3] < 187.8443:
                        var67 = -0.03473337
                    else:
                        var67 = 0.024399644
    else:
        var67 = -0.045652002
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var68 = 0.04081009
        else:
            if input[5] < 3138.0425:
                if input[5] < 1040.2141:
                    if input[1] < 56.845116:
                        var68 = 0.045427307
                    else:
                        var68 = -0.0011593729
                else:
                    if input[2] < 429.77728:
                        var68 = 0.008250505
                    else:
                        var68 = -0.03656495
            else:
                if input[5] < 4554.5503:
                    if input[3] < 172.44543:
                        var68 = 0.04471578
                    else:
                        var68 = -0.0036011362
                else:
                    if input[3] < 187.8443:
                        var68 = -0.033884782
                    else:
                        var68 = 0.0242241
    else:
        var68 = -0.045401763
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var69 = 0.040228494
        else:
            if input[0] < 36.260155:
                if input[0] < 34.86882:
                    if input[0] < 34.571377:
                        var69 = 0.00092383457
                    else:
                        var69 = 0.039538164
                else:
                    if input[3] < 75.37392:
                        var69 = -0.041602444
                    else:
                        var69 = -0.010620224
            else:
                if input[1] < 78.1442:
                    var69 = 0.03821353
                else:
                    var69 = -0.0067069978
    else:
        var69 = -0.04514477
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var70 = 0.0397374
        else:
            if input[0] < 25.636688:
                if input[1] < 85.865974:
                    if input[1] < 83.43807:
                        var70 = 0.013767491
                    else:
                        var70 = -0.040617686
                else:
                    var70 = 0.046789482
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var70 = 0.013350978
                    else:
                        var70 = -0.041695513
                else:
                    if input[1] < 63.508068:
                        var70 = -0.020144662
                    else:
                        var70 = 0.020233938
    else:
        var70 = -0.04488273
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var71 = 0.039104603
        else:
            if input[0] < 25.986551:
                if input[2] < 423.73544:
                    if input[1] < 83.43807:
                        var71 = 0.04021959
                    else:
                        var71 = 0.010957538
                else:
                    if input[0] < 23.34363:
                        var71 = -0.018114088
                    else:
                        var71 = 0.020547343
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var71 = 0.008797097
                    else:
                        var71 = -0.044878084
                else:
                    if input[5] < 4496.4277:
                        var71 = 0.016775852
                    else:
                        var71 = -0.030617842
    else:
        var71 = -0.044612102
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var72 = 0.03858938
        else:
            if input[0] < 25.636688:
                if input[1] < 85.865974:
                    if input[1] < 83.43807:
                        var72 = 0.013228056
                    else:
                        var72 = -0.03974783
                else:
                    var72 = 0.04536857
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var72 = 0.01250082
                    else:
                        var72 = -0.04013454
                else:
                    if input[1] < 63.508068:
                        var72 = -0.019730901
                    else:
                        var72 = 0.019426038
    else:
        var72 = -0.04434352
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var73 = 0.03793091
        else:
            if input[5] < 3138.0425:
                if input[5] < 938.6545:
                    if input[5] < 652.72906:
                        var73 = -0.00394588
                    else:
                        var73 = 0.04056055
                else:
                    if input[2] < 429.77728:
                        var73 = 0.008950743
                    else:
                        var73 = -0.02835171
            else:
                if input[5] < 4554.5503:
                    if input[4] < 7.293997:
                        var73 = 0.042866196
                    else:
                        var73 = -0.0048613194
                else:
                    if input[3] < 185.74408:
                        var73 = -0.03162303
                    else:
                        var73 = 0.020009479
    else:
        var73 = -0.044057768
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var74 = 0.037383337
        else:
            if input[5] < 3138.0425:
                if input[5] < 938.6545:
                    if input[5] < 652.72906:
                        var74 = -0.00332097
                    else:
                        var74 = 0.03882616
                else:
                    if input[2] < 429.77728:
                        var74 = 0.008592038
                    else:
                        var74 = -0.027468467
            else:
                if input[5] < 4554.5503:
                    if input[3] < 172.44543:
                        var74 = 0.04237789
                    else:
                        var74 = -0.0042441804
                else:
                    if input[0] < 28.20128:
                        var74 = 0.019468796
                    else:
                        var74 = -0.031048521
    else:
        var74 = -0.043763027
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[3] < 12.350893:
                var75 = 0.0052136467
            else:
                var75 = 0.043786105
        else:
            if input[4] < 7.3523836:
                if input[5] < 459.61935:
                    var75 = -0.027672863
                else:
                    if input[2] < 423.73544:
                        var75 = 0.02604239
                    else:
                        var75 = 0.0025170222
            else:
                var75 = -0.030765815
    else:
        var75 = -0.04355853
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var76 = 0.036158077
        else:
            if input[1] < 55.81447:
                if input[5] < 1040.2141:
                    var76 = 0.04325324
                else:
                    if input[5] < 1230.6306:
                        var76 = -0.036034677
                    else:
                        var76 = 0.015171409
            else:
                if input[0] < 21.280195:
                    if input[1] < 64.23323:
                        var76 = -0.004542367
                    else:
                        var76 = -0.042038657
                else:
                    if input[0] < 25.087263:
                        var76 = 0.024636067
                    else:
                        var76 = -0.005260871
    else:
        var76 = -0.043148126
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var77 = 0.0355844
        else:
            if input[5] < 3138.0425:
                if input[5] < 1040.2141:
                    if input[1] < 56.845116:
                        var77 = 0.0425452
                    else:
                        var77 = -0.0013239993
                else:
                    if input[2] < 429.77728:
                        var77 = 0.008845647
                    else:
                        var77 = -0.034009017
            else:
                if input[5] < 4554.5503:
                    if input[3] < 172.44543:
                        var77 = 0.04140677
                    else:
                        var77 = -0.0040659383
                else:
                    if input[0] < 28.530838:
                        var77 = 0.01842167
                    else:
                        var77 = -0.029963193
    else:
        var77 = -0.042831924
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[3] < 12.350893:
                var78 = 0.0043702833
            else:
                var78 = 0.041723225
        else:
            if input[4] < 7.3523836:
                if input[5] < 459.61935:
                    var78 = -0.025381634
                else:
                    if input[2] < 423.73544:
                        var78 = 0.024684321
                    else:
                        var78 = 0.0023261223
            else:
                var78 = -0.02990652
    else:
        var78 = -0.042595994
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var79 = 0.034355108
        else:
            if input[0] < 25.636688:
                if input[1] < 85.865974:
                    if input[1] < 83.43807:
                        var79 = 0.01225267
                    else:
                        var79 = -0.037749056
                else:
                    var79 = 0.042105384
            else:
                if input[0] < 29.948753:
                    if input[4] < 7.256852:
                        var79 = 0.010433953
                    else:
                        var79 = -0.039186943
                else:
                    if input[1] < 63.508068:
                        var79 = -0.014941935
                    else:
                        var79 = 0.017727545
    else:
        var79 = -0.04218164
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[3] < 12.350893:
                var80 = 0.0031246128
            else:
                var80 = 0.040200625
        else:
            if input[4] < 7.3523836:
                if input[5] < 459.61935:
                    var80 = -0.023844352
                else:
                    if input[2] < 423.73544:
                        var80 = 0.023705654
                    else:
                        var80 = 0.0019498747
            else:
                var80 = -0.028790036
    else:
        var80 = -0.041918974
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var81 = 0.033426546
        else:
            if input[3] < 133.33838:
                if input[5] < 938.6545:
                    if input[5] < 652.72906:
                        var81 = -0.0039329007
                    else:
                        var81 = 0.036599316
                else:
                    if input[1] < 43.66826:
                        var81 = 0.019076008
                    else:
                        var81 = -0.016100325
            else:
                if input[4] < 7.310009:
                    var81 = 0.02773211
                else:
                    var81 = -0.0044914335
    else:
        var81 = -0.041490853
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var82 = 0.0055611115
            else:
                var82 = 0.042825617
        else:
            if input[4] < 7.3523836:
                if input[5] < 459.61935:
                    var82 = -0.022730999
                else:
                    if input[2] < 423.73544:
                        var82 = 0.022822438
                    else:
                        var82 = 0.0016510967
            else:
                var82 = -0.02775879
    else:
        var82 = -0.041230164
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var83 = 0.032416184
        else:
            if input[3] < 133.33838:
                if input[5] < 938.6545:
                    if input[5] < 652.72906:
                        var83 = -0.0033561958
                    else:
                        var83 = 0.035098072
                else:
                    if input[1] < 83.43807:
                        var83 = 0.0011537815
                    else:
                        var83 = -0.028523294
            else:
                if input[4] < 7.310009:
                    var83 = 0.02690344
                else:
                    var83 = -0.0047366503
    else:
        var83 = -0.04081976
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var84 = 0.005309171
            else:
                var84 = 0.041564055
        else:
            if input[4] < 7.3523836:
                if input[5] < 459.61935:
                    var84 = -0.021137476
                else:
                    if input[2] < 423.73544:
                        var84 = 0.022258786
                    else:
                        var84 = 0.0011172993
            else:
                var84 = -0.02695084
    else:
        var84 = -0.040557414
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var85 = 0.031585626
        else:
            if input[3] < 133.33838:
                if input[5] < 938.6545:
                    if input[5] < 652.72906:
                        var85 = -0.0029086173
                    else:
                        var85 = 0.03360821
                else:
                    if input[1] < 43.66826:
                        var85 = 0.018177956
                    else:
                        var85 = -0.015597479
            else:
                if input[4] < 7.310009:
                    var85 = 0.026159221
                else:
                    var85 = -0.0039341277
    else:
        var85 = -0.040149804
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var86 = 0.0045943283
            else:
                var86 = 0.04077999
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.260155:
                    if input[3] < 21.621714:
                        var86 = -0.033990994
                    else:
                        var86 = 0.0065815165
                else:
                    if input[5] < 1007.39386:
                        var86 = 0.039581593
                    else:
                        var86 = -0.0054109655
            else:
                var86 = -0.026603237
    else:
        var86 = -0.039874762
    if input[2] < 462.86743:
        if input[2] < 380.03854:
            var87 = 0.030828808
        else:
            if input[1] < 55.81447:
                if input[5] < 1040.2141:
                    var87 = 0.04007664
                else:
                    if input[5] < 1230.6306:
                        var87 = -0.034634273
                    else:
                        var87 = 0.014877795
            else:
                if input[0] < 21.280195:
                    if input[1] < 64.23323:
                        var87 = -0.006267588
                    else:
                        var87 = -0.04059015
                else:
                    if input[0] < 25.087263:
                        var87 = 0.022427801
                    else:
                        var87 = -0.0051548514
    else:
        var87 = -0.039424222
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var88 = 0.0034934815
            else:
                var88 = 0.039665166
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.260155:
                    if input[3] < 21.621714:
                        var88 = -0.033299
                    else:
                        var88 = 0.0062304744
                else:
                    if input[5] < 1007.39386:
                        var88 = 0.039043978
                    else:
                        var88 = -0.0049118344
            else:
                var88 = -0.026309205
    else:
        var88 = -0.03911721
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[2] < 452.94366:
                if input[2] < 399.29376:
                    var89 = 0.032390818
                else:
                    if input[5] < 2244.283:
                        var89 = -0.008848445
                    else:
                        var89 = 0.016581988
            else:
                var89 = 0.03778733
        else:
            if input[0] < 30.878813:
                if input[0] < 21.619698:
                    if input[4] < 7.3376346:
                        var89 = 0.012605335
                    else:
                        var89 = 0.0025418685
                else:
                    if input[3] < 91.50338:
                        var89 = -0.03852735
                    else:
                        var89 = -0.006028147
            else:
                if input[2] < 429.77728:
                    var89 = 0.023416586
                else:
                    var89 = -0.004440712
    else:
        var89 = -0.038713157
    if input[2] < 462.86743:
        if input[4] < 7.0906034:
            var90 = 0.029290287
        else:
            if input[1] < 55.81447:
                if input[5] < 1080.2268:
                    var90 = 0.0387511
                else:
                    if input[5] < 1230.6306:
                        var90 = -0.033332873
                    else:
                        var90 = 0.01365143
            else:
                if input[0] < 21.280195:
                    if input[1] < 64.23323:
                        var90 = -0.0055964827
                    else:
                        var90 = -0.039076693
                else:
                    if input[0] < 25.087263:
                        var90 = 0.021574477
                    else:
                        var90 = -0.005208349
    else:
        var90 = -0.038295526
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var91 = 0.0023073717
            else:
                var91 = 0.0386835
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.260155:
                    if input[3] < 21.621714:
                        var91 = -0.0326734
                    else:
                        var91 = 0.005784548
                else:
                    if input[5] < 1007.39386:
                        var91 = 0.038028307
                    else:
                        var91 = -0.005278614
            else:
                var91 = -0.02558266
    else:
        var91 = -0.037980556
    if input[2] < 462.86743:
        if input[2] < 407.72763:
            if input[5] < 1105.8707:
                var92 = 0.033846736
            else:
                if input[1] < 81.52184:
                    var92 = 0.009504938
                else:
                    var92 = -0.00557714
        else:
            if input[1] < 55.81447:
                if input[4] < 7.243017:
                    var92 = -0.016228227
                else:
                    if input[0] < 23.958542:
                        var92 = 0.04495263
                    else:
                        var92 = 0.0034304278
            else:
                if input[1] < 62.443443:
                    var92 = -0.03140034
                else:
                    if input[0] < 30.605228:
                        var92 = -0.011372893
                    else:
                        var92 = 0.018217532
    else:
        var92 = -0.037525073
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var93 = 0.0015679443
            else:
                var93 = 0.03755003
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.119766:
                    if input[3] < 21.621714:
                        var93 = -0.031908292
                    else:
                        var93 = 0.005555043
                else:
                    if input[5] < 1007.39386:
                        var93 = 0.03703524
                    else:
                        var93 = -0.0055558137
            else:
                var93 = -0.024989149
    else:
        var93 = -0.03716825
    if input[4] < 7.3822474:
        if input[5] < 395.23544:
            var94 = 0.025815874
        else:
            if input[5] < 523.5276:
                if input[4] < 7.1964808:
                    var94 = -0.02680153
                else:
                    var94 = -0.0033780586
            else:
                if input[4] < 7.256852:
                    if input[0] < 22.883705:
                        var94 = -0.01021039
                    else:
                        var94 = 0.02540343
                else:
                    if input[1] < 83.43807:
                        var94 = 0.005252684
                    else:
                        var94 = -0.019076964
    else:
        if input[0] < 33.13334:
            var94 = -0.038043175
        else:
            var94 = -0.003825511
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[2] < 452.94366:
                if input[2] < 399.29376:
                    var95 = 0.029995415
                else:
                    if input[5] < 2244.283:
                        var95 = -0.009550664
                    else:
                        var95 = 0.014740159
            else:
                var95 = 0.034870174
        else:
            if input[0] < 30.878813:
                if input[0] < 21.619698:
                    var95 = 0.00861283
                else:
                    if input[3] < 91.50338:
                        var95 = -0.03722317
                    else:
                        var95 = -0.004837817
            else:
                if input[2] < 429.77728:
                    var95 = 0.020941429
                else:
                    var95 = -0.0056420113
    else:
        var95 = -0.036434162
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[2] < 452.94366:
                if input[2] < 399.29376:
                    var96 = 0.029578269
                else:
                    if input[5] < 2244.283:
                        var96 = -0.00892237
                    else:
                        var96 = 0.014402888
            else:
                var96 = 0.033894457
        else:
            if input[0] < 30.878813:
                if input[0] < 21.619698:
                    var96 = 0.008270944
                else:
                    if input[3] < 91.50338:
                        var96 = -0.036221884
                    else:
                        var96 = -0.0046210117
            else:
                if input[2] < 429.77728:
                    var96 = 0.020132711
                else:
                    var96 = -0.005775502
    else:
        var96 = -0.036039006
    var97 = var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[2] < 452.94366:
                if input[2] < 399.29376:
                    var98 = 0.02905471
                else:
                    if input[5] < 2244.283:
                        var98 = -0.008539165
                    else:
                        var98 = 0.0139359655
            else:
                var98 = 0.032878924
        else:
            if input[1] < 83.43807:
                if input[1] < 77.085434:
                    if input[0] < 21.619698:
                        var98 = 0.020618612
                    else:
                        var98 = -0.024441296
                else:
                    var98 = 0.023961343
            else:
                var98 = -0.026443845
    else:
        var98 = -0.035652336
    if input[2] < 462.86743:
        if input[5] < 938.6545:
            if input[3] < 29.437603:
                if input[1] < 86.296745:
                    if input[1] < 60.456154:
                        var99 = 0.02387806
                    else:
                        var99 = -0.013560575
                else:
                    var99 = 0.027813528
            else:
                var99 = 0.036516394
        else:
            if input[5] < 1294.5337:
                if input[5] < 1040.2141:
                    var99 = -0.0056320424
                else:
                    var99 = -0.034603126
            else:
                if input[4] < 7.3376346:
                    if input[5] < 4554.5503:
                        var99 = 0.02211616
                    else:
                        var99 = -0.01765374
                else:
                    var99 = -0.021834139
    else:
        var99 = -0.035249423
    if input[2] < 462.86743:
        if input[5] < 938.6545:
            if input[3] < 29.437603:
                if input[0] < 35.580082:
                    if input[5] < 431.76425:
                        var100 = 0.017114658
                    else:
                        var100 = -0.020954793
                else:
                    var100 = 0.02308848
            else:
                var100 = 0.03581735
        else:
            if input[5] < 1294.5337:
                if input[1] < 45.1439:
                    var100 = -0.0012817461
                else:
                    var100 = -0.03129578
            else:
                if input[4] < 7.3376346:
                    if input[5] < 4554.5503:
                        var100 = 0.02125597
                    else:
                        var100 = -0.017147457
                else:
                    var100 = -0.02143295
    else:
        var100 = -0.034848135
    if input[2] < 462.86743:
        if input[5] < 938.6545:
            if input[3] < 29.437603:
                if input[1] < 86.296745:
                    if input[1] < 60.456154:
                        var101 = 0.02381023
                    else:
                        var101 = -0.012878331
                else:
                    var101 = 0.027485713
            else:
                var101 = 0.035199586
        else:
            if input[5] < 1294.5337:
                if input[5] < 1040.2141:
                    var101 = -0.0049273483
                else:
                    var101 = -0.03353182
            else:
                if input[4] < 7.3376346:
                    if input[5] < 4554.5503:
                        var101 = 0.020637328
                    else:
                        var101 = -0.016632568
                else:
                    var101 = -0.021097336
    else:
        var101 = -0.034451015
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var102 = 0.00006262233
            else:
                var102 = 0.034982443
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.119766:
                    if input[3] < 21.621714:
                        var102 = -0.028470278
                    else:
                        var102 = 0.0040446734
                else:
                    if input[3] < 24.631073:
                        var102 = 0.03372278
                    else:
                        var102 = -0.00012332221
            else:
                var102 = -0.02275052
    else:
        var102 = -0.03409713
    if input[2] < 462.86743:
        if input[5] < 938.6545:
            if input[3] < 29.437603:
                if input[0] < 35.580082:
                    if input[5] < 431.76425:
                        var103 = 0.016330404
                    else:
                        var103 = -0.019614419
                else:
                    var103 = 0.02213742
            else:
                var103 = 0.034375552
        else:
            if input[5] < 1294.5337:
                if input[1] < 45.1439:
                    var103 = -0.00090225023
                else:
                    var103 = -0.030300096
            else:
                if input[0] < 22.883705:
                    if input[2] < 429.77728:
                        var103 = 0.010883964
                    else:
                        var103 = -0.037220802
                else:
                    if input[1] < 83.59157:
                        var103 = 0.025398815
                    else:
                        var103 = -0.008161548
    else:
        var103 = -0.033683177
    if input[4] < 7.4472933:
        if input[2] < 429.77728:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var104 = -0.0035227505
                else:
                    var104 = 0.034176458
            else:
                if input[0] < 30.878813:
                    if input[4] < 7.2781405:
                        var104 = 0.013314764
                    else:
                        var104 = -0.03333756
                else:
                    if input[4] < 7.2208877:
                        var104 = -0.011568416
                    else:
                        var104 = 0.023467636
        else:
            if input[5] < 888.78937:
                if input[4] < 7.293997:
                    if input[4] < 7.243017:
                        var104 = -0.0038450107
                    else:
                        var104 = 0.03149875
                else:
                    var104 = -0.009544638
            else:
                if input[5] < 4126.573:
                    if input[1] < 46.92819:
                        var104 = 0.0043925806
                    else:
                        var104 = -0.041647803
                else:
                    var104 = 0.0171013
    else:
        var104 = -0.033310484
    if input[2] < 462.86743:
        if input[4] < 7.256852:
            if input[1] < 88.93255:
                if input[4] < 7.243017:
                    if input[2] < 429.77728:
                        var105 = 0.014951688
                    else:
                        var105 = -0.03494559
                else:
                    var105 = 0.029770691
            else:
                var105 = 0.03345005
        else:
            if input[0] < 34.571377:
                if input[0] < 25.986551:
                    if input[1] < 66.80687:
                        var105 = 0.01964411
                    else:
                        var105 = -0.009351608
                else:
                    if input[0] < 30.878813:
                        var105 = -0.04010207
                    else:
                        var105 = -0.0013111675
            else:
                if input[0] < 36.583706:
                    var105 = 0.027804116
                else:
                    var105 = 0.0012397695
    else:
        var105 = -0.03288116
    if input[4] < 7.4472933:
        if input[2] < 429.77728:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var106 = -0.0036443602
                else:
                    var106 = 0.033173602
            else:
                if input[0] < 27.043375:
                    var106 = -0.020139841
                else:
                    if input[3] < 103.43883:
                        var106 = 0.012522163
                    else:
                        var106 = -0.011486012
        else:
            if input[5] < 888.78937:
                if input[4] < 7.293997:
                    if input[4] < 7.243017:
                        var106 = -0.0033879594
                    else:
                        var106 = 0.030532716
                else:
                    var106 = -0.009060223
            else:
                if input[5] < 4126.573:
                    if input[1] < 46.92819:
                        var106 = 0.0041189305
                    else:
                        var106 = -0.041025665
                else:
                    var106 = 0.016460376
    else:
        var106 = -0.0325047
    if input[2] < 462.86743:
        if input[4] < 7.256852:
            if input[1] < 88.93255:
                if input[4] < 7.243017:
                    if input[2] < 429.77728:
                        var107 = 0.014014441
                    else:
                        var107 = -0.034263667
                else:
                    var107 = 0.029042443
            else:
                var107 = 0.03291339
        else:
            if input[0] < 34.571377:
                if input[0] < 25.986551:
                    if input[1] < 66.80687:
                        var107 = 0.018960085
                    else:
                        var107 = -0.009528334
                else:
                    if input[4] < 7.365371:
                        var107 = -0.039294455
                    else:
                        var107 = -0.00060880976
            else:
                if input[0] < 36.583706:
                    var107 = 0.027087161
                else:
                    var107 = 0.0014594446
    else:
        var107 = -0.032053843
    if input[4] < 7.4472933:
        if input[5] < 431.76425:
            if input[1] < 73.03348:
                var108 = -0.0014341928
            else:
                var108 = 0.033133183
        else:
            if input[4] < 7.3523836:
                if input[0] < 36.119766:
                    if input[3] < 21.621714:
                        var108 = -0.027508864
                    else:
                        var108 = 0.004013401
                else:
                    if input[3] < 24.631073:
                        var108 = 0.0321126
                    else:
                        var108 = 0.0004142386
            else:
                var108 = -0.023559077
    else:
        var108 = -0.031698655
    if input[2] < 462.86743:
        if input[4] < 7.256852:
            if input[5] < 4452.413:
                if input[2] < 429.77728:
                    if input[3] < 20.239094:
                        var109 = -0.0052888514
                    else:
                        var109 = 0.03883641
                else:
                    if input[4] < 7.243017:
                        var109 = -0.020240974
                    else:
                        var109 = 0.027973918
            else:
                var109 = -0.014027983
        else:
            if input[0] < 34.571377:
                if input[0] < 25.986551:
                    if input[1] < 66.80687:
                        var109 = 0.018194044
                    else:
                        var109 = -0.00909872
                else:
                    if input[0] < 30.878813:
                        var109 = -0.038890876
                    else:
                        var109 = -0.00081048254
            else:
                if input[0] < 36.583706:
                    var109 = 0.02639635
                else:
                    var109 = 0.00133198
    else:
        var109 = -0.03129901
    if input[2] < 462.86743:
        if input[2] < 407.72763:
            if input[5] < 1105.8707:
                var110 = 0.028640358
            else:
                var110 = 0.002484991
        else:
            if input[1] < 55.81447:
                if input[4] < 7.243017:
                    var110 = -0.015869534
                else:
                    if input[0] < 23.958542:
                        var110 = 0.038783614
                    else:
                        var110 = 0.0045184097
            else:
                if input[0] < 21.280195:
                    if input[1] < 64.23323:
                        var110 = -0.0061515043
                    else:
                        var110 = -0.035791762
                else:
                    if input[1] < 62.443443:
                        var110 = -0.026394809
                    else:
                        var110 = 0.0058152676
    else:
        var110 = -0.0308867
    if input[4] < 7.3822474:
        if input[5] < 395.23544:
            var111 = 0.02118123
        else:
            if input[5] < 523.5276:
                var111 = -0.019116495
            else:
                if input[4] < 7.256852:
                    if input[0] < 22.883705:
                        var111 = -0.011711601
                    else:
                        var111 = 0.023259556
                else:
                    if input[0] < 34.70366:
                        var111 = -0.010657571
                    else:
                        var111 = 0.015551679
    else:
        if input[3] < 62.92014:
            var111 = -0.007774127
        else:
            var111 = -0.030032909
    if input[4] < 7.4472933:
        if input[2] < 429.77728:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var112 = -0.0043252287
                else:
                    var112 = 0.032300774
            else:
                if input[0] < 27.043375:
                    var112 = -0.018804677
                else:
                    if input[0] < 34.86882:
                        var112 = 0.015086091
                    else:
                        var112 = -0.0073443176
        else:
            if input[5] < 888.78937:
                if input[4] < 7.293997:
                    if input[3] < 22.530313:
                        var112 = -0.00024502625
                    else:
                        var112 = 0.029282186
                else:
                    var112 = -0.008827964
            else:
                if input[5] < 4126.573:
                    if input[1] < 46.92819:
                        var112 = 0.003354077
                    else:
                        var112 = -0.04025068
                else:
                    var112 = 0.01627527
    else:
        var112 = -0.030162966
    if input[4] < 7.3822474:
        if input[3] < 133.33838:
            if input[5] < 938.6545:
                if input[3] < 29.437603:
                    if input[0] < 35.580082:
                        var113 = -0.00877682
                    else:
                        var113 = 0.018947948
                else:
                    var113 = 0.032904338
            else:
                if input[2] < 429.77728:
                    if input[1] < 83.59157:
                        var113 = 0.026230065
                    else:
                        var113 = -0.016365267
                else:
                    if input[1] < 46.92819:
                        var113 = 0.0041390075
                    else:
                        var113 = -0.031792164
        else:
            if input[2] < 423.73544:
                var113 = 0.024438793
            else:
                var113 = 0.0041860873
    else:
        if input[0] < 30.605228:
            var113 = -0.0291953
        else:
            var113 = -0.007781944
    if input[2] < 462.86743:
        if input[4] < 7.256852:
            if input[5] < 4452.413:
                if input[3] < 21.621714:
                    var114 = -0.008066981
                else:
                    if input[0] < 22.883705:
                        var114 = -0.004358606
                    else:
                        var114 = 0.035930775
            else:
                var114 = -0.0141352555
        else:
            if input[0] < 34.571377:
                if input[0] < 25.986551:
                    if input[3] < 29.437603:
                        var114 = -0.014180786
                    else:
                        var114 = 0.013833279
                else:
                    if input[4] < 7.365371:
                        var114 = -0.037888825
                    else:
                        var114 = 0.00007838628
            else:
                if input[0] < 36.583706:
                    var114 = 0.025160214
                else:
                    var114 = 0.0016557679
    else:
        var114 = -0.029418131
    if input[4] < 7.3822474:
        if input[5] < 395.23544:
            var115 = 0.02069967
        else:
            if input[5] < 523.5276:
                var115 = -0.01829018
            else:
                if input[4] < 7.256852:
                    if input[3] < 60.078743:
                        var115 = 0.02870116
                    else:
                        var115 = -0.0020729236
                else:
                    if input[0] < 34.70366:
                        var115 = -0.0098495325
                    else:
                        var115 = 0.015363638
    else:
        if input[1] < 78.951355:
            var115 = -0.028541317
        else:
            var115 = -0.0076916623
    if input[4] < 7.4472933:
        if input[2] < 429.77728:
            if input[0] < 25.986551:
                if input[0] < 21.101826:
                    var116 = -0.0034461857
                else:
                    var116 = 0.031439602
            else:
                if input[0] < 30.878813:
                    if input[0] < 27.195625:
                        var116 = -0.016850516
                    else:
                        var116 = -0.0033151377
                else:
                    if input[4] < 7.2208877:
                        var116 = -0.012822434
                    else:
                        var116 = 0.021219341
        else:
            if input[5] < 888.78937:
                if input[4] < 7.293997:
                    if input[3] < 22.530313:
                        var116 = -0.00057274057
                    else:
                        var116 = 0.028249292
                else:
                    var116 = -0.008329041
            else:
                if input[5] < 4126.573:
                    if input[1] < 46.92819:
                        var116 = 0.002510977
                    else:
                        var116 = -0.039299168
                else:
                    var116 = 0.016655615
    else:
        var116 = -0.02875485
    if input[4] < 7.3822474:
        if input[3] < 133.33838:
            if input[5] < 938.6545:
                if input[5] < 652.72906:
                    if input[5] < 395.23544:
                        var117 = 0.018796612
                    else:
                        var117 = -0.010798542
                else:
                    var117 = 0.028644968
            else:
                if input[2] < 429.77728:
                    if input[1] < 83.59157:
                        var117 = 0.02562364
                    else:
                        var117 = -0.015380773
                else:
                    if input[1] < 46.92819:
                        var117 = 0.003227022
                    else:
                        var117 = -0.03051782
        else:
            if input[2] < 423.73544:
                var117 = 0.023791853
            else:
                var117 = 0.004487411
    else:
        var117 = -0.023771076
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[5] < 4554.5503:
                if input[0] < 22.883705:
                    if input[4] < 7.2208877:
                        var118 = 0.018253088
                    else:
                        var118 = -0.024223713
                else:
                    if input[0] < 24.973854:
                        var118 = 0.035361674
                    else:
                        var118 = 0.007010384
            else:
                var118 = -0.016038282
        else:
            if input[0] < 30.878813:
                if input[0] < 21.619698:
                    var118 = 0.0069029303
                else:
                    var118 = -0.027005404
            else:
                if input[1] < 75.8811:
                    var118 = -0.00551295
                else:
                    var118 = 0.017450344
    else:
        var118 = -0.02804996
    if input[2] < 462.86743:
        if input[4] < 7.293997:
            if input[5] < 4554.5503:
                if input[5] < 3097.8657:
                    if input[2] < 452.94366:
                        var119 = -0.0012265963
                    else:
                        var119 = 0.028632378
                else:
                    var119 = 0.033572175
            else:
                var119 = -0.015639158
        else:
            if input[1] < 83.43807:
                if input[1] < 77.085434:
                    if input[0] < 21.619698:
                        var119 = 0.017355163
                    else:
                        var119 = -0.021014355
                else:
                    var119 = 0.020667957
            else:
                var119 = -0.022998573
    else:
        var119 = -0.02764996
    if input[2] < 462.86743:
        if input[2] < 407.72763:
            if input[1] < 82.106895:
                var120 = 0.021831814
            else:
                var120 = 0.00020666978
        else:
            if input[1] < 55.81447:
                if input[4] < 7.243017:
                    var120 = -0.014519629
                else:
                    if input[0] < 23.958542:
                        var120 = 0.035924576
                    else:
                        var120 = 0.004830724
            else:
                if input[0] < 21.280195:
                    var120 = -0.024738401
                else:
                    if input[0] < 25.087263:
                        var120 = 0.016251648
                    else:
                        var120 = -0.0077829
    else:
        var120 = -0.0272833
    if input[4] < 7.3822474:
        if input[3] < 133.33838:
            if input[1] < 55.81447:
                if input[5] < 1105.8707:
                    var121 = 0.03169033
                else:
                    if input[3] < 55.90395:
                        var121 = -0.018028516
                    else:
                        var121 = 0.010187386
            else:
                if input[0] < 37.875954:
                    if input[5] < 395.23544:
                        var121 = 0.015626555
                    else:
                        var121 = -0.012431658
                else:
                    var121 = 0.01816471
        else:
            if input[4] < 7.2781405:
                var121 = 0.022219086
            else:
                var121 = 0.003489795
    else:
        var121 = -0.022458013
    if input[2] < 462.86743:
        if input[4] < 7.256852:
            if input[5] < 459.61935:
                var122 = -0.011003052
            else:
                if input[3] < 60.078743:
                    if input[0] < 24.973854:
                        var122 = 0.03528322
                    else:
                        var122 = 0.010856517
                else:
                    if input[1] < 61.794598:
                        var122 = -0.0199615
                    else:
                        var122 = 0.011528568
        else:
            if input[0] < 34.571377:
                if input[0] < 25.986551:
                    if input[1] < 66.80687:
                        var122 = 0.017651262
                    else:
                        var122 = -0.0076513453
                else:
                    if input[0] < 30.878813:
                        var122 = -0.036685497
                    else:
                        var122 = -0.0010580723
            else:
                if input[0] < 36.583706:
                    var122 = 0.023940418
                else:
                    var122 = 0.0017549515
    else:
        var122 = -0.02656264
    if input[4] < 7.3376346:
        if input[5] < 4554.5503:
            if input[5] < 3138.0425:
                if input[0] < 35.580082:
                    if input[0] < 24.484314:
                        var123 = 0.010820228
                    else:
                        var123 = -0.019216657
                else:
                    var123 = 0.020471042
            else:
                var123 = 0.035216913
        else:
            var123 = -0.01715991
    else:
        if input[5] < 431.76425:
            var123 = 0.017199762
        else:
            if input[1] < 77.56267:
                var123 = -0.009705539
            else:
                var123 = -0.034277793
    if input[2] < 429.77728:
        if input[3] < 31.188398:
            if input[1] < 76.9051:
                if input[1] < 67.65288:
                    var124 = 0.001218825
                else:
                    var124 = -0.028813666
            else:
                var124 = 0.016897826
        else:
            if input[1] < 83.82618:
                var124 = 0.031012645
            else:
                if input[1] < 88.93255:
                    var124 = -0.01927074
                else:
                    var124 = 0.006734793
    else:
        if input[5] < 751.1005:
            if input[2] < 439.61963:
                var124 = 0.022345854
            else:
                var124 = -0.0021485991
        else:
            if input[5] < 4126.573:
                if input[1] < 46.92819:
                    var124 = -0.00013793063
                else:
                    var124 = -0.03831937
            else:
                var124 = 0.010257176
    if input[4] < 7.293997:
        if input[5] < 4496.4277:
            if input[0] < 22.883705:
                if input[5] < 1105.8707:
                    var125 = 0.007149007
                else:
                    var125 = -0.020437842
            else:
                if input[0] < 24.973854:
                    if input[2] < 433.85468:
                        var125 = 0.009780437
                    else:
                        var125 = 0.038579013
                else:
                    if input[5] < 3097.8657:
                        var125 = -0.00535719
                    else:
                        var125 = 0.03154534
        else:
            var125 = -0.014702745
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var125 = 0.009768981
                else:
                    var125 = -0.020195438
            else:
                var125 = 0.014296481
        else:
            if input[0] < 36.119766:
                var125 = -0.034611918
            else:
                var125 = 0.00065359345
    if input[4] < 7.293997:
        if input[5] < 4496.4277:
            if input[0] < 22.883705:
                if input[5] < 1105.8707:
                    var126 = 0.007143628
                else:
                    var126 = -0.019463627
            else:
                if input[0] < 24.973854:
                    if input[2] < 433.85468:
                        var126 = 0.00951536
                    else:
                        var126 = 0.03785777
                else:
                    if input[5] < 3097.8657:
                        var126 = -0.0050909664
                    else:
                        var126 = 0.03105387
        else:
            var126 = -0.01434242
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var126 = 0.009526657
                else:
                    var126 = -0.019667737
            else:
                var126 = 0.013906218
        else:
            if input[0] < 36.119766:
                var126 = -0.03417741
            else:
                var126 = 0.0006424245
    if input[2] < 429.77728:
        if input[3] < 31.188398:
            if input[5] < 431.76425:
                var127 = 0.015011172
            else:
                var127 = -0.019062689
        else:
            if input[1] < 83.82618:
                var127 = 0.030307656
            else:
                if input[1] < 88.93255:
                    var127 = -0.018518588
                else:
                    var127 = 0.0070375362
    else:
        if input[5] < 751.1005:
            if input[5] < 652.72906:
                if input[3] < 21.621714:
                    var127 = -0.012056935
                else:
                    var127 = 0.008999578
            else:
                var127 = 0.023996374
        else:
            if input[5] < 4126.573:
                if input[1] < 46.92819:
                    var127 = 0.00014425378
                else:
                    var127 = -0.037220236
            else:
                var127 = 0.009144546
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var128 = 0.0070129144
            else:
                var128 = -0.0186759
        else:
            if input[0] < 24.973854:
                var128 = 0.032947276
            else:
                if input[2] < 433.85468:
                    if input[1] < 86.296745:
                        var128 = 0.020140843
                    else:
                        var128 = -0.008959539
                else:
                    if input[0] < 29.121038:
                        var128 = -0.023492064
                    else:
                        var128 = 0.0024251428
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var128 = 0.009455759
                else:
                    var128 = -0.019646047
            else:
                var128 = 0.013318558
        else:
            if input[0] < 35.9314:
                var128 = -0.03340465
            else:
                var128 = 0.0005289658
    if input[4] < 7.293997:
        if input[2] < 452.94366:
            if input[2] < 439.61963:
                if input[5] < 4090.0388:
                    if input[3] < 82.98708:
                        var129 = 0.003447605
                    else:
                        var129 = 0.025899604
                else:
                    var129 = -0.0081673665
            else:
                var129 = -0.013053784
        else:
            var129 = 0.0250031
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var129 = 0.00923001
                else:
                    var129 = -0.019259997
            else:
                var129 = 0.0130732125
        else:
            if input[0] < 35.9314:
                var129 = -0.032901328
            else:
                var129 = 0.0003994725
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var130 = 0.006730159
            else:
                var130 = -0.018252978
        else:
            if input[0] < 24.973854:
                var130 = 0.03205827
            else:
                if input[0] < 36.119766:
                    if input[5] < 1230.6306:
                        var130 = -0.02170231
                    else:
                        var130 = 0.0075189057
                else:
                    var130 = 0.019209204
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var130 = 0.009208234
                else:
                    var130 = -0.018848164
            else:
                var130 = 0.01276245
        else:
            if input[0] < 35.9314:
                var130 = -0.032473076
            else:
                var130 = 0.0004624385
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var131 = 0.006608723
            else:
                var131 = -0.01772899
        else:
            if input[0] < 24.973854:
                if input[2] < 433.85468:
                    var131 = 0.009811638
                else:
                    var131 = 0.03657138
            else:
                if input[0] < 36.119766:
                    if input[5] < 1230.6306:
                        var131 = -0.021071808
                    else:
                        var131 = 0.0073049637
                else:
                    var131 = 0.018874455
    else:
        if input[2] < 452.94366:
            if input[0] < 34.329613:
                if input[0] < 23.014591:
                    var131 = 0.0068375603
                else:
                    if input[1] < 77.085434:
                        var131 = -0.028902564
                    else:
                        var131 = 0.0043059136
            else:
                var131 = 0.013816419
        else:
            var131 = -0.029234726
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var132 = 0.006425671
            else:
                var132 = -0.017231913
        else:
            if input[0] < 24.973854:
                if input[2] < 433.85468:
                    var132 = 0.009603776
                else:
                    var132 = 0.03616193
            else:
                if input[0] < 36.119766:
                    if input[5] < 1230.6306:
                        var132 = -0.02049621
                    else:
                        var132 = 0.00693817
                else:
                    var132 = 0.018547567
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var132 = 0.008896038
                else:
                    var132 = -0.018596282
            else:
                var132 = 0.012260523
        else:
            if input[0] < 35.385204:
                var132 = -0.031409
            else:
                var132 = -0.00008529585
    if input[4] < 7.3376346:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var133 = 0.009207349
                else:
                    if input[1] < 75.40523:
                        var133 = -0.032730486
                    else:
                        var133 = -0.008966227
            else:
                if input[5] < 919.0119:
                    var133 = 0.030856092
                else:
                    if input[5] < 1284.4312:
                        var133 = -0.025220323
                    else:
                        var133 = 0.011697247
        else:
            var133 = 0.020652654
    else:
        if input[5] < 1040.2141:
            var133 = 0.0064201276
        else:
            var133 = -0.026893258
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var134 = 0.006387058
            else:
                var134 = -0.01658022
        else:
            if input[0] < 24.973854:
                if input[2] < 433.85468:
                    var134 = 0.009241181
                else:
                    var134 = 0.03529101
            else:
                if input[1] < 78.951355:
                    if input[2] < 433.85468:
                        var134 = 0.018780164
                    else:
                        var134 = -0.00781667
                else:
                    if input[1] < 90.07144:
                        var134 = -0.023046317
                    else:
                        var134 = 0.004952851
    else:
        if input[2] < 433.85468:
            if input[0] < 30.878813:
                if input[0] < 24.035046:
                    var134 = 0.008868904
                else:
                    var134 = -0.017780585
            else:
                var134 = 0.012079629
        else:
            if input[0] < 35.385204:
                var134 = -0.030765815
            else:
                var134 = -0.00028903768
    if input[4] < 7.3376346:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var135 = 0.008498166
                else:
                    if input[1] < 75.40523:
                        var135 = -0.03216166
                    else:
                        var135 = -0.008755574
            else:
                if input[5] < 919.0119:
                    var135 = 0.030184535
                else:
                    if input[5] < 1284.4312:
                        var135 = -0.024424689
                    else:
                        var135 = 0.011417695
        else:
            var135 = 0.020160664
    else:
        if input[5] < 1040.2141:
            var135 = 0.0062410436
        else:
            var135 = -0.025892157
    if input[4] < 7.256852:
        if input[5] < 459.61935:
            var136 = -0.012045552
        else:
            if input[3] < 60.078743:
                if input[2] < 433.85468:
                    var136 = 0.03300369
                else:
                    var136 = 0.008757335
            else:
                if input[1] < 61.794598:
                    var136 = -0.017242743
                else:
                    if input[0] < 31.948093:
                        var136 = 0.017561462
                    else:
                        var136 = -0.0016716028
    else:
        if input[5] < 442.2211:
            var136 = 0.013558437
        else:
            if input[4] < 7.3523836:
                if input[0] < 34.70366:
                    if input[0] < 25.986551:
                        var136 = 0.0058786008
                    else:
                        var136 = -0.030424094
                else:
                    var136 = 0.016498644
            else:
                var136 = -0.027881185
    if input[2] < 429.77728:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                var137 = 0.033611137
            else:
                if input[0] < 30.878813:
                    if input[1] < 66.80687:
                        var137 = 0.014035116
                    else:
                        var137 = -0.02198724
                else:
                    var137 = 0.018484477
        else:
            if input[5] < 514.5741:
                var137 = -0.015860505
            else:
                var137 = 0.0025272726
    else:
        if input[5] < 888.78937:
            if input[5] < 652.72906:
                if input[0] < 25.742085:
                    var137 = 0.000016672831
                else:
                    var137 = -0.00112782
            else:
                var137 = 0.020456428
        else:
            if input[5] < 4126.573:
                if input[1] < 46.92819:
                    var137 = 0.00079575944
                else:
                    var137 = -0.03685724
            else:
                var137 = 0.009618268
    if input[4] < 7.293997:
        if input[0] < 22.883705:
            if input[5] < 1105.8707:
                var138 = 0.005849086
            else:
                var138 = -0.015827278
        else:
            if input[0] < 24.973854:
                var138 = 0.028828416
            else:
                if input[0] < 36.119766:
                    if input[5] < 1230.6306:
                        var138 = -0.019477962
                    else:
                        var138 = 0.0060364297
                else:
                    var138 = 0.017495917
    else:
        if input[2] < 433.85468:
            if input[3] < 46.6483:
                if input[1] < 76.9051:
                    var138 = -0.019439157
                else:
                    var138 = 0.013624108
            else:
                if input[5] < 2890.5234:
                    var138 = 0.01690764
                else:
                    var138 = -0.00018522315
        else:
            if input[5] < 1007.39386:
                var138 = -0.0017891735
            else:
                var138 = -0.02916917
    if input[4] < 7.3376346:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var139 = 0.008006012
                else:
                    if input[1] < 75.40523:
                        var139 = -0.031366866
                    else:
                        var139 = -0.008595388
            else:
                if input[5] < 919.0119:
                    var139 = 0.029115135
                else:
                    if input[5] < 1284.4312:
                        var139 = -0.022964213
                    else:
                        var139 = 0.011232067
        else:
            var139 = 0.019865666
    else:
        if input[1] < 81.32996:
            if input[1] < 77.32407:
                var139 = -0.014440681
            else:
                var139 = 0.023007696
        else:
            var139 = -0.027853234
    if input[2] < 429.77728:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                var140 = 0.03297983
            else:
                if input[0] < 30.878813:
                    if input[1] < 66.80687:
                        var140 = 0.013570884
                    else:
                        var140 = -0.020957982
                else:
                    var140 = 0.018399443
        else:
            if input[5] < 630.765:
                var140 = -0.012222747
            else:
                var140 = 0.000012837084
    else:
        if input[5] < 888.78937:
            if input[5] < 652.72906:
                if input[0] < 25.742085:
                    var140 = 0.00012505217
                else:
                    var140 = -0.00053784315
            else:
                var140 = 0.019978555
        else:
            if input[5] < 4126.573:
                if input[1] < 46.92819:
                    var140 = 0.00065935386
                else:
                    var140 = -0.03583781
            else:
                var140 = 0.008945032
    if input[4] < 7.3822474:
        if input[1] < 55.81447:
            if input[5] < 1105.8707:
                var141 = 0.029252177
            else:
                if input[1] < 44.30488:
                    var141 = -0.010798383
                else:
                    var141 = 0.00761348
        else:
            if input[3] < 30.156466:
                if input[3] < 18.372265:
                    if input[1] < 73.03348:
                        var141 = -0.0061142184
                    else:
                        var141 = 0.018942581
                else:
                    if input[1] < 85.703255:
                        var141 = -0.027766436
                    else:
                        var141 = -0.0071132393
            else:
                if input[5] < 4554.5503:
                    if input[2] < 417.8072:
                        var141 = 0.028741488
                    else:
                        var141 = 0.0004691958
                else:
                    var141 = -0.009033302
    else:
        var141 = -0.016038446
    if input[4] < 7.3376346:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var142 = 0.0075737545
                else:
                    if input[1] < 75.40523:
                        var142 = -0.030109093
                    else:
                        var142 = -0.008024003
            else:
                if input[5] < 919.0119:
                    var142 = 0.028363807
                else:
                    if input[5] < 1284.4312:
                        var142 = -0.022140399
                    else:
                        var142 = 0.011431356
        else:
            var142 = 0.019755905
    else:
        if input[1] < 81.32996:
            if input[1] < 77.32407:
                var142 = -0.013856835
            else:
                var142 = 0.02208961
        else:
            var142 = -0.027031759
    if input[4] < 7.3523836:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var143 = 0.007026019
                else:
                    if input[1] < 76.9051:
                        var143 = -0.029461384
                    else:
                        var143 = -0.007995068
            else:
                if input[5] < 919.0119:
                    var143 = 0.027766442
                else:
                    if input[3] < 48.123383:
                        var143 = -0.016907923
                    else:
                        var143 = 0.008000239
        else:
            var143 = 0.019352384
    else:
        if input[3] < 13.901499:
            var143 = 0.0072589717
        else:
            var143 = -0.022566006
    if input[2] < 429.77728:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                var144 = 0.03226745
            else:
                if input[0] < 30.878813:
                    if input[0] < 25.986551:
                        var144 = 0.007024647
                    else:
                        var144 = -0.026956176
                else:
                    var144 = 0.01819737
        else:
            var144 = -0.007633604
    else:
        if input[5] < 888.78937:
            if input[2] < 439.61963:
                var144 = 0.018873837
            else:
                var144 = -0.0010288995
        else:
            if input[5] < 4126.573:
                if input[1] < 46.92819:
                    var144 = 0.0011122504
                else:
                    var144 = -0.034911014
            else:
                var144 = 0.009123638
    if input[4] < 7.3523836:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var145 = 0.006891051
                else:
                    var145 = -0.024076572
            else:
                if input[5] < 938.6545:
                    var145 = 0.026393075
                else:
                    if input[3] < 48.123383:
                        var145 = -0.018252151
                    else:
                        var145 = 0.008230896
        else:
            var145 = 0.019551745
    else:
        if input[3] < 13.901499:
            var145 = 0.0071206577
        else:
            var145 = -0.021801306
    if input[2] < 429.77728:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                var146 = 0.03158609
            else:
                if input[0] < 30.878813:
                    if input[0] < 25.986551:
                        var146 = 0.006875758
                    else:
                        var146 = -0.026418466
                else:
                    var146 = 0.017769193
        else:
            var146 = -0.0076669194
    else:
        if input[5] < 888.78937:
            if input[2] < 439.61963:
                var146 = 0.018728686
            else:
                var146 = -0.0012205857
        else:
            if input[5] < 4111.662:
                if input[1] < 46.92819:
                    var146 = 0.0008400364
                else:
                    var146 = -0.03435677
            else:
                var146 = 0.008332295
    if input[4] < 7.3523836:
        if input[0] < 36.119766:
            if input[3] < 29.437603:
                if input[1] < 67.20121:
                    var147 = 0.006411283
                else:
                    var147 = -0.023743648
            else:
                if input[5] < 938.6545:
                    var147 = 0.025674824
                else:
                    if input[5] < 1284.4312:
                        var147 = -0.014099366
                    else:
                        var147 = 0.008361663
        else:
            var147 = 0.019402819
    else:
        if input[3] < 13.901499:
            var147 = 0.0067011677
        else:
            var147 = -0.02131128
    if input[4] < 7.3523836:
        if input[3] < 13.104021:
            var148 = -0.012301122
        else:
            if input[2] < 423.73544:
                if input[1] < 86.296745:
                    var148 = 0.028969495
                else:
                    var148 = -0.0025402408
            else:
                if input[0] < 23.014591:
                    if input[1] < 62.774673:
                        var148 = 0.0037390764
                    else:
                        var148 = -0.029607235
                else:
                    if input[1] < 78.1442:
                        var148 = 0.01707221
                    else:
                        var148 = -0.0045062536
    else:
        if input[3] < 13.901499:
            var148 = 0.0067961426
        else:
            var148 = -0.020653289
    if input[2] < 429.77728:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                var149 = 0.03078543
            else:
                if input[0] < 30.878813:
                    if input[0] < 25.986551:
                        var149 = 0.007374426
                    else:
                        var149 = -0.02573339
                else:
                    var149 = 0.017398244
        else:
            var149 = -0.007618595
    else:
        if input[5] < 888.78937:
            if input[2] < 439.61963:
                var149 = 0.018853506
            else:
                var149 = -0.0013939807
        else:
            if input[5] < 4111.662:
                if input[1] < 46.92819:
                    var149 = 0.0011228871
                else:
                    var149 = -0.033706743
            else:
                var149 = 0.008241058
    if input[4] < 7.3523836:
        if input[0] < 36.119766:
            if input[0] < 25.986551:
                if input[2] < 423.73544:
                    var150 = 0.028647674
                else:
                    if input[0] < 23.014591:
                        var150 = -0.01459907
                    else:
                        var150 = 0.016374534
            else:
                if input[3] < 42.17376:
                    var150 = -0.026172979
                else:
                    if input[1] < 86.296745:
                        var150 = 0.0147175
                    else:
                        var150 = -0.00924134
        else:
            var150 = 0.019485118
    else:
        if input[3] < 13.901499:
            var150 = 0.0064508985
        else:
            var150 = -0.020301174
    if input[4] < 7.3523836:
        if input[0] < 36.119766:
            if input[0] < 25.986551:
                if input[2] < 423.73544:
                    var151 = 0.028390616
                else:
                    if input[0] < 23.014591:
                        var151 = -0.013888716
                    else:
                        var151 = 0.016079828
            else:
                if input[3] < 42.17376:
                    var151 = -0.025536967
                else:
                    if input[1] < 86.296745:
                        var151 = 0.014485727
                    else:
                        var151 = -0.008782603
        else:
            var151 = 0.019200925
    else:
        if input[3] < 13.901499:
            var151 = 0.006542202
        else:
            var151 = -0.019964958
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var152 = -0.07463422
            else:
                var152 = 0.00029522585
        else:
            var152 = 0.010726034
    else:
        if input[2] < 737.73047:
            if input[2] < 433.85468:
                if input[5] < 4315.5137:
                    if input[5] < 537.6977:
                        var152 = 0.060625013
                    else:
                        var152 = -0.015928261
                else:
                    if input[0] < 26.50474:
                        var152 = 0.0432373
                    else:
                        var152 = 0.13499646
            else:
                if input[4] < 8.151678:
                    if input[4] < 7.293997:
                        var152 = 0.09096066
                    else:
                        var152 = 0.1491811
                else:
                    if input[2] < 721.7867:
                        var152 = 0.115403704
                    else:
                        var152 = 0.038584508
        else:
            if input[2] < 753.20294:
                if input[1] < 58.03831:
                    if input[0] < 26.043957:
                        var152 = -0.0695116
                    else:
                        var152 = -0.005717687
                else:
                    if input[4] < 8.301448:
                        var152 = 0.025175137
                    else:
                        var152 = -0.06641266
            else:
                if input[2] < 768.4635:
                    if input[4] < 8.092142:
                        var152 = 0.0432373
                    else:
                        var152 = -0.057847437
                else:
                    if input[5] < 1387.4912:
                        var152 = 0.00029522585
                    else:
                        var152 = -0.07461809
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var153 = -0.07188632
            else:
                var153 = -0.000014205415
        else:
            var153 = 0.0094101885
    else:
        if input[2] < 737.73047:
            if input[2] < 429.77728:
                if input[0] < 25.986551:
                    if input[4] < 7.3376346:
                        var153 = -0.054805703
                    else:
                        var153 = 0.042695023
                else:
                    if input[0] < 37.875954:
                        var153 = 0.08192452
                    else:
                        var153 = -0.04762375
            else:
                if input[4] < 8.151678:
                    if input[4] < 7.293997:
                        var153 = 0.07734693
                    else:
                        var153 = 0.12901382
                else:
                    if input[2] < 721.7867:
                        var153 = 0.10159587
                    else:
                        var153 = 0.0350378
        else:
            if input[2] < 753.20294:
                if input[1] < 58.03831:
                    if input[0] < 26.043957:
                        var153 = -0.06724893
                    else:
                        var153 = -0.0051414887
                else:
                    if input[4] < 8.301448:
                        var153 = 0.02333524
                    else:
                        var153 = -0.06422189
            else:
                if input[2] < 768.4635:
                    if input[4] < 8.236438:
                        var153 = -0.028216515
                    else:
                        var153 = -0.06728862
                else:
                    if input[5] < 1387.4912:
                        var153 = -0.000122115
                    else:
                        var153 = -0.071878776
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var154 = -0.069470696
            else:
                var154 = 0.0001119926
        else:
            var154 = 0.008548968
    else:
        if input[2] < 737.73047:
            if input[2] < 429.77728:
                if input[0] < 25.986551:
                    if input[4] < 7.3376346:
                        var154 = -0.052780237
                    else:
                        var154 = 0.04059353
                else:
                    if input[0] < 37.875954:
                        var154 = 0.07505345
                    else:
                        var154 = -0.04617496
            else:
                if input[4] < 8.151678:
                    if input[4] < 7.293997:
                        var154 = 0.06956202
                    else:
                        var154 = 0.11442667
                else:
                    if input[2] < 721.7867:
                        var154 = 0.09077542
                    else:
                        var154 = 0.03196874
        else:
            if input[2] < 753.20294:
                if input[1] < 58.03831:
                    if input[0] < 26.043957:
                        var154 = -0.06520667
                    else:
                        var154 = -0.0042542256
                else:
                    if input[4] < 8.301448:
                        var154 = 0.02186711
                    else:
                        var154 = -0.062206812
            else:
                if input[2] < 768.4635:
                    if input[4] < 8.236438:
                        var154 = -0.025669018
                    else:
                        var154 = -0.064774446
                else:
                    if input[5] < 1387.4912:
                        var154 = -0.0004400544
                    else:
                        var154 = -0.06946819
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var155 = -0.06734051
            else:
                var155 = 0.00026070746
        else:
            var155 = 0.007499259
    else:
        if input[2] < 737.73047:
            if input[2] < 433.85468:
                if input[5] < 4315.5137:
                    if input[5] < 537.6977:
                        var155 = 0.05298835
                    else:
                        var155 = -0.016428214
                else:
                    if input[3] < 187.8443:
                        var155 = 0.10130415
                    else:
                        var155 = 0.02974915
            else:
                if input[4] < 8.151678:
                    if input[4] < 7.293997:
                        var155 = 0.06647214
                    else:
                        var155 = 0.10348556
                else:
                    if input[2] < 715.4301:
                        var155 = 0.089499354
                    else:
                        var155 = 0.034692097
        else:
            if input[2] < 753.20294:
                if input[1] < 58.03831:
                    if input[0] < 26.043957:
                        var155 = -0.06313028
                    else:
                        var155 = -0.0035653727
                else:
                    if input[4] < 8.301448:
                        var155 = 0.020519773
                    else:
                        var155 = -0.060467124
            else:
                if input[2] < 768.4635:
                    if input[4] < 8.236438:
                        var155 = -0.023545265
                    else:
                        var155 = -0.06267794
                else:
                    if input[5] < 1387.4912:
                        var155 = -0.0006755327
                    else:
                        var155 = -0.06732859
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var156 = -0.06545923
            else:
                var156 = 0.00042535548
        else:
            var156 = 0.006506798
    else:
        if input[2] < 737.73047:
            if input[2] < 433.85468:
                if input[5] < 4315.5137:
                    if input[5] < 537.6977:
                        var156 = 0.050319653
                    else:
                        var156 = -0.0153445555
                else:
                    if input[3] < 187.8443:
                        var156 = 0.09308608
                    else:
                        var156 = 0.027825734
            else:
                if input[4] < 8.151678:
                    if input[4] < 7.293997:
                        var156 = 0.06060916
                    else:
                        var156 = 0.09488884
                else:
                    if input[2] < 721.7867:
                        var156 = 0.07545652
                    else:
                        var156 = 0.026264159
        else:
            if input[2] < 753.20294:
                if input[4] < 8.168125:
                    if input[1] < 54.21738:
                        var156 = -0.054142453
                    else:
                        var156 = 0.03366848
                else:
                    if input[4] < 8.301448:
                        var156 = -0.016982367
                    else:
                        var156 = -0.060807496
            else:
                if input[2] < 768.4635:
                    if input[4] < 8.236438:
                        var156 = -0.021454178
                    else:
                        var156 = -0.060756594
                else:
                    if input[5] < 1387.4912:
                        var156 = -0.0008428159
                    else:
                        var156 = -0.06544014
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var157 = -0.06379612
            else:
                var157 = 0.0006022145
        else:
            var157 = 0.0056543685
    else:
        if input[2] < 739.5616:
            if input[4] < 8.16224:
                if input[2] < 433.85468:
                    if input[5] < 4693.2686:
                        var157 = 0.0066811293
                    else:
                        var157 = 0.08640718
                else:
                    if input[4] < 7.322918:
                        var157 = 0.061472524
                    else:
                        var157 = 0.087880224
            else:
                if input[2] < 721.7867:
                    if input[0] < 21.677387:
                        var157 = 0.00578206
                    else:
                        var157 = 0.07740883
                else:
                    if input[0] < 26.970547:
                        var157 = -0.021442167
                    else:
                        var157 = 0.04707053
        else:
            if input[4] < 8.187523:
                if input[2] < 748.9394:
                    if input[3] < 141.65678:
                        var157 = 0.038366098
                    else:
                        var157 = -0.023697615
                else:
                    if input[4] < 8.092142:
                        var157 = 0.0156798
                    else:
                        var157 = -0.051270932
            else:
                if input[2] < 768.4635:
                    if input[3] < 121.46589:
                        var157 = -0.060759284
                    else:
                        var157 = -0.027557133
                else:
                    if input[5] < 1387.4912:
                        var157 = -0.0009539385
                    else:
                        var157 = -0.063765146
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var158 = -0.062321078
            else:
                var158 = 0.00078657997
        else:
            var158 = 0.0047623017
    else:
        if input[2] < 739.5616:
            if input[4] < 8.16224:
                if input[2] < 433.85468:
                    if input[5] < 4315.5137:
                        var158 = 0.0046246913
                    else:
                        var158 = 0.07615797
                else:
                    if input[4] < 7.322918:
                        var158 = 0.056738447
                    else:
                        var158 = 0.08229112
            else:
                if input[2] < 721.7867:
                    if input[0] < 21.677387:
                        var158 = 0.0051808106
                    else:
                        var158 = 0.07182433
                else:
                    if input[0] < 26.970547:
                        var158 = -0.02046453
                    else:
                        var158 = 0.043784443
        else:
            if input[4] < 8.187523:
                if input[2] < 748.9394:
                    if input[3] < 141.65678:
                        var158 = 0.035807613
                    else:
                        var158 = -0.022198264
                else:
                    if input[4] < 8.092142:
                        var158 = 0.014751214
                    else:
                        var158 = -0.049268987
            else:
                if input[2] < 768.4635:
                    if input[3] < 121.46589:
                        var158 = -0.059001435
                    else:
                        var158 = -0.025541624
                else:
                    if input[5] < 1387.4912:
                        var158 = -0.0010190405
                    else:
                        var158 = -0.062286086
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var159 = -0.06100874
            else:
                var159 = 0.00067193306
        else:
            var159 = 0.004465763
    else:
        if input[2] < 739.5616:
            if input[4] < 8.151678:
                if input[4] < 7.293997:
                    if input[5] < 4693.2686:
                        var159 = 0.018841242
                    else:
                        var159 = 0.07597076
                else:
                    if input[2] < 429.77728:
                        var159 = 0.039642222
                    else:
                        var159 = 0.07770007
            else:
                if input[2] < 730.8562:
                    if input[0] < 21.677387:
                        var159 = -0.008069164
                    else:
                        var159 = 0.059655186
                else:
                    if input[5] < 2698.7034:
                        var159 = 0.046617772
                    else:
                        var159 = -0.04171615
        else:
            if input[4] < 8.187523:
                if input[2] < 748.9394:
                    if input[5] < 1799.6632:
                        var159 = -0.023226587
                    else:
                        var159 = 0.034536865
                else:
                    if input[4] < 8.092142:
                        var159 = 0.014238584
                    else:
                        var159 = -0.0472792
            else:
                if input[2] < 768.4635:
                    if input[3] < 121.46589:
                        var159 = -0.05749423
                    else:
                        var159 = -0.023594033
                else:
                    if input[5] < 1387.4912:
                        var159 = -0.0010466496
                    else:
                        var159 = -0.060973506
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var160 = -0.05984199
            else:
                var160 = 0.00058835885
        else:
            var160 = 0.0042177523
    else:
        if input[2] < 742.155:
            if input[4] < 8.151678:
                if input[4] < 7.293997:
                    if input[5] < 4693.2686:
                        var160 = 0.01738384
                    else:
                        var160 = 0.071774095
                else:
                    if input[2] < 429.77728:
                        var160 = 0.037428018
                    else:
                        var160 = 0.07358688
            else:
                if input[2] < 730.8562:
                    if input[0] < 21.677387:
                        var160 = -0.008367227
                    else:
                        var160 = 0.05538706
                else:
                    if input[3] < 98.00895:
                        var160 = 0.04146106
                    else:
                        var160 = -0.02572007
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[3] < 92.85021:
                        var160 = -0.042587396
                    else:
                        var160 = 0.0020760808
                else:
                    if input[0] < 23.645546:
                        var160 = -0.02678687
                    else:
                        var160 = -0.058877796
            else:
                if input[5] < 1387.4912:
                    var160 = -0.0010439883
                else:
                    var160 = -0.059826892
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var161 = -0.05880285
            else:
                var161 = 0.00053029426
        else:
            var161 = 0.0040097404
    else:
        if input[2] < 739.5616:
            if input[4] < 8.16224:
                if input[2] < 433.85468:
                    if input[5] < 4693.2686:
                        var161 = 0.0037189394
                    else:
                        var161 = 0.069558926
                else:
                    if input[4] < 7.322918:
                        var161 = 0.046538435
                    else:
                        var161 = 0.07058833
            else:
                if input[2] < 721.7867:
                    if input[0] < 21.677387:
                        var161 = 0.0025327755
                    else:
                        var161 = 0.060067315
                else:
                    if input[0] < 26.970547:
                        var161 = -0.020664332
                    else:
                        var161 = 0.03657424
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[1] < 90.64338:
                        var161 = 0.000024847015
                    else:
                        var161 = -0.052972
                else:
                    if input[0] < 23.645546:
                        var161 = -0.027021646
                    else:
                        var161 = -0.0579861
            else:
                if input[5] < 1387.4912:
                    var161 = -0.0010171294
                else:
                    var161 = -0.058785606
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var162 = -0.057875704
            else:
                var162 = 0.0004930265
        else:
            var162 = 0.0038345736
    else:
        if input[2] < 742.155:
            if input[2] < 715.4301:
                if input[4] < 7.3376346:
                    if input[2] < 429.77728:
                        var162 = 0.0022986752
                    else:
                        var162 = 0.04632517
                else:
                    if input[5] < 395.23544:
                        var162 = 0.01953651
                    else:
                        var162 = 0.068856016
            else:
                if input[4] < 8.230444:
                    if input[3] < 155.53893:
                        var162 = 0.047605272
                    else:
                        var162 = -0.0016698539
                else:
                    if input[5] < 2681.302:
                        var162 = 0.027960762
                    else:
                        var162 = -0.05215407
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[3] < 92.85021:
                        var162 = -0.03977083
                    else:
                        var162 = 0.003778568
                else:
                    if input[0] < 23.645546:
                        var162 = -0.023695188
                    else:
                        var162 = -0.05648132
            else:
                if input[5] < 1387.4912:
                    var162 = -0.0009712306
                else:
                    var162 = -0.057856392
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var163 = -0.05704699
            else:
                var163 = 0.00047261114
        else:
            var163 = 0.003686291
    else:
        if input[2] < 742.155:
            if input[2] < 715.4301:
                if input[4] < 7.3376346:
                    if input[2] < 429.77728:
                        var163 = 0.0022182993
                    else:
                        var163 = 0.04335462
                else:
                    if input[1] < 40.452465:
                        var163 = 0.022444336
                    else:
                        var163 = 0.06644948
            else:
                if input[4] < 8.092142:
                    if input[5] < 3616.1387:
                        var163 = 0.068233356
                    else:
                        var163 = 0.013402901
                else:
                    if input[4] < 8.230444:
                        var163 = 0.026382653
                    else:
                        var163 = -0.017506689
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[3] < 92.85021:
                        var163 = -0.03821543
                    else:
                        var163 = 0.0043669124
                else:
                    if input[0] < 23.645546:
                        var163 = -0.021947082
                    else:
                        var163 = -0.055395093
            else:
                if input[5] < 1387.4912:
                    var163 = -0.00091068196
                else:
                    var163 = -0.057025637
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var164 = -0.05630491
            else:
                var164 = 0.00046571755
        else:
            var164 = 0.0035599086
    else:
        if input[2] < 742.155:
            if input[2] < 715.4301:
                if input[4] < 7.3376346:
                    if input[2] < 462.86743:
                        var164 = 0.01856792
                    else:
                        var164 = 0.064778626
                else:
                    if input[5] < 395.23544:
                        var164 = 0.014261641
                    else:
                        var164 = 0.06431251
            else:
                if input[4] < 8.092142:
                    if input[5] < 3616.1387:
                        var164 = 0.06625309
                    else:
                        var164 = 0.011916387
                else:
                    if input[0] < 21.366615:
                        var164 = -0.031230832
                    else:
                        var164 = 0.022629267
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[1] < 90.64338:
                        var164 = -0.000043893688
                    else:
                        var164 = -0.05825138
                else:
                    if input[0] < 23.645546:
                        var164 = -0.020662822
                    else:
                        var164 = -0.054318964
            else:
                if input[5] < 1387.4912:
                    var164 = -0.0008389903
                else:
                    var164 = -0.056281444
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var165 = -0.055639137
            else:
                var165 = 0.00046951935
        else:
            var165 = 0.0034512344
    else:
        if input[2] < 742.155:
            if input[4] < 8.151678:
                if input[4] < 7.3376346:
                    if input[2] < 462.86743:
                        var165 = 0.01719053
                    else:
                        var165 = 0.062419374
                else:
                    if input[2] < 737.73047:
                        var165 = 0.06184808
                    else:
                        var165 = 0.01565832
            else:
                if input[0] < 21.95693:
                    if input[0] < 20.804243:
                        var165 = 0.012944631
                    else:
                        var165 = -0.053104933
                else:
                    if input[4] < 8.296122:
                        var165 = 0.03502224
                    else:
                        var165 = -0.035502505
        else:
            if input[2] < 768.4635:
                if input[4] < 8.265591:
                    if input[1] < 90.64338:
                        var165 = 0.00072884397
                    else:
                        var165 = -0.05699786
                else:
                    if input[0] < 23.645546:
                        var165 = -0.019073397
                    else:
                        var165 = -0.053418066
            else:
                if input[5] < 1387.4912:
                    var165 = -0.0007592186
                else:
                    var165 = -0.05561346
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var166 = -0.055042136
            else:
                var166 = 0.00074156985
        else:
            var166 = 0.0029725346
    else:
        if input[2] < 744.1235:
            if input[4] < 8.151678:
                if input[4] < 7.3523836:
                    if input[2] < 439.61963:
                        var166 = 0.009033951
                    else:
                        var166 = 0.043489434
                else:
                    if input[2] < 715.4301:
                        var166 = 0.061624687
                    else:
                        var166 = 0.042424098
            else:
                if input[2] < 730.8562:
                    if input[0] < 21.677387:
                        var166 = -0.015934488
                    else:
                        var166 = 0.039258655
                else:
                    if input[3] < 98.00895:
                        var166 = 0.023090329
                    else:
                        var166 = -0.027262285
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[1] < 81.32996:
                        var166 = 0.060487654
                    else:
                        var166 = -0.01408633
                else:
                    if input[3] < 104.90332:
                        var166 = -0.04827581
                    else:
                        var166 = -0.012959062
            else:
                if input[5] < 1387.4912:
                    var166 = -0.0006738969
                else:
                    var166 = -0.05501262
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var167 = -0.054502923
            else:
                var167 = 0.00074375654
        else:
            var167 = 0.0029096273
    else:
        if input[2] < 744.1235:
            if input[4] < 8.151678:
                if input[4] < 7.3523836:
                    if input[0] < 25.986551:
                        var167 = 0.00413864
                    else:
                        var167 = 0.038612586
                else:
                    if input[2] < 715.4301:
                        var167 = 0.060247745
                    else:
                        var167 = 0.040454347
            else:
                if input[0] < 21.95693:
                    if input[4] < 8.241077:
                        var167 = -0.043848883
                    else:
                        var167 = 0.047634706
                else:
                    if input[4] < 8.241077:
                        var167 = 0.03260595
                    else:
                        var167 = -0.018334705
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[5] < 3686.298:
                        var167 = 0.059040714
                    else:
                        var167 = -0.012305896
                else:
                    if input[3] < 104.90332:
                        var167 = -0.04692561
                    else:
                        var167 = -0.011813483
            else:
                if input[5] < 1387.4912:
                    var167 = -0.0005851361
                else:
                    var167 = -0.054470982
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var168 = -0.054017942
            else:
                var168 = 0.0010134944
        else:
            var168 = 0.0025374051
    else:
        if input[2] < 744.1235:
            if input[4] < 8.151678:
                if input[4] < 7.3523836:
                    if input[2] < 462.86743:
                        var168 = 0.014798273
                    else:
                        var168 = 0.057877835
                else:
                    if input[2] < 715.4301:
                        var168 = 0.059035577
                    else:
                        var168 = 0.038548402
            else:
                if input[0] < 21.95693:
                    if input[4] < 8.241077:
                        var168 = -0.04273243
                    else:
                        var168 = 0.046095505
                else:
                    if input[4] < 8.241077:
                        var168 = 0.030844674
                    else:
                        var168 = -0.01728659
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[1] < 81.32996:
                        var168 = 0.0551201
                    else:
                        var168 = -0.015458124
                else:
                    if input[3] < 104.90332:
                        var168 = -0.045669947
                    else:
                        var168 = -0.01039061
            else:
                if input[5] < 1387.4912:
                    var168 = -0.0004946702
                else:
                    var168 = -0.05398152
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var169 = -0.05357917
            else:
                var169 = 0.0012792073
        else:
            var169 = 0.002197034
    else:
        if input[2] < 742.155:
            if input[2] < 715.4301:
                if input[4] < 7.3523836:
                    if input[5] < 4693.2686:
                        var169 = 0.014102958
                    else:
                        var169 = 0.05918027
                else:
                    if input[5] < 395.23544:
                        var169 = 0.002831838
                    else:
                        var169 = 0.057459015
            else:
                if input[4] < 8.092142:
                    if input[5] < 3616.1387:
                        var169 = 0.058948345
                    else:
                        var169 = 0.0013623416
                else:
                    if input[1] < 45.71353:
                        var169 = -0.03170726
                    else:
                        var169 = 0.016154973
        else:
            if input[2] < 768.4635:
                if input[4] < 8.301448:
                    if input[1] < 90.64338:
                        var169 = 0.0017623472
                    else:
                        var169 = -0.054240633
                else:
                    var169 = -0.050994094
            else:
                if input[5] < 1387.4912:
                    var169 = -0.0004039459
                else:
                    var169 = -0.053538065
    if input[2] < 407.72763:
        if input[4] < 7.322918:
            if input[5] < 4394.467:
                var170 = -0.053179163
            else:
                var170 = 0.0012605498
        else:
            var170 = 0.0021846942
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[4] < 7.3523836:
                    if input[2] < 462.86743:
                        var170 = 0.012534203
                    else:
                        var170 = 0.05540684
                else:
                    if input[5] < 395.23544:
                        var170 = 0.0019404099
                    else:
                        var170 = 0.056431383
            else:
                if input[4] < 8.230444:
                    if input[3] < 155.53893:
                        var170 = 0.030969381
                    else:
                        var170 = -0.016698215
                else:
                    if input[5] < 2681.302:
                        var170 = 0.016939644
                    else:
                        var170 = -0.049254857
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[3] < 168.97972:
                        var170 = 0.0030355453
                    else:
                        var170 = 0.074243456
                else:
                    if input[0] < 28.530838:
                        var170 = -0.010855321
                    else:
                        var170 = -0.047384664
            else:
                if input[5] < 1387.4912:
                    var170 = -0.00031413222
                else:
                    var170 = -0.053135123
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var171 = 0.009887596
        else:
            var171 = -0.052912224
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var171 = 0.010047891
                    else:
                        var171 = 0.05723476
                else:
                    if input[4] < 8.151678:
                        var171 = 0.056345712
                    else:
                        var171 = 0.03536276
            else:
                if input[4] < 8.230444:
                    if input[3] < 155.53893:
                        var171 = 0.02921694
                    else:
                        var171 = -0.016048465
                else:
                    if input[5] < 2681.302:
                        var171 = 0.016116789
                    else:
                        var171 = -0.047869343
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[3] < 168.97972:
                        var171 = 0.0029955197
                    else:
                        var171 = 0.07152918
                else:
                    if input[5] < 3616.1387:
                        var171 = -0.036225114
                    else:
                        var171 = -0.0014753917
            else:
                if input[5] < 1387.4912:
                    var171 = -0.000226169
                else:
                    var171 = -0.052767795
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var172 = 0.010487251
        else:
            var172 = -0.052581307
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var172 = 0.009312962
                    else:
                        var172 = 0.055770513
                else:
                    if input[4] < 8.151678:
                        var172 = 0.05558927
                    else:
                        var172 = 0.033546057
            else:
                if input[4] < 8.206008:
                    if input[3] < 155.53893:
                        var172 = 0.031646006
                    else:
                        var172 = -0.01676158
                else:
                    if input[5] < 2681.302:
                        var172 = 0.030133141
                    else:
                        var172 = -0.038636807
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[3] < 168.97972:
                        var172 = 0.0027883002
                    else:
                        var172 = 0.06870905
                else:
                    if input[0] < 28.530838:
                        var172 = -0.008202232
                    else:
                        var172 = -0.045624174
            else:
                if input[5] < 1387.4912:
                    var172 = -0.00014080417
                else:
                    var172 = -0.05243174
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var173 = 0.010394942
        else:
            var173 = -0.052277524
    else:
        if input[2] < 742.155:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var173 = 0.008690853
                    else:
                        var173 = 0.05449388
                else:
                    if input[4] < 8.151678:
                        var173 = 0.054907728
                    else:
                        var173 = 0.03173953
            else:
                if input[4] < 8.092142:
                    if input[5] < 3616.1387:
                        var173 = 0.055691004
                    else:
                        var173 = -0.0015498304
                else:
                    if input[0] < 21.366615:
                        var173 = -0.032122593
                    else:
                        var173 = 0.013121227
        else:
            if input[2] < 768.4635:
                if input[4] < 8.301448:
                    if input[3] < 92.85021:
                        var173 = -0.031470045
                    else:
                        var173 = 0.009000175
                else:
                    var173 = -0.048314884
            else:
                if input[5] < 1387.4912:
                    var173 = -0.000058651054
                else:
                    var173 = -0.05212302
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var174 = 0.010942945
        else:
            var174 = -0.051998537
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var174 = 0.008069528
                    else:
                        var174 = 0.053207476
                else:
                    if input[4] < 8.151678:
                        var174 = 0.054287612
                    else:
                        var174 = 0.030005783
            else:
                if input[4] < 8.206008:
                    if input[3] < 155.53893:
                        var174 = 0.028932905
                    else:
                        var174 = -0.016358707
                else:
                    if input[5] < 2681.302:
                        var174 = 0.028933791
                    else:
                        var174 = -0.036642335
        else:
            if input[2] < 768.4635:
                if input[4] < 8.112143:
                    if input[3] < 168.97972:
                        var174 = 0.0022395675
                    else:
                        var174 = 0.065346204
                else:
                    if input[5] < 3616.1387:
                        var174 = -0.033288594
                    else:
                        var174 = 0.002208119
            else:
                if input[5] < 1387.4912:
                    var174 = 0.000019879082
                else:
                    var174 = -0.051838107
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var175 = 0.011462277
        else:
            var175 = -0.051740717
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var175 = 0.0074857348
                    else:
                        var175 = 0.051999416
                else:
                    if input[4] < 8.151678:
                        var175 = 0.05372491
                    else:
                        var175 = 0.028387917
            else:
                if input[4] < 8.230444:
                    if input[3] < 155.53893:
                        var175 = 0.024141721
                    else:
                        var175 = -0.01420091
                else:
                    if input[5] < 1747.7112:
                        var175 = 0.03954002
                    else:
                        var175 = -0.03131524
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.301448:
                        var175 = 0.009210245
                    else:
                        var175 = -0.044160903
                else:
                    if input[4] < 8.12684:
                        var175 = 0.010319702
                    else:
                        var175 = -0.043080565
            else:
                if input[5] < 1387.4912:
                    var175 = 0.000094419636
                else:
                    var175 = -0.0515738
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var176 = 0.011953569
        else:
            var176 = -0.051501196
    else:
        if input[2] < 746.90137:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var176 = 0.0067448835
                    else:
                        var176 = 0.050938886
                else:
                    if input[4] < 8.151678:
                        var176 = 0.053209182
                    else:
                        var176 = 0.02683946
            else:
                if input[4] < 8.206008:
                    if input[3] < 155.53893:
                        var176 = 0.026315436
                    else:
                        var176 = -0.014838618
                else:
                    if input[5] < 2681.302:
                        var176 = 0.028125942
                    else:
                        var176 = -0.034515448
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[3] < 172.44543:
                        var176 = 0.01042741
                    else:
                        var176 = -0.038264062
                else:
                    if input[4] < 8.12684:
                        var176 = 0.009347204
                    else:
                        var176 = -0.04223403
            else:
                if input[5] < 1387.4912:
                    var176 = 0.00016473366
                else:
                    var176 = -0.051327165
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var177 = 0.012417485
        else:
            var177 = -0.051277347
    else:
        if input[2] < 737.73047:
            if input[4] < 7.3376346:
                if input[5] < 4693.2686:
                    if input[3] < 133.33838:
                        var177 = 0.013591726
                    else:
                        var177 = -0.060139406
                else:
                    var177 = 0.04875887
            else:
                if input[4] < 8.092142:
                    if input[3] < 13.104021:
                        var177 = -0.0032792576
                    else:
                        var177 = 0.05192386
                else:
                    if input[2] < 715.4301:
                        var177 = 0.03719582
                    else:
                        var177 = 0.009003886
        else:
            if input[2] < 768.4635:
                if input[4] < 8.301448:
                    if input[1] < 93.82345:
                        var177 = 0.005395409
                    else:
                        var177 = -0.047472797
                else:
                    var177 = -0.046678647
            else:
                if input[5] < 1387.4912:
                    var177 = 0.00023067101
                else:
                    var177 = -0.051095527
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var178 = 0.012854728
        else:
            var178 = -0.051066726
    else:
        if input[2] < 753.20294:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var178 = 0.005311873
                    else:
                        var178 = 0.048952367
                else:
                    if input[4] < 8.151678:
                        var178 = 0.052303124
                    else:
                        var178 = 0.023477407
            else:
                if input[4] < 8.081833:
                    if input[5] < 3686.298:
                        var178 = 0.04923927
                    else:
                        var178 = -0.014499842
                else:
                    if input[0] < 21.366615:
                        var178 = -0.029284328
                    else:
                        var178 = 0.008287004
        else:
            if input[4] < 8.236438:
                if input[1] < 53.759136:
                    if input[3] < 138.7908:
                        var178 = -0.0063572684
                    else:
                        var178 = 0.08920139
                else:
                    if input[4] < 8.092142:
                        var178 = 0.02179914
                    else:
                        var178 = -0.03798288
            else:
                if input[0] < 20.484303:
                    var178 = 0.01327353
                else:
                    if input[5] < 1600.5679:
                        var178 = 0.0043513207
                    else:
                        var178 = -0.05117802
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var179 = 0.012366364
        else:
            var179 = -0.05085972
    else:
        if input[2] < 753.20294:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var179 = 0.004901301
                    else:
                        var179 = 0.04801886
                else:
                    if input[4] < 8.151678:
                        var179 = 0.051885374
                    else:
                        var179 = 0.022126548
            else:
                if input[4] < 8.081833:
                    if input[5] < 3686.298:
                        var179 = 0.048241567
                    else:
                        var179 = -0.013960125
                else:
                    if input[1] < 58.03831:
                        var179 = -0.0119579835
                    else:
                        var179 = 0.0125213405
        else:
            if input[2] < 768.4635:
                if input[1] < 53.759136:
                    if input[4] < 8.236438:
                        var179 = 0.06525815
                    else:
                        var179 = -0.037850212
                else:
                    if input[0] < 20.484303:
                        var179 = 0.04403694
                    else:
                        var179 = -0.034860373
            else:
                if input[5] < 1387.4912:
                    var179 = 0.00063468475
                else:
                    var179 = -0.050672956
    if input[2] < 399.29376:
        if input[1] < 40.452465:
            var180 = 0.012491231
        else:
            var180 = -0.050664067
    else:
        if input[2] < 756.0391:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[1] < 43.66826:
                        var180 = -0.046794254
                    else:
                        var180 = 0.013236894
                else:
                    if input[4] < 8.151678:
                        var180 = 0.051495474
                    else:
                        var180 = 0.020837637
            else:
                if input[3] < 152.17412:
                    if input[4] < 8.136787:
                        var180 = 0.039123114
                    else:
                        var180 = 0.0029444725
                else:
                    if input[1] < 47.42564:
                        var180 = -0.06459594
                    else:
                        var180 = -0.0025829708
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var180 = 0.03597243
                    else:
                        var180 = -0.030018756
                else:
                    var180 = -0.0471761
            else:
                if input[5] < 1387.4912:
                    var180 = 0.0006730074
                else:
                    var180 = -0.05047194
    if input[2] < 399.29376:
        if input[1] < 40.763638:
            var181 = 0.0063737496
        else:
            var181 = -0.05047328
    else:
        if input[2] < 756.0391:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var181 = 0.0036896348
                    else:
                        var181 = 0.04657625
                else:
                    if input[4] < 8.151678:
                        var181 = 0.051122587
                    else:
                        var181 = 0.019510072
            else:
                if input[3] < 152.17412:
                    if input[4] < 8.136787:
                        var181 = 0.037808333
                    else:
                        var181 = 0.0030137224
                else:
                    if input[1] < 47.42564:
                        var181 = -0.0628518
                    else:
                        var181 = -0.002479839
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var181 = 0.033654835
                    else:
                        var181 = -0.02909785
                else:
                    var181 = -0.046666596
            else:
                if input[5] < 1387.4912:
                    var181 = 0.0007075754
                else:
                    var181 = -0.05027702
    if input[2] < 399.29376:
        if input[1] < 40.763638:
            var182 = 0.006806468
        else:
            var182 = -0.05028686
    else:
        if input[2] < 737.73047:
            if input[4] < 7.3376346:
                if input[5] < 4693.2686:
                    if input[3] < 133.33838:
                        var182 = 0.009994356
                    else:
                        var182 = -0.056471985
                else:
                    var182 = 0.04409293
            else:
                if input[4] < 8.092142:
                    if input[2] < 433.85468:
                        var182 = 0.011787155
                    else:
                        var182 = 0.050386596
                else:
                    if input[0] < 21.81601:
                        var182 = -0.017994685
                    else:
                        var182 = 0.018936018
        else:
            if input[2] < 768.4635:
                if input[1] < 93.82345:
                    if input[3] < 172.44543:
                        var182 = 0.0055074054
                    else:
                        var182 = -0.03897178
                else:
                    if input[4] < 8.12684:
                        var182 = -0.00063495757
                    else:
                        var182 = -0.05453191
            else:
                if input[5] < 1387.4912:
                    var182 = 0.00073847384
                else:
                    var182 = -0.050086286
    if input[2] < 399.29376:
        if input[1] < 40.763638:
            var183 = 0.0072159427
        else:
            var183 = -0.05010384
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[1] < 56.845116:
                        var183 = -0.019455772
                    else:
                        var183 = 0.015321624
                else:
                    if input[4] < 8.151678:
                        var183 = 0.050439425
                    else:
                        var183 = 0.017345076
            else:
                if input[4] < 8.301448:
                    if input[1] < 90.64338:
                        var183 = 0.010398793
                    else:
                        var183 = -0.019528048
                else:
                    if input[4] < 8.378964:
                        var183 = -0.04545102
                    else:
                        var183 = 0.011281405
        else:
            if input[5] < 1387.4912:
                var183 = 0.00076579466
            else:
                var183 = -0.049897876
    if input[2] < 380.03854:
        var184 = -0.04983089
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var184 = -0.011934662
                    else:
                        var184 = 0.017758882
                else:
                    if input[4] < 8.151678:
                        var184 = 0.050094076
                    else:
                        var184 = 0.016238576
            else:
                if input[4] < 8.301448:
                    if input[1] < 90.64338:
                        var184 = 0.009815785
                    else:
                        var184 = -0.01855014
                else:
                    if input[0] < 20.865282:
                        var184 = 0.01290129
                    else:
                        var184 = -0.044549983
        else:
            if input[5] < 1387.4912:
                var184 = 0.00078964356
            else:
                var184 = -0.04971003
    if input[2] < 380.03854:
        var185 = -0.04965351
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var185 = -0.011113354
                    else:
                        var185 = 0.016707743
                else:
                    if input[4] < 8.151678:
                        var185 = 0.04975522
                    else:
                        var185 = 0.015435393
            else:
                if input[4] < 8.301448:
                    if input[1] < 90.64338:
                        var185 = 0.009329266
                    else:
                        var185 = -0.017535267
                else:
                    if input[4] < 8.378964:
                        var185 = -0.04420258
                    else:
                        var185 = 0.012810655
        else:
            if input[5] < 1387.4912:
                var185 = 0.00081019144
            else:
                var185 = -0.049521264
    if input[4] < 7.1246004:
        var186 = -0.049281217
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var186 = -0.011186973
                    else:
                        var186 = 0.017094577
                else:
                    if input[2] < 739.5616:
                        var186 = 0.04891497
                    else:
                        var186 = 0.0023654152
            else:
                if input[0] < 21.81601:
                    if input[4] < 8.12684:
                        var186 = 0.047393564
                    else:
                        var186 = -0.03139462
                else:
                    if input[4] < 8.301448:
                        var186 = 0.009528717
                    else:
                        var186 = -0.04046243
        else:
            if input[5] < 1387.4912:
                var186 = 0.00082758407
            else:
                var186 = -0.04932939
    if input[2] < 380.03854:
        var187 = -0.04929233
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var187 = 0.0006492375
                    else:
                        var187 = 0.042827997
                else:
                    if input[2] < 691.64557:
                        var187 = 0.05062286
                    else:
                        var187 = 0.021043552
            else:
                if input[4] < 8.092142:
                    if input[5] < 3686.298:
                        var187 = 0.045306418
                    else:
                        var187 = -0.027310789
                else:
                    if input[0] < 36.260155:
                        var187 = 0.0028140363
                    else:
                        var187 = -0.025301134
        else:
            if input[5] < 1387.4912:
                var187 = 0.0008419533
            else:
                var187 = -0.049133264
    if input[4] < 7.1246004:
        var188 = -0.04886611
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var188 = -0.010229758
                    else:
                        var188 = 0.015641479
                else:
                    if input[2] < 739.5616:
                        var188 = 0.048102092
                    else:
                        var188 = 0.0016059786
            else:
                if input[0] < 21.81601:
                    if input[4] < 8.254773:
                        var188 = -0.03296357
                    else:
                        var188 = 0.039583724
                else:
                    if input[4] < 8.301448:
                        var188 = 0.009008696
                    else:
                        var188 = -0.03988974
        else:
            if input[5] < 1387.4912:
                var188 = 0.0008535096
            else:
                var188 = -0.048930716
    if input[2] < 380.03854:
        var189 = -0.04891404
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 36.260155:
                        var189 = 0.009710328
                    else:
                        var189 = -0.024798311
                else:
                    if input[2] < 729.3266:
                        var189 = 0.050375797
                    else:
                        var189 = 0.007928871
            else:
                if input[3] < 43.021126:
                    var189 = 0.04927519
                else:
                    if input[5] < 1708.4924:
                        var189 = -0.026259711
                    else:
                        var189 = 0.0047099325
        else:
            if input[5] < 1387.4912:
                var189 = 0.0008623909
            else:
                var189 = -0.048720386
    if input[4] < 7.1246004:
        var190 = -0.048400894
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var190 = -0.009773677
                    else:
                        var190 = 0.014427676
                else:
                    if input[2] < 729.3266:
                        var190 = 0.05018569
                    else:
                        var190 = 0.007668275
            else:
                if input[3] < 43.021126:
                    var190 = 0.04756934
                else:
                    if input[5] < 3346.2974:
                        var190 = -0.004622861
                    else:
                        var190 = 0.011708965
        else:
            if input[5] < 1387.4912:
                var190 = 0.0008687127
            else:
                var190 = -0.048500653
    if input[4] < 7.0906034:
        var191 = -0.048652302
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var191 = 0.00020895067
                    else:
                        var191 = 0.0403693
                else:
                    if input[2] < 691.64557:
                        var191 = 0.04982084
                    else:
                        var191 = 0.017542249
            else:
                if input[4] < 8.301448:
                    if input[3] < 152.17412:
                        var191 = 0.009426723
                    else:
                        var191 = -0.009489163
                else:
                    if input[3] < 170.29514:
                        var191 = -0.042371497
                    else:
                        var191 = 0.013006066
        else:
            if input[5] < 1387.4912:
                var191 = 0.00087275606
            else:
                var191 = -0.0482699
    if input[2] < 380.03854:
        var192 = -0.048281323
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 36.260155:
                        var192 = 0.008714019
                    else:
                        var192 = -0.023882559
                else:
                    if input[2] < 729.3266:
                        var192 = 0.049824238
                    else:
                        var192 = 0.0066544535
            else:
                if input[3] < 43.021126:
                    var192 = 0.045939293
                else:
                    if input[5] < 3346.2974:
                        var192 = -0.004936117
                    else:
                        var192 = 0.011340634
        else:
            if input[5] < 1387.4912:
                var192 = 0.00087440293
            else:
                var192 = -0.04802653
    var193 = var152 + var153 + var154 + var155 + var156 + var157 + var158 + var159 + var160 + var161 + var162 + var163 + var164 + var165 + var166 + var167 + var168 + var169 + var170 + var171 + var172 + var173 + var174 + var175 + var176 + var177 + var178 + var179 + var180 + var181 + var182 + var183 + var184 + var185 + var186 + var187 + var188 + var189 + var190 + var191 + var192
    if input[4] < 7.0906034:
        var194 = -0.048207384
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var194 = -0.009800582
                    else:
                        var194 = 0.013140214
                else:
                    if input[2] < 729.3266:
                        var194 = 0.04963013
                    else:
                        var194 = 0.0062586255
            else:
                if input[4] < 8.301448:
                    if input[3] < 173.21967:
                        var194 = 0.0072072656
                    else:
                        var194 = -0.017803056
                else:
                    if input[2] < 733.0016:
                        var194 = 0.015580745
                    else:
                        var194 = -0.04112449
        else:
            if input[0] < 22.122957:
                if input[0] < 21.55322:
                    var194 = -0.025417248
                else:
                    var194 = 0.019328816
            else:
                var194 = -0.048779137
    if input[4] < 7.0906034:
        var195 = -0.047951374
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var195 = -0.009485598
                    else:
                        var195 = 0.012520094
                else:
                    if input[2] < 729.3266:
                        var195 = 0.049433123
                    else:
                        var195 = 0.005773163
            else:
                if input[5] < 3346.2974:
                    if input[5] < 2698.7034:
                        var195 = 0.009819833
                    else:
                        var195 = -0.028030083
                else:
                    if input[3] < 152.17412:
                        var195 = 0.036379457
                    else:
                        var195 = -0.0055669597
        else:
            if input[0] < 22.122957:
                var195 = -0.0029078543
            else:
                var195 = -0.04852793
    if input[4] < 7.0906034:
        var196 = -0.047680445
    else:
        if input[2] < 768.4635:
            if input[2] < 715.4301:
                if input[2] < 462.86743:
                    if input[4] < 7.293997:
                        var196 = -0.00593267
                    else:
                        var196 = 0.015401586
                else:
                    if input[2] < 691.64557:
                        var196 = 0.04902367
                    else:
                        var196 = 0.014595339
            else:
                if input[1] < 90.64338:
                    if input[1] < 80.01135:
                        var196 = -0.00045574768
                    else:
                        var196 = 0.026231522
                else:
                    if input[2] < 742.155:
                        var196 = -0.00045302883
                    else:
                        var196 = -0.047754515
        else:
            if input[0] < 22.122957:
                var196 = -0.0016517146
            else:
                var196 = -0.04826053
    if input[4] < 7.0906034:
        var197 = -0.04739314
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 25.636688:
                        var197 = -0.009446471
                    else:
                        var197 = 0.011794748
                else:
                    if input[2] < 729.3266:
                        var197 = 0.04906315
                    else:
                        var197 = 0.0051044924
            else:
                if input[5] < 3346.2974:
                    if input[5] < 2698.7034:
                        var197 = 0.009034435
                    else:
                        var197 = -0.02705785
                else:
                    if input[3] < 152.17412:
                        var197 = 0.03443128
                    else:
                        var197 = -0.0052055577
        else:
            if input[0] < 22.122957:
                var197 = -0.00044507463
            else:
                var197 = -0.04797598
    if input[4] < 7.1246004:
        var198 = -0.04647721
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[4] < 7.3822474:
                    if input[0] < 25.636688:
                        var198 = -0.009194455
                    else:
                        var198 = 0.011031604
                else:
                    if input[2] < 739.5616:
                        var198 = 0.042853754
                    else:
                        var198 = -0.0005969062
            else:
                if input[5] < 3636.057:
                    if input[2] < 750.9746:
                        var198 = 0.002196309
                    else:
                        var198 = -0.03452107
                else:
                    if input[5] < 3955.953:
                        var198 = 0.041175015
                    else:
                        var198 = -0.0036115944
        else:
            if input[0] < 22.122957:
                var198 = 0.0007107782
            else:
                var198 = -0.047673088
    if input[4] < 7.0906034:
        var199 = -0.04676791
    else:
        if input[2] < 768.4635:
            if input[2] < 700.4231:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var199 = -0.00046211682
                    else:
                        var199 = 0.03643257
                else:
                    if input[4] < 8.151678:
                        var199 = 0.048345864
                    else:
                        var199 = 0.013556363
            else:
                if input[2] < 703.2164:
                    if input[5] < 2748.8748:
                        var199 = -0.005045582
                    else:
                        var199 = -0.061032355
                else:
                    if input[2] < 715.4301:
                        var199 = 0.03217913
                    else:
                        var199 = 0.0017779463
        else:
            if input[0] < 22.122957:
                var199 = 0.0018146922
            else:
                var199 = -0.047350794
    if input[2] < 380.03854:
        var200 = -0.046310615
    else:
        if input[2] < 768.4635:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[0] < 36.260155:
                        var200 = 0.0070207203
                    else:
                        var200 = -0.02259087
                else:
                    if input[2] < 729.3266:
                        var200 = 0.04846047
                    else:
                        var200 = 0.0036228504
            else:
                if input[1] < 47.42564:
                    if input[3] < 152.17412:
                        var200 = -0.001125452
                    else:
                        var200 = -0.05679009
                else:
                    if input[1] < 54.039787:
                        var200 = 0.027329251
                    else:
                        var200 = 0.0006879771
        else:
            if input[0] < 22.122957:
                var200 = 0.002866136
            else:
                var200 = -0.047008086
    if input[4] < 7.0906034:
        var201 = -0.046072472
    else:
        if input[4] < 8.324405:
            if input[2] < 700.4231:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var201 = -0.00045328515
                    else:
                        var201 = 0.035295464
                else:
                    if input[4] < 8.151678:
                        var201 = 0.047858864
                    else:
                        var201 = 0.012440524
            else:
                if input[2] < 703.2164:
                    if input[5] < 2913.364:
                        var201 = -0.0031826876
                    else:
                        var201 = -0.063828096
                else:
                    if input[0] < 29.823307:
                        var201 = 0.007971334
                    else:
                        var201 = -0.00866266
        else:
            if input[2] < 733.0016:
                var201 = 0.013747665
            else:
                var201 = -0.046446286
    if input[4] < 7.0906034:
        var202 = -0.04568817
    else:
        if input[2] < 768.4635:
            if input[2] < 730.8562:
                if input[4] < 7.293997:
                    if input[1] < 97.78946:
                        var202 = -0.008672575
                    else:
                        var202 = 0.034458593
                else:
                    if input[2] < 700.4231:
                        var202 = 0.030484665
                    else:
                        var202 = 0.007750409
            else:
                if input[3] < 172.44543:
                    if input[3] < 168.97972:
                        var202 = -0.0006789672
                    else:
                        var202 = 0.05564032
                else:
                    if input[4] < 8.12684:
                        var202 = 0.031767838
                    else:
                        var202 = -0.05150496
        else:
            if input[0] < 22.122957:
                var202 = 0.0054975217
            else:
                var202 = -0.0463306
    if input[4] < 7.0906034:
        var203 = -0.045270756
    else:
        if input[4] < 8.324405:
            if input[4] < 8.065835:
                if input[2] < 462.86743:
                    if input[5] < 4737.7285:
                        var203 = -0.00079769373
                    else:
                        var203 = 0.034222707
                else:
                    if input[2] < 729.3266:
                        var203 = 0.047806975
                    else:
                        var203 = 0.0023649207
            else:
                if input[5] < 1556.7986:
                    if input[4] < 8.241077:
                        var203 = 0.0039307447
                    else:
                        var203 = 0.06852593
                else:
                    if input[5] < 1708.4924:
                        var203 = -0.048348274
                    else:
                        var203 = 0.0027096218
        else:
            if input[2] < 733.0016:
                var203 = 0.01309654
            else:
                var203 = -0.045726392
    if input[4] < 7.0906034:
        var204 = -0.04483656
    else:
        if input[4] < 8.324405:
            if input[5] < 2698.7034:
                if input[1] < 58.03831:
                    if input[2] < 726.6149:
                        var204 = 0.008307438
                    else:
                        var204 = -0.039772224
                else:
                    if input[3] < 80.19552:
                        var204 = 0.009860517
                    else:
                        var204 = 0.044900544
            else:
                if input[3] < 120.56106:
                    if input[1] < 55.418133:
                        var204 = 0.028867086
                    else:
                        var204 = -0.04335095
                else:
                    if input[0] < 23.221859:
                        var204 = -0.013760309
                    else:
                        var204 = 0.017898088
        else:
            if input[2] < 733.0016:
                var204 = 0.012566979
            else:
                var204 = -0.045329373
    if input[2] < 380.03854:
        var205 = -0.044277277
    else:
        if input[4] < 8.324405:
            if input[2] < 737.73047:
                if input[1] < 41.845177:
                    if input[1] < 40.452465:
                        var205 = 0.017565085
                    else:
                        var205 = -0.036177512
                else:
                    if input[2] < 429.77728:
                        var205 = -0.0077782273
                    else:
                        var205 = 0.01745007
            else:
                if input[1] < 93.82345:
                    if input[1] < 80.92803:
                        var205 = -0.0070289667
                    else:
                        var205 = 0.024431754
                else:
                    if input[4] < 8.12684:
                        var205 = 0.00079604145
                    else:
                        var205 = -0.047735374
        else:
            if input[2] < 733.0016:
                var205 = 0.01269348
            else:
                var205 = -0.044912823
    if input[0] < 20.11864:
        var206 = -0.045056533
    else:
        if input[4] < 8.324405:
            if input[2] < 429.77728:
                if input[0] < 25.986551:
                    if input[0] < 21.101826:
                        var206 = 0.011067003
                    else:
                        var206 = -0.041996453
                else:
                    if input[0] < 37.875954:
                        var206 = 0.011691942
                    else:
                        var206 = -0.035487376
            else:
                if input[2] < 700.4231:
                    if input[4] < 7.3523836:
                        var206 = 0.00833869
                    else:
                        var206 = 0.04298735
                else:
                    if input[2] < 703.2164:
                        var206 = -0.041956596
                    else:
                        var206 = 0.0031888038
        else:
            if input[2] < 733.0016:
                var206 = 0.012388869
            else:
                var206 = -0.044456318
    if input[0] < 20.11864:
        var207 = -0.044399202
    else:
        if input[4] < 8.324405:
            if input[5] < 4737.7285:
                if input[5] < 3955.953:
                    if input[5] < 3930.5964:
                        var207 = 0.004940763
                    else:
                        var207 = 0.08208432
                else:
                    if input[2] < 733.0016:
                        var207 = 0.005543064
                    else:
                        var207 = -0.052580196
            else:
                if input[4] < 8.236438:
                    if input[5] < 4948.595:
                        var207 = 0.06659456
                    else:
                        var207 = 0.015084073
                else:
                    var207 = -0.04012708
        else:
            if input[2] < 733.0016:
                var207 = 0.012094804
            else:
                var207 = -0.043995783
    if input[0] < 20.11864:
        var208 = -0.043684583
    else:
        if input[4] < 8.324405:
            if input[5] < 4798.541:
                if input[5] < 3955.953:
                    if input[5] < 3930.5964:
                        var208 = 0.004613582
                    else:
                        var208 = 0.077899806
                else:
                    if input[2] < 733.0016:
                        var208 = 0.0064770556
                    else:
                        var208 = -0.043587416
            else:
                if input[4] < 8.230444:
                    if input[0] < 26.55467:
                        var208 = -0.007464004
                    else:
                        var208 = 0.051922526
                else:
                    var208 = -0.04046825
        else:
            if input[2] < 733.0016:
                var208 = 0.012080649
            else:
                var208 = -0.043481242
    if input[0] < 20.11864:
        var209 = -0.042926203
    else:
        if input[4] < 8.324405:
            if input[0] < 36.260155:
                if input[5] < 2698.7034:
                    if input[1] < 58.03831:
                        var209 = -0.012601988
                    else:
                        var209 = 0.024912806
                else:
                    if input[3] < 94.63197:
                        var209 = -0.07261943
                    else:
                        var209 = 0.0029959083
            else:
                if input[1] < 47.170612:
                    var209 = -0.040961064
                else:
                    if input[1] < 55.418133:
                        var209 = 0.0434809
                    else:
                        var209 = -0.015853254
        else:
            if input[2] < 733.0016:
                var209 = 0.011753073
            else:
                var209 = -0.042988773
    if input[4] < 7.0906034:
        var210 = -0.0420055
    else:
        if input[4] < 8.324405:
            if input[5] < 4737.7285:
                if input[5] < 3955.953:
                    if input[5] < 3912.1926:
                        var210 = 0.0038788256
                    else:
                        var210 = 0.07309245
                else:
                    if input[2] < 733.0016:
                        var210 = 0.0051360773
                    else:
                        var210 = -0.05036822
            else:
                if input[4] < 8.236438:
                    if input[5] < 4948.595:
                        var210 = 0.06413935
                    else:
                        var210 = 0.012842975
                else:
                    var210 = -0.038752582
        else:
            if input[2] < 733.0016:
                var210 = 0.011902254
            else:
                var210 = -0.042459074
    if input[0] < 20.11864:
        var211 = -0.041859064
    else:
        if input[4] < 8.324405:
            if input[5] < 4737.7285:
                if input[5] < 3955.953:
                    if input[5] < 3912.1926:
                        var211 = 0.0036704615
                    else:
                        var211 = 0.06949394
                else:
                    if input[2] < 733.0016:
                        var211 = 0.0045560426
                    else:
                        var211 = -0.0493776
            else:
                if input[4] < 8.236438:
                    if input[5] < 4948.595:
                        var211 = 0.061941326
                    else:
                        var211 = 0.012212574
                else:
                    var211 = -0.03802743
        else:
            if input[2] < 733.0016:
                var211 = 0.012039307
            else:
                var211 = -0.04184867
    if input[0] < 20.11864:
        var212 = -0.04105622
    else:
        if input[2] < 742.155:
            if input[1] < 41.845177:
                if input[1] < 40.763638:
                    if input[0] < 25.36608:
                        var212 = -0.01770062
                    else:
                        var212 = 0.034373127
                else:
                    if input[5] < 3735.5132:
                        var212 = -0.046609577
                    else:
                        var212 = -0.0074287984
            else:
                if input[2] < 429.77728:
                    if input[0] < 25.986551:
                        var212 = -0.027846256
                    else:
                        var212 = 0.0020515004
                else:
                    if input[4] < 8.151678:
                        var212 = 0.02438069
                    else:
                        var212 = 0.0019410978
        else:
            if input[1] < 90.64338:
                if input[3] < 172.44543:
                    if input[3] < 93.38004:
                        var212 = -0.024121247
                    else:
                        var212 = 0.013963004
                else:
                    if input[3] < 196.0285:
                        var212 = -0.046679046
                    else:
                        var212 = 0.010292002
            else:
                var212 = -0.0479025
    if input[0] < 20.11864:
        var213 = -0.04021506
    else:
        if input[4] < 8.324405:
            if input[5] < 4737.7285:
                if input[5] < 3955.953:
                    if input[5] < 3930.5964:
                        var213 = 0.0032900504
                    else:
                        var213 = 0.06807078
                else:
                    if input[2] < 733.0016:
                        var213 = 0.0040508914
                    else:
                        var213 = -0.04839957
            else:
                if input[4] < 8.236438:
                    if input[5] < 4948.595:
                        var213 = 0.060069885
                    else:
                        var213 = 0.011541332
                else:
                    var213 = -0.037207983
        else:
            if input[2] < 733.0016:
                var213 = 0.012060102
            else:
                var213 = -0.040976115
    if input[0] < 20.11864:
        var214 = -0.03929359
    else:
        if input[4] < 8.324405:
            if input[0] < 36.260155:
                if input[5] < 2698.7034:
                    if input[1] < 58.03831:
                        var214 = -0.012876657
                    else:
                        var214 = 0.023123216
                else:
                    if input[5] < 2994.474:
                        var214 = -0.032292232
                    else:
                        var214 = 0.0060070315
            else:
                if input[1] < 74.49065:
                    if input[1] < 66.80687:
                        var214 = 0.00214985
                    else:
                        var214 = -0.051353224
                else:
                    if input[1] < 89.49603:
                        var214 = 0.016118683
                    else:
                        var214 = -0.023497399
        else:
            if input[2] < 733.0016:
                var214 = 0.011581338
            else:
                var214 = -0.040419362
    if input[5] < 431.76425:
        if input[3] < 12.350893:
            var215 = -0.00075879594
        else:
            var215 = -0.048227746
    else:
        if input[2] < 737.73047:
            if input[1] < 41.845177:
                if input[1] < 40.763638:
                    if input[0] < 25.36608:
                        var215 = -0.01662308
                    else:
                        var215 = 0.03389968
                else:
                    if input[5] < 3735.5132:
                        var215 = -0.04393593
                    else:
                        var215 = -0.007691437
            else:
                if input[4] < 7.3376346:
                    if input[5] < 459.61935:
                        var215 = 0.0349222
                    else:
                        var215 = -0.00886666
                else:
                    if input[4] < 8.151678:
                        var215 = 0.033542804
                    else:
                        var215 = 0.0015634861
        else:
            if input[3] < 172.44543:
                if input[3] < 168.97972:
                    if input[1] < 58.8646:
                        var215 = -0.02718328
                    else:
                        var215 = 0.0024245505
                else:
                    if input[2] < 760.2625:
                        var215 = 0.013910924
                    else:
                        var215 = 0.057262715
            else:
                if input[3] < 196.0285:
                    var215 = -0.046517067
                else:
                    var215 = 0.010133225
    if input[0] < 20.11864:
        var216 = -0.03831921
    else:
        if input[2] < 742.155:
            if input[1] < 41.845177:
                if input[1] < 40.763638:
                    if input[0] < 25.36608:
                        var216 = -0.015980223
                    else:
                        var216 = 0.03295386
                else:
                    if input[5] < 3735.5132:
                        var216 = -0.04361873
                    else:
                        var216 = -0.0076983343
            else:
                if input[2] < 429.77728:
                    if input[0] < 25.986551:
                        var216 = -0.026134921
                    else:
                        var216 = 0.0018160718
                else:
                    if input[4] < 8.151678:
                        var216 = 0.022015566
                    else:
                        var216 = 0.0017245401
        else:
            if input[1] < 90.64338:
                if input[0] < 24.202885:
                    if input[1] < 73.290535:
                        var216 = -0.01833074
                    else:
                        var216 = 0.049433827
                else:
                    if input[3] < 93.38004:
                        var216 = -0.036282297
                    else:
                        var216 = 0.0010733701
            else:
                var216 = -0.047092382
    if input[5] < 431.76425:
        if input[3] < 12.350893:
            var217 = 0.000010187112
        else:
            var217 = -0.047038626
    else:
        if input[2] < 737.73047:
            if input[1] < 41.845177:
                if input[1] < 40.763638:
                    if input[0] < 25.36608:
                        var217 = -0.015534341
                    else:
                        var217 = 0.03298005
                else:
                    if input[5] < 3735.5132:
                        var217 = -0.041436877
                    else:
                        var217 = -0.007644728
            else:
                if input[4] < 7.3376346:
                    if input[5] < 459.61935:
                        var217 = 0.032567266
                    else:
                        var217 = -0.008171149
                else:
                    if input[4] < 8.151678:
                        var217 = 0.0317339
                    else:
                        var217 = 0.0020864576
        else:
            if input[3] < 172.44543:
                if input[3] < 168.97972:
                    if input[1] < 73.290535:
                        var217 = -0.017524827
                    else:
                        var217 = 0.008259217
                else:
                    if input[2] < 760.2625:
                        var217 = 0.01210193
                    else:
                        var217 = 0.055168804
            else:
                if input[3] < 196.0285:
                    var217 = -0.045895644
                else:
                    var217 = 0.01012214
    if input[0] < 20.11864:
        var218 = -0.036866087
    else:
        if input[4] < 8.324405:
            if input[5] < 4737.7285:
                if input[5] < 3955.953:
                    if input[5] < 3912.1926:
                        var218 = 0.0024337007
                    else:
                        var218 = 0.062443495
                else:
                    if input[2] < 733.0016:
                        var218 = 0.0035975787
                    else:
                        var218 = -0.047314826
            else:
                if input[4] < 8.236438:
                    if input[5] < 4948.595:
                        var218 = 0.057709236
                    else:
                        var218 = 0.010119279
                else:
                    var218 = -0.036001775
        else:
            if input[2] < 733.0016:
                var218 = 0.012117185
            else:
                var218 = -0.038675647
    if input[5] < 431.76425:
        if input[3] < 12.350893:
            var219 = 0.00065065885
        else:
            var219 = -0.04605349
    else:
        if input[1] < 90.64338:
            if input[1] < 73.03348:
                if input[4] < 8.236438:
                    if input[5] < 4693.2686:
                        var219 = 0.00009118962
                    else:
                        var219 = 0.04646578
                else:
                    if input[2] < 730.8562:
                        var219 = 0.011156796
                    else:
                        var219 = -0.049876776
            else:
                if input[4] < 8.254773:
                    if input[4] < 8.168125:
                        var219 = 0.021262394
                    else:
                        var219 = -0.017891524
                else:
                    if input[4] < 8.324405:
                        var219 = 0.06662887
                    else:
                        var219 = -0.028722722
        else:
            if input[2] < 742.155:
                if input[1] < 91.62102:
                    if input[4] < 8.132412:
                        var219 = -0.014872382
                    else:
                        var219 = -0.05833139
                else:
                    if input[4] < 7.243017:
                        var219 = -0.036318567
                    else:
                        var219 = 0.02402022
            else:
                var219 = -0.045974903
    if input[0] < 20.11864:
        var220 = -0.035629116
    else:
        if input[0] < 36.260155:
            if input[5] < 2698.7034:
                if input[1] < 58.03831:
                    if input[2] < 726.6149:
                        var220 = 0.006297182
                    else:
                        var220 = -0.036840115
                else:
                    if input[1] < 77.085434:
                        var220 = 0.038716022
                    else:
                        var220 = 0.0010600385
            else:
                if input[3] < 94.63197:
                    var220 = -0.06926492
                else:
                    if input[1] < 60.95962:
                        var220 = 0.014665045
                    else:
                        var220 = -0.007073798
        else:
            if input[1] < 74.49065:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var220 = -0.03819849
                    else:
                        var220 = 0.028259233
                else:
                    var220 = -0.049780466
            else:
                if input[1] < 89.49603:
                    if input[5] < 2832.3289:
                        var220 = 0.026385183
                    else:
                        var220 = -0.011154012
                else:
                    if input[2] < 726.6149:
                        var220 = -0.0088903075
                    else:
                        var220 = -0.030249685
    if input[5] < 431.76425:
        if input[3] < 12.350893:
            var221 = 0.0003650436
        else:
            var221 = -0.04530443
    else:
        if input[0] < 36.260155:
            if input[5] < 2698.7034:
                if input[1] < 58.03831:
                    if input[0] < 23.958542:
                        var221 = -0.03777757
                    else:
                        var221 = 0.0075059505
                else:
                    if input[2] < 748.9394:
                        var221 = 0.03006469
                    else:
                        var221 = -0.02186741
            else:
                if input[3] < 94.63197:
                    var221 = -0.0668309
                else:
                    if input[1] < 60.95962:
                        var221 = 0.013874389
                    else:
                        var221 = -0.0074401605
        else:
            if input[1] < 74.49065:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var221 = -0.037297964
                    else:
                        var221 = 0.027675465
                else:
                    var221 = -0.048241463
            else:
                if input[1] < 89.49603:
                    if input[5] < 2832.3289:
                        var221 = 0.025753548
                    else:
                        var221 = -0.010520602
                else:
                    var221 = -0.02411641
    if input[5] < 431.76425:
        if input[3] < 12.350893:
            var222 = 0.0008994423
        else:
            var222 = -0.044545855
    else:
        if input[1] < 90.64338:
            if input[1] < 73.03348:
                if input[4] < 8.236438:
                    if input[5] < 4693.2686:
                        var222 = -0.0006191495
                    else:
                        var222 = 0.044129636
                else:
                    if input[2] < 730.8562:
                        var222 = 0.011804818
                    else:
                        var222 = -0.04879545
            else:
                if input[3] < 121.46589:
                    if input[5] < 2582.5962:
                        var222 = 0.019628605
                    else:
                        var222 = -0.050145872
                else:
                    if input[3] < 171.65364:
                        var222 = 0.053253617
                    else:
                        var222 = -0.01703054
        else:
            if input[2] < 742.155:
                if input[1] < 91.62102:
                    if input[4] < 8.132412:
                        var222 = -0.013545263
                    else:
                        var222 = -0.056538988
                else:
                    if input[4] < 7.243017:
                        var222 = -0.03546978
                    else:
                        var222 = 0.023416601
            else:
                var222 = -0.04476865
    if input[0] < 20.11864:
        var223 = -0.03375083
    else:
        if input[0] < 36.260155:
            if input[5] < 2698.7034:
                if input[1] < 58.03831:
                    if input[1] < 53.28753:
                        var223 = 0.0029385658
                    else:
                        var223 = -0.042163756
                else:
                    if input[1] < 77.085434:
                        var223 = 0.037036367
                    else:
                        var223 = -0.000011356626
            else:
                if input[5] < 2994.474:
                    if input[4] < 8.168125:
                        var223 = -0.0008109227
                    else:
                        var223 = -0.048373286
                else:
                    if input[1] < 79.73578:
                        var223 = -0.005351176
                    else:
                        var223 = 0.022955287
        else:
            if input[1] < 74.49065:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var223 = -0.036740087
                    else:
                        var223 = 0.026868924
                else:
                    var223 = -0.04625521
            else:
                if input[1] < 82.91693:
                    if input[2] < 491.71915:
                        var223 = 0.00007324507
                    else:
                        var223 = 0.03014787
                else:
                    if input[3] < 44.51236:
                        var223 = 0.012372776
                    else:
                        var223 = -0.031494506
    if input[5] < 431.76425:
        if input[1] < 77.085434:
            if input[3] < 13.104021:
                var224 = 0.021289108
            else:
                var224 = -0.025427923
        else:
            var224 = -0.047881674
    else:
        if input[2] < 742.155:
            if input[0] < 26.432243:
                if input[0] < 25.77969:
                    if input[2] < 423.73544:
                        var224 = -0.033689797
                    else:
                        var224 = 0.004360514
                else:
                    if input[1] < 61.794598:
                        var224 = -0.06044818
                    else:
                        var224 = -0.0016472739
            else:
                if input[0] < 30.605228:
                    if input[1] < 85.46175:
                        var224 = 0.040857762
                    else:
                        var224 = 0.001309508
                else:
                    if input[0] < 31.022959:
                        var224 = -0.051169228
                    else:
                        var224 = 0.0060292156
        else:
            if input[1] < 90.64338:
                if input[0] < 24.202885:
                    if input[1] < 73.290535:
                        var224 = -0.015021184
                    else:
                        var224 = 0.043288093
                else:
                    if input[1] < 63.28969:
                        var224 = 0.010038373
                    else:
                        var224 = -0.024943896
            else:
                var224 = -0.044173528
    if input[0] < 20.11864:
        var225 = -0.032624897
    else:
        if input[0] < 36.260155:
            if input[0] < 34.86882:
                if input[0] < 29.948753:
                    if input[0] < 26.970547:
                        var225 = -0.0012204075
                    else:
                        var225 = 0.025520025
                else:
                    if input[4] < 8.206008:
                        var225 = 0.00129093
                    else:
                        var225 = -0.043919418
            else:
                if input[4] < 8.230444:
                    if input[1] < 86.296745:
                        var225 = 0.045086693
                    else:
                        var225 = 0.0047812676
                else:
                    var225 = -0.014716498
        else:
            if input[1] < 71.01151:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var225 = -0.036072772
                    else:
                        var225 = 0.025769567
                else:
                    var225 = -0.04945628
            else:
                if input[2] < 737.73047:
                    if input[4] < 7.2781405:
                        var225 = -0.027746236
                    else:
                        var225 = 0.03479677
                else:
                    if input[3] < 45.044186:
                        var225 = 0.0108163245
                    else:
                        var225 = -0.03593483
    if input[5] < 431.76425:
        if input[1] < 77.085434:
            if input[3] < 13.104021:
                var226 = 0.02120202
            else:
                var226 = -0.024264308
        else:
            var226 = -0.046719782
    else:
        if input[1] < 90.64338:
            if input[1] < 73.290535:
                if input[4] < 8.236438:
                    if input[5] < 4693.2686:
                        var226 = -0.00090190204
                    else:
                        var226 = 0.042191133
                else:
                    if input[2] < 730.8562:
                        var226 = 0.011412906
                    else:
                        var226 = -0.048030373
            else:
                if input[4] < 8.254773:
                    if input[4] < 8.168125:
                        var226 = 0.01853675
                    else:
                        var226 = -0.016802942
                else:
                    if input[0] < 25.415422:
                        var226 = 0.066710144
                    else:
                        var226 = -0.017310431
        else:
            if input[1] < 91.62102:
                if input[3] < 119.888596:
                    var226 = -0.05302344
                else:
                    var226 = -0.011366576
            else:
                if input[2] < 742.155:
                    if input[4] < 7.243017:
                        var226 = -0.03335054
                    else:
                        var226 = 0.022314921
                else:
                    var226 = -0.04276808
    if input[5] < 431.76425:
        if input[1] < 77.085434:
            if input[3] < 13.104021:
                var227 = 0.020898903
            else:
                var227 = -0.023686236
        else:
            var227 = -0.045913752
    else:
        if input[5] < 523.5276:
            if input[4] < 7.1964808:
                var227 = 0.038765002
            else:
                var227 = 0.0070893527
        else:
            if input[4] < 7.256852:
                if input[0] < 22.883705:
                    if input[4] < 7.2208877:
                        var227 = -0.013797769
                    else:
                        var227 = 0.028142396
                else:
                    if input[5] < 4452.413:
                        var227 = -0.037540834
                    else:
                        var227 = 0.012235799
            else:
                if input[5] < 1556.7986:
                    if input[5] < 938.6545:
                        var227 = -0.005865492
                    else:
                        var227 = 0.027198238
                else:
                    if input[5] < 1708.4924:
                        var227 = -0.034726005
                    else:
                        var227 = 0.001410609
    if input[0] < 20.11864:
        var228 = -0.03088188
    else:
        if input[0] < 36.260155:
            if input[5] < 2713.444:
                if input[1] < 58.03831:
                    if input[1] < 53.28753:
                        var228 = 0.003107128
                    else:
                        var228 = -0.041646898
                else:
                    if input[1] < 77.085434:
                        var228 = 0.0362353
                    else:
                        var228 = -0.00057600066
            else:
                if input[3] < 118.32198:
                    if input[0] < 32.96395:
                        var228 = -0.045898113
                    else:
                        var228 = 0.0070487545
                else:
                    if input[0] < 23.221859:
                        var228 = -0.011871814
                    else:
                        var228 = 0.010437485
        else:
            if input[1] < 71.01151:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var228 = -0.036486823
                    else:
                        var228 = 0.02495979
                else:
                    var228 = -0.04746289
            else:
                if input[2] < 737.73047:
                    if input[4] < 7.2781405:
                        var228 = -0.026922692
                    else:
                        var228 = 0.033365414
                else:
                    if input[5] < 1674.2129:
                        var228 = 0.0025666046
                    else:
                        var228 = -0.03242628
    if input[5] < 431.76425:
        if input[1] < 77.085434:
            var229 = -0.0010983474
        else:
            var229 = -0.044566587
    else:
        if input[0] < 36.260155:
            if input[3] < 21.621714:
                var229 = 0.039793693
            else:
                if input[4] < 7.1964808:
                    if input[3] < 131.16777:
                        var229 = -0.034714635
                    else:
                        var229 = -0.0096748015
                else:
                    if input[5] < 2713.444:
                        var229 = 0.009193172
                    else:
                        var229 = -0.0022768723
        else:
            if input[1] < 71.01151:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var229 = -0.035613537
                    else:
                        var229 = 0.024338922
                else:
                    var229 = -0.04619922
            else:
                if input[2] < 737.73047:
                    if input[4] < 7.2781405:
                        var229 = -0.026384661
                    else:
                        var229 = 0.032546237
                else:
                    if input[5] < 1674.2129:
                        var229 = 0.002560575
                    else:
                        var229 = -0.031933527
    if input[5] < 431.76425:
        if input[1] < 77.085434:
            var230 = -0.0006649432
        else:
            var230 = -0.043757074
    else:
        if input[0] < 36.260155:
            if input[3] < 21.621714:
                var230 = 0.038959876
            else:
                if input[4] < 7.1964808:
                    if input[0] < 28.786358:
                        var230 = -0.03591984
                    else:
                        var230 = -0.011243488
                else:
                    if input[0] < 34.02495:
                        var230 = 0.0012195399
                    else:
                        var230 = 0.022986492
        else:
            if input[1] < 71.01151:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var230 = -0.035086434
                    else:
                        var230 = 0.023140294
                else:
                    var230 = -0.044919237
            else:
                if input[1] < 89.49603:
                    if input[2] < 737.73047:
                        var230 = 0.023613205
                    else:
                        var230 = -0.007893503
                else:
                    var230 = -0.022979295
    if input[1] < 47.42564:
        if input[3] < 152.17412:
            if input[3] < 142.28612:
                if input[4] < 8.151678:
                    if input[4] < 7.322918:
                        var231 = -0.021702303
                    else:
                        var231 = 0.030817667
                else:
                    if input[1] < 41.056152:
                        var231 = 0.001716989
                    else:
                        var231 = -0.04784678
            else:
                var231 = 0.044855263
        else:
            var231 = -0.04245456
    else:
        if input[1] < 54.039787:
            if input[0] < 26.55467:
                if input[1] < 52.178165:
                    if input[2] < 717.82:
                        var231 = 0.01578234
                    else:
                        var231 = -0.045945715
                else:
                    var231 = 0.043964423
            else:
                var231 = 0.04844112
        else:
            if input[2] < 753.20294:
                if input[4] < 8.254773:
                    if input[1] < 58.03831:
                        var231 = -0.024071204
                    else:
                        var231 = 0.002725929
                else:
                    if input[1] < 73.03348:
                        var231 = -0.01381653
                    else:
                        var231 = 0.057676036
            else:
                if input[0] < 22.122957:
                    if input[5] < 2645.4595:
                        var231 = 0.054494716
                    else:
                        var231 = -0.009653059
                else:
                    if input[4] < 8.181944:
                        var231 = 0.005987126
                    else:
                        var231 = -0.048121613
    if input[1] < 47.42564:
        if input[3] < 152.17412:
            if input[3] < 142.28612:
                if input[4] < 8.151678:
                    if input[3] < 60.078743:
                        var232 = -0.019545127
                    else:
                        var232 = 0.031680238
                else:
                    if input[1] < 41.056152:
                        var232 = 0.0013434712
                    else:
                        var232 = -0.046833307
            else:
                var232 = 0.04392725
        else:
            var232 = -0.04157299
    else:
        if input[1] < 54.039787:
            if input[0] < 21.95693:
                if input[5] < 1822.3998:
                    var232 = -0.036227874
                else:
                    var232 = 0.005334483
            else:
                if input[4] < 8.236438:
                    if input[4] < 8.136787:
                        var232 = 0.0029939918
                    else:
                        var232 = 0.05876396
                else:
                    var232 = -0.025329767
        else:
            if input[2] < 753.20294:
                if input[4] < 8.254773:
                    if input[1] < 58.03831:
                        var232 = -0.02326638
                    else:
                        var232 = 0.002812577
                else:
                    if input[1] < 73.03348:
                        var232 = -0.012755391
                    else:
                        var232 = 0.0535666
            else:
                if input[0] < 22.122957:
                    if input[5] < 2545.023:
                        var232 = 0.053623747
                    else:
                        var232 = -0.009811799
                else:
                    if input[4] < 8.181944:
                        var232 = 0.005835287
                    else:
                        var232 = -0.04758399
    if input[0] < 20.11864:
        var233 = -0.029432146
    else:
        if input[0] < 36.260155:
            if input[0] < 34.86882:
                if input[0] < 29.948753:
                    if input[0] < 26.970547:
                        var233 = -0.0009226768
                    else:
                        var233 = 0.023701284
                else:
                    if input[4] < 8.206008:
                        var233 = 0.00032493292
                    else:
                        var233 = -0.040968522
            else:
                if input[4] < 8.230444:
                    if input[1] < 86.296745:
                        var233 = 0.042162213
                    else:
                        var233 = 0.0048314603
                else:
                    var233 = -0.012760343
        else:
            if input[1] < 71.01151:
                if input[1] < 66.80687:
                    if input[1] < 47.42564:
                        var233 = -0.03336061
                    else:
                        var233 = 0.020618748
                else:
                    var233 = -0.043730304
            else:
                if input[1] < 89.49603:
                    if input[2] < 737.73047:
                        var233 = 0.0227797
                    else:
                        var233 = -0.0067021116
                else:
                    var233 = -0.0223795
    if input[0] < 36.260155:
        if input[0] < 26.432243:
            if input[4] < 8.254773:
                if input[5] < 2346.022:
                    if input[5] < 2022.6626:
                        var234 = -0.007401527
                    else:
                        var234 = 0.037296638
                else:
                    if input[3] < 130.4914:
                        var234 = -0.030522719
                    else:
                        var234 = -0.0038886534
            else:
                if input[1] < 73.290535:
                    if input[2] < 744.1235:
                        var234 = 0.01614678
                    else:
                        var234 = -0.03153798
                else:
                    if input[2] < 762.44934:
                        var234 = 0.054408874
                    else:
                        var234 = -0.004230997
        else:
            if input[2] < 744.1235:
                if input[1] < 78.56071:
                    if input[5] < 2748.8748:
                        var234 = 0.046508703
                    else:
                        var234 = 0.0026862463
                else:
                    if input[3] < 80.19552:
                        var234 = -0.032670826
                    else:
                        var234 = 0.017934073
            else:
                if input[5] < 3671.9841:
                    var234 = -0.04530775
                else:
                    if input[1] < 63.28969:
                        var234 = 0.023271864
                    else:
                        var234 = -0.016969686
    else:
        if input[1] < 71.01151:
            if input[1] < 66.80687:
                if input[1] < 47.42564:
                    var234 = -0.03284293
                else:
                    var234 = 0.019818043
            else:
                var234 = -0.04258023
        else:
            if input[1] < 89.49603:
                if input[2] < 737.73047:
                    if input[2] < 452.94366:
                        var234 = 0.0037650173
                    else:
                        var234 = 0.029207626
                else:
                    var234 = -0.007005942
            else:
                var234 = -0.022015862
    if input[0] < 36.260155:
        if input[0] < 34.86882:
            if input[5] < 4798.541:
                if input[5] < 3955.953:
                    if input[5] < 3912.1926:
                        var235 = 0.00014183215
                    else:
                        var235 = 0.049997386
                else:
                    if input[0] < 23.580992:
                        var235 = 0.02384094
                    else:
                        var235 = -0.030821813
            else:
                if input[5] < 4948.595:
                    var235 = 0.047836658
                else:
                    if input[2] < 748.9394:
                        var235 = 0.036557965
                    else:
                        var235 = -0.037079703
        else:
            if input[4] < 8.230444:
                if input[1] < 86.296745:
                    var235 = 0.040201873
                else:
                    var235 = 0.0055224644
            else:
                var235 = -0.013081983
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                if input[1] < 66.80687:
                    var235 = -0.0070427195
                else:
                    var235 = -0.045102876
            else:
                if input[3] < 88.21615:
                    var235 = 0.026944507
                else:
                    var235 = -0.020457916
        else:
            if input[1] < 82.91693:
                var235 = 0.019405851
            else:
                if input[3] < 44.51236:
                    var235 = 0.0112712635
                else:
                    var235 = -0.029466584
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var236 = -0.0007907638
                    else:
                        var236 = 0.041972365
                else:
                    if input[4] < 8.081833:
                        var236 = 0.0094464775
                    else:
                        var236 = -0.034605708
            else:
                var236 = 0.048749395
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var236 = -0.037799593
                    else:
                        var236 = 0.012570172
                else:
                    if input[3] < 189.17482:
                        var236 = 0.046411235
                    else:
                        var236 = -0.018053908
            else:
                var236 = -0.049549222
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var236 = -0.00963417
            else:
                if input[0] < 38.797752:
                    var236 = 0.052468743
                else:
                    var236 = 0.00066108775
        else:
            if input[1] < 52.434742:
                var236 = 0.005105397
            else:
                var236 = -0.0345044
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var237 = -0.00080732844
                    else:
                        var237 = 0.040271502
                else:
                    if input[4] < 8.081833:
                        var237 = 0.009040858
                    else:
                        var237 = -0.033453003
            else:
                var237 = 0.047574807
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var237 = -0.036796164
                    else:
                        var237 = 0.012419081
                else:
                    if input[3] < 189.17482:
                        var237 = 0.045699935
                    else:
                        var237 = -0.01747435
            else:
                var237 = -0.048748285
    else:
        if input[4] < 8.236438:
            if input[5] < 4948.595:
                var237 = 0.04686032
            else:
                if input[2] < 748.9394:
                    if input[0] < 40.43362:
                        var237 = 0.041383345
                    else:
                        var237 = -0.0018453591
                else:
                    var237 = -0.035038125
        else:
            var237 = -0.03213014
    if input[1] < 47.42564:
        if input[3] < 152.17412:
            if input[3] < 142.28612:
                if input[4] < 8.151678:
                    if input[3] < 60.078743:
                        var238 = -0.01903773
                    else:
                        var238 = 0.030988028
                else:
                    if input[1] < 41.056152:
                        var238 = -0.000049213344
                    else:
                        var238 = -0.044992406
            else:
                var238 = 0.04029824
        else:
            var238 = -0.038020317
    else:
        if input[1] < 54.039787:
            if input[1] < 52.178165:
                if input[2] < 737.73047:
                    if input[0] < 21.746157:
                        var238 = -0.020724608
                    else:
                        var238 = 0.045352094
                else:
                    if input[2] < 764.464:
                        var238 = -0.03973454
                    else:
                        var238 = -0.004750512
            else:
                if input[1] < 53.28753:
                    var238 = 0.06306552
                else:
                    var238 = 0.017564794
        else:
            if input[0] < 30.605228:
                if input[4] < 8.254773:
                    if input[0] < 26.432243:
                        var238 = -0.0061959415
                    else:
                        var238 = 0.0165762
                else:
                    if input[2] < 762.44934:
                        var238 = 0.03936082
                    else:
                        var238 = -0.017725496
            else:
                if input[4] < 8.16224:
                    if input[0] < 31.022959:
                        var238 = -0.04769101
                    else:
                        var238 = 0.012638085
                else:
                    if input[3] < 62.15085:
                        var238 = -0.00043917896
                    else:
                        var238 = -0.044530995
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var239 = -0.00083187496
                    else:
                        var239 = 0.038723577
                else:
                    if input[4] < 8.081833:
                        var239 = 0.009102649
                    else:
                        var239 = -0.032430116
            else:
                var239 = 0.04618538
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var239 = -0.035803124
                    else:
                        var239 = 0.012201316
                else:
                    if input[3] < 189.17482:
                        var239 = 0.044830732
                    else:
                        var239 = -0.016851036
            else:
                var239 = -0.048074372
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var239 = -0.008805367
            else:
                if input[0] < 38.797752:
                    var239 = 0.050872814
                else:
                    var239 = 0.00068472937
        else:
            if input[1] < 55.418133:
                var239 = 0.0040696743
            else:
                var239 = -0.03315167
    if input[0] < 36.260155:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                if input[2] < 429.77728:
                    var240 = -0.039873168
                else:
                    if input[0] < 22.883705:
                        var240 = 0.031565577
                    else:
                        var240 = -0.013703271
            else:
                if input[5] < 4798.541:
                    if input[5] < 2713.444:
                        var240 = 0.0074767764
                    else:
                        var240 = -0.0048178304
                else:
                    if input[5] < 4948.595:
                        var240 = 0.044554945
                    else:
                        var240 = -0.0025709101
        else:
            if input[4] < 8.230444:
                if input[1] < 86.296745:
                    var240 = 0.036737815
                else:
                    var240 = 0.0046406686
            else:
                var240 = -0.010640296
    else:
        if input[1] < 71.01151:
            if input[1] < 54.43293:
                if input[1] < 47.42564:
                    var240 = -0.030636584
                else:
                    var240 = 0.030173665
            else:
                var240 = -0.036120895
        else:
            if input[1] < 89.49603:
                if input[5] < 2201.0266:
                    var240 = 0.021738356
                else:
                    var240 = -0.004143499
            else:
                var240 = -0.021104585
    if input[1] < 90.64338:
        if input[1] < 80.01135:
            if input[3] < 62.92014:
                if input[5] < 1080.2268:
                    if input[1] < 57.08752:
                        var241 = -0.036902893
                    else:
                        var241 = 0.009378358
                else:
                    if input[4] < 7.256852:
                        var241 = 0.0052110604
                    else:
                        var241 = 0.039333377
            else:
                if input[1] < 63.28969:
                    if input[4] < 8.236438:
                        var241 = 0.007212215
                    else:
                        var241 = -0.029235393
                else:
                    if input[2] < 750.9746:
                        var241 = -0.008637437
                    else:
                        var241 = -0.04548916
        else:
            if input[3] < 126.27938:
                if input[5] < 2624.5793:
                    if input[5] < 2269.6565:
                        var241 = -0.0057954486
                    else:
                        var241 = 0.05346442
                else:
                    if input[4] < 8.12684:
                        var241 = 0.0056101726
                    else:
                        var241 = -0.05859362
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var241 = 0.05949017
                    else:
                        var241 = 0.0051883953
                else:
                    if input[1] < 86.480606:
                        var241 = 0.01592948
                    else:
                        var241 = -0.04453684
    else:
        if input[1] < 91.62102:
            if input[5] < 2391.5444:
                var241 = -0.050643902
            else:
                var241 = -0.009482823
        else:
            if input[2] < 742.155:
                if input[3] < 99.609856:
                    if input[3] < 48.872616:
                        var241 = -0.008304554
                    else:
                        var241 = 0.048547417
                else:
                    if input[5] < 4033.4216:
                        var241 = -0.020018974
                    else:
                        var241 = 0.02661232
            else:
                var241 = -0.03965233
    if input[1] < 47.42564:
        if input[3] < 152.17412:
            if input[3] < 142.28612:
                if input[4] < 8.151678:
                    if input[3] < 60.078743:
                        var242 = -0.018287595
                    else:
                        var242 = 0.029781638
                else:
                    if input[1] < 41.056152:
                        var242 = -0.0005996082
                    else:
                        var242 = -0.043951128
            else:
                var242 = 0.0385607
        else:
            var242 = -0.03643314
    else:
        if input[1] < 54.039787:
            if input[1] < 52.178165:
                if input[2] < 737.73047:
                    if input[0] < 21.746157:
                        var242 = -0.020261616
                    else:
                        var242 = 0.044054464
                else:
                    if input[3] < 166.72157:
                        var242 = -0.038456835
                    else:
                        var242 = -0.0076600276
            else:
                if input[1] < 53.28753:
                    var242 = 0.06123793
                else:
                    var242 = 0.016427504
        else:
            if input[2] < 753.20294:
                if input[4] < 8.254773:
                    if input[1] < 58.03831:
                        var242 = -0.022346294
                    else:
                        var242 = 0.0028729187
                else:
                    if input[1] < 73.03348:
                        var242 = -0.008784911
                    else:
                        var242 = 0.0468658
            else:
                if input[0] < 22.122957:
                    if input[5] < 2416.7178:
                        var242 = 0.04880663
                    else:
                        var242 = -0.0075546936
                else:
                    if input[4] < 8.181944:
                        var242 = 0.005928732
                    else:
                        var242 = -0.046597265
    if input[1] < 90.64338:
        if input[1] < 80.01135:
            if input[3] < 62.92014:
                if input[5] < 1080.2268:
                    if input[1] < 57.08752:
                        var243 = -0.035621386
                    else:
                        var243 = 0.008497623
                else:
                    if input[4] < 7.256852:
                        var243 = 0.004977941
                    else:
                        var243 = 0.03772859
            else:
                if input[1] < 63.28969:
                    if input[5] < 1799.6632:
                        var243 = -0.041759204
                    else:
                        var243 = 0.0058615915
                else:
                    if input[2] < 750.9746:
                        var243 = -0.008362989
                    else:
                        var243 = -0.044760853
        else:
            if input[3] < 126.27938:
                if input[5] < 2624.5793:
                    if input[5] < 2269.6565:
                        var243 = -0.005364097
                    else:
                        var243 = 0.051299166
                else:
                    if input[4] < 8.12684:
                        var243 = 0.0054547423
                    else:
                        var243 = -0.056853194
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var243 = 0.057694107
                    else:
                        var243 = 0.004993441
                else:
                    if input[1] < 86.480606:
                        var243 = 0.015404038
                    else:
                        var243 = -0.043695655
    else:
        if input[1] < 91.62102:
            if input[4] < 8.120774:
                var243 = -0.0109426
            else:
                var243 = -0.049708154
        else:
            if input[2] < 742.155:
                if input[4] < 7.310009:
                    if input[1] < 97.52708:
                        var243 = -0.032041978
                    else:
                        var243 = 0.016585834
                else:
                    if input[4] < 8.215596:
                        var243 = 0.031538483
                    else:
                        var243 = -0.004921796
            else:
                var243 = -0.038937997
    if input[1] < 47.42564:
        if input[3] < 152.17412:
            if input[3] < 142.28612:
                if input[4] < 8.151678:
                    if input[3] < 60.078743:
                        var244 = -0.01786562
                    else:
                        var244 = 0.028443499
                else:
                    if input[5] < 3097.8657:
                        var244 = -0.04146902
                    else:
                        var244 = -0.0075242887
            else:
                var244 = 0.037054043
        else:
            var244 = -0.035383087
    else:
        if input[1] < 54.039787:
            if input[1] < 52.178165:
                if input[2] < 737.73047:
                    if input[0] < 21.746157:
                        var244 = -0.0198566
                    else:
                        var244 = 0.042821683
                else:
                    if input[3] < 166.72157:
                        var244 = -0.037532933
                    else:
                        var244 = -0.008236223
            else:
                if input[1] < 53.28753:
                    var244 = 0.0592767
                else:
                    var244 = 0.015447569
        else:
            if input[2] < 753.20294:
                if input[4] < 8.254773:
                    if input[5] < 4737.7285:
                        var244 = -0.0019414177
                    else:
                        var244 = 0.032110065
                else:
                    if input[1] < 73.03348:
                        var244 = -0.0084050065
                    else:
                        var244 = 0.04458024
            else:
                if input[0] < 22.122957:
                    if input[5] < 2416.7178:
                        var244 = 0.04627108
                    else:
                        var244 = -0.0074895206
                else:
                    if input[4] < 8.181944:
                        var244 = 0.0059044943
                    else:
                        var244 = -0.04599775
    if input[0] < 36.260155:
        if input[0] < 34.86882:
            if input[4] < 7.256852:
                if input[2] < 429.77728:
                    var245 = -0.038818892
                else:
                    if input[0] < 22.883705:
                        var245 = 0.029747574
                    else:
                        var245 = -0.012935869
            else:
                if input[5] < 4798.541:
                    if input[0] < 30.605228:
                        var245 = 0.0030156837
                    else:
                        var245 = -0.014760484
                else:
                    if input[5] < 4948.595:
                        var245 = 0.042147603
                    else:
                        var245 = -0.0027158032
        else:
            if input[5] < 2213.9355:
                var245 = 0.037565127
            else:
                if input[3] < 103.43883:
                    var245 = -0.017603347
                else:
                    var245 = 0.022540359
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                var245 = -0.03524312
            else:
                if input[5] < 3912.1926:
                    var245 = 0.014578774
                else:
                    var245 = -0.015716136
        else:
            if input[1] < 89.49603:
                if input[5] < 2832.3289:
                    if input[2] < 457.59:
                        var245 = 0.0069115087
                    else:
                        var245 = 0.025640076
                else:
                    var245 = -0.008482813
            else:
                var245 = -0.020018524
    if input[0] < 20.11864:
        var246 = -0.026297897
    else:
        if input[0] < 20.957043:
            if input[1] < 81.32996:
                if input[1] < 49.79559:
                    var246 = -0.0057766866
                else:
                    if input[2] < 429.77728:
                        var246 = 0.0063437307
                    else:
                        var246 = 0.043424126
            else:
                var246 = -0.024707003
        else:
            if input[0] < 21.366615:
                if input[3] < 163.58118:
                    var246 = -0.041961007
                else:
                    var246 = 0.0053988746
            else:
                if input[4] < 8.324405:
                    if input[4] < 7.293997:
                        var246 = -0.0098917745
                    else:
                        var246 = 0.0037745964
                else:
                    var246 = -0.030743817
    if input[0] < 36.260155:
        if input[0] < 26.432243:
            if input[4] < 8.254773:
                if input[4] < 8.187523:
                    if input[1] < 79.73578:
                        var247 = -0.009336775
                    else:
                        var247 = 0.01845171
                else:
                    if input[5] < 3600.7922:
                        var247 = -0.044830352
                    else:
                        var247 = 0.023833217
            else:
                if input[1] < 73.290535:
                    if input[2] < 746.90137:
                        var247 = 0.013536202
                    else:
                        var247 = -0.027062042
                else:
                    if input[4] < 8.301448:
                        var247 = 0.045173835
                    else:
                        var247 = -0.0058492064
        else:
            if input[2] < 744.1235:
                if input[1] < 77.89221:
                    if input[5] < 2748.8748:
                        var247 = 0.044434026
                    else:
                        var247 = 0.0018392407
                else:
                    if input[3] < 80.19552:
                        var247 = -0.029369796
                    else:
                        var247 = 0.017568612
            else:
                if input[5] < 3671.9841:
                    var247 = -0.044087306
                else:
                    if input[1] < 63.28969:
                        var247 = 0.019439531
                    else:
                        var247 = -0.016133165
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                var247 = -0.034288917
            else:
                if input[5] < 3912.1926:
                    var247 = 0.014577649
                else:
                    var247 = -0.015415765
        else:
            if input[1] < 89.49603:
                if input[3] < 75.37392:
                    var247 = 0.021550579
                else:
                    var247 = -0.008155089
            else:
                var247 = -0.019387653
    if input[0] < 20.11864:
        var248 = -0.025625572
    else:
        if input[0] < 20.957043:
            if input[1] < 81.32996:
                if input[1] < 49.79559:
                    var248 = -0.0050456217
                else:
                    if input[2] < 429.77728:
                        var248 = 0.006577571
                    else:
                        var248 = 0.04211264
            else:
                var248 = -0.023573125
        else:
            if input[0] < 21.366615:
                if input[3] < 163.58118:
                    var248 = -0.04084103
                else:
                    var248 = 0.004974644
            else:
                if input[4] < 8.324405:
                    if input[0] < 22.883705:
                        var248 = 0.014707597
                    else:
                        var248 = -0.00024053341
                else:
                    var248 = -0.030204182
    var249 = var193 + var194 + var195 + var196 + var197 + var198 + var199 + var200 + var201 + var202 + var203 + var204 + var205 + var206 + var207 + var208 + var209 + var210 + var211 + var212 + var213 + var214 + var215 + var216 + var217 + var218 + var219 + var220 + var221 + var222 + var223 + var224 + var225 + var226 + var227 + var228 + var229 + var230 + var231 + var232 + var233 + var234 + var235 + var236 + var237 + var238 + var239 + var240 + var241 + var242 + var243 + var244 + var245 + var246 + var247 + var248
    if input[0] < 36.260155:
        if input[0] < 26.432243:
            if input[4] < 8.254773:
                if input[5] < 2457.2336:
                    if input[5] < 2022.6626:
                        var250 = -0.0061760517
                    else:
                        var250 = 0.024910836
                else:
                    if input[3] < 118.32198:
                        var250 = -0.043988068
                    else:
                        var250 = -0.0045979307
            else:
                if input[2] < 762.44934:
                    if input[4] < 8.285472:
                        var250 = 0.047156062
                    else:
                        var250 = 0.0047089006
                else:
                    var250 = -0.011831808
        else:
            if input[2] < 744.1235:
                if input[4] < 8.206008:
                    if input[1] < 81.10271:
                        var250 = 0.03364536
                    else:
                        var250 = 0.002989313
                else:
                    if input[5] < 2681.302:
                        var250 = 0.03646093
                    else:
                        var250 = -0.041182563
            else:
                if input[5] < 3671.9841:
                    var250 = -0.0434851
                else:
                    if input[2] < 764.464:
                        var250 = -0.0094403215
                    else:
                        var250 = 0.027033908
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                var250 = -0.03359636
            else:
                if input[5] < 3912.1926:
                    var250 = 0.014041521
                else:
                    var250 = -0.014870237
        else:
            if input[1] < 89.49603:
                if input[5] < 2201.0266:
                    var250 = 0.020101268
                else:
                    var250 = -0.0013281929
            else:
                var250 = -0.018940404
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[4] < 8.168125:
                    if input[2] < 760.2625:
                        var251 = 0.0022903294
                    else:
                        var251 = 0.042625103
                else:
                    if input[0] < 30.605228:
                        var251 = -0.0029241887
                    else:
                        var251 = -0.025049696
            else:
                if input[0] < 23.580992:
                    var251 = -0.017049998
                else:
                    var251 = 0.046194788
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var251 = -0.03448656
                    else:
                        var251 = 0.012349576
                else:
                    if input[3] < 186.3421:
                        var251 = 0.03779189
                    else:
                        var251 = 0.00055764517
            else:
                var251 = -0.046600807
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var251 = -0.010759519
            else:
                if input[0] < 38.797752:
                    var251 = 0.047650147
                else:
                    var251 = 0.0007320847
        else:
            if input[1] < 57.57434:
                var251 = -0.0010730632
            else:
                var251 = -0.028604839
    if input[0] < 36.260155:
        if input[0] < 34.86882:
            if input[0] < 29.948753:
                if input[0] < 26.970547:
                    if input[5] < 4359.007:
                        var252 = 0.0009640475
                    else:
                        var252 = -0.03314816
                else:
                    if input[2] < 748.9394:
                        var252 = 0.03189777
                    else:
                        var252 = -0.0143855605
            else:
                if input[4] < 8.206008:
                    if input[0] < 31.948093:
                        var252 = -0.02613897
                    else:
                        var252 = 0.021948703
                else:
                    if input[3] < 65.1018:
                        var252 = -0.0012058528
                    else:
                        var252 = -0.046726253
        else:
            if input[2] < 730.8562:
                var252 = 0.031332657
            else:
                if input[4] < 8.155125:
                    var252 = 0.01461688
                else:
                    var252 = -0.010500322
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                var252 = -0.03290778
            else:
                if input[5] < 3912.1926:
                    var252 = 0.013509548
                else:
                    var252 = -0.014646905
        else:
            if input[1] < 82.91693:
                var252 = 0.01759281
            else:
                if input[3] < 44.51236:
                    var252 = 0.011055126
                else:
                    var252 = -0.027231157
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var253 = -0.0007376487
                    else:
                        var253 = 0.035519462
                else:
                    if input[0] < 22.946997:
                        var253 = -0.0040843775
                    else:
                        var253 = -0.045099508
            else:
                var253 = 0.039831217
        else:
            if input[0] < 23.580992:
                if input[4] < 8.142715:
                    var253 = 0.028702019
                else:
                    var253 = 0.008170134
            else:
                if input[2] < 733.0016:
                    if input[4] < 8.102652:
                        var253 = -0.020193674
                    else:
                        var253 = 0.028605912
                else:
                    var253 = -0.048093807
    else:
        if input[4] < 8.236438:
            if input[5] < 4948.595:
                var253 = 0.041027498
            else:
                if input[2] < 748.9394:
                    if input[3] < 173.21967:
                        var253 = 0.0018688135
                    else:
                        var253 = 0.035995204
                else:
                    var253 = -0.032364618
        else:
            var253 = -0.02836324
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var254 = -0.0006709494
                    else:
                        var254 = 0.034275007
                else:
                    if input[0] < 22.946997:
                        var254 = -0.0039093373
                    else:
                        var254 = -0.044313665
            else:
                var254 = 0.039093915
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var254 = -0.0331923
                    else:
                        var254 = 0.012230049
                else:
                    if input[3] < 186.3421:
                        var254 = 0.036562324
                    else:
                        var254 = 0.0011564348
            else:
                var254 = -0.045301076
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var254 = -0.009430073
            else:
                if input[5] < 5958.2637:
                    var254 = 0.04668471
                else:
                    var254 = 0.0014526359
        else:
            if input[1] < 57.57434:
                var254 = -0.0013896906
            else:
                var254 = -0.027711956
    if input[1] < 90.64338:
        if input[1] < 80.01135:
            if input[1] < 77.085434:
                if input[1] < 73.290535:
                    if input[4] < 8.241077:
                        var255 = 0.00096120854
                    else:
                        var255 = -0.029835472
                else:
                    if input[2] < 750.9746:
                        var255 = 0.040677615
                    else:
                        var255 = -0.01661536
            else:
                if input[0] < 23.404404:
                    if input[0] < 21.746157:
                        var255 = -0.022120295
                    else:
                        var255 = 0.028356483
                else:
                    if input[0] < 31.022959:
                        var255 = -0.043547682
                    else:
                        var255 = -0.011957593
        else:
            if input[3] < 126.27938:
                if input[5] < 2624.5793:
                    if input[5] < 2269.6565:
                        var255 = -0.005475707
                    else:
                        var255 = 0.045489665
                else:
                    if input[4] < 8.12684:
                        var255 = 0.0056292494
                    else:
                        var255 = -0.053634435
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var255 = 0.05306035
                    else:
                        var255 = 0.006054565
                else:
                    if input[1] < 86.480606:
                        var255 = 0.014364729
                    else:
                        var255 = -0.040330116
    else:
        if input[1] < 91.62102:
            if input[4] < 8.132412:
                var255 = -0.009966167
            else:
                var255 = -0.046860855
        else:
            if input[2] < 742.155:
                if input[3] < 99.609856:
                    if input[3] < 48.872616:
                        var255 = -0.006402736
                    else:
                        var255 = 0.0458375
                else:
                    if input[5] < 4033.4216:
                        var255 = -0.018868199
                    else:
                        var255 = 0.022962231
            else:
                var255 = -0.036253296
    if input[1] < 90.64338:
        if input[1] < 80.01135:
            if input[3] < 62.92014:
                if input[5] < 1080.2268:
                    if input[1] < 57.08752:
                        var256 = -0.033896472
                    else:
                        var256 = 0.0074288505
                else:
                    if input[4] < 7.256852:
                        var256 = 0.0059715565
                    else:
                        var256 = 0.036352556
            else:
                if input[1] < 63.28969:
                    if input[4] < 8.120774:
                        var256 = -0.019716853
                    else:
                        var256 = 0.009707834
                else:
                    if input[2] < 750.9746:
                        var256 = -0.008035076
                    else:
                        var256 = -0.043693256
        else:
            if input[3] < 126.27938:
                if input[5] < 2624.5793:
                    if input[5] < 2269.6565:
                        var256 = -0.0052524
                    else:
                        var256 = 0.044210847
                else:
                    if input[4] < 8.12684:
                        var256 = 0.005694791
                    else:
                        var256 = -0.052507192
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var256 = 0.05167518
                    else:
                        var256 = 0.005776688
                else:
                    if input[1] < 86.480606:
                        var256 = 0.013961727
                    else:
                        var256 = -0.039599508
    else:
        if input[1] < 91.62102:
            if input[4] < 8.132412:
                var256 = -0.009763419
            else:
                var256 = -0.04564663
        else:
            if input[2] < 742.155:
                if input[0] < 26.818922:
                    if input[3] < 94.150635:
                        var256 = 0.015977923
                    else:
                        var256 = -0.017654598
                else:
                    if input[0] < 33.560135:
                        var256 = 0.03969234
                    else:
                        var256 = -0.005746457
            else:
                var256 = -0.035701852
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[4] < 8.168125:
                    if input[2] < 760.2625:
                        var257 = 0.002014943
                    else:
                        var257 = 0.038050376
                else:
                    if input[0] < 30.605228:
                        var257 = -0.0026600494
                    else:
                        var257 = -0.022598125
            else:
                if input[0] < 23.580992:
                    var257 = -0.014316578
                else:
                    var257 = 0.042426493
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var257 = -0.0317588
                    else:
                        var257 = 0.011560666
                else:
                    if input[3] < 186.3421:
                        var257 = 0.035549056
                    else:
                        var257 = 0.0015253801
            else:
                var257 = -0.044749737
    else:
        if input[4] < 8.236438:
            if input[5] < 4948.595:
                var257 = 0.039352436
            else:
                if input[2] < 748.9394:
                    if input[3] < 176.31873:
                        var257 = 0.0017808123
                    else:
                        var257 = 0.034576315
                else:
                    var257 = -0.031199232
        else:
            var257 = -0.027333925
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[3] < 145.52826:
                    if input[3] < 140.61911:
                        var258 = -0.00068151095
                    else:
                        var258 = 0.044643387
                else:
                    if input[2] < 729.3266:
                        var258 = 0.011343355
                    else:
                        var258 = -0.030733133
            else:
                if input[0] < 23.580992:
                    var258 = -0.01363182
                else:
                    var258 = 0.041442156
        else:
            if input[0] < 23.580992:
                if input[3] < 192.77003:
                    var258 = 0.027732713
                else:
                    var258 = 0.0067988927
            else:
                if input[2] < 733.0016:
                    if input[2] < 462.86743:
                        var258 = -0.020835085
                    else:
                        var258 = 0.016891094
                else:
                    var258 = -0.046228737
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var258 = -0.00870323
            else:
                if input[5] < 5958.2637:
                    var258 = 0.04561017
                else:
                    var258 = 0.0005109807
        else:
            var258 = -0.018311134
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[4] < 8.168125:
                    if input[2] < 760.2625:
                        var259 = 0.001923629
                    else:
                        var259 = 0.036680587
                else:
                    if input[5] < 2681.302:
                        var259 = 0.0009392408
                    else:
                        var259 = -0.014738174
            else:
                if input[0] < 23.580992:
                    var259 = -0.013131102
                else:
                    var259 = 0.04018578
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var259 = -0.030706773
                    else:
                        var259 = 0.011824241
                else:
                    if input[3] < 186.3421:
                        var259 = 0.034694783
                    else:
                        var259 = 0.0016727321
            else:
                var259 = -0.043307655
    else:
        if input[4] < 8.236438:
            if input[0] < 27.271341:
                var259 = -0.006563451
            else:
                if input[5] < 5958.2637:
                    var259 = 0.043781683
                else:
                    var259 = -0.0026787065
        else:
            var259 = -0.02645574
    if input[1] < 41.845177:
        if input[0] < 23.34363:
            var260 = -0.035646852
        else:
            if input[2] < 726.6149:
                var260 = 0.01634656
            else:
                var260 = -0.013896318
    else:
        if input[1] < 43.866257:
            var260 = 0.027794668
        else:
            if input[1] < 47.42564:
                if input[4] < 8.151678:
                    if input[2] < 703.2164:
                        var260 = -0.014109778
                    else:
                        var260 = 0.017652925
                else:
                    if input[3] < 148.80124:
                        var260 = -0.034063734
                    else:
                        var260 = -0.00639364
            else:
                if input[1] < 50.49679:
                    if input[0] < 21.746157:
                        var260 = -0.006688432
                    else:
                        var260 = 0.03395691
                else:
                    if input[1] < 52.178165:
                        var260 = -0.026622398
                    else:
                        var260 = 0.0017815701
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[3] < 145.52826:
                    if input[3] < 140.61911:
                        var261 = -0.00063296984
                    else:
                        var261 = 0.043399736
                else:
                    if input[2] < 729.3266:
                        var261 = 0.01109621
                    else:
                        var261 = -0.030083722
            else:
                if input[0] < 23.580992:
                    var261 = -0.012337697
                else:
                    var261 = 0.039089378
        else:
            if input[0] < 23.580992:
                if input[3] < 192.77003:
                    var261 = 0.027077755
                else:
                    var261 = 0.0066965246
            else:
                if input[2] < 733.0016:
                    if input[2] < 462.86743:
                        var261 = -0.019695107
                    else:
                        var261 = 0.016137293
                else:
                    var261 = -0.045075458
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var261 = -0.0074622496
            else:
                if input[0] < 38.797752:
                    var261 = 0.043696966
                else:
                    var261 = -0.00074232754
        else:
            var261 = -0.017775944
    if input[1] < 41.845177:
        if input[0] < 23.34363:
            var262 = -0.034536228
        else:
            if input[2] < 726.6149:
                var262 = 0.01581629
            else:
                var262 = -0.013610131
    else:
        if input[1] < 43.866257:
            var262 = 0.026744518
        else:
            if input[1] < 47.42564:
                if input[4] < 8.151678:
                    if input[2] < 703.2164:
                        var262 = -0.013520013
                    else:
                        var262 = 0.017490843
                else:
                    if input[3] < 148.80124:
                        var262 = -0.032832336
                    else:
                        var262 = -0.0064147115
            else:
                if input[1] < 63.28969:
                    if input[4] < 8.120774:
                        var262 = -0.012014951
                    else:
                        var262 = 0.01805032
                else:
                    if input[1] < 64.715355:
                        var262 = -0.043909773
                    else:
                        var262 = 0.0004234566
    if input[0] < 20.957043:
        if input[1] < 81.32996:
            if input[1] < 50.848637:
                var263 = -0.0051268125
            else:
                if input[2] < 433.85468:
                    var263 = 0.005158196
                else:
                    var263 = 0.037330475
        else:
            var263 = -0.025315836
    else:
        if input[0] < 21.366615:
            if input[4] < 8.081833:
                var263 = 0.0014992038
            else:
                var263 = -0.0406639
        else:
            if input[4] < 8.324405:
                if input[0] < 22.883705:
                    if input[3] < 107.69633:
                        var263 = 0.039066218
                    else:
                        var263 = -0.009429877
                else:
                    if input[0] < 23.014591:
                        var263 = -0.036885094
                    else:
                        var263 = 0.0011476602
            else:
                var263 = -0.028404105
    if input[0] < 20.11864:
        var264 = -0.022606878
    else:
        if input[0] < 20.957043:
            if input[1] < 81.32996:
                if input[1] < 52.434742:
                    var264 = -0.0004742708
                else:
                    if input[0] < 20.484303:
                        var264 = 0.018180655
                    else:
                        var264 = 0.043166377
            else:
                var264 = -0.019627728
        else:
            if input[0] < 21.366615:
                if input[3] < 163.58118:
                    if input[4] < 8.081833:
                        var264 = -0.01206936
                    else:
                        var264 = -0.044178184
                else:
                    var264 = 0.004423508
            else:
                if input[4] < 8.324405:
                    if input[0] < 22.883705:
                        var264 = 0.013107264
                    else:
                        var264 = -0.00020584596
                else:
                    var264 = -0.02790445
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[4] < 8.187523:
                    if input[1] < 57.79943:
                        var265 = -0.008300086
                    else:
                        var265 = 0.0075837593
                else:
                    if input[3] < 86.07635:
                        var265 = 0.007941742
                    else:
                        var265 = -0.017919281
            else:
                if input[0] < 23.580992:
                    var265 = -0.012204487
                else:
                    var265 = 0.03779482
        else:
            if input[2] < 737.73047:
                if input[0] < 23.580992:
                    var265 = 0.026571417
                else:
                    if input[0] < 26.266321:
                        var265 = -0.032555826
                    else:
                        var265 = 0.010875159
            else:
                var265 = -0.041995205
    else:
        if input[4] < 8.230444:
            if input[0] < 26.55467:
                var265 = -0.006872037
            else:
                if input[5] < 5958.2637:
                    var265 = 0.04365108
                else:
                    var265 = -0.00005815666
        else:
            var265 = -0.017495979
    if input[0] < 20.11864:
        var266 = -0.02192802
    else:
        if input[0] < 20.865282:
            if input[1] < 81.32996:
                if input[1] < 52.434742:
                    var266 = 0.0014941002
                else:
                    if input[0] < 20.484303:
                        var266 = 0.017450517
                    else:
                        var266 = 0.041864544
            else:
                var266 = -0.018754024
        else:
            if input[0] < 21.366615:
                if input[4] < 8.081833:
                    var266 = 0.0029131405
                else:
                    var266 = -0.03971593
            else:
                if input[2] < 746.90137:
                    if input[0] < 22.883705:
                        var266 = 0.019621843
                    else:
                        var266 = 0.0008289651
                else:
                    if input[0] < 28.530838:
                        var266 = -0.0003193306
                    else:
                        var266 = -0.028975908
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[3] < 145.52826:
                    if input[3] < 140.61911:
                        var267 = -0.00073542347
                    else:
                        var267 = 0.04189867
                else:
                    if input[2] < 729.3266:
                        var267 = 0.0114585245
                    else:
                        var267 = -0.029547373
            else:
                if input[0] < 23.580992:
                    var267 = -0.011742392
                else:
                    var267 = 0.036910024
        else:
            if input[2] < 737.73047:
                if input[0] < 23.580992:
                    var267 = 0.026042799
                else:
                    if input[0] < 26.266321:
                        var267 = -0.031889133
                    else:
                        var267 = 0.010356157
            else:
                var267 = -0.041462116
    else:
        if input[5] < 4948.595:
            if input[1] < 53.759136:
                var267 = 0.03897728
            else:
                var267 = 0.008080069
        else:
            if input[2] < 748.9394:
                if input[4] < 8.177689:
                    var267 = 0.03345823
                else:
                    var267 = -0.014118175
            else:
                var267 = -0.033008102
    if input[1] < 41.845177:
        if input[0] < 23.34363:
            var268 = -0.033457514
        else:
            if input[2] < 726.6149:
                var268 = 0.015778758
            else:
                var268 = -0.013055014
    else:
        if input[1] < 43.866257:
            var268 = 0.025316974
        else:
            if input[1] < 47.42564:
                if input[4] < 8.151678:
                    if input[2] < 711.15344:
                        var268 = -0.010911285
                    else:
                        var268 = 0.016414888
                else:
                    if input[2] < 753.20294:
                        var268 = -0.03230438
                    else:
                        var268 = -0.0069268914
            else:
                if input[1] < 50.49679:
                    if input[0] < 23.958542:
                        var268 = 0.0035104025
                    else:
                        var268 = 0.030526012
                else:
                    if input[1] < 52.178165:
                        var268 = -0.025891436
                    else:
                        var268 = 0.0015086704
    if input[1] < 90.64338:
        if input[0] < 20.957043:
            if input[0] < 20.713284:
                if input[2] < 703.2164:
                    var269 = -0.015727738
                else:
                    if input[1] < 74.49065:
                        var269 = -0.0051020402
                    else:
                        var269 = 0.036791306
            else:
                var269 = 0.033383097
        else:
            if input[0] < 21.746157:
                if input[4] < 8.102652:
                    if input[1] < 63.508068:
                        var269 = -0.017857298
                    else:
                        var269 = 0.019370561
                else:
                    var269 = -0.041341726
            else:
                if input[0] < 22.883705:
                    if input[4] < 8.187523:
                        var269 = 0.032783195
                    else:
                        var269 = -0.009598689
                else:
                    if input[0] < 23.014591:
                        var269 = -0.035137173
                    else:
                        var269 = 0.001506673
    else:
        if input[1] < 91.62102:
            if input[4] < 8.132412:
                var269 = -0.0078319665
            else:
                var269 = -0.041902103
        else:
            if input[2] < 742.155:
                if input[3] < 99.609856:
                    if input[3] < 53.224903:
                        var269 = -0.007582513
                    else:
                        var269 = 0.04310059
                else:
                    if input[0] < 24.484314:
                        var269 = -0.021460306
                    else:
                        var269 = 0.011036661
            else:
                var269 = -0.03322787
    if input[1] < 90.64338:
        if input[0] < 20.957043:
            if input[0] < 20.713284:
                if input[2] < 703.2164:
                    var270 = -0.015088232
                else:
                    if input[4] < 8.142715:
                        var270 = 0.035302185
                    else:
                        var270 = -0.0057906597
            else:
                var270 = 0.032412183
        else:
            if input[0] < 21.746157:
                if input[4] < 8.102652:
                    if input[5] < 2244.283:
                        var270 = -0.004069151
                    else:
                        var270 = 0.0063741193
                else:
                    var270 = -0.040469762
            else:
                if input[0] < 22.883705:
                    if input[4] < 8.187523:
                        var270 = 0.031735446
                    else:
                        var270 = -0.009431235
                else:
                    if input[0] < 23.014591:
                        var270 = -0.034074694
                    else:
                        var270 = 0.0014287845
    else:
        if input[1] < 91.62102:
            if input[3] < 80.19552:
                var270 = -0.041143473
            else:
                var270 = -0.0073028267
        else:
            if input[2] < 742.155:
                if input[4] < 7.310009:
                    var270 = -0.0106788045
                else:
                    if input[4] < 8.215596:
                        var270 = 0.028372003
                    else:
                        var270 = -0.0035627538
            else:
                var270 = -0.032740876
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3600.7922:
                        var271 = -0.00086899765
                    else:
                        var271 = 0.02636593
                else:
                    if input[3] < 165.44615:
                        var271 = -0.03671463
                    else:
                        var271 = -0.0009663336
            else:
                var271 = 0.03152272
        else:
            if input[0] < 23.580992:
                var271 = 0.022599908
            else:
                if input[2] < 733.0016:
                    if input[2] < 462.86743:
                        var271 = -0.01876291
                    else:
                        var271 = 0.01578984
                else:
                    var271 = -0.04289086
    else:
        if input[4] < 8.230444:
            if input[0] < 27.043375:
                var271 = -0.005595501
            else:
                if input[0] < 36.260155:
                    var271 = 0.041786723
                else:
                    var271 = -0.0006677593
        else:
            var271 = -0.0171624
    if input[1] < 41.845177:
        if input[0] < 23.34363:
            var272 = -0.03217229
        else:
            if input[2] < 726.6149:
                var272 = 0.014876515
            else:
                var272 = -0.013234369
    else:
        if input[2] < 407.72763:
            if input[1] < 81.52184:
                var272 = -0.030353686
            else:
                var272 = 0.0005198183
        else:
            if input[1] < 43.866257:
                var272 = 0.02555619
            else:
                if input[1] < 47.42564:
                    if input[4] < 8.151678:
                        var272 = 0.0049760896
                    else:
                        var272 = -0.026419673
                else:
                    if input[1] < 54.039787:
                        var272 = 0.015978385
                    else:
                        var272 = 0.00007486764
    if input[1] < 90.64338:
        if input[3] < 120.56106:
            if input[3] < 115.57555:
                if input[1] < 58.03831:
                    if input[1] < 53.28753:
                        var273 = 0.0014967242
                    else:
                        var273 = -0.038781665
                else:
                    if input[1] < 66.5992:
                        var273 = 0.031576753
                    else:
                        var273 = -0.000604697
            else:
                if input[1] < 59.078312:
                    var273 = 0.02314392
                else:
                    var273 = -0.06430225
        else:
            if input[1] < 73.290535:
                if input[1] < 62.443443:
                    if input[1] < 52.178165:
                        var273 = -0.0056928694
                    else:
                        var273 = 0.023985496
                else:
                    if input[5] < 3234.9443:
                        var273 = 0.010308243
                    else:
                        var273 = -0.039765157
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var273 = 0.04616496
                    else:
                        var273 = 0.003357021
                else:
                    if input[4] < 8.112143:
                        var273 = 0.014726807
                    else:
                        var273 = -0.02427744
    else:
        if input[1] < 91.62102:
            if input[4] < 8.132412:
                var273 = -0.006948136
            else:
                var273 = -0.040464338
        else:
            if input[2] < 742.155:
                if input[3] < 95.972466:
                    if input[3] < 59.351093:
                        var273 = -0.00720623
                    else:
                        var273 = 0.04176623
                else:
                    if input[0] < 24.484314:
                        var273 = -0.021081338
                    else:
                        var273 = 0.009727761
            else:
                var273 = -0.031845715
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3912.1926:
                if input[3] < 155.53893:
                    if input[5] < 3636.057:
                        var274 = -0.0007618621
                    else:
                        var274 = 0.025677456
                else:
                    if input[0] < 22.946997:
                        var274 = -0.0026150728
                    else:
                        var274 = -0.038675807
            else:
                var274 = 0.029888961
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var274 = -0.027578607
                    else:
                        var274 = 0.01114045
                else:
                    if input[3] < 186.3421:
                        var274 = 0.03244189
                    else:
                        var274 = 0.0015000186
            else:
                var274 = -0.039695945
    else:
        if input[4] < 8.230444:
            if input[5] < 4948.595:
                var274 = 0.03815312
            else:
                if input[4] < 8.155125:
                    var274 = 0.017542193
                else:
                    var274 = -0.008884584
        else:
            var274 = -0.016752874
    if input[0] < 36.260155:
        if input[0] < 34.86882:
            if input[4] < 8.254773:
                if input[4] < 8.236438:
                    if input[5] < 4737.7285:
                        var275 = -0.0015616842
                    else:
                        var275 = 0.02243448
                else:
                    if input[1] < 86.93164:
                        var275 = -0.034213226
                    else:
                        var275 = 0.003927182
            else:
                if input[0] < 23.645546:
                    if input[3] < 130.4914:
                        var275 = 0.03924109
                    else:
                        var275 = 0.007010101
                else:
                    if input[2] < 750.9746:
                        var275 = 0.019620486
                    else:
                        var275 = -0.033658307
        else:
            if input[2] < 730.8562:
                var275 = 0.028247714
            else:
                var275 = 0.0021537652
    else:
        if input[1] < 74.49065:
            if input[5] < 2681.302:
                var275 = -0.03046777
            else:
                var275 = 0.00025169822
        else:
            if input[1] < 82.91693:
                var275 = 0.019109085
            else:
                if input[3] < 45.044186:
                    var275 = 0.0036801693
                else:
                    var275 = -0.021872755
    if input[1] < 85.865974:
        if input[1] < 85.052666:
            if input[0] < 20.804243:
                if input[5] < 1799.6632:
                    var276 = -0.0013369912
                else:
                    if input[2] < 733.0016:
                        var276 = 0.03773116
                    else:
                        var276 = 0.014349629
            else:
                if input[0] < 21.746157:
                    if input[4] < 8.102652:
                        var276 = -0.0000397714
                    else:
                        var276 = -0.039959386
                else:
                    if input[0] < 22.122957:
                        var276 = 0.031299856
                    else:
                        var276 = -0.0010023193
        else:
            if input[5] < 2645.4595:
                var276 = 0.040869135
            else:
                var276 = -0.005215287
    else:
        if input[0] < 24.414213:
            if input[4] < 8.241077:
                if input[1] < 96.06247:
                    var276 = -0.04361514
                else:
                    var276 = 0.0027840948
            else:
                var276 = 0.006756724
        else:
            if input[3] < 80.19552:
                if input[2] < 730.8562:
                    var276 = 0.016671946
                else:
                    var276 = -0.043583002
            else:
                if input[4] < 8.215596:
                    if input[4] < 8.136787:
                        var276 = 0.006199467
                    else:
                        var276 = 0.043744005
                else:
                    var276 = -0.010964186
    if input[1] < 90.64338:
        if input[0] < 20.957043:
            if input[4] < 8.206008:
                if input[4] < 8.142715:
                    if input[2] < 433.85468:
                        var277 = 0.0017779913
                    else:
                        var277 = 0.03363807
                else:
                    var277 = -0.03239601
            else:
                var277 = 0.030742077
        else:
            if input[0] < 21.746157:
                if input[4] < 8.102652:
                    var277 = 0.001879276
                else:
                    var277 = -0.037859198
            else:
                if input[0] < 22.883705:
                    if input[4] < 8.187523:
                        var277 = 0.030184973
                    else:
                        var277 = -0.009105886
                else:
                    if input[0] < 23.014591:
                        var277 = -0.031819914
                    else:
                        var277 = 0.0013082497
    else:
        if input[1] < 91.62102:
            var277 = -0.030136872
        else:
            if input[2] < 742.155:
                if input[3] < 95.972466:
                    if input[3] < 59.351093:
                        var277 = -0.0067042345
                    else:
                        var277 = 0.04056474
                else:
                    if input[0] < 24.484314:
                        var277 = -0.019759132
                    else:
                        var277 = 0.008743337
            else:
                var277 = -0.030899787
    if input[1] < 90.64338:
        if input[3] < 120.56106:
            if input[3] < 115.57555:
                if input[1] < 58.03831:
                    if input[1] < 53.28753:
                        var278 = 0.001649081
                    else:
                        var278 = -0.03720982
                else:
                    if input[1] < 66.5992:
                        var278 = 0.030256838
                    else:
                        var278 = -0.0002452562
            else:
                if input[1] < 53.759136:
                    var278 = 0.022526529
                else:
                    var278 = -0.061359804
        else:
            if input[1] < 73.290535:
                if input[1] < 62.443443:
                    if input[1] < 52.178165:
                        var278 = -0.005063434
                    else:
                        var278 = 0.02304258
                else:
                    if input[5] < 3234.9443:
                        var278 = 0.0099140955
                    else:
                        var278 = -0.038501095
            else:
                if input[3] < 171.65364:
                    if input[5] < 3955.953:
                        var278 = 0.04356083
                    else:
                        var278 = 0.0031674944
                else:
                    if input[2] < 737.73047:
                        var278 = 0.005358245
                    else:
                        var278 = -0.031359587
    else:
        if input[1] < 91.62102:
            var278 = -0.029189592
        else:
            if input[2] < 742.155:
                if input[3] < 95.972466:
                    if input[3] < 68.25924:
                        var278 = -0.0062325723
                    else:
                        var278 = 0.039595436
                else:
                    if input[0] < 24.484314:
                        var278 = -0.019264074
                    else:
                        var278 = 0.008677768
            else:
                var278 = -0.030562157
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.91044:
                if input[2] < 423.73544:
                    var279 = -0.028380027
                else:
                    if input[4] < 8.151678:
                        var279 = 0.0130925225
                    else:
                        var279 = -0.0065285936
            else:
                var279 = -0.044244435
        else:
            if input[2] < 726.6149:
                if input[2] < 717.82:
                    if input[0] < 34.571377:
                        var279 = 0.019871315
                    else:
                        var279 = -0.005143372
                else:
                    if input[5] < 3600.7922:
                        var279 = -0.040155385
                    else:
                        var279 = 0.023612086
            else:
                if input[1] < 86.296745:
                    if input[4] < 8.241077:
                        var279 = 0.049262058
                    else:
                        var279 = -0.013744111
                else:
                    if input[3] < 80.19552:
                        var279 = -0.037380643
                    else:
                        var279 = 0.015400144
    else:
        if input[1] < 63.28969:
            if input[1] < 52.178165:
                if input[5] < 3636.057:
                    var279 = -0.036720127
                else:
                    if input[1] < 45.71353:
                        var279 = 0.024030877
                    else:
                        var279 = -0.01691695
            else:
                if input[4] < 8.181944:
                    if input[5] < 3441.4753:
                        var279 = 0.05114713
                    else:
                        var279 = 0.0057664453
                else:
                    var279 = -0.008956197
        else:
            if input[1] < 73.290535:
                var279 = -0.040557135
            else:
                if input[0] < 26.754036:
                    if input[3] < 105.6937:
                        var279 = -0.019475859
                    else:
                        var279 = 0.017600961
                else:
                    if input[5] < 1630.4938:
                        var279 = -0.001455109
                    else:
                        var279 = -0.037182372
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.91044:
                if input[2] < 423.73544:
                    var280 = -0.027601926
                else:
                    if input[4] < 8.151678:
                        var280 = 0.01257073
                    else:
                        var280 = -0.0062527503
            else:
                var280 = -0.043093372
        else:
            if input[2] < 726.6149:
                if input[2] < 717.82:
                    if input[0] < 34.571377:
                        var280 = 0.01937819
                    else:
                        var280 = -0.005129226
                else:
                    if input[5] < 3600.7922:
                        var280 = -0.03877559
                    else:
                        var280 = 0.023121959
            else:
                if input[1] < 86.296745:
                    if input[4] < 8.241077:
                        var280 = 0.04833446
                    else:
                        var280 = -0.013284913
                else:
                    if input[3] < 80.19552:
                        var280 = -0.036660504
                    else:
                        var280 = 0.014961146
    else:
        if input[1] < 63.28969:
            if input[1] < 52.178165:
                if input[5] < 3636.057:
                    var280 = -0.036192212
                else:
                    if input[1] < 45.71353:
                        var280 = 0.023392288
                    else:
                        var280 = -0.016574418
            else:
                if input[4] < 8.181944:
                    if input[5] < 3441.4753:
                        var280 = 0.049424946
                    else:
                        var280 = 0.0055343015
                else:
                    var280 = -0.008647022
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var280 = 0.04351177
                    else:
                        var280 = -0.000986318
                else:
                    var280 = -0.02415557
            else:
                if input[1] < 84.55421:
                    if input[4] < 8.254773:
                        var280 = -0.040405374
                    else:
                        var280 = -0.0018849539
                else:
                    if input[3] < 139.43567:
                        var280 = -0.02569878
                    else:
                        var280 = 0.022353193
    if input[5] < 4737.7285:
        if input[4] < 8.254773:
            if input[3] < 155.53893:
                if input[3] < 139.43567:
                    if input[4] < 8.187523:
                        var281 = 0.0024683008
                    else:
                        var281 = -0.017974736
                else:
                    if input[4] < 8.151678:
                        var281 = -0.010690063
                    else:
                        var281 = 0.033209562
            else:
                if input[0] < 22.946997:
                    if input[4] < 8.081833:
                        var281 = 0.030082498
                    else:
                        var281 = -0.012605386
                else:
                    if input[1] < 75.40523:
                        var281 = -0.035998788
                    else:
                        var281 = -0.008559754
        else:
            if input[0] < 24.202885:
                if input[1] < 85.46175:
                    if input[1] < 73.290535:
                        var281 = 0.005536471
                    else:
                        var281 = 0.04086481
                else:
                    var281 = 0.0005958497
            else:
                if input[4] < 8.270223:
                    var281 = 0.013490008
                else:
                    var281 = -0.032318316
    else:
        if input[5] < 4948.595:
            var281 = 0.030966684
        else:
            if input[2] < 748.9394:
                if input[4] < 8.177689:
                    var281 = 0.031262007
                else:
                    var281 = -0.014452546
            else:
                var281 = -0.03109189
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.146177:
                if input[0] < 24.350086:
                    if input[0] < 23.812544:
                        var282 = 0.0031863288
                    else:
                        var282 = -0.030714003
                else:
                    if input[2] < 708.1484:
                        var282 = -0.0038316038
                    else:
                        var282 = 0.0424788
            else:
                if input[1] < 77.71787:
                    if input[3] < 94.150635:
                        var282 = -0.003926021
                    else:
                        var282 = -0.0565809
                else:
                    var282 = 0.028182987
        else:
            if input[2] < 726.6149:
                if input[2] < 715.4301:
                    if input[2] < 452.94366:
                        var282 = -0.000497574
                    else:
                        var282 = 0.032109156
                else:
                    if input[5] < 3600.7922:
                        var282 = -0.03736245
                    else:
                        var282 = 0.0149631
            else:
                if input[1] < 86.296745:
                    if input[4] < 8.241077:
                        var282 = 0.047713768
                    else:
                        var282 = -0.012577064
                else:
                    if input[3] < 80.19552:
                        var282 = -0.035845768
                    else:
                        var282 = 0.014627263
    else:
        if input[1] < 63.28969:
            if input[1] < 52.178165:
                if input[5] < 3636.057:
                    var282 = -0.03551115
                else:
                    if input[1] < 45.71353:
                        var282 = 0.022016171
                    else:
                        var282 = -0.016372299
            else:
                if input[4] < 8.181944:
                    if input[5] < 3441.4753:
                        var282 = 0.047703765
                    else:
                        var282 = 0.0049181576
                else:
                    var282 = -0.008659548
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var282 = 0.041522868
                    else:
                        var282 = -0.0010552703
                else:
                    var282 = -0.022993121
            else:
                if input[1] < 84.55421:
                    if input[0] < 33.817833:
                        var282 = -0.037338052
                    else:
                        var282 = 0.004924636
                else:
                    if input[3] < 139.43567:
                        var282 = -0.025180299
                    else:
                        var282 = 0.021030923
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.91044:
                if input[2] < 423.73544:
                    var283 = -0.027055994
                else:
                    if input[4] < 8.151678:
                        var283 = 0.012520445
                    else:
                        var283 = -0.0058825687
            else:
                var283 = -0.040032502
        else:
            if input[2] < 726.6149:
                if input[2] < 715.4301:
                    if input[2] < 452.94366:
                        var283 = -0.00044938936
                    else:
                        var283 = 0.031519677
                else:
                    if input[5] < 3600.7922:
                        var283 = -0.035199992
                    else:
                        var283 = 0.014039974
            else:
                if input[1] < 86.296745:
                    if input[4] < 8.241077:
                        var283 = 0.04644329
                    else:
                        var283 = -0.012158945
                else:
                    if input[4] < 8.168125:
                        var283 = -0.016694227
                    else:
                        var283 = -0.002363972
    else:
        if input[4] < 8.112143:
            if input[3] < 168.97972:
                var283 = -0.0028492906
            else:
                var283 = 0.033089858
        else:
            if input[3] < 172.44543:
                if input[5] < 3636.057:
                    if input[0] < 25.415422:
                        var283 = -0.000034149507
                    else:
                        var283 = -0.027639879
                else:
                    if input[2] < 750.9746:
                        var283 = -0.01303777
                    else:
                        var283 = 0.023847502
            else:
                var283 = -0.036480494
    if input[5] < 4737.7285:
        if input[4] < 8.254773:
            if input[3] < 155.53893:
                if input[3] < 139.43567:
                    if input[4] < 8.187523:
                        var284 = 0.0023473224
                    else:
                        var284 = -0.017537763
                else:
                    if input[4] < 8.151678:
                        var284 = -0.0100362515
                    else:
                        var284 = 0.031091068
            else:
                if input[0] < 22.946997:
                    if input[4] < 8.081833:
                        var284 = 0.028770028
                    else:
                        var284 = -0.012468419
                else:
                    if input[1] < 75.40523:
                        var284 = -0.034621526
                    else:
                        var284 = -0.008291939
        else:
            if input[0] < 25.415422:
                if input[1] < 73.290535:
                    var284 = -0.0043013017
                else:
                    if input[1] < 85.46175:
                        var284 = 0.040416267
                    else:
                        var284 = -0.00042656605
            else:
                var284 = -0.019983754
    else:
        if input[5] < 4948.595:
            var284 = 0.030035099
        else:
            if input[2] < 748.9394:
                var284 = 0.010696188
            else:
                var284 = -0.029729445
    if input[1] < 47.74073:
        if input[4] < 8.151678:
            if input[3] < 60.078743:
                var285 = -0.014645596
            else:
                if input[3] < 141.65678:
                    if input[0] < 24.631493:
                        var285 = 0.028794652
                    else:
                        var285 = 0.007648244
                else:
                    var285 = -0.010443809
        else:
            if input[5] < 3097.8657:
                var285 = -0.03485366
            else:
                if input[4] < 8.200379:
                    var285 = -0.011795878
                else:
                    var285 = 0.014981649
    else:
        if input[1] < 54.039787:
            if input[1] < 52.178165:
                if input[2] < 737.73047:
                    if input[0] < 22.014307:
                        var285 = -0.013497298
                    else:
                        var285 = 0.037518926
                else:
                    var285 = -0.02788872
            else:
                if input[0] < 24.035046:
                    var285 = 0.049744736
                else:
                    var285 = 0.009453513
        else:
            if input[2] < 750.9746:
                if input[4] < 8.254773:
                    if input[1] < 58.03831:
                        var285 = -0.020383166
                    else:
                        var285 = 0.0028267435
                else:
                    if input[1] < 73.03348:
                        var285 = -0.0032877603
                    else:
                        var285 = 0.03690689
            else:
                if input[1] < 75.110985:
                    var285 = -0.03908312
                else:
                    if input[3] < 171.65364:
                        var285 = 0.0043091746
                    else:
                        var285 = -0.026887948
    if input[5] < 4737.7285:
        if input[4] < 8.254773:
            if input[3] < 155.53893:
                if input[3] < 139.43567:
                    if input[4] < 8.187523:
                        var286 = 0.0022532495
                    else:
                        var286 = -0.01669596
                else:
                    if input[5] < 3955.953:
                        var286 = 0.025936544
                    else:
                        var286 = -0.017849255
            else:
                if input[0] < 22.946997:
                    if input[4] < 8.081833:
                        var286 = 0.027863571
                    else:
                        var286 = -0.011767293
                else:
                    if input[1] < 75.40523:
                        var286 = -0.03353562
                    else:
                        var286 = -0.007994437
        else:
            if input[0] < 25.415422:
                if input[2] < 762.44934:
                    if input[4] < 8.301448:
                        var286 = 0.03836997
                    else:
                        var286 = -0.0017478382
                else:
                    var286 = -0.007039538
            else:
                var286 = -0.020025669
    else:
        if input[5] < 4948.595:
            var286 = 0.029886771
        else:
            if input[2] < 748.9394:
                var286 = 0.010140571
            else:
                var286 = -0.028223261
    if input[5] < 4737.7285:
        if input[5] < 2320.111:
            if input[3] < 91.50338:
                if input[5] < 1864.8372:
                    if input[5] < 938.6545:
                        var287 = -0.005963926
                    else:
                        var287 = 0.010417576
                else:
                    if input[2] < 730.8562:
                        var287 = 0.0068726665
                    else:
                        var287 = -0.031883474
            else:
                if input[1] < 63.28969:
                    var287 = 0.037331115
                else:
                    var287 = 0.008105782
        else:
            if input[5] < 2511.7754:
                if input[1] < 80.43887:
                    if input[5] < 2457.2336:
                        var287 = -0.013251136
                    else:
                        var287 = -0.049760472
                else:
                    if input[2] < 739.5616:
                        var287 = 0.032616623
                    else:
                        var287 = -0.0023769157
            else:
                if input[5] < 2713.444:
                    if input[1] < 74.91183:
                        var287 = 0.03383002
                    else:
                        var287 = -0.007949404
                else:
                    if input[3] < 118.32198:
                        var287 = -0.018285953
                    else:
                        var287 = 0.0019873092
    else:
        if input[5] < 4948.595:
            var287 = 0.029168103
        else:
            if input[2] < 748.9394:
                var287 = 0.009830906
            else:
                var287 = -0.027823126
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.146177:
                if input[0] < 24.350086:
                    if input[4] < 8.254773:
                        var288 = -0.0062604113
                    else:
                        var288 = 0.034450915
                else:
                    if input[2] < 708.1484:
                        var288 = -0.004844945
                    else:
                        var288 = 0.04089987
            else:
                if input[1] < 77.71787:
                    if input[3] < 94.63197:
                        var288 = -0.0064388155
                    else:
                        var288 = -0.052159548
                else:
                    var288 = 0.026336387
        else:
            if input[2] < 726.6149:
                if input[2] < 715.4301:
                    if input[2] < 452.94366:
                        var288 = -0.000063289925
                    else:
                        var288 = 0.030730331
                else:
                    if input[5] < 3600.7922:
                        var288 = -0.03231664
                    else:
                        var288 = 0.013341804
            else:
                if input[1] < 76.9051:
                    if input[4] < 8.230444:
                        var288 = 0.050180353
                    else:
                        var288 = -0.0009866258
                else:
                    if input[5] < 2371.8145:
                        var288 = -0.0322528
                    else:
                        var288 = 0.013089
    else:
        if input[1] < 63.28969:
            if input[1] < 52.178165:
                if input[5] < 3636.057:
                    var288 = -0.033382997
                else:
                    if input[1] < 45.71353:
                        var288 = 0.019805016
                    else:
                        var288 = -0.013942577
            else:
                if input[4] < 8.181944:
                    if input[5] < 3441.4753:
                        var288 = 0.04449473
                    else:
                        var288 = 0.0044887722
                else:
                    var288 = -0.008008339
        else:
            if input[1] < 73.290535:
                var288 = -0.037319835
            else:
                if input[3] < 105.6937:
                    if input[5] < 1630.4938:
                        var288 = 0.009713663
                    else:
                        var288 = -0.038629208
                else:
                    if input[5] < 3955.953:
                        var288 = 0.022381462
                    else:
                        var288 = -0.032188922
    if input[1] < 47.74073:
        if input[4] < 8.151678:
            if input[3] < 60.078743:
                var289 = -0.014696355
            else:
                if input[0] < 25.290705:
                    var289 = 0.02592123
                else:
                    var289 = -0.0057593086
        else:
            if input[5] < 3097.8657:
                var289 = -0.033714022
            else:
                if input[2] < 748.9394:
                    var289 = -0.0073931986
                else:
                    var289 = 0.0105152605
    else:
        if input[1] < 54.039787:
            if input[0] < 21.95693:
                var289 = -0.013327593
            else:
                if input[2] < 737.73047:
                    var289 = 0.042328473
                else:
                    if input[2] < 760.2625:
                        var289 = -0.033456102
                    else:
                        var289 = 0.029790822
        else:
            if input[2] < 750.9746:
                if input[1] < 58.03831:
                    if input[3] < 94.63197:
                        var289 = -0.04181129
                    else:
                        var289 = 0.0153734265
                else:
                    if input[3] < 109.19461:
                        var289 = 0.01185639
                    else:
                        var289 = -0.005249881
            else:
                if input[1] < 75.110985:
                    var289 = -0.038026355
                else:
                    if input[0] < 22.122957:
                        var289 = 0.016367052
                    else:
                        var289 = -0.011118101
    if input[3] < 120.56106:
        if input[3] < 115.57555:
            if input[1] < 58.03831:
                if input[5] < 3061.5588:
                    if input[3] < 75.37392:
                        var290 = 0.0012576587
                    else:
                        var290 = -0.03828715
                else:
                    var290 = 0.029968483
            else:
                if input[1] < 63.28969:
                    if input[3] < 89.07573:
                        var290 = 0.0028210653
                    else:
                        var290 = 0.046314817
                else:
                    if input[2] < 739.5616:
                        var290 = 0.007996946
                    else:
                        var290 = -0.01722073
        else:
            if input[0] < 25.290705:
                if input[4] < 8.177689:
                    var290 = 0.03166403
                else:
                    var290 = -0.039641913
            else:
                var290 = -0.044486787
    else:
        if input[3] < 125.529655:
            var290 = 0.030665606
        else:
            if input[1] < 90.64338:
                if input[1] < 73.290535:
                    if input[3] < 168.97972:
                        var290 = -0.01302776
                    else:
                        var290 = 0.02002439
                else:
                    if input[3] < 171.65364:
                        var290 = 0.03011402
                    else:
                        var290 = -0.01067911
            else:
                if input[5] < 4047.857:
                    var290 = -0.029934088
                else:
                    var290 = 0.0025961197
    if input[2] < 407.72763:
        if input[5] < 2457.2336:
            var291 = -0.01721306
        else:
            var291 = -0.003817483
    else:
        if input[1] < 41.845177:
            if input[0] < 23.34363:
                var291 = -0.029285088
            else:
                if input[2] < 726.6149:
                    var291 = 0.009356438
                else:
                    var291 = -0.0078815585
        else:
            if input[2] < 742.155:
                if input[3] < 85.3771:
                    if input[3] < 80.19552:
                        var291 = 0.005281571
                    else:
                        var291 = 0.03625249
                else:
                    if input[0] < 29.823307:
                        var291 = 0.0059674405
                    else:
                        var291 = -0.016578395
            else:
                if input[1] < 63.28969:
                    if input[1] < 52.178165:
                        var291 = -0.016131759
                    else:
                        var291 = 0.022504326
                else:
                    if input[1] < 73.290535:
                        var291 = -0.03585007
                    else:
                        var291 = -0.0017820226
    if input[3] < 120.56106:
        if input[3] < 115.57555:
            if input[1] < 58.03831:
                if input[1] < 53.28753:
                    if input[3] < 75.37392:
                        var292 = 0.017266346
                    else:
                        var292 = -0.013089265
                else:
                    var292 = -0.03414315
            else:
                if input[1] < 63.28969:
                    if input[3] < 89.07573:
                        var292 = 0.0022105454
                    else:
                        var292 = 0.045161143
                else:
                    if input[2] < 739.5616:
                        var292 = 0.00775855
                    else:
                        var292 = -0.016221693
        else:
            if input[0] < 25.290705:
                if input[4] < 8.177689:
                    var292 = 0.030954072
                else:
                    var292 = -0.038887855
            else:
                var292 = -0.042835858
    else:
        if input[3] < 125.529655:
            var292 = 0.030123746
        else:
            if input[1] < 90.64338:
                if input[1] < 73.290535:
                    if input[3] < 168.97972:
                        var292 = -0.01240763
                    else:
                        var292 = 0.019229164
                else:
                    if input[3] < 171.65364:
                        var292 = 0.029318957
                    else:
                        var292 = -0.010220924
            else:
                if input[5] < 4047.857:
                    var292 = -0.029386753
                else:
                    var292 = 0.0029644396
    if input[3] < 120.56106:
        if input[3] < 115.57555:
            if input[1] < 58.03831:
                if input[5] < 3061.5588:
                    if input[3] < 75.37392:
                        var293 = 0.0007880225
                    else:
                        var293 = -0.036422264
                else:
                    var293 = 0.029392585
            else:
                if input[1] < 63.28969:
                    if input[3] < 89.07573:
                        var293 = 0.0019558342
                    else:
                        var293 = 0.04422255
                else:
                    if input[0] < 22.422846:
                        var293 = 0.022260416
                    else:
                        var293 = -0.005265948
        else:
            if input[0] < 25.290705:
                if input[4] < 8.177689:
                    var293 = 0.03044645
                else:
                    var293 = -0.03804667
            else:
                var293 = -0.041625444
    else:
        if input[3] < 152.17412:
            if input[5] < 2955.2168:
                if input[4] < 8.142715:
                    var293 = 0.016569674
                else:
                    var293 = -0.0331565
            else:
                if input[1] < 73.290535:
                    if input[2] < 746.90137:
                        var293 = 0.01752581
                    else:
                        var293 = -0.013522053
                else:
                    if input[1] < 89.73176:
                        var293 = 0.039132353
                    else:
                        var293 = 0.0013050605
        else:
            if input[3] < 165.44615:
                if input[2] < 721.7867:
                    var293 = 0.008345946
                else:
                    if input[1] < 82.106895:
                        var293 = -0.041435793
                    else:
                        var293 = -0.0010728211
            else:
                if input[1] < 86.480606:
                    if input[2] < 737.73047:
                        var293 = 0.025574429
                    else:
                        var293 = -0.0019937693
                else:
                    var293 = -0.015830897
    if input[2] < 407.72763:
        var294 = -0.014091909
    else:
        if input[1] < 85.865974:
            if input[1] < 85.052666:
                if input[0] < 20.804243:
                    if input[0] < 20.484303:
                        var294 = 0.009770027
                    else:
                        var294 = 0.0335333
                else:
                    if input[0] < 21.746157:
                        var294 = -0.026760269
                    else:
                        var294 = 0.0014051176
            else:
                if input[0] < 23.508352:
                    var294 = 0.03783088
                else:
                    var294 = 0.0033870346
        else:
            if input[0] < 24.414213:
                if input[4] < 8.241077:
                    if input[1] < 94.96665:
                        var294 = -0.03625218
                    else:
                        var294 = -0.005354883
                else:
                    var294 = 0.006890695
            else:
                if input[3] < 112.18744:
                    if input[4] < 8.12684:
                        var294 = 0.01311279
                    else:
                        var294 = -0.026041696
                else:
                    if input[5] < 4090.0388:
                        var294 = 0.032063242
                    else:
                        var294 = 0.00019833026
    if input[3] < 120.56106:
        if input[3] < 115.57555:
            if input[1] < 58.03831:
                if input[1] < 53.28753:
                    if input[3] < 75.37392:
                        var295 = 0.016393682
                    else:
                        var295 = -0.011458221
                else:
                    var295 = -0.031786222
            else:
                if input[1] < 63.28969:
                    if input[4] < 8.181944:
                        var295 = 0.03856724
                    else:
                        var295 = -0.0051906663
                else:
                    if input[2] < 739.5616:
                        var295 = 0.007090556
                    else:
                        var295 = -0.01549111
        else:
            if input[2] < 708.1484:
                var295 = -0.039526448
            else:
                if input[4] < 8.177689:
                    var295 = 0.028950578
                else:
                    var295 = -0.034250576
    else:
        if input[3] < 152.17412:
            if input[5] < 2955.2168:
                if input[4] < 8.142715:
                    var295 = 0.015964938
                else:
                    var295 = -0.032138254
            else:
                if input[1] < 73.290535:
                    if input[2] < 746.90137:
                        var295 = 0.01721121
                    else:
                        var295 = -0.012512751
                else:
                    if input[1] < 89.73176:
                        var295 = 0.037883375
                    else:
                        var295 = 0.00093382923
        else:
            if input[3] < 165.44615:
                if input[2] < 721.7867:
                    var295 = 0.008169386
                else:
                    if input[1] < 82.106895:
                        var295 = -0.040512875
                    else:
                        var295 = -0.0011325213
            else:
                if input[1] < 86.480606:
                    if input[2] < 737.73047:
                        var295 = 0.024480226
                    else:
                        var295 = -0.002161534
                else:
                    var295 = -0.014714074
    if input[2] < 407.72763:
        var296 = -0.014033876
    else:
        if input[1] < 85.865974:
            if input[1] < 85.052666:
                if input[0] < 20.804243:
                    if input[3] < 86.87295:
                        var296 = 0.002674012
                    else:
                        var296 = 0.026434842
                else:
                    if input[0] < 21.746157:
                        var296 = -0.025663475
                    else:
                        var296 = 0.0013697597
            else:
                if input[0] < 23.508352:
                    var296 = 0.03669436
                else:
                    var296 = 0.003175551
        else:
            if input[0] < 24.414213:
                if input[4] < 8.241077:
                    if input[1] < 94.96665:
                        var296 = -0.03527278
                    else:
                        var296 = -0.0053591197
                else:
                    var296 = 0.0069719055
            else:
                if input[3] < 80.19552:
                    if input[2] < 730.8562:
                        var296 = 0.014398711
                    else:
                        var296 = -0.03810412
                else:
                    if input[4] < 8.215596:
                        var296 = 0.024865307
                    else:
                        var296 = -0.013070156
    if input[5] < 4737.7285:
        if input[5] < 3955.953:
            if input[5] < 3748.7295:
                if input[5] < 3539.6162:
                    if input[5] < 3346.2974:
                        var297 = -0.0011343485
                    else:
                        var297 = 0.030543882
                else:
                    if input[2] < 756.0391:
                        var297 = -0.025231881
                    else:
                        var297 = 0.019708877
            else:
                if input[0] < 23.580992:
                    var297 = -0.007139632
                else:
                    var297 = 0.029632483
        else:
            if input[2] < 737.73047:
                if input[4] < 8.102652:
                    if input[1] < 81.73901:
                        var297 = -0.023475662
                    else:
                        var297 = 0.009673058
                else:
                    if input[3] < 186.3421:
                        var297 = 0.028492764
                    else:
                        var297 = 0.00081276085
            else:
                var297 = -0.03563887
    else:
        if input[5] < 4948.595:
            var297 = 0.028005091
        else:
            if input[4] < 8.177689:
                var297 = 0.009632791
            else:
                var297 = -0.020566499
    if input[1] < 85.865974:
        if input[1] < 85.052666:
            if input[0] < 20.804243:
                if input[5] < 1799.6632:
                    var298 = -0.00057014904
                else:
                    if input[2] < 733.0016:
                        var298 = 0.03203183
                    else:
                        var298 = 0.009485784
            else:
                if input[0] < 21.746157:
                    if input[4] < 8.102652:
                        var298 = -0.001987757
                    else:
                        var298 = -0.034680363
                else:
                    if input[1] < 55.418133:
                        var298 = 0.009118301
                    else:
                        var298 = -0.003268743
        else:
            if input[0] < 23.508352:
                var298 = 0.035393197
            else:
                var298 = 0.0026620326
    else:
        if input[0] < 24.414213:
            if input[4] < 8.241077:
                if input[1] < 95.49466:
                    var298 = -0.034814287
                else:
                    var298 = -0.00623969
            else:
                var298 = 0.006064515
        else:
            if input[3] < 80.19552:
                if input[2] < 730.8562:
                    var298 = 0.012144579
                else:
                    var298 = -0.03770906
            else:
                if input[4] < 8.215596:
                    if input[5] < 3803.4026:
                        var298 = 0.03478298
                    else:
                        var298 = 0.0046401727
                else:
                    var298 = -0.012407876
    if input[3] < 120.56106:
        if input[5] < 2832.3289:
            if input[1] < 58.03831:
                if input[1] < 54.039787:
                    if input[3] < 75.37392:
                        var299 = 0.015373446
                    else:
                        var299 = -0.014239149
                else:
                    var299 = -0.03571013
            else:
                if input[1] < 66.5992:
                    if input[3] < 76.086876:
                        var299 = 0.0033414941
                    else:
                        var299 = 0.03967018
                else:
                    if input[4] < 8.136787:
                        var299 = 0.0104308035
                    else:
                        var299 = -0.010873266
        else:
            if input[1] < 55.418133:
                var299 = 0.018344795
            else:
                if input[1] < 85.19493:
                    if input[4] < 8.065835:
                        var299 = -0.0036091965
                    else:
                        var299 = -0.045177575
                else:
                    var299 = 0.0009860072
    else:
        if input[3] < 152.17412:
            if input[5] < 2890.5234:
                if input[0] < 21.03765:
                    var299 = 0.0051179286
                else:
                    var299 = -0.025635233
            else:
                if input[2] < 758.4436:
                    if input[5] < 3234.9443:
                        var299 = 0.04064047
                    else:
                        var299 = 0.00949328
                else:
                    var299 = -0.0061999224
        else:
            if input[3] < 165.44615:
                if input[2] < 721.7867:
                    var299 = 0.007209809
                else:
                    if input[1] < 82.106895:
                        var299 = -0.0393444
                    else:
                        var299 = -0.0018455047
            else:
                if input[1] < 86.480606:
                    if input[2] < 737.73047:
                        var299 = 0.023540905
                    else:
                        var299 = -0.002346221
                else:
                    var299 = -0.013720045
    if input[2] < 407.72763:
        var300 = -0.013725206
    else:
        if input[1] < 85.865974:
            if input[1] < 85.052666:
                if input[0] < 20.804243:
                    if input[3] < 86.87295:
                        var300 = 0.0028459418
                    else:
                        var300 = 0.024660394
                else:
                    if input[0] < 21.746157:
                        var300 = -0.024150893
                    else:
                        var300 = 0.0013868161
            else:
                if input[0] < 23.508352:
                    var300 = 0.035048943
                else:
                    var300 = 0.0030461815
        else:
            if input[0] < 24.414213:
                if input[4] < 8.241077:
                    if input[1] < 94.96665:
                        var300 = -0.033534702
                    else:
                        var300 = -0.005831485
                else:
                    var300 = 0.0061780233
            else:
                if input[3] < 112.18744:
                    if input[4] < 8.12684:
                        var300 = 0.011094405
                    else:
                        var300 = -0.025114456
                else:
                    if input[4] < 8.155125:
                        var300 = -0.0003903136
                    else:
                        var300 = 0.029929891
    if input[2] < 742.155:
        if input[0] < 26.432243:
            if input[0] < 25.146177:
                if input[2] < 423.73544:
                    var301 = -0.024606949
                else:
                    if input[0] < 24.350086:
                        var301 = 0.00042837477
                    else:
                        var301 = 0.027267102
            else:
                if input[1] < 66.80687:
                    if input[1] < 50.49679:
                        var301 = -0.01083383
                    else:
                        var301 = -0.046580244
                else:
                    var301 = 0.009160092
        else:
            if input[2] < 726.6149:
                if input[2] < 715.4301:
                    if input[2] < 452.94366:
                        var301 = -0.00020837183
                    else:
                        var301 = 0.028817816
                else:
                    if input[1] < 71.01151:
                        var301 = -0.030583218
                    else:
                        var301 = 0.011324357
            else:
                if input[1] < 86.296745:
                    if input[4] < 8.215596:
                        var301 = 0.047222964
                    else:
                        var301 = 0.0018349806
                else:
                    var301 = -0.012237798
    else:
        if input[1] < 63.28969:
            if input[4] < 8.236438:
                if input[1] < 52.178165:
                    if input[4] < 8.200379:
                        var301 = -0.026062611
                    else:
                        var301 = 0.021117723
                else:
                    if input[0] < 27.350344:
                        var301 = 0.031637605
                    else:
                        var301 = 0.003299968
            else:
                var301 = -0.025965739
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var301 = 0.036250867
                    else:
                        var301 = -0.0020013247
                else:
                    var301 = -0.01951521
            else:
                if input[1] < 84.55421:
                    if input[4] < 8.254773:
                        var301 = -0.035310254
                    else:
                        var301 = 0.0012618914
                else:
                    if input[3] < 139.43567:
                        var301 = -0.020307323
                    else:
                        var301 = 0.0153790265
    if input[3] < 120.56106:
        if input[5] < 2832.3289:
            if input[1] < 58.03831:
                if input[1] < 54.039787:
                    if input[3] < 75.37392:
                        var302 = 0.014669657
                    else:
                        var302 = -0.0136702685
                else:
                    var302 = -0.034293924
            else:
                if input[1] < 66.5992:
                    if input[3] < 76.086876:
                        var302 = 0.0032074556
                    else:
                        var302 = 0.038200002
                else:
                    if input[4] < 8.136787:
                        var302 = 0.01010356
                    else:
                        var302 = -0.010502378
        else:
            if input[1] < 55.418133:
                var302 = 0.017263677
            else:
                if input[1] < 85.19493:
                    if input[4] < 8.065835:
                        var302 = -0.0034458362
                    else:
                        var302 = -0.043734394
                else:
                    var302 = 0.0004694597
    else:
        if input[3] < 152.17412:
            if input[5] < 2890.5234:
                var302 = -0.012717997
            else:
                if input[2] < 758.4436:
                    if input[5] < 3234.9443:
                        var302 = 0.03915007
                    else:
                        var302 = 0.009081437
                else:
                    var302 = -0.0058671157
        else:
            if input[3] < 165.44615:
                if input[2] < 721.7867:
                    var302 = 0.007523827
                else:
                    if input[1] < 82.106895:
                        var302 = -0.03876324
                    else:
                        var302 = -0.0018788446
            else:
                if input[0] < 27.271341:
                    if input[5] < 4359.007:
                        var302 = 0.011396438
                    else:
                        var302 = -0.023355624
                else:
                    var302 = 0.02327597
    if input[1] < 85.865974:
        if input[1] < 85.052666:
            if input[0] < 20.804243:
                if input[5] < 1799.6632:
                    var303 = -0.00034310846
                else:
                    if input[2] < 733.0016:
                        var303 = 0.030810287
                    else:
                        var303 = 0.008507802
            else:
                if input[0] < 21.746157:
                    if input[4] < 8.102652:
                        var303 = -0.0017747622
                    else:
                        var303 = -0.032854434
                else:
                    if input[0] < 22.122957:
                        var303 = 0.024600364
                    else:
                        var303 = -0.0007485226
        else:
            if input[0] < 23.508352:
                var303 = 0.033786368
            else:
                var303 = 0.0027292098
    else:
        if input[0] < 24.414213:
            if input[4] < 8.241077:
                if input[1] < 95.49466:
                    var303 = -0.03324965
                else:
                    var303 = -0.005980884
            else:
                var303 = 0.006474366
        else:
            if input[3] < 80.19552:
                if input[2] < 730.8562:
                    var303 = 0.010415824
                else:
                    var303 = -0.03616384
            else:
                if input[4] < 8.206008:
                    if input[5] < 3803.4026:
                        var303 = 0.033682078
                    else:
                        var303 = 0.001908868
                else:
                    var303 = -0.009137438
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var304 = -0.075126655
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var304 = -0.027579248
                    else:
                        var304 = -0.07023596
                else:
                    if input[5] < 4009.7493:
                        var304 = 0.06430854
                    else:
                        var304 = -0.05478443
        else:
            if input[2] < 721.7867:
                if input[0] < 21.677387:
                    if input[0] < 20.804243:
                        var304 = -0.012303113
                    else:
                        var304 = 0.04247964
                else:
                    if input[2] < 715.4301:
                        var304 = -0.06029289
                    else:
                        var304 = -0.01617717
            else:
                if input[3] < 99.609856:
                    if input[2] < 729.3266:
                        var304 = 0.059425216
                    else:
                        var304 = -0.029407298
                else:
                    if input[2] < 730.8562:
                        var304 = 0.015311256
                    else:
                        var304 = 0.09665585
    else:
        if input[2] < 753.20294:
            if input[4] < 8.168125:
                if input[1] < 55.629253:
                    var304 = 0.11460333
                else:
                    if input[5] < 3686.298:
                        var304 = -0.015810745
                    else:
                        var304 = 0.10079779
            else:
                if input[1] < 87.54926:
                    if input[0] < 34.02495:
                        var304 = 0.12014005
                    else:
                        var304 = 0.0540363
                else:
                    if input[0] < 23.580992:
                        var304 = 0.09931627
                    else:
                        var304 = -0.0003740636
        else:
            if input[4] < 8.092142:
                if input[1] < 70.87013:
                    var304 = 0.08525334
                else:
                    var304 = -0.00029406318
            else:
                if input[5] < 1387.4912:
                    var304 = 0.04247964
                else:
                    var304 = 0.14738138
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var305 = -0.07230016
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var305 = -0.02548638
                    else:
                        var305 = -0.06741324
                else:
                    if input[5] < 4009.7493:
                        var305 = 0.06316729
                    else:
                        var305 = -0.05257318
        else:
            if input[2] < 721.7867:
                if input[0] < 21.677387:
                    if input[4] < 8.181944:
                        var305 = 0.04315728
                    else:
                        var305 = -0.012033201
                else:
                    if input[2] < 715.4301:
                        var305 = -0.057933804
                    else:
                        var305 = -0.014646383
            else:
                if input[3] < 99.609856:
                    if input[2] < 729.3266:
                        var305 = 0.05527512
                    else:
                        var305 = -0.028946802
                else:
                    if input[2] < 730.8562:
                        var305 = 0.013832017
                    else:
                        var305 = 0.08881122
    else:
        if input[2] < 753.20294:
            if input[4] < 8.168125:
                if input[1] < 54.21738:
                    var305 = 0.1109057
                else:
                    if input[3] < 141.65678:
                        var305 = -0.014747711
                    else:
                        var305 = 0.08099517
            else:
                if input[5] < 3912.1926:
                    var305 = 0.10339023
                else:
                    if input[5] < 3955.953:
                        var305 = -0.049442884
                    else:
                        var305 = 0.097190164
        else:
            if input[4] < 8.092142:
                if input[1] < 70.87013:
                    var305 = 0.07841063
                else:
                    var305 = -0.0006942956
            else:
                if input[5] < 1387.4912:
                    var305 = 0.039618544
                else:
                    var305 = 0.12784502
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var306 = -0.06982203
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var306 = -0.023434242
                    else:
                        var306 = -0.064875565
                else:
                    if input[5] < 4009.7493:
                        var306 = 0.0621663
                    else:
                        var306 = -0.050503444
        else:
            if input[2] < 715.4301:
                if input[0] < 21.677387:
                    var306 = 0.010701489
                else:
                    if input[1] < 77.32407:
                        var306 = -0.06573093
                    else:
                        var306 = -0.022978125
            else:
                if input[0] < 22.199833:
                    if input[4] < 8.236438:
                        var306 = 0.09612864
                    else:
                        var306 = 0.038240343
                else:
                    if input[4] < 8.2596:
                        var306 = -0.0035024208
                    else:
                        var306 = 0.08507907
    else:
        if input[2] < 750.9746:
            if input[1] < 58.03831:
                if input[5] < 4781.7534:
                    var306 = 0.10693496
                else:
                    var306 = 0.030488914
            else:
                if input[5] < 3955.953:
                    if input[4] < 8.168125:
                        var306 = -0.014615177
                    else:
                        var306 = 0.065939076
                else:
                    var306 = 0.110359155
        else:
            if input[2] < 768.4635:
                if input[4] < 8.092142:
                    var306 = -0.0020640863
                else:
                    if input[3] < 139.43567:
                        var306 = 0.10994249
                    else:
                        var306 = 0.07724101
            else:
                if input[5] < 1387.4912:
                    var306 = 0.037018828
                else:
                    var306 = 0.114743225
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var307 = -0.06764348
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var307 = -0.02142114
                    else:
                        var307 = -0.062580414
                else:
                    if input[5] < 4009.7493:
                        var307 = 0.061284192
                    else:
                        var307 = -0.048559282
        else:
            if input[2] < 715.4301:
                if input[0] < 21.677387:
                    var307 = 0.011333837
                else:
                    if input[1] < 77.32407:
                        var307 = -0.06377481
                    else:
                        var307 = -0.021275893
            else:
                if input[0] < 22.199833:
                    var307 = 0.07533683
                else:
                    if input[4] < 8.2596:
                        var307 = -0.0035198256
                    else:
                        var307 = 0.079759724
    else:
        if input[2] < 750.9746:
            if input[4] < 8.206008:
                if input[1] < 54.21738:
                    if input[5] < 3600.7922:
                        var307 = 0.09445424
                    else:
                        var307 = 0.026939074
                else:
                    if input[5] < 3686.298:
                        var307 = 0.00021836009
                    else:
                        var307 = 0.07303389
            else:
                if input[2] < 748.9394:
                    if input[5] < 2058.9133:
                        var307 = 0.036922004
                    else:
                        var307 = 0.10589305
                else:
                    if input[3] < 130.4914:
                        var307 = -0.011726573
                    else:
                        var307 = 0.04482672
        else:
            if input[2] < 768.4635:
                if input[4] < 8.092142:
                    var307 = -0.0033083674
                else:
                    if input[3] < 139.43567:
                        var307 = 0.09998174
                    else:
                        var307 = 0.06984325
            else:
                if input[5] < 1387.4912:
                    var307 = 0.034645308
                else:
                    var307 = 0.10383345
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var308 = -0.06572549
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var308 = -0.019445332
                    else:
                        var308 = -0.060491305
                else:
                    if input[5] < 4009.7493:
                        var308 = 0.06050333
                    else:
                        var308 = -0.046726175
        else:
            if input[2] < 715.4301:
                if input[0] < 21.677387:
                    var308 = 0.012164622
                else:
                    if input[1] < 77.32407:
                        var308 = -0.061886813
                    else:
                        var308 = -0.019427406
            else:
                if input[1] < 47.42564:
                    var308 = 0.08155018
                else:
                    if input[0] < 22.199833:
                        var308 = 0.07083876
                    else:
                        var308 = -0.002687
    else:
        if input[2] < 750.9746:
            if input[4] < 8.168125:
                if input[1] < 54.21738:
                    var308 = 0.08461455
                else:
                    if input[5] < 3686.298:
                        var308 = -0.018735189
                    else:
                        var308 = 0.065317914
            else:
                if input[4] < 8.301448:
                    if input[4] < 8.254773:
                        var308 = 0.073056765
                    else:
                        var308 = -0.0024489725
                else:
                    var308 = 0.09256846
        else:
            if input[2] < 768.4635:
                if input[4] < 8.092142:
                    var308 = -0.0044421908
                else:
                    if input[3] < 139.43567:
                        var308 = 0.09207141
                    else:
                        var308 = 0.06358463
            else:
                if input[5] < 1387.4912:
                    var308 = 0.03246882
                else:
                    var308 = 0.09534683
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var309 = -0.06403265
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var309 = -0.017508391
                    else:
                        var309 = -0.05857861
                else:
                    if input[5] < 4009.7493:
                        var309 = 0.059803255
                    else:
                        var309 = -0.044993054
        else:
            if input[2] < 715.4301:
                if input[0] < 21.677387:
                    var309 = 0.012831072
                else:
                    if input[1] < 77.32407:
                        var309 = -0.060232352
                    else:
                        var309 = -0.017756708
            else:
                if input[5] < 2759.4326:
                    if input[0] < 21.280195:
                        var309 = 0.0746629
                    else:
                        var309 = -0.01875021
                else:
                    if input[2] < 730.8562:
                        var309 = 0.005664879
                    else:
                        var309 = 0.08275073
    else:
        if input[2] < 750.9746:
            if input[1] < 58.03831:
                if input[0] < 26.043957:
                    var309 = 0.08854997
                else:
                    if input[4] < 8.181944:
                        var309 = -0.026834005
                    else:
                        var309 = 0.07302643
            else:
                if input[5] < 3955.953:
                    if input[4] < 8.168125:
                        var309 = -0.015940042
                    else:
                        var309 = 0.050116368
                else:
                    var309 = 0.09176491
        else:
            if input[2] < 768.4635:
                if input[4] < 8.092142:
                    var309 = -0.005473119
                else:
                    if input[3] < 139.43567:
                        var309 = 0.08560839
                    else:
                        var309 = 0.058113035
            else:
                if input[5] < 1387.4912:
                    var309 = 0.030465124
                else:
                    var309 = 0.08859346
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var310 = -0.06253501
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var310 = -0.015613379
                    else:
                        var310 = -0.056817003
                else:
                    if input[3] < 163.58118:
                        var310 = 0.0737044
                    else:
                        var310 = -0.028825436
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var310 = 0.009838655
                    else:
                        var310 = -0.059891444
                else:
                    if input[4] < 8.193557:
                        var310 = 0.02141138
                    else:
                        var310 = -0.040683385
            else:
                if input[1] < 47.42564:
                    var310 = 0.0772442
                else:
                    if input[1] < 65.79639:
                        var310 = -0.017936742
                    else:
                        var310 = 0.036865328
    else:
        if input[2] < 753.20294:
            if input[5] < 1556.7986:
                var310 = -0.027535899
            else:
                if input[1] < 58.03831:
                    if input[5] < 4781.7534:
                        var310 = 0.080904864
                    else:
                        var310 = 0.016583161
                else:
                    if input[1] < 63.28969:
                        var310 = -0.02801809
                    else:
                        var310 = 0.050602954
        else:
            if input[4] < 8.092142:
                if input[1] < 70.87013:
                    var310 = 0.052868523
                else:
                    var310 = -0.0058217063
            else:
                if input[2] < 768.4635:
                    if input[1] < 53.759136:
                        var310 = 0.04653187
                    else:
                        var310 = 0.07921843
                else:
                    if input[5] < 1387.4912:
                        var310 = 0.02861393
                    else:
                        var310 = 0.08311493
    if input[2] < 737.73047:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var311 = -0.061205585
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var311 = -0.013757142
                    else:
                        var311 = -0.055180766
                else:
                    if input[5] < 4009.7493:
                        var311 = 0.060088664
                    else:
                        var311 = -0.04233891
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var311 = 0.010047991
                    else:
                        var311 = -0.05840711
                else:
                    if input[0] < 25.845655:
                        var311 = 0.022520985
                    else:
                        var311 = -0.03978775
            else:
                if input[5] < 2759.4326:
                    if input[0] < 21.280195:
                        var311 = 0.07038728
                    else:
                        var311 = -0.018356586
                else:
                    if input[2] < 730.8562:
                        var311 = 0.0051347422
                    else:
                        var311 = 0.076326385
    else:
        if input[2] < 753.20294:
            if input[5] < 1556.7986:
                var311 = -0.02719216
            else:
                if input[1] < 58.03831:
                    if input[5] < 4781.7534:
                        var311 = 0.07661201
                    else:
                        var311 = 0.014820284
                else:
                    if input[1] < 63.28969:
                        var311 = -0.027438134
                    else:
                        var311 = 0.046581138
        else:
            if input[2] < 768.4635:
                if input[0] < 20.484303:
                    var311 = -0.007211176
                else:
                    if input[4] < 8.236438:
                        var311 = 0.04888536
                    else:
                        var311 = 0.079626836
            else:
                if input[5] < 1387.4912:
                    var311 = 0.026898215
                else:
                    var311 = 0.078634635
    if input[2] < 733.0016:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var312 = -0.060023557
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var312 = -0.005188584
                    else:
                        var312 = -0.05228142
                else:
                    if input[5] < 4009.7493:
                        var312 = 0.049931284
                    else:
                        var312 = -0.03824446
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var312 = 0.0100481305
                    else:
                        var312 = -0.05720007
                else:
                    if input[5] < 2972.1619:
                        var312 = -0.03888545
                    else:
                        var312 = 0.02299568
            else:
                if input[1] < 45.71353:
                    var312 = 0.06284736
                else:
                    if input[5] < 4149.554:
                        var312 = 0.015311986
                    else:
                        var312 = -0.057775676
    else:
        if input[2] < 750.9746:
            if input[4] < 8.206008:
                if input[2] < 742.155:
                    if input[0] < 24.350086:
                        var312 = 0.033622507
                    else:
                        var312 = -0.040008
                else:
                    if input[3] < 168.97972:
                        var312 = 0.042928997
                    else:
                        var312 = -0.02537145
            else:
                if input[2] < 748.9394:
                    if input[5] < 2545.023:
                        var312 = 0.024010235
                    else:
                        var312 = 0.08469874
                else:
                    if input[3] < 130.4914:
                        var312 = -0.023111036
                    else:
                        var312 = 0.029810403
        else:
            if input[2] < 768.4635:
                if input[3] < 139.43567:
                    if input[0] < 21.101826:
                        var312 = 0.0044179186
                    else:
                        var312 = 0.072895974
                else:
                    if input[3] < 172.44543:
                        var312 = 0.020223252
                    else:
                        var312 = 0.075972125
            else:
                if input[5] < 1387.4912:
                    var312 = 0.025303563
                else:
                    var312 = 0.07489034
    if input[2] < 733.0016:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var313 = -0.058972806
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var313 = -0.0035850224
                    else:
                        var313 = -0.05078127
                else:
                    if input[5] < 4009.7493:
                        var313 = 0.049835395
                    else:
                        var313 = -0.03684149
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var313 = 0.010039389
                    else:
                        var313 = -0.05608514
                else:
                    if input[0] < 25.845655:
                        var313 = 0.023241056
                    else:
                        var313 = -0.037887525
            else:
                if input[1] < 45.71353:
                    var313 = 0.06110676
                else:
                    if input[5] < 4149.554:
                        var313 = 0.015016704
                    else:
                        var313 = -0.055889424
    else:
        if input[2] < 750.9746:
            if input[4] < 8.206008:
                if input[3] < 145.07802:
                    if input[5] < 2972.1619:
                        var313 = 0.0128615
                    else:
                        var313 = -0.051678687
                else:
                    if input[3] < 168.97972:
                        var313 = 0.0664668
                    else:
                        var313 = -0.010243933
            else:
                if input[2] < 748.9394:
                    if input[5] < 1556.7986:
                        var313 = -0.0138146
                    else:
                        var313 = 0.072935596
                else:
                    if input[3] < 130.4914:
                        var313 = -0.023629121
                    else:
                        var313 = 0.027898679
        else:
            if input[2] < 768.4635:
                if input[3] < 139.43567:
                    if input[0] < 21.101826:
                        var313 = 0.0033946272
                    else:
                        var313 = 0.069493346
                else:
                    if input[4] < 8.247992:
                        var313 = 0.013047995
                    else:
                        var313 = 0.06615305
            else:
                if input[5] < 1387.4912:
                    var313 = 0.02381771
                else:
                    var313 = 0.071733736
    if input[2] < 733.0016:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var314 = -0.058033615
            else:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var314 = 0.010236052
                    else:
                        var314 = -0.054889936
                else:
                    if input[5] < 2972.1619:
                        var314 = -0.03696486
                    else:
                        var314 = 0.024095869
        else:
            if input[4] < 8.092142:
                if input[5] < 3483.7427:
                    var314 = -0.055456784
                else:
                    var314 = -0.0054226187
            else:
                if input[0] < 21.280195:
                    if input[0] < 20.804243:
                        var314 = -0.0006248723
                    else:
                        var314 = 0.0804865
                else:
                    if input[1] < 45.71353:
                        var314 = 0.047109548
                    else:
                        var314 = -0.01193124
    else:
        if input[2] < 753.20294:
            if input[4] < 8.081833:
                if input[5] < 3686.298:
                    if input[1] < 77.56267:
                        var314 = -0.055582523
                    else:
                        var314 = 0.00073016965
                else:
                    var314 = 0.05370754
            else:
                if input[3] < 155.53893:
                    if input[4] < 8.168125:
                        var314 = 0.0028205279
                    else:
                        var314 = 0.041041493
                else:
                    if input[3] < 188.35179:
                        var314 = 0.067867
                    else:
                        var314 = 0.020920368
        else:
            if input[2] < 768.4635:
                if input[4] < 8.236438:
                    if input[1] < 53.759136:
                        var314 = -0.018309595
                    else:
                        var314 = 0.05504176
                else:
                    if input[0] < 20.865282:
                        var314 = 0.013330932
                    else:
                        var314 = 0.06996485
            else:
                if input[5] < 1387.4912:
                    var314 = 0.022430152
                else:
                    var314 = 0.0690541
    if input[2] < 733.0016:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var315 = -0.057191122
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var315 = 0.000103203136
                    else:
                        var315 = -0.048435535
                else:
                    if input[5] < 4009.7493:
                        var315 = 0.04950927
                    else:
                        var315 = -0.035510432
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var315 = 0.01119075
                    else:
                        var315 = -0.053568583
                else:
                    if input[4] < 8.193557:
                        var315 = 0.025399158
                    else:
                        var315 = -0.03583851
            else:
                if input[1] < 65.92256:
                    if input[1] < 45.71353:
                        var315 = 0.05656485
                    else:
                        var315 = -0.017428104
                else:
                    if input[5] < 3577.9521:
                        var315 = 0.08494171
                    else:
                        var315 = -0.05328868
    else:
        if input[2] < 753.20294:
            if input[4] < 8.301448:
                if input[1] < 58.03831:
                    if input[0] < 26.110664:
                        var315 = 0.06470133
                    else:
                        var315 = -0.011972751
                else:
                    if input[5] < 3955.953:
                        var315 = -0.001897249
                    else:
                        var315 = 0.07091166
            else:
                var315 = 0.06842562
        else:
            if input[2] < 768.4635:
                if input[4] < 8.236438:
                    if input[1] < 53.759136:
                        var315 = -0.018703973
                    else:
                        var315 = 0.052256133
                else:
                    if input[0] < 20.865282:
                        var315 = 0.0118925385
                    else:
                        var315 = 0.067467466
            else:
                if input[5] < 1387.4912:
                    var315 = 0.021131761
                else:
                    var315 = 0.066761784
    if input[2] < 733.0016:
        if input[4] < 8.151678:
            if input[2] < 715.4301:
                var316 = -0.05643622
            else:
                if input[3] < 152.17412:
                    if input[5] < 1674.2129:
                        var316 = 0.0012005407
                    else:
                        var316 = -0.047281567
                else:
                    if input[5] < 4009.7493:
                        var316 = 0.04832175
                    else:
                        var316 = -0.034808625
        else:
            if input[2] < 715.4301:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var316 = 0.011813368
                    else:
                        var316 = -0.052320536
                else:
                    if input[0] < 25.845655:
                        var316 = 0.026873175
                    else:
                        var316 = -0.034915235
            else:
                if input[1] < 65.92256:
                    if input[1] < 45.71353:
                        var316 = 0.05407694
                    else:
                        var316 = -0.01664648
                else:
                    if input[5] < 3577.9521:
                        var316 = 0.0796977
                    else:
                        var316 = -0.051971734
    else:
        if input[2] < 753.20294:
            if input[4] < 8.081833:
                if input[5] < 3686.298:
                    if input[1] < 77.56267:
                        var316 = -0.05430884
                    else:
                        var316 = 0.00061387423
                else:
                    var316 = 0.0498834
            else:
                if input[3] < 155.53893:
                    if input[1] < 58.03831:
                        var316 = 0.050570667
                    else:
                        var316 = 0.010667533
                else:
                    if input[3] < 188.35179:
                        var316 = 0.062143724
                    else:
                        var316 = 0.018275077
        else:
            if input[2] < 768.4635:
                if input[4] < 8.236438:
                    if input[1] < 53.759136:
                        var316 = -0.019007314
                    else:
                        var316 = 0.049697265
                else:
                    if input[0] < 20.865282:
                        var316 = 0.010546613
                    else:
                        var316 = 0.06529792
            else:
                if input[5] < 1387.4912:
                    var316 = 0.019914893
                else:
                    var316 = 0.06478784
    if input[2] < 730.8562:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var317 = -0.055758215
            else:
                if input[0] < 21.677387:
                    var317 = 0.021750344
                else:
                    if input[1] < 77.32407:
                        var317 = -0.050242264
                    else:
                        var317 = -0.006715073
        else:
            if input[4] < 8.092142:
                if input[2] < 729.3266:
                    var317 = -0.05282362
                else:
                    var317 = 0.0063163335
            else:
                if input[2] < 729.3266:
                    if input[5] < 3671.9841:
                        var317 = 0.030551976
                    else:
                        var317 = -0.014329718
                else:
                    if input[1] < 53.28753:
                        var317 = 0.0036628896
                    else:
                        var317 = -0.05700895
    else:
        if input[2] < 753.20294:
            if input[4] < 8.112143:
                if input[5] < 3686.298:
                    if input[0] < 20.383661:
                        var317 = 0.0024537812
                    else:
                        var317 = -0.05727759
                else:
                    if input[5] < 4202.73:
                        var317 = 0.06203869
                    else:
                        var317 = -0.015329956
            else:
                if input[3] < 155.53893:
                    if input[5] < 3748.7295:
                        var317 = 0.02838786
                    else:
                        var317 = -0.025256038
                else:
                    if input[1] < 81.93888:
                        var317 = 0.071573526
                    else:
                        var317 = 0.025919935
        else:
            if input[2] < 768.4635:
                if input[4] < 8.236438:
                    if input[1] < 53.759136:
                        var317 = -0.019115327
                    else:
                        var317 = 0.04732239
                else:
                    if input[0] < 20.865282:
                        var317 = 0.00926061
                    else:
                        var317 = 0.06340858
            else:
                if input[5] < 1387.4912:
                    var317 = 0.018772736
                else:
                    var317 = 0.0630781
    if input[2] < 730.8562:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var318 = -0.05514983
            else:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var318 = 0.0131190615
                    else:
                        var318 = -0.050633915
                else:
                    if input[5] < 2972.1619:
                        var318 = -0.03351405
                    else:
                        var318 = 0.028991658
        else:
            if input[4] < 8.092142:
                if input[2] < 729.3266:
                    var318 = -0.051667523
                else:
                    var318 = 0.007569284
            else:
                if input[2] < 729.3266:
                    if input[1] < 71.01151:
                        var318 = 0.029034412
                    else:
                        var318 = -0.0163017
                else:
                    if input[1] < 53.28753:
                        var318 = 0.0033593737
                    else:
                        var318 = -0.055441458
    else:
        if input[2] < 753.20294:
            if input[4] < 8.301448:
                if input[1] < 94.16656:
                    if input[1] < 58.03831:
                        var318 = 0.036817558
                    else:
                        var318 = -0.0032079
                else:
                    if input[0] < 21.746157:
                        var318 = 0.022513576
                    else:
                        var318 = 0.07865765
            else:
                var318 = 0.06366599
        else:
            if input[2] < 768.4635:
                if input[4] < 8.236438:
                    if input[3] < 138.7908:
                        var318 = 0.052171946
                    else:
                        var318 = -0.00807378
                else:
                    if input[0] < 20.865282:
                        var318 = 0.0080566015
                    else:
                        var318 = 0.061742432
            else:
                if input[5] < 1387.4912:
                    var318 = 0.017699359
                else:
                    var318 = 0.061589535
    if input[2] < 730.8562:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var319 = -0.054597445
            else:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var319 = 0.01292489
                    else:
                        var319 = -0.04988391
                else:
                    if input[4] < 8.193557:
                        var319 = 0.028901577
                    else:
                        var319 = -0.032804538
        else:
            if input[4] < 8.092142:
                if input[2] < 729.3266:
                    var319 = -0.05073644
                else:
                    var319 = 0.008303283
            else:
                if input[1] < 45.71353:
                    if input[1] < 41.25898:
                        var319 = 0.00066662446
                    else:
                        var319 = 0.07807534
                else:
                    if input[5] < 3671.9841:
                        var319 = 0.009928129
                    else:
                        var319 = -0.044658694
    else:
        if input[2] < 756.0391:
            if input[4] < 8.112143:
                if input[5] < 3686.298:
                    if input[0] < 20.383661:
                        var319 = 0.0016140739
                    else:
                        var319 = -0.059381463
                else:
                    if input[5] < 4202.73:
                        var319 = 0.060706925
                    else:
                        var319 = -0.015576451
            else:
                if input[3] < 155.53893:
                    if input[5] < 3748.7295:
                        var319 = 0.02790368
                    else:
                        var319 = -0.034432862
                else:
                    if input[1] < 81.93888:
                        var319 = 0.068169825
                    else:
                        var319 = 0.022124058
        else:
            if input[2] < 768.4635:
                if input[0] < 20.484303:
                    var319 = -0.01937183
                else:
                    if input[1] < 53.759136:
                        var319 = 0.01843016
                    else:
                        var319 = 0.05649906
            else:
                if input[5] < 1387.4912:
                    var319 = 0.016689535
                else:
                    var319 = 0.060287546
    if input[2] < 730.8562:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var320 = -0.054098792
            else:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var320 = 0.012374986
                    else:
                        var320 = -0.049337894
                else:
                    if input[0] < 25.845655:
                        var320 = 0.028401857
                    else:
                        var320 = -0.03236058
        else:
            if input[4] < 8.092142:
                if input[2] < 729.3266:
                    var320 = -0.049845386
                else:
                    var320 = 0.008991115
            else:
                if input[2] < 729.3266:
                    if input[5] < 3671.9841:
                        var320 = 0.03033132
                    else:
                        var320 = -0.0115225455
                else:
                    if input[1] < 53.28753:
                        var320 = 0.002857823
                    else:
                        var320 = -0.053762347
    else:
        if input[2] < 756.0391:
            if input[4] < 8.301448:
                if input[1] < 90.64338:
                    if input[1] < 58.03831:
                        var320 = 0.032052655
                    else:
                        var320 = -0.0059626764
                else:
                    if input[4] < 8.241077:
                        var320 = 0.06215657
                    else:
                        var320 = -0.010111039
            else:
                var320 = 0.060819905
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var320 = -0.00541614
                    else:
                        var320 = 0.051504113
                else:
                    var320 = 0.061010994
            else:
                if input[5] < 1387.4912:
                    var320 = 0.015738642
                else:
                    var320 = 0.059144
    if input[2] < 730.8562:
        if input[2] < 715.4301:
            if input[4] < 8.151678:
                var321 = -0.053645957
            else:
                if input[1] < 77.32407:
                    if input[1] < 41.25898:
                        var321 = 0.011836025
                    else:
                        var321 = -0.048817452
                else:
                    if input[4] < 8.193557:
                        var321 = 0.027997648
                    else:
                        var321 = -0.03201118
        else:
            if input[4] < 8.092142:
                if input[2] < 729.3266:
                    var321 = -0.04898965
                else:
                    var321 = 0.0096316375
            else:
                if input[2] < 729.3266:
                    if input[1] < 45.71353:
                        var321 = 0.054872155
                    else:
                        var321 = 0.0067389207
                else:
                    if input[1] < 53.28753:
                        var321 = 0.0025670212
                    else:
                        var321 = -0.052530855
    else:
        if input[2] < 756.0391:
            if input[4] < 8.301448:
                if input[1] < 94.16656:
                    if input[3] < 155.53893:
                        var321 = 0.001741861
                    else:
                        var321 = 0.039222714
                else:
                    if input[0] < 21.746157:
                        var321 = 0.019281982
                    else:
                        var321 = 0.072239235
            else:
                var321 = 0.05927637
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var321 = -0.0065012374
                    else:
                        var321 = 0.04995734
                else:
                    var321 = 0.0595739
            else:
                if input[5] < 1387.4912:
                    var321 = 0.014842555
                else:
                    var321 = 0.058135808
    if input[2] < 730.8562:
        if input[2] < 700.4231:
            if input[4] < 8.151678:
                var322 = -0.053500373
            else:
                if input[1] < 75.110985:
                    var322 = -0.042194255
                else:
                    var322 = 0.008662077
        else:
            if input[4] < 8.16224:
                if input[3] < 152.17412:
                    if input[2] < 703.2164:
                        var322 = 0.0052747536
                    else:
                        var322 = -0.042131227
                else:
                    if input[5] < 4009.7493:
                        var322 = 0.03590503
                    else:
                        var322 = -0.03250592
            else:
                if input[0] < 21.677387:
                    if input[0] < 20.804243:
                        var322 = 0.00051578693
                    else:
                        var322 = 0.07080788
                else:
                    if input[0] < 29.62127:
                        var322 = -0.024131697
                    else:
                        var322 = 0.025140965
    else:
        if input[2] < 756.0391:
            if input[4] < 8.301448:
                if input[1] < 90.64338:
                    if input[1] < 58.03831:
                        var322 = 0.030088333
                    else:
                        var322 = -0.00661954
                else:
                    if input[4] < 8.241077:
                        var322 = 0.05783489
                    else:
                        var322 = -0.011853016
            else:
                var322 = 0.057822656
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[0] < 27.78382:
                        var322 = 0.033570036
                    else:
                        var322 = -0.051086374
                else:
                    var322 = 0.058303304
            else:
                if input[5] < 1387.4912:
                    var322 = 0.013997585
                else:
                    var322 = 0.057243813
    if input[2] < 730.8562:
        if input[2] < 700.4231:
            if input[4] < 8.151678:
                var323 = -0.053148277
            else:
                if input[1] < 75.110985:
                    var323 = -0.041042976
                else:
                    var323 = 0.00985089
        else:
            if input[5] < 2457.2336:
                if input[1] < 57.79943:
                    if input[2] < 724.7756:
                        var323 = -0.033226456
                    else:
                        var323 = 0.06417993
                else:
                    var323 = -0.052584566
            else:
                if input[5] < 3748.7295:
                    if input[2] < 726.6149:
                        var323 = 0.036671586
                    else:
                        var323 = -0.02769638
                else:
                    if input[1] < 51.355244:
                        var323 = 0.009632355
                    else:
                        var323 = -0.044177044
    else:
        if input[2] < 768.4635:
            if input[4] < 8.301448:
                if input[1] < 94.16656:
                    if input[4] < 8.046498:
                        var323 = -0.048405185
                    else:
                        var323 = 0.016196216
                else:
                    if input[4] < 8.12684:
                        var323 = 0.01206132
                    else:
                        var323 = 0.06718855
            else:
                var323 = 0.057527132
        else:
            if input[5] < 1387.4912:
                var323 = 0.01320041
            else:
                var323 = 0.056451995
    if input[2] < 724.7756:
        if input[4] < 8.102652:
            if input[4] < 8.065835:
                var324 = -0.05285988
            else:
                if input[1] < 61.794598:
                    var324 = 0.004036157
                else:
                    var324 = -0.041980524
        else:
            if input[5] < 2545.023:
                if input[4] < 8.230444:
                    var324 = -0.05182266
                else:
                    var324 = 0.0068973745
            else:
                if input[3] < 116.54727:
                    var324 = 0.09070079
                else:
                    if input[0] < 21.677387:
                        var324 = 0.03456002
                    else:
                        var324 = -0.028926993
    else:
        if input[2] < 756.0391:
            if input[4] < 8.301448:
                if input[3] < 150.02435:
                    if input[4] < 8.112143:
                        var324 = -0.048497245
                    else:
                        var324 = 0.0104952995
                else:
                    if input[1] < 75.110985:
                        var324 = 0.056569315
                    else:
                        var324 = 0.0054823295
            else:
                var324 = 0.05609398
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var324 = -0.011268563
                    else:
                        var324 = 0.046349443
                else:
                    var324 = 0.056224436
            else:
                if input[5] < 1387.4912:
                    var324 = 0.012448032
                else:
                    var324 = 0.055746913
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var325 = -0.052537467
            else:
                if input[2] < 703.2164:
                    var325 = 0.009446722
                else:
                    var325 = -0.044534203
        else:
            if input[1] < 77.32407:
                if input[1] < 41.25898:
                    var325 = 0.014352927
                else:
                    var325 = -0.045730237
            else:
                if input[5] < 3019.7021:
                    var325 = 0.03757711
                else:
                    var325 = -0.010099108
    else:
        if input[2] < 756.0391:
            if input[4] < 8.092142:
                if input[5] < 3686.298:
                    if input[1] < 85.703255:
                        var325 = -0.056162067
                    else:
                        var325 = 0.0077086277
                else:
                    if input[1] < 52.722603:
                        var325 = -0.007195081
                    else:
                        var325 = 0.05687393
            else:
                if input[0] < 21.81601:
                    if input[4] < 8.12684:
                        var325 = -0.041148525
                    else:
                        var325 = 0.05662747
                else:
                    if input[4] < 8.301448:
                        var325 = 0.0071040913
                    else:
                        var325 = 0.05460751
        else:
            if input[2] < 768.4635:
                if input[0] < 28.530838:
                    if input[4] < 8.236438:
                        var325 = -0.011632672
                    else:
                        var325 = 0.0451314
                else:
                    var325 = 0.055021454
            else:
                if input[5] < 1387.4912:
                    var325 = 0.011737698
                else:
                    var325 = 0.055117108
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var326 = -0.052270975
            else:
                if input[2] < 703.2164:
                    var326 = 0.010841086
                else:
                    var326 = -0.043718528
        else:
            if input[4] < 8.193557:
                if input[0] < 25.845655:
                    if input[5] < 3019.7021:
                        var326 = 0.083219
                    else:
                        var326 = -0.010768968
                else:
                    var326 = -0.037944157
            else:
                var326 = -0.04397156
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[5] < 3686.298:
                    if input[1] < 82.52746:
                        var326 = -0.05600309
                    else:
                        var326 = -0.0015210101
                else:
                    if input[0] < 26.754036:
                        var326 = 0.05827449
                    else:
                        var326 = -0.0025359737
            else:
                if input[4] < 8.285472:
                    if input[1] < 90.64338:
                        var326 = 0.010916802
                    else:
                        var326 = 0.038519952
                else:
                    if input[0] < 23.276815:
                        var326 = 0.015615662
                    else:
                        var326 = 0.055737823
        else:
            if input[5] < 1387.4912:
                var326 = 0.0110669285
            else:
                var326 = 0.05455282
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var327 = -0.05202793
            else:
                if input[2] < 703.2164:
                    var327 = 0.012193623
                else:
                    var327 = -0.04289395
        else:
            if input[4] < 8.193557:
                if input[0] < 25.845655:
                    if input[5] < 3019.7021:
                        var327 = 0.08015575
                    else:
                        var327 = -0.00974162
                else:
                    var327 = -0.03712752
            else:
                var327 = -0.043074116
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[5] < 3686.298:
                    if input[1] < 82.52746:
                        var327 = -0.055185445
                    else:
                        var327 = -0.0009446936
                else:
                    if input[1] < 52.722603:
                        var327 = -0.007768561
                    else:
                        var327 = 0.053731527
            else:
                if input[4] < 8.285472:
                    if input[0] < 21.81601:
                        var327 = 0.038610633
                    else:
                        var327 = 0.0103808865
                else:
                    if input[0] < 23.276815:
                        var327 = 0.013924206
                    else:
                        var327 = 0.054831296
        else:
            if input[5] < 1387.4912:
                var327 = 0.01043338
            else:
                var327 = 0.054045636
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var328 = -0.051806696
            else:
                if input[2] < 703.2164:
                    var328 = 0.013504039
                else:
                    var328 = -0.04205814
        else:
            if input[1] < 77.32407:
                if input[1] < 41.845177:
                    var328 = 0.01100262
                else:
                    var328 = -0.043639842
            else:
                if input[5] < 3019.7021:
                    var328 = 0.03846393
                else:
                    var328 = -0.00660168
    else:
        if input[2] < 768.4635:
            if input[4] < 8.092142:
                if input[5] < 3686.298:
                    if input[1] < 82.52746:
                        var328 = -0.05452171
                    else:
                        var328 = -0.0006676717
                else:
                    if input[0] < 26.754036:
                        var328 = 0.05520158
                    else:
                        var328 = -0.0026625062
            else:
                if input[4] < 8.285472:
                    if input[0] < 36.260155:
                        var328 = 0.009817446
                    else:
                        var328 = 0.039512366
                else:
                    if input[0] < 23.276815:
                        var328 = 0.012363376
                    else:
                        var328 = 0.053886306
        else:
            if input[5] < 1387.4912:
                var328 = 0.009834932
            else:
                var328 = 0.053588312
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var329 = -0.051602453
            else:
                if input[2] < 703.2164:
                    var329 = 0.0147721395
                else:
                    var329 = -0.041209374
        else:
            if input[4] < 8.193557:
                if input[0] < 25.845655:
                    if input[5] < 3019.7021:
                        var329 = 0.077655084
                    else:
                        var329 = -0.007589154
                else:
                    var329 = -0.035685092
            else:
                var329 = -0.041815642
    else:
        if input[2] < 768.4635:
            if input[4] < 8.285472:
                if input[4] < 8.092142:
                    if input[5] < 3686.298:
                        var329 = -0.04294704
                    else:
                        var329 = 0.036878686
                else:
                    if input[0] < 21.81601:
                        var329 = 0.036891352
                    else:
                        var329 = 0.008843861
            else:
                if input[0] < 23.276815:
                    if input[1] < 73.61156:
                        var329 = -0.021169461
                    else:
                        var329 = 0.03907527
                else:
                    var329 = 0.053115953
        else:
            if input[5] < 1387.4912:
                var329 = 0.009269617
            else:
                var329 = 0.053174514
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var330 = -0.05141325
            else:
                if input[2] < 703.2164:
                    var330 = 0.015675746
                else:
                    var330 = -0.040411394
        else:
            if input[4] < 8.193557:
                if input[0] < 25.845655:
                    if input[5] < 3019.7021:
                        var330 = 0.075398386
                    else:
                        var330 = -0.0063985377
                else:
                    var330 = -0.03479039
            else:
                var330 = -0.04085369
    else:
        if input[2] < 768.4635:
            if input[4] < 8.285472:
                if input[3] < 43.021126:
                    var330 = -0.053323694
                else:
                    if input[0] < 36.260155:
                        var330 = 0.005295003
                    else:
                        var330 = 0.04462152
            else:
                if input[0] < 23.276815:
                    if input[2] < 750.9746:
                        var330 = -0.021520304
                    else:
                        var330 = 0.037940677
                else:
                    var330 = 0.05235563
        else:
            if input[5] < 1387.4912:
                var330 = 0.00873558
            else:
                var330 = 0.05279872
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var331 = -0.051238902
            else:
                if input[2] < 703.2164:
                    var331 = 0.016868897
                else:
                    var331 = -0.03953497
        else:
            if input[4] < 8.193557:
                if input[0] < 25.845655:
                    if input[5] < 3019.7021:
                        var331 = 0.072698794
                    else:
                        var331 = -0.005617796
                else:
                    var331 = -0.03407295
            else:
                var331 = -0.040071234
    else:
        if input[2] < 768.4635:
            if input[4] < 8.285472:
                if input[1] < 90.64338:
                    if input[1] < 80.01135:
                        var331 = 0.008806824
                    else:
                        var331 = -0.018761016
                else:
                    if input[3] < 65.86718:
                        var331 = 0.069859944
                    else:
                        var331 = 0.019919237
            else:
                if input[0] < 23.276815:
                    if input[1] < 73.61156:
                        var331 = -0.021999627
                    else:
                        var331 = 0.036984053
                else:
                    var331 = 0.05168006
        else:
            if input[5] < 1387.4912:
                var331 = 0.007996332
            else:
                var331 = 0.052460164
    if input[2] < 715.4301:
        if input[4] < 8.151678:
            if input[2] < 700.4231:
                var332 = -0.051076908
            else:
                if input[2] < 703.2164:
                    var332 = 0.018019827
                else:
                    var332 = -0.0386437
        else:
            if input[1] < 77.32407:
                if input[1] < 41.845177:
                    var332 = 0.012366983
                else:
                    var332 = -0.04146454
            else:
                if input[5] < 3019.7021:
                    var332 = 0.039434735
                else:
                    var332 = -0.0023716295
    else:
        if input[2] < 768.4635:
            if input[4] < 8.285472:
                if input[1] < 90.64338:
                    if input[1] < 80.01135:
                        var332 = 0.008193974
                    else:
                        var332 = -0.018115675
                else:
                    if input[3] < 65.86718:
                        var332 = 0.06792253
                    else:
                        var332 = 0.019053383
            else:
                if input[0] < 23.276815:
                    if input[1] < 73.61156:
                        var332 = -0.021988854
                    else:
                        var332 = 0.036201406
                else:
                    var332 = 0.05100357
        else:
            if input[5] < 1387.4912:
                var332 = 0.00753134
            else:
                var332 = 0.052145958
    if input[2] < 715.4301:
        if input[2] < 691.64557:
            var333 = -0.050956674
        else:
            if input[0] < 26.432243:
                if input[0] < 25.742085:
                    if input[4] < 8.16224:
                        var333 = -0.03944799
                    else:
                        var333 = 0.017546516
                else:
                    var333 = 0.061038632
            else:
                var333 = -0.043029785
    else:
        if input[2] < 768.4635:
            if input[4] < 8.285472:
                if input[3] < 43.021126:
                    var333 = -0.052165117
                else:
                    if input[0] < 36.260155:
                        var333 = 0.0040206965
                    else:
                        var333 = 0.041838806
            else:
                if input[0] < 23.276815:
                    if input[2] < 750.9746:
                        var333 = -0.02241161
                    else:
                        var333 = 0.035395354
                else:
                    var333 = 0.050373193
        else:
            if input[5] < 1387.4912:
                var333 = 0.0070923003
            else:
                var333 = 0.051856764
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var334 = -0.05078199
        else:
            if input[1] < 75.110985:
                var334 = -0.033793923
            else:
                var334 = 0.0149077
    else:
        if input[2] < 768.4635:
            if input[2] < 737.73047:
                if input[5] < 2713.444:
                    if input[1] < 57.79943:
                        var334 = 0.0064054183
                    else:
                        var334 = -0.032948487
                else:
                    if input[1] < 55.418133:
                        var334 = -0.017192384
                    else:
                        var334 = 0.024861818
            else:
                if input[1] < 93.82345:
                    if input[4] < 8.301448:
                        var334 = 0.008609306
                    else:
                        var334 = 0.047467925
                else:
                    if input[4] < 8.12684:
                        var334 = 0.007249412
                    else:
                        var334 = 0.058027513
        else:
            if input[5] < 1387.4912:
                var334 = 0.006677825
            else:
                var334 = 0.05158914
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var335 = -0.050644606
        else:
            if input[1] < 75.110985:
                var335 = -0.033304058
            else:
                var335 = 0.014958249
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var335 = -0.050938424
            else:
                if input[0] < 36.260155:
                    if input[4] < 8.301448:
                        var335 = 0.003441259
                    else:
                        var335 = 0.03962651
                else:
                    if input[2] < 737.73047:
                        var335 = 0.005999801
                    else:
                        var335 = 0.057866674
        else:
            if input[5] < 1387.4912:
                var335 = 0.0062866034
            else:
                var335 = 0.05133996
    if input[4] < 8.065835:
        if input[2] < 729.3266:
            var336 = -0.05063166
        else:
            if input[5] < 3686.298:
                if input[2] < 748.9394:
                    var336 = -0.039126486
                else:
                    var336 = 0.011245529
            else:
                var336 = 0.041268207
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var336 = -0.04979795
            else:
                if input[0] < 36.260155:
                    if input[0] < 26.970547:
                        var336 = 0.0136335185
                    else:
                        var336 = -0.006489474
                else:
                    if input[2] < 737.73047:
                        var336 = 0.008516519
                    else:
                        var336 = 0.054916322
        else:
            if input[5] < 1387.4912:
                var336 = 0.005917353
            else:
                var336 = 0.051104065
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var337 = -0.05038875
        else:
            if input[1] < 75.110985:
                var337 = -0.03260697
            else:
                var337 = 0.015381932
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var337 = -0.0487317
            else:
                if input[0] < 36.260155:
                    if input[4] < 8.301448:
                        var337 = 0.0031897377
                    else:
                        var337 = 0.03752401
                else:
                    if input[2] < 737.73047:
                        var337 = 0.006574744
                    else:
                        var337 = 0.056075793
        else:
            if input[5] < 1387.4912:
                var337 = 0.0055689625
            else:
                var337 = 0.050886136
    if input[4] < 8.065835:
        if input[2] < 729.3266:
            var338 = -0.05039814
        else:
            if input[5] < 3686.298:
                if input[2] < 748.9394:
                    var338 = -0.038424633
                else:
                    var338 = 0.010022278
            else:
                var338 = 0.039515108
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var338 = -0.04776788
            else:
                if input[5] < 3346.2974:
                    if input[5] < 2698.7034:
                        var338 = 0.004148856
                    else:
                        var338 = 0.038132347
                else:
                    if input[3] < 152.17412:
                        var338 = -0.0276913
                    else:
                        var338 = 0.01585394
        else:
            if input[5] < 1387.4912:
                var338 = 0.005240314
            else:
                var338 = 0.05067366
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var339 = -0.05014902
        else:
            if input[0] < 25.051813:
                var339 = -0.032929074
            else:
                var339 = 0.0153631745
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var339 = -0.046734657
            else:
                if input[0] < 36.260155:
                    if input[0] < 34.02495:
                        var339 = 0.0074363425
                    else:
                        var339 = -0.027191052
                else:
                    if input[2] < 737.73047:
                        var339 = 0.007457994
                    else:
                        var339 = 0.054998267
        else:
            if input[5] < 1387.4912:
                var339 = 0.004930302
            else:
                var339 = 0.05047507
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var340 = -0.050030805
        else:
            if input[0] < 25.051813:
                var340 = -0.0320185
            else:
                var340 = 0.015797889
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var340 = -0.045829203
            else:
                if input[0] < 36.260155:
                    if input[5] < 4798.541:
                        var340 = 0.007303366
                    else:
                        var340 = -0.024899416
                else:
                    if input[2] < 737.73047:
                        var340 = 0.006550965
                    else:
                        var340 = 0.053952854
        else:
            if input[5] < 1387.4912:
                var340 = 0.0046380144
            else:
                var340 = 0.050279982
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var341 = -0.049913805
        else:
            if input[1] < 75.110985:
                var341 = -0.03130892
            else:
                var341 = 0.016734602
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var341 = -0.044933636
            else:
                if input[0] < 36.260155:
                    if input[0] < 34.02495:
                        var341 = 0.0068568373
                    else:
                        var341 = -0.02617015
                else:
                    if input[2] < 737.73047:
                        var341 = 0.0067788586
                    else:
                        var341 = 0.053238507
        else:
            if input[5] < 1387.4912:
                var341 = 0.004362473
            else:
                var341 = 0.050089337
    if input[2] < 700.4231:
        if input[2] < 691.64557:
            var342 = -0.04984357
        else:
            if input[3] < 116.54727:
                var342 = 0.019979516
            else:
                var342 = -0.032652333
    else:
        if input[2] < 768.4635:
            if input[5] < 1556.7986:
                if input[5] < 1348.266:
                    if input[4] < 8.168125:
                        var342 = -0.033358373
                    else:
                        var342 = 0.04797385
                else:
                    var342 = -0.055697013
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var342 = 0.010860134
                    else:
                        var342 = 0.06414115
                else:
                    if input[2] < 703.2164:
                        var342 = 0.060038984
                    else:
                        var342 = 0.0035033033
        else:
            if input[5] < 1387.4912:
                var342 = 0.0041026506
            else:
                var342 = 0.049901217
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var343 = -0.049677365
        else:
            if input[1] < 75.110985:
                var343 = -0.030239591
            else:
                var343 = 0.017313765
    else:
        if input[2] < 768.4635:
            if input[4] < 8.301448:
                if input[3] < 172.44543:
                    if input[3] < 168.97972:
                        var343 = 0.0033945048
                    else:
                        var343 = -0.062742785
                else:
                    if input[4] < 8.112143:
                        var343 = -0.04527517
                    else:
                        var343 = 0.039874814
            else:
                if input[2] < 733.0016:
                    var343 = -0.01068726
                else:
                    var343 = 0.04488393
        else:
            if input[5] < 1387.4912:
                var343 = 0.003857928
            else:
                var343 = 0.049713932
    if input[2] < 691.64557:
        var344 = -0.049599376
    else:
        if input[2] < 768.4635:
            if input[5] < 1556.7986:
                if input[5] < 1348.266:
                    if input[4] < 8.168125:
                        var344 = -0.032877784
                    else:
                        var344 = 0.046772163
                else:
                    var344 = -0.054691114
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var344 = 0.009866565
                    else:
                        var344 = 0.062233813
                else:
                    if input[5] < 2292.848:
                        var344 = -0.013624373
                    else:
                        var344 = 0.008058269
        else:
            if input[5] < 1387.4912:
                var344 = 0.003626968
            else:
                var344 = 0.0495256
    var345 = var304 + var305 + var306 + var307 + var308 + var309 + var310 + var311 + var312 + var313 + var314 + var315 + var316 + var317 + var318 + var319 + var320 + var321 + var322 + var323 + var324 + var325 + var326 + var327 + var328 + var329 + var330 + var331 + var332 + var333 + var334 + var335 + var336 + var337 + var338 + var339 + var340 + var341 + var342 + var343 + var344
    if input[4] < 8.0126295:
        var346 = -0.049581286
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var346 = -0.042097952
            else:
                if input[0] < 37.22879:
                    if input[0] < 26.266321:
                        var346 = 0.010193644
                    else:
                        var346 = -0.006110984
                else:
                    if input[2] < 737.73047:
                        var346 = 0.009593188
                    else:
                        var346 = 0.048540704
        else:
            if input[5] < 1387.4912:
                var346 = 0.0034098278
            else:
                var346 = 0.049334824
    if input[2] < 691.64557:
        var347 = -0.049351826
    else:
        if input[2] < 768.4635:
            if input[4] < 8.301448:
                if input[5] < 4798.541:
                    if input[3] < 171.65364:
                        var347 = 0.0018354481
                    else:
                        var347 = 0.040667016
                else:
                    if input[5] < 4887.909:
                        var347 = -0.08077909
                    else:
                        var347 = 0.013745806
            else:
                if input[2] < 733.0016:
                    var347 = -0.010761406
                else:
                    var347 = 0.043581113
        else:
            if input[5] < 1387.4912:
                var347 = 0.0025153863
            else:
                var347 = 0.049142223
    if input[4] < 8.0126295:
        var348 = -0.04932713
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var348 = -0.04119231
            else:
                if input[0] < 36.260155:
                    if input[0] < 34.02495:
                        var348 = 0.0050681806
                    else:
                        var348 = -0.026294384
                else:
                    if input[2] < 737.73047:
                        var348 = 0.004007533
                    else:
                        var348 = 0.05094835
        else:
            if input[5] < 1387.4912:
                var348 = 0.0014626879
            else:
                var348 = 0.048944782
    if input[4] < 8.0126295:
        var349 = -0.04918949
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var349 = -0.04042204
            else:
                if input[0] < 36.260155:
                    if input[0] < 26.970547:
                        var349 = 0.0082306
                    else:
                        var349 = -0.008720498
                else:
                    if input[2] < 737.73047:
                        var349 = 0.003984343
                    else:
                        var349 = 0.050318707
        else:
            if input[5] < 1387.4912:
                var349 = 0.0004604568
            else:
                var349 = 0.04874062
    if input[2] < 691.64557:
        var350 = -0.048942067
    else:
        if input[2] < 768.4635:
            if input[4] < 8.301448:
                if input[5] < 4798.541:
                    if input[3] < 171.65364:
                        var350 = 0.001484701
                    else:
                        var350 = 0.03843401
                else:
                    if input[5] < 4887.909:
                        var350 = -0.07710337
                    else:
                        var350 = 0.0133318845
            else:
                if input[2] < 733.0016:
                    var350 = -0.011333108
                else:
                    var350 = 0.042827602
        else:
            if input[5] < 1387.4912:
                var350 = -0.0004921469
            else:
                var350 = 0.04852852
    if input[2] < 691.64557:
        var351 = -0.04879155
    else:
        if input[2] < 768.4635:
            if input[5] < 1556.7986:
                if input[5] < 1348.266:
                    if input[3] < 47.4293:
                        var351 = -0.017059227
                    else:
                        var351 = 0.036027543
                else:
                    var351 = -0.053699404
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var351 = 0.0104505485
                    else:
                        var351 = 0.061235905
                else:
                    if input[5] < 2292.848:
                        var351 = -0.014388709
                    else:
                        var351 = 0.0066570416
        else:
            if input[5] < 1387.4912:
                var351 = -0.0013970765
            else:
                var351 = 0.04830677
    if input[4] < 8.0126295:
        var352 = -0.048762996
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var352 = -0.039342362
            else:
                if input[5] < 1799.6632:
                    if input[4] < 8.241077:
                        var352 = 0.046573844
                    else:
                        var352 = -0.04220774
                else:
                    if input[5] < 2292.848:
                        var352 = -0.018107465
                    else:
                        var352 = 0.0064802133
        else:
            if input[5] < 1387.4912:
                var352 = -0.002254522
            else:
                var352 = 0.048074402
    if input[4] < 8.0126295:
        var353 = -0.04858844
    else:
        if input[2] < 768.4635:
            if input[4] < 8.301448:
                if input[5] < 4798.541:
                    if input[3] < 171.65364:
                        var353 = 0.001212225
                    else:
                        var353 = 0.035378654
                else:
                    if input[5] < 4887.909:
                        var353 = -0.074542694
                    else:
                        var353 = 0.013944052
            else:
                if input[2] < 733.0016:
                    var353 = -0.01045585
                else:
                    var353 = 0.042027384
        else:
            if input[5] < 1387.4912:
                var353 = -0.0030658792
            else:
                var353 = 0.047829926
    if input[2] < 691.64557:
        var354 = -0.04830017
    else:
        if input[2] < 768.4635:
            if input[1] < 47.42564:
                if input[3] < 152.17412:
                    if input[3] < 142.28612:
                        var354 = 0.022165297
                    else:
                        var354 = -0.051896263
                else:
                    var354 = 0.057820547
            else:
                if input[1] < 54.039787:
                    if input[0] < 27.120234:
                        var354 = 0.010522649
                    else:
                        var354 = -0.063724115
                else:
                    if input[5] < 2698.7034:
                        var354 = -0.007891572
                    else:
                        var354 = 0.01303745
        else:
            if input[5] < 1387.4912:
                var354 = -0.0034768481
            else:
                var354 = 0.04757961
    if input[4] < 8.0126295:
        var355 = -0.048245702
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var355 = -0.038522996
            else:
                if input[5] < 1799.6632:
                    if input[4] < 8.241077:
                        var355 = 0.045541883
                    else:
                        var355 = -0.04092563
                else:
                    if input[5] < 2292.848:
                        var355 = -0.017156253
                    else:
                        var355 = 0.0056717186
        else:
            if input[5] < 1387.4912:
                var355 = -0.004204429
            else:
                var355 = 0.047307514
    if input[4] < 8.0126295:
        var356 = -0.048042327
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 2713.444:
                    if input[1] < 58.03831:
                        var356 = 0.025362426
                    else:
                        var356 = -0.015673712
                else:
                    if input[0] < 24.574257:
                        var356 = 0.0069738156
                    else:
                        var356 = 0.05001254
            else:
                if input[3] < 152.17412:
                    if input[0] < 26.754036:
                        var356 = -0.06628485
                    else:
                        var356 = -0.006117509
                else:
                    if input[1] < 48.006947:
                        var356 = 0.055805285
                    else:
                        var356 = 0.0017687755
        else:
            if input[5] < 1387.4912:
                var356 = -0.0038511266
            else:
                var356 = 0.047027558
    if input[2] < 691.64557:
        var357 = -0.047757115
    else:
        if input[2] < 768.4635:
            if input[3] < 43.021126:
                var357 = -0.037398238
            else:
                if input[0] < 36.260155:
                    if input[5] < 4798.541:
                        var357 = 0.0037049612
                    else:
                        var357 = -0.024977367
                else:
                    if input[2] < 737.73047:
                        var357 = 0.0052680597
                    else:
                        var357 = 0.04791897
        else:
            if input[5] < 1387.4912:
                var357 = -0.0040272633
            else:
                var357 = 0.04673242
    if input[4] < 8.0126295:
        var358 = -0.04766793
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var358 = -0.037370473
            else:
                if input[0] < 36.260155:
                    if input[0] < 34.02495:
                        var358 = 0.0036741283
                    else:
                        var358 = -0.025575021
                else:
                    if input[2] < 737.73047:
                        var358 = 0.0051251855
                    else:
                        var358 = 0.047112536
        else:
            if input[5] < 1387.4912:
                var358 = -0.0048420834
            else:
                var358 = 0.046418317
    if input[2] < 691.64557:
        var359 = -0.04732972
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 2713.444:
                    if input[1] < 58.03831:
                        var359 = 0.025036005
                    else:
                        var359 = -0.014523487
                else:
                    if input[2] < 708.1484:
                        var359 = 0.083862595
                    else:
                        var359 = 0.018708393
            else:
                if input[3] < 152.17412:
                    if input[0] < 26.754036:
                        var359 = -0.06346847
                    else:
                        var359 = -0.005951297
                else:
                    if input[1] < 48.006947:
                        var359 = 0.054368377
                    else:
                        var359 = 0.0019091944
        else:
            if input[0] < 22.122957:
                var359 = -0.0010479052
            else:
                var359 = 0.047010045
    if input[4] < 8.0126295:
        var360 = -0.04724769
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var360 = -0.036640078
            else:
                if input[3] < 71.83606:
                    if input[4] < 8.136787:
                        var360 = -0.021065919
                    else:
                        var360 = 0.033972118
                else:
                    if input[5] < 2698.7034:
                        var360 = -0.012556418
                    else:
                        var360 = 0.0063498192
        else:
            if input[5] < 1387.4912:
                var360 = -0.0062577263
            else:
                var360 = 0.045754205
    if input[4] < 8.0126295:
        var361 = -0.04702013
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 2713.444:
                    if input[1] < 58.03831:
                        var361 = 0.022862015
                    else:
                        var361 = -0.013341242
                else:
                    if input[0] < 25.540907:
                        var361 = 0.010347041
                    else:
                        var361 = 0.053430427
            else:
                if input[3] < 152.17412:
                    if input[0] < 26.754036:
                        var361 = -0.05980693
                    else:
                        var361 = -0.0063865916
                else:
                    if input[1] < 48.006947:
                        var361 = 0.052393466
                    else:
                        var361 = 0.0011961529
        else:
            if input[0] < 22.122957:
                var361 = -0.003494959
            else:
                var361 = 0.046329908
    if input[2] < 691.64557:
        var362 = -0.046707176
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 3076.746:
                    if input[4] < 8.102652:
                        var362 = -0.04349681
                    else:
                        var362 = 0.0076318816
                else:
                    if input[0] < 25.146177:
                        var362 = 0.0055639665
                    else:
                        var362 = 0.083934195
            else:
                if input[3] < 152.17412:
                    if input[4] < 8.247992:
                        var362 = -0.032270823
                    else:
                        var362 = 0.035426445
                else:
                    if input[1] < 48.006947:
                        var362 = 0.05128168
                    else:
                        var362 = 0.0011239225
        else:
            if input[0] < 22.122957:
                var362 = -0.0038912222
            else:
                var362 = 0.0459395
    if input[2] < 691.64557:
        var363 = -0.046472266
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 3076.746:
                    if input[4] < 8.102652:
                        var363 = -0.0430425
                    else:
                        var363 = 0.007343882
                else:
                    if input[0] < 25.146177:
                        var363 = 0.005408206
                    else:
                        var363 = 0.0824075
            else:
                if input[3] < 152.17412:
                    if input[0] < 26.754036:
                        var363 = -0.055991095
                    else:
                        var363 = -0.0050748405
                else:
                    if input[1] < 48.006947:
                        var363 = 0.049873125
                    else:
                        var363 = 0.0010014996
        else:
            if input[5] < 1387.4912:
                var363 = -0.008167825
            else:
                var363 = 0.044639602
    if input[2] < 691.64557:
        var364 = -0.04622954
    else:
        if input[2] < 768.4635:
            if input[5] < 1556.7986:
                if input[5] < 1348.266:
                    var364 = 0.0152464835
                else:
                    var364 = -0.04925595
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var364 = 0.009446911
                    else:
                        var364 = 0.057629347
                else:
                    if input[3] < 62.92014:
                        var364 = -0.03266107
                    else:
                        var364 = 0.0029432806
        else:
            if input[0] < 22.122957:
                var364 = -0.006027372
            else:
                var364 = 0.045157474
    if input[4] < 8.0126295:
        var365 = -0.04604811
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var365 = -0.035617486
            else:
                if input[5] < 1799.6632:
                    if input[4] < 8.241077:
                        var365 = 0.04340629
                    else:
                        var365 = -0.03751002
                else:
                    if input[5] < 2292.848:
                        var365 = -0.01650389
                    else:
                        var365 = 0.0047554355
        else:
            if input[5] < 1387.4912:
                var365 = -0.009868651
            else:
                var365 = 0.043854266
    if input[2] < 691.64557:
        var366 = -0.045703884
    else:
        if input[4] < 8.324405:
            if input[5] < 1556.7986:
                if input[4] < 8.241077:
                    if input[4] < 8.181944:
                        var366 = -0.036570225
                    else:
                        var366 = 0.036521237
                else:
                    var366 = -0.05891475
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var366 = 0.007863243
                    else:
                        var366 = 0.05603792
                else:
                    if input[5] < 2292.848:
                        var366 = -0.013368236
                    else:
                        var366 = 0.005152528
        else:
            if input[2] < 733.0016:
                var366 = -0.010014317
            else:
                var366 = 0.04382331
    if input[4] < 8.0126295:
        var367 = -0.04552966
    else:
        if input[2] < 768.4635:
            if input[5] < 3346.2974:
                if input[5] < 3076.746:
                    if input[4] < 8.142715:
                        var367 = -0.018593116
                    else:
                        var367 = 0.01003525
                else:
                    if input[0] < 25.146177:
                        var367 = 0.0049890834
                    else:
                        var367 = 0.080617696
            else:
                if input[5] < 3539.6162:
                    if input[2] < 721.7867:
                        var367 = -0.007215017
                    else:
                        var367 = -0.049783427
                else:
                    if input[5] < 3600.7922:
                        var367 = 0.062343538
                    else:
                        var367 = -0.0053385007
        else:
            if input[0] < 22.122957:
                var367 = -0.008394763
            else:
                var367 = 0.043892648
    if input[2] < 691.64557:
        var368 = -0.045133155
    else:
        if input[2] < 768.4635:
            if input[3] < 120.56106:
                if input[5] < 2748.8748:
                    if input[1] < 58.03831:
                        var368 = 0.020967288
                    else:
                        var368 = -0.0114136925
                else:
                    if input[1] < 55.418133:
                        var368 = -0.026036127
                    else:
                        var368 = 0.057208877
            else:
                if input[0] < 23.221859:
                    if input[4] < 8.12684:
                        var368 = -0.02416662
                    else:
                        var368 = 0.03281201
                else:
                    if input[5] < 3955.953:
                        var368 = -0.039383855
                    else:
                        var368 = 0.0067030513
        else:
            if input[0] < 22.122957:
                var368 = -0.00859837
            else:
                var368 = 0.04345232
    if input[4] < 8.0126295:
        var369 = -0.0448965
    else:
        if input[2] < 796.5425:
            if input[5] < 1556.7986:
                if input[3] < 48.872616:
                    if input[3] < 43.822132:
                        var369 = -0.028891817
                    else:
                        var369 = 0.0366291
                else:
                    if input[1] < 68.04463:
                        var369 = -0.0066098734
                    else:
                        var369 = -0.055602968
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var369 = 0.007815708
                    else:
                        var369 = 0.05677655
                else:
                    if input[3] < 62.92014:
                        var369 = -0.031066705
                    else:
                        var369 = 0.0031253377
        else:
            var369 = 0.040020395
    if input[2] < 691.64557:
        var370 = -0.044480443
    else:
        if input[2] < 796.5425:
            if input[1] < 90.64338:
                if input[3] < 62.92014:
                    if input[1] < 79.53029:
                        var370 = -0.037092905
                    else:
                        var370 = 0.017773736
                else:
                    if input[3] < 73.62454:
                        var370 = 0.03941683
                    else:
                        var370 = -0.0005973227
            else:
                if input[2] < 742.155:
                    if input[1] < 92.5334:
                        var370 = 0.047017638
                    else:
                        var370 = -0.017523948
                else:
                    var370 = 0.047241803
        else:
            var370 = 0.03946595
    if input[4] < 8.0126295:
        var371 = -0.04426733
    else:
        if input[4] < 8.324405:
            if input[5] < 1556.7986:
                if input[4] < 8.241077:
                    if input[4] < 8.181944:
                        var371 = -0.03473843
                    else:
                        var371 = 0.03302583
                else:
                    var371 = -0.05358853
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var371 = 0.007530781
                    else:
                        var371 = 0.055825144
                else:
                    if input[5] < 2292.848:
                        var371 = -0.013719044
                    else:
                        var371 = 0.004601866
        else:
            if input[2] < 733.0016:
                var371 = -0.010497506
            else:
                var371 = 0.041714765
    if input[2] < 691.64557:
        var372 = -0.043847833
    else:
        if input[2] < 768.4635:
            if input[5] < 3636.057:
                if input[5] < 3539.6162:
                    if input[5] < 3346.2974:
                        var372 = 0.0065438747
                    else:
                        var372 = -0.04105727
                else:
                    if input[1] < 54.21738:
                        var372 = 0.0015098128
                    else:
                        var372 = 0.061761048
            else:
                if input[3] < 152.17412:
                    if input[0] < 36.583706:
                        var372 = -0.044409826
                    else:
                        var372 = 0.024866624
                else:
                    if input[4] < 8.155125:
                        var372 = 0.02709045
                    else:
                        var372 = -0.0054434403
        else:
            if input[5] < 1387.4912:
                var372 = -0.010390283
            else:
                var372 = 0.040866267
    if input[4] < 8.0126295:
        var373 = -0.0435883
    else:
        if input[2] < 796.5425:
            if input[1] < 90.64338:
                if input[1] < 73.290535:
                    if input[4] < 8.236438:
                        var373 = -0.0012116972
                    else:
                        var373 = 0.03579929
                else:
                    if input[4] < 8.254773:
                        var373 = 0.00071338407
                    else:
                        var373 = -0.05073765
            else:
                if input[2] < 729.3266:
                    if input[5] < 3671.9841:
                        var373 = 0.009498081
                    else:
                        var373 = -0.038183592
                else:
                    if input[4] < 8.241077:
                        var373 = 0.038438313
                    else:
                        var373 = -0.007916805
        else:
            var373 = 0.037552156
    if input[2] < 691.64557:
        var374 = -0.043187585
    else:
        if input[2] < 796.5425:
            if input[5] < 3636.057:
                if input[5] < 3539.6162:
                    if input[5] < 3346.2974:
                        var374 = 0.0063657225
                    else:
                        var374 = -0.03836141
                else:
                    if input[1] < 54.21738:
                        var374 = 0.0022387283
                    else:
                        var374 = 0.05991145
            else:
                if input[3] < 152.17412:
                    if input[4] < 8.247992:
                        var374 = -0.040894806
                    else:
                        var374 = 0.03001234
                else:
                    if input[4] < 8.155125:
                        var374 = 0.025973683
                    else:
                        var374 = -0.004825606
        else:
            var374 = 0.036992203
    if input[2] < 691.64557:
        var375 = -0.042816844
    else:
        if input[2] < 796.5425:
            if input[5] < 1556.7986:
                if input[5] < 1387.4912:
                    if input[1] < 84.09133:
                        var375 = -0.012267478
                    else:
                        var375 = 0.021849543
                else:
                    var375 = -0.04388648
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var375 = 0.0074380706
                    else:
                        var375 = 0.052974768
                else:
                    if input[1] < 47.74073:
                        var375 = 0.017121844
                    else:
                        var375 = -0.0013661388
        else:
            var375 = 0.036321107
    if input[4] < 8.0126295:
        var376 = -0.04254363
    else:
        if input[2] < 796.5425:
            if input[5] < 1556.7986:
                if input[5] < 1387.4912:
                    if input[1] < 84.09133:
                        var376 = -0.012107632
                    else:
                        var376 = 0.019897934
                else:
                    var376 = -0.04306967
            else:
                if input[5] < 1708.4924:
                    if input[5] < 1630.4938:
                        var376 = 0.007473229
                    else:
                        var376 = 0.052550506
                else:
                    if input[3] < 62.92014:
                        var376 = -0.029088354
                    else:
                        var376 = 0.0024182445
        else:
            var376 = 0.03579478
    if input[2] < 691.64557:
        var377 = -0.04210655
    else:
        if input[4] < 8.324405:
            if input[5] < 1556.7986:
                if input[4] < 8.241077:
                    if input[4] < 8.181944:
                        var377 = -0.033163548
                    else:
                        var377 = 0.03165308
                else:
                    var377 = -0.048245054
            else:
                if input[5] < 1799.6632:
                    if input[3] < 65.1018:
                        var377 = 0.013171191
                    else:
                        var377 = 0.04537236
                else:
                    if input[5] < 2292.848:
                        var377 = -0.01672318
                    else:
                        var377 = 0.004148777
        else:
            if input[2] < 733.0016:
                var377 = -0.010800759
            else:
                var377 = 0.039448928
    if input[4] < 8.0126295:
        var378 = -0.0418318
    else:
        if input[2] < 768.4635:
            if input[5] < 3636.057:
                if input[5] < 3539.6162:
                    if input[5] < 3346.2974:
                        var378 = 0.0057653883
                    else:
                        var378 = -0.03815147
                else:
                    if input[1] < 54.21738:
                        var378 = 0.0017341344
                    else:
                        var378 = 0.05769629
            else:
                if input[3] < 152.17412:
                    if input[0] < 36.583706:
                        var378 = -0.041477796
                    else:
                        var378 = 0.022079023
                else:
                    if input[4] < 8.155125:
                        var378 = 0.025175044
                    else:
                        var378 = -0.0051943506
        else:
            if input[0] < 22.122957:
                var378 = -0.010435497
            else:
                var378 = 0.03921579
    if input[2] < 691.64557:
        var379 = -0.041360315
    else:
        if input[4] < 8.301448:
            if input[4] < 8.254773:
                if input[0] < 26.970547:
                    if input[4] < 8.187523:
                        var379 = 0.002971129
                    else:
                        var379 = 0.029866511
                else:
                    if input[1] < 56.601948:
                        var379 = -0.03683972
                    else:
                        var379 = 0.0049122134
            else:
                if input[1] < 73.290535:
                    var379 = 0.040110596
                else:
                    if input[2] < 753.20294:
                        var379 = -0.07195147
                    else:
                        var379 = -0.008201221
        else:
            if input[0] < 22.122957:
                var379 = -0.021268276
            else:
                var379 = 0.04094746
    if input[4] < 8.0126295:
        var380 = -0.041064497
    else:
        if input[2] < 768.4635:
            if input[3] < 43.822132:
                var380 = -0.032057468
            else:
                if input[5] < 1799.6632:
                    if input[4] < 8.241077:
                        var380 = 0.039160382
                    else:
                        var380 = -0.031955384
                else:
                    if input[5] < 2292.848:
                        var380 = -0.015552958
                    else:
                        var380 = 0.0034219546
        else:
            if input[0] < 22.122957:
                var380 = -0.009017609
            else:
                var380 = 0.038189754
    if input[2] < 691.64557:
        var381 = -0.040610287
    else:
        if input[4] < 8.301448:
            if input[4] < 8.254773:
                if input[0] < 26.970547:
                    if input[4] < 8.187523:
                        var381 = 0.002737102
                    else:
                        var381 = 0.028639883
                else:
                    if input[1] < 56.601948:
                        var381 = -0.03534972
                    else:
                        var381 = 0.0046257824
            else:
                if input[1] < 73.290535:
                    var381 = 0.039311547
                else:
                    if input[2] < 753.20294:
                        var381 = -0.06915503
                    else:
                        var381 = -0.008142739
        else:
            if input[0] < 22.122957:
                var381 = -0.020680225
            else:
                var381 = 0.04037221
    if input[4] < 8.0126295:
        var382 = -0.040261436
    else:
        if input[2] < 744.1235:
            if input[0] < 26.970547:
                if input[0] < 24.82538:
                    if input[0] < 24.350086:
                        var382 = 0.0031105771
                    else:
                        var382 = -0.043965496
                else:
                    if input[1] < 61.240295:
                        var382 = 0.005933144
                    else:
                        var382 = 0.04851317
            else:
                if input[0] < 30.605228:
                    if input[1] < 85.46175:
                        var382 = -0.05232321
                    else:
                        var382 = -0.0009297007
                else:
                    if input[0] < 32.96395:
                        var382 = 0.042652305
                    else:
                        var382 = -0.010281469
        else:
            if input[3] < 104.90332:
                if input[0] < 25.290705:
                    if input[2] < 760.2625:
                        var382 = 0.013503029
                    else:
                        var382 = -0.051368143
                else:
                    if input[3] < 48.123383:
                        var382 = 0.010728754
                    else:
                        var382 = 0.0528484
            else:
                if input[5] < 2681.302:
                    var382 = -0.05668959
                else:
                    if input[3] < 172.44543:
                        var382 = -0.0005516404
                    else:
                        var382 = 0.03465208
    if input[2] < 691.64557:
        var383 = -0.039847177
    else:
        if input[4] < 8.301448:
            if input[4] < 8.254773:
                if input[0] < 26.970547:
                    if input[4] < 8.187523:
                        var383 = 0.002623227
                    else:
                        var383 = 0.027046168
                else:
                    if input[1] < 56.601948:
                        var383 = -0.033967335
                    else:
                        var383 = 0.004525755
            else:
                if input[1] < 73.290535:
                    var383 = 0.038369384
                else:
                    if input[2] < 753.20294:
                        var383 = -0.06700404
                    else:
                        var383 = -0.007962513
        else:
            if input[0] < 22.122957:
                var383 = -0.019361267
            else:
                var383 = 0.039769683
    if input[2] < 691.64557:
        var384 = -0.039440323
    else:
        if input[2] < 768.4635:
            if input[1] < 47.42564:
                if input[3] < 152.17412:
                    if input[3] < 142.28612:
                        var384 = 0.017413355
                    else:
                        var384 = -0.04329692
                else:
                    var384 = 0.04349311
            else:
                if input[1] < 54.039787:
                    if input[1] < 52.178165:
                        var384 = -0.00203827
                    else:
                        var384 = -0.053694606
                else:
                    if input[3] < 80.19552:
                        var384 = 0.017948115
                    else:
                        var384 = -0.0017665625
        else:
            if input[0] < 22.199833:
                var384 = -0.007174283
            else:
                var384 = 0.036305334
    if input[4] < 8.0126295:
        var385 = -0.039126165
    else:
        if input[2] < 744.1235:
            if input[0] < 26.970547:
                if input[0] < 24.82538:
                    if input[0] < 24.350086:
                        var385 = 0.0028823314
                    else:
                        var385 = -0.043506827
                else:
                    if input[1] < 61.240295:
                        var385 = 0.004114749
                    else:
                        var385 = 0.046323117
            else:
                if input[0] < 30.605228:
                    if input[1] < 85.46175:
                        var385 = -0.05130887
                    else:
                        var385 = -0.00090131676
                else:
                    if input[0] < 32.96395:
                        var385 = 0.041240845
                    else:
                        var385 = -0.009749686
        else:
            if input[1] < 90.64338:
                if input[1] < 73.290535:
                    if input[1] < 63.28969:
                        var385 = -0.0026066974
                    else:
                        var385 = 0.05351472
                else:
                    if input[5] < 3955.953:
                        var385 = -0.02809829
                    else:
                        var385 = 0.04509997
            else:
                var385 = 0.042986464
    if input[2] < 691.64557:
        var386 = -0.03870455
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                if input[2] < 733.0016:
                    var386 = 0.018393943
                else:
                    var386 = -0.011503159
            else:
                var386 = -0.038844552
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var386 = 0.0029517147
                else:
                    if input[5] < 1708.4924:
                        var386 = 0.047107365
                    else:
                        var386 = 0.01002945
            else:
                if input[5] < 2292.848:
                    if input[3] < 91.50338:
                        var386 = 0.004054121
                    else:
                        var386 = -0.05244575
                else:
                    if input[0] < 22.290503:
                        var386 = 0.022347232
                    else:
                        var386 = 0.00033836704
    if input[4] < 8.0126295:
        var387 = -0.03838388
    else:
        if input[3] < 43.822132:
            var387 = -0.030232579
        else:
            if input[0] < 37.22879:
                if input[0] < 34.02495:
                    if input[0] < 29.948753:
                        var387 = -0.0003144374
                    else:
                        var387 = 0.021477224
                else:
                    if input[4] < 8.241077:
                        var387 = -0.03376646
                    else:
                        var387 = 0.031256936
            else:
                if input[4] < 8.136787:
                    var387 = -0.0023366655
                else:
                    if input[3] < 83.67294:
                        var387 = 0.047044475
                    else:
                        var387 = 0.009423549
    if input[2] < 691.64557:
        var388 = -0.037924226
    else:
        if input[2] < 703.2164:
            if input[2] < 700.4231:
                var388 = -0.0072092726
            else:
                var388 = 0.043763295
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var388 = -0.038146205
                else:
                    var388 = 0.004414327
            else:
                if input[1] < 90.64338:
                    if input[5] < 3955.953:
                        var388 = -0.004516804
                    else:
                        var388 = 0.016237212
                else:
                    if input[5] < 4047.857:
                        var388 = 0.028017221
                    else:
                        var388 = -0.01883121
    if input[4] < 8.0126295:
        var389 = -0.037593182
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                if input[2] < 733.0016:
                    var389 = 0.01681437
                else:
                    var389 = -0.01196536
            else:
                var389 = -0.037957914
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var389 = 0.0023985626
                else:
                    if input[5] < 1708.4924:
                        var389 = 0.04673144
                    else:
                        var389 = 0.009975418
            else:
                if input[5] < 2111.4065:
                    if input[4] < 8.168125:
                        var389 = -0.05087604
                    else:
                        var389 = 0.017506689
                else:
                    if input[3] < 80.19552:
                        var389 = 0.03179094
                    else:
                        var389 = 0.0007336274
    if input[2] < 691.64557:
        var390 = -0.037161946
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                if input[2] < 733.0016:
                    var390 = 0.017442571
                else:
                    var390 = -0.011673038
            else:
                var390 = -0.037533488
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var390 = 0.0023584235
                else:
                    if input[5] < 1708.4924:
                        var390 = 0.044960316
                    else:
                        var390 = 0.009738888
            else:
                if input[4] < 8.301448:
                    if input[5] < 2292.848:
                        var390 = -0.01642085
                    else:
                        var390 = 0.002417135
                else:
                    if input[3] < 171.65364:
                        var390 = 0.039113224
                    else:
                        var390 = -0.009069343
    if input[2] < 691.64557:
        var391 = -0.03674512
    else:
        if input[3] < 120.56106:
            if input[5] < 2748.8748:
                if input[1] < 58.03831:
                    if input[1] < 52.722603:
                        var391 = -0.00082348735
                    else:
                        var391 = 0.042664412
                else:
                    if input[1] < 66.80687:
                        var391 = -0.044242136
                    else:
                        var391 = 0.0026778162
            else:
                if input[1] < 55.418133:
                    if input[2] < 733.0016:
                        var391 = -0.045361683
                    else:
                        var391 = 0.022754375
                else:
                    if input[2] < 721.7867:
                        var391 = 0.07942479
                    else:
                        var391 = 0.025666049
        else:
            if input[3] < 152.17412:
                if input[1] < 73.290535:
                    if input[4] < 8.155125:
                        var391 = -0.030108443
                    else:
                        var391 = 0.017039156
                else:
                    if input[5] < 2955.2168:
                        var391 = 0.01736319
                    else:
                        var391 = -0.056964118
            else:
                if input[2] < 729.3266:
                    if input[1] < 44.82583:
                        var391 = 0.03371739
                    else:
                        var391 = -0.02766633
                else:
                    if input[1] < 54.617172:
                        var391 = -0.01087579
                    else:
                        var391 = 0.025626073
    if input[4] < 8.0126295:
        var392 = -0.036383327
    else:
        if input[4] < 8.023403:
            var392 = 0.03136398
        else:
            if input[4] < 8.065835:
                if input[2] < 742.155:
                    var392 = -0.033181306
                else:
                    var392 = -0.005263956
            else:
                if input[3] < 120.56106:
                    if input[5] < 2748.8748:
                        var392 = -0.0016673793
                    else:
                        var392 = 0.030377317
                else:
                    if input[0] < 23.221859:
                        var392 = 0.014369174
                    else:
                        var392 = -0.012434481
    if input[2] < 691.64557:
        var393 = -0.035964753
    else:
        if input[5] < 1556.7986:
            if input[3] < 48.872616:
                var393 = 0.0077732354
            else:
                var393 = -0.032209907
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var393 = 0.0028863081
                else:
                    if input[5] < 1708.4924:
                        var393 = 0.043711126
                    else:
                        var393 = 0.009521797
            else:
                if input[4] < 8.301448:
                    if input[5] < 2292.848:
                        var393 = -0.01527181
                    else:
                        var393 = 0.0021088389
                else:
                    if input[3] < 171.65364:
                        var393 = 0.038348503
                    else:
                        var393 = -0.009931262
    if input[4] < 8.0126295:
        var394 = -0.035555635
    else:
        if input[4] < 8.023403:
            var394 = 0.030401675
        else:
            if input[4] < 8.065835:
                if input[2] < 742.155:
                    var394 = -0.032744702
                else:
                    var394 = -0.004807769
            else:
                if input[3] < 120.56106:
                    if input[5] < 2748.8748:
                        var394 = -0.0010171384
                    else:
                        var394 = 0.02846743
                else:
                    if input[0] < 23.221859:
                        var394 = 0.013349253
                    else:
                        var394 = -0.012104897
    if input[2] < 691.64557:
        var395 = -0.03512617
    else:
        if input[1] < 47.74073:
            if input[4] < 8.151678:
                if input[3] < 152.17412:
                    var395 = -0.030916885
                else:
                    var395 = 0.028655013
            else:
                if input[5] < 3097.8657:
                    var395 = 0.045258813
                else:
                    if input[1] < 42.593197:
                        var395 = -0.036411438
                    else:
                        var395 = 0.018473418
        else:
            if input[1] < 55.418133:
                if input[2] < 737.73047:
                    if input[5] < 1822.3998:
                        var395 = 0.0027879362
                    else:
                        var395 = -0.048965726
                else:
                    if input[2] < 760.2625:
                        var395 = 0.033960875
                    else:
                        var395 = -0.033493575
            else:
                if input[1] < 58.03831:
                    if input[3] < 127.876236:
                        var395 = 0.050604235
                    else:
                        var395 = 0.0017195874
                else:
                    if input[0] < 24.631493:
                        var395 = -0.0112970155
                    else:
                        var395 = 0.007771761
    if input[2] < 691.64557:
        var396 = -0.034659695
    else:
        if input[1] < 47.74073:
            if input[4] < 8.151678:
                if input[3] < 152.17412:
                    var396 = -0.03015841
                else:
                    var396 = 0.028127277
            else:
                if input[5] < 3097.8657:
                    var396 = 0.044570923
                else:
                    if input[1] < 42.593197:
                        var396 = -0.035645884
                    else:
                        var396 = 0.01807234
        else:
            if input[1] < 55.418133:
                if input[0] < 26.55467:
                    if input[2] < 724.7756:
                        var396 = -0.044964343
                    else:
                        var396 = 0.02644968
                else:
                    if input[4] < 8.230444:
                        var396 = -0.05258545
                    else:
                        var396 = 0.00014195598
            else:
                if input[1] < 58.03831:
                    if input[3] < 127.876236:
                        var396 = 0.049101483
                    else:
                        var396 = 0.0018305903
                else:
                    if input[5] < 2698.7034:
                        var396 = -0.010867452
                    else:
                        var396 = 0.0079022385
    if input[2] < 691.64557:
        var397 = -0.034227144
    else:
        if input[3] < 120.56106:
            if input[3] < 115.57555:
                if input[0] < 22.883705:
                    if input[1] < 56.123478:
                        var397 = 0.023339188
                    else:
                        var397 = -0.0407796
                else:
                    if input[1] < 85.46175:
                        var397 = -0.0020809297
                    else:
                        var397 = 0.036788657
            else:
                if input[1] < 53.759136:
                    var397 = -0.023097
                else:
                    if input[1] < 83.82618:
                        var397 = 0.07799
                    else:
                        var397 = 0.011659633
        else:
            if input[3] < 152.17412:
                if input[1] < 73.290535:
                    if input[4] < 8.155125:
                        var397 = -0.029110385
                    else:
                        var397 = 0.015698291
                else:
                    if input[5] < 2955.2168:
                        var397 = 0.015578918
                    else:
                        var397 = -0.05349032
            else:
                if input[2] < 729.3266:
                    if input[1] < 44.82583:
                        var397 = 0.030127933
                    else:
                        var397 = -0.02599414
                else:
                    if input[1] < 54.617172:
                        var397 = -0.009356176
                    else:
                        var397 = 0.024673095
    if input[4] < 8.0126295:
        var398 = -0.03392239
    else:
        if input[4] < 8.023403:
            var398 = 0.029173572
        else:
            if input[4] < 8.065835:
                if input[2] < 742.155:
                    var398 = -0.031760883
                else:
                    var398 = -0.004860424
            else:
                if input[3] < 120.56106:
                    if input[5] < 2748.8748:
                        var398 = -0.0011780799
                    else:
                        var398 = 0.02701358
                else:
                    if input[0] < 23.221859:
                        var398 = 0.01270277
                    else:
                        var398 = -0.011459673
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var399 = -0.035120558
        else:
            var399 = -0.003965688
    else:
        if input[2] < 703.2164:
            var399 = 0.03910218
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var399 = -0.037538793
                else:
                    var399 = 0.0043635457
            else:
                if input[1] < 90.64338:
                    if input[5] < 3955.953:
                        var399 = -0.004389752
                    else:
                        var399 = 0.015913323
                else:
                    if input[5] < 4047.857:
                        var399 = 0.026096595
                    else:
                        var399 = -0.016448257
    if input[4] < 8.0126295:
        var400 = -0.033120207
    else:
        if input[4] < 8.023403:
            var400 = 0.028390808
        else:
            if input[4] < 8.065835:
                if input[2] < 742.155:
                    var400 = -0.031173086
                else:
                    var400 = -0.004634857
            else:
                if input[0] < 20.597967:
                    if input[1] < 81.32996:
                        var400 = -0.027379064
                    else:
                        var400 = 0.013846924
                else:
                    if input[0] < 21.366615:
                        var400 = 0.03205023
                    else:
                        var400 = 0.0008183559
    var401 = var345 + var346 + var347 + var348 + var349 + var350 + var351 + var352 + var353 + var354 + var355 + var356 + var357 + var358 + var359 + var360 + var361 + var362 + var363 + var364 + var365 + var366 + var367 + var368 + var369 + var370 + var371 + var372 + var373 + var374 + var375 + var376 + var377 + var378 + var379 + var380 + var381 + var382 + var383 + var384 + var385 + var386 + var387 + var388 + var389 + var390 + var391 + var392 + var393 + var394 + var395 + var396 + var397 + var398 + var399 + var400
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var402 = -0.034365915
        else:
            var402 = -0.003942832
    else:
        if input[2] < 703.2164:
            var402 = 0.03694759
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var402 = -0.036983773
                else:
                    var402 = 0.004054054
            else:
                if input[1] < 90.64338:
                    if input[5] < 3955.953:
                        var402 = -0.0042059543
                    else:
                        var402 = 0.015349339
                else:
                    if input[5] < 4047.857:
                        var402 = 0.024697911
                    else:
                        var402 = -0.015886653
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var403 = -0.03390829
        else:
            var403 = -0.0042199106
    else:
        if input[2] < 703.2164:
            var403 = 0.035325006
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var403 = -0.03650773
                else:
                    var403 = 0.0039931326
            else:
                if input[1] < 52.178165:
                    if input[0] < 26.55467:
                        var403 = 0.027489224
                    else:
                        var403 = -0.01160464
                else:
                    if input[1] < 53.28753:
                        var403 = -0.059030592
                    else:
                        var403 = 0.0012710189
    if input[4] < 8.0126295:
        var404 = -0.031960428
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                var404 = 0.001222087
            else:
                var404 = -0.034724247
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var404 = 0.0032667906
                else:
                    if input[5] < 1708.4924:
                        var404 = 0.041789677
                    else:
                        var404 = 0.008594055
            else:
                if input[5] < 2111.4065:
                    if input[4] < 8.168125:
                        var404 = -0.04656483
                    else:
                        var404 = 0.016905135
                else:
                    if input[3] < 80.19552:
                        var404 = 0.02999933
                    else:
                        var404 = -0.000070335635
    if input[2] < 691.64557:
        var405 = -0.03149455
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                var405 = 0.0017069405
            else:
                var405 = -0.03430285
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var405 = 0.0031962318
                else:
                    if input[5] < 1708.4924:
                        var405 = 0.039966322
                    else:
                        var405 = 0.008450533
            else:
                if input[5] < 2111.4065:
                    if input[4] < 8.168125:
                        var405 = -0.045311313
                    else:
                        var405 = 0.017108543
                else:
                    if input[3] < 80.19552:
                        var405 = 0.02873728
                    else:
                        var405 = -0.00008932909
    if input[4] < 8.0126295:
        var406 = -0.031175807
    else:
        if input[5] < 1556.7986:
            if input[5] < 1387.4912:
                var406 = 0.0012454861
            else:
                var406 = -0.03366293
        else:
            if input[5] < 1799.6632:
                if input[5] < 1630.4938:
                    var406 = 0.0030307393
                else:
                    if input[5] < 1708.4924:
                        var406 = 0.04028088
                    else:
                        var406 = 0.008151186
            else:
                if input[5] < 2111.4065:
                    if input[4] < 8.168125:
                        var406 = -0.044097695
                    else:
                        var406 = 0.015785025
                else:
                    if input[3] < 80.19552:
                        var406 = 0.027724553
                    else:
                        var406 = -0.00008809118
    if input[2] < 691.64557:
        var407 = -0.03076445
    else:
        if input[5] < 1556.7986:
            if input[3] < 48.872616:
                var407 = 0.005630926
            else:
                var407 = -0.029265154
        else:
            if input[5] < 1799.6632:
                if input[3] < 65.1018:
                    var407 = 0.0073907427
                else:
                    var407 = 0.034841776
            else:
                if input[5] < 2111.4065:
                    if input[4] < 8.168125:
                        var407 = -0.042922348
                    else:
                        var407 = 0.015869584
                else:
                    if input[3] < 80.19552:
                        var407 = 0.026492134
                    else:
                        var407 = -0.00007605739
    if input[2] < 700.4231:
        if input[4] < 8.151678:
            var408 = -0.032278586
        else:
            var408 = -0.0039342004
    else:
        if input[2] < 703.2164:
            var408 = 0.033969946
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var408 = -0.03568088
                else:
                    var408 = 0.0043945312
            else:
                if input[1] < 90.64338:
                    if input[0] < 20.804243:
                        var408 = -0.026388353
                    else:
                        var408 = 0.0012520076
                else:
                    if input[0] < 28.786358:
                        var408 = 0.027699087
                    else:
                        var408 = -0.009109948
    if input[2] < 700.4231:
        if input[0] < 25.77969:
            var409 = -0.032592025
        else:
            var409 = -0.004502608
    else:
        if input[2] < 703.2164:
            var409 = 0.03219716
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var409 = -0.035250857
                else:
                    var409 = 0.0039215824
            else:
                if input[1] < 90.64338:
                    if input[5] < 3955.953:
                        var409 = -0.003935711
                    else:
                        var409 = 0.013578516
                else:
                    if input[0] < 28.786358:
                        var409 = 0.02620603
                    else:
                        var409 = -0.008694387
    if input[4] < 8.0126295:
        var410 = -0.02986992
    else:
        if input[2] < 746.90137:
            if input[0] < 26.970547:
                if input[0] < 24.82538:
                    if input[0] < 24.350086:
                        var410 = 0.000922579
                    else:
                        var410 = -0.04102735
                else:
                    if input[1] < 61.240295:
                        var410 = -0.0002244158
                    else:
                        var410 = 0.03840458
            else:
                if input[0] < 29.823307:
                    if input[4] < 8.16224:
                        var410 = 0.008293273
                    else:
                        var410 = -0.048522703
                else:
                    if input[2] < 726.6149:
                        var410 = 0.017872984
                    else:
                        var410 = -0.016665602
        else:
            if input[0] < 28.530838:
                if input[3] < 172.44543:
                    if input[1] < 73.290535:
                        var410 = 0.011493781
                    else:
                        var410 = -0.019365441
                else:
                    if input[0] < 27.195625:
                        var410 = 0.036321472
                    else:
                        var410 = -0.003642073
            else:
                if input[3] < 149.34422:
                    if input[4] < 8.177689:
                        var410 = 0.010158627
                    else:
                        var410 = 0.04092825
                else:
                    var410 = 0.001968983
    if input[5] < 1556.7986:
        if input[4] < 8.181944:
            var411 = -0.032179356
        else:
            if input[5] < 1348.266:
                var411 = 0.0071546673
            else:
                var411 = -0.016014976
    else:
        if input[5] < 1708.4924:
            if input[4] < 8.136787:
                var411 = 0.0068448535
            else:
                var411 = 0.03421305
        else:
            if input[3] < 62.92014:
                var411 = -0.02624175
            else:
                if input[3] < 73.62454:
                    if input[5] < 1822.3998:
                        var411 = -0.009512244
                    else:
                        var411 = 0.036065873
                else:
                    if input[3] < 75.37392:
                        var411 = -0.038347885
                    else:
                        var411 = 0.0005432858
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var412 = -0.031634852
        else:
            var412 = -0.0035755746
    else:
        if input[2] < 703.2164:
            var412 = 0.030758882
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var412 = -0.034713876
                else:
                    var412 = 0.0039604637
            else:
                if input[1] < 88.66651:
                    if input[1] < 73.290535:
                        var412 = 0.004025323
                    else:
                        var412 = -0.011040916
                else:
                    if input[5] < 3930.5964:
                        var412 = 0.023534292
                    else:
                        var412 = -0.013855711
    if input[5] < 1556.7986:
        if input[5] < 1387.4912:
            if input[4] < 8.168125:
                var413 = -0.02632449
            else:
                var413 = 0.012547749
        else:
            var413 = -0.032779668
    else:
        if input[5] < 1799.6632:
            if input[3] < 66.64307:
                var413 = 0.005997877
            else:
                var413 = 0.033161104
        else:
            if input[5] < 2292.848:
                if input[3] < 91.50338:
                    if input[4] < 8.151678:
                        var413 = -0.034084212
                    else:
                        var413 = 0.01905722
                else:
                    var413 = -0.044313546
            else:
                if input[5] < 2511.7754:
                    if input[1] < 80.43887:
                        var413 = 0.051954277
                    else:
                        var413 = -0.02164222
                else:
                    if input[5] < 2698.7034:
                        var413 = -0.029992217
                    else:
                        var413 = 0.002438924
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var414 = -0.0029953027
        else:
            var414 = -0.028600994
    else:
        if input[5] < 1708.4924:
            if input[4] < 8.136787:
                var414 = 0.0063293795
            else:
                var414 = 0.03355507
        else:
            if input[2] < 768.4635:
                if input[3] < 62.92014:
                    var414 = -0.025890518
                else:
                    if input[3] < 73.62454:
                        var414 = 0.022278171
                    else:
                        var414 = -0.0017904084
            else:
                var414 = 0.028524166
    if input[4] < 8.065835:
        if input[5] < 3735.5132:
            var415 = -0.0330962
        else:
            var415 = 0.019008828
    else:
        if input[3] < 120.56106:
            if input[5] < 2748.8748:
                if input[5] < 2511.7754:
                    if input[2] < 724.7756:
                        var415 = -0.031192327
                    else:
                        var415 = 0.010143712
                else:
                    if input[1] < 66.80687:
                        var415 = -0.042138074
                    else:
                        var415 = 0.009835522
            else:
                if input[1] < 55.418133:
                    if input[0] < 30.166073:
                        var415 = 0.0036208709
                    else:
                        var415 = -0.03662897
                else:
                    if input[1] < 87.54926:
                        var415 = 0.050353732
                    else:
                        var415 = -0.008200555
        else:
            if input[0] < 23.221859:
                if input[4] < 8.12684:
                    if input[0] < 21.55322:
                        var415 = -0.034014553
                    else:
                        var415 = -0.0012697575
                else:
                    if input[2] < 730.8562:
                        var415 = -0.008080113
                    else:
                        var415 = 0.045788076
            else:
                if input[5] < 3955.953:
                    if input[1] < 73.290535:
                        var415 = -0.0051282225
                    else:
                        var415 = -0.051730484
                else:
                    if input[0] < 26.911226:
                        var415 = 0.02604015
                    else:
                        var415 = -0.008782129
    if input[3] < 44.51236:
        var416 = -0.029571408
    else:
        if input[3] < 48.872616:
            var416 = 0.027562752
        else:
            if input[5] < 1556.7986:
                var416 = -0.02747163
            else:
                if input[5] < 1708.4924:
                    var416 = 0.031258125
                else:
                    if input[2] < 768.4635:
                        var416 = -0.0010808683
                    else:
                        var416 = 0.027809724
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var417 = -0.030807579
        else:
            var417 = -0.0032240842
    else:
        if input[2] < 703.2164:
            var417 = 0.029673392
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var417 = -0.034089655
                else:
                    var417 = 0.004153961
            else:
                if input[1] < 88.66651:
                    if input[1] < 73.290535:
                        var417 = 0.0038727329
                    else:
                        var417 = -0.010590242
                else:
                    if input[5] < 3930.5964:
                        var417 = 0.022886483
                    else:
                        var417 = -0.013165812
    if input[3] < 44.51236:
        var418 = -0.028972799
    else:
        if input[3] < 48.872616:
            var418 = 0.026881356
        else:
            if input[5] < 1556.7986:
                var418 = -0.02699397
            else:
                if input[5] < 1708.4924:
                    var418 = 0.030531568
                else:
                    if input[3] < 62.92014:
                        var418 = -0.02478244
                    else:
                        var418 = 0.0007561245
    if input[4] < 8.0126295:
        var419 = -0.027778432
    else:
        if input[2] < 746.90137:
            if input[0] < 26.970547:
                if input[0] < 24.82538:
                    if input[0] < 24.350086:
                        var419 = 0.0004886901
                    else:
                        var419 = -0.038775712
                else:
                    if input[1] < 61.240295:
                        var419 = -0.0017469985
                    else:
                        var419 = 0.03557705
            else:
                if input[0] < 29.823307:
                    if input[4] < 8.16224:
                        var419 = 0.008783935
                    else:
                        var419 = -0.04721357
                else:
                    if input[2] < 726.6149:
                        var419 = 0.017521478
                    else:
                        var419 = -0.016086781
        else:
            if input[0] < 28.530838:
                if input[2] < 760.2625:
                    if input[1] < 73.03348:
                        var419 = 0.025574854
                    else:
                        var419 = -0.006274762
                else:
                    if input[4] < 8.2596:
                        var419 = -0.025707
                    else:
                        var419 = 0.016897617
            else:
                if input[1] < 45.71353:
                    var419 = 0.0038956266
                else:
                    if input[0] < 38.07353:
                        var419 = 0.03852643
                    else:
                        var419 = 0.009648294
    if input[4] < 8.065835:
        if input[5] < 3735.5132:
            var420 = -0.032465
        else:
            var420 = 0.018628204
    else:
        if input[5] < 3636.057:
            if input[5] < 3539.6162:
                if input[5] < 3346.2974:
                    if input[5] < 3076.746:
                        var420 = 0.0005435526
                    else:
                        var420 = 0.035416156
                else:
                    if input[0] < 22.478123:
                        var420 = -0.010117556
                    else:
                        var420 = -0.03794593
            else:
                if input[3] < 154.30815:
                    var420 = 0.043104913
                else:
                    var420 = 0.010610039
        else:
            if input[3] < 152.17412:
                if input[1] < 77.56267:
                    if input[1] < 45.71353:
                        var420 = -0.029822057
                    else:
                        var420 = 0.010898866
                else:
                    var420 = -0.042454924
            else:
                if input[2] < 735.6771:
                    if input[1] < 51.355244:
                        var420 = 0.018118426
                    else:
                        var420 = -0.027709419
                else:
                    if input[0] < 27.271341:
                        var420 = 0.028189182
                    else:
                        var420 = -0.011177326
    if input[3] < 44.51236:
        var421 = -0.028373322
    else:
        if input[3] < 48.872616:
            var421 = 0.026011681
        else:
            if input[5] < 1556.7986:
                var421 = -0.026527477
            else:
                if input[5] < 1708.4924:
                    var421 = 0.029880002
                else:
                    if input[3] < 62.92014:
                        var421 = -0.024139933
                    else:
                        var421 = 0.0006540476
    if input[5] < 1600.5679:
        if input[4] < 8.181944:
            var422 = -0.030094592
        else:
            if input[5] < 1348.266:
                var422 = 0.00656726
            else:
                var422 = -0.012923211
    else:
        if input[5] < 1708.4924:
            var422 = 0.026816472
        else:
            if input[4] < 8.301448:
                if input[5] < 2320.111:
                    if input[3] < 89.07573:
                        var422 = 0.005486715
                    else:
                        var422 = -0.044730928
                else:
                    if input[0] < 22.290503:
                        var422 = 0.019721843
                    else:
                        var422 = -0.0030260333
            else:
                if input[4] < 8.385801:
                    var422 = 0.03287981
                else:
                    var422 = -0.0068250457
    if input[5] < 1600.5679:
        if input[4] < 8.181944:
            var423 = -0.029657414
        else:
            if input[5] < 1348.266:
                var423 = 0.0057116523
            else:
                var423 = -0.012745607
    else:
        if input[5] < 1708.4924:
            var423 = 0.025919015
        else:
            if input[3] < 62.92014:
                var423 = -0.023633355
            else:
                if input[3] < 73.62454:
                    if input[5] < 1822.3998:
                        var423 = -0.009252052
                    else:
                        var423 = 0.034104396
                else:
                    if input[3] < 75.37392:
                        var423 = -0.037323866
                    else:
                        var423 = 0.0004438494
    if input[3] < 44.51236:
        var424 = -0.02772369
    else:
        if input[2] < 742.155:
            if input[5] < 3748.7295:
                if input[5] < 3539.6162:
                    if input[2] < 726.6149:
                        var424 = 0.00917791
                    else:
                        var424 = -0.012388008
                else:
                    if input[2] < 717.82:
                        var424 = -0.011791213
                    else:
                        var424 = 0.045177024
            else:
                if input[1] < 45.71353:
                    var424 = 0.018120717
                else:
                    if input[0] < 24.350086:
                        var424 = -0.0030945912
                    else:
                        var424 = -0.04144242
        else:
            if input[3] < 93.38004:
                if input[0] < 24.035046:
                    var424 = -0.031074805
                else:
                    var424 = 0.042548187
            else:
                if input[5] < 2391.5444:
                    if input[4] < 8.187523:
                        var424 = -0.04584697
                    else:
                        var424 = -0.0028538518
                else:
                    if input[3] < 172.44543:
                        var424 = -0.00010733013
                    else:
                        var424 = 0.025862306
    if input[4] < 8.065835:
        if input[5] < 3735.5132:
            var425 = -0.03174902
        else:
            var425 = 0.017799923
    else:
        if input[3] < 120.56106:
            if input[5] < 2748.8748:
                if input[5] < 2511.7754:
                    if input[2] < 724.7756:
                        var425 = -0.030417252
                    else:
                        var425 = 0.0096402755
                else:
                    if input[1] < 66.80687:
                        var425 = -0.040952783
                    else:
                        var425 = 0.008886587
            else:
                if input[1] < 55.418133:
                    if input[2] < 730.8562:
                        var425 = -0.036438182
                    else:
                        var425 = 0.0032393278
                else:
                    if input[1] < 87.54926:
                        var425 = 0.048146203
                    else:
                        var425 = -0.008430131
        else:
            if input[0] < 23.221859:
                if input[2] < 730.8562:
                    if input[1] < 82.720825:
                        var425 = -0.025282288
                    else:
                        var425 = 0.018609239
                else:
                    if input[4] < 8.112143:
                        var425 = -0.015790446
                    else:
                        var425 = 0.044221792
            else:
                if input[5] < 3955.953:
                    if input[1] < 73.290535:
                        var425 = -0.004885678
                    else:
                        var425 = -0.048453867
                else:
                    if input[0] < 26.911226:
                        var425 = 0.023085011
                    else:
                        var425 = -0.008586282
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var426 = -0.029361183
        else:
            var426 = -0.0022327472
    else:
        if input[2] < 703.2164:
            var426 = 0.02697956
        else:
            if input[4] < 8.092142:
                if input[5] < 3686.298:
                    if input[1] < 81.73901:
                        var426 = -0.040987086
                    else:
                        var426 = -0.007657693
                else:
                    var426 = 0.026970362
            else:
                if input[5] < 2994.474:
                    if input[5] < 2832.3289:
                        var426 = 0.0016755406
                    else:
                        var426 = 0.039250202
                else:
                    if input[5] < 3076.746:
                        var426 = -0.035414454
                    else:
                        var426 = 0.0005919276
    if input[5] < 1600.5679:
        if input[4] < 8.181944:
            var427 = -0.028736705
        else:
            if input[5] < 1348.266:
                var427 = 0.0052144085
            else:
                var427 = -0.012337458
    else:
        if input[5] < 1708.4924:
            var427 = 0.025159178
        else:
            if input[3] < 62.92014:
                var427 = -0.023620067
            else:
                if input[3] < 73.62454:
                    if input[5] < 1822.3998:
                        var427 = -0.009676073
                    else:
                        var427 = 0.032891482
                else:
                    if input[3] < 75.37392:
                        var427 = -0.036506932
                    else:
                        var427 = 0.0005096563
    if input[4] < 8.065835:
        if input[5] < 3735.5132:
            var428 = -0.030668471
        else:
            var428 = 0.01576297
    else:
        if input[0] < 20.804243:
            if input[1] < 81.32996:
                if input[4] < 8.177689:
                    if input[4] < 8.12684:
                        var428 = -0.030073538
                    else:
                        var428 = 0.013528029
                else:
                    var428 = -0.041126486
            else:
                var428 = 0.02209807
        else:
            if input[0] < 21.484207:
                var428 = 0.03352834
            else:
                if input[2] < 744.1235:
                    if input[2] < 726.6149:
                        var428 = 0.00594883
                    else:
                        var428 = -0.01088928
                else:
                    if input[1] < 63.28969:
                        var428 = -0.00677657
                    else:
                        var428 = 0.017396254
    if input[5] < 1556.7986:
        if input[5] < 1387.4912:
            var429 = -0.005152303
        else:
            var429 = -0.028938202
    else:
        if input[5] < 1799.6632:
            if input[3] < 66.64307:
                var429 = 0.0017631121
            else:
                var429 = 0.028839145
        else:
            if input[5] < 2292.848:
                if input[3] < 91.50338:
                    if input[4] < 8.151678:
                        var429 = -0.032675903
                    else:
                        var429 = 0.01706363
                else:
                    var429 = -0.040794965
            else:
                if input[5] < 2511.7754:
                    if input[1] < 80.43887:
                        var429 = 0.047734175
                    else:
                        var429 = -0.02150775
                else:
                    if input[5] < 2713.444:
                        var429 = -0.026008222
                    else:
                        var429 = 0.0021799323
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var430 = -0.029126322
        else:
            var430 = -0.0018174619
    else:
        if input[2] < 703.2164:
            var430 = 0.025538936
        else:
            if input[2] < 715.4301:
                if input[4] < 8.187523:
                    var430 = -0.03288774
                else:
                    var430 = 0.0031427708
            else:
                if input[1] < 88.66651:
                    if input[1] < 73.290535:
                        var430 = 0.0033489857
                    else:
                        var430 = -0.00997049
                else:
                    if input[5] < 3930.5964:
                        var430 = 0.021820275
                    else:
                        var430 = -0.012401524
    if input[5] < 1600.5679:
        if input[4] < 8.181944:
            var431 = -0.027875667
        else:
            var431 = -0.0051652077
    else:
        if input[5] < 1708.4924:
            var431 = 0.023383997
        else:
            if input[4] < 8.301448:
                if input[5] < 2320.111:
                    if input[3] < 89.07573:
                        var431 = 0.0039475043
                    else:
                        var431 = -0.04160167
                else:
                    if input[0] < 22.36087:
                        var431 = 0.01851372
                    else:
                        var431 = -0.0027937365
            else:
                if input[4] < 8.378964:
                    var431 = 0.03146381
                else:
                    var431 = -0.0035838173
    if input[5] < 1600.5679:
        if input[4] < 8.181944:
            var432 = -0.027578184
        else:
            var432 = -0.005379853
    else:
        if input[5] < 1708.4924:
            var432 = 0.0225531
        else:
            if input[4] < 8.301448:
                if input[5] < 2320.111:
                    if input[3] < 89.07573:
                        var432 = 0.0037288212
                    else:
                        var432 = -0.040311094
                else:
                    if input[0] < 22.36087:
                        var432 = 0.017887263
                    else:
                        var432 = -0.0026032736
            else:
                if input[4] < 8.378964:
                    var432 = 0.030985415
                else:
                    var432 = -0.0037693013
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var433 = -0.0024320579
        else:
            var433 = -0.025124285
    else:
        if input[3] < 120.56106:
            if input[3] < 115.57555:
                if input[4] < 8.102652:
                    var433 = -0.029920924
                else:
                    if input[5] < 1708.4924:
                        var433 = 0.035950195
                    else:
                        var433 = 0.001274952
            else:
                if input[1] < 59.078312:
                    var433 = -0.022058988
                else:
                    if input[1] < 82.52746:
                        var433 = 0.06251358
                    else:
                        var433 = 0.005979679
        else:
            if input[3] < 152.17412:
                if input[4] < 8.168125:
                    if input[1] < 51.544662:
                        var433 = -0.0040271175
                    else:
                        var433 = -0.040046692
                else:
                    if input[0] < 23.221859:
                        var433 = 0.03575474
                    else:
                        var433 = -0.013412579
            else:
                if input[3] < 165.44615:
                    if input[2] < 721.7867:
                        var433 = -0.010843969
                    else:
                        var433 = 0.032801952
                else:
                    if input[1] < 86.480606:
                        var433 = -0.016310176
                    else:
                        var433 = 0.019917486
    if input[2] < 742.155:
        if input[3] < 86.07635:
            if input[0] < 28.652903:
                if input[2] < 733.0016:
                    if input[2] < 726.6149:
                        var434 = -0.018273847
                    else:
                        var434 = 0.035327815
                else:
                    var434 = -0.017976439
            else:
                if input[3] < 69.10682:
                    if input[3] < 62.92014:
                        var434 = -0.02519152
                    else:
                        var434 = 0.024870252
                else:
                    var434 = -0.044143494
        else:
            if input[5] < 3748.7295:
                if input[0] < 25.146177:
                    if input[2] < 724.7756:
                        var434 = -0.025128568
                    else:
                        var434 = 0.0103295995
                else:
                    if input[2] < 726.6149:
                        var434 = 0.058099058
                    else:
                        var434 = -0.015673883
            else:
                if input[1] < 45.71353:
                    var434 = 0.016192457
                else:
                    if input[0] < 24.350086:
                        var434 = -0.0046245004
                    else:
                        var434 = -0.039556257
    else:
        if input[1] < 63.28969:
            if input[1] < 52.178165:
                if input[5] < 3636.057:
                    var434 = 0.035675462
                else:
                    if input[1] < 45.71353:
                        var434 = -0.021659367
                    else:
                        var434 = 0.01669478
            else:
                if input[4] < 8.181944:
                    if input[5] < 3441.4753:
                        var434 = -0.047536787
                    else:
                        var434 = -0.004753161
                else:
                    var434 = 0.0091335615
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var434 = -0.04132567
                    else:
                        var434 = 0.0014066172
                else:
                    var434 = 0.023210475
            else:
                if input[1] < 84.55421:
                    if input[0] < 33.817833:
                        var434 = 0.037573878
                    else:
                        var434 = -0.0042826487
                else:
                    if input[3] < 139.43567:
                        var434 = 0.025539404
                    else:
                        var434 = -0.02039135
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var435 = -0.028345281
        else:
            var435 = -0.0027723375
    else:
        if input[2] < 703.2164:
            var435 = 0.022893924
        else:
            if input[2] < 715.4301:
                if input[0] < 24.973854:
                    var435 = -0.0011285091
                else:
                    var435 = -0.03101337
            else:
                if input[4] < 8.102652:
                    if input[5] < 3686.298:
                        var435 = -0.034126338
                    else:
                        var435 = 0.01933104
                else:
                    if input[5] < 4887.909:
                        var435 = 0.0010286862
                    else:
                        var435 = 0.026978716
    if input[2] < 730.8562:
        if input[4] < 8.215596:
            if input[5] < 4009.7493:
                if input[5] < 3097.8657:
                    if input[0] < 29.823307:
                        var436 = -0.019392494
                    else:
                        var436 = 0.017459143
                else:
                    if input[1] < 61.665955:
                        var436 = -0.0078467
                    else:
                        var436 = 0.040559135
            else:
                if input[5] < 5312.9517:
                    var436 = -0.033862803
                else:
                    var436 = -0.0052909306
        else:
            if input[1] < 51.355244:
                var436 = -0.0059851347
            else:
                if input[2] < 724.7756:
                    var436 = -0.009228448
                else:
                    var436 = -0.036931094
    else:
        if input[4] < 8.112143:
            if input[5] < 3686.298:
                var436 = -0.029870166
            else:
                var436 = 0.0023585327
        else:
            if input[3] < 172.44543:
                if input[5] < 3636.057:
                    if input[1] < 58.8646:
                        var436 = 0.022384914
                    else:
                        var436 = 0.001089141
                else:
                    if input[1] < 82.106895:
                        var436 = 0.004301828
                    else:
                        var436 = -0.031091405
            else:
                var436 = 0.038948666
    if input[2] < 730.8562:
        if input[4] < 8.215596:
            if input[5] < 4009.7493:
                if input[5] < 3097.8657:
                    if input[0] < 29.823307:
                        var437 = -0.018637773
                    else:
                        var437 = 0.016685748
                else:
                    if input[1] < 61.665955:
                        var437 = -0.0076683634
                    else:
                        var437 = 0.038659997
            else:
                if input[5] < 5312.9517:
                    var437 = -0.03330588
                else:
                    var437 = -0.004903405
        else:
            if input[1] < 51.355244:
                var437 = -0.006041383
            else:
                if input[2] < 724.7756:
                    var437 = -0.009194441
                else:
                    var437 = -0.036616348
    else:
        if input[4] < 8.112143:
            if input[3] < 168.97972:
                if input[3] < 145.07802:
                    var437 = -0.026986066
                else:
                    var437 = 0.031132435
            else:
                var437 = -0.036318853
        else:
            if input[3] < 172.44543:
                if input[5] < 3636.057:
                    if input[5] < 3464.0354:
                        var437 = 0.003693444
                    else:
                        var437 = 0.03595275
                else:
                    if input[1] < 82.106895:
                        var437 = 0.0043639634
                    else:
                        var437 = -0.029672978
            else:
                var437 = 0.038292095
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var438 = -0.0035667699
        else:
            var438 = -0.023593089
    else:
        if input[5] < 1799.6632:
            if input[3] < 66.64307:
                var438 = -0.00063272985
            else:
                var438 = 0.027531747
        else:
            if input[5] < 1864.8372:
                if input[4] < 8.16224:
                    var438 = -0.041282136
                else:
                    var438 = 0.012602913
            else:
                if input[3] < 82.3246:
                    if input[2] < 739.5616:
                        var438 = -0.004832427
                    else:
                        var438 = 0.03904273
                else:
                    if input[3] < 86.07635:
                        var438 = -0.03963859
                    else:
                        var438 = 0.0012346342
    if input[2] < 700.4231:
        if input[0] < 25.77969:
            var439 = -0.027975915
        else:
            var439 = -0.0023120516
    else:
        if input[2] < 703.2164:
            var439 = 0.020847116
        else:
            if input[2] < 715.4301:
                if input[4] < 8.181944:
                    var439 = -0.03026622
                else:
                    var439 = 0.00014589113
            else:
                if input[3] < 168.97972:
                    if input[3] < 155.53893:
                        var439 = -0.0006956248
                    else:
                        var439 = 0.031438448
                else:
                    if input[4] < 8.112143:
                        var439 = -0.03765177
                    else:
                        var439 = 0.002413524
    if input[2] < 730.8562:
        if input[4] < 8.215596:
            if input[5] < 4009.7493:
                if input[5] < 3097.8657:
                    if input[0] < 29.823307:
                        var440 = -0.018036652
                    else:
                        var440 = 0.015349701
                else:
                    if input[0] < 25.213438:
                        var440 = 0.0017373407
                    else:
                        var440 = 0.044161674
            else:
                if input[0] < 33.13334:
                    var440 = -0.032462344
                else:
                    var440 = -0.0048429314
        else:
            if input[1] < 51.355244:
                var440 = -0.005729945
            else:
                if input[2] < 724.7756:
                    var440 = -0.00899685
                else:
                    var440 = -0.035822667
    else:
        if input[4] < 8.112143:
            if input[3] < 168.97972:
                if input[3] < 145.07802:
                    var440 = -0.026290515
                else:
                    var440 = 0.030198911
            else:
                var440 = -0.034977343
        else:
            if input[3] < 172.44543:
                if input[5] < 3636.057:
                    if input[5] < 3464.0354:
                        var440 = 0.0035149928
                    else:
                        var440 = 0.034968548
                else:
                    if input[1] < 84.55421:
                        var440 = 0.0024220527
                    else:
                        var440 = -0.032058794
            else:
                var440 = 0.037340358
    if input[2] < 730.8562:
        if input[4] < 8.215596:
            if input[5] < 4009.7493:
                if input[5] < 3097.8657:
                    if input[0] < 29.823307:
                        var441 = -0.017367011
                    else:
                        var441 = 0.014503014
                else:
                    if input[1] < 61.665955:
                        var441 = -0.008256242
                    else:
                        var441 = 0.03521128
            else:
                if input[5] < 5023.009:
                    var441 = -0.031792205
                else:
                    var441 = -0.0044725705
        else:
            if input[1] < 51.355244:
                var441 = -0.0058327033
            else:
                if input[2] < 724.7756:
                    var441 = -0.008502647
                else:
                    var441 = -0.035184156
    else:
        if input[4] < 8.112143:
            if input[3] < 168.97972:
                if input[3] < 145.07802:
                    var441 = -0.025803646
                else:
                    var441 = 0.029614612
            else:
                var441 = -0.03429815
        else:
            if input[3] < 172.44543:
                if input[5] < 4781.7534:
                    if input[1] < 58.03831:
                        var441 = 0.018083634
                    else:
                        var441 = -0.00024341613
                else:
                    var441 = -0.020702401
            else:
                var441 = 0.036685396
    if input[2] < 700.4231:
        if input[0] < 25.77969:
            var442 = -0.027440874
        else:
            var442 = -0.002371549
    else:
        if input[2] < 703.2164:
            var442 = 0.019021174
        else:
            if input[2] < 715.4301:
                if input[4] < 8.181944:
                    var442 = -0.029392922
                else:
                    var442 = 0.0010441391
            else:
                if input[4] < 8.112143:
                    if input[1] < 63.508068:
                        var442 = 0.015140411
                    else:
                        var442 = -0.025609648
                else:
                    if input[1] < 65.92256:
                        var442 = -0.0047538
                    else:
                        var442 = 0.009036685
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var443 = -0.0268898
        else:
            var443 = -0.0022497987
    else:
        if input[2] < 703.2164:
            var443 = 0.017941078
        else:
            if input[2] < 715.4301:
                if input[4] < 8.181944:
                    var443 = -0.028870627
                else:
                    var443 = 0.0007761177
            else:
                if input[1] < 88.66651:
                    if input[3] < 60.685356:
                        var443 = -0.021028887
                    else:
                        var443 = 0.00053999637
                else:
                    if input[4] < 8.12684:
                        var443 = -0.013248648
                    else:
                        var443 = 0.017691934
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var444 = -0.0031061776
        else:
            var444 = -0.022628088
    else:
        if input[5] < 1799.6632:
            if input[3] < 66.64307:
                var444 = 0.0003653558
            else:
                var444 = 0.027171692
        else:
            if input[5] < 1864.8372:
                if input[4] < 8.16224:
                    var444 = -0.04008273
                else:
                    var444 = 0.0121406205
            else:
                if input[2] < 730.8562:
                    if input[2] < 726.6149:
                        var444 = 0.001933704
                    else:
                        var444 = -0.028159935
                else:
                    if input[0] < 24.414213:
                        var444 = 0.016214432
                    else:
                        var444 = -0.0015823639
    if input[2] < 700.4231:
        if input[1] < 77.56267:
            var445 = -0.02638281
        else:
            var445 = -0.0023178568
    else:
        if input[1] < 55.418133:
            if input[1] < 52.178165:
                if input[0] < 26.55467:
                    if input[2] < 717.82:
                        var445 = -0.021793516
                    else:
                        var445 = 0.025044007
                else:
                    if input[1] < 47.74073:
                        var445 = 0.005698807
                    else:
                        var445 = -0.028342867
            else:
                if input[1] < 53.28753:
                    var445 = -0.045011073
                else:
                    if input[3] < 164.87047:
                        var445 = 0.013031567
                    else:
                        var445 = -0.037672225
        else:
            if input[1] < 58.03831:
                if input[3] < 127.876236:
                    var445 = 0.039010894
                else:
                    var445 = -0.0009984492
            else:
                if input[5] < 3076.746:
                    if input[1] < 66.80687:
                        var445 = -0.030393362
                    else:
                        var445 = 0.00088231557
                else:
                    if input[1] < 69.12142:
                        var445 = 0.035226714
                    else:
                        var445 = -0.00013894938
    if input[2] < 742.155:
        if input[4] < 8.151678:
            if input[1] < 63.508068:
                if input[1] < 57.08752:
                    if input[1] < 41.577087:
                        var446 = 0.0023562277
                    else:
                        var446 = -0.027013639
                else:
                    if input[4] < 8.112143:
                        var446 = 0.052348375
                    else:
                        var446 = 0.008937061
            else:
                if input[3] < 168.16113:
                    var446 = -0.039458636
                else:
                    var446 = -0.004114855
        else:
            if input[0] < 22.199833:
                if input[4] < 8.200379:
                    var446 = 0.04382691
                else:
                    if input[0] < 20.804243:
                        var446 = -0.025405435
                    else:
                        var446 = 0.009508598
            else:
                if input[1] < 47.42564:
                    var446 = 0.025843028
                else:
                    if input[2] < 726.6149:
                        var446 = 0.005502348
                    else:
                        var446 = -0.019158306
    else:
        if input[1] < 63.28969:
            if input[4] < 8.236438:
                if input[1] < 52.178165:
                    if input[4] < 8.200379:
                        var446 = 0.027118562
                    else:
                        var446 = -0.02179905
                else:
                    if input[1] < 53.759136:
                        var446 = -0.04325444
                    else:
                        var446 = -0.014183226
            else:
                var446 = 0.027900314
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var446 = -0.038373426
                    else:
                        var446 = 0.0033624142
                else:
                    var446 = 0.021656252
            else:
                if input[1] < 84.55421:
                    if input[4] < 8.254773:
                        var446 = 0.036596492
                    else:
                        var446 = -0.0002561945
                else:
                    if input[3] < 139.43567:
                        var446 = 0.022775317
                    else:
                        var446 = -0.017489115
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var447 = -0.0031690497
        else:
            var447 = -0.022352602
    else:
        if input[3] < 120.56106:
            if input[3] < 115.57555:
                if input[2] < 717.82:
                    var447 = -0.031020677
                else:
                    if input[1] < 58.8646:
                        var447 = 0.01670338
                    else:
                        var447 = -0.0027937833
            else:
                if input[2] < 708.1484:
                    var447 = 0.04284717
                else:
                    if input[4] < 8.177689:
                        var447 = -0.028901119
                    else:
                        var447 = 0.034334864
        else:
            if input[0] < 24.350086:
                if input[2] < 729.3266:
                    if input[0] < 21.677387:
                        var447 = -0.0011913545
                    else:
                        var447 = -0.03116935
                else:
                    if input[5] < 3930.5964:
                        var447 = 0.023701996
                    else:
                        var447 = -0.008730571
            else:
                if input[4] < 8.270223:
                    if input[5] < 3955.953:
                        var447 = -0.028420938
                    else:
                        var447 = -0.0031543802
                else:
                    var447 = 0.025832186
    if input[1] < 55.418133:
        if input[1] < 52.178165:
            if input[2] < 721.7867:
                if input[1] < 44.82583:
                    var448 = 0.0055682478
                else:
                    var448 = -0.03144264
            else:
                if input[0] < 27.120234:
                    if input[1] < 42.79849:
                        var448 = 0.0007655094
                    else:
                        var448 = 0.032775186
                else:
                    if input[2] < 746.90137:
                        var448 = -0.027718041
                    else:
                        var448 = 0.0055128946
        else:
            if input[1] < 53.28753:
                var448 = -0.043437794
            else:
                if input[3] < 159.75792:
                    if input[2] < 739.5616:
                        var448 = -0.01485215
                    else:
                        var448 = 0.030261463
                else:
                    var448 = -0.035854053
    else:
        if input[1] < 58.03831:
            if input[3] < 127.876236:
                var448 = 0.03518115
            else:
                var448 = -0.0015592044
        else:
            if input[2] < 753.20294:
                if input[0] < 25.452896:
                    if input[3] < 109.19461:
                        var448 = -0.040172294
                    else:
                        var448 = -0.001531835
                else:
                    if input[5] < 2913.364:
                        var448 = -0.008248062
                    else:
                        var448 = 0.018691603
            else:
                if input[0] < 22.122957:
                    var448 = -0.016002921
                else:
                    if input[4] < 8.181944:
                        var448 = -0.00012135432
                    else:
                        var448 = 0.040375438
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var449 = -0.003334925
        else:
            var449 = -0.022129001
    else:
        if input[1] < 55.418133:
            if input[1] < 52.178165:
                if input[4] < 8.236438:
                    if input[0] < 24.27158:
                        var449 = 0.013044334
                    else:
                        var449 = -0.013583586
                else:
                    var449 = 0.026944218
            else:
                if input[1] < 53.28753:
                    var449 = -0.0424518
                else:
                    if input[3] < 159.75792:
                        var449 = 0.011283394
                    else:
                        var449 = -0.035069752
        else:
            if input[1] < 58.03831:
                if input[3] < 127.876236:
                    var449 = 0.038216896
                else:
                    var449 = -0.0013783455
            else:
                if input[2] < 753.20294:
                    if input[2] < 726.6149:
                        var449 = 0.0075459317
                    else:
                        var449 = -0.008897481
                else:
                    if input[4] < 8.181944:
                        var449 = -0.00027771713
                    else:
                        var449 = 0.029464722
    if input[2] < 700.4231:
        var450 = -0.018342227
    else:
        if input[1] < 55.418133:
            if input[1] < 52.178165:
                if input[0] < 26.55467:
                    if input[2] < 717.82:
                        var450 = -0.021459265
                    else:
                        var450 = 0.022540879
                else:
                    if input[1] < 47.74073:
                        var450 = 0.005595892
                    else:
                        var450 = -0.02731101
            else:
                if input[1] < 53.28753:
                    var450 = -0.04173281
                else:
                    if input[2] < 730.8562:
                        var450 = -0.030898405
                    else:
                        var450 = 0.01402534
        else:
            if input[1] < 58.03831:
                if input[3] < 127.876236:
                    var450 = 0.03442717
                else:
                    var450 = -0.0010409772
            else:
                if input[5] < 3076.746:
                    if input[1] < 66.80687:
                        var450 = -0.027968755
                    else:
                        var450 = 0.0009699377
                else:
                    if input[1] < 69.12142:
                        var450 = 0.03363854
                    else:
                        var450 = 0.00009392483
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var451 = -0.003405428
        else:
            var451 = -0.022136537
    else:
        if input[4] < 8.301448:
            if input[5] < 1799.6632:
                if input[3] < 66.64307:
                    var451 = -0.0011896518
                else:
                    var451 = 0.024243807
            else:
                if input[5] < 1864.8372:
                    if input[3] < 75.37392:
                        var451 = -0.03449934
                    else:
                        var451 = 0.002475608
                else:
                    if input[3] < 82.3246:
                        var451 = 0.016731618
                    else:
                        var451 = -0.00262656
        else:
            var451 = 0.018672694
    if input[5] < 1556.7986:
        if input[3] < 48.872616:
            var452 = -0.0034027086
        else:
            var452 = -0.022050237
    else:
        if input[4] < 8.301448:
            if input[5] < 1708.4924:
                var452 = 0.017020708
            else:
                if input[5] < 2320.111:
                    if input[3] < 89.07573:
                        var452 = 0.0009542067
                    else:
                        var452 = -0.035456296
                else:
                    if input[0] < 22.290503:
                        var452 = 0.017063005
                    else:
                        var452 = -0.0027614709
        else:
            var452 = 0.01816119
    if input[2] < 742.155:
        if input[4] < 8.151678:
            if input[1] < 63.508068:
                if input[1] < 57.08752:
                    if input[3] < 144.47627:
                        var453 = -0.026219515
                    else:
                        var453 = 0.0021729723
                else:
                    var453 = 0.03733374
            else:
                if input[3] < 168.16113:
                    var453 = -0.038852997
                else:
                    var453 = -0.004457171
        else:
            if input[0] < 22.199833:
                if input[4] < 8.200379:
                    var453 = 0.040905144
                else:
                    if input[2] < 721.7867:
                        var453 = -0.018257326
                    else:
                        var453 = 0.0046629687
            else:
                if input[1] < 47.42564:
                    var453 = 0.025348632
                else:
                    if input[2] < 726.6149:
                        var453 = 0.0062579424
                    else:
                        var453 = -0.018655526
    else:
        if input[1] < 63.28969:
            if input[4] < 8.236438:
                if input[1] < 52.178165:
                    if input[4] < 8.200379:
                        var453 = 0.026196862
                    else:
                        var453 = -0.020956986
                else:
                    if input[0] < 27.350344:
                        var453 = -0.031510953
                    else:
                        var453 = -0.003161234
            else:
                var453 = 0.02632392
        else:
            if input[0] < 23.645546:
                if input[1] < 85.865974:
                    if input[3] < 131.16777:
                        var453 = -0.036134813
                    else:
                        var453 = 0.0022149174
                else:
                    var453 = 0.019651249
            else:
                if input[1] < 84.55421:
                    if input[4] < 8.254773:
                        var453 = 0.035482317
                    else:
                        var453 = -0.0006153357
                else:
                    if input[3] < 139.43567:
                        var453 = 0.020573799
                    else:
                        var453 = -0.014953178
    if input[3] < 62.92014:
        if input[1] < 83.25298:
            if input[4] < 8.215596:
                var454 = -0.035605233
            else:
                var454 = -0.0062045637
        else:
            var454 = 0.01413923
    else:
        if input[3] < 73.62454:
            if input[1] < 74.91183:
                var454 = 0.030365942
            else:
                var454 = -0.008517069
        else:
            if input[3] < 75.37392:
                var454 = -0.028873712
            else:
                if input[3] < 120.56106:
                    if input[5] < 2748.8748:
                        var454 = -0.003503142
                    else:
                        var454 = 0.018632248
                else:
                    if input[3] < 125.529655:
                        var454 = -0.028368521
                    else:
                        var454 = -0.0014114985
    if input[3] < 62.92014:
        if input[1] < 83.25298:
            if input[4] < 8.215596:
                var455 = -0.03509709
            else:
                var455 = -0.006267603
        else:
            var455 = 0.013591294
    else:
        if input[3] < 73.62454:
            if input[1] < 74.91183:
                var455 = 0.029421521
            else:
                var455 = -0.008434324
        else:
            if input[3] < 75.37392:
                var455 = -0.028035184
            else:
                if input[3] < 80.19552:
                    if input[3] < 77.09872:
                        var455 = 0.0006090899
                    else:
                        var455 = 0.026858723
                else:
                    if input[3] < 86.07635:
                        var455 = -0.02187282
                    else:
                        var455 = 0.0007623671
    return softmax([0.5 + (var97 + var98 + var99 + var100 + var101 + var102 + var103 + var104 + var105 + var106 + var107 + var108 + var109 + var110 + var111 + var112 + var113 + var114 + var115 + var116 + var117 + var118 + var119 + var120 + var121 + var122 + var123 + var124 + var125 + var126 + var127 + var128 + var129 + var130 + var131 + var132 + var133 + var134 + var135 + var136 + var137 + var138 + var139 + var140 + var141 + var142 + var143 + var144 + var145 + var146 + var147 + var148 + var149 + var150 + var151), 0.5 + (var249 + var250 + var251 + var252 + var253 + var254 + var255 + var256 + var257 + var258 + var259 + var260 + var261 + var262 + var263 + var264 + var265 + var266 + var267 + var268 + var269 + var270 + var271 + var272 + var273 + var274 + var275 + var276 + var277 + var278 + var279 + var280 + var281 + var282 + var283 + var284 + var285 + var286 + var287 + var288 + var289 + var290 + var291 + var292 + var293 + var294 + var295 + var296 + var297 + var298 + var299 + var300 + var301 + var302 + var303), 0.5 + (var401 + var402 + var403 + var404 + var405 + var406 + var407 + var408 + var409 + var410 + var411 + var412 + var413 + var414 + var415 + var416 + var417 + var418 + var419 + var420 + var421 + var422 + var423 + var424 + var425 + var426 + var427 + var428 + var429 + var430 + var431 + var432 + var433 + var434 + var435 + var436 + var437 + var438 + var439 + var440 + var441 + var442 + var443 + var444 + var445 + var446 + var447 + var448 + var449 + var450 + var451 + var452 + var453 + var454 + var455)])


def predict_proba(input_features):
    return score(input_features)
