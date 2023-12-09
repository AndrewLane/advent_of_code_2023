debug = False

input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

input = """14 23 30 32 26 9 -22 -70 -138 -229 -346 -492 -670 -883 -1134 -1426 -1762 -2145 -2578 -3064 -3606
4 27 78 180 375 742 1428 2693 4965 8900 15460 26084 43181 71517 121785 219063 421510 859337 1812006 3854420 8122831
12 33 58 90 140 227 378 628 1020 1605 2442 3598 5148 7175 9770 13032 17068 21993 27930 35010 43372
8 20 43 88 185 401 878 1913 4113 8678 17903 36055 70882 136157 255860 470864 849326 1502400 2607395 4441106 7426759
5 14 28 46 72 124 261 652 1736 4562 11453 27208 61141 130356 264772 514542 960655 1729670 3013706 5097002 8390566
-2 4 30 95 234 523 1117 2301 4554 8626 15628 27135 45302 72993 113923 172813 255558 369408 523162 727375 994578
-2 2 9 20 43 97 234 609 1649 4398 11158 26641 60071 129171 267968 542171 1078918 2122391 4133699 7963449 15140741
23 47 87 162 303 551 955 1570 2455 3671 5279 7338 9903 13023 16739 21082 26071 31711 37991 44882 52335
5 28 76 161 295 490 758 1111 1561 2120 2800 3613 4571 5686 6970 8435 10093 11956 14036 16345 18895
10 2 5 45 167 455 1079 2385 5045 10285 20210 38246 69720 122600 208418 343400 549828 857660 1306435 1947491 2846525
11 20 28 37 51 84 172 395 937 2254 5486 13351 31941 74219 166844 363702 773007 1611356 3309648 6715181 13465567
12 20 28 33 35 39 55 90 118 10 -574 -2245 -5593 -9774 -8323 21013 138200 484444 1363352 3384881 7710315
16 23 42 91 196 390 719 1260 2156 3673 6284 10785 18448 31216 51945 84698 135096 210731 321646 480887 705132
1 8 34 87 175 317 566 1040 1964 3753 7225 14140 28440 58856 124019 261975 547235 1120454 2238908 4360653 8282317
19 22 25 42 93 205 422 833 1642 3337 7070 15450 34120 74849 161658 343159 717581 1483116 3037123 6166146 12398567
13 23 44 85 152 247 369 530 806 1449 3105 7241 17019 39117 87448 190442 404619 838691 1694498 3333829 6383738
24 38 54 75 115 218 502 1239 2989 6836 14838 30916 62601 124398 244140 474856 916926 1759830 3362026 6406045 12202199
2 23 61 125 231 402 668 1066 1640 2441 3527 4963 6821 9180 12126 15752 20158 25451 31745 39161 47827
0 3 12 33 74 142 239 369 577 1044 2263 5347 12634 29067 65509 146443 326722 725577 1591458 3419069 7150862
15 19 22 23 17 -10 -87 -255 -527 -741 -160 3442 15617 48571 126688 295063 632075 1267950 2414604 4422018 7902157
26 43 70 112 170 246 366 641 1401 3459 8591 20354 45407 95550 190753 363511 664932 1173043 2003884 3326052 5379456
-1 -1 6 41 131 303 573 925 1287 1542 1677 2311 6127 21290 68986 199159 522031 1269185 2908648 6356221 13354187
14 30 63 135 284 581 1162 2287 4449 8573 16371 30959 57905 106971 194932 349967 618142 1072306 1823093 3030381 4911112
17 35 77 154 276 452 690 997 1379 1841 2387 3020 3742 4554 5456 6447 7525 8687 9929 11246 12632
-1 8 38 109 255 539 1073 2051 3824 7091 13363 25989 52219 107015 219591 443936 874801 1670742 3085712 5510265 9522523
-5 -2 14 59 158 340 629 1031 1517 2002 2320 2195 1208 -1240 -5969 -14065 -26929 -46330 -74462 -114005 -168190
15 41 75 124 212 383 709 1319 2486 4847 9898 21022 45501 98269 208626 431805 868225 1694541 3212293 5922144 10634474
17 33 53 85 162 363 839 1841 3747 7085 12549 21005 33484 51159 75303 107225 148181 199257 261221 334341 418166
14 33 64 115 213 421 875 1854 3896 7973 15738 29857 54439 95577 162013 265940 423954 658169 997508 1479183 2150377
2 11 22 42 97 243 581 1276 2580 4859 8624 14566 23595 36883 55911 82520 118966 167979 232826 317378 426181
18 20 14 0 -8 36 245 876 2485 6200 14156 30158 60708 116693 216340 390573 692744 1215960 2123014 3696392 6419132
18 27 38 57 95 159 247 351 466 598 766 1008 1447 2608 6550 20326 65533 202760 590573 1621022 4218046
-8 -15 -16 14 124 401 998 2192 4501 8922 17424 33969 66582 131425 260614 517001 1022018 2008219 3918536 7593000 14616172
13 24 43 85 171 328 589 993 1585 2416 3543 5029 6943 9360 12361 16033 20469 25768 32035 39381 47923
8 31 68 136 280 598 1276 2633 5176 9665 17188 29246 47848 75616 115900 172903 251816 358963 501956 689860 933368
26 52 96 157 231 309 369 374 302 249 662 2774 9323 25636 61139 131305 259962 481738 844204 1408971 2250583
8 7 3 8 56 222 645 1549 3255 6191 10957 18622 31677 56536 109315 228053 496898 1091527 2360831 4968508 10130750
19 30 49 76 124 247 586 1446 3425 7619 15925 31465 59187 106849 187069 322378 558107 993992 1857093 3659894 7524106
-6 2 32 93 201 400 794 1603 3280 6766 14017 29010 59538 120307 238352 463045 885850 1681022 3190154 6094719 11757259
-2 -1 10 44 119 272 589 1264 2718 5840 12469 26341 54909 112747 227720 451799 879390 1677405 3133116 5728194 10250347
12 26 50 93 178 356 722 1433 2728 4950 8570 14213 22686 35008 52442 76529 109124 152434 209058 282029 374858
3 18 50 107 212 426 898 1955 4249 8987 18284 35698 67030 121501 213452 364752 608143 991800 1585438 2488357 3839880
3 20 55 129 282 581 1129 2082 3701 6496 11559 21233 40324 78133 151665 290462 543607 989556 1749575 3005689 5024190
18 32 43 48 50 58 87 178 470 1369 3886 10280 25277 58388 128277 270807 553406 1099850 2131577 4034364 7462776
2 11 20 30 45 72 121 205 340 545 842 1256 1815 2550 3495 4687 6166 7975 10160 12770 15857
13 24 34 39 26 -23 -103 -124 195 1496 5059 13266 30382 63843 126306 238779 435201 768872 1321128 2212601 3617282
20 41 70 103 136 163 186 251 523 1423 3879 9789 22850 49980 103715 206420 398504 756520 1436393 2779359 5568808
17 39 68 96 108 75 -54 -357 -925 -1782 -2634 -2249 2866 21012 69836 183940 427029 910537 1821232 3460962 6302472
12 25 47 91 184 376 749 1426 2580 4443 7315 11573 17680 26194 37777 53204 73372 99309 132183 173311 224168
9 23 48 89 150 244 427 871 2007 4801 11282 25548 55694 117542 241875 488328 971501 1908667 3704204 7094267 13387062
6 23 54 121 274 611 1304 2643 5138 9761 18474 35292 68298 133295 260192 503830 961822 1803179 3313102 5961427 10504914
13 31 60 106 181 312 561 1056 2033 3889 7246 13026 22537 37570 60507 94440 143301 212003 306592 434410 604269
24 41 70 117 200 377 795 1780 3998 8735 18379 37244 72966 138862 257972 470200 845388 1507873 2682964 4784091 8572860
21 40 70 108 162 261 462 853 1551 2694 4426 6874 10116 14139 18786 23691 28201 31284 31422 26488 13606
7 12 33 89 216 481 1015 2089 4264 8662 17457 34828 68952 136319 271009 544033 1102084 2242030 4548437 9137620 18073857
-4 -7 0 34 126 325 709 1424 2785 5486 10979 22095 43993 85536 161206 293683 517226 882007 1459562 2349536 3687912
0 12 35 68 104 129 121 60 -16 169 1592 6986 23067 64991 164926 388049 861778 1828597 3741459 7437683 14461140
23 32 41 50 59 68 77 86 95 104 113 122 131 140 149 158 167 176 185 194 203
10 16 27 42 65 110 220 523 1363 3562 8896 20916 46346 97537 197087 387281 750512 1454224 2848417 5670598 11460303
16 30 53 77 87 69 33 50 297 1099 2952 6506 12482 21492 33726 48465 63374 73524 70087 38643 -42967
19 41 72 108 148 204 324 637 1442 3387 7818 17438 37550 78461 160253 322316 642113 1271041 2500520 4879276 9414028
15 30 57 109 225 481 1000 1972 3707 6756 12147 21795 39157 70215 124882 218938 376615 633962 1043133 1677753 2639529
14 20 43 98 211 425 806 1449 2484 4082 6461 9892 14705 21295 30128 41747 56778 75936 100031 129974 166783
15 17 20 26 44 113 338 940 2327 5207 10791 21189 40222 75136 140257 264724 508495 994481 1970878 3927904 7809112
25 53 104 191 333 554 891 1420 2314 3961 7205 13863 27886 58003 123648 267820 583911 1269449 2729590 5769071 11935891
12 16 17 11 -7 -39 -70 -39 226 1156 3753 10204 25064 57585 126483 270012 567572 1186000 2477477 5182433 10839687
7 20 43 94 203 421 845 1667 3256 6283 11900 21985 39466 68738 116188 190844 305165 475990 725665 1083368 1586653
5 23 61 128 242 441 794 1412 2459 4163 6827 10840 16688 24965 36384 51788 72161 98639 132521 175280 228574
8 25 41 50 45 18 -40 -139 -290 -505 -797 -1180 -1669 -2280 -3030 -3937 -5020 -6299 -7795 -9530 -11527
8 7 14 44 119 268 527 939 1554 2429 3628 5222 7289 9914 13189 17213 22092 27939 34874 43024 52523
14 16 24 39 61 96 168 336 716 1508 3028 5745 10323 17668 28980 45810 70122 104360 151520 215227 299817
2 -1 10 47 123 250 446 771 1432 3035 7139 17415 41978 97915 219803 475319 993266 2013091 3971216 7649687 14428865
5 27 63 122 225 420 821 1697 3657 7999 17307 36390 73685 143357 268644 487701 864549 1510047 2621427 4554210 7947537
5 2 5 21 63 162 377 809 1636 3195 6146 11768 22468 42645 80160 148842 272735 493192 880483 1552343 2702885
8 14 45 120 263 503 874 1415 2170 3188 4523 6234 8385 11045 14288 18193 22844 28330 34745 42188 50763
21 38 62 111 217 426 798 1407 2341 3702 5606 8183 11577 15946 21462 28311 36693 46822 58926 73247 90041
12 24 49 92 155 230 298 344 409 730 2078 6502 18834 49516 119585 269006 569986 1147444 2209463 4091320 7317589
13 30 60 111 195 320 484 678 915 1327 2429 5773 15481 41716 108355 269591 645004 1491641 3347905 7312828 15574862
11 5 -6 -16 0 93 354 956 2256 5009 10793 22845 47697 98317 199945 400511 788473 1522157 2876252 5313038 9588222
6 11 29 69 142 273 532 1108 2475 5733 13254 29842 64780 135496 274323 541239 1047936 2002555 3790467 7115107 13234518
17 23 26 41 91 213 482 1068 2362 5238 11568 25197 53748 111908 227302 450762 873823 1657721 3080134 5608513 10012225
5 3 -1 -5 1 42 161 413 857 1577 2799 5219 10717 23704 53433 117701 248477 500111 960911 1769019 3133673
7 24 49 80 124 217 454 1039 2370 5176 10722 21094 39569 71065 122653 204097 328369 512064 775615 1143180 1642042
5 15 31 53 81 115 155 201 253 311 375 445 521 603 691 785 885 991 1103 1221 1345
6 11 14 23 53 127 281 573 1096 1995 3488 5891 9647 15359 23827 36089 53466 77611 110562 154799 213305
17 20 24 29 35 42 50 59 69 80 92 105 119 134 150 167 185 204 224 245 267
12 18 16 9 10 49 194 599 1596 3852 8616 18085 35922 67963 123154 214763 361916 591510 940560 1459041 2213290
15 30 42 43 16 -56 -162 -198 181 1887 7082 20536 52192 121777 266728 555347 1108231 2133328 3984966 7267933 13029812
6 9 23 75 208 493 1048 2076 3945 7340 13518 24690 44537 78838 136145 228381 371160 583531 886729 1301373 1842382
20 40 68 114 202 372 677 1171 1885 2803 3900 5419 8789 19006 50105 136993 360435 899732 2144689 4935498 11077705
2 14 42 93 173 301 549 1137 2624 6248 14498 32080 67609 136671 267411 510578 957062 1767458 3220154 5786927 10248101
14 38 75 127 206 347 641 1307 2830 6215 13455 28407 58464 117793 233621 458298 891926 1723576 3303971 6269539 11747586
1 11 31 61 101 151 211 281 361 451 551 661 781 911 1051 1201 1361 1531 1711 1901 2101
4 -1 1 30 112 271 515 813 1060 1027 293 -1844 -6480 -15245 -30473 -55405 -94428 -153353 -239735 -363238 -536048
10 21 41 80 161 333 692 1410 2772 5221 9411 16268 27059 43469 67686 102494 151374 218613 309421 430056 587957
15 45 97 181 323 583 1082 2048 3909 7503 14565 28831 58433 120835 252490 526816 1086147 2196177 4335249 8335809 15601591
7 9 27 71 162 360 816 1859 4136 8833 18028 35285 66725 123052 223427 402741 724821 1305505 2351449 4223099 7533604
21 38 62 95 139 196 268 357 465 594 746 923 1127 1360 1624 1921 2253 2622 3030 3479 3971
9 11 16 24 35 49 66 86 109 135 164 196 231 269 310 354 401 451 504 560 619
6 14 25 46 103 251 585 1269 2613 5250 10508 21149 42764 86256 171960 335927 638536 1174570 2081715 3540428 5751333
13 31 69 134 236 396 653 1065 1709 2708 4358 7519 14614 31922 74498 176324 410910 933058 2063916 4464405 9486389
15 36 78 145 252 438 783 1433 2637 4800 8556 14865 25138 41394 66453 104169 159707 239868 353466 511761 728952
26 44 62 88 144 278 582 1208 2367 4285 7075 10465 13299 12701 2761 -27433 -96632 -235390 -491460 -936978 -1677846
20 34 51 77 131 257 540 1126 2246 4244 7609 13011 21341 33755 51722 77076 112072 159446 222479 305065 411783
17 34 68 125 206 297 350 261 -135 -1015 -2408 -3846 -3735 1623 19311 61035 143389 285328 500072 778447 1063084
5 2 -1 -4 -7 -10 -13 -16 -19 -22 -25 -28 -31 -34 -37 -40 -43 -46 -49 -52 -55
19 26 31 42 76 163 358 769 1614 3340 6898 14408 30716 66798 146664 320414 687441 1435482 2903269 5676858 10732176
19 26 46 106 242 511 1026 2018 3936 7628 14717 28425 55378 109503 220293 449949 927972 1918877 3950775 8052827 16183409
20 31 49 86 176 402 943 2156 4718 9863 19759 38080 70838 127550 222825 378466 626192 1011095 1595957 2466562 3738148
21 38 78 154 290 530 955 1727 3192 6093 11965 23799 47057 91071 170733 308153 533642 885075 1404663 2132847 3100971
26 47 77 121 194 338 660 1401 3044 6459 13058 24883 44476 74317 115666 167034 223706 282724 364549 577436 1281654
7 32 70 121 185 262 352 455 571 700 842 997 1165 1346 1540 1747 1967 2200 2446 2705 2977
9 13 22 42 93 227 561 1334 2997 6345 12700 24154 43881 76527 128687 209478 331217 510213 767682 1130794 1633861
5 15 25 35 45 55 65 75 85 95 105 115 125 135 145 155 165 175 185 195 205
17 37 66 111 181 278 398 552 808 1347 2537 5097 10621 23194 53789 130960 324620 795294 1890505 4324968 9505338
10 21 47 103 213 415 777 1437 2682 5100 9899 19619 39701 81754 169905 352347 721122 1444279 2815799 5330023 9788669
13 11 15 41 109 242 465 804 1285 1933 2771 3819 5093 6604 8357 10350 12573 15007 17623 20381 23229
9 22 43 82 177 412 945 2068 4341 8873 17869 35625 70241 136463 260337 486970 894200 1618802 2911453 5259931 9673910
2 -1 -4 -7 -10 -13 -16 -19 -22 -25 -28 -31 -34 -37 -40 -43 -46 -49 -52 -55 -58
25 49 102 201 367 636 1085 1894 3480 6757 13615 27812 56703 114678 229950 457538 903072 1764642 3403789 6462856 12056176
19 32 57 103 188 352 682 1360 2763 5668 11651 23848 48453 97860 197624 402206 830175 1740496 3691429 7858001 16641182
9 13 29 71 161 335 651 1208 2201 4063 7786 15580 32139 66959 138424 280777 555665 1070737 2008835 3672709 6551973
-6 -2 11 33 64 104 153 211 278 354 439 533 636 748 869 999 1138 1286 1443 1609 1784
10 19 36 76 168 378 856 1914 4138 8533 16696 31008 54832 92700 150468 235414 356250 523015 746812 1039348 1412232
3 8 22 46 81 128 188 262 351 456 578 718 877 1056 1256 1478 1723 1992 2286 2606 2953
16 37 69 105 143 208 402 1000 2618 6505 15064 32800 68053 136153 265127 505970 951092 1767489 3256591 5962615 10868987
10 15 23 31 43 81 191 440 906 1689 3032 5752 12357 29481 72620 174613 399898 867299 1784981 3502261 6584199
9 27 49 82 139 239 411 705 1216 2142 3943 7783 16690 38372 91547 219216 514843 1171309 2568285 5421944 11032453
16 25 34 43 52 61 70 79 88 97 106 115 124 133 142 151 160 169 178 187 196
2 14 52 146 346 735 1456 2759 5074 9116 16028 27568 46346 76117 122136 191581 294050 442138 652100 944606 1345594
4 22 52 91 149 267 544 1173 2495 5113 10190 20225 40912 85206 181528 389233 826150 1715304 3460984 6768279 12825231
21 31 41 51 61 71 81 91 101 111 121 131 141 151 161 171 181 191 201 211 221
22 39 72 145 297 582 1067 1839 3058 5133 9152 17765 36801 77996 163319 331507 647558 1216083 2199584 3842905 6505297
7 22 45 76 115 162 217 280 351 430 517 612 715 826 945 1072 1207 1350 1501 1660 1827
-2 7 31 78 159 296 552 1105 2397 5400 12068 26128 54586 110827 221203 438926 872656 1743923 3500729 7041360 14157097
8 9 11 14 18 23 29 36 44 53 63 74 86 99 113 128 144 161 179 198 218
6 0 -7 -15 -24 -34 -45 -57 -70 -84 -99 -115 -132 -150 -169 -189 -210 -232 -255 -279 -304
17 19 27 43 64 82 84 52 -37 -211 -503 -951 -1598 -2492 -3686 -5238 -7211 -9673 -12697 -16361 -20748
12 5 -4 -11 -6 27 117 345 954 2578 6641 15972 35666 74195 144752 266839 468280 788319 1283522 2040251 3201106
-4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 0 6 33 93 197 360 624 1111 2119 4282 8849 18257 37523 77846 165693 364347 821630 1869014 4215989 9312565
3 24 63 118 180 246 360 704 1777 4737 12055 28769 64886 139977 291993 594335 1189351 2354894 4637403 9117248 17931616
15 27 45 64 76 74 77 190 710 2292 6215 14871 32800 69013 142156 291563 599909 1237785 2548293 5202538 10477368
9 27 49 75 105 139 177 219 265 315 369 427 489 555 625 699 777 859 945 1035 1129
7 18 30 56 118 246 481 882 1537 2578 4200 6684 10424 15958 24003 35494 51627 73906 104194 144768 198378
22 38 64 115 225 457 923 1831 3593 7057 13967 27808 55258 108546 209104 393002 718768 1278320 2211874 3727841 6128887
-2 4 31 90 193 351 574 885 1378 2381 4843 11181 27050 64901 150836 337205 724626 1498582 2987295 5748904 10696643
1 0 0 1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171
7 29 58 91 127 172 249 413 771 1507 2912 5419 9643 16426 26887 42477 65039 96873 140806 200267 279367
4 0 5 25 76 192 434 915 1864 3762 7604 15392 31092 62596 125907 254105 516044 1053596 2151911 4364551 8723660
-3 6 21 35 31 -24 -185 -535 -1197 -2368 -4390 -7828 -13368 -20937 -26496 -12926 72637 370342 1217155 3367177 8414593
20 26 38 63 101 141 158 111 -58 -424 -1078 -2125 -3681 -5869 -8814 -12637 -17448 -23338 -30370 -38569 -47911
14 28 61 139 297 577 1038 1795 3107 5546 10307 19780 38645 76065 150205 297571 592030 1182806 2369267 4747107 9493891
-5 4 33 99 226 449 827 1477 2650 4890 9360 18499 37307 75759 153144 305533 598125 1144928 2139131 3898643 6932648
-5 0 30 105 252 507 930 1643 2900 5202 9490 17509 32578 61290 117195 228414 452557 904480 1805570 3567701 6931124
9 14 35 86 196 416 827 1563 2880 5334 10188 20261 41566 86247 177473 356985 695751 1307394 2362317 4097188 6808892
20 42 79 134 210 310 437 594 784 1010 1275 1582 1934 2334 2785 3290 3852 4474 5159 5910 6730
18 36 67 112 184 327 642 1320 2682 5226 9681 17068 28768 46597 72888 110580 163314 235536 332607 460920 628024
1 16 54 127 246 414 616 806 891 712 22 -1539 -4472 -9450 -17352 -29300 -46699 -71280 -105146 -150821 -211302
12 19 18 9 11 86 368 1097 2671 5759 11578 22558 43872 86831 176168 365099 765198 1603104 3323596 6769750 13488005
13 25 47 82 144 270 532 1049 1999 3631 6277 10364 16426 25116 37218 53659 75521 104053 140683 187030 244916
18 44 82 141 251 474 923 1814 3590 7166 14354 28547 55782 106376 197468 357111 631345 1097711 1893752 3281337 5796298
-3 -5 -7 2 47 165 394 747 1161 1417 1059 -573 -3879 -7342 -2954 35062 176409 593127 1686497 4356260 10558447
9 18 38 77 151 288 532 947 1621 2670 4242 6521 9731 14140 20064 27871 37985 50890 67134 87333 112175
11 25 38 62 123 264 553 1108 2159 4181 8161 16115 32062 63820 126273 247277 478311 913625 1724420 3219124 5947937
7 10 28 80 197 425 826 1488 2569 4430 7980 15498 32465 71399 159412 352272 759211 1584594 3194820 6221348 11713301
4 -5 -19 -38 -62 -91 -125 -164 -208 -257 -311 -370 -434 -503 -577 -656 -740 -829 -923 -1022 -1126
-4 4 31 94 230 510 1063 2118 4078 7653 14099 25637 46160 82377 145591 254363 438376 743882 1241191 2034744 3276402
2 8 17 25 34 63 164 445 1105 2500 5292 10793 21711 43643 87849 176089 348620 676840 1282539 2366281 4248104
10 24 35 51 93 193 396 780 1514 2980 5991 12143 24345 47577 89932 164004 288690 491480 811315 1302099 2036957
1 18 49 95 156 231 318 414 515 616 711 793 854 885 876 816 693 494 205 -189 -704
0 10 37 83 148 241 415 848 2018 5075 12624 30344 70244 156988 339726 713399 1455732 2889320 5582623 10509641 19295916
1 17 40 70 112 175 263 355 378 202 -248 -517 1774 14377 58060 182207 494627 1215467 2770252 5944056 12128040
22 46 83 133 196 272 361 463 578 706 847 1001 1168 1348 1541 1747 1966 2198 2443 2701 2972
13 30 53 75 85 82 112 335 1124 3190 7729 16621 32805 61139 110361 197224 354507 645418 1187905 2193563 4027137
22 38 65 111 184 292 443 645 906 1234 1637 2123 2700 3376 4159 5057 6078 7230 8521 9959 11552
-7 -3 12 48 137 352 825 1759 3441 6286 10983 18885 32900 59312 111199 214421 417517 807255 1531986 2835306 5102751
6 19 48 101 195 380 773 1599 3249 6389 12189 22787 42160 77642 142408 259333 466736 826631 1436230 2443577 4068337
6 19 38 70 138 290 616 1278 2566 5025 9762 19156 38404 78737 163900 342877 714254 1471611 2985678 5948678 11620590
6 9 15 18 17 18 30 56 95 208 769 3130 11086 33741 90658 220534 495084 1040355 2068331 3922442 7141463
20 39 62 81 88 75 34 -35 -91 40 884 3815 12173 33765 86307 208785 484198 1083698 2351220 4967152 10272446
7 9 14 13 -9 -62 -130 -143 63 830 2907 8080 20783 51916 127332 305732 714777 1621365 3564450 7600425 15748881
26 35 41 44 44 41 35 26 14 -1 -19 -40 -64 -91 -121 -154 -190 -229 -271 -316 -364
22 40 75 133 217 327 455 570 588 322 -593 -2805 -7385 -16007 -31173 -56488 -96990 -159540 -253277 -390143 -585483
15 16 22 46 115 274 583 1100 1846 2755 3628 4144 4047 3750 5813 18109 60021 173670 442730 1021246 2172799
-3 1 10 18 22 27 50 123 295 633 1222 2164 3576 5587 8334 11957 16593 22369 29394 37750 47482
12 21 26 27 24 30 103 400 1264 3387 8173 18602 41262 90947 200630 442261 968683 2095790 4460305 9319056 19114059
6 20 33 42 56 107 261 629 1378 2742 5033 8652 14100 21989 33053 48159 68318 94696 128625 171614 225360
13 27 63 126 228 403 740 1460 3078 6709 14598 30978 63387 124605 235405 428348 752891 1282119 2121457 3419766 5383278
23 38 61 113 233 494 1046 2200 4565 9245 18102 34111 61903 108755 186601 316182 535323 914640 1585883 2790781 4961869
10 10 8 9 23 65 155 318 584 988 1570 2375 3453 4859 6653 8900 11670 15038 19084 23893 29555
24 44 69 109 194 389 823 1740 3580 7098 13529 24807 43846 74891 123947 199294 312096 477112 713517 1045841 1505034
-6 -9 -12 -15 -18 -21 -24 -27 -30 -33 -36 -39 -42 -45 -48 -51 -54 -57 -60 -63 -66
14 23 27 35 68 159 353 707 1290 2183 3479 5283 7712 10895 14973 20099 26438 34167 43475 54563 67644
7 29 79 166 310 557 1002 1833 3421 6497 12474 23996 45851 86522 160956 295738 538951 978833 1778229 3236182 5894304
17 36 74 133 209 291 371 488 845 2069 5756 15595 39653 94909 215969 471255 992125 2023845 4013000 7755418 14644761
12 15 15 11 10 46 223 792 2282 5740 13222 28869 61286 128655 269281 562489 1168671 2404083 4877858 9739127 19116561
7 23 47 83 135 207 303 427 583 775 1007 1283 1607 1983 2415 2907 3463 4087 4783 5555 6407
6 30 63 111 201 393 794 1572 2962 5248 8696 13404 19027 24329 26511 20265 -3490 -59222 -168763 -363635 -687675
15 13 15 38 108 260 538 995 1693 2703 4105 5988 8450 11598 15548 20425 26363 33505 42003 52018 63720"""

def debugprint(*args):
    if debug == True:
        print(*args)

def calculate_difference_array(values):
    return [values[i] - values[i - 1] for i in range(1, len(values))]

def extrapolate_next_sensor_value(sensor_values, depth=0):
    # if all sensor values are the same, extrapolate the next value as the same
    if len(set(sensor_values)) == 1:
        return sensor_values[0]
    difference_array = calculate_difference_array(sensor_values)
    value = sensor_values[-1] + extrapolate_next_sensor_value(difference_array, depth+1)
    return value

def parse_line(line):
    return [int(x.strip()) for x in line.split(" ") if x != ""]

def parse_input(input):
    total = 0
    for line in input.splitlines():
        sensor_values = parse_line(line)
        next_sensor_value = extrapolate_next_sensor_value(sensor_values)
        debugprint(f"if sensor values are {sensor_values}, next_sensor_value: {next_sensor_value}")
        total += next_sensor_value
    return total

print(parse_input(input))
